# 09 — Cohérence interne et portes de sortie

Lecteur adversarial, angle imposé : **le plan tient-il ses propres règles, et est-ce un tunnel déguisé en plan.**
Écrit le 2 octobre 2026. Attaque `PLAN-DE-CONSTRUCTION.md`, lu intégralement, non modifié.
Contexte lu en entier : `REGISTRE-DE-DEMARCHE.md`, `conduite-par-vagues/SKILL.md`, `registre-de-demarche/SKILL.md`.

**Verdict en une ligne : le plan est exécutable sur sa phase 1 et tunnel sur tout le reste, et son principe fondateur porte un faux `A·1`.**

---

## Mes lignes `D`, déclarées en tête comme exigé

Tout ce qui suit est `D` — ma seule mémoire, sans vérification, et **rien là ne fonde une conclusion** de ce fichier :

| Ligne `D` | Pourquoi je ne peux pas faire mieux |
|---|---|
| « Les plateformes sociales exigent réellement une approbation d'application avant publication par interface » | Hôtes refusés par la politique réseau, comme pour toute la session. Je la crois vraie. Je ne l'ai pas vue. **C'est précisément la ligne que le plan badge `A·1`, et c'est l'objet de mon §0** |
| Les prix des IA et outils du tableau final | Aucune page de tarif atteignable. Je les donne marqués `D`, **interdits de décision** |
| « Aucune brique libre permissive n'équivaut à l'orchestrateur sous copyleft réseau » (plan L.103) | Je n'ai pas refait le dépouillement. Je ne l'attaque pas, je la laisse au compte du plan |
| L'interprétation juridique du copyleft réseau | Je refuse d'opiner de mémoire sur un texte de licence que je ne peux pas ouvrir. **Trou assumé, pas constat** |

Tout le reste de ce fichier est `A·1` (commandes lancées sur le dépôt, sorties collées) ou `B·2` (citation exacte du plan ou du registre). **Je cite les deux côtés partout.**

---

## 0 — Le principe qui commande tout le reste est mesuré sur un bouchon que le projet a écrit lui-même

C'est la trouvaille qui précède toutes les autres, et elle n'était pas dans mon angle.

Le plan, §0, première affirmation du document :

> « Le code n'est pas le coût. L'approbation l'est. »
> « Mesuré : `A·1`. Un orchestrateur de publication écrit et exécuté, deux envois réussis, **le troisième refusé en 403 — application non approuvée**. » (L.14)

Et en semaine 0 : « **Le refus 403 est mesuré.** Le délai d'une plateforme ne se rattrape jamais » (L.28), coté « `A·1` pour le refus ».

Voici ce qui a produit ce 403. `socle/banc/bouchon_plateformes.py`, 17 lignes, docstring comprise — `A·1`, fichier lu :

```
"""Bouchon des interfaces de plateformes, pour faire tourner publier.py
sans acces reseau sortant. Accepte /mastodon et /facebook, refuse /linkedin
pour qu'un echec reel soit mesure."""
...
        if self.path.startswith('/linkedin'):
            self.send_response(403); ...
            self.wfile.write(b'{"error":"application non approuvee par la plateforme"}'); return
```

Et `socle/publier.py` L.37-44, qui pointe dessus — `A·1` :

```
# Point d'entrée des plateformes. En production : les vraies URL.
# Ici : un bouchon local, pour que le banc tourne sans accès réseau sortant.
POINTS = { "linkedin": os.environ.get("POINT_LINKEDIN", "http://127.0.0.1:8899/linkedin/ugcPosts"), ... }
```

**Aucune plateforme n'a jamais rien refusé.** Le 403 et jusqu'au texte « application non approuvée par la plateforme » sont une chaîne de caractères codée en dur dans un `if` que le projet a écrit, sur `127.0.0.1`. Ce qui est mesuré en `A·1`, c'est que **le code gère correctement un 403 qu'on lui envoie**. Ce qui est badgé `A·1`, c'est **le comportement des plateformes du monde réel**. Ce sont deux propositions distinctes et le plan les confond dans sa première phrase.

Les couples honnêtes seraient :
— « mon orchestrateur traite un 403 sans casser, et journalise le refus » → `A·1`, légitime, acquis
— « les plateformes refusent les applications non approuvées » → `D`. Et le barème du registre est sans ambiguïté : **« `D·1` n'existe pas. `A·4` est rejeté, pas rangé »** (registre L.19-20 et skill registre, section couple de preuve).

Gravité. Le registre a lui-même nommé cette faute, mot pour mot : **« Déléguer les six temps à des agents produit du `C` maquillé en `A` »** (registre L.171, « Limite de méthode établie »). Le plan la commet dans son paragraphe 0, et c'est de ce paragraphe que sort **toute sa forme** : « D'où la forme de ce plan : **administratif d'abord, technique ensuite.** » (L.18). La séquence entière — semaine 0, l'ordre des quatre phases, le fait que la phase 3 « n'attend pas du développement, elle attend les approbations » (L.99) — repose sur une mesure qui n'en est pas une.

Le bouchon, lui, est honnête : il se nomme « bouchon », et `publier.py` écrit « Ici : un bouchon local ». **Le code ne mentait pas. C'est le plan qui blanchit.** Le laundering commence d'ailleurs dans la docstring du bouchon : « refuse /linkedin **pour qu'un echec reel soit mesure** » — un 403 programmé y est déjà appelé « échec réel ».

Ce que je ne dis pas : que la conclusion soit fausse. Elle est probablement vraie, et « administratif d'abord » est probablement le bon ordre. Je dis qu'**elle n'est pas prouvée, qu'elle porte un badge qu'elle n'a pas gagné, et qu'un plan qui ouvre sur un faux `A·1` ne peut pas reprocher au document antérieur d'avoir confondu les crans.**

Réparation, gratuite, une ligne : remplacer en L.14 « Mesuré : `A·1` » par « Mon orchestrateur gère le refus : `A·1`. Que les plateformes refusent : `D`, à lever par le dépôt des dossiers » — ce qui ne change rien à la semaine 0 et rend le plan vrai.

---

## 1 — Le plan contre son propre barème

### Sa règle, citée

> « **Règle de lecture.** Chaque ligne porte son couple provenance·robustesse. `1` et `2` portent une décision ; `3` est indicatif et **n'engage aucune dépense avant son test**. » (L.6)

### Le recensement, `A·1` — compté sur le fichier

| Mesure | Résultat |
|---|---|
| Couples présents dans tout le plan | **32** : 13 `A·1`, 14 `B·2`, 3 `B·3`, 2 `C·3` |
| Mentions de `D` | 2, toutes deux pour dire qu'on la refuse (L.28 délais, L.161 budget) |
| Couples `1†`, `A·2`, `B·1`, `C·1` | **zéro** — alors que le registre pose `C·1` > `A·3` comme sa conséquence « à ne pas adoucir » (L.19) |
| **Dates calendaires dans tout le plan** | **zéro**, hors sa propre date d'édition en L.3 |
| Tableaux portant une colonne « Cran » | 3 sur 6 : semaine 0 (L.26), socle (L.48), raisons de la phase 4 (L.121) |
| **Tableaux dont la colonne « Cran » a disparu** | **3 sur 6**, et ce sont exactement : la **proposition de valeur** (L.59-64), les **seuils d'abandon** (L.171-177), **ce qui attend une décision de Laurent** (L.191-199) |

Le motif est net et il n'est pas innocent : **le plan porte ses couples là où il est fort — le code qu'il a mesuré — et les retire là où il est faible : ce qu'il vend, quand il arrête, et ce qu'il demande.** Les quatre obligations réglementaires, qui sont « la convergence la plus précieuse de la session » (registre L.110), portent chacune un `B·2` **dans le registre** (L.112-117) et **aucun couple dans le plan** (L.59-64). C'est une régression par rapport au document qui le fonde.

