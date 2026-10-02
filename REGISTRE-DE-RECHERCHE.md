# Registre de recherche

Ouvert le 2 octobre 2026, à la demande de Laurent Cieutat : garantir que toute recherche est consignée.

**Ce registre ne porte pas les conclusions** — elles sont dans `REGISTRE-DE-DEMARCHE.md`. Il porte **les recherches elles-mêmes** : où on est allé, ce qu'on a trouvé, ce qu'on n'a pas trouvé, et ce qui a été refusé.

---

## 1 — Ce qui est garanti, et ce qui ne l'est pas

Réponse franche avant l'inventaire.

| Objet | Garanti ? | Pourquoi |
|---|---|---|
| Les **sources citées** dans les travaux | **Oui** — inventaire ci-dessous, extrait mécaniquement des fichiers, jamais de mémoire | Elles sont écrites dans les fichiers |
| Les **hôtes refusés** par le réseau | **Oui** — chaque lecteur les a déclarés | Déclaration systématique exigée |
| Les **documents non lus** qui décidaient | **Oui** | Déclarés et portés au registre de démarche |
| Les **recherches infructueuses** | **Partiellement** — celles que les lecteurs ont déclarées, pas les autres | Rien ne les obligeait à les lister toutes |
| Les **requêtes exactes** passées | **Non, et c'est irrécupérable pour le passé** | Elles vivent dans des transcriptions que je ne peux pas relire. Aucune n'a été consignée |

**Donc : garanti pour l'avenir par la règle de la section 5, inventorié pour le passé, et un trou nommé entre les deux.**

---

## 2 — La faute mesurée, et elle est de ma conduite

Mon barème exigeait, pour le cran de source primaire, « URL et date de consultation ». **Je ne l'ai vérifié sur aucun des douze retours reçus.**

Mesure, par comptage mécanique des fichiers — `A·1`, la commande est rejouable :

| Fichier | Affirmations en source primaire | Adresses citées | Verdict |
|---|---|---|---|
`02-marche.md` | 4 | **0** | Tous les chiffres de marché sans une adresse |
`02-marche-liberal.md` | 0 déclaré, mais cite un code déontologique textuellement | **0** | Citation littérale sans sa source |
`01-juridique-relance.md` | 15 | **1** | Contrats et documentations sans adresse |
`01-juridique.md` | 13 | 32 | Le seul correctement sourcé |
`05-technique.md` | 2 | 5 | Cohérent — il mesure plus qu'il ne cite |
`03-methode.md` · `03-methode-relance.md` | 9 | 7 | Cohérent |
`04-doctrine*.md` | 13 | 1 | **Légitime** : sa source primaire est le document attaqué, pas le web |
| **Total** | **56** | **48** | — |

**Conséquence appliquée sans adoucir** : toute affirmation en source primaire sans adresse ni date **redescend d'un cran de robustesse**. Elle reste utilisable comme piste, elle n'engage plus une dépense. Les faits concernés restent au registre de démarche, mais leur couple est à réviser.

---

## 3 — Inventaire des sources atteintes

28 hôtes distincts, 48 adresses. Extraction mécanique, rejouable par la commande inscrite en section 6.

| Domaine de recherche | Hôtes atteints |
|---|---|
| **Droit et jurisprudence** | legifrance.gouv.fr · eur-lex.europa.eu · supremecourt.uk · legalis.net · lexbase.fr · read-only.conseil-constitutionnel.fr · senat.fr · culture.gouv.fr |
| **Protection des données** | cnil.fr |
| **Droits de reproduction** | cfcopies.com · dvpresse.fr |
| **Plateformes** | partner.booking.com · developers.booking.com · admin.booking.com · support.google.com · developers.google.com · googleapis.com · mybusiness.googleapis.com · mybusinessaccountmanagement.googleapis.com |
| **Marché et acteurs** | doctrine.fr · hr-infos.fr · cornucopiae.fr · presse.leboncoincorporate.com |
| **Bancs locaux** (pas des sources) | 127.0.0.1:8731 · 127.0.0.1:8099 · presse.example.gp — **fictifs, fabriqués pour mesurer** |
| **Hors sujet, atteint puis écarté** | openpetition.de · gradeworkinggroup.org |

---

## 4 — Inventaire des refus et des trous

### Hôtes refusés par la politique réseau de l'environnement

**Statistique et institutions** : insee.fr · data.gouv.fr
**Droit** : legifrance.gouv.fr en direct · curia.europa.eu · bailii · eur-lex.europa.eu en direct
**Plateformes** : facebook.com · developers.google.com · connectivity.booking.com · tripadvisor · cnb.avocat.fr
**Guadeloupe, en totalité** : la1ere · RCI · karibinfo · France-Antilles · CCI · Météo-France Guadeloupe
**Autres** : en.wikipedia.org · HuggingFace · hébergeurs · brandwatch.com

