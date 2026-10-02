# Critique adversariale — méthode des six temps, étalons, faisabilité

Cible : `00-PROMPT-DE-LANCEMENT.md` v4 du 2 octobre 2026, sections 5 et 6.
Lecteur : agent adversarial. Mission : casser, pas valider.
Date des mesures : **2 octobre 2026**. Environnement : conteneur Linux 6.18, 4 cœurs, 15 Gio RAM, Python 3.11.15, Node 22.22.0, SQLite 3.45.1, Docker 29.6.2.

---

## 0. Mes lignes en cran D — déclarées avant le contenu

Règle 4.1 du document. Ce qui suit est de la mémoire de modèle, non vérifié dans cette session. **Piste, jamais fondement.**

| # | Ligne en cran D | Pourquoi je n'ai pas pu monter de cran |
|---|---|---|
| D1 | Les coûts de développement logiciel se chiffrent couramment par méthodes paramétriques (COCOMO et dérivés) qui convertissent des lignes de code en mois-homme | Je n'ai pu atteindre aucune source primaire sur ces modèles. Je n'utilise donc **aucun** coefficient de conversion dans ce document, et je ne convertis jamais mes lignes de code en jours |
| D2 | Les plateformes de veille média (Meltwater, Brandwatch, Talkwalker) ne vendent pas d'essai en libre-service | Confirmé seulement par des pages de comparaison, cran C. Les pages des éditeurs eux-mêmes sont inaccessibles depuis ce conteneur |
| D3 | `Ryanair c. PR Aviation` est l'affaire C-30/14 de la CJUE, arrêt du 15 janvier 2015 | `curia.europa.eu` **bloqué par la politique de sortie réseau** de ce conteneur. Le document est déjà en D sur ce point ; je ne l'en sors pas |
| D4 | `NLA c. Meltwater` s'est conclu devant la Cour suprême du Royaume-Uni en 2013 | Aucune source primaire atteignable. Reste en D, comme dans le document |
| D5 | L'ordre de grandeur du parc hôtelier et para-hôtelier guadeloupéen | Je l'ignore. Je ne le chiffre nulle part dans ce document, et aucun de mes raisonnements n'en dépend |
| D6 | Les licences de contenu presse en France passent par le CFC | Non vérifié. Je ne chiffre pas |

**Un aveu de méthode, et il est structurant.** La politique de sortie réseau de ce conteneur refuse `la1ere.francetvinfo.fr`, `rci.fm`, `karibinfo.com`, `franceantilles.fr`, `guadeloupe.cci.fr`, `meteofrance.gp`, `connectivity.booking.com`, `developers.google.com`, `curia.europa.eu`, `brandwatch.com`. Sortie du diagnostic du mandataire :

```
"recentRelayFailures": [
  {"kind":"connect_rejected","detail":"gateway answered 403 to CONNECT (policy denial or upstream failure)",
   "host":"la1ere.francetvinfo.fr:443"},
  {"kind":"connect_rejected","detail":"gateway answered 403 to CONNECT (policy denial or upstream failure)",
   "host":"www.rci.fm:443"},
  ... www.franceantilles.fr:443, www.karibinfo.com:443,
      www.guadeloupe.cci.fr:443, www.meteofrance.gp:443
```

Conséquence : **je n'ai pas pu toucher une seule source guadeloupéenne réelle.** Je ne produis donc aucun chiffre guadeloupéen. Tout ce que je classe A est mesuré sur du code libre et sur des corpus que j'ai construits ou lus localement. C'est une limite de mon banc, pas un argument.

Et c'est déjà un résultat sur le document : **la méthode des six temps, telle qu'écrite, n'est pas exécutable par un agent.** Le temps 1 et le temps 2 exigent d'atteindre des produits propriétaires et des sites locaux. Un agent dans un conteneur d'entreprise ne les atteint pas. Si Laurent délègue les six temps à des agents, il délègue une tâche qu'ils ne peuvent pas faire, et il recevra du C déguisé en A. Le document n'a pas prévu ce cas.

---

## 1. Le coût réel de reconstruction, organe par organe

### 1.1 Ma méthode de chiffrage, et son honnêteté

Je refuse d'inventer des jours-homme. Je mesure un **proxy d'effort investi** sur les projets libres qui font déjà le travail : le *mois-auteur soutenu* = couple distinct (auteur, mois) comptant au moins 5 commits ce mois-là. Le seuil de 5 écarte les contributions de passage. Commande exacte, rejouable :

```bash
git log --all --date=format:'%Y-%m' --format='%ad|%aE' | tr 'A-Z' 'a-z' \
  | sort | uniq -c | awk '$1>=5' | wc -l
```

**Ce que ce proxy n'est pas.** Il ne dit pas combien il faut de jours pour refaire l'organe : un projet de 20 ans porte de la dette, des refontes, du support, des plateformes qu'on n'a pas besoin de viser. Il dit une chose, et elle suffit : **l'ordre de grandeur de l'effort que l'humanité a consacré à chacun de ces organes.** Quand ce chiffre est en dizaines d'années-auteur, « on le refait » demande une justification que le document ne donne pas.

### 1.2 La mesure — A-mesure

Six dépôts clonés et dépouillés le 2 octobre 2026. Sortie brute :

```
nutch            first=2005-01-23 last=2026-10-01 commits=4557  auteurs=119  AM>=5c=306  AY>=5c=25.5
openbao          first=2015-02-24 last=2026-10-02 commits=24207 auteurs=1722 AM>=5c=1173 AY>=5c=97.8
postiz-app       first=2024-01-26 last=2026-10-02 commits=3815  auteurs=87   AM>=5c=89   AY>=5c=7.4
storm-crawler    first=2013-04-12 last=2026-10-02 commits=2786  auteurs=97   AM>=5c=152  AY>=5c=12.7
tantivy          first=2016-01-10 last=2026-10-02 commits=4878  auteurs=238  AM>=5c=232  AY>=5c=19.3
trafilatura      first=2019-04-04 last=2026-10-02 commits=1676  auteurs=84   AM>=5c=66   AY>=5c=5.5
```

Taille du code, mesurée localement sur clone de profondeur 1 (lignes non vides, extensions `.py .java .rs .go .ts .tsx`, hors `node_modules`) :

```
nutch            total=   89099 dont_tests=  18203 net=  70896
openbao          total=  481647 dont_tests= 211362 net= 270285
postiz-app       total=  114131 dont_tests=      0 net= 114131
storm-crawler    total=   62104 dont_tests=  24174 net=  37930
tantivy          total=  158730 dont_tests=      0 net= 158730
trafilatura      total=   18611 dont_tests=  10368 net=   8243
```

*Réserve honnête* : `dont_tests=0` pour tantivy et postiz est un artefact de mon filtre — Rust met ses tests en `#[cfg(test)]` dans le fichier source, et postiz ne suit pas la convention `*.test.ts`. Pour ces deux-là, lire la colonne `total`.

Licences lues directement dans le fichier `LICENSE` de chaque dépôt, cran B :

| Projet | Licence lue | Portée pour un service hébergé commercial |
|---|---|---|
| trafilatura | Apache-2.0 | Sans contrainte |
| Apache Nutch | Apache-2.0 | Sans contrainte |
| StormCrawler | Apache-2.0 | Sans contrainte |
| tantivy | MIT | Sans contrainte |
| OpenBao | Mozilla Public License 2.0 | Copyleft de fichier, compatible service hébergé |
| **Postiz** | **GNU Affero GPL v3** | **Piège. Copyleft réseau : tout utilisateur du service a droit au code source du service** |

### 1.3 Le total, et le verdict sur le pari central

```
    25.5 années-auteur  Nutch (découverte/crawl, échelle web)
    12.7 années-auteur  StormCrawler (crawl)
     5.5 années-auteur  trafilatura (extraction propre multilingue)
    19.3 années-auteur  tantivy (index de recherche)
    97.8 années-auteur  OpenBao / Vault (gestion de secrets)
     7.4 années-auteur  Postiz (publication multi-plateforme)
  ------
   168.2 années-auteur  total
   142.7 années-auteur  en ne gardant qu'un seul crawler
     → 71 ans pour une équipe de 2 personnes à plein temps
```

**« On repère le meilleur modèle existant, on le mesure, on le refait » est faux, mais pas pour la raison attendue.**

Le document se trompe deux fois, en sens opposés, et c'est la vraie découverte :

**Erreur 1 — il surestime ce qu'il faut construire.** Quatre des huit organes de la section 6 ont déjà un équivalent libre bon, sous licence permissive, que j'ai fait tourner. Ils ne sont pas à reconstruire. Le temps 5 ne devrait jamais s'y appliquer. Le document ne le sait pas parce qu'il ne l'a pas mesuré.

**Erreur 2 — il sous-estime, à en être dangereux, deux organes.** La *garde des accès confiés* pèse 97,8 années-auteur et 270 000 lignes nettes. Le document la liste en section 6 comme un organe à reconstruire avec son étalon chiffré (« chiffrement au repos … révocation effective en minutes … cloisonnement entre clients »). **C'est la ligne la plus dangereuse du document.** On ne reconstruit pas un coffre à secrets : on le loue ou on l'installe. Un organe de cryptographie écrit par une très petite équipe sans audit externe est précisément ce qui fera échouer la revue de diligence que la section 2.6 veut passer. Le document veut se distinguer des aspirateurs par le sérieux, et s'apprête à écrire sa propre crypto.

