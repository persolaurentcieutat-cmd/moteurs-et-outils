# Relance — quatre trous comblés, et verdict révisé

**Suite de** `critiques/02-marche.md`, qui n'est pas modifié.
**Date de recherche** : 2 octobre 2026. Toutes les URL de ce document ont été consultées ce jour.
**Ce que la relance change** : mon verdict d'insolvabilité était conditionné à une cible de 800 établissements. **Il était faux à ce titre.** Le marché adressable est dix-huit fois plus grand et il est solvable. Ce qui ne tient pas, c'est la différenciation, pas la taille. Révision en § 6.

---

## 0. Mes lignes en cran D — déclarées avant le contenu

| # | Ligne en cran D | Pourquoi |
|---|---|---|
| D10 | **Le guichet de ReviewPro, TrustYou, Revinate et Qualitelis pour accéder aux avis** | Aucun des quatre ne le déclare. J'établis le mécanisme **côté plateforme** (Booking) sur source primaire, pas côté éditeur. Lequel des quatre est effectivement partenaire connectivité Booking : **inconnu** |
| D11 | **La présence réelle des quatre aux Antilles** | Je n'ai qu'un faisceau négatif : la répartition par pays des hôtels clients de ReviewPro ne mentionne aucun territoire caribéen. Absence de mention n'est pas absence d'activité |
| D12 | **Le temps réel passé par un prestataire pour produire la prestation à 80 €/mois** | Personne ne le publie. Je refuse d'inventer une durée. Je renverse donc le calcul : je dis ce que 80 € **achètent** à un taux sourcé, ce qui ne demande aucune durée inventée (§ 5) |
| D13 | **Le nombre d'avis mensuels reçus par un établissement guadeloupéen** | Non trouvé. C'est le facteur qui détermine la charge de « réponse à tous les avis ». Sans lui, le coût de revient a une inconnue qui ne se lève que par mesure |
| D14 | **Le coût employeur chargé d'une heure au SMIC en Guadeloupe** | J'ai le SMIC brut sur source primaire URSSAF. Je n'ai pas le taux de charges patronales après réduction générale dégressive. J'utilise donc le **brut comme plancher** et je le dis à chaque fois |
| D15 | **Le périmètre exact de la nomenclature U2P « alimentation » / « fabrication et services »** | Je ne sais pas si « alimentation » inclut la restauration. **Je n'additionne donc jamais les chiffres U2P aux chiffres INSEE**, et je garde les deux sources côte à côte sans les mélanger |
| D16 | **La ventilation des 14 582 établissements employeurs par secteur A17 ou A38** | Les fichiers INSEE Flores existent mais sont des .xlsx de 4 à 40 Mo non ouverts. Ma segmentation du § 4 utilise donc deux bases de champs différents, ce qui est signalé ligne par ligne |
| D17 | **Le fait que les campings et autres hébergements collectifs soient à zéro en Guadeloupe** | L'INSEE affiche « Ensemble 0 » au 1/1/2023. C'est probablement un effet de secret statistique ou de champ d'enquête, pas une réalité. Je le reporte en le marquant douteux |
| D3 (maintenue) | **Meta** | Toujours aucune source primaire. `facebook.com` inatteignable |

**Hôtes bloqués par le proxy de sortie de cet environnement**, constatés par échec direct : `www.insee.fr`, `support.google.com`, `developers.google.com`. Les trois ont été atteints par un récupérateur tiers, ce qui veut dire que **je n'ai pas vu les pages rendues** — j'ai vu le texte extrait. C'est une faiblesse de preuve que je ne peux pas lever d'ici, et je la signale sur chaque ligne concernée.

---

## 1. Trou n°1 — Les quatre acteurs du guichet 1 hôtelier

### 1.1 Le mécanisme, établi côté plateforme et non côté éditeur

Les quatre éditeurs ne déclarent pas leur voie d'accès. Mais **Booking.com documente la sienne**, et c'est la porte par laquelle il faut passer. C'est une meilleure preuve que n'importe quelle page marketing d'éditeur.

**Guest Review API de Booking.com** — `developers.booking.com/connectivity/docs/review-api`, page datée « Last updated 1 month ago » (donc ~septembre 2026), cran **B** :

> « Use the Review API to retrieve a property's reviews, render them in your interface, and let the property reply. »

> « **For internal use only** — Guest reviews retrieved by this API **may not be used on your public page**. The API is for internal use by properties. »

> « Your machine account should have the permission to access review-api. »

Donc : l'API existe, elle permet de lire les avis **et d'y répondre**, et son usage est contractuellement restreint à l'usage interne de l'établissement. Un produit qui republierait ces avis sur sa propre vitrine serait en infraction.

**Qui peut obtenir ce compte machine** — `connect.booking.com`, cran **B** :

> « **In an effort to ensure our teams are able to provide the strong partnership experience, we are pausing integrations with new connectivity providers until further notice.** »

> « I own a property listed on Booking.com. Can I use the Connectivity APIs? **We don't accept direct connections from individual properties right now**, but you can connect via a channel manager. »

