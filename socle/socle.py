#!/usr/bin/env python3
"""
SOCLE — collecte à provenance prouvée.
Fondation des quatre outils : veille, publication sociale, avis, blog.

Usage :
    python3 socle.py init                    # crée la base depuis schema.sql
    python3 socle.py sources sources.json    # charge et qualifie les sources
    python3 socle.py collecte [--max N]      # collecte, extrait, indexe, hache
    python3 socle.py assertions              # fabrique les assertions depuis les extractions
    python3 socle.py rapport [--jours 7]     # rapport de veille hebdomadaire
    python3 socle.py etalons                 # les étalons de provenance, chiffrés

Aucun secret n'est lu ni écrit par ce programme.
"""
import argparse, asyncio, gzip, hashlib, http.client, json, os, re, sqlite3, sys, time
import urllib.parse as up
import urllib.robotparser

VERSION = "socle 1.0"
AGENT = "socle-gp/1.0 (veille a provenance prouvee; contact: a-renseigner)"
RACINE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.join(RACINE, "socle.db")
ARCHIVES = os.path.join(RACINE, "archives")

RE_LIEN = re.compile(r'href=["\'](https?://[^"\'#]+|/[^"\'#]*)["\']', re.I)


def maintenant():
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def cx():
    c = sqlite3.connect(BASE)
    c.execute("PRAGMA foreign_keys = ON")
    return c


# ---------------------------------------------------------------- init
def cmd_init(_):
    os.makedirs(ARCHIVES, exist_ok=True)
    c = cx()
    c.executescript(open(os.path.join(RACINE, "schema.sql"), encoding="utf-8").read())
    c.execute("INSERT OR IGNORE INTO client(id,nom,ts_cree_utc) VALUES(1,'client-zero',?)", (maintenant(),))
    c.commit()
    n = c.execute("SELECT count(*) FROM sqlite_master WHERE type IN ('table','view','trigger')").fetchone()[0]
    print(f"base creee : {BASE}")
    print(f"objets de schema : {n}")
    print(f"archives : {ARCHIVES}/")


# ------------------------------------------------------------- sources
def cmd_sources(a):
    c = cx()
    conf = json.load(open(a.fichier, encoding="utf-8"))
    for s in conf["sources"]:
        c.execute("""INSERT INTO source(nom,url_base,guichet,licence_spdx,licence_nom,licence_url,
                     licence_lue_le,attribution_texte,cgu_url,cgu_lues_le,debit_max_rps,
                     verdict,motif_verdict,ts_cree_utc)
                     VALUES(:nom,:url_base,:guichet,:licence_spdx,:licence_nom,:licence_url,
                     :licence_lue_le,:attribution_texte,:cgu_url,:cgu_lues_le,:debit_max_rps,
                     :verdict,:motif_verdict,:ts)
                     ON CONFLICT(url_base) DO UPDATE SET
                       guichet=excluded.guichet, licence_spdx=excluded.licence_spdx,
                       licence_lue_le=excluded.licence_lue_le, verdict=excluded.verdict,
                       motif_verdict=excluded.motif_verdict, ts_modifie_utc=excluded.ts_cree_utc""",
                  {**s, "ts": maintenant()})
    c.commit()
    print(f"{'id':>3} {'guichet':<8} {'licence':<16} {'verdict':<22} nom")
    for r in c.execute("SELECT id,guichet,coalesce(licence_spdx,licence_nom,'?'),verdict,nom FROM v_sources_actives"):
        print(f"{r[0]:>3} {r[1]:<8} {r[2]:<16} {r[3]:<22} {r[4]}")
    ec = c.execute("SELECT count(*) FROM source WHERE verdict='ecarte'").fetchone()[0]
    print(f"\nsources retenues : {c.execute('SELECT count(*) FROM v_sources_actives').fetchone()[0]}  ecartees : {ec}")