**Conséquence tenue pour acquise : aucune mesure guadeloupéenne réelle n'a été possible. Zéro page locale captée.**

### Voies de contournement qui ont fonctionné, et c'est une leçon

— Les **forges de code publiques** donnent accès à des documents primaires quand le web est fermé : licences, textes officiels republiés, corpus. Tout le cran le plus haut d'un lecteur en vient
— Le site d'un **ordre professionnel** republie le texte intégral d'un règlement, avec sa jurisprudence annotée — plus riche que le document officiel inaccessible
— Un **récupérateur tiers** atteint ce que le réseau refuse en direct, mais **dégrade la preuve** : des libellés de colonnes ont disparu au passage et ont dû être inférés. Marqué comme tel par le lecteur, honnêtement

### Documents qui décidaient et n'ont pas été lus

| Document | Ce qu'il décidait | Sort |
|---|---|---|
| Fiche du vade-mecum d'un conseil national sur la publicité par internet | Si un avocat peut afficher des avis de clients | **Résolu autrement** — un code annoté, 34 pages lues en entier, s'est révélé plus riche |
| Fichiers statistiques détaillés par secteur | Le décompte fin par activité | Non ouverts, hôte refusé |
| Documentation d'une plateforme sociale majeure | Ses conditions d'accès | **Échec assumé**, hôte inatteignable, aucune voie trouvée |

---

## 5 — La règle pour l'avenir

Ce qui manque au passé ne manquera plus. Trois obligations, inscrites dans la compétence de conduite.

**1. Journal de requêtes.** Tout lecteur rend, en annexe de son fichier, la liste datée de ce qu'il a cherché : la requête ou l'adresse, l'outil employé, et le résultat en un mot — trouvé, rien, refusé. **Y compris les recherches qui n'ont rien donné : elles sont la moitié de l'information.**

**2. Pas d'adresse, pas de cran.** Une affirmation en source primaire sans adresse ni date de consultation est automatiquement ramenée d'un cran de robustesse. Le contrôle est mécanique, pas déclaratif : la commande de la section 6 compte les deux et affiche l'écart.

**3. L'écart est publié.** Le contrôle tourne à chaque clôture et son résultat entre ici. Un écart qui se creuse signale que la règle n'est plus tenue — sans que quiconque ait à s'en souvenir.

---

## 5 bis — Journaux de requêtes reçus

La règle de la section 5 s'applique à partir des lecteurs du plan de construction. Premier journal reçu, et il est conforme.

| Lecteur | Requêtes | Trouvé | Rien | Refusé | Crans revendiqués |
|---|---|---|---|---|---|
| Exécution du plan | **50** | 36 | 7 | 12 | 16 `A` sur sorties collées · **0 `B`** · 3 `C` dont 2 rétrogradées par lui-même · 3 `D` déclarées |

| Calendrier externe | **38** | 24 | 7 | 7 | **27 adresses primaires pour 27 affirmations — écart zéro** · 3 `D` déclarées |
| Trésorerie | **25** | 9 | 0 | 8 | **22 affirmations en source primaire pour 7 adresses → 15 lignes rétrogradées par lui-même**, le compte donné spontanément |
| Cohérence interne | court, assumé | — | — | — | Source primaire = le plan et le registre. **Trouvaille majeure hors brief, voir ci-dessous** |

### La faute que personne ne cherchait, et elle est de moi

Comptage mécanique : **les neuf retours de fond ne contiennent aucun couple à deux axes.** Soixante-cinq mentions d'un cran, toutes sur un seul axe. Les trente occurrences du barème à deux axes ne vivent que dans les deux fichiers de doctrine, et **les quatre retours écrits après sa réparation ne l'emploient pas**.

**Donc les trente-deux couples du plan de construction ont été attribués après coup par moi, à des affirmations d'autrui dont les auteurs n'avaient jamais déclaré la robustesse.** Deux conversions successives, aucune par l'auteur de la ligne.

Et l'écart que la compétence prévoit de publier **n'a jamais été calculé sur les crans : il vaut zéro sur neuf.** Le contrôle existait sur le papier, personne ne l'a lancé — moi le premier.

**Application** : neuf des quatorze lignes en source primaire du plan tombent. Les lignes porteuses passent de **27 sur 32 à 16 sur 32**. **Les quatre piliers de la convergence tombent**, trois venant du même fichier à zéro adresse.