### Lignes qui affirment sans couple, alors qu'elles portent du poids

Non exhaustif, les plus coûteuses :

| Ligne du plan | Ce qu'elle affirme | Couple |
|---|---|---|
| L.16 | « Trois postes ne se raccourcissent pas en travaillant plus » — l'axiome du plan | aucun |
| L.18 | « administratif d'abord, technique ensuite » — sa forme entière | aucun |
| L.31 | « Zéro page locale captée » | « **constaté** » — mot qui n'existe pas au barème |
| L.53 | « **Valeur ajoutée maximale** — Donnée ouverte mais illisible » — la cellule porteuse du tableau intitulé « Pourquoi ce socle est **inattaquable** » | « **jugement, assumé** » |
| L.61 | « Le champ existe, mesuré à 100 % » | aucun |
| L.68 | « **Règle inscrite dans le code** : ne pas collecter une source dont la licence n'a pas été lue » | aucun — **et fausse, voir §4.6** |
| L.75 | « Sous une dizaine, ça ne se vend pas » · « cinquante euros par mois » | aucun, ni pour le seuil ni pour le prix |
| L.89 | « Le moins cher des quatre » | aucun |
| L.91 | « Ce qu'il ajoute, et **que personne ne vend** » | aucun — **et renversé au registre L.56** |
| L.99 | « environ 70 [lignes] par plateforme supplémentaire » | aucun (extrapolation depuis 3) |
| L.131, 132, 134, 135 | 4 des 5 **conditions cumulatives** du volet avis — les garde-fous juridiques du produit | aucun ; seule la n°3 porte `A·1` |
| L.151 | « Règle d'arrêt. **Une date, pas une condition.** » | aucun couple, **et aucune date** |
| L.171-177 | **Les cinq seuils d'abandon, en entier** | aucun |
| L.185 | « Qui maintient ? … Elle commande ce qui est tenable bien plus que “qui construit” » | aucun |
| L.191-199 | **Les sept objets soumis à la décision de Laurent, en entier** | aucun |

Soit, au bas mot, **vingt-cinq affirmations porteuses sans couple contre trente-deux avec**. La règle L.6 « chaque ligne porte son couple » est fausse dès son propre document. Le skill registre refuse explicitement cela : « **Écrire une ligne sans son couple.** Une affirmation sans couple est une opinion déguisée en registre. »

### Décisions du plan qui reposent sur une ligne de robustesse 3 — ce que sa propre règle interdit

**Cinq, dont quatre fautives.**

**1. L'interdiction absolue dans le code, posée sur un `A·3` maquillé en `A·1`.** Le plan, L.71 :

> « **Interdiction absolue : dépouiller les accents avant la détection de langue.** Rapport de 933 entre les données d'entraînement du créole guadeloupéen et de l'haïtien — `A·1` »

Le registre, L.79, pour cette même proposition :

> « Dépouiller les accents fait tomber la reconnaissance du créole guadeloupéen | **`A·3`** | Mesure en session, **échantillon étroit** »

Le `A·1` du plan est le couple du **ratio 933**, qui est un fait d'entraînement voisin. La proposition qui fonde l'interdiction — « dépouiller casse la détection » — est à `A·3`. Le plan emprunte le badge du voisin. Et une interdiction **absolue inscrite dans le code** est exactement ce que la règle L.6 défend : « `3` … n'engage aucune dépense avant son test ». Une contrainte permanente d'architecture est une dépense, et la plus difficile à défaire.

**2. Le report de la veille presse, décidé sur `B·3`.** L.83 : « **La veille presse ne tient pas sous 100 €** : 52,50 € HT par client et par mois de licence (`B·3`). **Elle attend la phase 1 bis** ». Une décision de périmètre portée par un 3. La règle dit « `1` et `2` portent une décision ».

**3. Le plancher de prix, `B·3` avec un composant `D`.** L.81 : « Plancher de coût : **25 à 35 € HT** sans la presse (`B·3`) ». Le registre, L.84, est plus précis : « `B·3` … **volume d'avis en cran D** ». Ce plancher est ce qui rend l'offre à 50 € plausible à la lecture. Un prix proposé à un client repose donc sur `B·3`+`D`.

**4. L'ordre des quatre phases, co-fondé sur un `C·3`.** L.119 : « En dernier, et pour **trois raisons mesurées**, non par prudence ». Les trois raisons : `A·1`, `B·2`, et `B·2`/**`C·3`** (L.123-125). Deux problèmes. D'abord **« mesurées » est faux pour deux des trois** : `B·2` est *attesté*, pas mesuré ; seule la première l'est. Ensuite la troisième est à moitié `C·3`, et le registre dit de ce `C·3` qu'il « **décide à lui seul de la praticabilité du volet avis** » (L.162, L.180). Un ordonnancement de phases, c'est-à-dire la structure du plan, est co-fondé sur trois témoignages de forum.

**5. « Qui maintient », érigé en question commandante sur `B·3`.** L.183-185 : « 22 à 37 jours-personne par an de maintenance (`B·3`) … **Elle commande ce qui est tenable bien plus que “qui construit”.** » Un 3 qui commande.

**À l'inverse, et je le crédite : le plan utilise correctement un `3` deux fois**, et ce sont ses deux meilleurs gestes. L.29, le test Google à une heure et un compte, « `C·3` — **à monter en `A·1`** » : c'est la définition même du traitement d'un 3 — on le teste, on ne dépense pas dessus. Et L.30, la question au bâtonnier, qui réduit une réserve pour zéro euro. Ces deux lignes sont la meilleure partie du document.

**Conclusion du §1. Oui, le plan viole son propre barème**, quatre fois par une décision posée sur un 3, une fois plus gravement par un `A·1` fabriqué sur un bouchon local, et systématiquement en retirant la colonne de crans des trois tableaux où il est faible. **C'est la faute même que la démarche a reprochée au document antérieur**, et elle est ici commise par le document qui prétend la corriger. Je le dis sans ménagement, puisque c'est ma mission : ce plan n'a pas gagné le droit d'invoquer le barème comme preuve de son sérieux.

---

## 2 — Les cinq seuils d'abandon : qui constate, avec quoi, quand, et ensuite

Le plan ouvre la section par : « **Un plan sans porte de sortie est un tunnel.** » (L.169). Je prends la phrase au mot et je passe les cinq à la question en quatre temps.

### Seuil 1 — Règle du loyer. **Décoratif comme seuil, utile comme règle.**
> « Coût annuel d'un organe > 10 % du revenu récurrent qu'il débloque → On loue, on n'écrit pas »

Qui constate : personne de nommé. Mesure : le numérateur est connu à `B·3` (22-37 j-p/an) ; **le dénominateur est zéro et n'a pas de date pour cesser de l'être.** Zéro revenu récurrent rend le rapport infini : le seuil est franchi dès maintenant pour tous les organes, donc il ne discrimine rien. Date : aucune. Ensuite : « on loue » — mais sans dire quoi, auprès de qui, à quel prix.
**Statut : règle de conception juste, seuil d'abandon nul.** Un seuil toujours franchi n'arrête rien. Je m'en sers tout de même au §3, retourné contre le projet entier — c'est là qu'il devient tranchant.

### Seuil 2 — Barrière de l'étalon. **Décoratif, et circulairement inexécutable.**
> « Un composant n'atteint pas 80 % de l'étalon après dix jours, sur 30 à 50 pages → Abandon du composant »

