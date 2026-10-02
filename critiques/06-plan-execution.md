# 06 — Le plan à l'épreuve de l'exécution

Lecteur adversarial, contexte vierge, angle **exécution**. 2 octobre 2026.
Mission : ne pas vérifier des faits, dérouler le plan et dire **où il casse**.
`/home/user/moteurs-et-outils/PLAN-DE-CONSTRUCTION.md` lu intégralement, non modifié.
`REGISTRE-DE-DEMARCHE.md` lu intégralement — aucune assertion marquée renversée n'est recrue ici.

**Verdict en une ligne.** Le socle tourne et ses chiffres sont exacts, mais il tourne **sur des pages qu'il a lui-même générées**. Dès qu'on le pointe sur les trois sources réelles que le plan a retenues, il rend **0 capture, 0 assertion, 0 %** — et il rend un rapport, et il sort avec le code 0. Le plan ordonne un calendrier par les approbations ; il ordonne mal, parce que le geste qu'il met en semaine 0 (« élargir l'accès réseau ») est précisément celui qui transforme une absence de collecte en **collecte sans base de licence**, le garde-fou que le plan annonce « inscrit dans le code » n'y étant pas.

---

## 0 — Mes lignes `D`, déclarées en tête, comme l'exige le barème

Trois, et seulement trois. Tout le reste de ce fichier porte soit une sortie collée, soit une adresse.

| Ligne `D` | Ce que j'avance de mémoire | Ce qui la lèverait |
|---|---|---|
| `D·4` | Que les portails `bodacc-datadila.opendatasoft.com`, `data.economie.gouv.fr` et `meteo.data.gouv.fr` servent une **coquille d'application monopage** et exposent leurs données par une **interface REST JSON** paginée. Je le sais d'usage, je n'ai pas pu ouvrir un seul de ces hôtes : refusés par la politique réseau, lignes 27-28 et 45 de mon journal | Un `curl` sur chacun depuis un poste au réseau ouvert. Dix minutes |
| `D·4` | Qu'un hébergement mutualisé ou une machine virtuelle à bas coût est aujourd'hui couramment en **ARM**, ce qui rendrait inutilisables les quatre roues binaires `cp311-x86_64` du versement au dépôt | Un `uname -m` sur la machine cible. Trente secondes |
| `D·4` | Que le délai réel entre dépôt d'un dossier d'approbation et réponse dépasse souvent les 14 jours annoncés, par allers-retours de refus. Le plan écrit déjà « délai inconnu ⏳ » ; je ne prétends pas mieux, je dis seulement que le **nombre d'itérations** est le vrai coût, pas le délai d'un tour | Le premier dossier déposé. C'est la mesure, et elle est gratuite |

**Et je m'applique la règle de rétrogradation.** Trois blocs de ce fichier reposent sur des exigences de plateforme (Google, LinkedIn, Meta) dont **je n'ai pas pu ouvrir une seule page primaire** : `developers.google.com`, `learn.microsoft.com` et `developers.facebook.com` sont refusés par le réseau (journal, lignes 23, 40, 41 et 22). Je ne peux donc produire ni adresse consultée ni date de consultation pour ces exigences. Elles **ne sont pas** en `B`. Je les classe en **`C·2`** — secondaire, attesté par plusieurs résumés concordants — et elles **n'engagent aucune dépense avant d'être relues sur la page primaire**. Je le dis ici pour que le comptage ne me prenne pas en flagrant délit : dans tout ce fichier, **zéro ligne `B` ou `A` ne s'appuie sur une page web**. Mes `A` sont tous des sorties de commandes locales, collées.

---

## 1 — La semaine 0 et la phase 1, déroulées geste par geste

Le plan donne cinq gestes en semaine 0 et six « travaux » en phase 1. Je les prends dans l'ordre, et pour chacun j'écris **ce qu'il faut réellement faire** et **ce qui manque pour le faire**.

### Semaine 0, geste 1 — « Déposer les dossiers d'approbation sur chaque plateforme sociale visée »

Ce que le plan suppose : qu'on s'assoie et qu'on dépose. Ce qu'il faut réellement faire, dans cet ordre, parce que chaque étape est la condition de la suivante :

1. **Avoir une personne morale immatriculée.** Pas « être développeur ». Les exigences lues (`C·2`) réservent l'accès de gestion de communauté aux entités légalement enregistrées, et la vérification d'entreprise demande un extrait d'immatriculation, une licence ou un document fiscal au nom de la société.
2. **Avoir un nom de domaine et un site en ligne**, dont le domaine corresponde à l'adresse de courriel professionnelle déposée.
3. **Avoir une politique de confidentialité publiée** à une adresse atteignable, et conforme — ce qui veut dire, pour ce projet, avoir déjà tranché la chaîne RGPD que `01-juridique.md` a instruite sur des centaines de lignes et que **le plan ne mentionne pas une fois** (compté : 0 occurrence de « RGPD », journal ligne 44).
4. **Avoir une page d'entreprise vérifiée** sur la plateforme concernée, et un administrateur principal de cette page qui atteste l'application.
5. **Décrire un cas d'usage précis** — un cas d'usage vague est un motif de refus connu.
6. Pour le palier supérieur : **une vidéo d'écran** démontrant toutes les fonctions essentielles. Ce qui suppose un produit qui fonctionne, sur un vrai compte, pour un vrai établissement.

**La dépendance non écrite, et c'est la première tâche qui bloque le plan.** Le geste 1 de la semaine 0 est **le dernier** de cette liste, pas le premier. Il exige, en amont : une société immatriculée, un domaine, un site en ligne, une politique de confidentialité, une page d'entreprise vérifiée, et pour le palier utile, une démonstration filmée. Le plan n'en nomme **aucun**. Il ouvre sur « À engager immédiatement, avant toute ligne de code. Trois des quatre sont gratuites » — et le geste gratuit en question est, en réalité, bloqué par la création d'une entreprise que le plan n'évoque jamais.

Ce n'est pas un détail d'ordonnancement. Le plan tout entier est construit sur une thèse : *« Le code n'est pas le coût. L'approbation l'est. »* Si l'approbation est elle-même bloquée par une pile administrative non écrite, alors la thèse est juste et le plan est **faux sur son propre terrain** : le chemin critique ne commence pas au dépôt du dossier, il commence au greffe.

Nuance que je dois à l'honnêteté : **Mastodon ne demande rien de tout cela.** Une application s'y enregistre en quelques minutes sur n'importe quelle instance. Des trois plateformes de `publier.py`, une est immédiatement ouverte. Le plan aurait pu le dire et en tirer un ordre d'attaque ; il traite les trois comme un bloc homogène.

### Semaine 0, geste 2 — « Tester l'accès aux avis Google »

Le registre en fait la question la plus coûteuse du projet : « Si cet accès est cassé, le volet avis n'a aucune plateforme praticable », en `C·3` sur trois témoignages de forum.

**Je l'ai partiellement testé, gratuitement, et le résultat déplace la question.** L'hôte n'est pas refusé par le réseau de cet environnement, contrairement à `developers.google.com`. Sortie collée :

```
https://mybusiness.googleapis.com/v4/accounts/123/locations/456/reviews            HTTP 401
   {"error":{"code":401,"message":"Request is missing required authentication credential.
    Expected OAuth 2 access token, login cookie or other valid authentication credential."}}
https://mybusiness.googleapis.com/$discovery/rest?version=v4                       HTTP 404
   {"error":{"code":404,"message":"Method not found.","status":"NOT_FOUND"}}
https://mybusinessaccountmanagement.googleapis.com/v1/accounts                     HTTP 401
https://mybusinessbusinessinformation.googleapis.com/v1/categories                 HTTP 401
```

**Lecture.** Le point d'accès aux avis répond **401 « credential manquant »**, et non 404 ni `NOT_FOUND`. Il est routé, il est vivant, il réclame un jeton. Ce n'est donc **pas** un point d'accès supprimé. `A·2` — mesuré et rejouable, mais la portée est étroite et je la borne moi-même : un 401 prouve le routage et le défi d'authentification, **il ne prouve pas** qu'une application approuvée obtienne la liste des avis. Le quota par défaut est, d'après les exigences lues (`C·2`), **à zéro requête par minute** jusqu'à approbation manuelle.