# ------------------------------------------------------------ collecte
class Collecteur:
    def __init__(self, conn, source, limite):
        self.c, self.s, self.limite = conn, source, limite
        self.hote = up.urlparse(source["url_base"]).netloc
        self.delai = 1.0 / max(source["debit_max_rps"], 0.01)
        self.rp = urllib.robotparser.RobotFileParser()
        self.vus, self.n = set(), 0

    def robots(self):
        try:
            self.rp.set_url(up.urljoin(self.s["url_base"], "/robots.txt"))
            self.rp.read()
            self.c.execute("UPDATE source SET robots_lu_le=? WHERE id=?", (maintenant(), self.s["id"]))
            return True
        except Exception as e:
            print(f"  robots.txt illisible ({e}) — collecte refusee par prudence")
            return False

    def http(self, url):
        u = up.urlparse(url)
        Conn = http.client.HTTPSConnection if u.scheme == "https" else http.client.HTTPConnection
        cn = Conn(u.netloc, timeout=20)
        cn.request("GET", u.path or "/", headers={"User-Agent": AGENT, "Accept-Encoding": "identity"})
        r = cn.getresponse()
        corps = r.read()
        info = (r.status, dict(r.getheaders()), corps)
        cn.close()
        return info

    def archive(self, sha, corps):
        d = os.path.join(ARCHIVES, sha[:2])
        os.makedirs(d, exist_ok=True)
        p = os.path.join(d, sha + ".gz")
        if not os.path.exists(p):
            with gzip.open(p, "wb") as f:
                f.write(corps)
        return os.path.relpath(p, RACINE)

    def capture(self, url):
        if not self.rp.can_fetch(AGENT, url):
            return None
        st, hd, corps = self.http(url)
        sha = hashlib.sha256(corps).hexdigest()
        chemin = self.archive(sha, corps)
        ct = hd.get("Content-Type", "")
        enc = "utf-8"
        m = re.search(r"charset=([\w-]+)", ct, re.I)
        if m:
            enc = m.group(1)
        try:
            cur = self.c.execute(
                """INSERT INTO capture(source_id,url_demandee,url_finale,ts_capture_utc,http_statut,
                   http_etag,http_last_modified,type_mime,encodage,octets,sha256_corps,
                   chemin_archive,agent_utilisateur,version_collecteur)
                   VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                (self.s["id"], url, url, maintenant(), st, hd.get("ETag"), hd.get("Last-Modified"),
                 ct.split(";")[0], enc, len(corps), sha, chemin, AGENT, VERSION))
            cid = cur.lastrowid
        except sqlite3.IntegrityError:
            return ("deja", corps, enc, None)
        return ("neuf", corps, enc, cid)

    def extraire(self, cid, corps, enc):
        import trafilatura
        from py3langid.langid import rank
        html = corps.decode(enc, "replace")
        params = {"include_comments": False, "favor_recall": False}
        txt = trafilatura.extract(html, **params) or ""
        meta = trafilatura.extract_metadata(html)
        titre = (meta.title if meta else None) or ""
        auteur = (meta.author if meta else None) or None
        datepub = (meta.date if meta else None) or None
        # LANGUE : sur le texte ACCENTUE, jamais apres normalisation.
        lg, marge = None, None
        if len(txt) > 20:
            r = rank(txt)[:2]
            lg = r[0][0]
            marge = round(r[0][1] - r[1][1], 2) if len(r) > 1 else None
        self.c.execute(
            """INSERT OR IGNORE INTO extraction(capture_id,outil,version_outil,parametres_json,
               ts_extraction_utc,titre,auteur,date_publication,texte,sha256_texte,
               langue_code,langue_marge,langue_detecteur,langue_avant_normalisation)
               VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,1)""",
            (cid, "trafilatura", trafilatura.__version__, json.dumps(params, sort_keys=True),
             maintenant(), titre, auteur, datepub, txt,
             hashlib.sha256(txt.encode()).hexdigest(), lg, marge, "py3langid 0.4.0"))
        eid = self.c.execute("SELECT id FROM extraction WHERE capture_id=? ORDER BY id DESC LIMIT 1",
                             (cid,)).fetchone()
        if eid and txt:
            url = self.c.execute("SELECT url_finale FROM capture WHERE id=?", (cid,)).fetchone()[0]
            self.c.execute("INSERT INTO texte_idx(titre,corps,extraction_id,url,langue) VALUES(?,?,?,?,?)",
                           (titre, txt, eid[0], url, lg or ""))
        return txt

    def liens(self, corps, url):
        out = []
        for m in RE_LIEN.findall(corps.decode("utf-8", "replace")):
            u = up.urljoin(url, m)
            if up.urlparse(u).netloc == self.hote and u not in self.vus:
                out.append(u)
        return out

    def run(self):
        if not self.robots():
            return 0
        file = [self.s["url_base"]]
        self.vus.add(self.s["url_base"])
        while file and self.n < self.limite:
            url = file.pop(0)
            try:
                res = self.capture(url)
                if res is None:
                    continue
                etat, corps, enc, cid = res
                if etat == "neuf":
                    self.extraire(cid, corps, enc)
                    self.n += 1
                for u in self.liens(corps, url)[:30]:
                    self.vus.add(u)
                    file.append(u)
                time.sleep(self.delai)
            except Exception as e:
                print(f"  echec {url} : {type(e).__name__}: {str(e)[:70]}")
        self.c.commit()
        return self.n


def cmd_collecte(a):
    c = cx()
    tot, t0 = 0, time.time()
    for s in c.execute("""SELECT id,nom,url_base,debit_max_rps FROM source
                          WHERE actif=1 AND verdict<>'ecarte'""").fetchall():
        src = {"id": s[0], "nom": s[1], "url_base": s[2], "debit_max_rps": s[3]}
        print(f"source {s[0]} — {s[1]}")
        n = Collecteur(c, src, a.max).run()
        print(f"  {n} capture(s) neuve(s)")
        tot += n
    dt = time.time() - t0
    print(f"\n{tot} capture(s) en {dt:.1f}s" + (f"  ({tot/dt:.1f} doc/s)" if dt > 0 else ""))


# ---------------------------------------------------------- assertions
def cmd_assertions(a):
    """Une assertion par phrase porteuse, citation verbatim et offsets conservés.
    Pas d'IA ici : genere_par_ia reste à 0 et la chaîne est factuelle."""
    c = cx()
    n = 0
    # Seules les captures en 200 nourrissent des assertions. Une page d'erreur
    # est un fait de provenance valide, ce n'est pas une source d'affirmation.
    for eid, txt in c.execute("""SELECT e.id, e.texte FROM extraction e
                                 JOIN capture c ON c.id = e.capture_id
                                 WHERE e.texte <> '' AND c.http_statut = 200
                                   AND e.id NOT IN
                                 (SELECT DISTINCT extraction_id FROM assertion)""").fetchall():
        pos = 0
        for ph in re.split(r"(?<=[.!?])\s+", txt):
            d = txt.find(ph, pos)
            if d < 0:
                continue
            pos = d + len(ph)
            if len(ph) < 60 or len(ph) > 400:
                continue
            c.execute("""INSERT INTO assertion(extraction_id,client_id,texte,citation_exacte,
                         offset_debut,offset_fin,ts_assertion_utc,genere_par_ia,mention_ia_affichee)
                         VALUES(?,1,?,?,?,?,?,0,0)""",
                      (eid, ph.strip(), ph, d, d + len(ph), maintenant()))
            n += 1
            if n % 3 == 0:
                break
    c.commit()
    print(f"{n} assertion(s) creee(s)")


