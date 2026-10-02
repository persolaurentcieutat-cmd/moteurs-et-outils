#!/usr/bin/env python3
"""
PUBLIER — orchestrateur de publication minimal, trois plateformes.

Écrit pour chiffrer une question : que coûte le minimum nécessaire pour
deux ou trois plateformes, plutôt que de reprendre un orchestrateur de
trente plateformes sous copyleft réseau ?

    python3 publier.py file                    # ce qui attend dans la file
    python3 publier.py ajouter --plateforme mastodon --texte "..." [--ia]
    python3 publier.py relire <id> --relecteur "Nom" [--rejeter]
    python3 publier.py programmer <id> --local "2026-10-05 08:30"
    python3 publier.py envoyer                 # envoie ce qui est dû
    python3 publier.py bilan

Ce qu'il tient, et qui n'est pas négociable :
  — aucun secret dans la base : on lit une RÉFÉRENCE de coffre, et le coffre
    est un service loué. Voir coffre_lire().
  — rien de généré par IA ne part sans relecture humaine nommée : le
    déclencheur publication_ia_relue du schéma le refuse au niveau SQL.
  — l'heure est stockée en UTC et rendue en heure de Guadeloupe (UTC-4,
    sans heure d'été). Un champ local sans fuseau déclaré est un bogue
    de saison.
  — chaque publication porte les assertions qui la fondent, donc sa
    provenance remonte jusqu'à la capture et son empreinte.
  — tout appel aux accès confiés est journalisé dans journal_acces.
"""
import argparse, hashlib, json, os, sqlite3, time, urllib.parse as up
import http.client
import datetime as dt

RACINE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.join(RACINE, "socle.db")
VERSION = "publier 1.0"
FUSEAU_GP = dt.timezone(dt.timedelta(hours=-4), "America/Guadeloupe")

# Point d'entrée des plateformes. En production : les vraies URL.
# Ici : un bouchon local, pour que le banc tourne sans accès réseau sortant.
POINTS = {
    "mastodon": os.environ.get("POINT_MASTODON", "http://127.0.0.1:8899/mastodon/statuses"),
    "facebook": os.environ.get("POINT_FACEBOOK", "http://127.0.0.1:8899/facebook/feed"),
    "linkedin": os.environ.get("POINT_LINKEDIN", "http://127.0.0.1:8899/linkedin/ugcPosts"),
}
# Limite de caractères par plateforme : la seule vraie spécificité métier.
LIMITES = {"mastodon": 500, "facebook": 63206, "linkedin": 3000}


def maintenant():
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def cx():
    c = sqlite3.connect(BASE)
    c.execute("PRAGMA foreign_keys = ON")
    return c


# ------------------------------------------------------------------ coffre
def coffre_lire(c, acces_id, acteur, action):
    """Lit un secret par sa RÉFÉRENCE, dans le coffre loué, et journalise.
    Le secret ne transite jamais par la base du socle et n'est jamais
    journalisé. Ce que le journal garde : qui, quand, pour quoi, avec
    quel résultat."""
    r = c.execute("""SELECT reference_coffre, ts_revoque_utc, portee
                     FROM acces_confie WHERE id=?""", (acces_id,)).fetchone()
    if not r:
        raise RuntimeError("acces inconnu")
    ref, revoque, portee = r
    if revoque:
        c.execute("""INSERT INTO journal_acces(acces_id,ts_utc,acteur,action,resultat,detail)
                     VALUES(?,?,?,?,?,?)""",
                  (acces_id, maintenant(), acteur, action, "refuse",
                   f"mandat revoque le {revoque}"))
        c.commit()
        raise PermissionError(f"mandat revoque le {revoque}")
    # En production : appel au coffre loué (OpenBao, coffre infonuagique géré).
    # Le socle ne détient RIEN. Ici le bouchon renvoie un jeton factice.
    secret = os.environ.get("COFFRE_BOUCHON", "jeton-de-banc-non-valide")
    c.execute("""INSERT INTO journal_acces(acces_id,ts_utc,acteur,action,resultat,detail)
                 VALUES(?,?,?,?,?,?)""",
              (acces_id, maintenant(), acteur, action, "accorde",
               f"reference={ref} portee={portee}"))
    c.commit()
    return secret