**Conséquence sur le plan, et elle est structurelle.** Le plan distingue deux natures de risque : la phase 3 attend « les approbations déposées en semaine 0 », la phase 4 attend un accès « douteux ». La mesure dit que c'est **le même obstacle** : une demande d'approbation d'application, avec quota à zéro avant feu vert. Le volet avis n'est pas bloqué par une porte murée, il est bloqué par **la même file d'attente** que le volet publication. Donc le geste 2 de la semaine 0, tel qu'il est écrit — « un compte, une heure » — ne répond pas à la question qu'il prétend trancher : avec un compte et une heure on obtient un 401, ce que j'ai obtenu en douze secondes sans compte. La question ne se tranche qu'**après approbation**, c'est-à-dire après la société, le site et la politique de confidentialité. Le geste 2 dépend du geste 1, et le plan les présente comme indépendants.

### Semaine 0, geste 3 — « Question au bâtonnier de Guadeloupe »

Rien à casser sur le fond : quatre points rédigés, gratuit, utile. Deux manques d'exécution :

- **Sous quelle signature ?** Une question de déontologie posée par un prestataire anonyme n'a pas le même sort qu'une question posée par une société identifiée qui annonce un service. Encore la dépendance au geste 1.
- `barreau-guadeloupe.avocat.fr` est **refusé par le réseau** de cet environnement (journal, ligne 31). L'adresse de dépôt de la question n'est donc pas vérifiable d'ici. Ligne du journal, pas un aveu.

### Semaine 0, geste 4 — « Élargir l'accès réseau de l'environnement »

**C'est le geste le plus dangereux du plan, et il est présenté comme « un réglage ».** Démonstration, en trois sorties collées.

Aujourd'hui, réseau fermé, la séquence d'installation du README appliquée au vrai fichier de sources :

```
source 1 — BODACC — annonces civiles et commerciales
  robots.txt illisible (<urlopen error Tunnel connection failed: 403 Forbidden>) — collecte refusee par prudence
  0 capture(s) neuve(s)
[… idem sources 2, 3, 4 …]
0 capture(s) en 1.3s  (0.0 doc/s)
```

Le refus vient de l'**impossibilité de lire `robots.txt`**, pas d'une règle de licence. Or `sources.json` déclare lui-même, en tête :

> « Chaque ligne `licence_lue_le` est a null tant que la page du jeu n'a pas ete ouverte. **LE COLLECTEUR NE DOIT PAS TOURNER SUR UNE SOURCE DONT `licence_lue_le` EST NULL.** »

Et le plan reprend cette règle comme une propriété du produit, en gras : « **Règle inscrite dans le code : ne pas collecter une source dont la licence n'a pas été lue** ».

**Elle n'est pas dans le code.** La sélection des sources du collecteur, `socle.py` ligne 207 :

```python
for s in c.execute("""SELECT id,nom,url_base,debit_max_rps FROM source
                      WHERE actif=1 AND verdict<>'ecarte'""").fetchall():
```

`licence_lue_le` n'est ni dans ce prédicat, ni dans aucune contrainte `CHECK` du schéma (les 14 `CHECK` de `schema.sql` relevés, aucun ne porte sur la licence). Épreuve directe : j'ai mis la source du banc en `licence_lue_le = NULL`, licence `non declaree`, guichet `5b`, et relancé.

```
source passee en LICENCE NON LUE / guichet 5b : ('Banc local de demonstration', '5b', 'non declaree', None, 'retenu')
=== COLLECTE SUR UNE SOURCE DONT LA LICENCE N EST PAS LUE ===
source 1 — Banc local de demonstration
  12 capture(s) neuve(s)

12 capture(s) en 4.7s  (2.6 doc/s)
21 assertion(s) creee(s)
=== Etalons de provenance ===
  assertions                                   : 21
  remontees a une source primaire              : 21/21 = 100.0 %
  datees                                       : 21/21 = 100.0 %
  rejouables a l'identique (sha256 + archive)  : 21/21 = 100.0 %
```

`A·1`. Douze captures et vingt et une assertions sur une source sans licence lue, en guichet 5b — et **les trois étalons de provenance affichent 100 %**. L'auto-audit du rapport n'audite pas la base juridique : il audite l'empreinte. Un rapport peut donc être parfaitement « prouvé » et reposer sur rien.

**Le défaut d'ordonnancement, nommé.** Aujourd'hui, le projet est protégé par un accident : le réseau est fermé. Le geste 4 de la semaine 0 lève cet accident **avant** que le garde-fou existe. Le premier `python3 socle.py collecte` lancé après l'élargissement du réseau collectera les quatre sources, dont celle que `sources.json` qualifie lui-même de « **CONTRE-EXEMPLE VOLONTAIRE** » en guichet 5b — le préfecture de Guadeloupe, sans licence déclarée. C'est exactement la configuration que le registre a marquée **renversée** : « Les conditions du degré 5b protègent le collecteur » → renversé, « citer, résumer, lier a été jugé extraction prohibée, et le but poursuivi importe peu ». Le plan ne recroit pas l'assertion renversée dans son texte ; **son code la rejouera**.

Correctif, et il coûte une ligne : `AND licence_lue_le IS NOT NULL` dans le `SELECT`, ou un déclencheur SQL comme pour la relecture humaine. Que ce ne soit pas déjà fait, alors que le même socle sait refuser une publication IA non relue **par le schéma**, est l'incohérence la plus parlante du lot : la règle qu'on tenait à démontrer est tenue par le schéma, la règle qu'on se contente d'annoncer ne l'est pas.

### Semaine 0, geste 5 — « Verser au dépôt les deux briques fragiles · une demi-journée »

Les deux briques ne sont pas nommées dans le plan. Elles le sont dans `critiques/05-technique.md` lignes 310-314 : **`trafilatura`, 1 mainteneur soutenu**, et **`py3langid`, 0 mainteneur soutenu, 3 commits sur 12 mois**. Ce sont, exactement, **les deux seules dépendances du socle**.

Ce que « verser au dépôt » exige réellement, mesuré :

```
=== poids reel du versement au depot ===
39M    .../wheels
19 fichiers
wheels binaires lies a CPython 3.11 / x86_64 : 4
  charset_normalizer-3.5.2-cp311-cp311-manylinux2014_x86_64…whl
  lxml-6.1.3-cp311-cp311-manylinux_2_26_x86_64…whl
  numpy-2.4.6-cp311-cp311-manylinux_2_27_x86_64…whl
  regex-2026.9.29-cp311-cp311-manylinux2014_x86_64…whl
```

`A·1`. Ce ne sont pas deux briques, c'est **19 paquets et 39 Mo**, dont `numpy` (tiré par `py3langid`), `lxml`, `regex` et `charset-normalizer` en **roues binaires compilées, verrouillées à CPython 3.11 et x86_64**. Le versement au dépôt, tel qu'il est écrit, fige donc aussi l'architecture et la version mineure de Python du serveur de production. Et il n'existe **aucun** fichier de verrouillage dans le socle :

```
=== pin de dependance dans tout le socle ? ===
AUCUN fichier de verrouillage de dependances
```

Pire, une version est **écrite en dur** au lieu d'être lue du paquet, `socle.py` ligne 162 :

```python
hashlib.sha256(txt.encode()).hexdigest(), lg, marge, "py3langid 0.4.0"))
```

À la première montée de `py3langid`, la base enregistrera silencieusement une version fausse dans le champ qui sert à prouver la reproductibilité. `A·1`.

**Et c'est ici que le plan se contredit.** Il affirme en ouverture de phase 1 que le socle est « **rejouable à un an sans réseau — `A·1`** ». Cette propriété **dépend** du geste 5 qu'il range en semaine 0 comme une précaution. Épreuve : j'ai rejoué la base avec `trafilatura` absent de l'environnement.

```
=== REJEU SANS trafilatura INSTALLE (poste neuf, sans reseau) ===
=== Rejeu de 21 assertion(s) ===
  archive     : 21/21 = 100.0 %
  extraction  : 0/21 = 0.0 %
  citation    : 0/21 = 0.0 %
  PROUVEES    : 0/21 = 0.0 %
```

`A·1`. **Zéro assertion prouvée.** Ce qui est réellement rejouable à un an sans réseau, c'est **l'archive** — 21/21, et c'est solide, le nom du fichier est son empreinte. Les deux autres contrôles exigent `trafilatura 2.3.0` présent, donc soit le réseau, soit un versement au dépôt qui n'existe pas. La formule juste serait : « archive rejouable sans réseau `A·1` ; extraction et citation rejouables **sous réserve** du versement au dépôt, non fait ». Le plan vend les trois pour le prix de l'un.

