# SOCLE — fondation des quatre outils

Version 1 — 2 octobre 2026

**Ce que c'est.** La couche de collecte à provenance prouvée sur laquelle viennent se
poser les trois autres outils du périmètre : publication sociale, gestion des avis, blog.
Ce n'est **pas** un produit fini. C'est l'étape un, et c'est la seule étape dont les
trois suivantes dépendent toutes.

**Pourquoi elle vient d'abord.** Les trois autres outils publient des affirmations.
Une affirmation sans provenance est une opinion, et une affirmation fausse publiée au
nom d'un client détruit la relation qui donne accès au guichet 2. La provenance n'est
donc pas une fonctionnalité parmi d'autres : c'est la condition des trois autres.

**Ce qu'elle coûte.** Installation complète mesurée : **7,1 secondes**, section
« Temps d'installation » ci-dessous. Aucun serveur, aucun service tiers, un fichier.

---

## 1. Installation

```bash
cd socle
python3 -m pip install trafilatura py3langid     # 2 dépendances, rien d'autre
python3 socle.py init                            # crée socle.db depuis schema.sql
python3 socle.py sources sources.json            # charge le registre de qualification
python3 socle.py collecte --max 200              # collecte, extrait, hache, indexe
python3 socle.py assertions                      # fabrique les assertions
python3 socle.py rapport --jours 7               # écrit rapport-AAAA-SNN.md
python3 socle.py etalons                         # les étalons, chiffrés
```

Prérequis : Python 3.11. SQLite est dans la bibliothèque standard, FTS5 compris —
il n'y a **ni serveur de base de données, ni moteur de recherche à installer**.

Pour voir la chaîne tourner sans accès réseau sortant :

```bash
python3 banc/generer.py
python3 -m http.server 8731 --bind 127.0.0.1 --directory banc/site &
python3 socle.py sources sources-demo.json
python3 socle.py collecte --max 40
```

### Temps d'installation, mesuré

Chronométré le 2 octobre 2026, conteneur Linux 6.18, 4 cœurs, Python 3.11.15,
dépendances déjà en cache :

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

**Ce que ces 7,1 secondes ne contiennent pas, et il faut le dire.** Elles mesurent
l'installation du logiciel, pas la mise en service chez un client. Ne sont pas
mesurés, et ne sont pas estimés ici : la qualification juridique de chaque source
(lecture de la licence et des conditions, une fiche par source), la signature du
mandat quand le volet avis arrive, et le réglage des débits. Le logiciel s'installe
en secondes ; **la mise en service est un travail de lecture, pas de code.**

---

## 2. Le schéma de provenance — quel champ, quelle empreinte, quel horodatage

Le principe tient en une phrase : **une capture est un fait immuable, tout le reste
en dérive et se recalcule.** Un déclencheur SQL interdit toute modification d'une
capture. Si une page change, on ajoute une capture, on n'écrase jamais l'ancienne.

### La chaîne de provenance, maillon par maillon