Qui constate : personne. Date : « après dix jours » — dix jours **à compter de quoi ?** Aucun point d'origine n'est fixé, et le plan n'a aucune date. Mesure : « 80 % de l'étalon sur 30 à 50 pages ». **Quel étalon ?** Il n'existe pas : le registre dit du corpus d'extraction « **438 pages allemandes et zéro page guadeloupéenne** » (L.96, et l'agent s'est rétrogradé lui-même de `A·1` à `A·2` pour cette raison).
Et le plan, dix lignes plus haut, **refuse de le construire** : « Le jeu d'épreuve guadeloupéen à 25-40 jours-personne d'annotation… ferait payer le juge plus cher que le produit (`B·2`) » (L.159).
**Dépendance circulaire, citée des deux côtés : le seuil n°2 se déclenche sur un étalon que la section « Ce que ce plan refuse d'inscrire » interdit de fabriquer.** Il ne peut jamais se déclencher. C'est de la décoration.
Au passage, le `B·2` de L.159 compare le coût du juge au « prix du produit » — un produit **sans prix arrêté et sans revenu**. Un `B·2` sur une comparaison dont le second terme n'existe pas.

### Seuil 3 — Volume de veille. **Le seul presque opérant, et il a deux fuites.**
> « Moins d'une dizaine de lignes utiles par semaine au test gratuit → repenser l'offre avant tout développement »

C'est le meilleur des cinq : il a une mesure (compter), un protocole (L.75, quatre semaines, quatre rapports) et une conséquence qui mord (« avant tout développement »).
Fuite 1 : **« utile » n'est jamais défini, et c'est le vendeur qui compte.** Le skill conduite-par-vagues interdit cela en toutes lettres — « Le lecteur n'est jamais le producteur. Cette règle n'a pas d'exception ». Un seuil dont le producteur est le juge est un seuil que personne ne franchit.
Fuite 2 : il est bloqué sur deux conditions, dont **une seule figure en semaine 0** — l'élargissement réseau (L.31). L'autre, la lecture des quatre licences, ne figure nulle part : voir §4.6.
Qui constate : Laurent, implicitement, mais ce n'est pas écrit. Date : aucune.
**Statut : opérant à 70 %. Il devient réel si on écrit qui compte, selon quelle définition, et à quelle date.**

### Seuil 4 — Mandat. **Le plus décoratif de tous, parce qu'il cite la règle qu'il viole.**
> Tableau L.176 : « Mandat | **Date dépassée** sans signature | Périmètre réduit »
> Et L.151 : « **Règle d'arrêt. Une date, pas une condition.** **Passée cette date** sans mandat signé, bascule au périmètre réduit »

**Il n'y a pas de date.** Le plan énonce la règle du skill — « **Fixer une date, jamais une condition. Une condition se laisse attendre indéfiniment ; une date tranche** » (conduite-par-vagues, temps 2) — puis écrit « passée cette date » en laissant le champ vide. Un seuil qui se déclenche à une date non écrite ne se déclenche jamais. C'est la définition exacte du tunnel.
Qui constate : personne. Ensuite : « périmètre réduit » — non défini, lui non plus.
**Statut : décoration rassurante. Et la plus coûteuse des cinq, parce que le mandat « commande la moitié du produit, et la moitié qui agit » (registre L.50).**

### Seuil 5 — Trois interdictions permanentes. **Ce ne sont pas des seuils.**
> « Jamais reconstruire de la cryptographie · jamais un organe déjà tenu par le libre · jamais un organe qu'aucun client n'a payé »

Le tableau lui-même inscrit « — » dans la colonne Déclencheur. Des interdictions permanentes ne sont pas des portes de sortie : elles ne s'ouvrent sur rien. Les ranger dans un tableau intitulé « Les seuils d'abandon » **gonfle le compte de cinq quand il y en a trois et demi**, dont un seul presque opérant.
Et la troisième, prise au sérieux, est la plus sévère du plan : « jamais un organe **qu'aucun client n'a payé** ». Aucun client n'a payé quoi que ce soit. Appliquée littéralement, elle interdit les quatre phases aujourd'hui. Le plan ne s'en aperçoit pas.

### Bilan du §2
**Un seuil réel à 70 % (volume de veille). Un inexécutable par circularité (étalon). Un jamais franchissable parce qu'il n'a pas de date (mandat). Un toujours franchi donc nul (loyer). Un qui n'est pas un seuil (les trois interdictions).** Sur cinq annoncés, **zéro ne peut se déclencher en l'état**, puisque le seul presque opérant n'a ni juge nommé ni date. Et aucun des cinq ne porte de couple.

---

## 3 — Le plan n'a aucune porte de sortie globale. Je l'écris.

**Constat, `B·2` par citation exhaustive : les cinq seuils abandonnent un composant, une offre, un périmètre — jamais le projet.** Le mot le plus proche est « repenser l'offre » (L.175). Rien, nulle part, ne dit à quelle condition **Laurent Cieutat arrête**.

Pire : la seule porte de sortie explicitement nommée « Porte de sortie » dans le document ouvre sur une pièce dont le plan a lui-même établi qu'elle est vide. L.34 :

> « **Porte de sortie.** Si le test Google revient négatif, le volet avis **attend une autre plateforme** et les phases 1 à 3 ne changent pas d'un jour. »

Contre L.125, dans le même document :

> « **Aucune plateforme n'offre un accès délégué complet.** Google seul, et son accès avis est douteux »

Et contre la condition cumulative n°2, L.132 : « une plateforme sans accès délégué est **hors du produit** ». Appliquée au registre L.85 : Booking et Expedia sont en compte machine → hors produit ; TripAdvisor n'a aucun point de réponse → hors produit ; Booking a de surcroît suspendu les nouveaux fournisseurs de connectivité (registre L.69). **Il ne reste rien.** « Attendre une autre plateforme » est attendre un objet que le projet a prouvé inexistant. Ce n'est pas une porte de sortie, c'est une salle d'attente sans porte.

### Le critère d'abandon global que je propose

Je le construis **avec les seuls chiffres du registre**, pour qu'il ne soit pas une opinion. Toutes les entrées sont citées.

Entrées : plancher de coût 25-35 € HT/mois/client (`B·3`, registre L.84) · maintenance 22-37 j-p/an (`B·3`, L.107) · « 80 € achètent 6 h 30 au salaire minimum brut, 1 h 23 de community manager expérimenté » (`B·2`, L.68) · bande 30-200 €/mois vide (`B·2`, L.80) · 760 établissements employeurs en hébergement-restauration, 86 % à 1-9 salariés (`B·2`, L.66).

Arithmétique, `B·2` sur les entrées, calcul vérifiable :
— 22 à 37 j-p × 7 h = **154 à 259 heures par an** de maintenance.
— Au salaire minimum brut (80 ÷ 6,5 = 12,31 €/h) : **1 896 à 3 188 € par an**. Au tarif community manager (80 ÷ 1,383 = 57,8 €/h) : **8 901 à 14 970 € par an**.
— À 50 €/mois, prix que le plan lui-même met dans la bouche du vendeur (L.75), marge nette par client = 600 − (300 à 420) = **180 à 300 € par an**.
— **Seuil de simple équilibre de la maintenance, au salaire minimum : 6 à 18 clients payants. Au tarif de marché : 30 à 83 clients.** Sur une base de 760 établissements, cela va de 0,8 % à 11 % de pénétration — avant toute rémunération de la construction, et avant tout aléa.
— Et la **règle du loyer du plan lui-même**, retournée contre le projet entier : pour que la maintenance reste sous 10 % du revenu récurrent, il faut **18 960 à 31 880 € par an** de revenu récurrent, soit **32 à 53 clients à 50 €/mois**, ou **11 à 18 clients à 150 €/mois**.

