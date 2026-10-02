# Relance — socle livré, règle du loyer appliquée aux quatre outils, verdicts créole et licence

Suite de `03-methode.md`, qui n'est pas modifié. Document cible non modifié. Aucun commit.
Date de toutes les mesures : **2 octobre 2026**. Conteneur Linux 6.18, 4 cœurs, 15 Gio,
Python 3.11.15, SQLite 3.45.1.

Périmètre tenu en entier par décision de Laurent Cieutat : **veille à provenance prouvée,
publication sociale, gestion des avis, blog.** Le socle livré ici n'est pas le produit,
c'est l'étape un — et la seule dont les trois autres dépendent toutes.

---

## 0. Mes lignes en cran D — déclarées avant le contenu

| # | Ligne en cran D | Pourquoi je n'ai pas pu monter de cran |
|---|---|---|
| D1 | **L'attachement de la Licence Ouverte 2.0 à chacun des trois jeux de données que je nomme** (BODACC, DECP, Météo-France) | `data.gouv.fr`, `data.economie.gouv.fr`, `meteo.data.gouv.fr` et `etalab.gouv.fr` sont tous **bloqués** par la politique de sortie réseau. Le *texte* de la licence est lu et vérifié en cran B ; son *attachement* à chaque jeu ne l'est pas. `sources.json` porte cette réserve en tête et `licence_lue_le` reste à `null` |
| D2 | La fréquence réelle de mise à jour de BODACC et de DECP, et leur granularité départementale pour la Guadeloupe | Même blocage. Je nomme ces jeux pour leur nature, pas pour un débit mesuré |
| D3 | Le plafond de 5 avis des interfaces publiques de Google et de TripAdvisor | Reste en cran C depuis mon premier retour. `developers.google.com` bloqué. **C'est la ligne D/C la plus coûteuse de tout mon travail** — voir la relance 1, test à moins de cent euros |
| D4 | Le fait qu'exécuter un programme AGPL **sans le modifier** ne déclenche pas l'obligation de publier son propre code | Lecture de la clause 13, qui s'ouvre sur « if you modify the Program ». C'est une lecture, pas un avis juridique. **À confirmer par un juriste avant d'y engager l'architecture** |
| D5 | Les délais d'approbation d'une application par Meta, LinkedIn, TikTok | Je l'ignore et je ne le chiffre pas. C'est pourtant le chemin critique du volet publication |
| D6 | Les conversions lignes de code → jours-homme | Toujours interdites dans mon travail. Je ne convertis nulle part |

**Ce que je n'ai toujours pas pu faire, et qui n'est pas de ma main.** Aucune source
guadeloupéenne réelle n'a été touchée. Je n'ai pas réessayé, conformément à la consigne.
La liste exacte des hôtes à ouvrir est en section 7.

---

## 1. La version minimale, livrée — et écrite comme une fondation

**Emplacement : `/home/user/moteurs-et-outils/socle/`.** Mode d'emploi complet dans
`socle/README.md`. Code tourné, sorties collées ci-dessous.

### 1.1 Ce qui est livré

| Fichier | Lignes non vides | Rôle |
|---|---|---|
| `schema.sql` | 375 | 24 objets : 12 tables déclarées, 2 vues, 4 déclencheurs, contraintes |
| `socle.py` | 326 | découverte, extraction, provenance, index, assertions, rapport, étalons |
| `verifier.py` | 122 | rejeu d'une ligne, trois contrôles indépendants |
| `publier.py` | 215 | orchestrateur de publication, trois plateformes |
| `banc/generer.py` | 128 | portail fictif multilingue, 4 langues dont le créole guadeloupéen |
| `banc/bouchon_plateformes.py` | 17 | bouchon des interfaces, pour tourner sans réseau sortant |
| **Total** | **1 183** | commentaires et documentation inclus |

Dépendances externes : **deux**, `trafilatura` (Apache-2.0) et `py3langid` (BSD).
Ni serveur de base de données, ni moteur de recherche, ni service tiers.

### 1.2 Le temps d'installation — mesuré, non estimé

Chronométré de bout en bout, dépendances déjà en cache :

```
### 2. init de la base        → 24 objets de schéma
### 3. qualification          → 1 source retenue
### 4. collecte               → 12 captures en 4,8 s (2,5 doc/s, débit bridé à 5 req/s)
### 5. assertions             → 21 assertions
### 6. étalons                → 100 % remontées / 100 % datées / 100 % rejouables
### 7. rapport                → rapport-2026-S40.md, 8 405 octets

=== TEMPS TOTAL D'INSTALLATION, MESURÉ : 7,1 s ===
base : 188 Ko   archives : 100 Ko
```

**Ce que ces 7,1 secondes ne sont pas.** Elles mesurent l'installation du logiciel, pas
la mise en service chez un client. Ne sont **ni mesurés ni estimés** ici : la lecture de
la licence et des conditions de chaque source (une fiche par source), la signature du
mandat quand le volet avis arrive, le réglage des débits. Le logiciel s'installe en
secondes ; **la mise en service est un travail de lecture.** C'est le vrai contenu de la
première semaine chez un client, et je refuse de le chiffrer sans l'avoir chronométré.

### 1.3 Le schéma de provenance — quel champ, quelle empreinte, quel horodatage

Principe : **une capture est un fait immuable**, un déclencheur SQL interdit de la
modifier. Si la page change, on ajoute une capture, on n'écrase jamais.

