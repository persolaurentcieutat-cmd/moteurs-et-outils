#!/usr/bin/env python3
"""
Génère le banc de démonstration du socle : un petit portail institutionnel
fictif, multilingue, avec le bruit habituel (bandeau cookies, navigation,
« à lire aussi », pied de page) que l'extracteur doit écarter.

    python3 banc/generer.py            # écrit banc/site/
    python3 -m http.server 8731 --bind 127.0.0.1 --directory banc/site

Les quatre langues des exigences guadeloupéennes sont représentées, créole
guadeloupéen inclus, AVEC LEURS ACCENTS — c'est le point mesuré : dépouiller
les accents fait tomber la reconnaissance du gcf.

Aucun contenu réel n'est repris : tout est écrit pour le banc.
"""
import os, html

RACINE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site")

ARTICLES = [
    ("fr", "2026-09-28", "Marché public de réfection du front de mer attribué",
     "La collectivité a attribué le marché de réfection du front de mer pour un montant de "
     "quatre cent douze mille euros. Les travaux débuteront après la fin de la saison cyclonique, "
     "soit au mois de décembre. Trois entreprises locales avaient répondu à l'appel d'offres, et "
     "le titulaire retenu dispose d'un délai de huit mois pour livrer l'ouvrage."),
    ("fr", "2026-09-29", "Vigilance jaune pour fortes pluies sur l'ensemble de l'archipel",
     "Le service météorologique place l'archipel en vigilance jaune pour fortes pluies et orages "
     "à compter de ce soir dix-huit heures locales. Les cumuls attendus atteignent quatre-vingts "
     "millimètres en douze heures sur les reliefs. Les professionnels du tourisme sont invités à "
     "reporter les sorties en mer prévues demain matin."),
    ("fr", "2026-09-30", "Vingt-deux créations d'entreprises enregistrées la semaine passée",
     "Le bulletin officiel recense vingt-deux immatriculations nouvelles sur la semaine écoulée, "
     "dont neuf dans l'hébergement et la restauration. Deux procédures de liquidation judiciaire "
     "ont également été publiées, toutes deux dans le commerce de détail. Le solde net reste "
     "positif pour le quatrième mois consécutif."),
    ("gcf", "2026-09-27", "Sé moun-la ka palé di maché-la",
     "An ka alé bouk-la chak jou pou vwè ki jan travay-la ka avansé, é sé moun-la té kontan vwè "
     "mwen. Yo ka di maché-la ké bèl lè i ké fini, men yo pa ka kwè sa ké fèt avan lanné "
     "pwochenn. Mèsi anpil pou tout sa zot ka fè pou péyi-la, sé konsa nou ké vansé ansanm."),
    ("gcf", "2026-09-26", "Lapli-la ka tonbé fò asi mòn-la",
     "Dépi yè oswè, lapli-la ka tonbé fò asi tout mòn-la é chimen-la glisé anpil. Sé moun-la ki "
     "ka travay déwò té oblijé rété lakay yo. Nou té ni cho tout lannuit-la é klimatizè-la pa té "
     "ka maché, men sé pa gwo pwoblem, nou ka pran kouraj."),
    ("en", "2026-09-28", "Cruise season opens with three additional port calls",
     "The port authority has confirmed three additional cruise calls for the coming season, "
     "bringing the total to forty-one scheduled arrivals between November and April. Local "
     "operators expect roughly twelve thousand additional day visitors. Shore excursion providers "
     "have been asked to register their capacity before the end of October."),
    ("es", "2026-09-29", "Nueva conexión aérea semanal desde Santo Domingo",
     "La compañía aérea ha anunciado una nueva conexión semanal desde Santo Domingo a partir del "
     "mes de diciembre. El vuelo operará los sábados con una capacidad de ciento ochenta plazas. "
     "Los profesionales del sector esperan un aumento de la clientela hispanohablante durante la "
     "temporada alta."),
    ("fr", "2026-10-01", "Recensement des hébergements touristiques classés",
     "La chambre consulaire a publié le recensement annuel des hébergements classés. "
     "Quatre-vingt-sept établissements sont désormais classés, soit six de plus que l'an dernier. "
     "La majorité reste constituée de très petites structures de moins de dix chambres, ce qui "
     "confirme la physionomie du tissu économique local."),
]