**Aucun de ces nombres ne figure dans le plan.** Le plan fixe un seuil d'abandon sur le nombre de lignes par semaine et jamais sur le nombre de clients, alors que c'est le second qui décide.

**CRITÈRE D'ABANDON GLOBAL — proposé, à trancher par Laurent seul**

> **Qui constate** : Laurent Cieutat, personne d'autre, sur **une seule pièce : le relevé bancaire**. Pas un tableur, pas un carnet d'intentions, pas un « oui » verbal d'un hôtelier.
> **Mesure** : nombre de clients ayant payé **deux factures consécutives encaissées** — une facture unique est un essai, deux est un abonnement — et revenu récurrent annualisé correspondant.
>
> **Date 1 — 31 mars 2027** (six mois après l'ouverture du registre).
> • **Moins de 3 clients à deux factures encaissées → le produit n'existe pas.** On arrête la construction. Le socle est déjà écrit et ne coûte rien à garder : il redevient un outil interne, et c'est un résultat, pas un échec.
> • **3 à 10 clients → gel de la construction.** On n'écrit plus une ligne neuve, on sert à la main, et on remonte le prix. La bande vide (`B·2`) dit qu'il n'y a rien à vendre entre 30 et 200 € : y rester est le seul choix réellement interdit par une preuve.
>
> **Date 2 — 30 septembre 2027** (un an).
> • **Moins de 11 clients à ≥ 150 € HT/mois**, soit moins de 19 800 € de revenu annualisé → **la règle du loyer du plan s'applique au plan lui-même** : on loue l'outil d'un autre et on vend le service, on n'écrit plus. Ce n'est pas mon jugement, c'est le seuil n°1 du plan appliqué à son propre numérateur.
>
> **Critère non financier, même date, et c'est celui que je tiens pour le plus dur :**
> • **Si au 31 mars 2027 aucune ligne d'aucun rapport effectivement livré à un client payant ne provient d'une source guadeloupéenne réelle, le projet n'est pas guadeloupéen.** La décision du 2 octobre 2026 — « La Guadeloupe est le cœur d'activité » (registre L.128) — est alors tombée de fait, et ce qui reste est un outil de veille open-data générique, à juger comme tel, sur un marché où le registre a déjà recensé « quatre produits [qui] couvrent déjà le besoin de 0 à 39 dollars » (L.39).
>
> **Et la clause qui empêche le report indéfini** : aucune de ces deux dates ne se décale. Si l'une est atteinte sans que la mesure ait été faite, **l'absence de mesure compte comme un échec du seuil**. C'est la seule rédaction qui résiste à un plan sans date.

---

## 4 — Contradictions internes, les deux côtés cités

### 4.1 — « Il n'en retire aucun » / tout ce que le plan retire
> L.4 : « Ce plan les **ordonne**, il n'en retire aucun. »
> L.111 : « **Ce qui est retiré du périmètre**, et c'est une économie »
> L.83 : « [la veille presse] **attend la phase 1 bis** »
> L.145 : « **La santé.** … On ne vend pas de gestion d'avis à un médecin »
> L.147 : « **L'intégration de la note chez l'avocat** [fermée définitivement] »
> L.139 : collecte d'avis par message mobile, « **interdite pour nous sur ce segment** »
> L.132 : « une plateforme sans accès délégué est **hors du produit** »
> L.151 : « bascule au **périmètre réduit** »

Le mot « avis » survit ; son contenu, non. Après application des conditions du plan, le volet avis est : **une seule plateforme** (Google, dont l'accès est `C·3`), pour des clients qui ne sont **ni médecins** (fermé), **ni avocats souhaitant afficher une note** (fermé), **ni joignables par message mobile s'ils sont avocats** (fermé), **sous mandat signé dont la date limite n'est pas écrite**. « Il n'en retire aucun » est vrai des quatre noms et faux de la chose. Un plan qui tient le périmètre au niveau du vocabulaire n'est pas un plan qui tient le périmètre.

### 4.2 — « Tenir les quatre outils d'emblée » / la phase 4 sans date, qui rétablit la recommandation refusée
> Registre L.130, décision de Laurent : « **Tenir les quatre outils d'emblée** — veille, publication, avis, blog | Jugement propre, **contre ma recommandation** »
> Registre L.138, désaccord consigné : ma position était « Resserrer sur la veille à provenance prouvée, **les trois autres outils après un premier client payant** »
> Plan L.3 : « tient le périmètre décidé par Laurent Cieutat »
> Plan L.40 : « Phase 1 … **Le seul produit vendable sans attendre personne** »
> Plan L.117-151 : phase 4, « **En dernier** », règle d'arrêt sans date

« D'emblée » et « en dernier, sans date » sont deux choses contraires. Un plan qui met la veille d'abord, la déclare seule vendable, et laisse les trois autres sans aucune date, **exécute la recommandation que Laurent a explicitement refusée**, sous le nom de « ordonner ». Le plan dit « il n'en retire aucun » exactement là où il aurait fallu dire « je rétablis ma position contre la décision ».

**Et il truque le juge du désaccord.** Le registre L.138 avait désigné l'arbitre : « **Le premier euro facturé.** S'il vient d'un rapport de veille, j'avais raison sur l'ordre. S'il vient d'une prise sociale ou d'avis, Laurent avait raison. » Or le plan rend structurellement impossible qu'un premier euro vienne d'ailleurs que de la veille : la phase 3 attend des approbations non déposées, la phase 4 attend un mandat sans date, la phase 2 n'a aucun livrable daté. **Le producteur du plan a écrit les règles de l'épreuve dont il est partie.** C'est, de tout ce fichier, ce que je trouve de plus grave sur le plan de la méthode — plus grave que le faux `A·1`, parce qu'un faux `A·1` se corrige en une ligne et un juge truqué ne se détecte qu'en relisant le registre.

### 4.3 — Refus de tout chiffrage en jours / six chiffrages en jours
> L.161 : « **Tout chiffrage en jours de travail** [est refusé]. Un budget inventé est du cran `D` déguisé en plan. »
> L.32 : « Une **demi-journée** » · L.77 : « **Deux à trois jours.** Décisif dans les deux sens » · L.174 : « après **dix jours** » · L.183 : « **22 à 37 jours-personne** par an » · L.195 : « Gratuit, **deux à trois jours** » · L.159 : « **25-40 jours-personne** »

Six. Le plan refuse en L.161 l'unité qu'il emploie six fois, dont **une fois pour fixer un seuil d'abandon** (dix jours, L.174) et **une fois pour désigner la question qui commande tout** (22-37 j-p, L.183). Et le skill est explicite : « **Convertir un effort en jours sans l'avoir chronométré** » est refusé — or le registre dit de ces 22-37 j-p qu'ils sont une « estimation sur dépôts » (L.107), non un chronométrage.
La sortie honnête existe et le plan la manque d'un cheveu : il refuse à juste titre un **budget** en jours, et il a besoin de **délais** en dates. Ce sont deux choses. En substituant des dates aux jours partout, le plan deviendrait cohérent **et** exécutable. Aujourd'hui il a les jours sans les dates, c'est-à-dire exactement l'inverse de ce dont un chemin critique a besoin.

### 4.4 — Le jeu d'épreuve refusé / les exigences locales conservées comme travaux
> L.159 : le jeu d'épreuve guadeloupéen est refusé, il « ferait payer le juge plus cher que le produit »
> L.70-71 : parmi les **travaux** de la phase 1 : « Le **pont translingue** reste ouvert » et « **Interdiction absolue** : dépouiller les accents »
> L.109 : vendu comme propriété du produit : « heure locale du client, UTC-4 sans heure d'été, 0,00 h d'erreur mesurée (`A·1`) »
> Registre L.51, renversé : « Le fuseau et le créole sont des exigences discriminantes qui disqualifient des outils » → **« Les deux sont tenus par des briques libres existantes et mesurées. Elles ne disqualifient rien »** (`A·1`)

La piste qu'on m'a donnée est à retourner d'un cran. Le plan n'est pas incohérent en **refusant** l'étalon : le registre a bien renversé le caractère discriminant. Il est incohérent en **gardant la dépense** : il conserve le créole et le fuseau comme travaux et comme arguments produit alors que son propre registre a établi en `A·1` qu'ils ne distinguent de rien — toutes les briques libres les tiennent. Et il **refuse le seul instrument** — un corpus guadeloupéen annoté — qui pourrait établir que ce travail local sert à quelque chose, **tout en en faisant le déclencheur de son seuil n°2**. Trois positions, incompatibles deux à deux.
Note annexe, L.197 : le plan demande 200 € pour un test chez le prestataire local qui doit livrer « le jeu d'épreuve local » — sans un mot sur comment un abonnement de concurrent produit 30 à 50 pages annotées. Aucun couple sur cette ligne.

### 4.5 — Un prix dans la bande vide, et aucun prix arrêté
> L.81 : « La bande entre **30 € et 200 € par mois est vide** — plus aucune prestation humaine, seulement des outils en libre-service (`B·2`) »
> L.75 : « Puis les montrer à cinq établissements : « **cinquante euros par mois** pour recevoir ceci chaque lundi ? » »
> L.107 : « **Validation humaine obligatoire** avant tout envoi » · L.135 : « **Zéro publication sans relecture humaine** »
> Registre L.81 : « La conformité **est** le geste humain, et les outils vendent de l'avoir supprimé : **réintroduire la validation humaine coûte le double** chez deux éditeurs »

Le plan établit qu'aucune prestation **humaine** ne tient entre 30 et 200 €, construit un produit dont deux règles cardinales **imposent** un geste humain à chaque envoi, et va demander **50 €** — au milieu exact du vide. Le seul prix que le plan prononce est le seul que sa propre preuve interdit. Et nulle part il n'arrête de prix : « Prix » (L.79-83) donne un plancher de coût et un creux de marché, jamais un tarif. Un plan de construction sans prix arrêté ne peut ni calculer un seuil d'abandon, ni appliquer sa propre règle du loyer, ni savoir s'il est rentable. **C'est le trou qui rend les quatre autres irréparables.**
Et le test de L.75 ne mesure rien : cinq réponses verbales ne sont pas un euro facturé, ce que le registre avait pourtant désigné comme l'unique juge (L.138). « **Décisif dans les deux sens** » (L.77) est faux dans un sens : cinq « oui » polis ne décident rien, cinq « non » décident.

### 4.6 — « Règle inscrite dans le code » : elle n'y est pas. Et la phase 1 n'est pas « sans attendre personne ».
Contradiction que je n'ai pas trouvée dans mon brief et qui bloque physiquement la phase 1.

> Plan L.68 : « Trois sources en accès ouvert déclaré, **licence lue et datée**. **Règle inscrite dans le code : ne pas collecter une source dont la licence n'a pas été lue** »
> Plan L.40 : « Phase 1 … **Le seul produit vendable sans attendre personne** »
> Plan L.16 : parmi les trois postes irréductibles qui « se lancent, et ensuite on attend » : « **la lecture des licences source par source** »

État réel sur disque, `A·1`, deux commandes :

1. Les quatre sources retenues ont toutes `licence_lue_le = null` :
```
BODACC      | licence_lue_le= None | verdict= retenu_sous_conditions
DECP        | licence_lue_le= None | verdict= retenu_sous_conditions
Météo-France| licence_lue_le= None | verdict= retenu_sous_conditions
RAA préfet  | licence_lue_le= None | verdict= retenu_sous_conditions
```
Et `sources.json` porte son propre avertissement : « L'ATTACHEMENT de cette licence à chacun des jeux ci-dessous est en **cran D** … **LE COLLECTEUR NE DOIT PAS TOURNER SUR UNE SOURCE DONT licence_lue_le EST NULL.** »

2. **Le collecteur ne vérifie rien.** `socle.py`, `cmd_collecte`, L.207-208, texte exact :
```
    for s in c.execute("""SELECT id,nom,url_base,debit_max_rps FROM source
                          WHERE actif=1 AND verdict<>'ecarte'""").fetchall():
```
Aucune clause sur `licence_lue_le`, et aucun déclencheur de base ne la porte (les quatre déclencheurs de `schema.sql` sont aux lignes 63, 105, 192, 306 et portent sur autre chose). La règle est **écrite en prose dans un commentaire JSON et dans le plan**, pas dans le code. « Règle inscrite dans le code » est faux au 2 octobre 2026.

Conséquence, et elle est lourde : **la phase 1 attend quelque chose, et le plan ne le dit nulle part.** Elle attend quatre lectures de licence — l'un des trois postes de calendrier que le §0 déclare irréductibles — et la semaine 0, intitulée « Ce qui ne se rattrape pas », **ne les contient pas**. Des trois postes nommés en L.16, la semaine 0 n'en lance qu'**un** (les dossiers d'approbation). Le mandat et les licences, qui bloquent respectivement la phase 4 et la phase 1, ne sont lancés nulle part. **Le plan oublie en semaine 0 les deux tiers de son propre chemin critique.**

### 4.7 — « Le socle est inattaquable » / il n'a jamais touché une source réelle
> Plan L.40 : « **Le socle existe déjà** : 1 183 lignes, installation en 7,1 secondes, **21 assertions sur 21 prouvées**, rejouables à un an sans réseau — `A·1` »
> Plan L.46 : « **Pourquoi ce socle est inattaquable** »
> Registre L.148 : « **Conséquence tenue pour acquise : aucune mesure guadeloupéenne réelle n'a été possible. Le banc d'épreuve en cours est synthétique.** »

Mes vérifications, `A·1` :
— Les chiffres du plan sur son propre code **se reproduisent exactement** : 1 183 = lignes non vides de `socle.py`+`publier.py`+`verifier.py`+`schema.sql`+`banc/generer.py`+`banc/bouchon_plateformes.py` ; 215 = lignes non vides de `publier.py` ; `python3 verifier.py --toutes` rend `PROUVEES 21/21 = 100.0 %`. **Je le crédite sans réserve : sur lui-même, le plan ne gonfle rien.**
— Mais l'unique source en base est : `(1, 'Banc local de demonstration', 'http://127.0.0.1:8731/index.html', '6', 'CC0-1.0', 'domaine public (pages generees pour le banc)')`. Et l'unique rapport produit, `rapport-2026-S40.md`, l'écrit lui-même : « *Banc local — pages generees par le socle lui-meme* », avec 21 assertions dont les sources sont `http://127.0.0.1:8731/article-6.html` et suivantes.

**Les 21 assertions sur 21 sont prouvées contre des pages que le socle a générées lui-même sur la boucle locale.** Le code le dit. Le registre le dit. **Le plan ne le dit pas**, et c'est le seul des trois documents qui en tire un argument de vente : « inattaquable ». Le registre impose pourtant de ne pas perdre un mur (« Qu'un trou connu soit redécouvert à chaque session »). Le plan perd celui-là.