| Table | Champs qui portent la preuve |
|---|---|
| `source` | `guichet`, `licence_spdx`, `licence_lue_le`, `attribution_texte`, `verdict`, `motif_verdict` |
| `capture` | **`sha256_corps`** (empreinte de l'octet-à-octet reçu), **`ts_capture_utc`** (ISO 8601 Z), `chemin_archive`, `http_statut`, `octets`, `agent_utilisateur`, `version_collecteur` |
| `extraction` | `outil`, `version_outil`, `parametres_json`, `sha256_texte`, `langue_code`, `langue_avant_normalisation` |
| `assertion` | `citation_exacte`, `offset_debut`, `offset_fin`, `genere_par_ia`, `relu_par_humain`, `relecteur`, `ts_relecture_utc` |

L'archive est conservée dans `archives/<2 car.>/<sha256>.gz` : **le nom du fichier est son
empreinte**, donc une archive altérée se détecte seule. Tout est stocké en UTC ; la
Guadeloupe est à UTC-4 toute l'année et le rendu local est séparé, avec son fuseau déclaré.

**Comment on rejoue une ligne un an plus tard** — `python3 verifier.py 10`, trois contrôles
indépendants pour savoir *lequel* a bougé. Sortie réelle :

```
=== assertion 10 ===
  texte      : An ka alé bouk-la chak jou pou vwè ki jan travay-la ka avansé, é sé moun-la té kontan vwè mwen.
  source     : Banc local de demonstration  (guichet 6, licence CC0-1.0, lue le 2026-10-02)
  url        : http://127.0.0.1:8731/article-4.html
  captee le  : 2026-10-02T19:41:26Z   par socle 1.0
  langue     : gcf  (detectee avant normalisation : oui)
  1. ARCHIVE  : INTACTE  attendu 402574d1380bf2ea…  obtenu 402574d1380bf2ea…  (2061 octets)
  2. EXTRACT. : REPRODUITE  trafilatura 2.3.0 {'favor_recall': False, 'include_comments': False}
  3. CITATION : PRESENTE   aux offsets 0-95 : oui
  --> PROUVEE
```

```
=== Rejeu de 21 assertion(s) ===
  archive     : 21/21 = 100.0 %
  extraction  : 21/21 = 100.0 %
  citation    : 21/21 = 100.0 %
  PROUVEES    : 21/21 = 100.0 %
```

`verifier.py` **ne touche pas au réseau**. Il prouve ce qui a été capté, pas ce que la
source dit aujourd'hui.

### 1.4 Ce que le schéma prévoit DÈS MAINTENANT pour les trois outils à venir

C'est la demande explicite, et c'est la partie qui évite une migration dans six mois.

**Les trois champs irrécupérables — ils existent avant leur usage, volontairement.**

| Champ | Table | Pourquoi il ne se rattrape jamais |
|---|---|---|
| **`date_experience_consommation`** | `avis` | La date de l'expérience de consommation ne se reconstitue pas. Non captée à l'origine, elle est perdue. Le champ compagnon **`date_experience_origine` est obligatoire** et contraint à quatre valeurs — `champ_plateforme`, `declaratif_client`, `deduite`, `absente_a_la_source`. « Absente à la source » est une réponse licite ; une absence silencieuse ne l'est pas |
| **`relu_par_humain` + `relecteur` + `ts_relecture_utc`** | `assertion`, `publication`, `article` | La trace de relecture humaine **avant** publication. Après l'envoi, on ne peut plus prouver qu'elle a eu lieu. Un déclencheur SQL refuse de passer en `programme` ou `envoye` un contenu généré sans relecteur nommé |
| **`genere_par_ia` + `mention_ia_affichee` + `modele_ia` + `version_modele_ia`** | `assertion`, `publication`, `article` | La mention d'un contenu généré. Dans six mois, personne ne saura plus quelle ligne sortait d'un modèle, ni duquel |

**Le reste de ce qui est déjà en place, et pourquoi l'ajouter plus tard coûterait cher :**

| Prévu | Ce qui serait cassé si on l'ajoutait après |
|---|---|
| `client_id` sur `avis`, `publication`, `article`, `assertion` | **Le cloisonnement par client existe dès le premier client.** L'ajouter plus tard impose de réécrire toutes les requêtes du produit |
| `publication.assertions_json` et `article.assertions_json` | Le lien entre ce qui est publié et la provenance qui le fonde. Sans lui, le blog et les réseaux publient des affirmations orphelines — exactement ce que le socle existe pour empêcher |
| `publication.fuseau` + `ts_programme_utc` **et** `ts_programme_local` | Un champ d'heure locale sans fuseau déclaré est un bogue qui se révèle au changement d'heure métropolitain. UTC-4 toute l'année ne se devine pas |
| `avis.note` **et** `avis.note_echelle_max` | Une note sur 5 et une note sur 10 ne se moyennent pas. Sans l'échelle, les avis de deux plateformes sont inutilisables ensemble |
| `avis.motif_non_publication` + `ts_moderation_utc` | Obligation de traitement des avis. Une modération sans motif ni date est indéfendable |
| `acces_confie` + `journal_acces` | **Aucun secret dans la base** : seulement une référence de coffre, plus le journal de qui a demandé quoi et quand |
| `mesure` | La doctrine de preuve en base : refus d'enregistrer une mesure sans `n`, sans intervalle, sans empreinte de jeu d'épreuve, sans `cran_preuve` ; et une contrainte vérifie que le jeu a été figé **avant** la mesure |
| `demande_retrait` | « Retrait sous demande de l'éditeur, procédure écrite et tenue » (§2.3 du prompt). Une procédure sans table est une promesse |

**Ce que le schéma refuse, par construction.** Preuve exécutée :

```
garde-fou OK : secret refuse par le schema -> CHECK constraint failed: reference_coffre LIKE 'coffre://%'
```

L'organe « garde des accès confiés » n'est pas construit et ne doit pas l'être —
97,8 années-auteur mesurées sur OpenBao/Vault. Le socle ne détient que l'adresse du coffre.

### 1.5 Le rapport de veille hebdomadaire — exemple réel produit par le code

`rapport-2026-S40.md`, 8 405 octets, 21 assertions. Extrait tel que produit :

```markdown
# Rapport de veille — semaine 2026-S40

Client : client-zero · Fuseau : America/Guadeloupe (UTC-4, sans heure d'été)
Période : 7 derniers jours · Édité le 2026-10-02T19:41:29Z

**Aucune ligne de ce rapport n'est générée par un modèle de langage.**

## Banc local de demonstration
*Guichet 6 · Licence CC0-1.0* · Banc local — pages generees par le socle lui-meme

- **[13]** Dépi yè oswè, lapli-la ka tonbé fò asi tout mòn-la é chimen-la glisé anpil.
  — Lapli-la ka tonbé fò asi mòn-la · langue `gcf` · publié 2026-09-26
  — source : http://127.0.0.1:8731/article-5.html
  — captée 2026-10-02T19:41:27Z · empreinte `8e74aa08b057607f…` · rejouable

- **[16]** La compañía aérea ha anunciado una nueva conexión semanal desde Santo Domingo…
  — Nueva conexión aérea semanal desde Santo Domingo · langue `es` · publié 2026-09-29
  — source : http://127.0.0.1:8731/article-7.html
  — captée 2026-10-02T19:41:27Z · empreinte `8423c280db038b23…` · rejouable

---
## Contrôle de provenance de ce rapport

| Étalon | Valeur |
|---|---|
| Part remontée à une source primaire | 100.0 % |
| Part datée | 100.0 % |
| Part rejouable à l'identique | 100.0 % |
| Assertions générées par IA | 0 |
```

**Les quatre choses qui font sa valeur, et qu'aucun concurrent n'affiche :**

1. Chaque ligne porte URL, horodatage UTC de captation et empreinte. Le client peut
   exiger le rejeu de n'importe quelle ligne et l'obtenir en une commande.
2. Le rapport finit par **son propre contrôle de provenance, chiffré**. Il s'audite.
3. Le tableau des sources porte la licence, **sa date de lecture** et l'attribution
   exacte. La Licence Ouverte 2.0 exige le nom du concédant *et la date de dernière mise
   à jour* : l'obligation est tenue dans le livrable, pas dans une annexe.
4. La ligne sur l'absence de contenu généré est **calculée depuis la base**, pas déclarée.

Défaut trouvé et corrigé pendant la mise au point : une page 404 avait produit une
assertion. Seules les captures en HTTP 200 nourrissent désormais des assertions — une
page d'erreur est un fait de provenance valide, pas une source d'affirmation.

---

## 2. Les trois sources en ouverture déclarée, hors presse

### 2.1 La contrainte de l'agent juridique est intégrée, et elle est dans le code

La presse n'est **pas** en guichet 6 : droit voisin des éditeurs, exception de courte
citation qui tombe dès que l'extrait dispense de se référer à l'article — ce qui est la
définition d'un produit de veille —, et licence payante auprès d'un organisme de gestion
collective. Donc **guichet 4, payant.**

Ce n'est pas une note de bas de page dans mon travail : c'est une ligne de
`sources.json`, avec `verdict: "ecarte"`, que le déclencheur `source_ecartee_inactive`
désactive automatiquement pour qu'aucun collecteur ne la touche par accident.

### 2.2 Ce que j'ai vérifié en cran B — le texte de la Licence Ouverte 2.0

`data.gouv.fr` est bloqué, mais **Etalab publie sa licence sur GitHub, qui est
atteignable.** Dépôt `etalab/licence-ouverte`, fichier `LO.md`, cloné et lu le
2 octobre 2026. Contenu décisif, cité :

- **Réutilisation commerciale explicitement autorisée** : « un droit non exclusif et
  gratuit de libre Réutilisation […] **à des fins commerciales ou non**, dans le monde
  entier et pour une durée illimitée »
- Droit d'**extraire et de transformer**, et de « l'inclure dans votre propre produit ou
  application »
- **Le droit sui generis des producteurs de bases de données est CÉDÉ** : « Lorsque le
  Concédant détient des Droits de propriété intellectuelle sur l'Information, il les cède
  au Réutilisateur de façon non exclusive, à titre gracieux », et la définition inclut
  explicitement « droit sui generis des producteurs de bases de données »
- **Obligation unique** : « mentionner la paternité de l'Information : sa source (a minima
  le nom du Concédant) **et la date de la dernière mise à jour** de l'Information
  réutilisée ». Une URL y suffit
- Interdits : suggérer une caution officielle ; « induire en erreur des tiers quant au
  contenu de l'Information, sa source et sa date de mise à jour »
- **Le RGPD reste pleinement applicable** quand l'information contient des données
  personnelles
- Compatible CC-BY, OGL, ODC-BY

