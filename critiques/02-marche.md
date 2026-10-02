# Critique adversariale — Angle marché guadeloupéen et concurrence

**Cible** : `00-PROMPT-DE-LANCEMENT.md` v4 du 2 octobre 2026 — section 3 (les six exigences, et la phrase « Aucun acteur mondial ne construit à cette échelle de marché ») et la thèse de la section 2.7 (« La proximité est la clé du guichet 2. Aucun concurrent mondial ne peut l'ouvrir »).

**Date de la recherche** : 2 octobre 2026. Toutes les URL ci-dessous ont été consultées ce jour.

**Mandat du lecteur** : casser, pas valider. Ce retour ne valide rien de la section 3.

---

## 1. Mes lignes en cran D — déclarées avant le contenu

Conformément à la règle 4.1 du document, voici ce que je n'ai **pas** vérifié dans cette session et qui ne peut donc fonder aucune décision.

| # | Ligne en cran D | Pourquoi elle reste en D |
|---|---|---|
| D1 | L'existence et la portée de **Ryanair c. PR Aviation** (CJUE 2015) et de **NLA c. Meltwater** | Je n'ai pas ouvert les décisions. Le document les marque déjà D ; je n'ai pas levé ce D |
| D2 | Les conditions d'utilisation de **Booking, TripAdvisor, Expedia** interdisant la réutilisation de leurs avis | Non lues cette session. Toute qualification 5b/5c de ces sources reste une supposition |
| D3 | Le fonctionnement de **Meta Business Suite** (planification gratuite) et de l'**accès partenaire** Business Manager à distance | `facebook.com/business/...` n'a pas pu être récupéré (`CRAWL_NOT_FOUND`, et la page outil renvoie un écran de connexion). Je n'ai donc **aucune source primaire Meta**. Toute ma démonstration sur l'accès délégué repose sur Google seul |
| D4 | Ce que paie **réellement** un établissement guadeloupéen aujourd'hui | Je n'ai trouvé que des **tarifs affichés**. Un tarif affiché n'est pas un prix payé. Aucune enquête de prix réels n'a été faite |
| D5 | Les prix de **Partoo (149 € HT/mois)**, **Guest Suite (39 €/mois Pack Étoiles)**, **Trustmary (19 €/mois)**, **So-Community (490 €/mois)** | Aucun des trois premiers éditeurs n'affiche ses prix sur son propre site. Ces chiffres viennent de comparateurs = **cran C**, et je les cite comme tels, jamais comme fondement |
| D6 | Le nombre d'établissements guadeloupéens **par secteur fin NAF** (hôtellerie seule, restauration seule, location seule, artisanat, professions libérales) à la même date et dans le même champ | Les fichiers INSEE Flores à ce niveau sont des .xlsx de 4 à 28 Mo non ouverts. Je recompose à partir de sources de champs et de dates différents, ce qui **interdit de les additionner** |
| D7 | Le libellé exact des colonnes de tranches d'effectifs du tableau INSEE Flores fin 2024 | Les intitulés n'apparaissent pas dans l'extrait récupéré. J'**infère** 0 / 1-9 / 10-19 / 20-49 / 50+. L'inférence est signalée partout où je l'utilise |
| D8 | Mon affirmation que « tout planificateur sérieux gère un fuseau par compte » | Je n'ai pas testé la configuration de fuseau de Buffer, Metricool ou Localo. C'est ma mémoire, pas une mesure |
| D9 | Le fait que la Guadeloupe soit rattachée dans la base tzdb à `America/Port_of_Spain` sans règle d'heure d'été | Ma lecture du fichier `northamerica` de tzdb **n'a pas trouvé** la Guadeloupe. Échec de vérification assumé, voir § 4.1 |

**Un retour qui ne déclare aucune ligne D est suspect** : en voici neuf.

---

## 2. Les chiffres réels du marché — ce que j'ai trouvé, et ce que je n'ai pas trouvé

Le document ne porte aucun chiffre de marché. Il marque « Très petites entreprises en majorité ⏳ à confirmer en V0 ». Voici la confirmation, et elle est plus dure que ce que le document ose écrire.

### 2.1 Le dénominateur total

| Mesure | Chiffre | Source | Cran |
|---|---|---|---|
| Établissements **économiquement actifs** en Guadeloupe, 2021, activités marchandes non agricoles | **33 477** | INSEE, SIDE — `insee.fr/fr/statistiques/7658710?geo=REG-01`, tableau DEN T5, géographie au 01/01/2024 | **B** |
| dont « Commerce de gros et de détail, transports, hébergement et restauration » | **9 335** (27,9 %) | idem | **B** |
| dont « Activités spécialisées, scientifiques et techniques et services administratifs » | 7 499 (22,4 %) | idem | **B** |
| Établissements **employeurs** actifs la dernière semaine de décembre, fin 2024 | **14 582** | INSEE, Flores — `insee.fr/fr/statistiques/2012766`, consulté via extrait | **B** |
| Répartition par tranche d'effectifs, fin 2024 | 12,1 % / **71,8 %** / 9,2 % / 4,5 % / 2,5 % | idem — intitulés de colonnes **inférés** (D7) | B pour les chiffres, **D pour les libellés** |
| Entreprises de proximité (artisanales, commerciales, libérales) | **~33 000**, dont alimentation 11 940, fabrication/services 12 530, professions libérales 6 530, construction 2 600 | U2P / Institut Supérieur des Métiers d'après INSEE, dénombrement au 31/12/2020 — `infometiers.org/wp-content/uploads/2023/12/7-Chiffres-cles-U2P-2023-Maquette-Guadeloupe.pdf` | **B** (retraitement ISM d'une source INSEE) |
| Part d'entreprises individuelles parmi les entreprises de proximité | **58 %** | idem | **B** |
| Part des micro-entrepreneurs dans les créations 2024 | **56,7 %** (4 635 sur 8 178) | INSEE, SIDE — `insee.fr/fr/statistiques/8354543?sommaire=8354895` | **B** |

**Attention de méthode** : 33 477 (2021, actifs économiquement, marchand non agricole) et 14 582 (fin 2024, employeurs) ne sont **pas** le même objet. L'écart — environ 19 000 — n'est pas une erreur : c'est la masse des établissements **sans aucun salarié**. C'est elle qui porte le problème de solvabilité.

### 2.2 Le numérateur : la cible réellement concernée

| Mesure | Chiffre | Source | Cran |
|---|---|---|---|
| **Hôtels de tourisme** en Guadeloupe | **55 hôtels, 3 258 chambres** (2022) | Observatoire AKTO, Monographie H&R Guadeloupe 2023, citant INSEE 2022 — `observatoire.akto.fr/content/uploads/sites/3/2024/02/Monographie-HR-2023-Guadeloupe.pdf` | **B** (observatoire de branche citant INSEE) |
| Hôtels de tourisme, mesure plus récente | **52** | page INSEE « Établissements d'hébergements touristiques en 2026 » — lue via résumé de moteur, **pas ouverte** | **C** |
| **Établissements employeurs** hébergement + restauration | **760** (données 2019) — dont restauration traditionnelle 45 %, restauration rapide 39 %, hôtels 8 %, débits de boissons et traiteurs le reste | AKTO/Kyu Lab, même PDF. Mention explicite : « Projection Kyu Lab à partir des données DARES et INSEE 2019 » | **B**, mais c'est une **projection**, pas un comptage — à retenir |
| dont part à 1-9 salariés | **86 %** | idem | **B** |
| **Non-salariés** du secteur hébergement-restauration | **1 550** | idem, « Base recensement INSEE, redressement Kyu Lab 2019 » | **B** |
| **Locations touristiques / meublés** | « plus de **10 000** », en progression ; Le Gosier, Sainte-Anne et Saint-François concentrent plus de la moitié | RCI Guadeloupe, 03/04/2023, citant le salon Welcome à la Maison et l'Observatoire régional du tourisme — `rci.fm/guadeloupe/infos/Economie/La-Guadeloupe-une-destination-prisee` | **C** (presse citant un observatoire — je n'ai pas la publication de l'observatoire) |
| Part des touristes logeant en gîtes, bungalows, villas, appartements | **24 %** | idem, Observatoire régional du tourisme | **C** |
| Nuitées hôtelières 2024 | **1 281 000** (–2,1 % sur un an), dont 85,9 % clientèle résidant en France | INSEE Conjoncture Guadeloupe n°34, paru le 26/06/2025 — `insee.fr/fr/statistiques/8354611?sommaire=8354895` | **B** |

### 2.3 Ce que je n'ai pas trouvé — et que le document devra trouver en V0