**Organe par organe — ce qui est réellement à faire :**

| Organe (section 6) | Effort déjà investi par le libre | Mesure que j'ai faite | Verdict que le document aurait dû écrire |
|---|---|---|---|
| **Découverte / crawl** | 12,7 à 25,5 années-auteur | **J'ai écrit et fait tourner un crawler de 47 lignes** : 3 000 pages, `robots.txt` respecté, 0 erreur | **Ne pas reconstruire, ne pas adopter Nutch non plus.** À l'échelle guadeloupéenne, 47 lignes suffisent. Nutch achète la distribution à l'échelle web, dont vous n'avez aucun besoin |
| **Extraction propre multilingue** | 5,5 années-auteur | **F1 = 0,916 mesuré** sur le corpus annoté du projet, 35,5 pages/s sur 1 cœur | **Adopter trafilatura, Apache-2.0.** Reconstruire serait détruire de la valeur. Reste à mesurer sur pages locales, ce que je n'ai pas pu faire |
| **Index de recherche** | 19,3 années-auteur (tantivy) | **SQLite FTS5, déjà dans Python** : 200 000 documents indexés en 28,2 s, 622 Mo, p50 = 82,7 ms | **Ne rien installer.** L'organe est dans la bibliothèque standard. Zéro année-auteur à dépenser |
| **Chaîne de provenance** | **inconnu — je n'ai trouvé aucun projet de référence à mesurer** | **Implémentée en ~15 lignes** dans ma chaîne : SHA-256 du brut, horodatage UTC, identité de l'extracteur, 100 % rejouable | **Le seul organe à construire, et il est petit.** Le document a raison de dire « notre couche », il a tort de la croire lourde |
| **Rédaction sourcée** | inconnu, non mesuré | aucune mesure | Je l'ignore. Ne pas chiffrer |
| **Publication multi-plateforme** | 7,4 années-auteur | **Postiz couvre 30+ plateformes** dont `facebook instagram linkedin x tiktok threads gmb wordpress bluesky mastodon` | **Ne pas reconstruire. Mais la licence est AGPL-3.0** : décision à prendre maintenant, pas en V1 |
| **Avis** | non mesurable en libre | voir section 2.3 : plafond de 5 avis sur les interfaces publiques | **Rien à reconstruire : il n'y a pas d'organe technique, il y a un guichet.** Le document confond les deux |
| **Garde des accès confiés** | **97,8 années-auteur, 270 285 lignes nettes** | aucune — et je refuse d'en proposer une | **Interdiction de reconstruire.** Louer, ou ne détenir aucun secret durable |

**La somme « plusieurs années-hommes » demandée dans la consigne : oui, et très au-delà — 142,7 années-auteur mesurées.** Mais le projet n'est pas une illusion pour cette raison. Il est une illusion parce qu'il a répertorié huit organes à reconstruire là où il y en a **un et demi**, et qu'il a mis dans la liste le seul qu'il ne faut jamais toucher.

---

## 2. Ce qui rend la méthode impraticable en l'état

### 2.1 Le temps 2 est impraticable — et il n'est pas seulement difficile, il est circulaire

Le temps 2 exige d'instrumenter le modèle propriétaire « par version d'essai ou compte de démonstration ».

**Obstacle 1 — il n'y a pas d'essai à instrumenter.** Cran C, je ne peux pas monter : les pages des éditeurs sont bloquées depuis ce conteneur. Ce que les comparatifs rapportent : ni Brandwatch, ni Meltwater, ni Talkwalker n'offrent d'essai en libre-service ; l'accès passe par une conversation commerciale. Côté gestion de réputation hôtelière, Revinate et ReviewPro sont sur devis. **À confirmer en cran B, obligatoirement, avant d'engager quoi que ce soit sur le temps 2.**

**Obstacle 2, et il est fatal — une démonstration commerciale n'est pas une mesure.** Le temps 2 veut « les chiffres observés, sortie collée », sur « un jeu d'épreuve réel guadeloupéen ». Une démonstration se déroule sur le jeu de données du vendeur, pilotée par le vendeur, sans export. Même un essai accordé est une horloge de 14 jours. Le rejet prévu au temps 2 — « les chiffres viennent de la documentation du vendeur » — décrit exactement le seul résultat qu'une démonstration peut produire. **Le temps 2 se rejette lui-même.**

**Obstacle 3 — l'ordre des temps est cassé.** Le temps 2 exige un jeu d'épreuve guadeloupéen pour instrumenter le modèle. Le temps 3 est le temps qui *fixe* le jeu d'épreuve. On ne peut donc pas faire le temps 2 avant le temps 3, et le document interdit le temps 3 avant le temps 2. Le paragraphe « Le pivot » tente de sauver la chose en renvoyant la constitution du corpus à V0, mais alors **le temps 3 ne fait plus rien** : il ne reste qu'un acte d'écriture. Les six temps sont en réalité cinq, et l'un des cinq est bloqué.

### 2.2 La doctrine de preuve verrouille la décision de construire — contradiction interne, et elle est totale

Règle 4.2, mot pour mot :

> **Aucune décision de construire ne se prend sur un cran B ou moins. Décider de reconstruire exige un A-mesure sur le modèle repéré.**

Un A-mesure sur le modèle repéré ne s'obtient qu'au temps 2. Le temps 2 est impraticable (2.1). Donc :

**Aucune décision de construire ne peut jamais être prise sous les règles du document.** Le projet est en impasse décisionnelle dès sa page de doctrine. Ce n'est pas une rigueur excessive, c'est un verrou logique : la règle qui devait empêcher de construire à l'aveugle empêche de construire tout court.

### 2.3 Les étalons de la section 6 sont pour partie non mesurables — et pas par manque d'annotation

Point par point.

**« Rappel sur corpus local figé » (Découverte) — le dénominateur n'existe pas.** Le rappel exige de connaître la réponse complète : tout ce qui a été publié en Guadeloupe dans une fenêtre donnée. Personne ne détient ce recensement. Ce n'est pas un problème d'annotation coûteuse, c'est un **dénominateur inconnaissable**. Aucun budget d'annotation ne le résout.
*Le correctif* : abandonner le rappel absolu, mesurer le **rappel relatif en bassin** — on réunit ce que trouvent tous les systèmes comparés, cette union sert de dénominateur, et chaque système est noté sur sa part. C'est la seule grandeur calculable, et elle est opposable pour *comparer*. Elle ne dit rien dans l'absolu, et il faut l'écrire.

**« Fraîcheur en heures entre publication et captation » (Découverte) — incompatible avec le jeu d'épreuve figé.** Un corpus de HTML gelé en V0 n'a plus d'horloge. La fraîcheur ne se mesure que sur du flux vivant. Le document impose un juge figé et une métrique qui exige du vivant, dans la même cellule du tableau. **Il faut deux bancs, pas un** : un banc figé pour l'extraction et la pertinence, un banc vivant daté pour la fraîcheur et le délai de détection. Le document n'en prévoit qu'un.

**« Part de texte propre » et « taux d'erreur par champ » (Extraction) — mesurables, et le travail d'annotation est déjà fait par d'autres.** Voir section 3. C'est le seul étalon de la section 6 que j'ai pu réellement produire.

**« Pertinence sur requêtes figées » (Index) — exige un jugement humain par couple requête-document.** Non annoté, non mesurable. Coût en section 3.

**« Part des assertions remontées à une source primaire … part datée … part rejouable » (Provenance) — mesurable sans aucune annotation humaine.** C'est une propriété du code, pas du monde. Je l'ai mesurée : 100 %, 100 %, 100 %, sur 1 000 documents. **Le document a donc, dans sa liste, un étalon qui est à la fois son avantage distinctif et le seul gratuit à mesurer. Il ne le voit pas.**

**« Taux de reprise par un humain » (Rédaction) — exige de faire travailler un humain sur chaque sortie.** Non automatisable par construction.

**« Part des avis captés sur ceux réellement présents » (Avis) — structurellement non mesurable sur les plateformes majeures.** Cran C, à confirmer en B : l'interface publique de Google plafonne à 5 avis par lieu, sans pagination ; l'interface de contenu de TripAdvisor renvoie 5 avis récents, et l'accès est réservé à des partenaires approuvés. Le dénominateur « ceux réellement présents » n'est accessible qu'au titulaire via le guichet 2, et seulement chez Google. **Donc : sur TripAdvisor, cette métrique ne pourra jamais être calculée autrement qu'en passant par le degré 5c, que la section 2.6 écarte.** L'étalon exige ce que la doctrine interdit. Deuxième contradiction interne.

**« Chiffrement au repos … révocation en minutes … cloisonnement » (Garde des accès confiés) — ce ne sont pas des étalons, ce sont des exigences d'un produit qu'on achète.** Les mesurer suppose qu'on l'écrit. Voir 1.3 : il ne faut pas l'écrire.

### 2.4 Trois incohérences internes qui prouvent que les tableaux n'ont pas été relus ensemble