# ------------------------------------------------------------- étalons
def cmd_etalons(_):
    c = cx()
    r = c.execute("SELECT * FROM v_etalon_provenance").fetchone()
    tot = r[0] or 1
    print("=== Etalons de provenance (section 6 du prompt de lancement) ===")
    print(f"  assertions                                   : {r[0]}")
    print(f"  remontees a une source primaire              : {r[1]}/{r[0]} = {100*r[1]/tot:.1f} %")
    print(f"  datees                                       : {r[2]}/{r[0]} = {100*r[2]/tot:.1f} %")
    print(f"  rejouables a l'identique (sha256 + archive)  : {r[3]}/{r[0]} = {100*r[3]/tot:.1f} %")
    print("\n=== Etat du socle ===")
    for t in ("source", "capture", "extraction", "assertion", "avis", "publication", "article"):
        print(f"  {t:<12} : {c.execute(f'SELECT count(*) FROM {t}').fetchone()[0]}")
    print("\n=== Langues detectees (sur texte accentue, jamais normalise) ===")
    for lg, n, m in c.execute("""SELECT langue_code, count(*), round(avg(langue_marge),1)
                                 FROM extraction WHERE langue_code IS NOT NULL
                                 GROUP BY 1 ORDER BY 2 DESC"""):
        print(f"  {lg or '?':<5} : {n:>5} document(s)   marge moyenne au 2e candidat {m}")
    o = c.execute("SELECT count(*), sum(octets) FROM capture").fetchone()
    print(f"\n  archives conservees : {o[0]} fichier(s), {(o[1] or 0)/1e6:.2f} Mo d'original")