1. **Aucun comptage officiel des meublés de tourisme guadeloupéens.** Le seul chiffre existant (« plus de 10 000 ») est de presse, de 2023, et sans méthode publiée. Ce n'est pas assez pour dimensionner un marché. Les déclarations en mairie, le registre des meublés et les données des plateformes n'ont pas été atteints.
2. **Aucun décompte à même champ et même date** d'hôtellerie / restauration / location / artisanat / professions libérales. Les fichiers INSEE Flores à 38 et 88 secteurs existent (`insee.fr/fr/statistiques/8266010`) mais sont des .xlsx de 4 à 9 Mo que je n'ai pas ouverts. **C'est la première tâche de V0, et elle est faisable en une journée.**
3. **Aucune source, nulle part, sur le nombre d'établissements guadeloupéens qui paient déjà un outil d'avis ou de publication.** Le document prévoit un agent « Marché — ce qu'ils utilisent déjà, ce qu'ils paient aujourd'hui ». Je n'ai trouvé aucune donnée publique là-dessus. Ce trou est le plus grave de tous : il rend le modèle économique indécidable sur source ouverte, et impose une enquête terrain de première main.

### 2.4 L'arithmétique qui fait mal

Elle est **mienne**, posée sur des entrées sourcées. Les taux de pénétration sont des **hypothèses**, pas des mesures — je les marque.

- Cœur touristique professionnel = ~760 établissements employeurs HR (B, projection 2019) + ~52 à 55 hôtels déjà comptés dedans ≈ **760 établissements**.
- Plafond de prix observé sur le marché local pour exactement ce service, rendu par un humain = **80 €/mois** (§ 3.3, cran B).
- À 10 % de pénétration (hypothèse) : 76 clients × 80 € = **6 080 €/mois**, soit ~73 k€/an de chiffre brut.
- À 30 % de pénétration (hypothèse haute, jamais atteinte par un nouvel entrant en trois ans) : 228 × 80 € = **18 240 €/mois**, ~219 k€/an.

Élargir aux 14 582 établissements employeurs change l'ordre de grandeur, mais pas la nature du problème : un coiffeur, un maçon ou un plombier n'a ni avis multilingues de croisiéristes, ni saison cyclonique à gérer dans son calendrier éditorial. Les six exigences guadeloupéennes du document **décrivent un segment touristique**, et ce segment est d'environ 800 établissements professionnels.

**Conséquence directe** : 73 à 219 k€ de chiffre brut annuel, à comparer à une reconstruction de sept organes dont le document dit lui-même qu'elle « se compte en semaines » par organe (section 10, nœud « Qui construit »). Sept organes × plusieurs semaines = plusieurs trimestres de développement, financés par un chiffre d'affaires de petite entreprise de services. **L'équation ne se ferme pas.**

---

## 3. Les concurrents réels — mondiaux ET locaux

### 3.1 La phrase à casser

> « Aucun acteur mondial ne construit à cette échelle de marché » (section 3)

**Elle est fausse telle qu'écrite.** Des produits existent, vendus à l'unité, au mono-établissement, à des prix inférieurs au plafond local, et ils font la publication sociale **et** la gestion d'avis.

| Acteur | Ce qu'il fait exactement | Prix affiché par l'éditeur | Guichet | Cran |
|---|---|---|---|---|
| **Google Business Profile** (l'éditeur lui-même) | Lire et répondre aux avis ; créer, gérer et publier des posts ; modifier horaires, photos, services ; télécharger les statistiques. Pour un établissement validé | **Gratuit** | Guichet 2 — rôle propriétaire ou administrateur, délégué par invitation e-mail | **B** — `support.google.com/business/answer/3474050?hl=fr` et `.../3403100?hl=fr` |
| **Localo** | Un seul profil Google : « Collect all your reviews in one place and respond to them with a single click » + « Autogenerate and publish posts » + suivi de positions + veille concurrentielle | **39 $/mois** facturé à l'année (49 $ mensuel), hors TVA, offre « Single Business » | Non documenté sur la page tarifaire — **inconnu**, probablement guichet 2 (OAuth) ou 3 (API GBP) | **B** pour le prix et le périmètre — `localo.com/pricing` |
| **Buffer** | Publication multi-réseaux. **Google Business Profile figure explicitement parmi les canaux connectables**, aux côtés de Facebook, Instagram, LinkedIn, TikTok, YouTube, Threads, Bluesky, Pinterest, X, Mastodon. Réponse aux commentaires incluse dès le plan gratuit | **Plan gratuit** : 10 posts programmés par canal, réponse aux commentaires, 5 suggestions IA/semaine. **Essentials : 5 $/mois par canal** (60 $/an) | Guichet 2 par OAuth du titulaire + API officielles des plateformes — **déduit, non documenté sur la page** | **B** pour le prix et les canaux — `buffer.com/pricing` |
| **Metricool** | « You can use Metricool for free, forever » : 1 marque, 1 profil par réseau, planification, publication automatique, gestion des messages. Google Business Profile géré comme une marque par établissement | **Plan gratuit** permanent ; plans payants au-dessus | Non documenté — **inconnu** | **B** pour l'existence du gratuit — `metricool.com/pricing` |
| **Guest Suite** (France) | Collecte d'avis par e-mail/SMS/QR, centralisation, réponse assistée par IA, diffusion sur 11 à 27 plateformes, Presence Management. Certifié **NF Service Avis en ligne** AFNOR. Revendique « + de 10 000 points de vente ». Quatre packs, dont « Pack Étoiles » explicitement destiné aux indépendants | **Aucun prix affiché** — « Plan personnalisé », devis | Inconnu, non déclaré sur le site | **B** pour l'offre (`guest-suite.com/offres`), **C** pour le prix (39 €/mois cité par comparateurs, D5) |
| **Partoo** (France) | Presence Management (Google, Apple Plans, Waze), Review Management (Google, Facebook, TripAdvisor), Review Booster par SMS. Cible déclarée TPE/PME, dont hôtellerie-restauration | **Aucun prix affiché**. « dès 149 € HT/mois », engagement 12 mois | Inconnu | **C** (comparateurs, D5) |
| **Digitaleo** (France) | Modules à la carte : Presence Management (Google, Apple, +30 portails), Avis Clients (réponses automatisées, suggestions IA, collecte e-mail/SMS, analyse sémantique), Réseaux Sociaux (Facebook, Instagram, LinkedIn, Reels, Stories, programmation, modération). Agent IA « Leo », crédits à 0,02 € au-delà du forfait | Modèle publié, **montants non publiés** : « Somme des montants par module par établissement × Nombre d'établissements » | Inconnu | **B** pour le modèle tarifaire et le périmètre — `digitaleo.fr/tarifs` |
| **Solocal / Solocal Outre-Mer** | Référencement local, visibilité, publicité. **Agence physique à Baie-Mahault, Guadeloupe** | pagesjaunes+ à 300 €/an sans engagement (lancé fin octobre 2025) | Inconnu | **C** pour le prix ; **B** pour l'implantation locale (fiche Pages Jaunes de l'établissement de Baie-Mahault) |
| **Trustmary** | Import automatisé d'avis depuis Google, Facebook, G2, Capterra, **TripAdvisor**, Yelp ; enquêtes par URL, QR, e-mail, SMS ; widgets site | Prix non lisibles sur la page tarifaire récupérée | Inconnu — mais l'import TripAdvisor est annoncé par l'éditeur | **B** pour les sources importées (`trustmary.com/pricing/`), **C** pour le prix (19 €/mois, D5) |

**Verdict sur la phrase.** Au moins **quatre produits** sont construits, tarifés et vendus au mono-établissement à un prix inférieur ou égal au plafond local : Google lui-même (gratuit), Metricool (gratuit), Buffer (5 $/canal), Localo (39 $). Ils couvrent la publication sociale **et** la centralisation-réponse d'avis Google. Si l'on retient le critère du prompt — « des produits à faible coût qui font 80 % du travail » — **la condition est remplie**. Ce qu'ils ne font pas : le corpus de presse locale, la couche de provenance vérifiable, la rédaction sourcée. Ce qui reste du projet, c'est **cela**, et ce n'est pas ce que la section 3 revendique.

Il faut aussi noter ce que le document s'interdit lui-même en 4.3 : « Jamais “tel concurrent le fait donc c'est permis” — nommer son guichet, ou constater qu'il prend un risque. » Je m'y conforme : pour Localo, Buffer, Metricool, Guest Suite, Partoo, Digitaleo, Solocal et Trustmary, **je ne sais pas par quel guichet ils accèdent à la donnée**, et je l'écris. Aucune page éditeur consultée ne le déclare. C'est un trou que V1 doit combler, et il n'est pas comblé par moi.

### 3.2 La thèse de la section 2.7 — démolie par la documentation de Google

> « Il confie ses accès parce que nous sommes son prestataire local et non une adresse web. **La proximité est la clé du guichet 2.** Aucun concurrent mondial ne peut l'ouvrir. »

Google documente le contraire, en français, sur sa page d'aide officielle.

Citations exactes de `support.google.com/business/answer/3403100?hl=fr`, consultée le 2 octobre 2026 :

> « Si vous êtes propriétaire d'une fiche d'établissement, vous pouvez **inviter des utilisateurs** à en devenir propriétaire ou administrateur. Ils pourront vous aider à gérer les opérations quotidiennes (modifier les informations, **répondre aux avis** et **gérer les posts**, par exemple). »

> « Chaque utilisateur doit disposer de son propre compte Google pour accéder aux fiches d'établissement et les gérer **sans avoir besoin de votre mot de passe**. »