| Où | Ce qui est écrit | Le fait |
|---|---|---|
| Section 4.4, champ « Organe visé » | « Lequel des **sept** de la section 6 » | La section 6 en liste **huit**. Le gabarit de fiche-organe n'a pas été remis à jour quand la v3 a ajouté la garde des accès confiés. Un agent qui remplit le gabarit n'a pas de case pour le huitième organe |
| Section 2.2, titre | « un péage à **cinq** guichets » | Le tableau juste dessous en a **six**, et la v4 dit elle-même avoir ajouté le sixième. Le titre n'a pas suivi |
| Section 1 « Ce qui est tranché » vs règle 4.2 | « Aucun choix de guichet ne se prend sur un cran D » | Les guichets 1, 3, 4 et les familles du guichet 6 sont tous marqués **⏳ D** dans le document, et pourtant les guichets 2 et 6 sont déjà déclarés « notre voie principale » en section 2. **Le document viole sa propre règle 4.2 dans sa propre section 1** |

La troisième n'est pas cosmétique. Le document se présente comme un appareil de discipline et commence par une décision qu'il s'interdit.

### 2.5 Le risque que le document ne nomme pas : le piège à perfectionnisme

Le document a douze mécanismes de refus — barème à quatre crans, règles de rejet, interdictions explicites, gabarit à douze champs, six temps avec rejet à chaque temps, six vagues chacune en attente de validation, deux relances automatiques, section 9 « ce que ce prompt refuse de produire ». Il a **zéro mécanisme de livraison**. Pas de version minimale utilisable, pas de jalon de revenu, pas de critère d'abandon, pas de date.

Le chemin critique écrit est : V0 (terrain + corpus figé + registre de qualification source par source) → V1 (« vague la plus lourde », juriste obligatoire) → V2 (six temps × 4 organes) → V3 → V4 → V5 (arbitrage). **La première ligne de code destinée à un client n'apparaît nulle part avant V5.** Le document ne dit pas combien de temps cela prend, et moi non plus : **je l'ignore, et je refuse de l'inventer.**

Mais je peux mesurer l'autre branche de l'alternative, et je l'ai fait. **La chaîne complète des quatre organes de collecte — découverte, extraction, provenance, index — tient en 64 lignes de code non vides et traite 1 000 documents en 9,5 secondes avec 100 % de provenance rejouable.** Voilà le coût d'opportunité : pendant que la méthode instruit V0 et V1, la version qui marche est déjà écrite.

Le document a raison sur un point et il faut le dire : un socle illicite ne se vend pas, et une mesure non opposable est une opinion. Le danger n'est pas la rigueur. **Le danger est que la rigueur soit placée avant la première valeur livrée, au lieu d'être placée autour d'elle.** Un barème à quatre crans sur un produit qui n'existe pas protège un actif de valeur nulle.

---

## 3. Le coût du jeu d'épreuve et des annotations

### 3.1 Combien de documents pour qu'une mesure soit statistiquement opposable — A-mesure

Le document exige des mesures opposables et ne dit **jamais** combien il faut d'items. C'est le trou central de la section 5. Je le comble par le calcul, rejouable.

**Intervalle de Wilson à 95 %, pour un rappel observé de 0,85 :**

```
     n  IC95 bas  IC95 haut   largeur
    20     0.640     0.948     30.8 pts
    30     0.684     0.937     25.3 pts
    50     0.726     0.924     19.7 pts
   100     0.767     0.907     14.0 pts
   200     0.794     0.893      9.9 pts
   384     0.811     0.882      7.1 pts
   500     0.816     0.879      6.3 pts
  1000     0.827     0.871      4.4 pts
  2000     0.834     0.865      3.1 pts
```

**Taille nécessaire pour comparer deux systèmes** (l'étalon propriétaire contre l'organe reconstruit — exactement le temps 6), test bilatéral de deux proportions, α = 0,05, puissance 0,80 :

```
  n par bras =    141   détecter 10 pts d'écart (85 % vs 95 %)
  n par bras =    686   détecter  5 pts d'écart (85 % vs 90 %)
  n par bras =   2036   détecter  3 pts d'écart (85 % vs 88 %)
  n par bras =   4724   détecter  2 pts d'écart (85 % vs 87 %)
```

**Ce que ces chiffres font au document.** Le temps 6 admet trois issues : égaler, dépasser, ou chiffrer l'écart. Or :

- Pour affirmer « nous égalons », il faut une **absence** d'écart démontrée. Avec 100 documents, l'intervalle est large de 14 points : on ne peut pas distinguer 85 % de 92 %. **« On fait aussi bien » sur 100 documents est exactement l'opinion que le document veut interdire.**
- Pour détecter un écart de 5 points — le genre d'écart qui décide d'un achat — il faut **686 documents annotés par bras**.
- Et la section 3 impose quatre langues (français, créole guadeloupéen, anglais, espagnol). Si la mesure doit tenir par langue : **686 × 4 = 2 744 documents annotés**. Pour un seul organe.

**Mon ordre de grandeur, et il est double — la distinction manque au document :**