Honnêteté sur une épreuve que j'ai tentée et qui n'a **rien** donné : j'ai simulé une montée de version de `trafilatura` (2.5.1) avec une sortie légèrement différente, pour voir si l'extraction divergeait. Elle n'a pas divergé, 21/21. Une montée de version **ne casse donc pas automatiquement** le rejeu. Je ne peux pas affirmer qu'elle le casserait ; je peux affirmer que l'absence du paquet le casse entièrement.

### Phase 1, travaux — « Trois sources en accès ouvert déclaré »

Deux écarts de comptage et un blocage dur.

**Comptage.** Le plan dit trois sources. `sources.json` en retient **quatre**, dont la préfecture en guichet 5b, et en écarte une (la presse). La quatrième est le contre-exemple volontaire. Un plan qui dit « trois » et un fichier qui en active quatre, dont une sans licence, est un écart qui se paiera à la première collecte réelle.

**Le blocage dur, et c'est le second grand point de rupture.** Les trois sources de guichet 6 ont pour `url_base` **la page d'accueil du portail** :

```
BODACC    → https://bodacc-datadila.opendatasoft.com/
DECP      → https://data.economie.gouv.fr/
Vigilance → https://meteo.data.gouv.fr/
```

Et le collecteur est un **explorateur HTML en largeur** : il part de `url_base`, extrait les liens par expression régulière `href=`, en suit jusqu'à 30 par page sur le même hôte, et passe chaque corps à `trafilatura.extract` pour en tirer de la prose, puis découpe cette prose en phrases pour fabriquer les assertions. Épreuve collée :

```
extraction trafilatura sur du JSON  -> None
extraction sur une coquille SPA     -> None
liens trouves dans la coquille SPA  -> []
```

`A·1` sur le comportement de la chaîne. **Donc, même réseau grand ouvert** : sur un enregistrement BODACC servi en JSON par une interface Opendatasoft, l'extraction rend `None`, aucune assertion n'est créée ; sur une coquille d'application monopage, l'extraction rend `None` **et** l'explorateur ne trouve aucun lien à suivre, donc la collecte s'arrête à la page d'accueil. Que ces trois portails soient effectivement en monopage avec interface JSON est ma ligne `D·4` déclarée en tête — mais le point qui compte ne dépend pas d'elle : **le socle n'a aucun chemin de code pour une source JSON**, ni table pour un enregistrement structuré. Sa table `extraction` est bâtie sur `outil`/`texte`/offsets de prose, et sa fabrication d'assertions sur « une assertion par phrase porteuse ». Une annonce BODACC n'est pas une phrase, c'est un enregistrement à champs.

**La dépendance non écrite, deuxième du nom.** Le plan exige « quatre semaines de données réelles **filtrées Guadeloupe** ». Il n'existe dans le socle **ni adaptateur d'interface JSON, ni pagination, ni cartographie de champs, ni filtre départemental 971**. Rien dans les 326 lignes ne sait dire « seulement le département 971 ». Et le code ne suit **pas les redirections** — `http()` ne lit jamais l'entête `Location`, et `url_finale` reçoit toujours l'URL demandée, ce qui fait de ce champ de provenance une valeur fausse par construction dès qu'un portail redirige, ce que font la quasi-totalité des portails publics.

Le test « gratuit, deux à trois jours » qui doit **décider du projet dans les deux sens** n'est donc pas exécutable avec ce socle. Ce n'est pas un réglage de débit : c'est un connecteur par jeu de données, plus une seconde forme d'assertion pour des enregistrements structurés, plus un filtre géographique. Et comme le plan refuse tout chiffrage en jours, il n'a aucun endroit où inscrire ce travail.

### Phase 1, travaux — les trois autres lignes

- **« Le rapport hebdomadaire, format arrêté »** — traité en section 4 ci-dessous : il n'est pas arrêté, et dans son état actuel il contient une violation de licence.
- **« Le pont translingue reste ouvert ⏳ »** — honnête, marqué en attente. Rien à casser.
- **« Interdiction absolue : dépouiller les accents »** — celle-là **est** tenue par le code. `CHECK (langue_avant_normalisation = 1)` ligne 139 du schéma, et l'index déclaré sans `remove_diacritics`. Vérifié, `A·1`. Je le signale parce que c'est l'exemple de ce que le plan sait faire quand il le veut : une règle portée par le schéma, pas par une phrase. Le contraste avec la règle de licence n'en est que plus net.

---

## 2 — Les tâches sous-estimées d'un facteur trois

J'en prends trois, celles que le plan présente comme légères.

### A — « Déposer les dossiers d'approbation · Gratuit » → ce n'est pas gratuit, c'est le chemin critique entier

Le plan le classe « Gratuit, délai inconnu ⏳ ». Le coût monétaire est peut-être nul ; le coût d'exécution est une pile de prérequis, chacun bloquant :