**C'est l'exact inverse du droit voisin de la presse.** Là où la presse interdit l'extrait
qui dispense de lire l'article, la Licence Ouverte autorise l'extraction, la
transformation, l'exploitation commerciale, et **lève elle-même l'obstacle du droit sui
generis** qui est le risque juridique central du guichet 5. Ce n'est pas une tolérance,
c'est une cession écrite.

### 2.3 Les trois sources, nommées

| # | Source | Guichet | Licence revendiquée | Ce qui bouge chaque semaine | Cran sur l'attachement |
|---|---|---|---|---|---|
| 1 | **BODACC** — Bulletin officiel des annonces civiles et commerciales | 6 | Licence Ouverte 2.0 | Immatriculations, cessions de fonds, procédures collectives, modifications — par département | **D** |
| 2 | **DECP** — données essentielles des marchés publics | 6 | Licence Ouverte 2.0 | Marchés attribués par les collectivités, avec titulaire, montant, durée | **D** |
| 3 | **Météo-France données ouvertes** — vigilance et observations | 6 | Licence Ouverte 2.0 | Vigilances, cumuls, alertes. Saison cyclonique du 1er juin au 30 novembre : exigence n°3 du prompt | **D** |

**Le contre-exemple que j'ai gardé volontairement dans le registre.** Le recueil des actes
administratifs de la préfecture est un portail institutionnel, et il est en **5b, pas en 6** :
pas de licence déclarée. `sources.json` le porte avec ce motif écrit, parce que la
confusion « institutionnel donc ouvert » est exactement l'erreur que le guichet 6 invite
à faire. **Un portail public sans licence déclarée n'est pas en accès ouvert déclaré.**

Et une règle est dans le code : *le collecteur ne doit pas tourner sur une source dont
`licence_lue_le` est nul.* Les trois lignes ci-dessus sont donc, à cette heure,
inexploitables — par construction, et c'est voulu.

### 2.4 Verdict franc : un produit de veille utile se construit-il sur ces seules sources ?

**Oui — mais ce n'est pas le produit que le document avait en tête, et il faut le dire
sans l'enjoliver.**

Ce qui se construit : une **veille officielle et économique**. Qui s'est créé, qui a
déposé, quel fonds a changé de main, quel marché public a été attribué et à qui, quelle
vigilance est active. Pour un hôtelier ou un restaurateur guadeloupéen, c'est : mon
concurrent a ouvert, mon fournisseur est en liquidation, la collectivité a attribué la
réfection du front de mer devant chez moi, et il faut annuler les sorties en mer de demain.

Ce qui ne se construit pas : une **revue de presse**. Pas d'articles, pas de citations de
journalistes, pas de « ce qu'on dit de vous dans la presse ». Si le client achète cela, il
faut la licence du guichet 4, et le périmètre change.

**Trois avantages que la presse n'a pas, et qui sont sous-estimés :**

1. **La publication est obligatoire.** Un éditeur de presse peut fermer son flux, modifier
   ses conditions, exiger une licence. Un bulletin officiel ne peut pas : sa publication
   est imposée. **Le risque de coupure, que la section 2.6 du prompt identifie comme ce
   qui « casse le jour où une plateforme modifie ses défenses », est ici structurellement nul.**
2. **Le droit sui generis est cédé par écrit** (§2.2). C'est le seul guichet où l'obstacle
   juridique central n'est pas contourné mais levé par le concédant.
3. **C'est une donnée que le client ne peut pas obtenir seul.** La presse, il la lit déjà.
   BODACC et DECP, il ne les ouvrira jamais : ce sont des fichiers volumineux et illisibles.
   **La valeur ajoutée est plus grande là où la donnée est ouverte mais indigeste.**

**Trois conséquences qu'il faut assumer, et dont deux allègent le projet :**

1. Ces sources sont des **jeux structurés, pas de la prose**. L'organe « extraction propre
   multilingue » — celui sur lequel j'ai mesuré F1 = 0,916 — y est **presque inutile**.
   Une veille open-data n'a pas besoin du détourage de pages web.
2. **L'exigence « Langues » ne s'applique pas à ce flux.** BODACC et DECP sont en français
   administratif. Le créole, l'anglais et l'espagnol concernent les **avis**, pas la veille
   open-data. Le prompt présente les six exigences comme pesant sur tout : elles ne pèsent
   pas toutes sur tout, et le dire économise du travail.
3. En revanche l'exigence **« Sources locales »** devient le cœur du travail : filtrer
   BODACC et DECP sur la Guadeloupe, et savoir quels codes de commune et quels
   identifiants d'acheteur public sont les bons. **Ce n'est pas du code, c'est de la
   connaissance de terrain** — et c'est précisément ce qu'un concurrent mondial n'a pas.

**Le risque que je ne peux pas écarter, et c'est ma conclusion la plus fragile.** Je n'ai
pas vérifié que BODACC et DECP contiennent assez de lignes guadeloupéennes par semaine
pour qu'un rapport hebdomadaire ait du contenu. Sur un territoire de cette taille, un
rapport à trois lignes ne se vend pas. **C'est testable pour zéro euro** — relance 1.

---

## 3. Le piège de licence de l'orchestrateur de publication — réponse nette

### 3.1 Ce que l'AGPL-3.0 impose exactement à un service hébergé

Clause 13 lue intégralement dans le fichier `LICENSE` du dépôt Postiz, cran B. Texte :

> **13. Remote Network Interaction; Use with the GNU General Public License.**
> Notwithstanding any other provision of this License, **if you modify the Program**,
> your modified version must prominently offer all users interacting with it remotely
> through a computer network (if your version supports such interaction) an opportunity
> to receive **the Corresponding Source of your version** by providing access to the
> Corresponding Source from a network server at no charge, through some standard or
> customary means of facilitating copying of software.

Ce que cela veut dire, précisément, pour un service vendu à des clients :

| Situation | Obligation |
|---|---|
| On installe Postiz **sans le modifier** et on vend l'accès | La clause 13 s'ouvre sur « **if you modify** ». Non modifié, elle ne déclenche pas la publication de son propre code. On garde les mentions de licence et l'offre de source du programme. **Cran D4 : c'est ma lecture, pas un avis juridique** |
| On modifie Postiz — ne serait-ce qu'une ligne | **Tout utilisateur du service, y compris un client payant, a le droit d'obtenir gratuitement le code source de la version modifiée.** Pas sur demande commerciale : par une offre affichée en évidence dans le service |
| On combine Postiz et notre produit en un seul programme | Le tout devient une œuvre couverte. Notre produit passe sous AGPL |
| On garde deux processus séparés qui se parlent par HTTP | C'est la parade usuelle, et elle n'est **pas** une garantie. C'est un jugement juridique, pas une propriété technique |

**Et voilà ce qui tranche la question, sans juriste.** Les six exigences guadeloupéennes
*obligent* à modifier : fuseau UTC-4 sans heure d'été, quatre langues dont le créole,
saisonnalité, prix plafond local. Un orchestrateur métropolitain non modifié ne tient pas
ces exigences — le prompt le dit lui-même en section 3, « tout outil de programmation
raisonnant en heure métropolitaine » est disqualifié. **Donc on modifie. Donc la clause 13
mord. Donc il faudrait livrer à chaque client le code source de notre orchestrateur.**

Ce n'est pas rédhibitoire en soi — on peut vendre du service autour de code ouvert. Mais
c'est une décision de modèle économique, pas un détail technique, et elle doit être prise
en connaissance de cause.

### 3.2 Existe-t-il une brique équivalente sous licence permissive ? Oui, et elle est petite

J'ai cloné trois candidats et lu leurs fichiers de licence directement, cran B :

| Projet | Licence lue dans le dépôt | Plateformes | Verdict |
|---|---|---|---|
| **Postiz** | **AGPL-3.0** (`LICENSE`) | **30+** : `facebook instagram linkedin x tiktok threads gmb wordpress bluesky mastodon reddit pinterest youtube telegram discord…` | Copleft réseau. Mord dès modification |
| **Mixpost** | **MIT** (`LICENSE.md`) | **3 à 4 seulement** : Facebook Page, Mastodon, Twitter/X, Meta | Permissive, mais voir ci-dessous |
| **trypost** | **AGPL-3.0** (`LICENSE.md`) | — | Même piège que Postiz |
| **Free-AI-Social-Media-Scheduler** | **MIT** (`LICENSE`) | YouTube, TikTok | Trop étroit |