| Usage de la mesure | Taille | Ce qu'on peut en dire |
|---|---|---|
| Barrière de non-régression, usage interne | **30 à 50 documents / ~150 décisions** | Rien de statistique. Détecte une casse franche. Suffit pour développer |
| **Estimer** la qualité d'un seul système, ± 3 points | **~400 décisions d'annotation** (ce que j'ai mesuré : 609 décisions → ± 2,2 pts) | Opposable sur le niveau atteint |
| **Comparer** deux systèmes, écart de 5 points | **686 documents par bras**, ×4 si par langue | Opposable sur l'écart. C'est ce que le temps 6 réclame |

Le document ne distingue pas « estimer » de « comparer ». C'est la confusion qui rend son jeu d'épreuve ni chiffré ni chiffrable.

### 3.2 Combien de travail humain — ce que je mesure, et ce que je refuse de chiffrer

**Ce que j'ai mesuré, cran A-mesure.** Le corpus d'évaluation du projet trafilatura, lu dans `tests/evaldata.json` :

```
=== Corpus d'évaluation de trafilatura (tests/evaldata.json) ===
taille du fichier : 883683 octets
nombre de pages annotées : 990
structure d'une entrée : {"file": "die-partei.net.luebeck.html",
  "with": ["Die GEMA dreht völlig am Zeiger!", "http://www.openpetition.de"],
  "without": ["31. Mai", "Impressum", "Steuerdarling"]}

chaînes 'with' (doit être extrait)   : 2951
chaînes 'without' (doit être exclu)  : 2966
total de décisions d'annotation      : 5917
moyenne par page                     : 6.0
```

Et la référence publiée par le projet, `tests/eval_baseline.json` :

```json
{"floors": {"fast": 0.9198, "fallback": 0.9257},
 "evaldata_sha": "b443dcaae4d0aa2097a1abc780495635786b5cb2b33a01787f20879a25a8e133",
 "entries": 990, "chunks": [2951, 2966]}
```

**Chiffres fermes, à retenir :** un corpus d'évaluation d'extraction sérieux et reconnu dans ce domaine = **990 pages, 5 917 décisions d'annotation, 6,0 décisions par page**, construit au fil de **7,5 ans de vie du projet et 5,5 années-auteur mesurées**.

C'est l'ordre de grandeur que la consigne demande, et il est mesuré, non estimé.

**Ce que je refuse de chiffrer, et pourquoi c'est la bonne réponse.** Combien de jours de travail humain pour 2 744 pages guadeloupéennes annotées en quatre langues, dont le créole ? **Je l'ignore.** Je n'ai pas de source primaire sur un débit d'annotation, je n'ai annoté aucune page moi-même, et le document m'interdit d'inventer. Un taux inventé ici serait précisément le faux vert que la section 4.1 dénonce.

**Ce qu'il faut faire à la place, et c'est opérationnel :** annoter **10 pages locales en chronométrant**, obtenir un débit réel en décisions par heure, et seulement alors multiplier. C'est une demi-journée qui transforme une inconnue en budget. **Le document, qui fait de la mesure sa doctrine, ne prévoit nulle part de mesurer le coût de sa propre mesure.** C'est son angle mort le plus coûteux.

**Un surcoût que personne n'a chiffré : le créole.** Pour le français, l'anglais et l'espagnol, on recrute un annotateur. Pour le créole guadeloupéen, il faut un locuteur, et il n'y a pas de marché d'annotation. Et la difficulté est réelle, mesurée :

```
py3langid 0.4.0 — nombre de langues du modèle: 142
>>> codes créoles présents: ['ht', 'gcf']

OK   attendu=gcf  prédit=gcf  conf=-343.552 | An ka ale Peyi-la pou vwe fanmi an mwen...
FAUX attendu=gcf  prédit=ht   conf=-290.827 | Se bon manje a-y la, pa ni pwoblem...
FAUX attendu=gcf  prédit=ht   conf=-309.779 | Mesi anpil pou akey-la, chanm-la te prop...
OK   attendu=gcf  prédit=gcf  conf=-278.826 | Nou te bien, dlo-la cho, plaj-la pa lwen...
OK   attendu=fr   prédit=fr   conf=-406.938 | L'accueil etait chaleureux et la chambre...
OK   attendu=en   prédit=en   conf=-364.244 | Lovely little guesthouse, the host was...
OK   attendu=es   prédit=es   conf=-356.851 | La habitacion estaba muy limpia...
exactitude: 5/7
```

Bonne nouvelle pour le document : `gcf`, le créole guadeloupéen, **est** couvert par un outil libre et gratuit — l'exigence « Langues » de la section 3 ne disqualifie pas tout. Mauvaise nouvelle : **2 des 4 échantillons créoles sont classés en créole haïtien**, sur des textes de longueur d'avis. Un acheminement par langue qui confond `gcf` et `ht` enverra des avis guadeloupéens dans la mauvaise file.

*Réserve, et elle est lourde* : **les sept phrases sont de moi, pas de vrais avis.** n = 7, donc l'intervalle de confiance est inutilisable. Ce bloc est un **signal, pas une mesure** : il dit où regarder, il ne dit pas combien. Il faut 50 à 100 avis créoles réels avant d'en conclure quoi que ce soit.

### 3.3 Ce que coûte le jeu d'épreuve — le bilan

| Poste | Chiffre | Cran |
|---|---|---|
| Barrière de non-régression utilisable tout de suite | 30-50 pages, ~150 décisions | A-mesure (calcul) |
| Estimation opposable d'un système, ± 2,2 pts | 609 décisions — je l'ai fait tourner | **A-mesure** |
| Comparaison opposable à l'étalon, écart de 5 pts | 686 pages par bras | A-mesure (calcul) |
| Même chose en 4 langues | 2 744 pages annotées, **par organe** | A-mesure (calcul) |
| Référence du domaine, pour comparaison | 990 pages / 5 917 décisions / 5,5 années-auteur | **A-mesure** |
| Jours-homme pour annoter tout cela | **inconnu — à mesurer sur 10 pages chronométrées** | je refuse d'inventer |
| Annotation du créole | pas de marché, et confusion `gcf`/`ht` observée | signal, n=7 |

---

## 4. Mes mesures de référence — les sorties collées

Pour que les sections 1 à 3 soient opposables, voici les bancs, rejouables à l'identique.

### 4.1 Extraction — trafilatura 2.3.0 contre son propre corpus annoté

Corpus : les 106 pages présentes dans `tests/cache/` du dépôt, avec les annotations de `tests/evaldata.json`. Jeu figé **avant** ma mesure : il est versionné dans le dépôt, et son empreinte est publiée (`evaldata_sha` ci-dessus).

```
trafilatura 2.3.0 — pages du corpus disponibles en cache : 106
décisions évaluées : 609  (erreurs de lecture: 0)
VP=273 FN=14 FP=36 VN=286
precision=0.883  rappel=0.951  F1=0.916  exactitude=0.918
débit : 35.5 pages/s sur 1 cœur (3.0s pour 106 pages)
```

Intervalles de Wilson sur mes propres chiffres :

```
rappel     = 0.951  IC95 [0.920 ; 0.971]  (+/- 2.5 pts, n=287)
precision  = 0.883  IC95 [0.843 ; 0.915]  (+/- 3.6 pts, n=309)
exactitude = 0.918  IC95 [0.893 ; 0.937]  (+/- 2.2 pts, n=609)
```

Mon 0,918 tombe entre les planchers publiés par le projet (0,9198 / 0,9257). **La mesure se reproduit.** C'est le seul étalon de la section 6 que ce document produit réellement — et il est tenu par un outil gratuit sous Apache-2.0, pas par un modèle propriétaire.

### 4.2 Index — SQLite FTS5, déjà présent dans Python 3.11

```
sqlite3 3.45.1 / FTS5
documents indexés      : 200000
temps d'indexation     : 28.2 s  (7082 doc/s)
taille de l'index      : 622.2 Mo  (3.11 ko/doc)
requêtes jouées        : 200
latence p50 / p95 / max: 82.7 / 165.0 / 270.8 ms
coût matériel          : 1 fichier, 0 serveur, 0 dépendance externe
```

*Réserve* : mon corpus synthétique tire 180 mots au hasard dans un vocabulaire de 6 000 — c'est un cas défavorable pour un index inversé, la p50 réelle sur de la presse sera meilleure. Mais le point tient : **l'organe « Index » de la section 6 ne demande ni construction ni installation.** 19,3 années-auteur de tantivy achètent de la performance dont le marché guadeloupéen n'a pas l'usage.

### 4.3 Découverte — crawler minimal, 47 lignes

```
lignes de code non vides du crawler : 47
concurrence=8 délai=0.0s  pages_ok=3000 erreurs=0 urls_découvertes=3001 octets=5.7Mo  durée=3.6s  débit=822.7 pages/s
concurrence=2 délai=0.2s  pages_ok=300  erreurs=0 urls_découvertes=3001 octets=0.7Mo  durée=30.4s  débit=9.9 pages/s
```

47 lignes : file d'attente, déduplication d'URL, lecture et respect de `robots.txt`, concurrence réglable, délai de politesse, agent déclaré. Le second passage est le réglage *poli* du 2.3 du document — 2 connexions, 200 ms d'attente — et il tient **9,9 pages/s, soit environ 855 000 pages par jour.**

*Réserve majeure, et elle est décisive* : **serveur local, pas une seule source guadeloupéenne réelle** (sortie réseau refusée, voir section 0). Ce banc mesure le moteur, pas le terrain : pas de TLS, pas de limitation de débit distante, pas de JavaScript, pas de défense anti-robot, pas de HTML malpropre. **Le vrai coût du crawl n'est pas dans ces 47 lignes, il est dans la liste des sources et leur qualification source par source.** Et cela, le document le voit très bien — c'est son V0. Ce qu'il ne voit pas, c'est que l'organe technique, lui, est quasi gratuit.

### 4.4 La chaîne complète — quatre organes en 64 lignes

Découverte → extraction → provenance → index → requête avec remontée à la source primaire, base SQLite unique :

```
lignes de code non vides : 64
=== chaîne dégradée : découverte + extraction + provenance + index ===
documents traités de bout en bout : 1000 en 9.5s  (105.4 doc/s)
base unique : 1.9 Mo
provenance : 1000 captures, 1000 empreintes brutes distinctes, 2.0 Mo d'original haché
requête + remontée à la source primaire : 5.9 ms
   http://127.0.0.1:8731/p/3.html 2026-10-02T19:18:37Z 58592cd375248edb... | Article 3 — [Guadeloupe]
   http://127.0.0.1:8731/p/2.html 2026-10-02T19:18:37Z 348da1765244a8c2... | Article 2 — [Guadeloupe]
   http://127.0.0.1:8731/p/0.html 2026-10-02T19:18:37Z d693d79edc23655d... | Article 0 — [Guadeloupe]

assertions remontables à une source primaire datée : 1000/1000 = 100%
assertions rejouables à l'identique (sha256 du brut conservé) : 100%
```

Le schéma porte une table `source` avec son **guichet** et sa **licence** — la qualification de la section 2.3 est dans la base, pas dans un document Word. Les trois étalons de Provenance de la section 6 sortent à 100 % sans aucune annotation humaine.

---

## 5. Verdict

### 5.1 La méthode des six temps est-elle exécutable par une très petite équipe ? **Non.**

Quatre raisons, dans l'ordre de gravité :

1. **Le temps 2 est bloqué** — pas d'essai en libre-service chez les modèles visés, et une démonstration commerciale produit exactement la preuve que le temps 2 rejette.
2. **La règle 4.2 transforme ce blocage en impasse** — sans A-mesure sur le modèle, aucune décision de construire n'est autorisée. Le projet ne peut pas démarrer sous ses propres règles.
3. **Le jeu d'épreuve opposable coûte 686 pages annotées par bras, 2 744 en quatre langues, par organe** — et le document n'a jamais écrit de chiffre. La référence du domaine, mesurée, a coûté 990 pages et 5,5 années-auteur.
4. **Les huit organes ne sont pas huit chantiers** — ils sont quatre cadeaux déjà emballés, un chantier réel et petit, deux guichets déguisés en organes, et un organe qu'il est imprudent d'écrire.

### 5.2 Ce qu'il faut retirer pour qu'elle le devienne

**Retirer — quatre coupes :**

1. **Supprimer le temps 2 comme préalable.** Le remplacer par : *« repérer l'étalon public de l'organe — un corpus d'évaluation déjà annoté et publié, ou le chiffre publié par le meilleur projet libre »*. J'ai montré que ça marche : 0,918 mesuré contre 0,9198 publié, sans parler à aucun commercial. Le temps 2 ne se fait qu'au cas où un essai réel existe, et il n'est jamais bloquant.
2. **Supprimer la règle « aucune décision de construire sur un cran B ou moins »** et la remplacer par : *« aucune décision de construire sans avoir d'abord mesuré l'équivalent libre sur le jeu d'épreuve »*. L'obstacle à franchir est le libre, pas le propriétaire. Le propriétaire n'est souvent même pas le bon étalon.
3. **Retirer « Garde des accès confiés » de la liste des organes à reconstruire.** Y inscrire une interdiction : on ne code pas de crypto, on loue un coffre ou on ne détient aucun secret durable.
4. **Retirer « Avis » et « Publication » de la liste des organes à reconstruire.** Ce ne sont pas des problèmes d'ingénierie, ce sont des guichets et une licence AGPL. Les traiter en V1, pas en V3.

**Ajouter — ce qui manque et que la consigne réclame :**

**La version minimale utilisable, définie par un client et non par un périmètre.** Un client guadeloupéen payant, trois sources en guichet 6 déclaré, la chaîne des quatre organes de collecte (64 lignes, mesurée), un rapport de veille hebdomadaire où **chaque assertion porte son URL, sa date et son empreinte**. Pas d'avis, pas de publication, aucun secret détenu. C'est le produit, et c'est déjà vendable : la provenance est l'argument, et c'est le seul organe que personne ne vend.

**Le jalon de revenu, placé avant V1 et non après V5.** *Un client payant avant d'ouvrir la vague des guichets.* Raison : V1 est décrite comme « la vague la plus lourde » et exige un juriste. Payer un juriste pour qualifier le mandat avant d'avoir un seul client qui veut confier un accès, c'est acheter la réponse à une question que personne n'a posée.

**Le critère d'abandon, et voici celui que je propose — la règle du loyer.**

> **Un organe n'est pas reconstruit si le louer coûte, par an, moins que le maintenir coûterait.** On loue quand : il existe un service ou un libre qui tient l'étalon ; son coût annuel est inférieur à 10 % du revenu récurrent annuel qu'il débloque ; et le remplacer prendrait moins de 30 jours si le fournisseur disparaissait.
>
> **Trois interdictions absolues, qui ne se négocient pas contre un chiffre :** on ne reconstruit jamais de la cryptographie ni un coffre à secrets ; on ne reconstruit jamais un organe dont l'équivalent libre tient déjà l'étalon ; on ne reconstruit jamais un organe dont aucun client n'a encore payé le résultat.
>
> **Et le critère de renoncement, celui qui manque le plus :** un organe est **abandonné**, pas reporté, si après 10 jours de travail il n'atteint pas 80 % de l'étalon sur la barrière de 30 à 50 pages. On consigne l'écart, on loue, et on passe. Le document admet trois issues au temps 6 ; il lui manque la quatrième, la seule qui fasse gagner du temps : **renoncer tôt.**

**Le banc dédoublé.** Un banc figé pour extraction, pertinence, provenance. Un banc vivant daté pour fraîcheur et délai de détection. Le document en demande un seul et lui confie des métriques incompatibles.

**La mesure du coût de la mesure.** Avant d'engager V0 : annoter 10 pages locales en chronométrant. Une demi-journée qui donne le budget du jeu d'épreuve. Sans elle, V0 est une tâche à durée inconnue placée sur le chemin critique.

### 5.3 Ce que le document a juste, et qu'il ne faut pas casser en le corrigeant

Trois choses, et elles portent le projet :

- **Le guichet 6 et la qualification source par source.** C'est l'apport de la v4 et c'est le bon. Ma chaîne le met en base dès le premier document.
- **La provenance comme couche propre.** Mesurée : 100 % des assertions remontables, datées, rejouables, pour une quinzaine de lignes. C'est le seul étalon de la section 6 à la fois distinctif, gratuit à mesurer, et que personne ne vend. **C'est le produit.** Le document le range au quatrième rang sur huit.
- **Le cran D et l'obligation de le déclarer.** C'est le meilleur mécanisme du document. Il m'a obligé à écrire la section 0, et la section 0 dit la chose la plus utile de ce retour : un agent enfermé dans un conteneur d'entreprise ne peut pas exécuter les temps 1 et 2, et rendra du C maquillé si on ne le lui demande pas en face.

---
---

# RELANCE 1 — anti-oubli

## Qu'ai-je oublié — trois candidats écartés, et pourquoi

**1 — Les modèles paramétriques de coût logiciel (COCOMO et dérivés), pour convertir mes lignes de code en mois-homme.** Écarté parce que je n'ai atteint aucune source primaire sur leurs coefficients (sortie réseau refusée), et que les appliquer de mémoire aurait produit un chiffre en jours-homme à l'allure impeccable et au fondement D. C'est exactement le faux vert que la section 4.1 décrit. J'ai préféré livrer des années-auteur mesurées, moins séduisantes et vraies. **Conséquence assumée : mon chiffrage ne se convertit pas en budget.** Il donne un ordre de grandeur et une décision — louer ou construire — pas une ligne comptable.

**2 — Readability, Boilerpipe, Goose3, newspaper3k, resiliparse, et le détourage par grand modèle de langage, comme concurrents de trafilatura.** Écartés par discipline, et le document me l'ordonne : « trois briques tenues valent quinze listées » (4.3). J'en ai tenu une, mesurée, reproductible. Mais l'omission a un prix réel : **je n'ai pas démontré que trafilatura est le meilleur libre, j'ai démontré qu'un libre gratuit tient 0,916.** Si un concurrent fait 0,95 sur pages locales difficiles, mon verdict « adopter trafilatura » est à refaire. Le banc est écrit, le rejouer sur trois extracteurs est une demi-journée.

**3 — Docker, alors qu'il est disponible dans le conteneur.** Écarté par arbitrage de temps : lancer Elasticsearch ou OpenSearch pour mesurer l'organe Index contre un vrai moteur distribué aurait pris plus longtemps que tous mes autres bancs réunis. Prix de l'omission : **ma comparaison d'index est unilatérale.** Je sais que FTS5 fait p50 = 82,7 ms sur 200 000 documents ; je ne sais pas ce que fait Elasticsearch sur le même corpus. Je ne peux donc pas dire « FTS5 suffit », seulement « FTS5 est à zéro coût et donne ce chiffre ». La conclusion « ne rien installer » tient quand même, parce qu'elle repose sur l'absence de besoin démontré, pas sur une supériorité.

## Que n'ai-je pas vu — ce que je n'ai pas pu vérifier, et ce qui m'a manqué

- **Toute la Guadeloupe.** Pas un octet de source locale réelle. `la1ere.francetvinfo.fr`, `rci.fm`, `karibinfo.com`, `franceantilles.fr`, `guadeloupe.cci.fr`, `meteofrance.gp` : tous refusés en 403 au CONNECT. Il m'a manqué une autorisation de sortie réseau. **Aucune de mes mesures n'est guadeloupéenne.** Elles sont des bornes de faisabilité, pas des résultats de terrain.
- **Les étalons propriétaires, c'est-à-dire le temps 1 et le temps 2 en entier.** Je n'ai pas vu tourner Meltwater, Brandwatch, Revinate, ReviewPro. Je n'ai donc pas *vérifié* que le temps 2 est impraticable : j'ai constaté que je ne pouvais pas le faire, et lu des comparatifs en cran C. **Mon argument le plus lourd — l'impasse décisionnelle de 2.2 — repose sur du C.** Il faut deux demi-journées humaines pour le monter en B : ouvrir les six pages de tarifs des éditeurs et constater s'il existe un bouton d'essai.
- **Les deux décisions de justice de la section 2.5.** `curia.europa.eu` bloqué. Le document les donne en D, elles restent en D. Je n'ai pas pu rendre ce service.
- **Le plafond de 5 avis chez Google et TripAdvisor.** C'est, après l'impasse décisionnelle, mon argument le plus conséquent — il rend un étalon de la section 6 non mesurable sans passer par le 5c interdit. Il repose sur des extraits de recherche et des blogs de vendeurs de moissonnage, **cran C**. `developers.google.com` et la documentation TripAdvisor sont bloqués. **À vérifier en B avant toute décision.**
- **Le débit d'annotation humaine.** Mon trou le plus net. Je n'ai ni source ni mesure. Je le dis au lieu de le combler.
- **Le créole en vrai.** Sept phrases écrites par moi. Je n'ai pas vu un seul avis guadeloupéen authentique.

## Qu'est-ce qui rendrait ce produit plus profitable — l'endroit exact où il perd de l'argent, et le geste qui le corrige

**L'endroit exact.** Le produit perd de l'argent dans la **séquence des vagues**, à une ligne précise : la section 8 place V1 — « vague la plus lourde », juriste obligatoire, licences de contenu presse, cartographie de tous les guichets de toutes les plateformes — **avant** toute livraison à un client. C'est la dépense maximale placée au point d'incertitude maximale. On paie un juriste pour sécuriser un mandat que personne n'a encore demandé, et une licence de contenu presse pour une veille que personne n'a encore achetée.

Le deuxième foyer de perte est dans la section 6 : elle inscrit « Garde des accès confiés » comme organe à reconstruire avec étalons chiffrés. 97,8 années-auteur mesurées en face. Tout jour dépensé là est perdu deux fois — en développement, puis en audit de sécurité qui le refusera.

**Le geste qui corrige, et il est unique.** *Inverser V0/V1 et V2, et vendre la provenance avant de construire quoi que ce soit d'autre.*

Concrètement : prendre les 64 lignes de la section 4.4, les pointer sur **trois sources guadeloupéennes en guichet 6 déclaré** — un portail de données ouvertes, un flux RSS institutionnel, un flux de presse — et livrer à un client un rapport de veille hebdomadaire où **chaque ligne porte son URL, son horodatage UTC et son empreinte SHA-256 vérifiable**. Pas d'avis. Pas de publication. Aucun secret détenu, donc aucun organe de garde, donc aucun juriste pour le mandat, donc pas de V1.

Pourquoi c'est le geste rentable, et pas une facilité :

- **Il encaisse avant de dépenser.** Le revenu arrive avant le juriste, avant la licence de contenu, avant le coffre à secrets.
- **Il vend l'organe que personne ne vend.** Le guichet 2 et la proximité sont un avantage réel (2.7) mais ils se gagnent en des mois de relation. La provenance vérifiable se livre en jours et se démontre en une capture d'écran. **C'est le seul étalon de la section 6 que j'ai mesuré à 100 % pour une quinzaine de lignes de code, et que je n'ai vu vendu par personne.**
- **Il remplace trois agents de V0 par un client.** « Qui achète, combien ils sont, ce qu'ils paient » s'apprend plus vite et plus vrai en facturant un établissement qu'en étudiant un marché.
- **Il reporte la dépense sans renier la doctrine.** Guichet 6 uniquement : attribution respectée, débit respectueux, aucune zone grise. Le registre de qualification source par source — le meilleur apport de la v4 — est tenu dès le premier document, en base, pas dans un document séparé. **La rigueur n'est pas retirée, elle est déplacée autour de la livraison au lieu d'être placée devant.**

Ce que ce geste coûte, et il faut l'assumer : on renonce au volet avis au départ, et c'est « ce que le client paie » selon la section 6. Le pari est que la veille sourcée se vend seule à un premier client, et que ce client ouvre ensuite le guichet 2 de lui-même parce qu'il nous fait confiance. **Si ce pari est faux, il est faux en semaines et pour quelques jours de travail — pas en mois et après V1.** C'est ce qui le rend meilleur que le plan écrit, dont la première réfutation possible arrive en V5.

---

# RELANCE 2 — preuve, étalon et guichet

## Ligne par ligne

### L1 — Années-auteur investies dans les six organes libres : 142,7
- **Testé ?** Oui.
- **Avec quoi exactement.** `git` sur six clones nus `--filter=blob:none` de `adbar/trafilatura`, `apache/nutch`, `DigitalPebble/storm-crawler`, `quickwit-oss/tantivy`, `openbao/openbao`, `gitroomhq/postiz-app`. Conteneur Linux 6.18, 4 cœurs. **2 octobre 2026.**
- **Commande.** `git log --all --date=format:'%Y-%m' --format='%ad|%aE' | tr 'A-Z' 'a-z' | sort | uniq -c | awk '$1>=5' | wc -l`
- **Obtenu.** Sortie collée en 1.2 (`nutch AY>=5c=25.5` … `openbao AY>=5c=97.8` …).
- **Validé / recopié.** Entièrement validé par moi. Rien de recopié. **Mais le seuil de 5 commits/mois est mon choix, non une convention établie** — un autre seuil donnerait d'autres chiffres (j'ai aussi calculé le seuil 15, disponible dans la sortie).
- **Opposable ?** **Oui.** Dépôts publics, commande d'une ligne, même résultat pour quiconque, aux commits postérieurs près. Préciser la date est obligatoire : le chiffre monte avec le temps.
- **Mais est-ce un étalon au sens du document ? Non.** Ce n'est pas guadeloupéen, et ce n'est pas un jeu d'épreuve. C'est une mesure d'effort investi, qui ne se convertit pas en jours-homme (voir D1).
- **Cran : A-mesure** pour les années-auteur. **D pour toute conversion en jours-homme — que je n'ai pas faite.**