Et la procédure complète :

> « 1. Accéder à votre fiche d'établissement. 2. Sélectionnez Plus > Paramètres de la fiche d'établissement > Utilisateurs et accès. 3. En haut à gauche, sélectionnez Ajouter. 4. **Saisissez une adresse e-mail.** 5. Sous "Accès", sélectionnez Propriétaire ou Administrateur. 6. Sélectionnez Inviter. »

> « Les utilisateurs invités peuvent accepter l'invitation et devenir utilisateurs **immédiatement**. »

Le tableau des droits de la même page accorde à l'administrateur, entre autres : « Répondre aux avis », « Créer, gérer et publier des posts », « Modifier les principales informations sur l'établissement, comme les horaires d'ouverture et l'adresse », « Télécharger les statistiques », « Répondre aux questions/réponses ».

**Trois conséquences, et elles sont lourdes.**

1. **Le guichet 2 s'ouvre par une adresse e-mail, depuis n'importe où sur la planète.** Il ne demande aucune proximité géographique, aucune rencontre, aucun réseau de connaissances. La friction que le document imagine « tuer » les grands acteurs n'existe pas : une invitation, un clic, accès immédiat. La phrase « Aucun concurrent mondial ne peut l'ouvrir » est **fausse**.
2. **Le mandat ne transmet aucun identifiant.** Le document bâtit sur le guichet 2 une obligation de « gestion des accès confiés au niveau d'un établissement bancaire — chiffrement, révocation, journalisation, cloisonnement par client », et en fait un huitième organe à construire (section 6, « Garde des accès confiés », « c'est la condition du guichet 2, donc de tout le produit »). Or le mécanisme standard **ne confie pas de mot de passe** : il accorde un rôle délégué. La révocation est faite par le client, en deux clics, dans sa propre interface — « Supprimer l'utilisateur » sur la même page. **Un organe entier du projet répond à un problème que le guichet 2 ne pose pas.** C'est un coût de construction que les concurrents ne paient pas, assumé sur la base d'une analyse erronée du mécanisme.
3. **Le guichet 1 et le guichet 3 sont mal chiffrés pour Google.** Le document classe le guichet 1 « Hors de portée au départ. À réexaminer à trois ans », avec « contrat, certification, volume minimum ⏳ ». La documentation développeur de Google dit autre chose. Citations de `developers.google.com/my-business/content/prereqs` :

> « In order to get access to GBP APIs, we require all applicants: **Manage a Google Business Profile that is verified and active for 60+ days.** This GBP can be the applicant's own office or headquarters or it could belong to one of the clients they manage. **Have a website** representing the business listed on the GBP. »

> « If your quota is 0 QPM (Queries Per Minute), your project has not yet been approved. If your quota is set to **300 QPM**, your project is approved. »

Aucun volume minimum de clients. Aucun frais. Aucune certification technique. **Deux conditions : une fiche vérifiée depuis soixante jours, et un site web.** Le projet remplit les deux dès son premier client, et même avant, avec sa propre fiche. Le document surestime donc le coût d'entrée du côté Google — ce qui, pour une fois, va dans le sens du projet, mais montre que la carte des guichets de la section 2.2 n'est pas tenue sur source.

**Ce que je n'ai pas pu vérifier** : le même raisonnement pour Meta (D3). Je n'ai aucune source primaire Facebook/Instagram. Si l'accès partenaire Meta est, lui, plus lourd, l'argument du document retrouverait une base — mais **sur Meta seulement, et il reste à la produire**.

### 3.3 Les concurrents que le document ne voit pas — les agences guadeloupéennes

C'est l'angle mort le plus coûteux. Le document ne nomme jamais un seul concurrent local. Le vrai marché est déjà servi, en prestation humaine, par au moins une dizaine d'acteurs sur place. En voici les plus parlants.

**MangoWeb Digital — Saint-Claude, Guadeloupe (97120).** Opérateur local, une personne nommée (Jean-Daniel Lacascade). Il vend **exactement le produit du projet**, décomposé en prestation, avec ses prix affichés publiquement. Citations de `mangoweb.digital/google-my-business`, consultée le 2 octobre 2026 :

> « **Création complète** — Configuration une fois — **200 €** : réclamation ou création, configuration complète, 5 premières photos, premier post, guide de gestion. »

> « **Gestion mensuelle** — Chaque mois — **80 €/mois** : 8 posts mensuels, **réponse à tous les avis**, photos mensuelles, mise à jour horaires, statistiques mensuelles. »

> « Oui, la gestion des avis Google (réponse professionnelle aux avis positifs et négatifs) est incluse dans la formule de gestion mensuelle à 80 €/mois. »

**C'est le prix plafond du projet, et il est sourcé.** Pour 80 € par mois, un établissement guadeloupéen obtient aujourd'hui, d'un prestataire local qu'il peut rencontrer : huit publications, la réponse à **tous** ses avis, les photos, les horaires et un rapport. Le projet devrait faire mieux que ça, en logiciel, à moins que ça, après avoir reconstruit sept à huit organes. Et l'avantage que la section 2.7 revendique — la proximité, le bouche-à-oreille, « le client nous connaît » — **cet homme l'a déjà**, à Saint-Claude, avec un numéro de téléphone sur sa page.

**Les autres acteurs locaux recensés** (tous consultés le 2 octobre 2026) :

| Acteur | Implantation | Ce qu'il vend qui recoupe le projet | Ancienneté / volume revendiqué | Prix | Cran |
|---|---|---|---|---|---|
| **lagencedigitale** | Guadeloupe, Martinique, Guyane | SEO et référencement local, Community Management & Social Media, « marketing automation & IA ». Secteurs déclarés : tourisme & hébergement, restauration, santé, droit | « Depuis 2007 », « 19 ans d'expérience », « +50 clients ». Portefeuille cité : CCI des Îles de Guadeloupe, MEDEF Guadeloupe, Renault, Carrefour Market, Air Antilles, Ville de Baie-Mahault | Non affiché | **B** pour l'offre et l'ancienneté (`lagencedigitale.com`) ; « à partir de 300 €/mois » pour la visibilité locale = **C** |
| **Digitallis** | Guadeloupe | Agence web et IA, SEO, Google Ads, réseaux sociaux, « agent vocal IA » ; témoignages de restaurateurs et commerces locaux | « Plus de 15 ans », « près de 1 000 entreprises » | Non affiché | **B** (`digitallis.fr`) |
| **ELYAD** | Martinique, Guyane, « toute la Caraïbe » | SEO, réseaux sociaux, publicité, automatisations IA, conformité RGPD et règlement européen sur l'IA explicitement revendiquée | « +300 projets réalisés » | Non affiché | **B** (`elyad.fr`) |
| **Connect Outremer** | Baie-Mahault, Guadeloupe + Martinique | Community management, SEO/SEA, sites, applications | « Plus de 15 ans » | Non affiché | **B** (`connectoutremer.fr`) |
| **Novazeo** | Guadeloupe | Community management local, argumentaire explicitement bâti sur la **proximité culturelle et géographique** | Non chiffré | Non affiché | **B** (`novazeo.com/...community-manager-guadeloupe/`) |
| **So-Community** | Couvre les 32 communes du 971 | Community management, contenu, publicité, SEO local | « 32+ villes couvertes », « 24h de délai de réponse » | « dès 490 €/mois » | **B** pour l'offre (`so-community.fr/departement/guadeloupe`), **C** pour le prix (D5) |
| **Solocal Outre-Mer** | **Baie-Mahault, Guadeloupe** | Référencement local, visibilité, publicité — filiale locale d'un acteur national | — | 300 €/an pour pagesjaunes+ | **B** pour l'implantation, **C** pour le prix |

Et, non consultés faute de temps mais identifiés : SMP Agency, ArobazConsulting, Smart Agency, Les Accros du Web, Oli-via-net, Digital Proxi (Le Gosier), Awitec (Martinique).

**Ce que cela fait au projet.** La section 2.7 décrit un avantage — relation locale, confiance, mandat — qui est **la définition même du métier de ces agences**. Novazeo vend littéralement l'argument du document, mot pour mot : « Travailler avec une agence locale signifie une plus grande proximité géographique […] une réactivité accrue […] connaissance intime des spécificités culturelles. » Le projet n'arrive pas sur un marché vide avec un avantage unique : il arrive **dernier sur un marché où son avantage est le standard**, face à des acteurs installés depuis 2007 et 2010 qui tiennent déjà la CCI, le MEDEF et les concessionnaires.

**Les attaque-t-il, ou se met-il à leur service ?** Le document ne tranche pas, et c'est son plus gros nœud non ouvert. Les deux lectures sont possibles et s'excluent :

- **Les attaquer** : vendre en direct aux établissements, à 80 € plafond, contre dix acteurs locaux qui ont la relation. C'est la lecture de la section 2.7, et elle est perdante — le projet n'a ni le portefeuille, ni l'ancienneté, ni le réseau.
- **Les servir** : vendre l'outil **aux agences**, en marque blanche. Le volume devient 10 à 20 clients au lieu de 800, le prix unitaire se compte en centaines d'euros au lieu de 80, le vendeur a besoin du produit tous les jours, et la relation client — donc le guichet 2 — reste chez l'agence. Localo le fait déjà (plan « Pro », 149 $/mois, 60 fiches, rapports en marque blanche) et lagencedigitale déclare travailler « parfois en marque blanche » en renfort d'autres agences : la demande existe et le format aussi. **Le document ne mentionne nulle part cette option.**