**La nuance qui décide, et qu'aucun comparatif ne dit** — lue dans le `README.md` de
Mixpost lui-même, ligne 71 :

> *This repository contains the **Lite version** of Mixpost Pro, a commercial product.*

Donc : la seule brique permissive sérieuse est **le palier gratuit d'un produit
commercial**, elle couvre **3 ou 4 plateformes**, elle est en **PHP/Laravel** (9 156 lignes)
— une pile étrangère au socle, qui est en Python — et les plateformes intéressantes sont
vraisemblablement dans le palier payant.

**Conclusion nette : il n'existe pas de brique libre permissive couvrant trente
plateformes. Le choix réel est entre trois plateformes sous MIT, trente sous copyleft
réseau, ou écrire soi-même.**

### 3.3 Le coût d'écrire le minimum pour deux ou trois plateformes — mesuré

Je l'ai écrit et fait tourner. `socle/publier.py`, **215 lignes non vides**, trois
plateformes, contre un bouchon local d'interfaces. Sortie réelle :

```
=== tentative de programmer le contenu IA SANS relecture ===
REFUSE par le schema : contenu genere par IA : relecture humaine nommee obligatoire avant envoi

publication 3 relue par Laurent Cieutat : accepte
publication 1 programmee  local 2026-10-02 10:00 (UTC-4)  =  UTC 2026-10-02T14:00Z

 id plateforme statut      IA  relu par       prevu local       car.
  1 mastodon   programme   non -              2026-10-02T10:00  146
  2 facebook   programme   non -              2026-10-02T11:00  102
  3 linkedin   programme   oui Laurent Cieuta 2026-10-02T12:00  70

3 publication(s) due(s)
  1 mastodon  ENVOYE   http=201 distant=dist-1000
  2 facebook  ENVOYE   http=201 distant=dist-1001
  3 linkedin  ECHEC    http=403 {"error":"application non approuvee par la plateforme"}

  taux de publication reussie : 2/3 = 66.7 %
  taux de rejet plateforme    : 1/3 = 33.3 %
  contenus IA envoyes sans relecture nommee (doit valoir 0) : 0
  contenus IA envoyes sans mention affichee (doit valoir 0) : 0

=== Journal des acces confies ===
  2026-10-02T19:44:34Z  mastodon  publication  accorde   par publier 1.0
  2026-10-02T19:44:34Z  facebook  publication  accorde   par publier 1.0
```

Ce que ces 215 lignes tiennent déjà : file à statuts, limite de caractères par
plateforme, conversion de fuseau explicite et vérifiable, relecture humaine imposée **au
niveau SQL** et non par le programme, journal de chaque accès aux identifiants confiés,
zéro secret en base, et les deux étalons de la section 6 — taux de publication réussie et
taux de rejet plateforme — calculés depuis la base.

**Et voici le point le plus important de toute cette section.** Le 403 du bouchon dit
« application non approuvée par la plateforme ». **Ce n'est pas un détail de banc, c'est
le vrai coût de cet outil.** Écrire l'orchestrateur, c'est 215 lignes mesurées. Faire
approuver une application par Meta, par LinkedIn, par TikTok, c'est un dossier par
plateforme, avec des délais que **j'ignore et que je refuse d'estimer (cran D5)**. Trente
plateformes sous AGPL ne servent à rien si l'on n'a l'approbation d'aucune.