### L2 — trafilatura 2.3.0 : F1 = 0,916, rappel 0,951, précision 0,883, 35,5 pages/s
- **Testé ?** Oui.
- **Avec quoi.** trafilatura 2.3.0 installé par `pip`, Python 3.11.15. Corpus : 106 pages de `tests/cache/` du dépôt, annotations de `tests/evaldata.json`. **2 octobre 2026.**
- **Obtenu.** `VP=273 FN=14 FP=36 VN=286 / precision=0.883 rappel=0.951 F1=0.916` — sortie complète en 4.1.
- **Validé / recopié.** Mesure validée par moi. **Recopié du dépôt : les annotations, et le plancher publié `{"fast": 0.9198, "fallback": 0.9257}`.** Je n'ai pas annoté une seule page.
- **Opposable ?** **Oui, et c'est ma meilleure ligne.** Le jeu était figé avant ma mesure — versionné dans le dépôt, empreinte publiée `b443dcaa…`. Mon 0,918 d'exactitude tombe entre les deux planchers du projet : **la mesure se reproduit indépendamment.**
- **Guadeloupéen ?** **Non.** Corpus multilingue européen. **Ce n'est donc pas un étalon valide au sens de la section 5 du document.** C'est la démonstration qu'un étalon de ce type est constructible et reproductible, pas le chiffre à retenir pour la Guadeloupe.
- **Cran : A-mesure.**