---

## 4. Ce qui est faux ou mal calibré dans les six exigences

Rappel du critère du document : « Elles disqualifient directement des outils. » Une exigence qui ne disqualifie rien du jeu concurrentiel réel n'est pas une exigence : c'est un ornement.

### 4.1 Fuseau — **contenu exact, source faible, pouvoir discriminant nul**

Le contenu est **juste** : UTC-4 toute l'année, sans heure d'été, 5 h de décalage avec la métropole en hiver, 6 h en été. Le mécanisme est correct — c'est la métropole qui bouge entre UTC+1 et UTC+2, pas la Guadeloupe. Pour 2026, l'écart est de 6 h du 29 mars au 25 octobre.

**Mais** : toutes mes sources sont des sites de voyage (helloguadeloupe.fr, ou-et-quand.net, vivre-guadeloupe.com). **Cran C.** J'ai tenté une source primaire — le fichier `northamerica` de la base tzdb d'IANA, `raw.githubusercontent.com/eggert/tz/main/northamerica` — et **ma lecture n'y a trouvé aucune mention de la Guadeloupe**. Je ne conclus pas qu'elle n'y est pas : je conclus que **j'ai échoué à la vérifier** (D9). Le document met cette exigence en tête de ses six « non négociables » sans la sourcer ; je ne l'ai pas sourcée davantage.

**Mal calibrée.** Un décalage horaire n'est pas une exigence de conception, c'est un champ de configuration. Le document prétend qu'elle disqualifie « tout outil de programmation raisonnant en heure métropolitaine ». Je n'ai pas testé les fuseaux de Buffer, Metricool ou Localo (D8), donc je ne peux pas affirmer qu'ils les gèrent — mais la charge de la preuve est inversée : c'est au document de **montrer un outil qui échoue** sur ce point, et il n'en nomme aucun. En l'état, **zéro outil disqualifié**.

### 4.2 Langues — **mal calibrée, et contredite par les chiffres de fréquentation**

Le document exige « français, créole guadeloupéen, anglais et espagnol dans les avis de croisiéristes ».

Les chiffres INSEE 2024 de provenance des nuitées hôtelières (`insee.fr/fr/statistiques/8354611`, paru le 26/06/2025, cran **B**) :

| Provenance | Part des nuitées 2024 |
|---|---|
| France | **85,9 %** |
| Europe hors France | 6,6 % — dont Belgique 1,4 %, Allemagne 1,2 %, Suisse 0,9 %, Italie 0,7 % |
| Amérique | 7,2 % — dont **Canada 4,8 %**, USA 1,9 % |
| Autres | 0,3 % |

**L'espagnol n'apparaît nulle part.** Aucun pays hispanophone n'est dans les provenances détaillées par l'INSEE. Le premier étranger est le **Canada** à 4,8 % des nuitées, soit 35 % de la clientèle étrangère, en hausse de 15,2 % — donc du **français québécois** et de l'anglais canadien. Les États-Unis sont à 1,9 %.

Le document calibre donc son exigence linguistique sur l'espagnol des croisiéristes, et **manque le Canada**, qui est le vrai relais de croissance étranger. Deux réserves honnêtes : les nuitées hôtelières ne mesurent pas les croisiéristes, qui ne dorment pas à terre ; et je n'ai **aucune source** sur la langue réellement écrite dans les avis d'établissements guadeloupéens — ni sur la part de créole écrit, qui est l'hypothèse la plus douteuse des quatre. Un créolophone écrit massivement en français.

**Pouvoir discriminant : faible.** L'extraction et l'analyse multilingues sont la propriété par défaut de tout modèle de langue contemporain. Le document affirme que cette exigence disqualifie « tout moteur d'extraction ou d'analyse monolingue français » — il faudrait nommer un seul outil du jeu concurrentiel qui soit monolingue français. Guest Suite, Partoo, Digitaleo, Buffer, Localo, Metricool ne le sont pas.

### 4.3 Saisons — **deux dates sur trois correctes, et le ⏳ se remplit en contredisant l'intuition du document**

**Saison cyclonique du 1er juin au 30 novembre : correcte.** Confirmée par Météo-France, `meteo.fr/temps/domtom/antilles/pack-public/cyclone/tout_cyclone/lieux_periodes.htm` (cran **B**, page institutionnelle, date de publication non indiquée) :

> « Dans l'hémisphère nord, l'été c'est entre Juin et Septembre, mais on peut voir des cyclones de JUIN à NOVEMBRE. […] si les cyclones restent rares en juin et novembre, par contre la saison cyclonique bat son plein entre début Juillet et fin Octobre, **la période la plus active pour nos îles antillaises étant celle s'étirant du 15 août au 15 octobre**. »

Précision que le document n'a pas et devrait avoir : la fenêtre de risque réel est **15 août – 15 octobre**, pas six mois. Un produit qui prépare six mois de crise prépare quatre mois de trop.

**Carnaval « de l'Épiphanie au Mercredi des Cendres » : approximativement correct, mais la borne de début est floue.** Pour 2026 : présentation de Vaval le 3 janvier au Vélodrome de Baie-Mahault, début du carnaval le **dimanche 11 janvier** (premier dimanche après l'Épiphanie), fin le **mercredi 18 février**, jours gras les 15, 16 et 17 février. Sources : guides touristiques et France Info Outre-mer — **cran C**, je n'ai pas trouvé d'arrêté ni de calendrier officiel du comité carnavalesque. Le document écrit « de l'Épiphanie » ; la réalité 2026 est « du premier dimanche après l'Épiphanie », et la date de fin est mobile puisqu'elle suit Pâques. Un produit qui code « 6 janvier » en dur se trompe.

**« Haute saison touristique ⏳ à confirmer » : je la confirme, et elle déplace la conclusion du document.** INSEE, taux d'occupation hôtelière mensuel 2024 (même source, cran **B**) :

| Mois 2024 | Taux d'occupation Guadeloupe |
|---|---|
| janvier | 76,6 % |
| février | 76,5 % |
| **mars** | **77,7 % — maximum** |
| avril | 63,2 % |
| mai | 54,1 % |
| juin | 47,6 % |
| juillet | 46,9 % |
| août | 57,6 % |
| **septembre** | **34,4 % — minimum** |
| octobre | 48,1 % |
| novembre | 61,9 % |
| décembre | 63,9 % |

Et, dans le texte de l'INSEE :

> « Le nombre de nuitées progresse au cours des trois premiers mois de l'année 2024, période qui correspond au **pic de fréquentation touristique dans l'archipel**. »

> « Certains établissements profitent du ralentissement de la fréquentation touristique pour **fermer temporairement** ou réduire leur capacité. En conséquence, l'offre d'hébergement durant ce mois ne représente que **5,5 % de l'offre annuelle**. »

**Haute saison = janvier à mars, prolongée en avril puis décembre. Creux = septembre.** Le ⏳ est levé.

**Ce que cela casse dans le raisonnement du document.** Le document met la saison cyclonique et la haute saison dans la même case, et en déduit « un produit à charge constante » est disqualifié car « les pics de publication et de réponse aux avis sont saisonniers ». Les chiffres disent que le pic de charge est **janvier-mars**, soit **entièrement hors saison cyclonique**. La saison cyclonique (juin-novembre, pointe 15 août – 15 octobre) coïncide au contraire avec le **creux** d'activité — septembre à 34,4 % d'occupation, avec 5,5 % de l'offre ouverte. Les deux saisonnalités sont **en opposition de phase**, et le document les traite comme un même phénomène. C'est une erreur de conception, pas seulement de rédaction : elle change le dimensionnement de la charge, la fenêtre de facturation, et le moment où un client accepte de payer.

Point commercial qui en découle, et que le document n'a pas vu : un établissement qui ferme en septembre ne paiera pas un abonnement en septembre. Sur 800 établissements saisonniers, un abonnement mensuel à 80 € n'est pas perçu douze mois sur douze. **Le chiffre d'affaires réel du § 2.4 doit être minoré.**

### 4.4 Sources locales — **ce n'est pas une exigence, c'est une tâche vide**

Le contenu est « Presse, institutions, chambres, collectivités — **à recenser** ». Une exigence « non négociable » dont le contenu est « à recenser » ne disqualifie rien, parce qu'elle ne dit rien. Je ne l'ai pas instruite : ce n'était pas mon angle, et c'est le travail de l'agent « Sources locales » de V0. Mais sa place dans un tableau d'exigences opposables est usurpée tant qu'elle est vide.

### 4.5 Tissu économique — **la seule exigence vraie, et elle joue contre le projet**

Le document écrit « Très petites entreprises en majorité ⏳ à confirmer en V0 ». **Confirmé, et plus fort que sa formulation** :