**Si la seule voie propre est de construire, voici son prix, et je le donne dans l'unité
où il est honnête :** le code est de l'ordre de **215 lignes pour trois plateformes, et
environ 70 lignes par plateforme supplémentaire** (un adaptateur = un point d'entrée, une
limite de caractères, un format de charge utile, une lecture de code d'erreur). Ce que je
ne convertis pas en jours, c'est le reste, et le reste est le vrai calendrier :
**un dossier d'approbation par plateforme, et le délai de la plateforme, qui ne se réduit
pas en embauchant.** Voir section 5.

**Ma recommandation.** Écrire les trois adaptateurs. Pas reprendre Postiz, pas reprendre
Mixpost. Non par orgueil : parce que 215 lignes mesurées valent moins cher que la
décision AGPL et moins cher qu'une pile PHP à côté d'un socle Python, et parce que
l'orchestrateur n'est **pas** le goulot — l'approbation l'est.

---

## 4. Le verdict créole — tranché, et la cause est identifiée

### 4.1 Ce que j'avais écrit, et ce que j'ai trouvé

Mon premier retour donnait 2 échantillons sur 4 classés en créole haïtien, à n = 7,
déclaré comme signal et non comme mesure. **J'avais raison de ne pas conclure, et la
cause n'était pas celle que j'imaginais.**

J'ai écrit 10 phrases en créole guadeloupéen de longueur d'avis et je les ai passées au
détecteur deux fois : avec leurs accents, puis dépouillées de leurs accents. Sortie réelle :

```
=== TEST DECISIF : meme texte, avec accents puis sans accents (n=10) ===
  # AVEC accents           SANS accents            marge avec  marge sans
  1 gcf                    gcf                          +98.0        +0.3
  2 gcf                    ht                           +59.4        -2.5
  3 gcf                    ht                           +53.9        -5.7
  4 gcf                    gcf                          +46.8       +18.7
  5 gcf                    ht                           +86.2        -4.0
  6 gcf                    ht                           +59.3       -14.8
  7 gcf                    gcf                          +39.1       +10.0
  8 gcf                    gcf                          +33.2        +9.1
  9 gcf                    gcf                          +48.7       +18.4
 10 gcf                    gcf                          +66.9        +1.9

  gcf correctement reconnu AVEC accents : 10/10   marge mediane +56.6
  gcf correctement reconnu SANS accents :  6/10   marge mediane  +1.1
  pertes causees par le seul depouillement des accents : 4/10
  ou va le texte depouille : {'gcf': 6, 'ht': 4}

=== Et le francais, l'anglais, l'espagnol resistent-ils au depouillement ? ===
  fr: avec=fr   sans=fr    STABLE
  fr: avec=fr   sans=fr    STABLE
  en: avec=en   sans=en    STABLE
  es: avec=es   sans=es    STABLE
```

**La confusion n'est pas causée par la paire de langues. Elle est causée par le
dépouillement des accents.** Mon premier essai avait des accents retirés — pour éviter un
problème d'encodage. C'est moi qui avais fabriqué la panne.

Deuxième sonde, pour vérifier que le détecteur a bien appris la distinction : paires
minimales sur le marqueur progressif, `ka` en guadeloupéen contre `ap` en haïtien.

```
=== SONDE 1 : paires minimales sur le marqueur progressif (gcf 'ka' / ht 'ap') ===
  le detecteur suit le marqueur discriminant : 6/8
```

Troisième sonde, effet de la longueur : la marge **croît** avec le texte, de +98 sur une
phrase à +414 sur dix. Un avis court est donc le cas le plus difficile, et il reste du bon
côté quand les accents sont là.

### 4.2 Pourquoi la fragilité est structurelle — et c'est sourcé

J'ai cloné `JHU-CLSP/Kreyol-MT` (MIT), la plus grande collection documentée de traduction
automatique pour les créoles, et compté ce qui existe pour le créole guadeloupéen :

```
=== TOUT le creole guadeloupeen (gcf) documente par Kreyol-MT ===
    1807 lignes  CREOLORAL      (Narrative)
    1559 lignes  MiBelNouvel    (Bible)
    1540 lignes  Tatoeba        (Narrative)
    1099 lignes  PwovebKreyol   (Narrative)
     252 lignes  APICS          (Educational)
      70 lignes  Tatoeba        (Other/Mix)
      64 lignes  LegoMT         (Other/Mix)
      52 lignes  kapes          (Educational)
      24 lignes  Wikipedia      (Other/Mix)
  ------
    6467 lignes AU TOTAL, toutes sources confondues

  creole haitien (hat) pour comparaison : 6030673 lignes  =  933x plus
```

**6 467 lignes de créole guadeloupéen contre 6 030 673 de créole haïtien : un rapport de
933.** Voilà le mécanisme. Le modèle a appris `gcf` sur un millième des données de `ht`.
Le signal qui le distingue est donc mince — et les accents en sont la part portante.
Retirez-les, et la marge tombe de +56,6 à +1,1 : le modèle hésite, et un rapport de 933
décide à sa place.

Troisième élément, mesuré : **l'autre détecteur libre courant ne connaît aucun créole.**

```
py3langid 0.4.0 : 142 langues | gcf=True ht=True gcr=True
lingua          :  75 langues | creoles: AUCUN
```

### 4.3 Le verdict, et la règle qui en sort

**La confusion ne tient pas.** `py3langid` reconnaît le créole guadeloupéen 10 fois sur 10
sur du texte correctement accentué, avec une marge confortable qui croît avec la longueur.
L'exigence « Langues » du prompt est **tenable avec un outil gratuit**, et elle ne
disqualifie pas la chaîne.

**Mais elle tient à une condition d'ingénierie, et une seule :**

> **Ne jamais dépouiller les accents avant la détection de langue, et ne jamais indexer
> le créole sans ses accents.**

Cette règle est entrée dans le code livré, à deux endroits :

- `extraction.langue_avant_normalisation` est contraint à `1` : **le schéma refuse**
  d'enregistrer une détection faite après normalisation.
- l'index plein texte est déclaré `tokenize = 'unicode61'`, **sans** `remove_diacritics`.
  **La première version de mon propre socle utilisait `remove_diacritics 2`** — un bogue
  silencieux qui aurait dégradé le créole sans jamais lever d'erreur. Je l'ai trouvé parce
  que j'ai fait la mesure, pas parce que je l'ai deviné.

C'est le résultat le plus directement rentable de tout mon travail : une ligne de
configuration par défaut, parfaitement raisonnable pour le français, détruisait
silencieusement une des six exigences.

### 4.4 Ce qui reste ouvert, et ce qu'il faudrait pour le fermer

**Les 10 phrases sont de moi.** Je ne suis pas locuteur, et mon créole est peut-être plus
proche de la norme écrite que des avis réels. Ce qui est établi : le **mécanisme** (accents
porteurs, rapport de données 933:1) et la **règle d'ingénierie**, qui tient quel que soit
le taux. Ce qui n'est pas établi : le **taux** sur des avis authentiques, avec leurs
fautes, leur graphie libre et leurs abréviations — et c'est là que les accents manquent
le plus souvent dans la vraie vie.

**Ce qu'il faudrait pour trancher complètement, et c'est petit :** le découpage `gcf` de
Kreyol-MT, soit **6 467 lignes** réelles, code MIT et données en Creative Commons pour la
part Tatoeba et CC-BY pour APICS. Un téléchargement. Les hôtes nécessaires sont en
section 7. Avec cela, mon banc tourne tel quel et le taux devient opposable en une heure.

---

## 5. La règle du loyer appliquée aux quatre outils

Rappel de la règle, posée dans mon premier retour : *on loue quand il existe un service ou
un libre qui tient l'étalon, que son coût annuel est inférieur à 10 % du revenu récurrent
qu'il débloque, et qu'on pourrait le remplacer en moins de 30 jours. On ne reconstruit
jamais de la cryptographie, jamais un organe déjà tenu par le libre, jamais un organe
qu'aucun client n'a payé.*

### 5.1 Outil 1 — Veille à provenance prouvée

| | |
|---|---|
| **Louer** | **Rien.** Aucun serveur, aucun service tiers. SQLite et FTS5 sont dans la bibliothèque standard de Python |
| **Assembler** | `trafilatura` (Apache-2.0, F1 = 0,916 mesuré) · `py3langid` (BSD, 142 langues dont `gcf`) · SQLite FTS5 (200 000 documents en 28,2 s, mesuré) |
| **Construire** | La chaîne de provenance et le registre de qualification. **FAIT** : 375 lignes de schéma, 326 de collecteur, 122 de vérificateur. 21/21 assertions prouvées |
| **Reste à faire** | La qualification juridique des trois sources (lecture, pas code) · le filtrage Guadeloupe de BODACC et DECP (connaissance de terrain) |

### 5.2 Outil 2 — Publication sociale

| | |
|---|---|
| **Louer** | **Le coffre à secrets.** 97,8 années-auteur sur OpenBao/Vault. Interdiction absolue de l'écrire |
| **Assembler** | **Rien de satisfaisant.** Postiz couvre 30 plateformes mais en AGPL-3.0, et les exigences guadeloupéennes obligent à modifier donc la clause 13 mord. Mixpost est MIT mais c'est le palier gratuit d'un produit commercial, 3 à 4 plateformes, en PHP |
| **Construire** | L'orchestrateur minimal. **FAIT** : 215 lignes, 3 plateformes, relecture humaine imposée au niveau SQL, fuseau UTC-4 explicite, journal des accès. ~70 lignes par plateforme supplémentaire |
| **Le vrai coût** | **Un dossier d'approbation par plateforme**, et le délai de la plateforme. Délais inconnus de moi (D5). C'est le chemin critique, et il est **calendaire** |

### 5.3 Outil 3 — Avis

| | |
|---|---|
| **Louer** | **L'accès.** Le guichet 2 chez Google Business Profile est la seule voie connue donnant les avis complets au titulaire mandaté |
| **Assembler** | **Rien trouvé en libre.** C'est le seul des quatre outils sans brique libre identifiée |
| **Construire** | Un capteur par plateforme, la réponse, la modération. La **table est faite** avec ses champs irrécupérables ; le collecteur reste à écrire |
| **Le vrai coût** | Le mandat écrit, et le plafond de 5 avis des interfaces publiques (**cran C, D3** — à vérifier en priorité, voir relance 1). Si le plafond est confirmé, l'étalon « part des avis captés » n'est calculable que chez Google, sous mandat |

### 5.4 Outil 4 — Blog

| | |
|---|---|
| **Louer** | L'hébergement. Rien d'autre |
| **Assembler** | Un générateur de site statique libre et permissif. Le choix n'est pas fait et n'est pas urgent |
| **Construire** | **Presque rien.** La table `article` est faite. Le blog est un **rendu** de cette table : les mêmes assertions qui nourrissent le rapport hebdomadaire nourrissent les billets |
| **Le vrai coût** | Rédactionnel, pas technique. Et la relecture humaine, que le schéma impose déjà |

### 5.5 Le chiffre que Laurent attend — et la forme honnête de ce chiffre

**Ce que je peux donner, parce que je l'ai mesuré.** Après application de la règle du loyer,
le code de la suite complète est de l'ordre de **1 200 lignes déjà écrites et tournées**,
plus **environ 70 lignes par plateforme de publication supplémentaire** et **un capteur
d'avis par plateforme**. Sur les huit organes du prompt : quatre sont assemblés depuis du
libre permissif, un est loué et interdit à l'écriture, un est un rendu, et **un seul reste
un vrai chantier — le capteur d'avis.**

**Ce que je refuse de donner, et pourquoi ce refus est utile.** Je ne convertis pas ces
lignes en jours : ce serait du cran D déguisé en budget, exactement ce que mon premier
retour reproche au prompt. Et surtout, **ce ne serait pas le bon chiffre.**

**Le chiffre juste, et c'est le résultat de cette section : le chemin critique de la suite
complète n'est pas un effort, c'est un calendrier.** Trois postes le composent, et aucun
ne se raccourcit en travaillant plus :

| Poste | Unité réelle | Se réduit-il avec plus de monde ? |
|---|---|---|
| Approbation des applications par les plateformes | un dossier par plateforme, puis **le délai de la plateforme** | **Non.** On attend |
| Mandat écrit du titulaire pour les avis | une signature par client | **Non.** Rythme du client |
| Lecture et qualification des licences et conditions, source par source | une fiche par source | Un peu, et c'est de la lecture |

**Conséquence d'ordonnancement, et c'est la décision que ce chiffre impose : déposer les
dossiers d'approbation des plateformes MAINTENANT**, pendant que le socle tourne et que
les premières sources se qualifient. Le code se rattrape ; le délai d'une plateforme ne se
rattrape pas. Si l'on écrit l'orchestrateur avant de déposer les dossiers, on attend deux
fois.

Et la règle du loyer donne elle-même l'ordre : **outil 1 (fait) → outil 4, le blog (un
rendu, presque gratuit) → outil 2, la publication (le code est fait, on attend les
approbations) → outil 3, les avis (le seul vrai chantier, et le seul qui exige un mandat).**
Le prompt plaçait les avis au cœur. Ils sont le plus coûteux et le plus tardif.