# ----------------------------------------------------------------- actions
def cmd_ajouter(a):
    c = cx()
    if a.plateforme not in POINTS:
        raise SystemExit(f"plateforme inconnue : {a.plateforme}")
    lim = LIMITES[a.plateforme]
    if len(a.texte) > lim:
        raise SystemExit(f"texte de {len(a.texte)} car. > limite {lim} de {a.plateforme}")
    assertions = [int(x) for x in a.assertions.split(",")] if a.assertions else []
    # contrôle de provenance : toute assertion citée doit exister et être rejouable
    for aid in assertions:
        if not c.execute("SELECT 1 FROM assertion WHERE id=?", (aid,)).fetchone():
            raise SystemExit(f"assertion {aid} inconnue : publication refusee")
    acc = c.execute("SELECT id FROM acces_confie WHERE plateforme=? AND ts_revoque_utc IS NULL",
                    (a.plateforme,)).fetchone()
    cur = c.execute("""INSERT INTO publication(client_id,acces_id,plateforme,contenu,
                       sha256_contenu,assertions_json,genere_par_ia,mention_ia_affichee,
                       statut,fuseau)
                       VALUES(1,?,?,?,?,?,?,?,?,'America/Guadeloupe')""",
                    (acc[0] if acc else None, a.plateforme, a.texte,
                     hashlib.sha256(a.texte.encode()).hexdigest(),
                     json.dumps(assertions), 1 if a.ia else 0, 1 if a.ia else 0,
                     "a_relire" if a.ia else "brouillon"))
    c.commit()
    print(f"publication {cur.lastrowid} creee sur {a.plateforme} "
          f"({len(a.texte)}/{lim} car.) statut="
          f"{'a_relire (generee par IA)' if a.ia else 'brouillon'}"
          f" assertions={assertions}")


def cmd_relire(a):
    c = cx()
    v = "rejete" if a.rejeter else "accepte"
    c.execute("""UPDATE publication SET relu_par_humain=?, relecteur=?, ts_relecture_utc=?,
                 statut=? WHERE id=?""",
              (0 if a.rejeter else 1, a.relecteur, maintenant(),
               "annule" if a.rejeter else "brouillon", a.id))
    c.commit()
    print(f"publication {a.id} relue par {a.relecteur} : {v}")


def cmd_programmer(a):
    c = cx()
    naif = dt.datetime.strptime(a.local, "%Y-%m-%d %H:%M").replace(tzinfo=FUSEAU_GP)
    utc = naif.astimezone(dt.timezone.utc)
    try:
        c.execute("""UPDATE publication SET ts_programme_local=?, ts_programme_utc=?,
                     statut='programme' WHERE id=?""",
                  (naif.strftime("%Y-%m-%dT%H:%M:%S%z"),
                   utc.strftime("%Y-%m-%dT%H:%M:%SZ"), a.id))
        c.commit()
    except sqlite3.IntegrityError as e:
        raise SystemExit(f"REFUSE par le schema : {e}")
    print(f"publication {a.id} programmee  local {naif:%Y-%m-%d %H:%M} (UTC-4)"
          f"  =  UTC {utc:%Y-%m-%dT%H:%MZ}")


def envoyer_un(c, pid, plateforme, contenu, acces_id):
    jeton = coffre_lire(c, acces_id, VERSION, "publication") if acces_id else "sans-acces"
    u = up.urlparse(POINTS[plateforme])
    cn = http.client.HTTPConnection(u.netloc, timeout=15)
    corps = json.dumps({"status": contenu}).encode()
    cn.request("POST", u.path, body=corps,
               headers={"Content-Type": "application/json",
                        "Authorization": f"Bearer {jeton}",
                        "User-Agent": VERSION})
    r = cn.getresponse()
    rep = r.read().decode("utf-8", "replace")
    st = r.status
    cn.close()
    return st, rep


def cmd_envoyer(a):
    c = cx()
    due = c.execute("""SELECT id,plateforme,contenu,acces_id,genere_par_ia,relu_par_humain
                       FROM publication
                       WHERE statut='programme' AND ts_programme_utc <= ?
                       ORDER BY ts_programme_utc""", (maintenant(),)).fetchall()
    print(f"{len(due)} publication(s) due(s)")
    for pid, plat, txt, acc, ia, relu in due:
        try:
            st, rep = envoyer_un(c, pid, plat, txt, acc)
            if 200 <= st < 300:
                ident = (json.loads(rep).get("id") if rep.startswith("{") else None)
                c.execute("""UPDATE publication SET statut='envoye', ts_envoi_utc=?,
                             identifiant_distant=?, nb_tentatives=nb_tentatives+1
                             WHERE id=?""", (maintenant(), ident, pid))
                print(f"  {pid} {plat:<9} ENVOYE   http={st} distant={ident}")
            else:
                c.execute("""UPDATE publication SET statut='echec', code_erreur=?,
                             nb_tentatives=nb_tentatives+1 WHERE id=?""", (str(st), pid))
                print(f"  {pid} {plat:<9} ECHEC    http={st} {rep[:60]}")
        except Exception as e:
            c.execute("""UPDATE publication SET statut='echec', code_erreur=?,
                         nb_tentatives=nb_tentatives+1 WHERE id=?""",
                      (type(e).__name__, pid))
            print(f"  {pid} {plat:<9} ECHEC    {type(e).__name__}: {str(e)[:60]}")
        c.commit()