Et les conditions d'admission au programme, telles que listées sur la page des exigences partenaires : conformité PCI et PII, logiciel hébergé en nuage ou sur serveur central, **gestion des prix et des disponibilités**, **gestion des réservations**, mise à jour temps réel des tarifs et disponibilités, confirmation instantanée des réservations, gestion du contenu de l'établissement.

**Trois conclusions, et elles sont dures.**

1. **Le guichet 1 de Booking est fermé.** Pas « coûteux », pas « à réexaminer à trois ans » : **fermé aux nouveaux entrants, par la décision écrite de Booking**, sans date de réouverture annoncée.
2. **Même s'il était ouvert, le projet ne remplirait pas les conditions.** Pour obtenir l'API avis, il faut supporter la gestion des tarifs, des disponibilités, des réservations et des confirmations instantanées — c'est-à-dire **être un channel manager**. Un outil d'avis pur ne qualifie pas. Le guichet 1 n'est pas une porte chère : c'est une porte réservée à un autre métier.
3. **Le document avait raison sur ce point, et pour une raison plus forte que celle qu'il donne.** La section 2.2 classe le guichet 1 « Hors de portée au départ. À réexaminer à trois ans », avec « contrat, certification, volume minimum ⏳ ». La réalité est pire et plus simple : il est fermé, et conditionné à l'exercice d'un métier différent. **Je corrige donc ma première critique** : là où je reprochais au document de surestimer le coût du guichet 1, c'était vrai pour Google et **faux pour Booking**.

### 1.2 Les quatre acteurs, un par un

| Acteur | Ce qu'il fait | Prix affiché par l'éditeur | Guichet | Antilles | Cran |
|---|---|---|---|---|---|
| **Shiji ReviewPro Reputation** | Centralisation d'avis multi-plateformes, « Global Review Index », analyse sémantique, benchmark concurrentiel, enquêtes. Expose sa propre API sortante, dont un point d'accès « Published Reviews Export » | **Non publié** — « Request a Demo / Price quote » | **Inconnu.** Son réseau développeur revendique « the highest quality and largest quantity of online guest-written review data available worldwide » sans jamais nommer sa voie d'accès. Booking figure parmi ses sources | **Aucune mention caribéenne** dans la répartition par pays de ses 112 hôtels clients référencés : Espagne 16, Émirats 15, Royaume-Uni 12, États-Unis 11, Brésil 10, **France 1**, zéro Antilles | **B** pour l'offre (`developer.reviewpro.com`), **B** pour la répartition clients (`hoteltechreport.com/marketing/reputation-management/reviewpro`, source tierce vérifiée hôteliers), **D10/D11** pour le guichet et les Antilles |
| **TrustYou CXP** | **Lite** : boîte de réception centralisée de tous les avis, IA de sentiment, benchmark concurrentiel, tableau de bord, rapports. **Essential** : rapports programmés, module d'enquête, widgets, multilingue. **Professional** : enquêtes illimitées + **« Response AI for automated, AI-generated review responses (UNLIMITED) »** | **Lite 75 € / établissement / mois**, **Essential 130 €**, **Professional 180 €**, facturés à l'année | **Inconnu** | Non mentionnées | **B** pour les prix et le périmètre (`trustyou.com/pricing/cxp/`), **D10** pour le guichet |
| **Revinate Reputation** | Tableau de bord, gestion des avis, **réponse directe à l'avis**, assistant de réponse, rapport de réponse, benchmark concurrentiel, comptes sociaux liés, alertes | **125 $ / établissement / mois** (clients récurrents), **200 $** (nouveaux). Options : avis pour points de vente 50 $/mois, concurrents supplémentaires 75 $/mois, API Porter 185 $/mois | **Inconnu** | Non mentionnées — siège unique affiché à Bend, Oregon | **B** pour les prix (`revinate.com/plans-guest-feedback/`), **D10** pour le guichet |
| **Qualitelis (groupe Septeo)** | Enquêtes et parcours client connectés au logiciel métier, centralisation multi-plateformes, **réponses assistées par IA**, analyse sémantique, diffusion. Revendique **7 000 établissements**. Cible déclarée : hôtellerie, résidences de tourisme, camping, restauration, immobilier. **Hébergement souverain en France, RGPD et CNIL natifs, pas de transfert hors UE, SLA 99,9 %** | **Non publié** | **Inconnu** | Non mentionnées. Présence déclarée : France, Belgique, Suisse, Espagne, Canada | **B** pour l'offre (`qualitelis.septeo.com`), **D10/D11** |

### 1.3 Ce que ce trou, comblé, fait au projet — dans les deux sens

**Contre le projet.** **TrustYou vend à 75 € par établissement et par mois** une boîte de réception centralisée de tous les avis, une IA de sentiment et un benchmark concurrentiel. C'est **sous le plafond local de 80 €**. Et à 180 €, il vend la **rédaction automatique illimitée des réponses aux avis**, c'est-à-dire exactement l'organe « Avis » que le projet veut construire. Revinate vend la réponse directe à l'avis à 125 $. Qualitelis est français, souverain, RGPD natif, et sert 7 000 établissements — ce qui vide l'exigence 6 du document de tout pouvoir discriminant, cette fois sur le segment hôtelier lui-même. **Trois des quatre vendent déjà l'organe « Avis » du projet, et l'un d'eux sous le plafond de prix local.**