GABARIT = """<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <title>{titre} — Portail du banc</title>
  <meta name="description" content="{titre}">
  <meta property="article:published_time" content="{date}T08:00:00Z">
  <meta name="author" content="Service de l'information">
</head>
<body>
  <div id="bandeau-cookies">Ce site utilise des cookies pour mesurer son audience.
    <button>Tout accepter</button> <button>Refuser</button></div>
  <nav><ul><li><a href="/index.html">Accueil</a></li>
    <li><a href="/rubriques.html">Rubriques</a></li>
    <li><a href="/newsletter.html">Lettre d'information</a></li></ul></nav>
  <header><h1>{titre}</h1>
    <p class="chapo">Publié le {date} par le Service de l'information</p></header>
  <article>
    <p>{corps}</p>
  </article>
  <aside>
    <h2>À lire aussi</h2>
    <ul>{autres}</ul>
    <div class="pub">Encart partenaire — offre de la semaine</div>
  </aside>
  <footer>Mentions légales · Données personnelles · Plan du site ·
    Tous droits réservés</footer>
</body>
</html>
"""


def main():
    os.makedirs(RACINE, exist_ok=True)
    noms = [f"article-{i+1}.html" for i in range(len(ARTICLES))]
    for i, (lang, date, titre, corps) in enumerate(ARTICLES):
        autres = "".join(
            f'<li><a href="/{noms[j]}">{html.escape(ARTICLES[j][2])}</a></li>'
            for j in range(len(ARTICLES)) if j != i)
        open(os.path.join(RACINE, noms[i]), "w", encoding="utf-8").write(
            GABARIT.format(lang=lang, titre=html.escape(titre), date=date,
                           corps=html.escape(corps), autres=autres))
    liens = "".join(f'<li><a href="/{n}">{html.escape(a[2])}</a> '
                    f'<time>{a[1]}</time></li>' for n, a in zip(noms, ARTICLES))
    open(os.path.join(RACINE, "index.html"), "w", encoding="utf-8").write(
        f"""<!doctype html><html lang="fr"><head><meta charset="utf-8">
<title>Portail du banc — dernières publications</title></head><body>
<nav><a href="/index.html">Accueil</a></nav>
<h1>Dernières publications</h1><ul>{liens}</ul>
<p><a href="/flux.xml">Flux de syndication</a></p>
<footer>Mentions légales</footer></body></html>""")
    items = "".join(
        f"<item><title>{html.escape(a[2])}</title>"
        f"<link>http://127.0.0.1:8731/{n}</link>"
        f"<pubDate>{a[1]}</pubDate></item>" for n, a in zip(noms, ARTICLES))
    open(os.path.join(RACINE, "flux.xml"), "w", encoding="utf-8").write(
        f"""<?xml version="1.0" encoding="utf-8"?><rss version="2.0"><channel>
<title>Portail du banc</title><link>http://127.0.0.1:8731/</link>{items}
</channel></rss>""")
    open(os.path.join(RACINE, "robots.txt"), "w", encoding="utf-8").write(
        "User-agent: *\nDisallow: /prive/\nCrawl-delay: 1\n")
    os.makedirs(os.path.join(RACINE, "prive"), exist_ok=True)
    open(os.path.join(RACINE, "prive", "interdit.html"), "w", encoding="utf-8").write(
        "<html><body><p>Cette page est interdite par robots.txt. "
        "Le collecteur ne doit jamais la capter.</p></body></html>")
    open(os.path.join(RACINE, "rubriques.html"), "w", encoding="utf-8").write(
        f"""<!doctype html><html lang="fr"><head><meta charset="utf-8">
<title>Rubriques</title></head><body><h1>Rubriques</h1><ul>{liens}</ul>
<p><a href="/prive/interdit.html">Zone privee</a></p></body></html>""")
    n = len(os.listdir(RACINE))
    print(f"banc ecrit dans {RACINE}/ : {len(ARTICLES)} articles en "
          f"{len(set(a[0] for a in ARTICLES))} langues, 1 flux, 1 robots.txt, "
          f"1 page interdite  ({n} entrees)")
    print("langues :", ", ".join(sorted(set(a[0] for a in ARTICLES))))


if __name__ == "__main__":
    main()