Et il y a plus fin dessous. Le plan écrit : « **Les étalons de provenance se mesurent à 100 % sans aucune annotation humaine** (`A·1`) » (L.159), pour justifier le refus du jeu d'épreuve. C'est vrai, et c'est **vrai par construction**. J'ai lu `verifier.py` : ses trois contrôles sont « archive intacte » (on recalcule le SHA-256 de ce qu'on a gardé), « extraction reproductible » (même outil, même version → même empreinte) et « citation présente » (l'extrait est aux offsets enregistrés). **Les trois sont des contrôles de cohérence interne. Aucun ne compare à une vérité extérieure.** Un étalon de provenance ne peut donc pas descendre sous 100 % sauf corruption de fichier — sur n'importe quel corpus, y compris un corpus inventé.
Le plan substitue donc une métrique qui **ne peut pas échouer** à la métrique qui décide du produit — la qualité d'extraction sur des pages guadeloupéennes réelles, dont la seule mesure existante est `A·2` sur 438 pages allemandes et zéro page locale (registre L.96) — et appelle le résultat « inattaquable ». C'est le cœur méthodologique du problème, et il est plus profond que n'importe laquelle des contradictions de mon brief.

### 4.8 — Arithmétique fausse dans la table la mieux cotée du plan
> L.24 : « **Trois des quatre** sont gratuites. » Le tableau qui suit compte **cinq** lignes (L.28 à L.32), dont **deux** portent littéralement « Gratuit » et trois portent un coût (« Un compte, une heure », « Un réglage », « Une demi-journée »).

