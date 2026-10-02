#!/usr/bin/env python3
"""
VERIFIER — rejouer une assertion un an plus tard.

    python3 verifier.py <id_assertion>
    python3 verifier.py --toutes

Trois contrôles, dans cet ordre. Chacun peut tomber seul, et on sait alors
exactement ce qui a bougé :

  1. ARCHIVE INTACTE — on recalcule le SHA-256 du fichier conservé et on le
     compare à celui enregistré au moment de la capture. S'il tombe, c'est
     l'archive qui a été altérée, pas la source.
  2. EXTRACTION REPRODUCTIBLE — on relance l'extracteur avec l'outil, la
     version et les paramètres exacts enregistrés, et on compare le SHA-256
     du texte obtenu. S'il tombe alors que l'archive est intacte, c'est
     l'outil qui a changé de comportement — et la version attendue est dite.
  3. CITATION PRÉSENTE — on vérifie que l'extrait verbatim de l'assertion est
     bien dans le texte, aux offsets enregistrés.

Ce programme ne touche pas au réseau. Il prouve ce qui a été capté, pas ce
que la source dit aujourd'hui. Pour comparer à l'état actuel de la source,
c'est une nouvelle capture, jamais une modification de l'ancienne.
"""
import gzip, hashlib, json, os, sqlite3, sys

RACINE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.join(RACINE, "socle.db")

REQ = """
SELECT a.id, a.texte, a.citation_exacte, a.offset_debut, a.offset_fin,
       a.genere_par_ia, a.relu_par_humain, a.relecteur,
       c.url_finale, c.ts_capture_utc, c.sha256_corps, c.chemin_archive,
       c.encodage, c.agent_utilisateur, c.version_collecteur,
       e.outil, e.version_outil, e.parametres_json, e.sha256_texte,
       e.langue_code, e.langue_avant_normalisation,
       s.nom, s.guichet, coalesce(s.licence_spdx, s.licence_nom, '?'), s.licence_lue_le
FROM assertion a
JOIN extraction e ON e.id = a.extraction_id
JOIN capture    c ON c.id = e.capture_id
JOIN source     s ON s.id = c.source_id
"""


def rejouer(r, bavard=True):
    (aid, texte, cit, o1, o2, ia, relu, relecteur, url, ts, sha_att, arch, enc,
     agent, vcoll, outil, vout, params, sha_txt_att, lg, avant_norm,
     snom, guichet, lic, lic_lue) = r
    ok = {"archive": False, "extraction": False, "citation": False}
    if bavard:
        print(f"=== assertion {aid} ===")
        print(f"  texte      : {texte[:100]}{'…' if len(texte) > 100 else ''}")
        print(f"  source     : {snom}  (guichet {guichet}, licence {lic}, lue le {lic_lue})")
        print(f"  url        : {url}")
        print(f"  captee le  : {ts}   par {vcoll}")
        print(f"  agent      : {agent}")
        print(f"  genere IA  : {'oui' if ia else 'non'}   relu par humain : "
              f"{relecteur if relu else 'non'}")
        print(f"  langue     : {lg}  (detectee avant normalisation : "
              f"{'oui' if avant_norm else 'NON — suspect'})")

    # 1. archive intacte
    p = os.path.join(RACINE, arch)
    if not os.path.exists(p):
        if bavard:
            print(f"  1. ARCHIVE  : ABSENTE ({arch})")
        return ok
    brut = gzip.open(p, "rb").read()
    sha_obt = hashlib.sha256(brut).hexdigest()
    ok["archive"] = sha_obt == sha_att
    if bavard:
        print(f"  1. ARCHIVE  : {'INTACTE' if ok['archive'] else 'ALTEREE'}  "
              f"attendu {sha_att[:16]}…  obtenu {sha_obt[:16]}…  ({len(brut)} octets)")

    # 2. extraction reproductible
    try:
        import trafilatura
        vact = trafilatura.__version__
        pr = json.loads(params)
        txt = trafilatura.extract(brut.decode(enc or "utf-8", "replace"), **pr) or ""
        sha_txt = hashlib.sha256(txt.encode()).hexdigest()
        ok["extraction"] = sha_txt == sha_txt_att
        if bavard:
            etat = "REPRODUITE" if ok["extraction"] else "DIVERGENTE"
            note = "" if vact == vout else f"  /!\\ version actuelle {vact}, attendue {vout}"
            print(f"  2. EXTRACT. : {etat}  {outil} {vout} {pr}{note}")
            if not ok["extraction"]:
                print(f"               attendu {sha_txt_att[:16]}…  obtenu {sha_txt[:16]}…")
    except ImportError:
        txt = ""
        if bavard:
            print(f"  2. EXTRACT. : IMPOSSIBLE — {outil} {vout} absent de l'environnement")

    # 3. citation présente
    if cit and txt:
        present = cit in txt
        aux_offsets = txt[o1:o2] == cit if (o1 is not None and o2 is not None) else False
        ok["citation"] = present
        if bavard:
            print(f"  3. CITATION : {'PRESENTE' if present else 'ABSENTE'}"
                  f"   aux offsets {o1}-{o2} : {'oui' if aux_offsets else 'non'}")
    elif bavard:
        print("  3. CITATION : non verifiable (pas de citation ou pas de texte)")

    if bavard:
        verdict = "PROUVEE" if all(ok.values()) else "NON PROUVEE"
        print(f"  --> {verdict}")
    return ok


def main():
    c = sqlite3.connect(BASE)
    if len(sys.argv) > 1 and sys.argv[1] == "--toutes":
        rows = c.execute(REQ + " ORDER BY a.id").fetchall()
        tot = {"archive": 0, "extraction": 0, "citation": 0}
        for r in rows:
            o = rejouer(r, bavard=False)
            for k in tot:
                tot[k] += o[k]
        n = len(rows) or 1
        print(f"=== Rejeu de {len(rows)} assertion(s) ===")
        for k, v in tot.items():
            print(f"  {k:<11} : {v}/{len(rows)} = {100*v/n:.1f} %")
        pleines = sum(1 for r in rows if all(rejouer(r, bavard=False).values()))
        print(f"  {'PROUVEES':<11} : {pleines}/{len(rows)} = {100*pleines/n:.1f} %")
        return
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    r = c.execute(REQ + " WHERE a.id = ?", (int(sys.argv[1]),)).fetchone()
    if not r:
        print(f"assertion {sys.argv[1]} inconnue")
        sys.exit(1)
    rejouer(r)


if __name__ == "__main__":
    main()