# ------------------------------------------------------------- rapport
def cmd_rapport(a):
    c = cx()
    seuil = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(time.time() - a.jours * 86400))
    lignes = c.execute("""
        SELECT a.id, a.texte, c.url_finale, c.ts_capture_utc, c.sha256_corps,
               s.nom, s.guichet, coalesce(s.licence_spdx,s.licence_nom,'?'),
               s.attribution_texte, e.langue_code, e.titre, e.date_publication
        FROM assertion a
        JOIN extraction e ON e.id = a.extraction_id
        JOIN capture    c ON c.id = e.capture_id
        JOIN source     s ON s.id = c.source_id
        WHERE c.ts_capture_utc >= ?
        ORDER BY s.nom, c.ts_capture_utc DESC, a.id""", (seuil,)).fetchall()
    semaine = time.strftime("%Y-S%V", time.gmtime())
    out = []
    out.append(f"# Rapport de veille — semaine {semaine}")
    out.append("")
    out.append(f"Client : client-zero · Fuseau : America/Guadeloupe (UTC-4, sans heure d'été)")
    out.append(f"Période : {a.jours} derniers jours · Édité le {maintenant()}")
    out.append(f"Produit par : {VERSION}")
    out.append("")
    out.append("**Comment lire ce rapport.** Chaque assertion porte son URL, la date et l'heure UTC "
               "de sa captation, et les 16 premiers caractères de l'empreinte SHA-256 de la page "
               "telle qu'elle est arrivée. L'original est conservé. N'importe quelle ligne se "
               "rejoue : `python3 verifier.py <id>`.")
    out.append("")
    out.append("**Aucune ligne de ce rapport n'est générée par un modèle de langage.** "
               "Les assertions sont des extraits verbatim de sources en accès ouvert déclaré.")
    out.append("")
    cour = None
    for (aid, txt, url, ts, sha, snom, guichet, lic, attrib, lg, titre, datepub) in lignes:
        if snom != cour:
            cour = snom
            out.append("")
            out.append(f"## {snom}")
            out.append(f"*Guichet {guichet} · Licence {lic}*" + (f" · {attrib}" if attrib else ""))
            out.append("")
        out.append(f"- **[{aid}]** {txt}")
        out.append(f"  <br>— {titre or '(sans titre)'} · langue `{lg or '?'}`"
                   + (f" · publié {datepub}" if datepub else ""))
        out.append(f"  <br>— source : {url}")
        out.append(f"  <br>— captée {ts} · empreinte `{sha[:16]}…` · rejouable")
    r = c.execute("SELECT * FROM v_etalon_provenance").fetchone()
    tot = r[0] or 1
    out.append("")
    out.append("---")
    out.append("")
    out.append("## Contrôle de provenance de ce rapport")
    out.append("")
    out.append("| Étalon | Valeur |")
    out.append("|---|---|")
    out.append(f"| Assertions dans la base | {r[0]} |")
    out.append(f"| Part remontée à une source primaire | {100*r[1]/tot:.1f} % |")
    out.append(f"| Part datée | {100*r[2]/tot:.1f} % |")
    out.append(f"| Part rejouable à l'identique | {100*r[3]/tot:.1f} % |")
    out.append(f"| Assertions générées par IA | {c.execute('SELECT count(*) FROM assertion WHERE genere_par_ia=1').fetchone()[0]} |")
    out.append("")
    out.append("## Sources mobilisées et leurs licences")
    out.append("")
    out.append("| Source | Guichet | Licence | Licence lue le | Attribution |")
    out.append("|---|---|---|---|---|")
    for s in c.execute("""SELECT nom,guichet,coalesce(licence_spdx,licence_nom,'?'),
                          coalesce(licence_lue_le,'non lue'),coalesce(attribution_texte,'')
                          FROM v_sources_actives ORDER BY nom"""):
        out.append(f"| {s[0]} | {s[1]} | {s[2]} | {s[3]} | {s[4]} |")
    txt = "\n".join(out) + "\n"
    chemin = os.path.join(RACINE, f"rapport-{semaine}.md")
    open(chemin, "w", encoding="utf-8").write(txt)
    print(f"rapport ecrit : {chemin}  ({len(lignes)} assertion(s), {len(txt)} octets)")
    return chemin


def main():
    p = argparse.ArgumentParser(prog="socle")
    sp = p.add_subparsers(dest="cmd", required=True)
    sp.add_parser("init").set_defaults(f=cmd_init)
    q = sp.add_parser("sources"); q.add_argument("fichier"); q.set_defaults(f=cmd_sources)
    q = sp.add_parser("collecte"); q.add_argument("--max", type=int, default=50); q.set_defaults(f=cmd_collecte)
    sp.add_parser("assertions").set_defaults(f=cmd_assertions)
    sp.add_parser("etalons").set_defaults(f=cmd_etalons)
    q = sp.add_parser("rapport"); q.add_argument("--jours", type=int, default=7); q.set_defaults(f=cmd_rapport)
    a = p.parse_args()
    a.f(a)


if __name__ == "__main__":
    main()