| Prérequis réel | Déjà prévu au plan ? |
|---|---|
| Personne morale immatriculée (document d'immatriculation, licence ou document fiscal) | **non — 0 occurrence** |
| Nom de domaine, site en ligne, courriel professionnel sur le même domaine | **non — 0 occurrence** |
| Politique de confidentialité publiée | **non** |
| Page d'entreprise vérifiée + attestation par un administrateur principal | **non** |
| Cas d'usage écrit, précis (le vague est un motif de refus connu) | non |
| Vidéo d'écran démontrant les fonctions essentielles, pour le palier utile | **non** |
| Quota par défaut à **zéro** avant approbation côté Google | non |

`C·2`, et je l'assume comme tel : exigences concordantes de plusieurs résumés secondaires, **pages primaires refusées par le réseau** (`developers.google.com`, `learn.microsoft.com`, `developers.facebook.com` — journal lignes 23, 40, 41, 22). Pas d'adresse consultée, donc pas de `B`. Cela reste une piste, elle n'engage aucune dépense — mais elle suffit à établir que la case « gratuit » du tableau de la semaine 0 est trompeuse sur ce qu'elle demande, et le facteur trois est prudent. On ne dépose pas un dossier en une après-midi : on constitue une entreprise, un site et une démonstration, puis on dépose, puis on itère sur les refus.

**Et une conséquence que le plan ne voit pas.** La vidéo de démonstration demande de montrer le produit en marche sur un vrai établissement. Or la phase 3 « n'attend pas du développement, elle attend les approbations ». Il y a donc une boucle : l'approbation demande une démonstration, la démonstration demande un produit en service, le produit en service attend l'approbation. On la casse par le palier de développement, qui s'obtient avec moins — mais il faut le savoir et le dire, et le plan ne distingue pas les deux paliers.

### B — « La lecture des licences source par source » → ce n'est pas une lecture, c'est une qualification juridique par jeu

Le plan la range parmi les trois postes incompressibles, ce qui est juste. Il la décrit comme une lecture. Ce qu'elle est réellement, pour **une seule** source, d'après ce que le socle lui-même demande comme champs : `guichet`, `licence_spdx`, `licence_lue_le`, `attribution_texte`, `cgu_url`, `cgu_lues_le`, `verdict`, `motif_verdict`, `debit_max_rps`, `robots_lu_le`.

Ce qui veut dire, par jeu de données : ouvrir la page du jeu, relever la licence **attachée à ce jeu** (le registre l'établit : le texte de la Licence Ouverte 2.0 est lu en `B`, son **attachement** à chaque jeu est en cran `D`) ; lire les conditions générales du portail, qui sont distinctes de la licence ; relever `robots.txt` **et** son `Crawl-delay`, que le collecteur ne lit pas aujourd'hui ; rédiger la chaîne d'attribution exacte, qui doit porter le nom du concédant **et la date de dernière mise à jour du jeu** ; et consigner un verdict motivé. Pour la préfecture en 5b, il faut en plus lire les mentions légales et requalifier.

Le facteur trois est là : le plan compte une lecture de licence, il faut compter **une fiche de qualification par jeu**, avec quatre documents à ouvrir et une chaîne d'attribution à rédiger. Et ce travail est le **seul** qui débloque la collecte si l'on corrige le garde-fou manquant — il passe donc du statut de tâche de fond au statut de chemin critique.

### C — « Le rapport hebdomadaire, format arrêté » → il n'est pas arrêté, et il porte une violation de licence

Mesuré en section 4. Je le compte ici parce que le plan le traite comme une ligne de travaux parmi six, alors qu'il porte le livrable. Facteur trois au minimum : il manque la variante « semaine vide », la mention légale, la chaîne d'attribution réelle, et la différence entre un rapport et une liste.

**Je ne retiens pas** « la mise en service chez un premier client » comme sous-estimée d'un facteur trois, bien qu'elle le soit sans doute, parce que le README le dit déjà lui-même et honnêtement : « Elles mesurent l'installation du logiciel, pas la mise en service chez un client. […] la mise en service est un travail de lecture, pas de code. » On ne casse pas un aveu. Je le porte en section 4 sous un autre angle : non pas ce qu'elle coûte, mais ce qu'elle exige **qui n'existe nulle part**.

---

## 3 — Installation et exécution du socle : ce que j'ai mesuré moi-même

Environnement : conteneur Linux 6.18.44, Python 3.11.15, SQLite 3.45.1 avec FTS5, Node 22.22, Docker, `psql`, `git`, `curl`, `jq`. `trafilatura 2.3.0`, `py3langid 0.4.0`, `lxml 6.1.3` **déjà présents** — je n'ai donc pas chronométré le `pip install`, exactement comme le README qui précise « dépendances déjà en cache ». Copie du socle dans un répertoire de travail, base et archives supprimées, état de départ propre. Le socle d'origine n'a **pas** été modifié.

### 3.1 — La séquence d'installation du README, littéralement, sur le vrai fichier de sources

```
=== T0 === 20:27:58
base creee : …/socle.db
objets de schema : 24
--- rc init=0
 id guichet  licence          verdict                nom
  1 6        etalab-2.0       retenu_sous_conditions BODACC — annonces civiles et commerciales
  2 6        etalab-2.0       retenu_sous_conditions DECP — donnees essentielles des marches publics
  3 6        etalab-2.0       retenu_sous_conditions Meteo-France donnees ouvertes — vigilance
  4 5b       non declaree     retenu_sous_conditions Recueil des actes administratifs — prefecture de Guadeloupe
sources retenues : 4  ecartees : 1
--- rc sources=0
source 1 — BODACC …
  robots.txt illisible (<urlopen error Tunnel connection failed: 403 Forbidden>) — collecte refusee par prudence
  0 capture(s) neuve(s)
[… sources 2, 3, 4 : idem …]
0 capture(s) en 1.3s  (0.0 doc/s)
--- rc collecte=0
0 assertion(s) creee(s)
--- rc assertions=0
rapport ecrit : …/rapport-2026-S40.md  (0 assertion(s), 1544 octets)
--- rc rapport=0
=== Etalons de provenance ===
  assertions                                   : 0
  remontees a une source primaire              : 0/0 = 0.0 %
  datees                                       : 0/0 = 0.0 %
  rejouables a l'identique (sha256 + archive)  : 0/0 = 0.0 %
--- rc etalons=0

real    0m2.161s
```

`A·1`. **La séquence d'installation du README, suivie à la lettre, produit un socle vide et rend 0 % sur les trois étalons** — et rend le code de sortie 0 à chacune des six étapes. Le plan et le README affichent tous deux « 21 assertions sur 21 prouvées » comme une propriété du socle. Ce n'en est pas une : c'est une propriété du **banc**.

### 3.2 — Le banc de démonstration, chronométré

Le banc est donné dans une section secondaire du README (« Pour voir la chaîne tourner sans accès réseau sortant »). C'est pourtant **le seul chemin qui reproduit les chiffres annoncés**.

```
banc ecrit … : 8 articles en 4 langues, 1 flux, 1 robots.txt, 1 page interdite  (13 entrees)
langues : en, es, fr, gcf
 id guichet  licence          verdict  nom
  1 6        CC0-1.0          retenu   Banc local de demonstration
sources retenues : 1  ecartees : 0
source 1 — Banc local de demonstration
  12 capture(s) neuve(s)
12 capture(s) en 5.5s  (2.2 doc/s)
21 assertion(s) creee(s)
rapport ecrit : …/rapport-2026-S40.md  (21 assertion(s), 8405 octets)
=== Etalons de provenance ===
  assertions                                   : 21
  remontees a une source primaire              : 21/21 = 100.0 %
  datees                                       : 21/21 = 100.0 %
  rejouables a l'identique (sha256 + archive)  : 21/21 = 100.0 %
=== Langues detectees (sur texte accentue, jamais normalise) ===
  fr    :     6 document(s)   marge moyenne au 2e candidat 242.6
  en    :     2 document(s)   marge moyenne au 2e candidat 99.0
  gcf   :     2 document(s)   marge moyenne au 2e candidat 143.9
  es    :     1 document(s)   marge moyenne au 2e candidat 114.8
  archives conservees : 12 fichier(s), 0.02 Mo d'original
=== TEMPS TOTAL MESURE : 7.609 s (dont 1 s de sleep) ===
```

Et le rejeu :

```
=== Rejeu de 21 assertion(s) ===
  archive     : 21/21 = 100.0 %
  extraction  : 21/21 = 100.0 %
  citation    : 21/21 = 100.0 %
  PROUVEES    : 21/21 = 100.0 %
```

**Les chiffres du plan sont exacts.** 7,6 s mesurées dont 1 s d'attente volontaire pour le serveur local, soit 6,6 s nettes contre 7,1 s annoncées ; 21 assertions sur 21 prouvées, les trois contrôles indépendants à 100 % ; comptage des lignes non vides **1 183 exactement**, fichier par fichier. Le socle tourne du premier coup, sans incident. `A·1`, et je ne le minore pas : c'est du travail propre, et la détection du `gcf` à 2 documents sur 2 avec une marge de 143,9 au second candidat est réelle.

**Mais la portée est celle d'un banc synthétique.** Les 8 articles ont été écrits par `banc/generer.py`, 128 lignes du même dépôt. Le socle se mesure sur des pages qu'il a lui-même fabriquées : prose propre, encodage maîtrisé, `robots.txt` complaisant, zéro JavaScript, zéro défense anti-robot, zéro redirection. Le README le dit en section 7, à son crédit. Le plan, lui, reprend les chiffres **sans l'astérisque** et les met au service d'une affirmation qui ne s'en déduit pas : « **Pourquoi ce socle est inattaquable** ». Un socle mesuré contre son propre banc n'est pas inattaquable, il est **non éprouvé**.

### 3.3 — L'orchestrateur de publication, et le 403 fondateur du plan

```
publication 1 creee sur mastodon (25/500 car.) statut=brouillon assertions=[1, 2]
publication 3 creee sur linkedin (8/3000 car.) statut=a_relire (generee par IA) assertions=[]
--- programmer le contenu IA sans relecture ---
REFUSE par le schema : contenu genere par IA : relecture humaine nommee obligatoire avant envoi
rc=1
publication 1 programmee  local 2026-10-02 10:00 (UTC-4)  =  UTC 2026-10-02T14:00Z
  1 mastodon  ENVOYE   http=201 distant=dist-1000
  2 facebook  ENVOYE   http=201 distant=dist-1001
  3 linkedin  ECHEC    http=403 {"error":"application non approuvee par la plateforme"}
  taux de publication reussie : 2/3 = 66.7 %
  contenus IA envoyes sans relecture nommee (doit valoir 0) : 0
  contenus IA envoyes sans mention affichee (doit valoir 0) : 0
=== Journal des acces confies ===
=== Secrets presents dans la base du socle ===
  table acces_confie : 0 reference(s) de coffre, 0 secret
```

Deux choses à reten, et la seconde est lourde.

**Le refus du contenu IA non relu est réel et vient bien du schéma**, code de sortie 1. Reproduit. `A·1`. C'est la plus belle pièce du socle.

**Le 403 ne mesure rien.** Le plan ouvre sur lui, en section 0, comme sur son principe fondateur : *« Mesuré : `A·1`. Un orchestrateur de publication écrit et exécuté, deux envois réussis, le troisième refusé en 403 — application non approuvée. »* Voici d'où vient ce 403, intégralement, `banc/bouchon_plateformes.py` :

```python
"""Bouchon des interfaces de plateformes, pour faire tourner publier.py
sans acces reseau sortant. Accepte /mastodon et /facebook, refuse /linkedin
pour qu'un echec reel soit mesure."""
…
        if self.path.startswith('/linkedin'):
            self.send_response(403); …
            self.wfile.write(b'{"error":"application non approuvee par la plateforme"}'); return
```

**Dix-sept lignes écrites par le projet, qui refusent `/linkedin` en dur, pour « qu'un échec réel soit mesuré ».** L'échec n'est pas réel : il est fabriqué. On mesure le bouchon, et le bouchon rend ce qu'on lui a dit de rendre. Le « taux de publication réussie : 2/3 = 66,7 % » est le quotient de deux constantes choisies par l'auteur.

Je sépare soigneusement deux choses, parce que l'enjeu n'est pas de railler. **La conclusion est très probablement vraie** : les plateformes exigent bien une approbation d'application, et un appel non approuvé est bien rejeté. Mais cette vérité est de provenance **secondaire ou primaire documentaire**, pas mesurée — au mieux `C·2` dans l'état de mon accès, `B·2` si quelqu'un ouvre les pages primaires et les date. Le plan la classe `A·1`, et le registre dit que `1` et `2` « portent une décision ». Le plan a donc **ordonné tout son calendrier — « administratif d'abord, technique ensuite » — sur une mesure circulaire**. L'ordre reste probablement le bon ; le fondement affiché ne le tient pas. Reclassement proposé : la thèse « le code n'est pas le coût, l'approbation l'est » passe en `C·2`, à monter en `A·1` par la seule épreuve qui la mesurerait vraiment — **un vrai appel à une vraie plateforme avec une application non approuvée**, qui coûte zéro euro et une heure, et que personne n'a faite.

**Et un défaut de reproductibilité du README.** Le README affiche une sortie de journal des accès confiés :

```
=== Journal des acces confies ===
  2026-10-02T19:44:34Z  mastodon  publication  accorde   par publier 1.0
```

Mon installation propre rend ce bloc **vide**. Raison, vérifiée : aucune sous-commande de `publier.py` ne crée de ligne dans `acces_confie` (les sous-commandes sont `ajouter`, `relire`, `programmer`, `envoyer`, `file`, `bilan`), et `coffre_lire()` n'est appelée que `if acces_id`, donc jamais. La base livrée dans le dépôt contient pourtant trois lignes :

```
(1, 1, 'mastodon', 'coffre://clients/1/mastodon', 'publication seule…', '2026-10-01', 'mandat-2026-001.pdf', None)
(2, 1, 'facebook', 'coffre://clients/1/facebook', …)
(3, 1, 'linkedin', 'coffre://clients/1/linkedin', …)
```

Insérées à la main, hors de tout chemin de code, et référençant un mandat `mandat-2026-001.pdf` qui **n'existe nulle part sur le disque** (`find -iname "*mandat*"` : aucun résultat). Conséquence d'exécution : l'organe « garde des accès confiés », que le registre range parmi les acquis mesurés (« révocation en 123 ms », « journal haché »), **n'est traversé par aucun chemin de code du socle**. La sortie du README qui le montre n'est pas rejouable depuis une installation propre. `A·1`. Reclassement : la ligne du plan sur le journal d'accès passe de `A·1` à `A·3` — mesuré, mais sur un état de base fabriqué à la main, non reproductible.

Le garde-fou de secret, lui, **est** réel : `CHECK (reference_coffre LIKE 'coffre://%')` et trois `CHECK` de rejet de motifs de secret, vérifiés dans le schéma. `A·1`.

---

## 4 — La phase 1 est-elle livrable sans les phases suivantes ? Ce qu'un client reçoit le premier lundi

Le plan l'affirme : « Le seul produit vendable **sans attendre personne** ». Je déroule littéralement le premier lundi.

### Ce qui arrive, dans l'état du socle, si la semaine a été mauvaise

Fichier intégral, 1 544 octets, produit par `python3 socle.py rapport --jours 7` avec les vraies sources et le réseau tel qu'il est :

```markdown
# Rapport de veille — semaine 2026-S40

Client : client-zero · Fuseau : America/Guadeloupe (UTC-4, sans heure d'été)
Période : 7 derniers jours · Édité le 2026-10-02T20:30:19Z
Produit par : socle 1.0

**Comment lire ce rapport.** Chaque assertion porte son URL, la date et l'heure UTC de sa
captation, et les 16 premiers caractères de l'empreinte SHA-256 […]

**Aucune ligne de ce rapport n'est générée par un modèle de langage.** […]

---

## Contrôle de provenance de ce rapport

| Étalon | Valeur |
|---|---|
| Assertions dans la base | 0 |
| Part remontée à une source primaire | 0.0 % |
| Part datée | 0.0 % |
| Part rejouable à l'identique | 0.0 % |
| Assertions générées par IA | 0 |

## Sources mobilisées et leurs licences

| Source | Guichet | Licence | Licence lue le | Attribution |
|---|---|---|---|---|
| BODACC — annonces civiles et commerciales | 6 | etalab-2.0 | non lue | Source : DILA / BODACC — derniere mise a jour : <date du jeu> |
| DECP — donnees essentielles des marches publics | 6 | etalab-2.0 | non lue | Source : ministere de l'Economie / DECP — derniere mise a jour : <date du jeu> |
| Meteo-France donnees ouvertes — vigilance | 6 | etalab-2.0 | non lue | Source : Meteo-France — derniere mise a jour : <date du jeu> |
| Recueil des actes administratifs — prefecture de Guadeloupe | 5b | non declaree | non lue |  |
```

`A·1`. Quatre choses, et la troisième est grave.

1. **Un client payant reçoit un document de zéro ligne utile**, dont l'auto-audit affiche fièrement 0,0 % trois fois, et le programme sort avec le code 0. Rien, nulle part, ne distingue « la semaine a été calme » de « le collecteur a été bloqué sept jours ». La supervision du produit n'existe pas : le plan n'a aucun geste de surveillance, et le socle aucun code de sortie non nul en cas de collecte vide.
2. La colonne « Licence lue le » affiche **« non lue »** pour les quatre sources. C'est à porter au crédit du format — il est honnête — mais c'est un aveu imprimé sur le livrable facturé.
3. **La chaîne d'attribution contient le gabarit non rempli `<date du jeu>`.** Or le plan met en première ligne de sa table des quatre obligations servies par la provenance : « Mentionner source et date de mise à jour, quel que soit le support — **Le champ existe, mesuré à 100 %** ». Le champ existe, en effet. **Son contenu est un trou.** La Licence Ouverte 2.0 exige le nom du concédant *et* la date de dernière mise à jour ; le livrable sort avec un marqueur de remplacement à la place de la date. L'obligation que le plan présente comme sa plus belle convergence est, dans l'artefact réel, **non tenue**. `A·1`, c'est dans le fichier produit.
4. Le rapport porte « Client : **client-zero** ». Il n'y a pas de nom de client parce qu'il n'y a pas de client, et aucune commande pour en créer un.

### Ce qui arrive si la semaine a été bonne : un produit, ou une liste ?

Le format non vide (celui du banc) est une **liste d'extraits verbatim groupés par source**, chaque ligne portant titre, langue, date de publication, URL, horodatage de captation et 16 caractères d'empreinte. C'est rigoureux. Ce n'est pas un produit de veille.

Ce qui manque pour que ce soit un produit, et qu'aucune phase du plan ne porte : un classement par **ce que ça change pour le client** (une liquidation d'un concurrent direct ne vaut pas une création à l'autre bout de l'île) ; un filtre de pertinence par secteur et par commune ; une suppression des doublons semaine après semaine ; et un seuil de rappel — le plan fixe lui-même « sous une dizaine de lignes utiles par semaine, ça ne se vend pas », mais le socle **ne sait pas compter les lignes utiles**, seulement les assertions. Le seuil d'abandon du plan n'a donc pas d'instrument.

### Tout ce qui manque entre « le code tourne » et « un client paie »

Je nomme, et j'indique à chaque fois si le plan en parle. Vérifié par comptage dans le plan (journal, ligne 44) : **`société` 0 · `statut` 0 · `SIRET` 0 · `facture` 0 · `facturation` 0 · `CGV` 0 · `conditions générales` 0 · `contrat` 0 · `paiement` 0 · `assurance` 0 · `RGPD` 0 · `sauvegarde` 0 · `SLA` 0 · `astreinte` 0 · `site` 0 · `web` 0 · `domaine` 0 · `hébergement` 0.** Et dans le socle : aucune occurrence de `cron`, `smtp`, `courriel`, `facture`, `paiement`.

| Manquant | Sans quoi | Au plan ? |
|---|---|---|
| **Une entité qui facture** — immatriculation, numéro, régime de TVA (la Guadeloupe a ses taux propres) | On ne peut pas émettre de facture valable | non |
| **Une facture conforme** — mentions obligatoires, numérotation continue, conservation | Toute recette est irrégulière | non |
| **Un moyen d'encaissement** — virement avec coordonnées bancaires, ou prélèvement, ou paiement en ligne | Un client qui dit oui ne peut pas payer | non |
| **Des conditions générales de vente** et un contrat d'abonnement : durée, préavis, prix, ce qui est promis et ce qui ne l'est pas | Un litige au premier rapport vide se règle sans écrit | non |
| **Un contrat de sous-traitance de données** et la chaîne RGPD que `01-juridique.md` a instruite (information des personnes, art. 14, exemption 14.5.b à sécuriser par un juriste, analyse d'impact) | Le volet avis est illégal, et la politique de confidentialité exigée par les plateformes est invérifiable | **non, 0 occurrence** |
| **Un site et un nom de domaine**, avec mentions légales et politique de confidentialité | Pas d'inscription possible, et le dossier d'approbation est refusé d'office | non |
| **Un envoi automatique** du rapport le lundi matin — ordonnanceur et courriel | Le rapport existe sur un disque et n'arrive chez personne. Le socle n'a **ni ordonnanceur ni envoi** | non — le README l'assume (« une tâche planifiée et un fichier Markdown suffisent »), mais la tâche n'existe pas |
| **Un serveur, et sa sauvegarde** des archives et de la base | Perdre `archives/` détruit la rejouabilité, donc le produit. Le plan chiffre le serveur (450-700 €/an) et ne dit pas un mot de la sauvegarde | non |
| **Un relevé des incidents et une conduite du dimanche soir** | Un rapport attendu lundi 8 h, cassé samedi, n'a personne. Le plan pose « qui maintient ? » comme une décision de fond et ne pose jamais la question de l'astreinte | la question « qui maintient » est posée, l'astreinte non |
| **Une création de client** dans l'outil | La table `client` existe, aucune commande ne la peuple ; le rapport dit « client-zero » | non |
| **Le deuxième client qui veut autre chose** | Le schéma cloisonne par client (bien vu), mais `sources.json` est **global** : un second client qui veut une source de plus l'impose au premier. Il n'y a pas de rattachement source↔client | non |
| **Une adresse de contact dans l'agent de collecte** | L'agent annoncé aux serveurs publics est `socle-gp/1.0 (…; contact: a-renseigner)`. Un portail public qui voit passer un robot sans contact le bloque, et c'est légitime | non |

**Réponse à la question posée.** Non. La phase 1 est **techniquement** indépendante des phases 2 à 4 — c'est vrai et c'est un bon acquis. Elle n'est pas **commercialement** livrable seule, parce qu'entre le code et l'euro il y a une douzaine de pièces dont le plan n'en nomme aucune. Et le plan ne peut pas se défendre en disant qu'elles sont hors sujet : il consacre une section entière à « Ce que ce plan refuse d'inscrire », il a donc un endroit pour dire qu'il les écarte volontairement. Il ne le dit pas. Elles sont absentes, pas écartées.

---

## 5 — Les trous : ce que le plan oublie entièrement

Au-delà de la liste ci-dessus, quatre oublis de nature différente.

**La sauvegarde, et elle est fatale.** Tout l'argument de vente est la rejouabilité par empreinte. La rejouabilité repose sur `archives/<2 car.>/<sha256>.gz`, sur un disque, sans copie. Un disque perdu ne détruit pas « des données » : il détruit **la preuve**, c'est-à-dire la seule chose que ce produit vend et qu'aucun concurrent ne vend. Le plan chiffre le serveur et pas sa sauvegarde. C'est le seul endroit où je dirais que le plan ne sous-estime pas : il **omet**.

**Le dimanche soir.** Le produit est hebdomadaire et son rendez-vous est le lundi. C'est le pire gabarit possible pour un service sans astreinte : la panne du samedi n'a pas de rattrapage, et le client découvre l'absence avant le prestataire. Le plan pose « qui maintient ? » comme la question que personne n'a posée — elle est bonne — et s'arrête avant la suivante : **qui répond, et dans quel délai ?** Sans engagement écrit, la réponse sera « quand je peux », et c'est une rupture de confiance au premier incident.

**Le deuxième client.** Le schéma cloisonne par `client` dès la première ligne, et le README a raison d'en être fier. Mais la **qualification des sources est globale** : un fichier `sources.json` unique, une table `source` sans rattachement client. Donc le deuxième client qui demande une source que le premier ne veut pas, ou un périmètre géographique différent, oblige soit à collecter pour tous, soit à réécrire le filtrage. Le cloisonnement a été mis à la bonne place pour les données et pas pour la **configuration**.

**Le RGPD, et c'est le trou le plus coûteux.** Zéro occurrence dans le plan, alors que `critiques/01-juridique.md` consacre une section entière (« M3 ») à établir que « **le projet ne survit pas sans une exemption nommée** » au titre de l'article 14, et qu'une analyse d'impact est probablement obligatoire. Un plan de construction qui ordonne quatre outils dont deux traitent des données nominatives (les avis portent des prénoms, les annonces BODACC portent des noms de dirigeants) et qui ne nomme pas une fois le régime applicable n'a pas oublié un détail : il a laissé dehors le travail que le projet avait déjà payé pour instruire.

---

## 6 — Classement de mes affirmations, ligne par ligne, après application de la règle de rétrogradation

| # | Affirmation | Couple | Fondement |
|---|---|---|---|
| 1 | La séquence d'installation du README, appliquée à `sources.json`, rend 0 capture, 0 assertion, 0 % sur les trois étalons, et sort en code 0 à chaque étape | `A·1` | Sortie collée §3.1 |
| 2 | Le banc reproduit les chiffres annoncés : 6,6 s nettes, 12 captures, 21 assertions, 21/21 aux trois contrôles, 1 183 lignes non vides exactement | `A·1` | Sorties collées §3.2 |
| 3 | La règle « ne pas collecter une source dont la licence n'a pas été lue » **n'est pas dans le code** : 12 captures et 21 assertions obtenues sur `licence_lue_le = NULL`, guichet 5b, avec étalons à 100 % | `A·1` | Épreuve collée §1, geste 4 |
| 4 | Sans `trafilatura` installé, le rejeu rend 0/21 prouvées ; archive seule tient à 21/21. Aucun fichier de verrouillage de dépendances n'existe | `A·1` | Sortie collée §1, geste 5 |
| 5 | Le « versement au dépôt » est 19 paquets, 39 Mo, dont 4 roues binaires verrouillées à CPython 3.11 / x86_64 | `A·1` | Sortie collée §1, geste 5 |
| 6 | `py3langid 0.4.0` est écrit en dur dans `socle.py` au lieu d'être lu du paquet | `A·1` | `socle.py` ligne 162 |
| 7 | Le 403 fondateur du plan vient d'un bouchon de 17 lignes du projet qui refuse `/linkedin` en dur. La mesure est circulaire | `A·1` | Code collé §3.3 |
| 8 | La thèse « le code n'est pas le coût, l'approbation l'est » est vraisemblablement juste, mais sa provenance n'est pas mesurée | `C·2` | Pages primaires refusées ; résumés concordants |
| 9 | Aucune sous-commande ne crée de ligne `acces_confie` ; le journal d'accès est vide sur installation propre ; les 3 lignes de la base livrée sont insérées à la main et citent un mandat absent du disque | `A·1` | §3.3, `find` sans résultat |
| 10 | Le refus de publication IA non relue vient bien du schéma, code de sortie 1. La contrainte de secret du coffre est réelle | `A·1` | Sortie collée §3.3 |
| 11 | `trafilatura.extract` rend `None` sur un enregistrement JSON et sur une coquille monopage ; l'extracteur de liens par expression régulière rend `[]` sur une coquille monopage. Le socle n'a aucun chemin de code pour une source JSON, ni filtre départemental, ni suivi de redirection | `A·1` | Épreuve collée §1, phase 1 |
| 12 | Que les trois portails retenus soient effectivement en monopage avec interface JSON | `D·4` | Déclarée en tête. Hôtes refusés |
| 13 | Le rapport d'une semaine vide est livré avec 0,0 % × 3 et code de sortie 0, sans rien qui distingue une semaine calme d'une collecte cassée | `A·1` | Fichier collé §4 |
| 14 | La chaîne d'attribution du livrable contient le gabarit non rempli `<date du jeu>` : l'obligation de mentionner la date de mise à jour n'est **pas** tenue dans l'artefact | `A·1` | Fichier collé §4 |
| 15 | Le point d'accès aux avis Google répond 401 « credential manquant », donc il est routé et vivant ; ce n'est pas un point d'accès supprimé | `A·2` | Sortie collée §1, geste 2. Portée bornée : ne prouve pas qu'une application approuvée lise les avis |
| 16 | Le dépôt d'un dossier d'approbation exige société immatriculée, domaine, site en ligne, politique de confidentialité, page d'entreprise vérifiée, et vidéo de démonstration au palier supérieur ; quota Google par défaut à zéro | `C·2` | **Rétrogradé par moi** : pages primaires `developers.google.com`, `learn.microsoft.com`, `developers.facebook.com` refusées par le réseau. Aucune adresse consultée, donc pas de `B` |
| 17 | Mastodon n'exige aucune de ces pièces | `C·3` | Connaissance d'usage, non vérifiée ici faute d'accès à `mastodon.social` |
| 18 | Le plan ne mentionne ni société, ni facturation, ni CGV, ni contrat, ni paiement, ni assurance, ni RGPD, ni sauvegarde, ni site, ni hébergement, ni astreinte : 0 occurrence pour chacun | `A·1` | Comptage collé §4 |
| 19 | Le socle n'a ni ordonnanceur, ni envoi de courriel, ni facturation : 0 occurrence de `cron`, `smtp`, `courriel`, `facture`, `paiement` | `A·1` | Comptage §4 |
| 20 | La qualification des sources est globale, sans rattachement source↔client, alors que les données sont cloisonnées par client | `A·1` | Lecture du schéma et de `sources.json` |
| 21 | L'agent de collecte annonce `contact: a-renseigner` aux serveurs publics | `A·1` | Sortie de `verifier.py` §3.2 |
| 22 | Le plan compte trois sources en phase 1, `sources.json` en active quatre dont une en 5b sans licence | `A·1` | Sorties §3.1 |
| 23 | Les délais d'approbation réels dépassent souvent 14 jours par itérations de refus | `D·4` | Déclarée en tête |
| 24 | Un hébergement à bas coût est couramment en ARM, ce qui invaliderait les roues `x86_64` versées | `D·4` | Déclarée en tête |

---

## 7 — Les deux questions que je me pose à moi-même

### Laquelle de mes conclusions, si elle est fausse, coûte le plus cher au projet ?

Pas celle sur le 403, qui ne change qu'un cran. **Celle-ci : « le socle n'est pas capable de collecter les trois sources réelles que le plan a retenues, parce que ce sont des interfaces JSON derrière des coquilles monopage, et qu'il n'a aucun chemin de code pour cela » (lignes 11 et 12 du tableau).**

Si elle est **vraie**, le test gratuit « quatre semaines de données réelles, deux à trois jours, décisif dans les deux sens » n'existe pas : il faut d'abord écrire un connecteur par jeu et une seconde forme d'assertion pour des enregistrements structurés, et la phase 1 n'est pas à quelques jours de son épreuve de vérité.

Si elle est **fausse** — si ces portails servent du HTML indexable que l'explorateur suit sans peine — alors j'ai envoyé le projet écrire un connecteur dont il n'avait pas besoin, j'ai discrédité le seul test gratuit et décisif du plan, et j'ai fait reculer d'un cran la seule affirmation du plan qui tenait debout. C'est de loin l'erreur la plus chère que je peux commettre, parce qu'elle attaque le produit vendable, pas un cran de preuve.

**Comment la tester pour moins de cent euros : elle se teste pour zéro euro et dix minutes.** Depuis n'importe quel poste au réseau ouvert :

```bash
curl -s -o /tmp/b.html -w "%{http_code} %{size_download} %{content_type}\n" https://bodacc-datadila.opendatasoft.com/
grep -c 'href=' /tmp/b.html          # combien de liens suivables l'explorateur trouverait-il ?
python3 -c "import trafilatura,sys; print(repr(trafilatura.extract(open('/tmp/b.html').read()))[:300])"
```

Trois lignes, trois fois (BODACC, DECP, Météo-France). Le verdict est binaire : si `grep -c href=` rend un nombre à deux chiffres et que `trafilatura.extract` rend de la prose, j'ai tort et le socle est prêt ; si l'un des deux rend zéro ou `None`, j'ai raison et il manque un connecteur. **Et le même poste, dans la même minute, peut lever ma ligne `D·4` et les trois `licence_lue_le`** en ouvrant les pages des trois jeux — c'est le même geste, et il vaut plus cher que les 200 € du test chez le prestataire local, parce qu'il décide si le produit existe.

### Qu'ai-je réellement écarté ?

Sans quota, et zéro est une réponse valable. J'en ai écarté **quatre**, et je les nomme pour qu'elles ne reviennent pas :

1. **« Le socle ne tourne pas. »** C'était mon hypothèse de travail la plus probable en commençant, et elle est fausse. Il tourne du premier coup, les chiffres annoncés sont exacts au dixième, le comptage de lignes tombe à l'unité. Écartée par mesure.
2. **« Une montée de version de `trafilatura` casse le rejeu. »** Testée avec une version simulée 2.5.1 dont la sortie différait : 21/21, rien n'a bougé. Je ne peux pas l'affirmer. Écartée faute de preuve — seule l'**absence** du paquet casse le rejeu, et ça, c'est mesuré.
3. **« L'accès aux avis Google est mort. »** C'est la conclusion vers laquelle penchait le registre en `C·3`. Le 401 dit le contraire au niveau du routage. Non seulement je l'écarte, mais je propose de marquer la version forte de cette crainte comme **renversée** au registre : le point d'accès existe, l'obstacle est l'approbation, pas la suppression.
4. **« La mise en service chez un premier client est sous-estimée d'un facteur trois. »** Elle l'est probablement, mais le README l'aveue explicitement et honnêtement. On ne compte pas comme une faute ce qui est déjà déclaré. Écartée comme cible, reprise sous un autre angle en section 4.

---

## 8 — Les cinq colonnes

| MCP à installer | Logiciels manquants | Outils déjà disponibles | IA existantes qui font ce travail, et à quel prix | Futurs possibles à 12 mois ⏳ |
|---|---|---|---|---|
| Un serveur MCP **de qualification de source** : prend une URL, rend licence, conditions, `robots.txt`, `Crawl-delay`, et rédige la chaîne d'attribution. C'est le poste incompressible n° 3 du plan, et le seul des trois qu'un outil peut vraiment accélérer | **Un adaptateur de source JSON** (Opendatasoft et apparentés) : pagination, cartographie de champs, filtre département 971. Sans lui la phase 1 ne collecte rien de réel | `python3` 3.11.15, `sqlite3` 3.45.1 **avec FTS5** — ni serveur de base, ni moteur de recherche à installer, le plan a raison là-dessus | Les quatre produits que le registre a déjà relevés, de 0 à 39 $/mois, qui couvrent le besoin de veille générique. **Ils ne portent pas la provenance par empreinte** — c'est le seul écart réel et il tient | ⏳ **Le palier de développement des plateformes expire** : LinkedIn attend l'achèvement de l'intégration dans les douze mois du palier de développement (`C·2`). Une approbation obtenue trop tôt se périme avant le premier client |
| Un MCP **d'émission de facture** et de suivi d'abonnement, ou l'usage d'un service existant. Rien dans le socle ne facture | **Un ordonnanceur et un envoi de courriel.** Zéro occurrence de `cron` et `smtp` dans le socle. Le rapport existe sur un disque et n'arrive chez personne | `git` — et le clone partiel `--filter=blob:none` que `05-technique.md` désigne comme l'outil de qualification de vitalité le plus rentable de la session | Les générateurs de texte généralistes, qui produisent une réponse d'avis pour quelques centimes — **et une faute disciplinaire chez l'avocat** si l'on annonce un taux de succès (`B·2` au registre). Le prix n'est pas le sujet, le garde-fou métier l'est | ⏳ **`py3langid` est abandonné** : 0 mainteneur soutenu, 3 commits sur douze mois. C'est la brique qui tient le créole guadeloupéen, et le socle en dépend sans verrou de version |
| Un MCP de **surveillance** : alerte si la collecte hebdomadaire rend moins de N lignes. Aujourd'hui une semaine vide sort en code 0 | **Une sauvegarde de `archives/` et de `socle.db`.** Sans elle, un disque perdu détruit la preuve, donc le produit | `curl`, `jq` — suffisants pour tout le test à 0 € de la section 7 | **Aucune IA ne fait le travail qui manque réellement** : constituer une société, publier une politique de confidentialité, faire approuver une application, signer un mandat. Prix : zéro, et c'est bien le problème — c'est du temps humain non compressible | ⏳ **Les roues binaires `cp311-x86_64` versées au dépôt deviennent inutilisables** à la première migration de serveur ou de version de Python. 39 Mo figés sur une architecture |
| — | **Un verrou de dépendances** (`requirements.txt` épinglé, ou roues versées) : c'est la condition de la rejouabilité à un an, et elle n'existe pas | `docker` et `psql`, présents et **inutiles ici** : le socle est volontairement en SQLite sur un fichier. À ne pas introduire avant qu'un client l'ait demandé | — | ⏳ **L'exigence de vidéo de démonstration se durcit** (`C·2`, à relire sur page primaire). Elle crée une boucle : l'approbation demande une démonstration, la démonstration demande un produit en service |

---

## Annexe — Journal de requêtes

Toutes mes recherches, dans l'ordre, le 2 octobre 2026. Les lignes « rien » et « refusé » valent autant que les autres : elles disent où il est inutile de retourner.

| # | Requête ou adresse | Outil | Résultat |
|---|---|---|---|
| 1 | arborescence `/home/user/moteurs-et-outils/`, `socle/`, `critiques/` | Bash `ls` | trouvé |
| 2 | `PLAN-DE-CONSTRUCTION.md` (199 lignes) | Bash `cat` | trouvé |
| 3 | `REGISTRE-DE-DEMARCHE.md` (197 lignes) | Bash `cat` | trouvé |
| 4 | `socle/README.md` | Bash `cat` | trouvé |
| 5 | versions `python3`, `node`, roues installées, FTS5 | Bash | trouvé |
| 6 | copie du socle au bac à sable, état propre | Bash `cp`/`rm` | trouvé |
| 7 | séquence d'installation du README sur `sources.json`, chronométrée | Bash | trouvé (0 capture) |
| 8 | séquence du banc : `generer.py`, serveur local, `collecte --max 40` | Bash | trouvé (21/21) |
| 9 | `verifier.py 10` et `verifier.py --toutes` | Bash | trouvé |
| 10 | `publier.py` : ajouter, relire, programmer, envoyer, bilan | Bash | trouvé |
| 11 | `banc/bouchon_plateformes.py` (lecture du code du 403) | Bash `cat` | trouvé |
| 12 | `journal_acces` dans `publier.py` | Bash `grep` | trouvé |
| 13 | base livrée `socle/socle.db` : comptes, `acces_confie`, `journal_acces` | Bash `sqlite3` | trouvé |
| 14 | en-tête de `sources.json` ; recherche d'un fichier de verrouillage | Bash | trouvé / **rien** (aucun verrou) |
| 15 | `licence_lue_le` dans `socle.py` et `schema.sql` | Bash `grep` | **rien** (aucun garde-fou) |
| 16 | `cmd_collecte` et les 14 `CHECK` du schéma | Bash | trouvé |
| 17 | collecte forcée sur `licence_lue_le = NULL`, guichet 5b | Bash | trouvé (12 captures) |
| 18 | rapport avec licence non lue, puis rapport à 0 assertion | Bash | trouvé |
| 19 | rejeu sous `trafilatura` absent, puis sous version simulée 2.5.1 | Bash | trouvé / **rien** (version : aucune divergence) |
| 20 | `pip download trafilatura==2.3.0 py3langid==0.4.0` | Bash | trouvé (19 roues, 39 Mo) |
| 21 | `find -iname "*mandat*"` | Bash | **rien** |
| 22 | `https://developers.facebook.com/` | Bash `curl` | **refusé** (403 au CONNECT) |
| 23 | `https://developers.google.com/` | Bash `curl` | **refusé** |
| 24 | `https://business.google.com/` | Bash `curl` | **refusé** |
| 25 | `https://www.linkedin.com/` | Bash `curl` | **refusé** |
| 26 | `https://mastodon.social/` | Bash `curl` | **refusé** |
| 27 | `https://www.data.gouv.fr/` | Bash `curl` | **refusé** |
| 28 | `https://bodacc-datadila.opendatasoft.com/` | Bash `curl` | **refusé** |
| 29 | `https://www.legifrance.gouv.fr/` | Bash `curl` | **refusé** |
| 30 | `https://www.insee.fr/` | Bash `curl` | **refusé** |
| 31 | `https://barreau-guadeloupe.avocat.fr/` | Bash `curl` | **refusé** |
| 32 | `https://www.guadeloupe.gouv.fr/` (via le collecteur) | socle | **refusé** |
| 33 | `https://pypi.org/` | Bash `curl` | trouvé (200, hôte autorisé) |
| 34 | `mybusiness.googleapis.com/v4/accounts/…/reviews` | Bash `curl` | trouvé (401) |
| 35 | `mybusiness.googleapis.com/$discovery/rest?version=v4` | Bash `curl` | trouvé (404) |
| 36 | `mybusinessaccountmanagement.googleapis.com/v1/accounts` | Bash `curl` | trouvé (401) |
| 37 | `mybusinessbusinessinformation.googleapis.com/v1/categories` | Bash `curl` | trouvé (401) |
| 38 | « Google Business Profile API access request form requirements quota approval 2026 » | WebSearch | trouvé (secondaire) |
| 39 | « LinkedIn Community Management API access requirements verified company page development tier 2026 » | WebSearch | trouvé (secondaire) |
| 40 | `learn.microsoft.com/…/community-management-app-review` | WebFetch | **refusé** (EGRESS_BLOCKED) |
| 41 | `developers.google.com/my-business/content/prereqs` | WebFetch | **refusé** (EGRESS_BLOCKED) |
| 42 | « Meta app review business verification requirements pages_manage_posts 2026 » | WebSearch | trouvé (secondaire) |
| 43 | `facturation|SIRET|CGV|assurance|RGPD` dans `critiques/` | Bash `grep` | trouvé (RGPD très présent dans `01-juridique.md`) |
| 44 | 24 termes d'entreprise et de droit dans le plan | Bash `grep -c` | **rien** (0 occurrence pour chacun) |
| 45 | `url_base` des 5 sources de `sources.json` | Bash | trouvé |
| 46 | `Collecteur`, `run`, `liens`, `http` dans `socle.py` | Bash | trouvé (aucun suivi de redirection) |
| 47 | `trafilatura.extract` sur JSON et sur coquille monopage | Bash | trouvé (`None`, `None`, `[]`) |
| 48 | lignes non vides des 6 fichiers du socle | Bash `grep -cve` | trouvé (1 183) |
| 49 | `cron|smtp|courriel|facture|paiement` dans le socle | Bash `grep` | **rien** |
| 50 | `git status` (contrôle : rien commité, rien modifié) | Bash | trouvé (arbre propre) |

**Récapitulatif du journal : 50 requêtes · 36 trouvé · 7 rien · 12 refusé** (les lignes 14 et 19 comptent deux résultats). Hôtes refusés, à ne pas réessayer depuis cet environnement : `developers.facebook.com`, `developers.google.com`, `business.google.com`, `www.linkedin.com`, `mastodon.social`, `www.data.gouv.fr`, `bodacc-datadila.opendatasoft.com`, `www.legifrance.gouv.fr`, `www.insee.fr`, `barreau-guadeloupe.avocat.fr`, `www.guadeloupe.gouv.fr`, `learn.microsoft.com`. Hôtes atteignables et utiles : `pypi.org`, `mybusiness.googleapis.com`, `mybusinessaccountmanagement.googleapis.com`, `mybusinessbusinessinformation.googleapis.com`.

**Contrôle de mon propre sourçage, puisqu'il est compté.** Affirmations classées `A` : 16, **toutes** adossées à une sortie de commande locale collée dans ce fichier. Affirmations classées `B` : **zéro** — je n'en revendique aucune, n'ayant pu ouvrir aucune page primaire. Affirmations classées `C` : 3, dont 2 rétrogradées par moi depuis `B` faute d'adresse consultable. Affirmations `D` : 3, déclarées en tête. Adresses web réellement citées : 4, toutes des points d'accès `googleapis.com` que j'ai appelés moi-même et dont j'ai collé le code de réponse. L'écart entre revendication de source primaire et adresses citées est donc **nul par construction** : je ne revendique aucune source primaire.