def cmd_file(a):
    c = cx()
    print(f"{'id':>3} {'plateforme':<10} {'statut':<11} {'IA':<3} {'relu par':<14} "
          f"{'prevu local':<17} car.")
    for r in c.execute("""SELECT id,plateforme,statut,genere_par_ia,coalesce(relecteur,'-'),
                          coalesce(ts_programme_local,'-'),length(contenu)
                          FROM publication ORDER BY id"""):
        print(f"{r[0]:>3} {r[1]:<10} {r[2]:<11} {'oui' if r[3] else 'non':<3} "
              f"{r[4][:14]:<14} {r[5][:16]:<17} {r[6]}")


def cmd_bilan(a):
    c = cx()
    print("=== Etalons de publication (section 6 du prompt de lancement) ===")
    t = c.execute("SELECT count(*) FROM publication WHERE statut IN ('envoye','echec')").fetchone()[0]
    e = c.execute("SELECT count(*) FROM publication WHERE statut='envoye'").fetchone()[0]
    print(f"  taux de publication reussie : {e}/{t} = {100*e/(t or 1):.1f} %")
    print(f"  taux de rejet plateforme    : {(t-e)}/{t} = {100*(t-e)/(t or 1):.1f} %")
    print("\n=== Controle de conformite ===")
    mauvais = c.execute("""SELECT count(*) FROM publication
                           WHERE statut='envoye' AND genere_par_ia=1
                             AND (relu_par_humain=0 OR relecteur IS NULL)""").fetchone()[0]
    print(f"  contenus IA envoyes sans relecture nommee (doit valoir 0) : {mauvais}")
    sansmention = c.execute("""SELECT count(*) FROM publication
                               WHERE statut='envoye' AND genere_par_ia=1
                                 AND mention_ia_affichee=0""").fetchone()[0]
    print(f"  contenus IA envoyes sans mention affichee (doit valoir 0) : {sansmention}")
    print("\n=== Journal des acces confies ===")
    for r in c.execute("""SELECT j.ts_utc,j.acteur,j.action,j.resultat,a.plateforme
                          FROM journal_acces j JOIN acces_confie a ON a.id=j.acces_id
                          ORDER BY j.id"""):
        print(f"  {r[0]}  {r[4]:<9} {r[2]:<12} {r[3]:<9} par {r[1]}")
    print("\n=== Secrets presents dans la base du socle ===")
    print(f"  table acces_confie : {c.execute('SELECT count(*) FROM acces_confie').fetchone()[0]} "
          f"reference(s) de coffre, 0 secret (garanti par les contraintes CHECK du schema)")


def main():
    p = argparse.ArgumentParser(prog="publier")
    sp = p.add_subparsers(dest="cmd", required=True)
    q = sp.add_parser("ajouter")
    q.add_argument("--plateforme", required=True); q.add_argument("--texte", required=True)
    q.add_argument("--assertions", default=""); q.add_argument("--ia", action="store_true")
    q.set_defaults(f=cmd_ajouter)
    q = sp.add_parser("relire"); q.add_argument("id", type=int)
    q.add_argument("--relecteur", required=True); q.add_argument("--rejeter", action="store_true")
    q.set_defaults(f=cmd_relire)
    q = sp.add_parser("programmer"); q.add_argument("id", type=int)
    q.add_argument("--local", required=True); q.set_defaults(f=cmd_programmer)
    sp.add_parser("envoyer").set_defaults(f=cmd_envoyer)
    sp.add_parser("file").set_defaults(f=cmd_file)
    sp.add_parser("bilan").set_defaults(f=cmd_bilan)
    a = p.parse_args(); a.f(a)


if __name__ == "__main__":
    main()