### L3 — Intervalles de Wilson et tailles d'échantillon (686 par bras pour 5 points)
- **Testé ?** Oui — calculé, pas cru.
- **Avec quoi.** Python 3.11.15, `math` seul. Wilson à z = 1,96 ; taille d'échantillon pour deux proportions à α = 0,05 et puissance 0,80 (z = 1,959964 / 0,8416212). **2 octobre 2026.**
- **Obtenu.** Tableaux collés en 3.1 ; intervalles sur mes propres chiffres en 4.1.
- **Validé / recopié.** Calcul exécuté par moi. **Les formules viennent de ma mémoire** — je n'ai pu atteindre aucune source primaire de statistique.
- **Opposable ?** Le calcul, oui : trois lignes de Python, résultat déterministe, tout statisticien le refait. **Le choix d'un test de deux proportions pour comparer deux extracteurs sur le même corpus est discutable** — un test apparié (McNemar) serait plus puissant et demanderait moins de documents. Mes chiffres sont donc une **borne haute prudente**, et je le dis plutôt que de le cacher.
- **Cran : A-mesure** pour les nombres. **D pour le choix du test** — à faire valider par un statisticien.

### L4 — Corpus annoté de référence : 990 pages, 5 917 décisions, 6,0 par page
- **Testé ?** Oui, lu et dépouillé.
- **Avec quoi.** `json.load` sur `tests/evaldata.json`, clone de profondeur 1 du dépôt. **2 octobre 2026.**
- **Obtenu.** Sortie collée en 3.2, avec la structure d'une entrée et `eval_baseline.json` intégral.
- **Validé / recopié.** Comptages validés par moi. **Le fichier est recopié du dépôt** — c'est un document primaire que j'ai lu, pas une affirmation de tiers.
- **Opposable ?** **Oui.** Fichier public, empreinte publiée dans le dépôt, comptage trivial à refaire.
- **Cran : A-mesure** (j'ai compté) **adossé à B** (document primaire lu, dépôt public, 2 octobre 2026).

### L5 — Licences : Apache-2.0 ×3, MIT, MPL-2.0, et **Postiz en AGPL-3.0**
- **Testé ?** Oui — fichiers `LICENSE` lus à la racine de chaque dépôt.
- **Avec quoi.** `head` sur `LICENSE` / `LICENSE-binary` de chaque clone. **2 octobre 2026.**
- **Obtenu.** Tableau en 1.2 ; en-tête intégral de `postiz-app/LICENSE` : `GNU AFFERO GENERAL PUBLIC LICENSE / Version 3, 19 November 2007`.
- **Validé / recopié.** Lu directement. Conforme à l'exigence de 4.4 (« licence SPDX lue dans le fichier LICENSE »).
- **Opposable ?** Oui.
- **Réserve honnête.** J'ai lu le fichier à la racine. **Je n'ai pas audité les licences des dépendances transitives** — pour postiz (114 131 lignes TypeScript) c'est un travail à part entière.
- **Cran : B** (document primaire lu, URL du dépôt, date).

### L6 — SQLite FTS5 : 200 000 documents, 28,2 s, 622 Mo, p50 = 82,7 ms
- **Testé ?** Oui.
- **Avec quoi.** `sqlite3` 3.45.1 via Python 3.11.15, `fts5(tokenize='unicode61 remove_diacritics 2')`, `bm25()`, 200 requêtes. **2 octobre 2026.**
- **Obtenu.** Sortie collée en 4.2.
- **Validé / recopié.** Entièrement mesuré par moi.
- **Opposable ?** **Non, et c'est le plus faible de mes bancs.** Le corpus est synthétique, graine `random.seed(42)` : 180 mots tirés dans 6 000, ce qui est pathologique pour un index inversé. Pas de presse réelle, pas de requêtes réelles, pas de jugements de pertinence. **Un tiers rejouerait mon script à l'identique et obtiendrait mes chiffres ; il n'en conclurait rien sur la Guadeloupe.** La métrique « pertinence sur requêtes figées » de la section 6 n'est pas mesurée du tout ici.
- **Cran : A-usage.** Pas A-mesure : il n'y a pas d'étalon en face, et le jeu n'est ni réel ni guadeloupéen.

### L7 — Crawler de 47 lignes : 3 000 pages, 0 erreur, 9,9 pages/s en réglage poli
- **Testé ?** Oui.
- **Avec quoi.** Script de 47 lignes non vides que j'ai écrit (`asyncio`, `http.client`, `urllib.robotparser`), contre un `python3 -m http.server` local servant 3 000 pages générées sur `127.0.0.1:8731`. **2 octobre 2026.**
- **Obtenu.** Sortie collée en 4.3.
- **Validé / recopié.** Tout écrit et mesuré par moi.
- **Opposable ?** **Non, pour le monde réel.** Serveur local : pas de TLS, pas de latence réseau, pas de limitation distante, pas de JavaScript, pas de défense anti-robot, HTML que j'ai moi-même produit et donc propre. **Il mesure une borne haute de débit du moteur, pas une capacité de collecte.** Ce qui est opposable : les 47 lignes, et le fait qu'elles incluent `robots.txt` et un délai de politesse.
- **Cran : A-usage.** Jamais A-mesure.

### L8 — Chaîne complète en 64 lignes : 1 000 documents, 9,5 s, provenance 100 %
- **Testé ?** Oui.
- **Avec quoi.** Script de 64 lignes non vides, trafilatura 2.3.0 + SQLite FTS5 + SHA-256, contre le même serveur local. **2 octobre 2026.**
- **Obtenu.** Sortie collée en 4.4, avec trois résultats de requête remontant à l'URL, l'horodatage et l'empreinte.
- **Validé / recopié.** Tout mesuré par moi.
- **Opposable ?** **Les trois étalons de Provenance, oui — et c'est la seule chose de ce retour qui soit un étalon de la section 6 réellement produit.** « Part des assertions remontées à une source primaire », « part datée », « part rejouable à l'identique » valent 100 %, et c'est vérifiable par construction : l'empreinte du brut est en base. **Ces métriques-là ne dépendent pas du corpus** — c'est pourquoi elles sont mesurables sans annotation, et pourquoi elles restent vraies sur des sources guadeloupéennes.
- **Ce qui n'est pas opposable** : le débit de 105 doc/s (serveur local) et la qualité d'extraction (HTML que j'ai écrit).
- **Cran : A-mesure pour les trois taux de provenance. A-usage pour le reste.**

### L9 — Détection du créole guadeloupéen : `gcf` couvert, 2 échantillons sur 4 confondus avec `ht`
- **Testé ?** Oui.
- **Avec quoi.** `py3langid` 0.4.0 installé par `pip`, modèle `data/model.npz.xz` ouvert en `lzma` + `numpy` pour lister les 142 classes, puis `classify()` sur 7 phrases. **2 octobre 2026.**
- **Obtenu.** Sortie collée en 3.2.
- **Validé / recopié.** La liste des 142 langues et les prédictions sont mesurées par moi. **Les 7 phrases sont écrites par moi, et c'est la faiblesse décisive.**
- **Opposable ?** **Non.** n = 7, dont 4 en créole. Aucune représentativité, aucun intervalle de confiance utilisable, et je suis à la fois l'auteur du corpus et celui qui déclare la vérité de terrain — ce qui est exactement le défaut que le document interdit. **Un tiers rejouerait mon script à l'identique, mais le corpus n'a aucune valeur de preuve.**
- **Ce qui tient quand même.** Une chose, vérifiable : **`gcf` figure dans les 142 classes du modèle.** C'est un fait sur le modèle, pas sur mon corpus, et il suffit à dire que l'exigence « Langues » de la section 3 ne disqualifie pas tout le libre.
- **Cran : A-usage pour la présence de `gcf`. C pour le taux de confusion `gcf`/`ht`** — signal à vérifier sur 50 à 100 avis réels avant toute conclusion.

### L10 — Pas d'essai en libre-service chez les plateformes de veille ; gestion de réputation hôtelière sur devis
- **Testé ?** **Non.** Je n'ai ouvert aucun compte, tenté aucune inscription.
- **Avec quoi.** `WebSearch`, 2 octobre 2026. Les pages des éditeurs (`brandwatch.com`) sont **bloquées par la politique de sortie réseau** ; `WebFetch` renvoie `EGRESS_BLOCKED`.
- **Obtenu.** Des extraits de comparatifs. Aucun document d'éditeur lu.
- **Validé / recopié.** **Entièrement recopié.** Rien validé.
- **Opposable ?** Non.
- **Cran : C.** Et comme la section 4.1 l'ordonne : **va au dépôt.** C'est gênant, parce que c'est ce qui soutient mon argument de 2.1. Deux demi-journées humaines le montent en B.

### L11 — Plafond de 5 avis : Google Places et TripAdvisor Content API ; avis complets réservés au titulaire via Google Business Profile
- **Testé ?** **Non.** Aucune clé d'interface, aucun appel.
- **Avec quoi.** `WebSearch`, 2 octobre 2026. `developers.google.com` et `tripadvisor-content-api.readme.io` renvoient `EGRESS_BLOCKED`.
- **Obtenu.** Extraits de blogs, dont des vendeurs de moissonnage — **partie intéressée à affirmer que les interfaces officielles sont insuffisantes.**
- **Validé / recopié.** Entièrement recopié, de sources suspectes.
- **Opposable ?** Non.
- **Cran : C.** Au dépôt. **Et c'est le plus coûteux de mes aveux** : l'affirmation « l'étalon Avis de la section 6 est structurellement non mesurable sans passer par le 5c » est le plus gros reproche de ce retour, et il repose sur du C. **À confirmer en B avant toute décision d'architecture.**

### L12 — Booking.com : minimum de propriétés, ABRN 3 000, 250 annonces ouvertes en moyenne journalière
- **Testé ?** Non.
- **Avec quoi.** `WebSearch`, 2 octobre 2026. `connectivity.booking.com` **bloqué**.
- **Obtenu.** Extrait décrivant la page de l'éditeur lui-même — mais **je n'ai pas lu cette page.**
- **Cran : C.** Au dépôt. Le document classait déjà le guichet 1 en ⏳ D ; je ne l'en sors pas, et son verdict « hors de portée au départ » reste non étayé — probablement juste, non prouvé.

### L13 — Incohérences internes du document : « sept » organes contre huit, « cinq » guichets contre six, règle 4.2 violée par la section 1
- **Testé ?** Oui — lecture intégrale et comptage.
- **Avec quoi.** Lecture des 329 lignes de `00-PROMPT-DE-LANCEMENT.md`, comptage des lignes de tableau. **2 octobre 2026.**
- **Obtenu.** Section 6 : 8 lignes d'organes. Section 4.4 : « Lequel des **sept** de la section 6 ». Section 2.2, titre : « **cinq** guichets » ; tableau en dessous : 6 lignes. Section 1 tranche les guichets 2 et 6 ; tous les guichets du tableau 2.2 portent ⏳ D ; règle 4.2 : « Aucun choix de guichet ne se prend sur un cran D ».
- **Validé / recopié.** Validé par moi sur le document lui-même.
- **Opposable ?** **Oui, totalement.** Le document est le document primaire, n'importe qui recompte.
- **Cran : A-usage** (lecture et comptage directs du document visé). C'est, avec L8, la partie la plus solide de ce retour — et elle n'a coûté que de la lecture.

## Par quel guichet accèdent les acteurs que je cite ?

Le document l'exige (relance 2), et c'est la question sur laquelle je suis le plus faible.

| Acteur cité | Guichet | Comment je le sais |
|---|---|---|
| trafilatura, Nutch, StormCrawler, tantivy, OpenBao, Postiz | **Sans objet** — ce sont des outils, pas des collecteurs. Ils n'accèdent à rien ; le guichet dépend de qui les pointe sur quoi | Lecture du code et des licences, cran B |
| Meltwater, Brandwatch, Talkwalker | **Inconnu.** Le document avance le guichet 4 pour la veille presse via `NLA c. Meltwater` — en cran D, non vérifié par moi | **Je l'ignore, et je l'écris** |
| Revinate, ReviewPro, TrustYou | **Inconnu.** Probablement guichet 2 chez Google (avis complets au titulaire) et peut-être guichet 1 ailleurs. **Je ne le sais pas** | **Je l'ignore, et je l'écris** |
| Vendeurs de moissonnage cités dans mes extraits de recherche (L11) | **Guichet 5, et vraisemblablement 5c** — ils vendent explicitement le dépassement du plafond de 5 avis | Déduction depuis leur offre, **cran C**. Je ne l'affirme pas |
| **Mon propre banc** | **Aucun guichet : serveur local que j'ai moi-même généré.** Je n'ai collecté strictement rien sur Internet | A-usage, et c'est la limite centrale de ce retour |

## Reclassement final

| # | Ligne | Cran | Sort |
|---|---|---|---|
| L1 | 142,7 années-auteur sur six organes libres | **A-mesure** | Livrable. Conversion en jours-homme : **interdite, cran D** |
| L2 | trafilatura F1 = 0,916 / 35,5 pages/s | **A-mesure** | Livrable. **Non guadeloupéen** : pas un étalon au sens de la section 5 |
| L3 | 686 pages par bras pour 5 points d'écart | **A-mesure** (calcul) | Livrable. Choix du test statistique à valider — **D** |
| L4 | 990 pages / 5 917 décisions d'annotation | **A-mesure + B** | Livrable |
| L5 | Licences, dont **Postiz en AGPL-3.0** | **B** | Livrable, marqué B. Dépendances transitives non auditées |
| L6 | FTS5 : 200 k docs, p50 = 82,7 ms | **A-usage** | Livrable comme borne. Corpus synthétique : rien sur la pertinence |
| L7 | Crawler de 47 lignes, 9,9 pages/s poli | **A-usage** | Livrable comme borne de faisabilité. **Jamais comme capacité de collecte** |
| L8 | Chaîne de 64 lignes, provenance 100 % | **A-mesure** (provenance) / **A-usage** (reste) | Livrable. **Le seul étalon de la section 6 réellement produit** |
| L9 | `gcf` dans le modèle / confusion avec `ht` | **A-usage** (présence) / **C** (confusion) | Présence livrable. Confusion → **au dépôt**, signal seul |
| L10 | Pas d'essai en libre-service chez les éditeurs de veille | **C** | **Au dépôt.** Soutient pourtant mon argument de 2.1 — à monter en B |
| L11 | Plafond de 5 avis chez Google et TripAdvisor | **C** | **Au dépôt.** Mon reproche le plus lourd repose dessus — **à monter en B en priorité** |
| L12 | Seuils du programme de connectivité Booking | **C** | **Au dépôt** |
| L13 | Trois incohérences internes du document | **A-usage** | Livrable. Document primaire, recomptable par quiconque |

**Bilan de crans : 5 lignes en A-mesure, 3 en A-usage, 1 en B, 4 en C, et 6 lignes déclarées en D en section 0.** Les quatre C portent tout mon volet « accès et marché » — autrement dit : **mon attaque sur la faisabilité technique est solide et mesurée ; mon attaque sur l'impraticabilité du temps 2, qui est ma conclusion la plus lourde, est la plus fragile de ce retour.** Elle est à refaire par un humain avec un navigateur, et cela prend deux demi-journées.

---
---

# Les cinq colonnes

## 1. MCP à installer

| MCP | Ce qu'il débloque | Prérequis |
|---|---|---|
| **Serveur de récupération web avec sortie autorisée** (Fetch, Playwright, ou passerelle maison) | **Le blocage le plus coûteux de cette session.** Sans lui, aucune source guadeloupéenne n'est atteignable, donc le temps 1, le temps 2 et la constitution du jeu d'épreuve sont hors de portée de tout agent | Liste blanche de domaines à ouvrir dans la politique de sortie : presse et institutions locales, `developers.google.com`, `curia.europa.eu`, `legifrance.gouv.fr`, pages de tarifs des éditeurs |
| **MCP de données ouvertes françaises** (`data.gouv.fr`, API institutionnelles) | Le guichet 6 de la section 2.4, par interface plutôt que par moissonnage. Alimente directement le registre de sources qualifiées de V0 | Jeton d'interface, licence lue source par source |
| **MCP juridique** (Légifrance, EUR-Lex, CJUE) | Fait passer les deux décisions de la section 2.5 de D à B, et la règle 4.2 l'exige pour tout choix de guichet | Accès ouvert, sortie réseau autorisée |
| **MCP PostgreSQL** | Le client est déjà installé (16.14). Fait passer la chaîne de SQLite à une base multi-clients cloisonnée quand le premier client en appelle un second | Serveur à provisionner ; inutile avant le deuxième client |
| **MCP Google Business Profile** | **Le seul guichet 2 réellement outillé pour les avis.** Avis complets, réponse possible, pour les établissements qui nous mandatent | Validation Google, mandat écrit du titulaire, garde des accès |

## 2. Logiciels manquants

| Manquant | Pourquoi il bloque |
|---|---|
| **Sortie réseau vers les domaines guadeloupéens** | Ce n'est pas un logiciel, c'est la cause première. Tout le reste en découle |
| **Un deuxième et un troisième extracteur** (resiliparse, goose3, readability) | Pour que « adopter trafilatura » soit un verdict et non un défaut de comparaison (relance 1, écarté n° 2) |
| **Un corpus d'avis guadeloupéens réels, même petit** | 50 à 100 avis en 4 langues, dont le créole. Sans eux, L9 reste un signal à n = 7 |
| **Un chronomètre d'annotation** — 10 pages annotées à la main, minutées | **Le manquant le plus rentable du lot.** Une demi-journée qui transforme le budget du jeu d'épreuve d'inconnu en chiffre |
| **Elasticsearch ou OpenSearch en conteneur** | Docker est là, je ne l'ai pas utilisé. Rendrait la comparaison d'index bilatérale |
| **Un coffre à secrets loué** (coffre infonuagique géré, ou OpenBao installé non modifié) | Et l'interdiction écrite de reconstruire cet organe |

## 3. Outils déjà disponibles et non exploités

| Déjà là | Ce qu'il fait, et que le document ignore |
|---|---|
| **SQLite 3.45.1 avec FTS5, dans Python** | **L'organe « Index » de la section 6, à coût nul.** 200 000 documents, un fichier, zéro serveur. Mesuré |
| **`hashlib` + `datetime` de la bibliothèque standard** | **L'organe « Provenance », à 100 % sur ses trois étalons, en une quinzaine de lignes.** Mesuré. C'est l'avantage distinctif du projet, et il est dans la bibliothèque standard |
| **`asyncio` + `urllib.robotparser`** | L'organe « Découverte » à l'échelle locale : 47 lignes, `robots.txt` respecté, délai de politesse. Mesuré |
| **trafilatura 2.3.0 sous Apache-2.0** | L'organe « Extraction » à F1 = 0,916, **avec son corpus de 990 pages annotées déjà fait et sa référence publiée.** Le temps 1 et le temps 3 de la section 5 sont déjà faits pour cet organe, gratuitement |
| **Docker 29.6.2, PostgreSQL 16.14, Node 22.22** | Installés, inutilisés dans cette session |
| **`git` sur dépôts publics** | **Un substitut au temps 2 que le document n'a pas vu** : l'effort investi, les licences, les corpus d'évaluation et les chiffres de référence des modèles libres se mesurent sans parler à aucun commercial |

## 4. IA et produits existants qui font ce travail, et à quel prix

**Tous ces prix sont en cran C** — extraits de comparatifs, pages d'éditeurs inaccessibles depuis ce conteneur. Et aucun guichet d'accès n'est établi. **Ne fonder aucune décision là-dessus** : la règle 4.2 l'interdit.

| Qui | Organe couvert | Prix rapporté | Cran | Guichet |
|---|---|---|---|---|
| Revinate | Avis, réputation | ~4 $/chambre/mois, plancher ~399 $ ; aussi cité de 150 à 1 000 $+/établissement/mois | **C** | Inconnu |
| TrustYou | Avis, réputation | 75 à 350 $/établissement/mois, base citée à 100 $ | **C** | Inconnu |
| ReviewPro (Shiji) | Avis, réputation | Sur devis | **C** | Inconnu |
| Meltwater, Brandwatch, Talkwalker | Veille, presse, social | Non public, sans essai en libre-service | **C** | Inconnu ; guichet 4 avancé par le document en cran D |
| Postiz (AGPL-3.0) | **Publication multi-plateforme, 30+ plateformes** | Gratuit à installer soi-même | **B** (licence lue) | Guichet par plateforme, chacun à qualifier |
| trafilatura (Apache-2.0) | **Extraction** | Gratuit, F1 = 0,916 mesuré | **A-mesure** | Sans objet |
| OpenBao (MPL-2.0) | **Garde des accès confiés** | Gratuit à installer soi-même, 97,8 années-auteur en face | **B** | Sans objet |

**Ce que cette colonne dit, et c'est le nerf.** Le concurrent facture 75 à 350 $ par établissement et par mois pour l'organe Avis — celui que le document ne peut atteindre que par le guichet 2, et dont l'étalon est peut-être non mesurable (L11, cran C). Les organes que le document voulait reconstruire sont gratuits. **L'argent est du côté du guichet, jamais du côté du code.** La section 5 est une méthode d'ingénierie appliquée à un problème qui n'en est pas un.

## 5. Futurs possibles à douze mois — ⏳ non advenus, donc non décidables

- ⏳ **Un corpus annoté d'évaluation d'extraction pour le français d'outre-mer et les créoles.** Rien de tel n'existe à ma connaissance (cran D). S'il apparaît, le coût d'annotation de la section 3.2 s'effondre. Le constituer soi-même et le publier ferait de ce projet la référence de son domaine — et c'est une autre façon de vendre la provenance.
- ⏳ **Détection fiable du créole guadeloupéen distinguée du haïtien.** `gcf` est déjà dans les 142 classes de `py3langid` (A-usage) ; la confusion observée avec `ht` est un signal à n = 7. Douze mois de modèles multilingues peuvent la résoudre, ou pas. **Non décidable aujourd'hui.**
- ⏳ **Évolution des interfaces d'avis.** Le plafond de 5 avis (L11, cran C) peut bouger dans les deux sens. Le document a raison en 2.6 : un socle qui dépend d'une défense technique casse sans préavis. **Corollaire qu'il ne tire pas : un étalon qui dépend d'un plafond d'interface vieillit aussi vite.** Tout étalon doit porter sa date de validité, pas seulement sa date de mesure.
- ⏳ **Détourage et extraction par grand modèle de langage, à coût d'inférence en baisse.** Pourrait dépasser trafilatura sur les pages locales difficiles. À mesurer sur le même banc, jamais à supposer. Vigilance : une extraction par modèle fabrique du texte qui n'est pas dans la page — **incompatible en l'état avec l'organe Provenance**, qui est l'avantage du projet. Un gain d'extraction payé par une perte de provenance serait un mauvais échange.
- ⏳ **Un cadre européen d'accès aux données de plateformes.** Il pourrait ouvrir un septième guichet, ou élargir le guichet 3. Je n'ai aucune source primaire et la sortie réseau vers EUR-Lex est bloquée. **Cran D, piste de veille pour V1, jamais un fondement.**

---

*Fin de la critique. Aucun commit git effectué. Le document cible n'a pas été modifié.*
*Bancs rejouables conservés dans le répertoire de brouillon de session : `crawler.py` (47 lignes), `chaine.py` (64 lignes), scripts de mesure des dépôts et de calcul statistique.*