---

## 6. Ce que mes deux relances donnent

### RELANCE 1 — anti-oubli, avec la question corrigée

#### Qu'as-tu oublié — ce que j'ai réellement écarté, sans quota

**1 — Les corpus de créole guadeloupéen réels.** Tatoeba, HuggingFace, le découpage `gcf`
de Kreyol-MT. Écartés **parce que bloqués** : `downloads.tatoeba.org`, `huggingface.co` et
`tatoeba.org` répondent 403 au CONNECT. J'ai cloné le dépôt Kreyol-MT depuis GitHub mais il
ne contient que la documentation (108 Ko de fichiers README), pas le texte. Conséquence
assumée : mon verdict créole établit le mécanisme et la règle d'ingénierie, pas le taux.

**2 — Elasticsearch et OpenSearch**, alors que Docker est installé. Écartés par arbitrage
de temps, comme dans mon premier retour, et je n'ai pas corrigé cet angle mort. Je ne sais
toujours pas ce que vaut FTS5 contre un vrai moteur. La conclusion « ne rien installer »
tient sur l'absence de besoin démontré, pas sur une supériorité mesurée.

**3 — Les autres extracteurs** (resiliparse, goose3, readability). Toujours écartés, même
raison, même aveu : je n'ai pas démontré que trafilatura est le meilleur libre.

**4 — Mixpost comme solution réelle.** Écarté après lecture, et c'est un écart motivé :
MIT vérifié, mais palier gratuit d'un produit commercial, 3 à 4 plateformes, pile PHP
étrangère au socle. Je l'ai écarté *après* avoir cloné et lu, pas avant.

**5 — La parade « deux processus séparés » pour l'AGPL.** Je la nomme en 3.1 et je refuse
de m'appuyer dessus : c'est un jugement juridique, pas une propriété technique, et mon
premier retour interdit de décider d'un guichet ou d'une licence sur un cran D.

**6 — Le portail de la préfecture comme source du guichet 6.** Écarté volontairement et
**gardé dans le registre comme contre-exemple** : institutionnel ne veut pas dire ouvert.

#### Que n'as-tu pas vu

- **Aucune source guadeloupéenne.** Rien n'a changé : tout mon banc est local ou fictif.
- **Le volume hebdomadaire réel de BODACC et DECP pour la Guadeloupe.** C'est le trou qui
  décide si l'outil 1 se vend. Voir la question corrigée ci-dessous.
- **Les délais d'approbation des plateformes**, qui sont le chemin critique des outils 2 et 3.
- **Le plafond de 5 avis**, toujours en cran C depuis mon premier retour.
- **Le débit d'annotation humaine.** Toujours inconnu, toujours non estimé.
- **Les dépendances transitives** de trafilatura et py3langid : j'ai lu les licences
  racines, pas l'arbre.

#### Laquelle de mes conclusions, si elle est fausse, coûte le plus cher — et comment la tester pour moins de cent euros

**La conclusion la plus coûteuse si elle est fausse : « les trois sources en ouverture
déclarée suffisent à un produit de veille vendable ».** Si elle est fausse, tout le chemin
dégradé s'écroule. On revient à la presse, donc au guichet 4 payant dont je ne connais pas
le prix, ou aux avis, qui exigent un mandat et dont l'étalon est peut-être non mesurable.
C'est la conclusion sur laquelle reposent l'ordre de construction, le jalon de revenu et
l'argument commercial entier.

**Le test, et il coûte zéro euro.** Pas de licence à acheter, pas d'abonnement, pas d'outil.

1. Télécharger quatre semaines d'extraits BODACC et DECP filtrés sur la Guadeloupe.
   Gratuit, Licence Ouverte 2.0, réutilisation commerciale autorisée.
2. Les passer dans le socle livré et produire **quatre rapports hebdomadaires réels**.
   Le code existe, il tourne en 7,1 secondes.
3. Compter : **combien de lignes par semaine ?** En dessous d'une dizaine d'assertions
   utiles, un rapport hebdomadaire ne se vend pas et la conclusion est fausse.
4. Montrer les quatre rapports à cinq établissements et poser **une seule question** :
   « paieriez-vous cinquante euros par mois pour recevoir ceci chaque lundi ? »

Coût : **zéro euro**, deux à trois jours de calendrier, aucune compétence technique après
l'étape 2. Et le résultat est décisif dans les deux sens : si le volume est là et que deux
établissements sur cinq disent oui, l'ordre de construction de la section 5 est validé et
le premier revenu arrive avant toute dépense. Si le volume n'est pas là, on l'apprend pour
rien plutôt que pour six mois de travail.

**Deuxième conclusion la plus coûteuse : le plafond de 5 avis (cran C, D3).** Elle décide
si l'étalon « part des avis captés » existe, donc si l'outil 3 est mesurable. **Test à
moins de cent euros :** ouvrir un projet chez Google, activer l'interface Places, appeler
le détail d'un seul établissement guadeloupéen, et **compter les avis renvoyés**. Le
crédit d'essai couvre largement un appel. Résultat en cran A-usage, en une heure, pour
quelques centimes. **C'est le meilleur rapport valeur/coût de toute ma liste, et je n'ai
pas pu le faire : la sortie réseau est bloquée.**

**Troisième : ma lecture de la clause 13 de l'AGPL (D4).** Si elle est fausse dans le sens
défavorable, une installation non modifiée oblige déjà à publier. La partie gratuite du
test est faite — la licence est lue et citée. Le reste est une question à un juriste, et je
ne prétends pas qu'elle tient dans cent euros.

### RELANCE 2 — preuve, étalon et guichet