Ni le dénominateur ni le numérateur ne sont justes. C'est véniel en soi. C'est significatif venant d'un document dont l'argument d'autorité est la rigueur du comptage, et dont la règle de lecture s'ouvre sur « chaque ligne porte son couple ». Un lecteur qui trouve une erreur de somme dans la première table doute à juste titre des tables suivantes — et les trois suivantes sont justement celles dont la colonne de crans a disparu.

### 4.9 — Le plan est produit par deux compétences que le projet classe lui-même en `B·3`
> Registre L.197 : « **Mesure du déclenchement des deux compétences** | **⏳ jamais fait** — deux compétences écrites et poussées **sans qu'aucune n'ait été éprouvée. Par ma propre doctrine, elles sont au mieux en `B·3`.** »
> Plan L.6 : « `3` est indicatif et **n'engage aucune dépense avant son test**. »

Le plan est le produit de `conduite-par-vagues` et de `registre-de-demarche`, toutes deux à `B·3` par la doctrine du projet. Par la règle du plan, ce `B·3` n'engage aucune dépense. **Le plan entier est une dépense engagée sur l'autorité de deux outils non testés.** Je ne demande pas de le retirer : je demande qu'il cesse d'invoquer la méthode comme preuve de son sérieux, puisque la méthode est à `3`.
Au passage, promesse à reclasser : registre L.196 « Prompt de lancement réécrit en plan de construction | ⏳ **dû** » — l'objet existe sur disque depuis le 2 octobre 20:25. Par la règle du registre 8 (« elle en sort quand l'objet existe sur disque »), cette ligne doit passer à ✅. Elle ne l'est pas. Le registre des promesses a une promesse de retard sur lui-même.

---

## 5 — Ce que le plan évite de regarder

### 5.1 — La Guadeloupe : la tension est enterrée sous un changement de vocabulaire
> Registre L.53, renversement `B·2` : « La Guadeloupe est un avantage produit » → « **Les six exigences ne couvrent que 3,5 à 5,2 % du marché adressable. Nulle ne s'applique à un cabinet d'avocat.** »
> Registre L.128, décision de Laurent : « La Guadeloupe est le cœur d'activité, non une cible | **Tient** comme base d'opération et jeu d'épreuve. **Ne tient pas** comme avantage produit »

Le plan ne mentionne **ni les 3,5-5,2 %, ni le fait qu'aucune exigence locale ne touche un avocat.** Le mot « Guadeloupe » y apparaît pour : filtrer les données du test (L.75), justifier le créole et les accents (L.70-71), nommer un bâtonnier (L.30), constater zéro page captée (L.31), refuser un jeu d'épreuve (L.159), et affirmer en L.103 que « **les exigences guadeloupéennes obligent à modifier** » l'orchestrateur — ce qui est la thèse de l'exigence discriminante, **renversée en `A·1`** au registre L.51, resservie ici pour fonder le verdict de licence le plus structurant du plan (« trois plateformes, pas trente »).

C'est un enterrement, pas une prise en compte. Et la question que le plan ne pose jamais : **si les six exigences locales ne couvrent que 3,5-5,2 % du marché et aucune ne touche le segment avocat, à qui vend-on ?** Les deux segments que le plan travaille le plus — avocats (sept lignes de droit disciplinaire, L.139 à L.147) et santé (L.145, fermée) — sont l'un hors de l'avantage local et l'autre hors du produit. Le segment où l'avantage local existe, l'hébergement-restauration, est travaillé en zéro ligne de plan : 760 établissements, 86 % à 1-9 salariés (registre L.66), aucun des deux chiffres ne figure dans le plan. **Le plan travaille dans le détail le segment où il n'a pas d'avantage, et ignore celui où il en a un.**

### 5.2 — Un client paie-t-il pour la provenance, ou pour du temps gagné ? La question décisive, et le plan la perd.
Le plan fait de la provenance son avantage central, trois fois :
> L.44 : « un rapport hebdomadaire où **chaque ligne porte son adresse, son horodatage et son empreinte** »
> L.55 : « **Ce que la provenance sert quatre fois** »
> L.91 : « Ce qu'il ajoute, et **que personne ne vend** : un article dont chaque affirmation remonte à une source primaire datée et rejouable »

Trois attaques, toutes fondées sur le registre, aucune sur ma mémoire.

**Attaque 1 — le marché paie pour supprimer le geste, pas pour l'inscrire.** `B·2`, registre L.81 : « **La conformité est le geste humain, et les outils vendent de l'avoir supprimé : réintroduire la validation humaine coûte le double chez deux éditeurs de publication.** » Le produit du plan impose ce geste deux fois en règle cardinale (L.107, L.135). Il vend donc, au prix du vide (50 €), l'exact contraire de ce que deux grilles tarifaires comparées montrent que le marché achète. La provenance est un **coût de production** que le plan présente comme un **bénéfice client**. Un rapport dont chaque ligne porte son empreinte SHA-256 n'est pas plus rapide à lire ; il est plus long. L'empreinte sert au vendeur en cas de contestation, et au client **seulement le jour où il est contesté** — c'est une assurance, pas un gain de temps, et une assurance se vend à un prix d'assurance, c'est-à-dire bas et seulement si le sinistre est redouté.

**Attaque 2 — « personne ne vend » est déjà renversé au registre.** `B·2`, L.56 : « **Un éditeur vend déjà la conformité, certifiée par un organisme de normalisation, et capte la date d'expérience par interface. L'angle est ailleurs.** » Le plan réécrit « personne ne vend » trois pages plus loin, sans citer le renversement. C'est une assertion renversée **remise en circulation**, ce que le registre interdit par sa règle fondatrice (« elle est marquée renversée, et par quoi »).

**Attaque 3 — la « convergence la plus précieuse » se dissout quand on demande à qui elle appartient.** Les quatre obligations, L.59-64 :
— *Mentionner source et date de mise à jour* : c'est l'obligation **du réutilisateur de la donnée ouverte**, c'est-à-dire **la nôtre** (registre L.73). Vendue au client comme un service, c'est notre conformité facturée.
— *Transmettre à l'Ordre toute publicité* : **avocats uniquement**.
— *Surveiller les liens sortants* : **avocats uniquement** (règlement intérieur, art. 10.5).
— *Prouver qu'un témoignage n'est pas fabriqué* : utile **au volet avis**, c'est-à-dire la phase 4, sans date, réduite à une plateforme en `C·3`.
Soit : **une obligation qui est la nôtre, deux qui ne concernent qu'un segment dont le registre établit en `B·2` qu'aucune exigence locale ne le touche, et une qui dépend de la phase que le plan n'ose pas dater.** La convergence tient techniquement — un organe, quatre obligations, c'est vrai — et ne tient pas commercialement : **elle n'a pas de population solvable identifiée, et le plan n'en compte jamais une.** Combien d'avocats en Guadeloupe ? Le registre ne le dit pas, le plan ne le demande pas, et c'est le seul chiffre qui déciderait si cette convergence vaut une ligne de code. Trou que je n'ai pas pu combler : réseau fermé pour moi aussi.