| Table | Ce qu'elle fixe | Champs qui portent la preuve |
|---|---|---|
| `source` | D'où on a le droit de collecter | `guichet`, `licence_spdx`, `licence_lue_le`, `attribution_texte`, `verdict`, `motif_verdict` |
| `capture` | Ce qui est **réellement** arrivé | `sha256_corps` (empreinte de l'octet-à-octet reçu), `ts_capture_utc`, `chemin_archive`, `http_statut`, `octets`, `agent_utilisateur`, `version_collecteur` |
| `extraction` | Comment on en a tiré du texte | `outil`, `version_outil`, `parametres_json`, `sha256_texte`, `langue_code`, `langue_avant_normalisation` |
| `assertion` | Ce qui sera publié | `citation_exacte`, `offset_debut`, `offset_fin`, `genere_par_ia`, `relu_par_humain`, `relecteur`, `ts_relecture_utc` |

**L'empreinte.** `sha256_corps` est le SHA-256 du corps HTTP tel qu'il est arrivé,
avant tout décodage. Le fichier original est conservé compressé dans
`archives/<2 premiers caractères>/<sha256>.gz`. Le nom du fichier **est** son empreinte :
une archive renommée ou altérée se détecte immédiatement.

**L'horodatage.** `ts_capture_utc` est en ISO 8601 avec `Z`. **Tout est stocké en UTC,
sans exception.** La Guadeloupe est à UTC-4 toute l'année, sans heure d'été : le rendu
en heure locale se fait à l'affichage, et le fuseau est déclaré explicitement
(`publication.fuseau`). Un champ d'heure locale sans fuseau déclaré est un bogue qui
se révèle au changement d'heure métropolitain.

### Comment on rejoue une ligne un an plus tard

```bash
python3 verifier.py 10        # une assertion
python3 verifier.py --toutes  # toute la base
```

Trois contrôles indépendants, pour que l'on sache **lequel** a bougé :

1. **Archive intacte** — on recalcule le SHA-256 du fichier conservé et on le compare
   à celui enregistré. S'il tombe, c'est l'archive qui a été altérée, pas la source.
2. **Extraction reproductible** — on relance l'extracteur avec `outil`,
   `version_outil` et `parametres_json` **exacts**, et on compare `sha256_texte`.
   S'il tombe alors que l'archive est intacte, c'est l'outil qui a changé — et la
   version attendue est affichée.
3. **Citation présente** — l'extrait verbatim est bien dans le texte, aux offsets
   enregistrés.

Sortie réelle, 2 octobre 2026 :

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
source dit aujourd'hui. Comparer à l'état actuel, c'est une nouvelle capture.

---

## 3. Ce que le schéma prévoit DÈS MAINTENANT pour les trois outils à venir

Un champ oublié aujourd'hui coûte une migration dans six mois. Pire : trois champs de
cette liste portent des données **irrécupérables après coup**. Ils existent avant leur
usage, volontairement.

### Irrécupérables — à capter à l'origine ou perdus pour toujours

| Champ | Table | Pourquoi il ne se rattrape pas |
|---|---|---|
| `date_experience_consommation` | `avis` | **La date de l'expérience de consommation ne se reconstitue pas.** Si on ne la capte pas au moment de la collecte de l'avis, elle est perdue. Le champ compagnon `date_experience_origine` est obligatoire et contraint à quatre valeurs — `champ_plateforme`, `declaratif_client`, `deduite`, `absente_a_la_source` — pour qu'on sache toujours **d'où elle vient**. « Absente à la source » est une réponse licite ; une absence silencieuse ne l'est pas |
| `relu_par_humain`, `relecteur`, `ts_relecture_utc` | `assertion`, `publication`, `article` | La trace de relecture humaine **avant** publication. Après l'envoi, on ne peut plus prouver qu'il y a eu relecture. Un déclencheur SQL refuse de passer une publication générée par IA en `programme` ou `envoye` si le relecteur n'est pas nommé |
| `genere_par_ia`, `mention_ia_affichee`, `modele_ia`, `version_modele_ia` | `assertion`, `publication`, `article` | La mention d'un contenu généré. Six mois plus tard, personne ne saura plus quelle ligne sortait d'un modèle ni duquel |

### Déjà en place pour les trois outils

| Outil à venir | Tables prêtes | Ce qui est déjà tenu |
|---|---|---|
| **Publication sociale** | `publication`, `acces_confie`, `journal_acces` | File avec statuts, `assertions_json` qui relie le contenu publié à sa provenance, heure UTC + heure locale + fuseau déclaré, compteur de tentatives, code d'erreur, journal de tout accès aux identifiants confiés |
| **Avis** | `avis` | Note et son échelle (une note sur 5 et une note sur 10 ne se mélangent pas), langue, date de publication **et** date d'expérience, motif de non-publication et horodatage de modération, réponse avec sa relecture et son envoi |
| **Blog** | `article` | Statuts brouillon / à relire / publié / retiré, `assertions_json`, langue, URL publiée |
| **Les trois** | `client` | **Le cloisonnement par client existe dès la première ligne**, avec un seul client. L'ajouter plus tard imposerait de réécrire toutes les requêtes du produit |
| **Les trois** | `mesure` | La doctrine de preuve en base : une mesure sans `n`, sans intervalle de confiance, sans empreinte de jeu d'épreuve et sans `cran_preuve` est refusée. Une contrainte vérifie que le jeu a été figé **avant** la mesure |
| **Obligation du 2.3** | `demande_retrait` | « Retrait sous demande de l'éditeur, procédure écrite et tenue ». Une procédure sans table est une promesse |

### Ce que le schéma interdit, par construction

`acces_confie` **ne contient aucun secret**. Elle ne porte qu'une référence vers un
coffre loué, et des contraintes `CHECK` refusent ce qui ressemble à un secret collé
par erreur. Preuve exécutée :

```
garde-fou OK : secret refuse par le schema -> CHECK constraint failed: reference_coffre LIKE 'coffre://%'
```

**L'organe « garde des accès confiés » n'est pas construit, et ne doit pas l'être** :
97,8 années-auteur mesurées sur OpenBao/Vault. On loue un coffre, le socle n'en détient
que l'adresse, et `journal_acces` garde qui a demandé quoi, quand, et avec quel résultat.

---

## 4. Le rapport de veille hebdomadaire

`python3 socle.py rapport --jours 7` écrit `rapport-AAAA-SNN.md`. Format réel, extrait
du rapport produit le 2 octobre 2026 :

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
| Assertions dans la base | 21 |
| Part remontée à une source primaire | 100.0 % |
| Part datée | 100.0 % |
| Part rejouable à l'identique | 100.0 % |
| Assertions générées par IA | 0 |

## Sources mobilisées et leurs licences

| Source | Guichet | Licence | Licence lue le | Attribution |
|---|---|---|---|---|
| Banc local de demonstration | 6 | CC0-1.0 | 2026-10-02 | Banc local — pages generees… |
```

**Les quatre choses qui font la valeur de ce format**, et qu'aucun concurrent n'affiche :

1. Chaque ligne porte son URL, son horodatage UTC de captation, et les 16 premiers
   caractères de l'empreinte de la page. Le client peut demander le rejeu de n'importe
   quelle ligne, et obtenir une réponse en une commande.
2. Le rapport se termine par **son propre contrôle de provenance**, chiffré. Il
   s'audite lui-même.
3. Le tableau des sources porte la **licence, sa date de lecture et l'attribution
   exacte**. La Licence Ouverte 2.0 exige le nom du concédant *et la date de dernière
   mise à jour* : la colonne existe pour cela, et l'obligation est tenue dans le
   livrable, pas dans une annexe.
4. La ligne sur l'absence de génération par modèle de langage est **calculée depuis la
   base**, pas déclarée à la main.

Seules les captures en HTTP 200 nourrissent des assertions : une page d'erreur est un
fait de provenance valide, ce n'est pas une source d'affirmation.

---

## 5. La leçon mesurée qui est entrée dans le code : ne jamais dépouiller les accents

Mesure du 2 octobre 2026, `py3langid` 0.4.0, 10 phrases en créole guadeloupéen,
même texte avec puis sans accents :

```
  gcf correctement reconnu AVEC accents : 10/10   marge mediane +56.6
  gcf correctement reconnu SANS accents :  6/10   marge mediane  +1.1
  pertes causees par le seul depouillement des accents : 4/10
  ou va le texte depouille : {'gcf': 6, 'ht': 4}   (ht = creole haitien)

  fr, en, es : STABLE dans les deux cas
```

Deux conséquences, toutes deux dans le code :

- `extraction.langue_avant_normalisation` est contraint à `1`. Le schéma **refuse**
  d'enregistrer une détection de langue faite après normalisation.
- l'index plein texte est déclaré `tokenize = 'unicode61'` **sans**
  `remove_diacritics`. La première version de ce socle utilisait
  `remove_diacritics 2` : c'était un bogue silencieux qui aurait dégradé le créole
  sans jamais lever d'erreur.

La recherche insensible aux accents se fait côté requête, jamais en détruisant l'index.

---

## 6. L'orchestrateur de publication minimal

`publier.py`, **215 lignes non vides**, trois plateformes. Écrit pour chiffrer une
question : que coûte le minimum, plutôt que de reprendre un orchestrateur de trente
plateformes sous copyleft réseau.

```bash
python3 banc/bouchon_plateformes.py &          # bouchon local des interfaces
python3 publier.py ajouter --plateforme mastodon --texte "…" --assertions 1,2
python3 publier.py ajouter --plateforme linkedin --texte "…" --ia
python3 publier.py relire 3 --relecteur "Nom"
python3 publier.py programmer 1 --local "2026-10-05 08:30"
python3 publier.py envoyer
python3 publier.py bilan
```

Sortie réelle, et les trois points à retenir :

```
=== tentative de programmer le contenu IA SANS relecture ===
REFUSE par le schema : contenu genere par IA : relecture humaine nommee obligatoire avant envoi

publication 1 programmee  local 2026-10-02 10:00 (UTC-4)  =  UTC 2026-10-02T14:00Z

  1 mastodon  ENVOYE   http=201 distant=dist-1000
  2 facebook  ENVOYE   http=201 distant=dist-1001
  3 linkedin  ECHEC    http=403 {"error":"application non approuvee par la plateforme"}

  taux de publication reussie : 2/3 = 66.7 %
  contenus IA envoyes sans relecture nommee (doit valoir 0) : 0

=== Journal des acces confies ===
  2026-10-02T19:44:34Z  mastodon  publication  accorde   par publier 1.0
```

1. **Le refus vient du schéma, pas du programme.** Un déclencheur SQL interdit
   l'envoi d'un contenu généré sans relecteur nommé. Un autre programme qui écrirait
   dans la même base serait soumis à la même règle.
2. **La conversion de fuseau est explicite et vérifiable** : 10:00 local = 14:00 UTC.
3. **Le 403 du bouchon est le vrai sujet.** Le code de publication n'est pas le coût
   de cet outil : le coût est l'approbation de l'application par chaque plateforme.
   215 lignes ne font pas approuver une application.

---

## 7. Limites honnêtes de cette version

- **Aucune source guadeloupéenne réelle n'a été collectée.** La politique de sortie
  réseau de l'environnement d'analyse refuse les hôtes locaux en 403 au CONNECT. Le
  banc tourne sur un portail fictif généré par `banc/generer.py`. Les débits, les
  défenses anti-robot, le HTML réel et les taux d'extraction sur pages locales ne sont
  **pas** mesurés.
- **Les licences du fichier `sources.json` sont en cran D**, et le fichier le déclare
  en tête. Le **texte** de la Licence Ouverte 2.0 est lu et vérifié (cran B, dépôt
  `etalab/licence-ouverte`) ; son **attachement** à chaque jeu de données ne l'est pas,
  `data.gouv.fr` étant bloqué. Règle tenue dans le code : *ne pas lancer le collecteur
  sur une source dont `licence_lue_le` est nul.*
- Le collecteur est séquentiel et mono-processus. Suffisant pour quelques dizaines de
  sources institutionnelles ; à revoir au-delà, et seulement alors.
- Pas d'ordonnanceur, pas d'interface web, pas d'authentification. Une tâche planifiée
  et un fichier Markdown suffisent au premier client, et il faut résister à les
  remplacer avant qu'un client l'ait demandé.

## 8. Inventaire des fichiers

Comptes relevés par `grep -cve '^\s*$'` le 2 octobre 2026 :

| Fichier | Lignes non vides | Rôle |
|---|---|---|
| `schema.sql` | 375 | 24 objets : 12 tables déclarées (+ la table FTS5 et ses tables d'ombre), 2 vues, 4 déclencheurs |
| `socle.py` | 326 | collecte, extraction, provenance, index, assertions, rapport, étalons |
| `verifier.py` | 122 | rejeu d'une ligne, trois contrôles indépendants |
| `publier.py` | 215 | orchestrateur de publication, trois plateformes |
| `banc/generer.py` | 128 | portail fictif multilingue, 4 langues dont gcf |
| `banc/bouchon_plateformes.py` | 17 | bouchon des interfaces de plateformes |
| `sources.json` | — | registre de qualification, une fiche par source |

**Total du code et du schéma livrés : 1 183 lignes non vides**, commentaires et
documentation inclus — dont 375 de schéma SQL commenté, 215 pour la publication et 145
pour le banc de démonstration. La chaîne de collecte proprement dite — découverte,
extraction, provenance, index, rapport — tient dans les 326 lignes de `socle.py`.

Dépendances externes : `trafilatura` (Apache-2.0), `py3langid` (BSD). Rien d'autre.