| # | Ligne | Testé avec quoi, date | Obtenu | Validé ou recopié | Opposable, rejouable par un tiers ? | Cran |
|---|---|---|---|---|---|---|
| R1 | Socle installé de bout en bout en **7,1 s**, 12 captures, 21 assertions | `bash install.sh` sur le socle livré, Python 3.11.15, 2026-10-02 | sortie collée §1.2 | mesuré par moi | **Oui** pour le temps et les compteurs. **Non** pour toute extrapolation à un client réel : banc local, source fictive | **A-usage** |
| R2 | **21/21 assertions prouvées** : archive intacte, extraction reproduite, citation présente | `python3 verifier.py --toutes`, 2026-10-02 | sortie collée §1.3 | mesuré par moi | **Oui, et c'est ma meilleure ligne.** Le contrôle est une propriété du code, indépendante du corpus : il reste vrai sur sources guadeloupéennes | **A-mesure** |
| R3 | Le schéma **refuse** un secret collé dans `acces_confie` | `INSERT` d'un faux jeton `ya29.…`, 2026-10-02 | `CHECK constraint failed: reference_coffre LIKE 'coffre://%'` | mesuré par moi | Oui | **A-usage** |
| R4 | Le schéma **refuse** d'envoyer un contenu IA sans relecteur nommé | `publier.py programmer 3` avant relecture, 2026-10-02 | `REFUSE par le schema : contenu genere par IA : relecture humaine nommee obligatoire avant envoi` | mesuré par moi | Oui | **A-usage** |
| R5 | Conversion de fuseau : 10:00 local Guadeloupe = **14:00 UTC** | `publier.py programmer 1 --local "2026-10-02 10:00"` | `local 2026-10-02 10:00 (UTC-4) = UTC 2026-10-02T14:00Z` | mesuré par moi | Oui | **A-usage** |
| R6 | Orchestrateur minimal : **215 lignes**, 3 plateformes, 2 envois sur 3, le 3e refusé en 403 « application non approuvée » | `publier.py` contre bouchon local, 2026-10-02 | sortie collée §3.3 | mesuré par moi | **Le compte de lignes, oui. Les taux, non** : le bouchon est de moi, le 403 est simulé. Il illustre le vrai obstacle, il ne le mesure pas | **A-usage** pour les lignes · **D** pour les délais d'approbation |
| R7 | **Licence Ouverte 2.0** : réutilisation commerciale autorisée, **droit sui generis cédé**, attribution = nom du concédant + date de dernière mise à jour | Clone de `etalab/licence-ouverte`, fichier `LO.md` lu intégralement, 2026-10-02 | citations collées §2.2 | **recopié** d'un document primaire que j'ai lu | **Oui.** Dépôt public d'Etalab, fichier lisible par quiconque | **B** |
| R8 | **AGPL-3.0 clause 13** : l'obligation s'ouvre sur « if you modify the Program » et porte sur « the Corresponding Source of your version » | Fichier `LICENSE` du dépôt Postiz, clause 13 lue intégralement, 2026-10-02 | texte collé §3.1 | **recopié** d'un document primaire lu | **Oui** pour le texte. **Non** pour mon interprétation, qui reste une lecture | **B** pour le texte · **D4** pour l'interprétation |
| R9 | **Mixpost est MIT**, **trypost est AGPL-3.0**, et Mixpost est le palier **Lite** d'un produit commercial, 3-4 plateformes | Clones de profondeur 1, fichiers `LICENSE.md` et `README.md` lus, 2026-10-02 | tableau §3.2, citation ligne 71 du README | **recopié** de documents primaires lus | Oui | **B** |
| R10 | **Postiz couvre 30+ plateformes** · 9 156 lignes PHP dans Mixpost | `find` et `grep` sur les clones, 2026-10-02 | listes §3.2 | mesuré par moi sur les dépôts | Oui | **A-usage** |
| R11 | **gcf reconnu 10/10 avec accents, 6/10 sans** ; marge médiane +56,6 → +1,1 ; fr/en/es stables | `py3langid` 0.4.0, 10 phrases, avec et sans accents, 2026-10-02 | sortie collée §4.1 | mesuré par moi | **Le script, oui** — rejouable à l'identique. **Le corpus, non** : les 10 phrases sont de moi, je ne suis pas locuteur, n=10. **Le mécanisme est établi, le taux ne l'est pas** | **A-usage** pour l'effet des accents · **C** pour le taux sur avis réels |
| R12 | **6 467 lignes de gcf au total** contre **6 030 673 de ht — rapport de 933** | `csv` de `scripts/count/counter.csv` du dépôt Kreyol-MT (MIT), 2026-10-02 | sortie collée §4.2 | **comptage à moi** sur un fichier primaire du dépôt | **Oui.** Dépôt public, comptage trivial à refaire | **A-mesure** adossé à **B** |
| R13 | **`lingua` (75 langues) ne connaît aucun créole** ; `py3langid` en a 142 dont `gcf`, `ht`, `gcr` | Inventaire des classes des deux modèles, 2026-10-02 | sortie collée §4.2 | mesuré par moi | Oui | **A-usage** |
| R14 | Les trois sources (BODACC, DECP, Météo-France) sont sous Licence Ouverte 2.0 | **non testé** — `data.gouv.fr` et consorts bloqués | rien | **recopié de ma mémoire** | **Non** | **D1** |
| R15 | Plafond de 5 avis chez Google et TripAdvisor | **non testé**, aucune clé, aucun appel | extraits de recherche, dont des vendeurs de moissonnage | **recopié**, de sources intéressées | **Non** | **C / D3** |

**Mon étalon est-il opposable ?** Pour R2, R3, R4, R5, R12 : oui, un tiers rejoue à
l'identique avec le code et les dépôts publics. Pour R1, R6, R11 : le script est rejouable
mais **le corpus est de moi**, donc l'étalon n'est pas opposable sur le fond — et aucun
n'est guadeloupéen. **Aucun de mes bancs ne satisfait l'exigence du prompt « le jeu
d'épreuve doit être guadeloupéen, réel, et figé avant toute construction ».** Je ne
prétends nulle part le contraire.

**Par quel guichet accèdent les acteurs que je cite ?**