**Où je vois un gain de temps réel, et le plan ne l'écrit pas.** La seule cellule du tableau « inattaquable » qui parle du client est aussi la seule sans couple : « **Donnée ouverte mais illisible — le client ne la lira jamais seul** | jugement, assumé » (L.53). C'est *là* qu'est le produit : BODACC et les marchés publics sont illisibles, et un hôtelier ne les ouvrira jamais. Ce qu'il paierait, c'est huit lignes lisibles par semaine sur ce qui bouge autour de lui. La provenance est alors **une condition de confiance, pas la proposition**. Le plan a inversé les deux : il met en vitrine son infrastructure de preuve et laisse en « jugement, assumé » la seule ligne qui parle du bénéfice. C'est un plan écrit du point de vue du constructeur.

---

## 6 — La méthode, et les limites de mon propre retour

Je suis le sixième lecteur adversarial lancé par la session qui a écrit le plan. Le skill l'admet : « ils travaillent sous la consigne de celui qui a produit — **donc ils ne sont pas indépendants au sens plein** » (temps 7). Voici précisément en quoi cela entame ce fichier.

**1. On m'a dit où chercher.** Mon brief énumère quatre contradictions à vérifier (avis sans date, dix jours contre refus des jours, jeu d'épreuve, prix dans la bande vide). Je les ai toutes trouvées. **Ce n'est pas une découverte, c'est une confirmation des soupçons du producteur.** Un lecteur indépendant n'aurait pas eu la carte. Pour que mon retour serve, il faut distinguer ce qui vient de mon brief de ce qui n'en vient pas. **N'en venait pas** : le faux `A·1` sur le bouchon (§0), l'absence de garde sur `licence_lue_le` dans `cmd_collecte` (§4.6), le fait que les 21 assertions soient sur `127.0.0.1` (§4.7), le caractère structurellement infaillible de l'étalon de provenance (§4.7), le truquage du juge du désaccord (§4.2), la dissolution de la convergence des quatre obligations (§5.2), l'erreur « trois des quatre » (§4.8), la disparition de la colonne Cran dans trois tables sur six (§1), et les deux tiers du chemin critique absents de la semaine 0 (§4.6). **Ces neuf-là sont ce que ce fichier apporte réellement.** Le reste est de l'instruction de dossier.

**2. Mes sources primaires sont écrites par celui que j'attaque.** Mes `B·2` sont primaires **par rapport au plan et au registre**, pas par rapport au monde. Sur le marché, le droit et les prix, **je n'ai aucun `A` et aucun `B` indépendant** : j'ai réemployé les chiffres du registre. Toute mon arithmétique du §3 s'effondre si la bande vide ou le plancher de coût sont faux — avec exactement la même confiance qu'elle tient s'ils sont justes. Je reproduis le trou que le registre déclare lui-même : « **Zéro `A` sur tout le volet marché et tout le volet juridique** » (L.159).

**3. Le réseau est fermé pour moi aussi.** Je n'ai ouvert aucune source guadeloupéenne, aucune page de tarif, aucun texte de licence. Je **reproduis** le mur central du projet au lieu de le lever. Mes seuls `A·1` sont sur le dépôt : du code lu, des commandes lancées, des bases interrogées.

**4. Je suis le même modèle que le producteur.** Toute la chaîne — plan, registre, cinq critiques, celle-ci — est une seule famille d'inférences sur le même corpus. Une convergence entre nous n'est pas une confirmation ; c'est une corrélation.

**Ce qu'il faudrait pour une lecture réellement indépendante**, par ordre de rendement :
— **Le `DDCC` en session neuve** que le skill prescrit, sur le plan seul, **sans angle assigné** et sans ce fichier. C'est la seule lecture dont l'indépendance est entière, et sa condition de validité est que le producteur ne la déclenche pas. Rien dans ce que j'ai lu ne dit qu'elle a été faite.
— **Les deux demi-journées d'un humain avec un navigateur**, que le registre a déjà établies comme irremplaçables (L.171). Le plus rentable de ces gestes n'est pas technique : **ouvrir une page de tarif réelle et un texte de licence réel**, qui décideraient à eux seuls le §3 et le §5.
— **Un lecteur qui n'est pas Claude.** Un comptable local pour l'arithmétique du §3, un avocat guadeloupéen pour les sept lignes disciplinaires du plan. **Toute la doctrine juridique de ce projet remonte à un seul modèle lisant des documents qu'il ne peut plus réouvrir.** C'est le point de fragilité unique le plus grave de l'ensemble, plus grave qu'aucune contradiction que j'ai citée.
— Et une règle de procédure, gratuite : **interdire au producteur d'écrire l'angle du lecteur.** Donner le document, la consigne « casse-le », et rien d'autre. J'ai été trop bien guidé pour être un juge.

---

## 7 — Ma conclusion la plus coûteuse si elle est fausse, et son test à moins de cent euros

**La conclusion** : celle du §3 et du §5.2 — qu'il faut facturer **au-dessus de 200 €** ou ne rien faire, parce que la bande 30-200 € est vide pour toute prestation humaine et que le produit impose un geste humain. Elle commande mon critère d'abandon global entier.

**Si elle est fausse**, elle est la plus chère de tout ce fichier : elle tue un produit viable. Un abonnement à 50 € peut tenir si la relecture humaine n'est pas *par envoi* mais *par exception* — un rapport de veille qui ne contient aucune ligne générée (c'est déjà le cas : le rapport existant porte « **Aucune ligne de ce rapport n'est générée par un modèle de langage** ») n'a presque rien à relire. Dans ce cas la bande n'est pas vide pour *ce* produit, mon seuil de 11 clients à 150 € est deux à trois fois trop sévère, et je ferais abandonner à tort.

**Le test, et il tient sous cent euros.** Un seul protocole, qui mesure la seule chose que personne n'a jamais mesurée dans ce projet : **une carte débitée.**
1. Rendre le rapport réel : quatre semaines de BODACC + marchés publics filtrés Guadeloupe, une fois le réseau ouvert et les quatre licences lues. **0 €.**
2. Ouvrir deux liens de paiement sur un encaisseur sans abonnement, l'un à **50 €/mois**, l'autre à **150 €/mois**, pour **le même rapport, mot pour mot**. **0 € de frais fixes.**
3. Douze établissements, choisis dans les 760 de l'hébergement-restauration, **tirés au sort entre les deux prix** — six et six. Un appel, le rapport en pièce, le lien. Pas de question, pas de « seriez-vous prêt à ». **Un lien.**
4. **Frais de transaction si quelqu'un paie : environ 2 à 3 % de 50 à 150 €, soit moins de 30 € au total. Coût maximal du test : sous 50 €.**