**Pour le projet, et je dois l'écrire.** Ces quatre acteurs **ne sont pas en Guadeloupe** et ne servent pas la taille d'établissement guadeloupéenne. La répartition par taille des hôtels clients de ReviewPro est sans ambiguïté : **4 petits (10-49 chambres), 21 moyens (50-99), 79 grands (100-499), 19 très grands (500+)**. Leur marché est le grand hôtel de chaîne — Peninsula, IHG, Langham sont cités. Or le parc guadeloupéen, sur source INSEE primaire (`insee.fr/fr/statistiques/7653165?geo=DEP-971`, tableau TOU T1 au 1/1/2023, cran **B**) :

| Catégorie | Hôtels | Chambres |
|---|---|---|
| **Ensemble** | **55** | **3 252** |
| 5 étoiles | 1 | 52 |
| 4 étoiles | 11 | 943 |
| 3 étoiles | 14 | 1 327 |
| 2 étoiles | 5 | 147 |
| 1 étoile | 0 | 0 |
| **Non classé** | **24** | **783** |

Taille moyenne : **59 chambres**. Et **24 des 55 hôtels ne sont pas classés**, pour 783 chambres, soit une moyenne de 33 chambres — la tranche où ReviewPro ne compte que quatre clients dans le monde entier.

**Donc l'intuition du document est juste sur ce segment précis, et seulement là** : les détenteurs du guichet 1 ne descendent pas à l'échelle de l'hôtel guadeloupéen non classé de 33 chambres. Mais ce segment compte **24 à 55 établissements**. Ce n'est pas un marché, c'est une liste de clients. On ne finance pas la reconstruction de sept organes avec vingt-quatre hôtels non classés.