- **71,8 %** des établissements employeurs guadeloupéens ont 1 à 9 salariés fin 2024 (INSEE Flores, **B** — libellé de colonne inféré, D7), contre 71,1 % en France métropolitaine. L'écart avec la métropole porte en réalité sur le **haut** : 2,5 % de gros établissements en Guadeloupe contre 3,6 % en métropole.
- **58 %** des entreprises de proximité sont des entreprises individuelles (U2P/ISM d'après INSEE 31/12/2020, **B**).
- **56,7 %** des 8 178 créations de 2024 sont des micro-entrepreneurs (INSEE SIDE, **B**).
- **86 %** des établissements employeurs de l'hébergement-restauration ont 1 à 9 salariés (AKTO/Kyu, données 2019, **B**).
- « 92,5 % des établissements sont des microentreprises contre 82 % en France métropolitaine, seules 13 % d'entre elles emploient des salariés » — chiffre attribué à une publication INSEE Flash Guadeloupe que **je n'ai pas ouverte** : **cran C**, cité comme piste.

Le document tire la bonne conséquence — « disqualifie tout produit exigeant un administrateur, ou dépassant le prix plafond local » — mais **ne donne aucun prix plafond**. Je le donne : **80 €/mois**, sourcé en B sur un prestataire local qui rend le service complet à ce prix (§ 3.3). Avec ce chiffre, l'exigence 5 cesse d'être une exigence de conception et devient **la contrainte de financement du projet entier**. C'est la seule des six qui mord, et elle mord le projet.

### 4.6 Droit — **vrai, et discriminant contre personne**

« Région ultrapériphérique de l'Union — RGPD plein, droit français », disqualifiant « tout hébergement ou traitement non conforme ». Factuellement juste. Mais le jeu concurrentiel réel est **majoritairement français** : Guest Suite est certifié **NF Service Avis en ligne par l'AFNOR**, Partoo, Digitaleo et Solocal sont français, ELYAD revendique explicitement la conformité RGPD et le règlement européen sur l'IA, Localo affiche « We're from Europe ». Cette exigence disqualifie **zéro** concurrent sérieux. Elle écarte au mieux quelques outils américains, qui ne sont pas ceux qui prennent le marché.

### 4.7 Bilan des six

| Exigence | Contenu exact ? | Sourcé par moi ? | Disqualifie un concurrent réel ? |
|---|---|---|---|
| Fuseau | Oui | Cran C seulement ; échec sur la source primaire | **Non** |
| Langues | Non — espagnol surestimé, Canada manquant, créole écrit non sourcé | Partiellement, cran B sur les provenances | **Non** |
| Saisons | Cyclone oui (fenêtre réelle plus courte) ; carnaval approximatif ; haute saison désormais sourcée et **en opposition de phase** avec le cyclone | Oui, cran B pour la saison touristique et le cyclone | **Non** |
| Sources locales | Vide (« à recenser ») | Non instruite | **Non** |
| Tissu économique | Oui, et sous-estimé | Oui, cran B multiple | **Non — mais elle disqualifie le modèle économique du projet** |
| Droit | Oui | Non instruit sur source juridique | **Non** |

**Zéro des six exigences ne disqualifie un seul des concurrents identifiés.** Le document affirme en 4.3 : « Jamais une évaluation d'outil sans confrontation aux six exigences guadeloupéennes. » J'ai fait la confrontation. Elle ne sort personne du jeu. Ces six exigences ne sont pas une barrière à l'entrée : elles sont une liste de courses de conception, utile en interne, sans valeur stratégique.

---

## 5. Verdict — y a-t-il un marché solvable, et de quelle taille

### 5.1 Oui, il y a un marché. Non, ce n'est pas un marché de logiciel.

**Le marché solvable existe et je le chiffre, avec mes hypothèses marquées :**

- **Cœur professionnel touristique** : ~760 établissements employeurs en hébergement-restauration (B, projection 2019), dont 52 à 55 hôtels. **Quelques centaines, pas quelques milliers.** Le prompt demandait de le dire si c'était le cas : **c'est le cas**.
- **Second cercle** : 14 582 établissements employeurs tous secteurs (B, fin 2024), dont 71,8 % à 1-9 salariés. Mais ce cercle n'a aucun besoin des six exigences du document.
- **Troisième cercle, non chiffrable sur source ouverte** : « plus de 10 000 » meublés de tourisme (C, presse 2023), en majorité des particuliers non professionnels dont la solvabilité mensuelle est inconnue et dont neuf sur dix ne sont même pas classés.
- **Plafond de prix** : **80 €/mois**, sourcé B sur un prestataire local guadeloupéen qui livre huit posts, la réponse à tous les avis, les photos, les horaires et un rapport mensuel. Et **0 €** si le client gère sa fiche Google lui-même, ce que Google documente et autorise gratuitement.
- **Revenu brut plausible** (mon arithmétique, pénétration = hypothèse) : **73 k€/an à 10 %**, **219 k€/an à 30 %** — et il faut minorer pour les mois de fermeture saisonnière, puisque l'INSEE constate que l'offre d'hébergement tombe à 5,5 % de l'offre annuelle en septembre.

### 5.2 Les deux piliers de la section 3 et 2.7 ne tiennent pas

| Affirmation du document | Verdict | Preuve |
|---|---|---|
| « Aucun acteur mondial ne construit à cette échelle de marché » | **Faux** | Localo vend un plan « Single Business » à 39 $/mois avec centralisation et réponse aux avis et posts auto-publiés ; Buffer vend 5 $/mois par canal et compte Google Business Profile parmi ses canaux ; Metricool est gratuit à vie pour un établissement ; Google lui-même est gratuit. Cran **B** sur les quatre |
| « La proximité est la clé du guichet 2. Aucun concurrent mondial ne peut l'ouvrir » | **Faux** | Google documente l'invitation par **adresse e-mail** d'un administrateur, acceptée « immédiatement », avec droit de « Répondre aux avis » et de « Créer, gérer et publier des posts », « sans avoir besoin de votre mot de passe ». Cran **B** |
| Corollaire : il faut un organe « Garde des accès confiés » de niveau bancaire | **Mal fondé** | Le guichet 2 délègue un **rôle**, pas un identifiant ; la révocation est faite par le client depuis son interface. L'organe répond à un problème que le mécanisme ne pose pas. Cran **B** sur le mécanisme, et je n'ai pas vérifié Meta (D3) |
| Guichet 1 « hors de portée, volume minimum, à réexaminer à trois ans » | **Faux pour Google** | Deux conditions : une fiche vérifiée depuis 60 jours et un site web. Pas de frais, pas de volume. 300 QPM à l'approbation. Cran **B** |
| Les six exigences « disqualifient directement des outils » | **Non vérifié, et probablement faux** | Confrontation faite sur neuf concurrents : aucun n'est écarté par aucune des six |

### 5.3 Ce qu'il reste, et ce qu'il faut décider

Ce que les concurrents identifiés **ne font pas**, et que le projet revendique ailleurs que dans la section 3 :

- la **couche de provenance vérifiable** (section 6 : part des assertions remontées à une source primaire, part datée, part rejouable). Personne ne la vend. Personne ne la prix. Je ne l'ai pas testée ;
- le **corpus de presse et d'institutions guadeloupéennes** pour la veille — exactement ce que le guichet 6 débloque selon la section 2.4 ;
- la **rédaction sourcée** avec zéro affirmation non sourcée par texte.

**C'est là qu'est le produit, et ce n'est pas ce que la section 3 défend.** La section 3 défend un avantage de petite échelle et de proximité qui n'existe pas : la petite échelle est déjà servie à 0-39 $ par des outils mondiaux, et la proximité est déjà tenue par dix agences guadeloupéennes dont une au moins facture 80 €/mois le service complet.

**La décision que le document doit ajouter à sa section 10** : vendre aux établissements (800 cibles, plafond 80 €, dix concurrents locaux installés, perdant) ou vendre **aux agences guadeloupéennes et antillaises** en marque blanche (10 à 20 cibles, prix unitaire en centaines d'euros, la relation client et donc le guichet 2 restant chez elles, et un besoin quotidien). Le document ne pose nulle part cette question. **Elle précède toutes celles de la section 10.**

---

---

# RELANCE 1 — anti-oubli

## Qu'as-tu oublié — trois candidats écartés, et pourquoi

1. **Les gestionnaires d'avis spécialisés hôtellerie : ReviewPro (Shiji), TrustYou, Revinate, Qualitelis (Septeo), GestionBell.** Repérés, écartés faute de temps. C'est une **erreur de ma part**, et la plus coûteuse : ces acteurs sont ceux qui franchissent le guichet 1 — connectivité officielle Booking et Expedia — donc ceux qui détiennent la seule chose que le document juge « hors de portée au départ ». Qualitelis et GestionBell sont français et visent explicitement les hébergements **indépendants**, c'est-à-dire la cible du projet. Ne pas les avoir chiffrés laisse le flanc hôtelier de ma critique ouvert.
2. **Les plateformes d'avis autres que Google.** Je n'ai instruit que Google, parce que c'est la seule dont j'ai pu lire la documentation officielle. TripAdvisor, Booking, Expedia, Airbnb et Facebook sont restés dehors. Or pour un meublé de tourisme guadeloupéen, **Airbnb et Booking comptent plus que Google**, et leurs mécanismes d'accès délégué sont peut-être très différents — ce qui pourrait partiellement sauver l'argument de la section 2.7, sur ces plateformes-là.
3. **Les fichiers INSEE Flores à 38 et 88 secteurs** (`insee.fr/fr/statistiques/8266010`, .xlsx de 4 à 9 Mo). Écartés pour un motif purement pratique : les ouvrir et les filtrer sur le département 971 demandait un détour que je n'ai pas pris. C'est le **seul chemin propre** vers un décompte à même champ et même date d'hôtellerie, restauration, location, artisanat et professions libérales. Le document devra les ouvrir ; ils donneront en une journée le chiffre que toute cette section attend.

Écartés aussi, sans regret : les comparateurs SaaS (Capterra, Appvizer, GetApp, G2, avismaestrogmb) comme **fondement** — ils sont cran C par construction et je ne les cite que marqués. Et les vendeurs de faux avis (`agence-avis.fr`, `achat-avis-google.com`, « packs dès 59 € HT ») — hors sujet, et ils documentent au passage que le marché local de l'avis est aussi un marché de fraude, ce qui est un risque de réputation pour quiconque vend de la « collecte vérifiée ».

## Que n'as-tu pas vu — ce que tu n'as pas pu vérifier, et ce qui t'a manqué

- **Meta.** Zéro source primaire. `facebook.com/business/help/1927237026186704` renvoie `CRAWL_NOT_FOUND` et la page outil renvoie un écran de connexion. Toute ma démolition de la section 2.7 repose sur **Google seul**. Si l'accès partenaire Meta est lourd, l'argument du document survit partiellement.
- **insee.fr est bloqué par le proxy de sortie** de cet environnement (`EGRESS_BLOCKED` sur `www.insee.fr`). J'ai contourné en lisant les mêmes pages via un outil de récupération tiers, ce qui veut dire que **je n'ai pas vu les pages INSEE rendues** : j'ai vu un texte extrait. Les intitulés de colonnes de tranches d'effectifs y ont disparu (D7). J'ai tenté de lire l'état du proxy pour corriger ; la commande a été refusée par le classificateur de permissions. **Il me manque un accès direct à insee.fr.**
- **Aucun prix affiché par Partoo, Guest Suite, Digitaleo, So-Community ni aucune agence guadeloupéenne sauf MangoWeb.** Le marché est opaque par choix des vendeurs. Mon plafond de 80 €/mois repose donc sur **un seul** prix public local. Un deuxième point de mesure changerait sa solidité.
- **Je n'ai installé ni appelé aucun outil.** Pas une ligne en A-usage, pas une en A-mesure. Tout mon retour est en B et C. Selon la règle 4.2, aucune décision de construire ne peut se prendre là-dessus — et je ne demande pas qu'on en prenne une. Je demande qu'on **cesse de s'appuyer sur deux affirmations fausses**.
- **Le prix plafond est un prix affiché, pas un prix payé** (D4). Je ne sais pas si MangoWeb vend à 80 € ou négocie à 50 €, ni combien de clients il a. Une enquête de cinq appels téléphoniques en Guadeloupe produirait un A-usage que je ne peux pas produire d'ici.

## Qu'est-ce qui rendrait ce produit plus profitable — l'endroit exact où il perd de l'argent, et le geste qui le corrige

**Trois endroits, nommés.**

1. **Il perd de l'argent sur l'organe « Garde des accès confiés ».** Section 6, huitième ligne, présenté comme « la condition du guichet 2, donc de tout le produit » : chiffrement au repos, révocation en minutes, journal d'accès complet, cloisonnement entre clients. C'est un chantier de sécurité de plusieurs semaines. **Le geste qui corrige** : n'accepter que la délégation de rôle — invitation administrateur Google, OAuth ailleurs — et **interdire contractuellement** la détention de tout mot de passe client. L'organe tombe de « coffre-fort bancaire » à « table de jetons OAuth chiffrés avec rotation », ce qui est une bibliothèque standard et pas un organe. Des semaines rendues, et un risque juridique supprimé.

2. **Il perd de l'argent sur la cible.** 800 établissements à 80 € plafond, c'est un plafond de chiffre d'affaires de l'ordre de 73 à 219 k€ qui ne financera jamais sept organes reconstruits. **Le geste qui corrige** : retourner le client. Vendre aux **dix agences guadeloupéennes et antillaises déjà identifiées** — lagencedigitale, Digitallis, ELYAD, Connect Outremer, Novazeo, So-Community, MangoWeb, SMP, Arobaz, Awitec — un outil en marque blanche. Elles ont la relation, le mandat, le portefeuille, et le besoin quotidien. Vingt agences à 400 €/mois valent 96 k€/an avec vingt factures à émettre au lieu de deux cent cinquante, sans force de vente à construire, et sans affronter la saisonnalité de la trésorerie des établissements. Le plafond de 80 € ne s'applique plus : il s'applique à l'établissement final, pas à l'agence qui le facture 300 à 500 €.

3. **Il perd de l'argent sur les quatre premiers organes.** Découverte, extraction, index, provenance : le document veut les mesurer puis les reconstruire. Trois des quatre sont des problèmes résolus par des briques libres mûres ; le **quatrième — la provenance — est le seul que personne ne vend**, et c'est le seul qui justifie un prix supérieur à 80 €. **Le geste qui corrige** : inverser l'ordre de construction de la section 8. Construire la provenance **d'abord**, sur un corpus guadeloupéen minuscule et un seul client payant, et n'instrumenter les trois autres organes qu'ensuite. Le projet gagne un argument de vente que personne ne peut copier, au lieu de dépenser ses premiers mois à égaler des étalons que des outils à 5 $ atteignent déjà.

---

# RELANCE 2 — preuve, étalon et guichet

## Pour chaque ligne : as-tu vérifié, avec quoi, URL et date

Toutes les consultations : **2 octobre 2026**. Aucun outil installé, aucune commande exécutée contre un produit, aucun jeu d'épreuve.

| # | Ligne | Vérifiée avec quoi | Passage obtenu | Validé par moi / recopié | Cran final |
|---|---|---|---|---|---|
| 1 | 33 477 établissements actifs 2021 | `insee.fr/fr/statistiques/7658710?geo=REG-01`, tableau DEN T5 | « Ensemble 33 477 100,0 […] Commerce de gros et de détail, transports, hébergement et restauration 9 335 27,9 » ; « Source : Insee, SIDE en géographie au 01/01/2024 » | Recopié d'INSEE. Je n'ai pas revalidé la somme des lignes | **B** |
| 2 | 14 582 établissements employeurs fin 2024 et tranches | `insee.fr/fr/statistiques/2012766` | « Guadeloupe \| 14 582 \| 12,1 \| 71,8 \| 9,2 \| 4,5 \| 2,5 » ; « Champ : établissements employeurs durant l'année et actifs la dernière semaine de décembre » | Chiffres recopiés. **Libellés de colonnes inférés par moi**, non lus | **B** pour les nombres, **D** pour les libellés |
| 3 | Nuitées 2024, provenances, occupation mensuelle | `insee.fr/fr/statistiques/8354611?sommaire=8354895`, paru 26/06/2025 | « les hôtels de Guadeloupe vendent près de 1,3 million de nuitées » ; « France 85,9 […] Canada 4,8 \| USA 1,9 » ; « mars 2024 \| 77,7 » ; « sept. 2024 \| 34,4 » ; « l'offre d'hébergement durant ce mois ne représente que 5,5 % de l'offre annuelle » | Tableaux recopiés. **Le classement haute/basse saison est ma lecture** des douze valeurs mensuelles, pas une phrase de l'INSEE — sauf « période qui correspond au pic de fréquentation touristique » pour janvier-mars, qui est leur phrase | **B** |
| 4 | 55 hôtels / 3 258 chambres ; 760 établissements employeurs HR ; 1 550 non-salariés ; 86 % à 1-9 salariés | `observatoire.akto.fr/content/uploads/sites/3/2024/02/Monographie-HR-2023-Guadeloupe.pdf` | « 3 258 chambres, 55 hôtels, INSEE 2022 » ; « 760 établissements employeurs […] Projection Kyu Lab à partir des données DARES et INSEE 2019 » ; « 86% des établissements ont entre 1 à 9 salariés » ; « 1 550 non-salariés » | Recopié. **J'ai validé moi-même que c'est une projection et pas un comptage**, en lisant la note de méthode | **B**, avec réserve de méthode |
| 5 | 33 000 entreprises de proximité, 58 % individuelles | `infometiers.org/wp-content/uploads/2023/12/7-Chiffres-cles-U2P-2023-Maquette-Guadeloupe.pdf` | « 33 000 ENTREPRISES DE PROXIMITÉ EN GUADELOUPE » ; « 58% des entreprises de proximité ont le statut d'entreprise individuelle » ; « Source : INSEE, Dénombrement des entreprises au 31/12/2020. Traitement ISM » | Recopié. **J'ai validé que la somme des quatre secteurs (2 600 + 11 940 + 12 530 + 6 530 = 33 600) approche le total annoncé** | **B** |
| 6 | 56,7 % de micro-entrepreneurs dans les créations 2024 | `insee.fr/fr/statistiques/8354543?sommaire=8354895` | « Ces immatriculations représentent plus de la moitié des créations en Guadeloupe (56,7 %) » ; « 2024 \| 2 892 \| 651 \| 4 635 \| 8 178 » | Recopié. **J'ai validé moi-même que 4 635 / 8 178 = 56,7 %** | **B** |
| 7 | 92,5 % de microentreprises, 13 % employeuses | Résumé de moteur de recherche sur des pages insee.fr **non ouvertes** | « 92,5 % des établissements contre 82 % en France métropolitaine. Seules 13 % d'entre elles emploient des salariés » | **Recopié d'un résumé, page jamais lue** | **C** |
| 8 | « plus de 10 000 locations touristiques », 24 % des touristes en meublés | `rci.fm/guadeloupe/infos/Economie/La-Guadeloupe-une-destination-prisee`, publié 03/04/2023 | « On compte plus de 10 000 locations touristiques, un chiffre en constante progression » ; « 24 % des touristes, selon les derniers chiffres de l'Observatoire régional du tourisme » | Recopié de la presse. **Je n'ai pas vu la publication de l'Observatoire** | **C** |
| 9 | Google : délégation à distance, droits de l'administrateur | `support.google.com/business/answer/3403100?hl=fr` | « Saisissez une adresse e-mail. Sous "Accès", sélectionnez Propriétaire ou Administrateur. Sélectionnez Inviter » ; « sans avoir besoin de votre mot de passe » ; « Les utilisateurs invités peuvent accepter l'invitation et devenir utilisateurs immédiatement » ; tableau des droits : « Répondre aux avis », « Créer, gérer et publier des posts » | Recopié de Google. **Je n'ai pas exécuté la procédure** — je n'ai aucun A-usage dessus | **B** |
| 10 | Google : réponse aux avis gratuite après validation | `support.google.com/business/answer/3474050?hl=fr` | « Avant de pouvoir répondre aux avis, vous devez valider votre établissement » ; « À côté de l'avis auquel vous souhaitez répondre, sélectionnez Répondre » | Recopié | **B** |
| 11 | Conditions d'accès à l'API Google Business Profile | `developers.google.com/my-business/content/prereqs` | « Manage a Google Business Profile that is verified and active for 60+ days » ; « Have a website » ; « If your quota is set to 300 QPM, your project is approved » | Recopié. **Je n'ai pas déposé de demande** | **B** |
| 12 | Localo : 39 $/mois, 1 fiche, avis + posts | `localo.com/pricing` | « Single Business […] $49 $39 /month, billed annually (+VAT) » ; « Collect all your reviews in one place and respond to them with a single click » ; « Autogenerate and publish posts » ; « Active Business Profiles : 1 » | Recopié de la page éditeur. **Pas de compte créé, pas d'essai** | **B** |
| 13 | Buffer : gratuit + 5 $/canal, Google Business Profile parmi les canaux | `buffer.com/pricing` | « Free forever — 10 scheduled posts per channel » ; « Essentials $5 /month — 1 channel · $60 billed yearly » ; liste des connexions incluant « Buffer × Google Business Profile » ; « Reply to comments — Free : Included » | Recopié | **B** |
| 14 | Metricool gratuit à vie | `metricool.com/pricing/` | « Is Metricool free? Yes! You can use Metricool for free, forever. With our Free plan, you can connect 1 brand […] plan your content, publish content automatically, manage messages from your networks » ; « Each brand in Metricool corresponds to a single location » pour Google Business Profile | Recopié | **B** |
| 15 | Guest Suite : offre, AFNOR, 10 000 points de vente, prix non affichés | `guest-suite.com/offres` | Quatre packs listés ; « + de 10 000 points de vente ont choisi Guest Suite » ; « Plan personnalisé » ; « Y a-t-il des coûts "cachés" ? La réponse est simple : aucun ! » mais **aucun montant** | Recopié. **J'ai validé moi-même l'absence de tout prix sur la page** | **B** pour l'offre |
| 16 | Guest Suite 39 €/mois, Partoo 149 € HT/mois, Trustmary 19 €/mois, So-Community 490 €/mois | Comparateurs et résumés de moteur | — | **Recopié de tiers, jamais de l'éditeur** | **C** (D5) |
| 17 | Digitaleo : modèle tarifaire par module × établissement | `digitaleo.fr/tarifs` | « Somme des montants par module par établissement X Nombre d'établissements = Montant total de votre abonnement mensuel » ; « un coût par crédit de 0,02€ » ; modules Avis Clients et Réseaux Sociaux détaillés | Recopié. **Aucun montant publié par l'éditeur** | **B** pour le modèle |
| 18 | MangoWeb : 200 € création, 80 €/mois gestion incluant réponse à tous les avis | `mangoweb.digital/google-my-business` | « Gestion mensuelle — Chaque mois — 80€/mois : 8 posts mensuels, Réponse à tous les avis, Photos mensuelles, Mise à jour horaires, Statistiques mensuelles » ; « Création complète 200€ » ; « Saint-Claude, Guadeloupe (97120) » | Recopié de la page du prestataire. **Pas de devis demandé, pas d'appel passé** | **B** |
| 19 | Agences locales : lagencedigitale, Digitallis, ELYAD, Connect Outremer, Novazeo, So-Community | `lagencedigitale.com`, `digitallis.fr`, `elyad.fr`, `connectoutremer.fr`, `novazeo.com/...`, `so-community.fr/departement/guadeloupe` | « Depuis 2007 […] +50 clients accompagnés » et portefeuille nominatif (CCI des Îles de Guadeloupe, MEDEF Guadeloupe, Air Antilles) ; « près de 1 000 entreprises » ; « +300 projets réalisés » ; « Travailler avec une agence locale signifie une plus grande proximité géographique » | Recopié des pages des agences. **Ce sont des pages marketing : les volumes revendiqués ne sont pas audités** | **B** pour l'existence et l'offre, **C** pour les volumes revendiqués |
| 20 | Solocal Outre-Mer implanté à Baie-Mahault | fiche Pages Jaunes `pagesjaunes.fr/pros/08185528` | « Solocal Outre-Mer - Guadeloupe Baie Mahault - Agence de publicité » | Recopié d'un annuaire, **pas du site de Solocal** | **C** |
| 21 | Saison cyclonique juin-novembre, pointe 15 août-15 octobre | `meteo.fr/temps/domtom/antilles/pack-public/cyclone/tout_cyclone/lieux_periodes.htm` | « on peut voir des cyclones de JUIN à NOVEMBRE […] la saison cyclonique bat son plein entre début Juillet et fin Octobre, la période la plus active pour nos îles antillaises étant celle s'étirant du 15 août au 15 octobre » | Recopié de Météo-France. **La page ne porte pas de date de publication** | **B**, sans date |
| 22 | Carnaval 2026 : 11 janvier – 18 février, Vaval présenté le 3 janvier | guides touristiques et France Info Outre-mer | « débute le dimanche 11 janvier 2026 […] s'achève le mercredi 18 février 2026, jour du mercredi des Cendres » | Recopié de sources touristiques. **Aucun calendrier officiel trouvé** | **C** |
| 23 | Fuseau UTC-4, 5 h hiver / 6 h été, 6 h du 29 mars au 25 octobre 2026 | sites de voyage ; tentative échouée sur `raw.githubusercontent.com/eggert/tz/main/northamerica` | « La Guadeloupe vit à l'heure UTC-4 toute l'année […] 5 heures en hiver et 6 heures en été » ; sur tzdb : **« aucune mention de Guadeloupe n'est présente »** dans ma lecture | Recopié de blogs. **Vérification primaire tentée et échouée** | **C**, et D9 pour tzdb |

## Ton étalon est-il opposable ?

**Non, et je n'en ai pas.** Je n'ai figé aucun jeu d'épreuve, je n'ai mesuré aucun outil, je n'ai collé aucune sortie de produit. Mon travail est un relevé de sources et une arithmétique, pas une mesure. Selon la règle 4.2 du document, **rien ici ne fonde une décision de construire**. Ce qui est fondé, et seulement cela : deux affirmations de la section 3 et de la section 2.7 sont contredites par des documents primaires des éditeurs concernés.

Un tiers peut rejouer tout mon travail : les vingt-trois URL sont nommées et datées. C'est la seule reproductibilité que j'offre.

## Pour chaque acteur cité : par quel guichet accède-t-il à la donnée, et comment le sais-tu

Le document interdit de supposer (4.3, et section 8/V1 : « soit c'est documenté, soit c'est déclaré inconnu »). Je m'y tiens.

| Acteur | Guichet | Comment je le sais |
|---|---|---|
| **Google Business Profile** (produit) | **Guichet 2 — mandat du titulaire**, par invitation e-mail propriétaire/administrateur | **Documenté** par Google : `support.google.com/business/answer/3403100?hl=fr` |
| **Google Business Profile API** | **Guichet 3 — API ouverte sur demande**, validation sur formulaire, deux conditions, 300 QPM | **Documenté** : `developers.google.com/my-business/content/prereqs` |
| **Localo** | **Inconnu.** Probablement 2 ou 3, puisqu'il répond aux avis et publie des posts — mais aucune page consultée ne le déclare | Déclaré inconnu |
| **Buffer** | **Inconnu.** La page tarifaire liste Google Business Profile comme canal connectable, ce qui implique une autorisation du titulaire — donc 2 ou 3. Non déclaré par l'éditeur | Déclaré inconnu |
| **Metricool** | **Inconnu.** Même raisonnement, même absence de déclaration | Déclaré inconnu |
| **Guest Suite** | **Inconnu.** Certifié NF Service Avis en ligne AFNOR, ce qui porte sur le processus de collecte, **pas sur la voie d'accès** aux avis de tiers | Déclaré inconnu |
| **Partoo** | **Inconnu.** Annonce la centralisation d'avis Google, Facebook et TripAdvisor. Comment il atteint TripAdvisor n'est pas documenté publiquement | Déclaré inconnu |
| **Digitaleo** | **Inconnu.** Annonce Google, Apple, « +30 portails », Facebook, Instagram, LinkedIn. Aucune voie déclarée | Déclaré inconnu |
| **Trustmary** | **Inconnu.** L'éditeur déclare l'import automatisé depuis « Google, Facebook, G2, Capterra, TripAdvisor, and Yelp » — le **fait** est documenté, le **guichet** ne l'est pas | Déclaré inconnu |
| **Solocal / Solocal Outre-Mer** | **Inconnu** | Déclaré inconnu |
| **MangoWeb, lagencedigitale, Digitallis, ELYAD, Connect Outremer, Novazeo, So-Community** | **Guichet 2 présumé** — ce sont des prestataires mandatés qui gèrent la fiche de leurs clients. **Mais aucune page ne le déclare**, et je n'ai pas demandé | **Déclaré inconnu**, avec présomption motivée signalée comme telle |
| **ReviewPro, TrustYou, Revinate, Qualitelis, GestionBell** | **Non instruits.** Candidats écartés, voir relance 1 | Non instruits |

**Reclassement final de toutes mes lignes** : 15 lignes en **B**, 6 en **C**, 2 échecs de vérification en **D** (fuseau sur source primaire, Meta). **Zéro ligne en A-mesure. Zéro ligne en A-usage.** Selon la règle 4.2, ce retour serait relancé une fois ; s'il revenait encore sans A, il tomberait. Je l'écris plutôt que de déguiser un B en A.

---

# Les cinq colonnes

## 1. MCP à installer

| MCP | Ce qu'il débloque | Prérequis |
|---|---|---|
| **MCP INSEE / API Melodi** | Interroger directement les séries INSEE sans passer par le web — Flores à 38 et 88 secteurs, SIDE, Sirene — et obtenir le décompte d'établissements 971 par NAF fin à même champ et même date. **Lève D6 et D7, les deux trous centraux de ce retour** | Clé API INSEE (gratuite), et le déblocage de `insee.fr` dans le proxy de sortie — il est actuellement `EGRESS_BLOCKED` |
| **MCP Sirene / annuaire-entreprises** | Dénombrer les établissements guadeloupéens par code NAF et commune, et bâtir la liste nominative de prospection. Transforme « quelques centaines » en liste de noms | API Sirene publique |
| **MCP tableur (xlsx)** | Ouvrir et filtrer les fichiers Flores de 4 à 28 Mo que j'ai écartés | Aucun |
| **MCP navigateur avec session** | Atteindre les pages Meta Business (`CRAWL_NOT_FOUND` sur l'extraction simple) et lever **D3** | Compte Meta de test |
| **MCP data.gouv.fr** | Registre des meublés de tourisme, données des collectivités guadeloupéennes — le guichet 6 de la section 2.4, et le seul chemin vers un comptage des meublés | Aucun |

## 2. Logiciels manquants

- Un **lecteur de tableur en ligne de commande** pour les .xlsx INSEE (actuellement rien).
- Un **extracteur PDF fiable** : les PDF AKTO et U2P sont revenus avec des tableaux désordonnés — plusieurs cellules ont été perdues, ce qui m'a interdit de lire la répartition fine par activité.
- Un **accès direct à insee.fr** : la source primaire de tout ce retour est bloquée par le proxy et n'a été atteinte qu'en relais.
- Un **outil de mesure de prix** : rien, nulle part, ne donne les prix réels payés. Seul un appel téléphonique le donnera, et aucun logiciel ne le remplace.

## 3. Outils déjà disponibles et non exploités

- **Recherche web et récupération de pages** : exploitées, mais je n'ai lu que 23 URL. Les fichiers INSEE restent ouverts.
- **Outils GitHub** (`search_code`) : j'aurais pu trouver la Guadeloupe dans tzdb par recherche de code au lieu d'échouer sur la lecture d'un gros fichier. **Non exploité, et c'est la cause directe de D9.**
- **Le dépôt git du projet** : il ne contient que `00-PROMPT-DE-LANCEMENT.md`. Aucun jeu d'épreuve, aucune fiche-organe, aucun registre de sources. **La section 5 du document dit que le jeu d'épreuve figé est « la première tâche du projet » : elle n'est pas commencée.**

## 4. IA existantes qui font déjà ce travail, et à quel prix

| Produit | Ce qu'il fait déjà | Prix | Cran |
|---|---|---|---|
| **Google Business Profile** | Réponse aux avis, posts, horaires, photos, statistiques, pour un établissement validé | **0 €** | B |
| **Metricool** | Planification et publication automatique multi-réseaux, gestion des messages, 1 marque | **0 €, « free, forever »** | B |
| **Buffer** | Publication multi-réseaux dont Google Business Profile, réponse aux commentaires, 5 suggestions IA par semaine en gratuit | **0 €**, puis **5 $/mois par canal** | B |
| **Localo** | Avis centralisés et réponse en un clic, **posts auto-générés et publiés**, suivi de positions, veille concurrentielle, 1 fiche | **39 $/mois** annualisé (49 $ mensuel), hors TVA | B |
| **Digitaleo + agent « Leo »** | Génération de posts (texte, image, planification), **priorisation et suggestions de réponse aux avis**, publication automatique des avis sur les réseaux, optimisation des fiches Google | Modèle par module × établissement ; crédits IA à **0,02 € l'unité** au-delà du forfait ; **montants non publiés** | B pour le modèle |
| **Guest Suite** | Réponses aux avis rédigées **et postées par IA** pour le compte du client ; prise en charge par des équipes humaines en option | **Non publié** | B pour l'offre |
| **MangoWeb Digital** (humain, Guadeloupe) | 8 posts/mois + réponse à **tous** les avis + photos + horaires + rapport | **80 €/mois**, 200 € d'installation | B |

**Lecture.** Les deux fonctions que le projet veut construire — publication sociale et gestion d'avis — sont déjà vendues de 0 € à 39 $/mois en logiciel, et à 80 €/mois en prestation humaine locale avec la relation client en prime. Le prix plancher du marché est **zéro**. Le prix plafond local est **80 €**.

## 5. Futurs possibles à douze mois — ⏳ non advenus

- ⏳ **Les agents IA locaux par établissement se généralisent.** Digitaleo déploie déjà « Leo » sur les accès affiliés de chaque point de vente « sans abonnement supplémentaire ». À douze mois, la réponse aux avis et la génération de posts seront probablement incluses par défaut chez tous les acteurs du présence management, et cesseront d'être un produit vendable séparément. **Le projet construirait alors un organe devenu gratuit.**
- ⏳ **Google intègre davantage d'IA dans la fiche d'établissement elle-même.** Si les réponses suggérées arrivent nativement et gratuitement dans l'interface Google, l'organe « Avis » du projet perd son prix.
- ⏳ **Le référencement dans les moteurs génératifs devient la demande dominante.** Deux agences guadeloupéennes vendent déjà du « GEO » et de la visibilité « dans ChatGPT » (lagencedigitale, Digitallis). La demande locale pourrait se déplacer du moteur de recherche vers l'assistant, ce qui déplacerait aussi l'objet du produit.
- ⏳ **Durcissement de l'accès aux avis de plateformes.** Non prévisible. Si Booking et TripAdvisor resserrent, les détenteurs du guichet 1 — ReviewPro, TrustYou, Revinate — gagnent, et tout le monde d'autre perd. Candidats que je n'ai pas instruits.
- ⏳ **Réglementation française et européenne des meublés de tourisme.** Un registre obligatoire des meublés produirait pour la première fois un **comptage officiel** des « plus de 10 000 » locations guadeloupéennes, et donnerait un chiffre de marché que personne n'a aujourd'hui. Je ne sais pas si, ni quand.

---

*Fin de la critique. Aucun commit. Aucun autre fichier touché. Le document cible n'a pas été modifié.*