**Lecture.** Zéro paiement sur douze aux deux prix → ma conclusion tient, et le critère d'abandon global s'applique tel qu'écrit. Au moins deux paiements à 50 € → **j'ai tort**, la bande n'est pas vide pour ce produit, mon seuil doit être recalculé à 32-53 clients et le projet a un prix. Des paiements à 150 € et aucun à 50 € → ma conclusion tient **et** le projet est meilleur que le plan ne le croit.
**Ce test remplace celui du plan en L.75** (« cinquante euros par mois pour recevoir ceci chaque lundi ? », cinq établissements, réponse verbale), qui mesure une politesse, teste un seul prix, et ce prix est celui que la preuve du plan interdit. Même coût, même durée, et il produit le **premier euro facturé** que le registre a désigné comme l'unique juge du désaccord (L.138).

---

## 8 — Ce que j'ai réellement écarté

Sans quota. Quatre choses, et je les nomme parce qu'elles auraient fait de bonnes attaques et qu'elles sont fausses.

**1. « Les chiffres que le plan donne sur son propre code sont gonflés. »** Écarté, `A·1`. J'ai cherché à casser 1 183, 215 et 21/21. Les trois se reproduisent exactement : 1 183 est la somme des lignes non vides des six fichiers de code, 215 celle de `publier.py`, et `python3 verifier.py --toutes` rend `PROUVEES 21/21 = 100.0 %`. **Sur lui-même, ce plan ne gonfle rien, et c'est à son honneur.** Tout mon §0 et mon §4.7 portent sur ce que ces chiffres mesurent, jamais sur leur exactitude.

**2. « Les propriétés de schéma annoncées en phase 3 et 4 sont du vent. »** Écarté, `A·1`. `schema.sql` porte bien quatre déclencheurs (L.63, 105, 192, 306), dont `assertion_relecture_nommee` et `publication_ia_relue` qui sont les « deux déclencheurs » de L.107. Et la date d'expérience est bien là, avec l'obligation de déclarer l'absence : `date_experience_origine TEXT NOT NULL CHECK (… IN ('champ_plateforme','declaratif_client','deduite','absente_a_la_source'))`, précédée du commentaire « CONTRAINTE JURIDIQUE IRRÉVERSIBLE ». Le plan dit vrai en L.133.

**3. « Le verdict de licence sur l'orchestrateur copyleft réseau (L.103) est juridiquement faux. »** Écarté comme attaque, **conservé comme trou**. Je ne peux pas ouvrir le texte de la licence, et opiner de mémoire sur une clause de copyleft réseau serait du `D` — ce que je reproche au plan. Je laisse la ligne au compte du plan et je signale que c'est **la décision la plus structurante qu'aucun lecteur n'a vérifiée sur source** : elle fait passer le périmètre de trente plateformes à trois.

**4. « La phase 2, le blog, est une promesse sans substance. »** Écarté. La table `article` existe en base, et un rendu de table est trivial. Le plan a raison de dire « l'organe existe ». Mon seul reproche sur la phase 2 est qu'elle n'a **ni date, ni couple, ni livrable**, et il est déjà au §4.2.

---

## 9 — Les cinq colonnes

Les prix sont `D` — aucune page de tarif atteignable depuis cet environnement. **Interdits de décision**, conformément au barème.

| MCP à installer | Logiciels manquants | Outils déjà disponibles | IA qui font ce travail, et à quel prix (`D`) | Futurs à 12 mois ⏳ |
|---|---|---|---|---|
| Un MCP **navigateur sortant** sur liste blanche (BODACC, data.economie, Météo-France, préfecture, Légifrance, pages de tarif). C'est le préalable de tout : §4.6, §4.7 et §5 sont tous bloqués dessus | **Rien à écrire pour la phase 1.** Ce qui manque est une **garde** de 3 lignes dans `cmd_collecte` : `AND licence_lue_le IS NOT NULL`, pour que L.68 devienne vraie | `socle.py`, `publier.py`, `verifier.py`, `schema.sql`, `sources.json` — **1 183 lignes, 21/21 rejouables, `A·1` vérifié par moi** | **Quatre produits de 0 à 39 $/mois couvrent déjà le besoin** — `B·2`, registre L.39, seul chiffre de ce tableau qui ne soit pas `D` | ⏳ **Le délai d'approbation des plateformes** : inconnu, et il fixe seul la date de la phase 3. Rien ne commence avant le dépôt |
| Un MCP **encaissement** (lien de paiement, sans abonnement) : sans lui le test du §7 n'existe pas, et le projet ne saura jamais ce qu'un client paie | Un **étalon de 30-50 pages guadeloupéennes annotées** — sans quoi le seuil n°2 du plan est inexécutable (§2). Le plan le refuse ; il faut alors retirer le seuil, ou l'écrire | Les deux briques à `un` et `zéro` mainteneur, à verser au dépôt — demi-journée, registre L.108 | Veille open-data générique : outils en libre-service, **bande 30-200 € vide pour toute prestation humaine** — `B·2`, registre L.80 | ⏳ **Le pont translingue créole** (plan L.70). Aucune date, aucun couple, et le registre a établi en `A·1` qu'il ne distingue de rien |
| Un MCP **calendrier**, et ce n'est pas une facilité : le plan contient **zéro date** (§1). Toute date écrite ailleurs que dans un calendrier opposable se décale | Un **prix arrêté**. C'est le manque le plus grave du plan : sans prix, ni le seuil n°1, ni mon critère global, ni la rentabilité ne se calculent (§4.5) | Les deux compétences `conduite-par-vagues` et `registre-de-demarche` — **mais à `B·3` par la doctrine du projet, jamais éprouvées** (registre L.197) | Rédaction d'avis / réponses automatisées : **fonction phare de trois concurrents, et interdite pour nous sur le segment avocat** — `B·2`, plan L.139 | ⏳ **L'avis déontologique de 2012 sur les liens vers les réseaux sociaux** : probablement dépassé, **toujours republié en 2026, donc opposable par un bâtonnier** — `B·3`, registre L.94 |
| Aucun MCP pour le volet avis **avant** le test Google à 0 €. Installer un connecteur avant de savoir si le point d'accès existe, c'est dépenser sur un `C·3` | Un **juge extérieur** : le `DDCC` en session neuve, et un lecteur humain non-Claude sur les sept lignes disciplinaires (§6) | Le bouchon de plateformes, 17 lignes — **utile pour le banc, et il ne prouve rien sur le monde** (§0) | Conformité certifiée par un organisme de normalisation, **déjà vendue par un éditeur, avec captation de la date d'expérience** — `B·2`, registre L.56 | ⏳ **Les 25 % restant à construire, 24 à 41 jours** (`A·2`, registre L.105) — mais l'unité juste est une date, pas un jour (§4.3) |

---

## Verdict

**Exécutable** : la semaine 0 pour ses deux gestes gratuits et décisifs (test Google, question au bâtonnier) — les deux meilleures lignes du document ; et la phase 1, **à condition** d'ajouter ce que le plan a oublié : lire les quatre licences, poser la garde dans `cmd_collecte`, et capter une première page guadeloupéenne réelle.

**Tunnel** : tout le reste. Les phases 2, 3 et 4 n'ont **aucune date**, le document n'en contient aucune ; la règle d'arrêt du mandat énonce « une date, pas une condition » et laisse le champ vide ; la seule « porte de sortie » nommée ouvre sur une plateforme dont le plan a prouvé qu'elle n'existe pas ; les cinq seuils d'abandon ne portent pas un seul couple et aucun ne peut se déclencher en l'état ; aucun critère n'arrête **le projet** ; et le principe qui commande toute la forme du plan est mesuré sur un bouchon de dix-sept lignes que le projet a écrit lui-même.

**Ce n'est pas un plan malhonnête — son code est honnête et ses chiffres se reproduisent. C'est un plan qui a confondu l'inventaire de ses preuves avec un calendrier.** Six dates et un prix le rendraient exécutable en entier. Il n'en a aucun.