### La correction de doctrine, et elle est capitale

La sanction appliquée symétriquement n'est pas freinante, **elle est dangereuse** : six des neuf lignes qui tombent sont des **interdictions**. Lever « on ne vend pas de gestion d'avis à un médecin » en attendant une meilleure preuve coûterait une faute disciplinaire chez le client.

> **La descente d'un cran s'applique à ce qui AUTORISE. Jamais à ce qui INTERDIT ou ARRÊTE.**

Deux corollaires gratuits : **un numéro de ligne vaut une adresse** pour une source interne au dépôt ; et **un calcul n'est pas une source** — le barème n'a pas de case pour le dérivé, il lui en faut une.

### Le geste au meilleur rendement de tout le projet

**Rouvrir une seule page** — le règlement professionnel republié par un ordre — **remonte sept lignes du plan d'un cran. Zéro euro, une demi-heure.**

### La limite que ce lecteur pose sur lui-même, et sur les huit autres

Il écrit : *même modèle que le producteur, donc une convergence entre nous est une corrélation*. Et : on lui a donné quatre contradictions à trouver, donc l'essentiel de son travail est de l'instruction, non de la découverte — **neuf trouvailles seulement ne venaient pas de son brief**, dont celle ci-dessus.

Deux règles qui en sortent, contre moi :
— **Interdire au producteur d'écrire l'angle du lecteur.** Un angle dicté produit de l'instruction déguisée en découverte
— Il faut **un lecteur qui n'est pas Claude** sur les sept lignes disciplinaires : toute la doctrine juridique du projet remonte à un seul modèle lisant des documents qu'il ne peut plus réouvrir

### Le trou que ce lecteur refuse de combler de mémoire, et il a raison

**Le verdict sur la licence à copyleft réseau** — la décision la plus structurante du volet publication — **n'a été vérifiée sur source par aucun lecteur.** Il refuse d'opiner sans la rouvrir. C'est le trou le mieux nommé de la session.


**Zéro source primaire revendiquée par le premier, et c'est honnête** : il a mesuré au lieu de citer. Le second affiche un **écart nul**, a rétrogradé une de ses propres lignes contre son intérêt d'argumentation, et a corrigé quatre manquements trouvés par son propre audit mécanique. **La règle tient dès son premier jour d'application.**

### La règle mord dès son premier jour, et contre son auteur

Le lecteur de la trésorerie a compté lui-même ses 22 affirmations en source primaire contre 7 adresses réelles, et **rétrogradé quinze de ses propres lignes**. Résultat le plus utile de l'opération : **le plancher de coût sur lequel le plan tarifait son produit tombe au cran le plus bas.** La sanction ne vide pas le travail — elle désigne exactement l'endroit où il ne fallait pas s'appuyer.

Il a aussi déclaré **huit hôtes refusés après une seule tentative chacun**, sans relance. Par la règle de la section ci-dessous, ce ne sont donc pas des refus : une heure de navigateur humain les règle tous les huit.

### La correction qui vaut pour tous les refus déjà inscrits

Le lecteur du calendrier a atteint **trois des cinq hôtes déclarés refusés** par les autres, via un outil de recherche tiers, et **les quatre résultats décisifs de son retour viennent tous de là**. Conséquence : **un refus inscrit après une seule tentative n'est pas un refus.** Les refus de la section 4 sont à relire sous cet angle. Règle ajoutée : **deux voies au minimum avant d'inscrire un refus.**

### Hôtes refusés par ce lecteur — à ne pas réessayer

developers.facebook.com · developers.google.com · business.google.com · linkedin.com · mastodon.social · data.gouv.fr · le portail des annonces commerciales en données ouvertes · legifrance.gouv.fr · insee.fr · le barreau de Guadeloupe · les services de l'État en Guadeloupe · learn.microsoft.com

## 6 — Le contrôle, rejouable

```
# Hôtes atteints, par fréquence
grep -ohE 'https?://[^ )"]+' critiques/*.md | sed -E 's#https?://##; s#/.*##; s#^www\.##' \
  | tr '[:upper:]' '[:lower:]' | sort | uniq -c | sort -rn

# L'écart : affirmations en source primaire contre adresses citées
grep -ohcE 'cran B|`B·|\bB·[0-9]' critiques/*.md | paste -sd+ | bc
grep -ohE 'https?://[^ )"]+' critiques/*.md | sort -u | wc -l
```

**Relevé du 2 octobre 2026** : 56 affirmations en source primaire · 48 adresses distinctes · écart de 8, et une répartition très inégale détaillée en section 2.