*(Note : le même tableau INSEE affiche « Ensemble 0 » pour les campings et pour les autres hébergements collectifs au 1/1/2023. Je reporte le chiffre en le marquant douteux — D17 — car il est invraisemblable et sent le secret statistique ou un champ d'enquête restreint.)*

---

## 2. Trou n°3 — Le point Google, confirmé sur source primaire Google, et aggravé

C'était mon affirmation la plus destructrice. Elle est confirmée, et sur **deux hôtes Google indépendants**, dont l'un est le contrat d'API lui-même. Les deux hôtes sont bloqués en accès direct par le proxy (`support.google.com` et `developers.google.com`, `EGRESS_BLOCKED` constaté) et ont été atteints par un récupérateur tiers : c'est la limite de preuve, je la nomme.

### 2.1 Première source — l'aide Google, côté interface

`support.google.com/business/answer/3403100?hl=fr`, page sans date de publication affichée, consultée le 2 octobre 2026, cran **B** :

> « Si vous êtes propriétaire d'une fiche d'établissement, vous pouvez **inviter des utilisateurs** à en devenir propriétaire ou administrateur. Ils pourront vous aider à gérer les opérations quotidiennes (modifier les informations, **répondre aux avis** et **gérer les posts**, par exemple). »

> « Remarque : Chaque utilisateur doit disposer de son propre compte Google pour accéder aux fiches d'établissement et les gérer **sans avoir besoin de votre mot de passe**. »

> « 3. En haut à gauche, sélectionnez **Ajouter**. 4. **Saisissez une adresse e-mail.** 5. Sous "Accès", sélectionnez **Propriétaire** ou **Administrateur**. 6. Sélectionnez **Inviter**. »

> « Les utilisateurs invités peuvent accepter l'invitation et devenir utilisateurs **immédiatement**. »

Droits de l'administrateur, extraits du tableau de la même page : « **Répondre aux avis** », « **Créer, gérer et publier des posts** », « Modifier les principales informations sur l'établissement, comme les horaires d'ouverture et l'adresse », « Ajouter, supprimer et modifier des photos de couverture et des photos supplémentaires », « Télécharger les statistiques », « Répondre aux questions/réponses ».

### 2.2 Seconde source — la référence d'API, côté machine

`developers.google.com/my-business/reference/accountmanagement/rest/v1/accounts.admins/create` et `.../accounts.admins`, consultées le 2 octobre 2026, cran **B** :

> « **Invites the specified user to become an administrator for the specified account.** The invitee must accept the invitation in order to be granted access to the account. »

> `POST https://mybusinessaccountmanagement.googleapis.com/v1/{parent=accounts/*}/admins`

Champ `admin` de la ressource Admin :

> « Optional. The name of the admin. **When making the initial invitation, this is the invitee's email address.** »

Énumération `AdminRole` : `PRIMARY_OWNER`, `OWNER`, `MANAGER`, `SITE_MANAGER`. Champ `pendingInvitation` : booléen. Portée OAuth requise : `https://www.googleapis.com/auth/business.manage`.

### 2.3 Ce que la seconde source ajoute, et c'est pire pour le document

La page d'aide montrait qu'un humain peut inviter un administrateur à distance. **La référence d'API montre que la machine peut le faire.** `accounts.admins.create` prend une adresse e-mail et un rôle, et pose une invitation en attente. Un concurrent mondial peut donc **automatiser l'ouverture du guichet 2, en série, par programme**, pour des milliers de comptes, sans jamais rencontrer personne, sans détenir un mot de passe, sans quitter son bureau.

**Conséquences, toutes confirmées :**

1. « Aucun concurrent mondial ne peut l'ouvrir » (section 2.7) est **faux**, deux fois documenté, dont une fois sous forme d'appel d'API programmable.
2. « Demander un mandat créerait une friction qui les tuerait » (section 2.7) est **faux** : la friction est un e-mail et un clic, et elle est scriptable.
3. L'organe « Garde des accès confiés » (section 6), présenté comme « la condition du guichet 2, donc de tout le produit », avec « chiffrement, révocation, journalisation, cloisonnement par client » au niveau d'un établissement bancaire, **répond à un problème que le mécanisme ne pose pas**. Google ne transmet aucun identifiant : il accorde un rôle, révocable par le client depuis sa propre interface (« Supprimer un propriétaire ou un administrateur », même page). Ce qu'il faut garder, c'est un jeton OAuth de portée `business.manage` — une table chiffrée avec rotation, pas un coffre-fort. **L'organe tombe, et avec lui des semaines de construction.**

Ce que cela ne dit **pas**, et que je ne dirai pas : rien de tout cela ne vaut pour Meta, TripAdvisor, Booking ou Airbnb. Pour Booking, le § 1.1 montre que c'est l'inverse — guichet fermé. **Le guichet 2 est ouvert à distance sur Google ; sur les autres plateformes, je l'ignore.**

---

## 3. Trou n°4 — Le coût de revient de la prestation à 80 €/mois

C'est, comme le dit la relance, la question qui décide. Je la traite sans inventer une seule durée.

### 3.1 La prestation à produire

`mangoweb.digital/google-my-business`, prestataire à Saint-Claude, Guadeloupe, cran **B** : **80 €/mois** pour « 8 posts mensuels, Réponse à tous les avis, Photos mensuelles, Mise à jour horaires, Statistiques mensuelles », après **200 €** d'installation.

### 3.2 Les taux horaires, sur source primaire

| Taux | Montant | Source | Cran |
|---|---|---|---|
| **SMIC horaire brut**, applicable « en métropole, **Guadeloupe**, Guyane, Martinique, à La Réunion… » à compter du 1er juin 2026 | **12,31 €/h** brut (1 867,02 € mensuel pour 35 h) | URSSAF, mis à jour le 27 mai 2026, visant l'**arrêté du 22 mai 2026** relatif au relèvement du salaire minimum de croissance — `urssaf.fr/accueil/actualites/augmentation-smic.html` | **B** |
| Tarif jour moyen d'un **community manager freelance expérimenté** | **405 €/jour** | Malt, baromètre des tarifs 2026, « sur la base des Community managers expérimentés actifs les 3 derniers mois » — `malt.fr/t/barometre-tarifs/communication/community-manager` | **B** |
| Tarif jour moyen, **0 à 2 ans d'expérience** | **256 €/jour** | idem | **B** |
| Coût employeur chargé d'une heure au SMIC | **non sourcé** | — | **D14** |

### 3.3 Le calcul, renversé pour ne rien inventer

Je ne sais pas combien d'heures prend la prestation (D12). Mais je sais exactement **ce que 80 € achètent**. Sur une journée de 7 heures :

| Main-d'œuvre | Taux horaire déduit | **Ce que 80 € achètent** |
|---|---|---|
| Community manager expérimenté (Malt, 405 €/j) | 57,86 €/h | **1 h 23 min** |
| Community manager débutant (Malt, 256 €/j) | 36,57 €/h | **2 h 11 min** |
| Salarié au SMIC **brut**, charges patronales non comptées (plancher absolu) | 12,31 €/h | **6 h 30 min** |

Et la décomposition par livrable, sans supposer aucune durée : si les 8 posts consommaient **tout** le budget et que la réponse aux avis, les photos, les horaires et le rapport étaient gratuits, chaque post disposerait de **10 €**, soit **10 minutes** au taux expérimenté, **16 minutes** au taux débutant.

### 3.4 La réponse à la question

**La prestation à 80 €/mois ne peut pas être produite à la main à un taux professionnel.** Au tarif de marché d'un community manager, 80 € achètent moins d'une heure et demie — et il faut y faire tenir huit publications rédigées et illustrées, la réponse à tous les avis, des photos, la mise à jour des horaires et un rapport mensuel. Ce n'est pas tenable.

Trois explications seulement, et elles s'additionnent plus qu'elles ne s'excluent :

1. **Le prestataire se paie bien en dessous du tarif de marché.** Un auto-entrepreneur solo qui facture 80 € pour cinq ou six heures travaille à l'équivalent du SMIC brut. C'est le scénario le plus probable pour un opérateur d'une personne à Saint-Claude.
2. **Il automatise déjà.** Les outils existent à 0 à 39 $ : Metricool gratuit, Buffer à 5 $ le canal, Localo à 39 $ avec posts auto-générés et réponse aux avis en un clic, Digitaleo avec crédits IA à 0,02 €, TrustYou Professional avec réponses IA illimitées. **Un prestataire rationnel à 80 € utilise déjà l'un d'eux.**
3. **C'est un produit d'appel.** 80 €/mois attaché à 200 € d'installation, pour amener un site, un logo, du Google Ads — ce que vendent toutes les agences locales recensées.

**Donc : oui, il y a une marge à capter, et elle est grosse.** L'écart entre 80 € de prix de vente et 1 h 23 de main-d'œuvre achetable est précisément la valeur de l'automatisation. C'est la bonne nouvelle pour le projet, et elle était absente de mon premier retour.

**Mais la marge est déjà captée.** Elle l'est par Localo à 39 $, par Metricool à 0 €, par Buffer à 5 $, par Digitaleo et par TrustYou. Le projet n'arriverait pas pour capter une marge laissée ouverte : il arriverait **troisième ou quatrième sur une marge déjà arbitrée**, avec un prix de vente plafonné par un plancher gratuit. L'écart 80 € – 39 $ est ce qui reste à se partager, et il ne finance pas sept organes.

**Ce que je ne peux pas calculer** : la charge réelle de « réponse à tous les avis » dépend du nombre d'avis mensuels, que je n'ai pas trouvé (D13). Si un restaurant guadeloupéen reçoit cinq avis par mois, la prestation tient en deux heures ; s'il en reçoit quarante, elle est intenable à 80 € même au SMIC. **Ce seul chiffre manquant déplace la conclusion**, et il se mesure.

---

## 4. Trou n°2 — Le marché adressable, par segment

Ma cible de 800 établissements était le **cœur touristique professionnel**, pas le marché. La relance a raison. Voici la segmentation, avec les champs et les dates qui ne se mélangent pas.

### 4.1 Les deux dénominateurs, qui ne s'additionnent pas

| Base | Chiffre | Champ exact | Source | Cran |
|---|---|---|---|---|
| **Établissements économiquement actifs 2021** | **33 477** | Activités marchandes non agricoles, sections B à S hors O | INSEE SIDE, `insee.fr/fr/statistiques/7658710?geo=REG-01`, tableau DEN T5 | **B** |
| **Établissements employeurs fin 2024** | **14 582** | Employeurs durant l'année et actifs la dernière semaine de décembre, hors défense et particuliers employeurs | INSEE Flores, `insee.fr/fr/statistiques/2012766` | **B** |
| Entreprises de proximité | **~33 000** | Artisanales, commerciales et libérales au 31/12/2020 | U2P / ISM d'après INSEE | **B**, périmètre non superposable (D15) |

L'écart de ~19 000 entre les deux premiers est la masse des établissements **sans salarié**. C'est elle qui décide de la solvabilité.

### 4.2 La ventilation sectorielle — INSEE SIDE 2021, 33 477 établissements actifs

| Secteur (nomenclature A10) | Établissements | Part | Les avis publics décident-ils du chiffre d'affaires ? |
|---|---|---|---|
| Commerce, transports, **hébergement, restauration** | **9 335** | 27,9 % | **Oui pour l'hébergement-restauration ; partiellement pour le commerce** |
| Activités spécialisées, scientifiques, techniques, services administratifs et de soutien | 7 499 | 22,4 % | Peu — vente interentreprises |
| Administration publique, enseignement, **santé humaine**, action sociale | 4 919 | 14,7 % | **Oui pour la santé libérale** |
| Construction | 3 554 | 10,6 % | Partiellement — devis et bouche-à-oreille |
| Industrie manufacturière, extractives et autres | 2 653 | 7,9 % | Peu |
| Autres activités de services (coiffure, soins, réparation…) | 2 003 | 6,0 % | **Oui** |
| Activités immobilières | 1 855 | 5,5 % | **Oui** |
| Activités financières et d'assurance | 948 | 2,8 % | Partiellement |
| Information et communication | 711 | 2,1 % | Peu |

Source : INSEE SIDE, DEN T5, géographie au 01/01/2024. Cran **B** pour les chiffres ; la colonne de droite est **mon jugement**, pas une donnée.

**Je ne peux pas croiser cette ventilation avec les 14 582 employeurs** : la ventilation sectorielle de Flores à 17 ou 38 postes est dans des .xlsx non ouverts (D16). C'est la mesure manquante la moins chère à obtenir : les fichiers sont gratuits.

### 4.3 Les quatre segments, chiffrés

**Segment A — Tourisme et hospitalité.** Les six exigences du document s'y appliquent toutes.
- Hôtels : **55**, 3 252 chambres, dont **24 non classés** (INSEE au 1/1/2023, **B**).
- Branche HCR, établissements employeurs : **507** (AKTO, monographie HCR 2024, données ACOSS 2022, projection Kyu Lab, **B**), dont **88 % à 1-9 salariés** et 11 % à 10-49.
- Périmètre plus large hébergement + restauration rapide + restauration collective, établissements employeurs : **760** (AKTO, monographie H&R 2023, données 2019, **B**).
- Non-salariés de la branche : **970** (AKTO 2024) ou **1 550** (AKTO 2023) selon le périmètre.
- Meublés de tourisme : « plus de **10 000** » (presse 2023, **C**, aucun comptage officiel).
→ **Cible professionnelle : 507 à 760 établissements employeurs.** Les deux chiffres sont des périmètres et des dates différents, je ne tranche pas entre eux. Plus un gisement de plus de 10 000 loueurs non chiffré et de solvabilité inconnue.

**Segment B — Commerce de détail et services de proximité à clientèle locale.** Les avis Google comptent, la saisonnalité touristique beaucoup moins, le multilingue pas du tout.
- Dans les 9 335 du commerce-transport-hébergement-restauration, une fois l'hospitalité retirée : de l'ordre de **8 500 à 8 800 établissements actifs**, dont une part majoritaire sans salarié. Plus 2 003 « autres activités de services ».
→ **Cible : plusieurs milliers d'établissements actifs, dont le sous-ensemble employeur est inconnu (D16).**

**Segment C — Professions libérales, santé, droit.** C'est le segment que le document ignore entièrement, et c'est peut-être le meilleur.
- Entreprises de professions libérales : **6 530**, pour 7 270 salariés (U2P/ISM d'après INSEE au 31/12/2020, **B**). **97 %** de leurs apprentis sont formés à un niveau d'études supérieures, indice d'un segment à pouvoir d'achat élevé.
- Secteur « administration publique, enseignement, santé humaine, action sociale » : 4 919 établissements actifs (INSEE 2021, **B**) — périmètre plus large, non superposable.
- Confirmation de marché : lagencedigitale déclare la **santé (médecins, dentistes, kinésithérapeutes, pharmacies, centres médicaux, cliniques)** et le **droit (avocats, notaires)** comme ses deux premiers secteurs d'intervention, depuis 2007 (`lagencedigitale.com`, **B**).
→ **Cible : ~6 500 entreprises libérales.** Un dentiste vit de ses avis Google. Il n'a ni saison cyclonique, ni croisiéristes hispanophones, ni créole dans ses avis, ni haute saison de carême.

**Segment D — Artisanat et construction.**
- Construction : 3 554 établissements actifs (INSEE 2021, **B**) ; 2 600 entreprises de proximité du bâtiment (U2P 2020, **B**, périmètre différent).
- Alimentation : 11 940 entreprises de proximité (U2P 2020, **B**, périmètre incertain, D15).
- Fabrication et services : 12 530 (U2P 2020, **B**).
→ **Cible : plusieurs milliers.** Avis moins décisifs, prix plafond probablement encore plus bas.

### 4.4 Le marché adressable, en trois chiffres

| Définition | Chiffre | Au plafond de 80 €/mois, ceiling théorique annuel |
|---|---|---|
| **Toute entreprise ayant une fiche Google** | **~33 000** établissements actifs | ~31,7 M€ |
| **Marché adressable solvable** — établissements employeurs, qui ont une trésorerie mensuelle | **14 582** | **~14,0 M€** |
| **Marché auquel les six exigences guadeloupéennes s'appliquent** | **507 à 760** | **0,49 à 0,73 M€** |

Les plafonds théoriques sont **mon arithmétique** (effectif × 80 € × 12), pas des prévisions : ils supposent 100 % de pénétration, ce qui n'arrive jamais. Ils servent à une seule chose, et elle est décisive : **montrer le rapport d'échelle de 19 à 1 entre le marché adressable solvable et le marché que la section 3 décrit.**

### 4.5 Le constat qui tue la section 3, par un autre chemin que le premier

Les six exigences guadeloupéennes — fuseau, langues, saisons, sources locales, tissu économique, droit — ne s'appliquent **qu'au segment A**, soit **3,5 à 5,2 % du marché adressable solvable** (507 à 760 sur 14 582). Sur les 95 % restants — le dentiste, l'avocat, le garagiste, le coiffeur, le maçon — il n'y a ni saison cyclonique à gérer, ni croisiériste hispanophone, ni carnaval dans le calendrier éditorial.

Donc : **soit** le projet vise le segment A, et ses six exigences ont un sens mais son marché fait 500 à 800 clients ; **soit** il vise le marché adressable réel de 14 582 établissements, et alors ses six exigences ne lui donnent **aucun avantage sur 95 % de sa cible**. Dans les deux cas, la phrase « Aucun acteur mondial ne construit à cette échelle de marché, et aucun ne peut ouvrir le guichet 2. C'est ce qui rend la position tenable » ne décrit pas le marché réel.

---

## 5. Les deux questions corrigées de la relance

### 5.1 Quelle hypothèse de mon retour, si elle est fausse, coûte le plus cher — et comment la tester pour moins de cent euros

**L'hypothèse la plus coûteuse est le plafond de prix de 80 €/mois.** Tout mon verdict en dépend : le coût de revient du § 3, le plafond de recettes du § 4.4, la conclusion que la marge est déjà arbitrée, et l'arbitrage entre vendre aux établissements ou aux agences. Et elle repose sur **une seule liste de prix publique, d'un seul opérateur solo**. Les indices contraires existent : So-Community annonce « dès 490 €/mois », et des sources de comparaison évoquent 300 à 800 €/mois pour la gestion d'une présence locale. Si le plafond réel est 250 à 400 €/mois, le marché adressable solvable passe de 14 à 45-70 M€ théoriques, la marge à capter devient confortable, et **la conclusion s'inverse**.

**Le test, pour 80 €, soit sous les cent euros** : **acheter un mois de la prestation MangoWeb à 80 €**, pour la fiche Google du projet lui-même. Un achat réel, sans tromperie, chez un fournisseur qui publie son prix. Ce que cela mesure, en une seule dépense :

1. **Le plafond** — confirmé ou démenti par le devis réel et par ce qui est négocié.
2. **Le coût de revient** — en observant les délais de livraison des 8 posts, leur degré de personnalisation, et si les réponses aux avis sont manifestement générées. On voit tout de suite si l'opérateur automatise déjà, et avec quoi.
3. **L'étalon de qualité** — c'est le **jeu d'épreuve guadeloupéen réel** que la section 5 du document réclame comme première tâche de V0, et il arrive tout fait, produit par un concurrent, sur un établissement réel.
4. **Le guichet** — en observant ce qu'il demande pour accéder à la fiche : une invitation administrateur, ou un mot de passe. Si c'est une invitation, le § 2 est confirmé par l'usage.

C'est le seul achat à moins de cent euros qui produise simultanément un **A-usage** et un **A-mesure**, et il comble quatre de mes trous d'un coup. **Deuxième test, gratuit** : ouvrir les fichiers INSEE Flores à 17 et 38 secteurs (`insee.fr/fr/statistiques/8266010`) et filtrer sur le département 971, ce qui lève D16 et donne la ventilation employeur par secteur en une heure.

### 5.2 Ce que j'ai réellement écarté ce tour-ci, et pourquoi

Pas de quota. Voici ce qui a été écarté, et rien de plus.

1. **Les API et conditions d'accès de TripAdvisor, Airbnb, Abritel, Expedia et Yelp.** Écartées parce que Booking suffisait à établir le fait décisif — qu'un guichet 1 majeur est fermé aux nouveaux entrants et réservé aux channel managers. Ajouter cinq plateformes aurait allongé le retour sans changer la conclusion. **Mais c'est un choix contestable** : pour un meublé de tourisme guadeloupéen, Airbnb et Abritel comptent plus que Booking, et je ne sais rien de leurs guichets.
2. **Le coût employeur chargé d'une heure de travail en Guadeloupe.** Écarté faute de source primaire URSSAF sur la réduction générale dégressive. J'ai préféré utiliser le SMIC brut comme plancher explicite plutôt que de recopier un coefficient de charges non vérifié. **L'effet sur ma conclusion est nul** : le calcul du § 3.3 est encore plus défavorable à la production manuelle si l'on charge le salaire.
3. **Rien d'autre.** Les quatre trous étaient le travail ; je les ai comblés et je n'ai pas élargi. En particulier je n'ai **pas** touché à Meta, qui reste le trou que je n'arrive pas à combler dans cet environnement, et qui n'est pas un choix mais un échec.

---

## 6. Verdict révisé

### 6.1 Ce que je corrige de mon premier retour

| Mon affirmation initiale | Correction |
|---|---|
| « Marché solvable : ~800 établissements, donc le modèle économique ne tient pas » | **Faux comme énoncé du marché.** 800 est le cœur touristique, pas le marché. Le marché adressable solvable est de **14 582 établissements employeurs** (INSEE Flores fin 2024), soit **dix-huit fois plus**, pour un plafond théorique de ~14 M€/an à 80 €. **Le marché est solvable.** |
| « Le document surestime le coût du guichet 1 » | **Vrai pour Google, faux pour Booking.** Booking écrit lui-même qu'il **suspend les intégrations de nouveaux fournisseurs de connectivité jusqu'à nouvel ordre**, et réserve l'API avis aux partenaires qui gèrent tarifs, disponibilités et réservations. Le document avait raison, pour une raison plus forte que celle qu'il donne |
| « Aucun acteur mondial ne construit à cette échelle » est faux, point final | **À nuancer sur le segment hôtelier.** Les détenteurs du guichet 1 servent le grand hôtel : la répartition des clients de ReviewPro est de 4 petits (10-49 chambres) contre 79 grands (100-499). Le parc guadeloupéen fait 59 chambres de moyenne et compte 24 hôtels non classés. **Sur ce segment précis, le document a raison.** Mais ce segment compte 24 à 55 établissements : une liste de clients, pas un marché |

### 6.2 Ce qui est confirmé, et renforcé

1. **La thèse de proximité de la section 2.7 est morte.** Confirmée fausse sur deux hôtes Google indépendants, dont la référence d'API : `accounts.admins.create` invite un administrateur **par adresse e-mail**, par appel programmatique, rôles `OWNER` ou `MANAGER`, avec droit de répondre aux avis et de publier des posts, sans mot de passe. Un concurrent mondial peut ouvrir le guichet 2 **en série, par script**.
2. **L'organe « Garde des accès confiés » tombe.** Le guichet 2 délègue un rôle et un jeton OAuth de portée `business.manage`, jamais un identifiant. Révocation par le client, dans son interface. Ce n'est pas un coffre-fort bancaire, c'est une table de jetons chiffrés avec rotation. Des semaines de construction rendues.
3. **Le plafond de prix tient, et il est encerclé par le bas et par le haut.** Plancher **0 €** : Google Business Profile fait les avis et les posts gratuitement ; Metricool est gratuit à vie. Milieu : Buffer 5 $/canal, Localo 39 $ avec posts auto-générés et réponse aux avis. **Nouveau cette fois : TrustYou Lite à 75 € par établissement et par mois**, sous le plafond local, avec boîte de réception centralisée de tous les avis, IA de sentiment et benchmark concurrentiel ; et TrustYou Professional à 180 € avec **réponses aux avis générées par IA, illimitées**. Plafond local en prestation humaine : **80 €**.
4. **Les six exigences ne s'appliquent qu'à 3,5-5,2 % du marché adressable solvable.** C'est le constat neuf de ce tour, et il est plus dévastateur que celui du premier. Sur 95 % de sa cible réelle, « la Guadeloupe est le cœur » ne donne aucun avantage.

### 6.3 Le verdict

**Y a-t-il un marché solvable ? Oui, et plus grand que je ne l'avais dit : 14 582 établissements employeurs, dont ~6 500 entreprises libérales que le document ne vise pas et qui n'ont aucun besoin de ses six exigences.**

**Le projet, tel que la section 3 le justifie, n'y a pas de place.** Non parce que le marché est trop petit, mais parce que :

- son avantage revendiqué — la proximité qui ouvre le mandat — est un mécanisme que Google documente comme un appel d'API ;
- son plafond de prix est de 80 € avec un plancher à 0 €, et trois à cinq produits occupent déjà l'intervalle, dont un sous le plafond ;
- la marge d'automatisation existe et elle est grosse — 80 € de prix de vente contre 1 h 23 de community manager achetable — **mais elle est déjà captée** par Localo, Metricool, Buffer, Digitaleo et TrustYou ;
- ses six exigences ne discriminent rien sur 95 % du marché adressable, et le segment où elles discriminent fait 500 à 800 clients.

**Les deux chemins qui restent ouverts, et qu'il faut trancher avant la section 10 :**

**Chemin 1 — vendre aux agences.** Dix acteurs locaux recensés, qui ont la relation client, le mandat, le portefeuille et quinze à dix-neuf ans d'ancienneté. Vingt agences à 400 €/mois valent 96 k€/an, sans force de vente, sans affronter la saisonnalité de trésorerie des établissements, et le plafond de 80 € ne s'applique plus — il s'applique à l'établissement final, pas à l'agence qui le facture. Localo le fait déjà avec son plan Pro à 149 $ pour 60 fiches en marque blanche, et lagencedigitale déclare travailler « parfois en marque blanche ».

**Chemin 2 — abandonner l'argument de marché et ne garder que la couche que personne ne vend.** Aucun des neuf concurrents du premier retour ni des quatre de celui-ci ne vend de **provenance vérifiable** : part des assertions remontées à une source primaire, part datée, part rejouable à l'identique. Aucun ne vend de **corpus de presse et d'institutions guadeloupéennes** — ce que le guichet 6 débloque selon la section 2.4. Aucun ne vend de **rédaction sourcée à zéro affirmation non vérifiée**. C'est là qu'est le produit. Ce n'est pas ce que la section 3 défend, et c'est ce que la section 6 décrit déjà sous le nom d'organe « Provenance ». **Le document contient déjà sa propre réponse, dans une autre section que celle qui prétend la porter.**

### 6.4 État de preuve de ce second retour

**Lignes en B : 22. Lignes en C : 2. Lignes en D : 8, déclarées en tête. A-mesure : zéro. A-usage : zéro.**

J'ai amélioré la qualité des sources — l'affirmation la plus destructrice est désormais confirmée sur deux hôtes Google indépendants dont le contrat d'API, les prix de TrustYou et Revinate viennent de leurs propres pages, les taux horaires viennent de Malt et de l'URSSAF citant un arrêté, le parc hôtelier vient de l'INSEE. **Mais je n'ai toujours rien mesuré ni installé**, et selon la règle 4.2 aucune décision de construire ne peut se prendre là-dessus. Le § 5.1 dit comment obtenir le premier A pour 80 €.

---

*Fin de la relance. Aucun commit. `critiques/02-marche.md` et `00-PROMPT-DE-LANCEMENT.md` non modifiés.*