| Acteur | Guichet | Comment je le sais |
|---|---|---|
| Mon propre socle | **Guichet 6 déclaré** pour les trois sources visées, **aucun** dans le banc (serveur local que j'ai généré) | A-usage |
| Postiz, Mixpost, trypost | **Sans objet** : ce sont des orchestrateurs, le guichet dépend de l'approbation obtenue par celui qui les installe | Lecture du code, B |
| Google Business Profile | **Guichet 2**, mandat du titulaire — avis complets au gestionnaire vérifié | **C**, non vérifié |
| TripAdvisor Content API | **Guichet 1**, partenariat approuvé, et plafonné | **C**, non vérifié |
| Presse locale | **Guichet 4**, licence payante — établi par l'agent juridique, intégré dans `sources.json` | Non vérifié par moi |
| BODACC, DECP, Météo-France | **Guichet 6** revendiqué, **licence du jeu non lue** | **D1** |

**Bilan de crans : 2 lignes en A-mesure, 7 en A-usage, 3 en B, 1 en C, 2 en D** — plus les
6 lignes D déclarées en section 0. Ce qui est solide : le socle, ses garde-fous, le rejeu,
l'effet des accents, le rapport 933:1, et les licences lues. Ce qui est fragile et doit
être vérifié avant toute décision : **les licences des trois jeux de données (D1), le
plafond de 5 avis (D3/C), et mon interprétation de la clause 13 (D4).**

---

## 7. Les hôtes à ouvrir — à demander une fois, et bien

Liste exacte, par usage, pour que l'ouverture soit demandée en une fois. Tous répondent
aujourd'hui **403 au CONNECT**.

**Indispensables — sans eux, les temps 1 et 2 de la méthode restent hors de portée**

| Hôte | Ce qu'il débloque |
|---|---|
| `www.data.gouv.fr`, `data.economie.gouv.fr`, `meteo.data.gouv.fr`, `bodacc-datadila.opendatasoft.com` | **Fait passer les trois sources de D1 à B** et permet le test à zéro euro de la relance 1 |
| `www.etalab.gouv.fr` | La page de la licence, en complément du dépôt GitHub déjà lu |
| `la1ere.francetvinfo.fr`, `www.rci.fm`, `www.karibinfo.com`, `www.franceantilles.fr` | Le jeu d'épreuve guadeloupéen réel. Pour **mesurer**, même si la presse est écartée de la collecte |
| `www.guadeloupe.gouv.fr`, `www.guadeloupe.cci.fr`, `www.regionguadeloupe.fr`, `www.meteofrance.gp` | Sources institutionnelles locales, et la requalification du 5b en 6 ou l'inverse |

**Pour trancher les questions encore ouvertes**

| Hôte | Ce qu'il débloque |
|---|---|
| `developers.google.com`, `business.google.com` | **Le plafond de 5 avis et les conditions du guichet 2.** Priorité : c'est ma ligne C la plus coûteuse |
| `tripadvisor-content-api.readme.io`, `developer-tripadvisor.com` | Idem pour TripAdvisor |
| `connectivity.booking.com` | Les seuils du guichet 1, aujourd'hui en C |
| `curia.europa.eu`, `eur-lex.europa.eu`, `www.legifrance.gouv.fr` | Les deux décisions de la section 2.5 du prompt, aujourd'hui en D |
| `huggingface.co`, `downloads.tatoeba.org`, `tatoeba.org` | **Les 6 467 lignes de créole guadeloupéen réel.** Ferme définitivement le verdict créole |
| `www.brandwatch.com`, `www.meltwater.com`, `www.revinate.com`, `www.trustyou.com` | Les pages de tarifs des éditeurs : fait passer le temps 2 de C à B |

**Déjà atteignables, et c'est ce qui a sauvé ce travail :** `github.com`,
`raw.githubusercontent.com`, `pypi.org`, `files.pythonhosted.org`. Tout mon cran A et mes
trois lignes B en viennent. **Leçon de méthode : quand le web est fermé, les dépôts
publics et les registres de paquets restent une voie d'accès à des documents primaires.**

---

## 8. Les cinq colonnes

### 1. MCP à installer

| MCP | Ce qu'il débloque | Prérequis |
|---|---|---|
| **Récupération web avec sortie autorisée** | Le blocage central. Sans lui, ni jeu d'épreuve guadeloupéen, ni licence vérifiée, ni plafond d'avis tranché | La liste blanche de la section 7 |
| **MCP données ouvertes françaises** | BODACC, DECP, Sirene, météo par interface plutôt que par moissonnage. Alimente directement la table `source` du socle | Jeton d'interface ; licence lue source par source |
| **MCP Google Business Profile** | Le seul guichet 2 outillé pour les avis : avis complets et réponse, pour les établissements qui mandatent | Validation Google, mandat écrit, coffre loué |
| **MCP coffre à secrets** (OpenBao ou coffre infonuagique géré) | Remplit `acces_confie` sans jamais que le socle détienne un secret. L'organe loué, jamais écrit | Un coffre provisionné |
| **MCP juridique** (Légifrance, EUR-Lex, CJUE) | Fait passer de D à B les deux décisions de la section 2.5, que la règle 4.2 exige en B pour tout choix de guichet | Sortie réseau |

### 2. Logiciels manquants

| Manquant | Pourquoi il bloque |
|---|---|
| **La sortie réseau de la section 7** | Cause première de tout ce qui reste en C et en D |
| **Le découpage `gcf` de Kreyol-MT** — 6 467 lignes | Ferme le verdict créole. Mon banc tourne tel quel dessus |
| **Un extrait réel de BODACC et DECP sur la Guadeloupe** | Le test à zéro euro de la relance 1. Décide si l'outil 1 se vend |
| **Un coffre à secrets provisionné** | Rend `acces_confie` opérationnelle. À louer, jamais à écrire |
| **Elasticsearch ou OpenSearch en conteneur** | Docker est là, je ne l'ai toujours pas utilisé. Rendrait la comparaison d'index bilatérale |
| **Un deuxième extracteur** (resiliparse, goose3) | Pour que « adopter trafilatura » soit un verdict et non un défaut de comparaison |
| **Un chronomètre d'annotation** — 10 pages minutées | Transforme le budget du jeu d'épreuve d'inconnu en chiffre. Toujours le manquant le plus rentable |

### 3. Outils déjà disponibles et non exploités

| Déjà là | Ce qu'il fait |
|---|---|
| **SQLite 3.45.1 avec FTS5, dans Python** | L'organe Index à coût nul. 200 000 documents en 28,2 s. **Le socle livré n'installe aucune base de données** |
| **`hashlib` + `gzip` de la bibliothèque standard** | Toute la chaîne de provenance : 21/21 assertions prouvées, archives nommées par leur empreinte |
| **`datetime` avec fuseau explicite** | UTC-4 sans heure d'été, vérifié : 10:00 local = 14:00 UTC |
| **Les déclencheurs et contraintes de SQLite** | Les obligations légales imposées **au niveau des données**, donc valables pour tout programme qui écrit dans la base — pas seulement le mien |
| **trafilatura (Apache-2.0) et py3langid (BSD)** | Les deux seules dépendances. F1 = 0,916 et 142 langues dont `gcf` |
| **`github.com` et `pypi.org`, atteignables** | La voie d'accès aux documents primaires quand le web est fermé : licences, corpus, textes de référence |
| **Docker 29.6.2, PostgreSQL 16.14, Node 22** | Installés, toujours inutilisés. Le socle n'en a pas besoin, et c'est un résultat |

### 4. IA et produits existants qui font ce travail, et à quel prix

Prix en **cran C**, pages d'éditeurs inaccessibles. La règle 4.2 interdit d'y fonder une décision.

| Qui | Organe | Prix rapporté | Cran | Guichet |
|---|---|---|---|---|
| Revinate | Avis | ~4 $/chambre/mois, plancher ~399 $ | **C** | Inconnu |
| TrustYou | Avis | 75 à 350 $/établissement/mois | **C** | Inconnu |
| ReviewPro (Shiji) | Avis | Sur devis | **C** | Inconnu |
| Meltwater, Brandwatch, Talkwalker | Veille presse | Non public, sans essai en libre-service | **C** | Guichet 4 avancé, non vérifié |
| **Postiz** | Publication, 30+ plateformes | Gratuit à installer — **AGPL-3.0** | **B** | Par plateforme, approbation requise |
| **Mixpost Lite** | Publication, 3-4 plateformes | Gratuit — **MIT**, palier gratuit d'un produit commercial | **B** | Idem |
| **trafilatura** | Extraction | Gratuit — Apache-2.0, F1 = 0,916 mesuré | **A-mesure** | Sans objet |
| **py3langid** | Langue, 142 dont `gcf` | Gratuit — BSD | **A-usage** | Sans objet |
| **OpenBao** | Coffre à secrets | Gratuit à installer — MPL-2.0, 97,8 années-auteur en face | **B** | Sans objet |
| **Le socle livré** | Veille à provenance prouvée | **Gratuit, 1 183 lignes, 2 dépendances** | **A-mesure** | Guichet 6 |

**Ce que cette colonne dit.** Les concurrents facturent 75 à 350 $ par établissement et par
mois pour l'organe Avis — celui dont l'étalon est peut-être non mesurable et qui exige un
mandat. Tous les organes techniques sont gratuits. **L'argent est du côté du guichet et de
l'approbation, jamais du côté du code.** C'est pourquoi l'ordre de construction de la
section 5 met les avis en dernier et les dossiers d'approbation en premier.

### 5. Futurs possibles à douze mois — ⏳ non advenus, donc non décidables

- ⏳ **Un corpus annoté de créole guadeloupéen digne du nom.** 6 467 lignes aujourd'hui
  contre 6 030 673 pour le haïtien. Le constituer et le publier ferait de ce projet la
  référence de son domaine — et c'est une autre façon de vendre la provenance.
- ⏳ **Un détecteur robuste au créole non accentué.** Le besoin est réel : les vrais avis
  sont mal accentués, et c'est exactement là que la marge tombe à +1,1. Douze mois de
  modèles multilingues peuvent le résoudre. **En attendant, la règle « ne jamais dépouiller
  les accents » est la parade, et elle est gratuite.**
- ⏳ **Évolution des plafonds d'avis.** Mon premier retour notait qu'un socle dépendant
  d'une défense technique casse sans préavis ; le corollaire vaut ici : **un étalon qui
  dépend d'un plafond d'interface vieillit aussi vite.** Tout étalon doit porter sa date de
  validité, pas seulement sa date de mesure. La table `mesure` du socle a les champs pour
  cela.
- ⏳ **Rédaction par grand modèle de langage, à coût d'inférence en baisse.** Le schéma
  l'attend déjà : `genere_par_ia`, `modele_ia`, `version_modele_ia`, `mention_ia_affichee`,
  et la relecture imposée par déclencheur. **Vigilance : une rédaction par modèle fabrique
  du texte absent de la source, donc incompatible avec la provenance, qui est l'avantage
  du projet.** D'où `assertions_json` sur `publication` et `article` : un contenu généré
  doit pointer les assertions qui le fondent, sinon il n'a pas sa place dans ce produit.
- ⏳ **Un cadre européen d'accès aux données de plateformes**, qui pourrait ouvrir un
  septième guichet. Aucune source primaire, EUR-Lex bloqué. **Cran D, veille pour V1,
  jamais un fondement.**

---

*Fin de la relance. Document cible non modifié. `03-methode.md` non modifié. Aucun commit git.*
*Code livré dans `/home/user/moteurs-et-outils/socle/` — 1 183 lignes, 2 dépendances, installation mesurée à 7,1 s.*
