# Relance juridique — faisabilité guichet 3, spécifications, test de l'hypothèse, dossier juriste

Suite de `critiques/01-juridique.md`. **Version 2 du 2 octobre 2026**, après la décision de périmètre
de Laurent Cieutat : le périmètre est tenu en entier, le volet avis se fait sous les cinq conditions
cumulatives, la publication automatique se fait sous responsabilité éditoriale.

**Ce qui est ajouté en version 2** — §§ 8 à 11, et c'est là que se trouve le cœur de ce retour :
— **§ 8** — le test de non-conformité sur les quatre produits réellement en place, traité en priorité.
  Il contient une **correction factuelle de la prémisse du coordinateur** : l'agence à 80 €/mois
  n'existe pas sur ce marché, et ce que j'ai trouvé à la place est une meilleure nouvelle.
— **§ 9** — les spécifications étendues aux quatre outils : publication, blog, veille.
— **§ 10** — le coût et le calendrier de la conformité avant le premier euro de revenu, avec **un
  tarif de licence de veille réel, en euros, obtenu sur contrat**.
— **§ 11** — ce que tout cela fait à la stratégie.

Les §§ 0 à 7 sont inchangés et restent valables.
Date de toutes les consultations : **2 octobre 2026**. Aucune référence non datée.

**Rappel d'outillage, inchangé.** `legifrance.gouv.fr`, `curia.europa.eu`, `bailii.org`,
`eur-lex.europa.eu` et `tripadvisor.com` restent bloqués en sortie directe. EUR-Lex et les portails
développeurs ont été atteints par la récupération côté serveur du MCP EXA. La convention **B-miroir**
est conservée : texte normatif lu, mais pas sur sa source officielle.

---

## 0. Mes lignes en cran D — déclarées avant le contenu

Quatre lignes neuves. Les sept lignes D du premier fichier restent valables et ne sont pas répétées.

| # | Affirmation | Pourquoi D |
|---|---|---|
| **D8** | Airbnb permet, via son API partenaire, de **publier** une réponse d'hôte à un avis. | La page de description de l'API dit « Operations for retrieving **and responding to** guest and host reviews », mais le schéma que j'ai lu n'expose que **deux opérations GET**, aucune mutation. Le verbe « responding » n'est corroboré par aucun endpoint d'écriture que j'aie vu. **Lecture : oui. Écriture : non établie.** |
| **D9** | Les avis / recommandations de Pages Facebook sont en voie de fermeture pour les tiers. | La page de référence du nœud `Recommendation` porte « This field is deprecated for v22.0 and future versions », mais la phrase est attachée à un champ et je n'ai pas pu établir si elle vise `open_graph_story` seul ou l'arête `/ratings` entière. Signal, pas conclusion. |
| **D10** | Une réponse à un avis client n'est pas un « texte publié dans le but d'informer le public sur des questions d'intérêt public » au sens de l'art. 50(4) al. 2 du règlement IA. | Mon interprétation. Aucune ligne directrice lue sur ce point précis. **Elle me conduit à corriger mon premier fichier** — voir § 5.1. |
| **D11** | Le prix mensuel réel de Partoo et de Guest Suite. | Leurs pages « tarifs » ne publient aucun chiffre atteignable ; Guest Suite annonce des « tarifs dégressifs » sans grille. **Non vérifié. Je ne les range donc pas d'office dans la tranche 0-80 €.** Le seul prix public obtenu est celui de Meditrust. |

**Quatre lignes D ajoutées en version 2 :**

| # | Affirmation | Pourquoi D |
|---|---|---|
| **D12** | Le tarif de la licence CFC Veille Web que je cite au § 10 (105 € + 52,50 € HT par trimestre et par client) est le tarif qui nous serait appliqué. | Le contrat d'où viennent ces chiffres est un contrat CFC réel, publié sur un agrégateur de contrats, **mais c'est le contrat d'un autre cocontractant**, non daté, et l'article 4.1.1 précise que le montant résulte d'« une remise sur la redevance fixée initialement à 200 €HT par trimestre ». Le ratio droit voisin / droit d'auteur de 50 % est, lui, **confirmé par le CFC lui-même** et passe en B. **Le montant de base est donc un ordre de grandeur négocié, pas un tarif public.** |
| **D13** | Le coût d'un avis juridique sur les 21 points du § 4. | Je n'ai relevé aucun tarif d'avocat sur source primaire dans cette session. Tout chiffre que je donnerais serait de mémoire. **Je le traite au § 10.4 en unités de travail, pas en euros.** |
| **D14** | Le temps réel d'obtention des accès plateforme chez Booking, Expedia et Airbnb. | Aucun délai publié. Les seuls délais chiffrés que je tienne sont celui annoncé par Google (7-10 jours ouvrés) et celui constaté par les développeurs du forum (dépassé, sans réponse). Pour Airbnb je n'ai qu'une estimation de tiers, « weeks to months » (cran C). |
| **D15** | Que les outils de publication examinés au § 8 ne marquent pas les contenus générés par IA. | J'ai lu leurs pages de tarifs et de fonctionnalités, qui annoncent un assistant IA sans jamais mentionner de marquage. **L'absence de mention sur une page commerciale n'est pas la preuve d'une absence de marquage.** C'est un soupçon fondé, testable pour 6 $, et le test est au § 10.6. |

---

## 1. TRAVAIL 1 — Faisabilité plateforme par plateforme, en guichet 3

### 1.1 Le tableau de verdict

Trois questions par plateforme : (Q1) existe-t-il un accès délégué permettant à un tiers d'agir pour
le compte de l'établissement **sans détenir ses identifiants** ; (Q2) cet accès permet-il de **lire**
les avis, d'y **répondre**, ou l'un seulement ; (Q3) conditions d'obtention.

| Plateforme | Q1 — accès délégué sans identifiants | Q2 — lire / répondre | Q3 — conditions | Guichet réel | Cran |
|---|---|---|---|---|---|
| **Google Business Profile** | **Oui.** OAuth 2.0, scope `business.manage`, accès *gestionnaire* accordé par le commerçant, révocable par lui. | **Les deux.** `accounts.locations.reviews.list` (lire), `reviews.updateReply` en PUT (répondre), `reviews.deleteReply`. | Projet Google Cloud + demande de *Basic API Access* + vérification de marque OAuth. **Et un obstacle décisif, voir § 1.2.** | **3**, en théorie | **B** (endpoints) |
| **Booking.com** | **Non.** L'authentification de la Guest Review API est un **compte machine** du partenaire (JWT), les propriétés étant rattachées via le Provider Portal. Pas de jeton par établissement. | **Les deux.** `GET /review-api/properties/{id}/reviews`, `GET .../reviews/{review_id}`, `POST .../reviews/{review_id}` avec `{"reply": "…"}`. | Être **Connectivity Partner** sous accord de partenariat de connectivité avec Booking.com, et que le compte machine ait la permission `review-api`. | **1** | **B** |
| **TripAdvisor** | **Non.** Clé partenaire au niveau du partenaire, aucune délégation par établissement. | **Lecture seule, et plafonnée.** « The Location Reviews request returns **up to 5 of the most recent reviews** ». La réponse d'exploitant est **lue** si elle existe. **Aucun endpoint de réponse n'existe.** Répondre se fait à la main dans le Management Center. | Accord de licence négocié : « Access to review content is **dependent on the terms of use agreement between Tripadvisor and each individual partner**. You may not have access to all calls, fields, and functionality. » | **1** pour la lecture ; **aucun** pour la réponse | **B** |
| **Airbnb** | **Oui.** OAuth 2.0 *authorization code*, un hôte = une autorisation, scopes dont `reviews:read`. | **Lecture : oui** (`/listings/{id}/reviews`, `/reservations/{id}/reviews`). **Réponse : non établie** — voir **D8**. | Agrément de l'entreprise comme partenaire logiciel : NDA mutuel, acceptation des API Terms, *Partner Specific Terms*, **revue de sécurité des données** réussie, et « implementing all mandatory API features **within 6 months of their release** ». Compte de démonstration à fournir à la demande. | **1 pour l'agrément, puis 3 par hôte** | **B** (conditions) / **C** (schéma) |
| **Facebook / Meta** | **Oui.** Jeton de Page obtenu via Facebook Login for Business, demandé par une personne ayant la tâche `CREATE_CONTENT`, `MANAGE` ou `MODERATE` sur la Page. | **Lecture : oui** — `GET /{page-id}/ratings` avec `pages_read_user_content`. **Réponse : indirecte seulement** — pas de champ « réponse » sur une recommandation ; on commente, via `pages_manage_engagement`. | **App Review** obligatoire, **vérification d'entreprise** obligatoire pour l'accès au contenu public de Page, captation vidéo du parcours à fournir. **Et le signal de dépréciation D9.** | **3**, sous revue d'application | **B** |
| **Expedia (hôtel, côté offre)** | **Non.** Identifiants de partenaire de connectivité, par marque. « Vrbo reviews are only accessible when authenticating with Vrbo credentials ». | **Les deux.** Lodging Supply GraphQL : requête `reviews`, requête `aggregatedReviews`, **mutation `setReviewResponse`**, plus webhooks `GuestReviewSubmitted`, `ReviewsApproved`, `ReviewsManagementResponseApproved`, `ReviewsManagementResponseRejected`. | Être partenaire de connectivité Expedia. Contraintes : seuls les avis **approuvés** sont retournés, modération jusqu'à 14 jours ; `isEligibleForResponse: false` si une réponse approuvée existe, si une réponse est en modération, **ou si l'avis a été importé par le partenaire de connectivité** ; 100 avis par page ; pas de requête inter-marques. | **1** | **B** |
| **Expedia (côté demande, pour affichage)** | Sans objet — c'est une licence d'affichage, pas une délégation. | **Lecture seule**, jusqu'à 100 avis, avec **mois et année du séjour**. Cache 48 h maximum. | Compte configuré pour l'accès **et** respect des *launch requirements*, via un Account Manager. | **4** (licence de contenu) | **B** |
| **Yelp, Trustpilot, PagesJaunes/Solocal, Agoda** | **Non vérifié.** | — | — | **inconnu** | **non vérifié** |

Sources, toutes consultées le 2 octobre 2026 :
Google — `developers.google.com/my-business/content/implement-oauth`, `/content/oauth-setup`,
`/content/review-data`, `/reference/rest/v4/accounts.locations.reviews/list`, `/updateReply`.
Booking — `developers.booking.com/connectivity/docs/review-api`, `/review-api/retrieve-reviews`,
`/review-api/review-api-self-assessment-tutorial`, `/review-api/reviews-troubleshooting`.
TripAdvisor — `developer-tripadvisor.com/partner/json-api/get-started/`,
`tripadvisor-content-api.readme.io/reference/getlocationreviews`, `/review-implementation-policy`,
`/display-requirements`, `docs.terra.tripadvisor.com/docs/review-implementation-policy`.
Airbnb — `airbnb.com/help/article/3418` (API Terms), `developer.withairbnb.com`.
Meta — `developers.facebook.com/docs/graph-api/reference/page/ratings/`, `/reference/recommendation/`,
`/docs/pages-api/manage-pages/`, `/docs/permissions/`, `/docs/features-reference/page-public-content-access/`.
Expedia — `connectivityportal.expediagroup.com/documentation/expedia/property_mgmt_apis/reviews/intro`,
`developers.expediagroup.com/rapid/lodging/content/guest-reviews`, `/rapid/lodging/reference/verified-guest-reviews`.

### 1.2 Le fait qui change le verdict Google — et qui corrige mon premier fichier

Dans `01-juridique.md` j'ai écrit que Google était « ouvert dès maintenant au prix d'un onboarding par
client ». **C'est à nuancer fortement, et la nuance est opérationnellement décisive.**

Tous les endpoints d'avis — `reviews.list`, `reviews.updateReply`, `reviews.deleteReply` — vivent
exclusivement sur l'API **legacy v4, `mybusiness.googleapis.com`**. Les trois API modernes
(`mybusinessaccountmanagement`, `mybusinessbusinessinformation`, `businessprofileperformance`) **ne
contiennent aucun endpoint d'avis**. Cela se vérifie sur la documentation de référence elle-même :
les méthodes `accounts.locations.reviews.*` sont servies depuis `https://mybusiness.googleapis.com/v4/`
(**cran B**).

Or, sur le forum développeurs de Google lui-même
(`discuss.google.dev/t/business-profile-api-reviews-endpoint-mybusiness-googleapis-com-cant-be-enabled-basic-access-pending-10-business-days/389462`,
fil du **12 août 2026**, consulté le 2 octobre 2026 — **cran C**, ce sont des déclarations de tiers),
trois développeurs distincts, chacun avec un identifiant de dossier Google, rapportent la même chose.
Verbatim :

> « `mybusiness.googleapis.com` (v4, reviews) — **CANNOT be enabled at all.** Running
> `gcloud services enable mybusiness.googleapis.com` returns PERMISSION_DENIED / "Service
> mybusiness.googleapis.com is not available to this consumer." »

> « I was approved for Basic API Access […] the legacy Google My Business API (v4) — **the only one
> with the reviews endpoint** […] — is completely inaccessible: It does not appear in the API Library
> […] A live call to the v4 reviews endpoint → 403 SERVICE_DISABLED. »

> « **Basic API Access approval does not unlock the legacy v4 reviews endpoint.** […] this means there
> is currently **no documented path** for an approved developer to reach reviews access at all. »

Et le cas d'usage décrit par ces développeurs est mot pour mot le nôtre : « a platform managing
reviews/Q&A for small businesses that grant manager access to their own verified profiles ».

**Verdict corrigé pour Google : guichet 3 ouvert sur le papier, et selon trois témoignages
concordants d'août 2026, inatteignable en pratique pour un nouvel entrant, derrière une liste
blanche non documentée.** Ce n'est pas une ligne B, c'est une ligne C — mais c'est exactement le
genre de C qui doit déclencher un test avant toute construction, et le § 6.3 dit comment le tester
pour moins de cent euros.

### 1.3 Ce que la faisabilité révèle, et que le document ne pouvait pas voir

**Aucune plateforme majeure n'offre le guichet 3 complet.** Sur sept plateformes examinées :

- **Lire et répondre par programme : trois** — Google (v4, sous réserve § 1.2), Booking, Expedia.
  **Aucune des trois par délégation OAuth par établissement.** Booking et Expedia passent par un
  compte machine de partenaire de connectivité : **guichet 1**. Google seul est en OAuth délégué, et
  c'est celui dont l'accès est bloqué.
- **Lire seulement : TripAdvisor** (5 avis maximum) et, sous réserve de **D8**, Airbnb.
- **Lire, et répondre par un détour : Meta**, sous App Review et vérification d'entreprise, avec un
  signal de dépréciation (**D9**).

**Conséquence d'architecture.** La thèse du § 2.7 du document — la proximité ouvre un guichet que les
acteurs mondiaux ne peuvent pas ouvrir — ne tient pas pour Booking, TripAdvisor et Expedia : chez eux
la porte n'est pas chez le client, elle est **chez la plateforme**, et elle s'ouvre par un accord
d'entreprise à entreprise où la proximité guadeloupéenne ne pèse rien. La proximité ne vaut que là où
le client est le porteur de l'autorisation : **Google, Airbnb, Meta**. C'est un périmètre, et il est
beaucoup plus étroit que celui du document.

### 1.4 Trois pièges contractuels trouvés en chemin, et qui valent plus que les endpoints

**(a) Booking interdit l'affichage public de ses avis.** Verbatim, sur la page d'accueil de la Review
API : « **Guest reviews retrieved by this API may not be used on your public page. The API is for
internal use by properties.** » (**cran B**). Tout widget, toute façade grand public, toute page
client affichant des avis Booking est en violation. Booking propose à la place un `reviews_iframe`
dont l'usage décrit est l'intégration « within the interface of a property management system (PMS) ».
→ Le volet « façade » du document (V4) ne pourra **jamais** afficher d'avis Booking.

**(b) TripAdvisor impose une obfuscation qui entre en collision frontale avec le droit français.**
*Review Implementation Policy*, verbatim (**cran B**) :

> « The review content **should never appear directly in the source code of the loaded page**, be it
> in HTML or JavaScript. […] The review content **must be loaded via an external JavaScript call that
> is blocked in robots.txt so that Google cannot crawl the review text.** »

Et *Display Requirements*, verbatim :

> « **You may only quote from a rave review – a review accompanied by a 5-bubble rating – if the
> overall property rating is at least a 4 out of 5** and you MUST include the date of the quoted review »

La première clause oblige à rendre le texte des avis non indexable et chargé par un appel bloqué dans
`robots.txt`. La seconde **interdit contractuellement de citer autre chose qu'un avis 5 étoiles**. Or
l'art. D111-17 1° c) du Code de la consommation exige d'indiquer « les critères de classement des avis
**parmi lesquels figurent le classement chronologique** », et l'art. L121-4 28° répute trompeux le fait
de « modifier des avis de consommateurs […] afin de promouvoir des produits ». **On ne peut pas à la
fois respecter les conditions d'affichage de TripAdvisor et offrir un affichage loyal au sens du droit
français.** Il faut choisir, et le choix est : ne pas afficher d'avis TripAdvisor du tout. C'est la
conclusion la plus nette de ce travail 1.

**(c) Expedia expédie déjà l'obligation européenne à ses partenaires.** *Verified guest reviews*,
verbatim (**cran B**) :

> « **To meet review legal regulations, we require that the following information be provided along
> with the guest reviews:** Expedia Group verifies reviews to ensure the traveler booked with Expedia
> Group. Travelers may receive a savings voucher when they submit a review. Expedia Group publishes
> all reviews that meet our guidelines, whether positive or negative. »

Trois mentions imposées par contrat, qui sont la traduction exacte de l'art. L121-4 27° et de
l'art. D111-17 2° a) (« l'existence ou non de contrepartie fournie en échange du dépôt d'avis »).
→ L'obligation n'est pas théorique : une OTA mondiale la répercute déjà sur ses partenaires. Elle est
donc **opposable, documentée et outillée** — et c'est un argument de vente, pas une charge.

---

## 2. TRAVAIL 2 — Le droit transformé en spécification produit

Niveau de précision : cahier des charges. Une ligne par obligation. « Champ » = colonne de base,
« Trace » = ce qui doit rester prouvable, « Porte » = geste humain bloquant.

### 2.1 Schéma de données — champs obligatoires sur chaque avis capté

| # | Spécification | Fondement | Cran |
|---|---|---|---|
| S1 | Champ `date_experience_consommation` (date, nullable **mais nullité tracée**), distinct de `date_publication`. | C. consom. **D111-17 1° b)** : « La date de publication de chaque avis, **ainsi que celle de l'expérience de consommation concernée par l'avis** » | **B** |
| S2 | Champ `date_experience_source` à valeurs contraintes : `api_directe` \| `jointure_reservation` \| `declare_client` \| `indisponible`. Un avis en `indisponible` **ne peut pas** être affiché à un consommateur. | Même article + impossibilité technique établie en § 2.2 ci-dessous | **B appliqué** |
| S3 | Champ `reservation_id` conservé quand la plateforme le fournit, et clé de jointure vers la date de sortie du séjour. | Booking Review API : l'objet avis porte `reservation_id`, mais **aucune date de séjour** ; Expedia `reviews` porte « reservation dates » | **B** |
| S4 | Champ `procedure_controle_source` à valeurs contraintes : `verifie_par_reservation` \| `verifie_autrement` \| `non_verifie` \| `inconnu`, renseigné **par source** et non par avis. | C. consom. **D111-17 1° a)** « L'existence ou non d'une procédure de contrôle des avis » ; **L121-4 27°** | **B** |
| S5 | Champ `contrepartie_depot` (booléen + texte), renseigné par source. Expedia impose de déclarer le bon de réduction. | **D111-17 2° a)** ; Expedia *verified guest reviews* | **B** |
| S6 | Champ `langue_avis` (ISO 639-1) **et** `langue_reponse_autorisee`, parce que Booking refuse les réponses hors langue de l'avis ou anglais. | Booking, *Responding to guest reviews* : « You can respond […] in the language of the review or in English. **Responses in other languages won't be published.** » | **B** |
| S7 | Champ `delai_max_conservation` par source, et purge automatique à son échéance. | **D111-17 2° b)** « Le délai maximum de publication **et de conservation** d'un avis » ; RGPD art. 5.1.e | **B** |
| S8 | Champ `texte_avis` en **écriture unique**, avec contrainte base interdisant l'`UPDATE`. Toute correction se fait par nouvelle version horodatée, jamais par écrasement. | **L121-4 28°** : « ou **modifier des avis de consommateurs** […] afin de promouvoir des produits » — pratique réputée trompeuse, irréfragable | **B** |
| S9 | Champ `source_donnee` : URL ou identifiant d'API exact d'où l'avis vient, conservé par avis. | RGPD art. 14.2 f) ; CNIL 30 avril 2020 : « les informations prévues à l'article 14 […] et notamment celle **relative à la source des données** » | **B** |
| S10 | Champ `usage_public_autorise` (booléen) par source, **initialisé à faux**, et passé à vrai seulement sur licence écrite. Booking impose faux ; TripAdvisor impose faux en pratique (§ 1.4 b). | Booking Review API : « may not be used on your public page » ; TripAdvisor *Review Implementation Policy* | **B** |
| S11 | Champ `etat_reponse` à valeurs `brouillon` \| `soumise` \| `en_moderation` \| `approuvee` \| `rejetee` \| `rejetee_violation`, plus `motif_rejet`. Les trois plateformes qui acceptent les réponses les modèrent. | Google : `reviewReplyState` ∈ {PENDING, REJECTED, APPROVED} + `policyViolation` ; Booking : modération 48-72 h ; Expedia : webhooks `…ResponseApproved` / `…ResponseRejected` | **B** |
| S12 | Champ `eligible_reponse` (booléen), lu à la source et non déduit. Expedia refuse la réponse si une réponse existe, si une est en modération, **ou si l'avis a été importé par le partenaire**. | Expedia, `isEligibleForResponse: false` — trois cas énumérés | **B** |

### 2.2 Le constat qui commande S1 et S2, et qui est le résultat le plus dur de ce travail

**La date de l'expérience de consommation n'est pas exposée par la majorité des plateformes.**

| Plateforme | Date du séjour exposée ? | Preuve |
|---|---|---|
| **Expedia Rapid** | **Oui** | « **Month and year of the traveler's stay** and date of review submission » |
| **Expedia Lodging Supply** | **Oui** | « Review data includes details such as review ID, reservation ID, header, review text, score, reviewer name, **and reservation dates** » |
| **Booking** | **Non directement** — l'objet avis porte `created_timestamp`, `last_change_timestamp`, `reservation_id`, et **aucune date de séjour**. Récupérable **par jointure** sur `reservation_id`. | Payload complet de `GET /review-api/properties/{id}/reviews` lu |
| **Google** | **Non.** L'objet `Review` porte `createTime`, `updateTime`, `starRating`, `comment`, `reviewer`, `reviewReply`. Aucune notion de date d'expérience — Google n'a pas de réservation. | Référence REST `accounts.locations.reviews` lue |
| **TripAdvisor** | **Partiellement** — le champ `travel_date` (AAAA-MM) existe dans la réponse `/location-reviews`. | Documentation JSON Partner API lue |
| **Airbnb** | **Non établi** — le schéma lu porte `created_at`, pas de date de séjour, mais `reservation_id` est présent. | Schéma mirroir, **cran C** |
| **Meta** | **Non.** `created_time` seul. | Référence `Recommendation` lue |

**Conséquence, et elle est structurelle, pas corrigeable.** Pour Google — qui est la plateforme la
plus importante pour un établissement guadeloupéen et celle qui n'a aucune réservation à joindre —
**la date de l'expérience de consommation est définitivement indisponible**. Donc un avis Google
agrégé **ne peut pas** être affiché à un consommateur en conformité avec l'art. D111-17 1° b).

Il n'y a que trois sorties, et il faut en choisir une en V0 :

1. **Ne jamais afficher d'avis agrégé à un consommateur.** Le tableau de bord reste un outil interne
   au professionnel, ce qui le sort probablement du « diffuser » de L111-7-2 — à confirmer par le
   juriste, c'est la question **J4** du § 4.
2. **Afficher uniquement les avis collectés en première main**, par enquête, où la date d'expérience
   est connue parce qu'on l'a demandée. C'est la voie que le marché a déjà prise (§ 3.2).
3. **Afficher les avis agrégés avec la mention explicite que la date d'expérience n'est pas
   disponible pour cette source.** Conformité par la transparence du manque. Non éprouvée, et c'est
   la position la plus honnête.

### 2.3 Traces à conserver

| # | Spécification | Fondement | Cran |
|---|---|---|---|
| T1 | Journal immuable, par source : version des CGU lue, date de lecture, verdict de guichet, et **la balance d'intérêt légitime écrite**. Une source sans fiche ne peut pas être collectée — contrainte technique, pas procédure. | RGPD art. 6.1.f + art. 5.2 (responsabilité) ; CNIL *Réutilisateurs de données publiées sur Internet* : « l'intérêt légitime du réutilisateur doit être apprécié **au cas par cas** » | **B** |
| T2 | Journal des accès délégués : jeton, portée accordée, identité du mandant, date de consentement, **preuve écrite ou numérique du consentement**, date et canal de révocation. | Google, *third-party policies* : « To respond to reviews on behalf of the end customer, you must have an **explicit approval. Verbal consent isn't sufficient.** […] you must provide a **written or digital proof of consent** » | **B** |
| T3 | Liste repoussoir, consultée **avant** toute requête de collecte, indexée sur l'identifiant d'auteur de la source, et jamais purgée. | CNIL fiche moissonnage du 19 juin 2025 : « prévoir un **droit d'opposition discrétionnaire et préalable** […] mécanismes de « **liste repoussoir** » […] en s'abstenant de collecter » | **B** |
| T4 | Journal `robots.txt` : pour chaque domaine collecté hors API, l'état du fichier au moment de la collecte, horodaté et archivé. Un `robots.txt` restrictif bloque la collecte **et** doit pouvoir être prouvé *a posteriori*. | Même fiche CNIL : le traitement « ne pourra pas entrer dans les attentes raisonnables » si le responsable n'exclut pas les sites qui s'opposent | **B** |
| T5 | Journal éditorial : pour chaque contenu publié, l'identité de la personne physique qui l'a relu, l'horodatage de la relecture, le texte avant et après. | LCEN art. 6 et loi du 29 juillet 1881 (qualification d'éditeur) ; règlement IA art. 50(4) al. 2 pour les contenus qui en relèvent | **C** (LCEN lue sur miroir) / **B-miroir** (art. 50) |
| T6 | Rejeu : tout affichage consommateur doit pouvoir être reconstruit à l'identique à une date passée — quels avis, dans quel ordre, avec quelles mentions. | **D111-17 1° c)** sur les critères de classement : une obligation d'affichage non rejouable n'est pas démontrable | **B appliqué** |

### 2.4 Portes humaines bloquantes

| # | Spécification | Fondement | Cran |
|---|---|---|---|
| P1 | **Aucune publication de texte généré sans validation humaine nominative enregistrée.** Le système refuse l'appel de publication si `relecteur_id` est nul. Pas un réglage par défaut : une contrainte. | Responsabilité d'éditeur (LCEN + loi de 1881, pas d'abri d'hébergeur sur un contenu généré) ; et condition d'exonération de l'art. 50(4) al. 2 **là où il s'applique** — voir la correction en § 5.1 | **C** + **B-miroir** |
| P2 | **Première collecte sur une source nouvelle impossible sans fiche de qualification validée** (guichet, degré, CGU lues, balance d'intérêt légitime, `usage_public_autorise`). | T1 + § 2.3 du document cible, qui prévoit la fiche mais ne la rend pas bloquante | **B appliqué** |
| P3 | **Aucun envoi de sollicitation d'avis sans filtrage préalable de la liste repoussoir et de BLOCTEL**, selon le canal. | CNIL 30 avril 2020 : « les logiciels doivent permettre de ne pas collecter les données des personnes inscrites sur des listes anti-prospection […] ou auprès du dispositif BLOCTEL » | **B** |
| P4 | **Aucune sélection d'avis par la note pour l'affichage.** Le tri par défaut est chronologique, et tout autre critère est déclaré à l'écran. Verrou de code, pas réglage client. | **D111-17 1° c)** : critères de classement « parmi lesquels **figurent le classement chronologique** » ; **L121-4 28°** | **B** |

### 2.5 Mentions à afficher

| # | Spécification | Fondement | Cran |
|---|---|---|---|
| M1 | À proximité de **chaque** avis : existence ou non d'une procédure de contrôle ; date de publication ; date de l'expérience de consommation ; critères de classement. | **D111-17 1°** | **B** |
| M2 | Dans une rubrique dédiée facilement accessible : existence ou non de contrepartie ; délai maximum de publication et de conservation ; caractéristiques principales du contrôle ; possibilité de contacter l'auteur ; possibilité ou non de modifier un avis ; motifs de refus de publication. | **D111-17 2°** et **D111-18** | **B** |
| M3 | Fonctionnalité **gratuite** permettant au responsable du produit ou du service de signaler un doute motivé sur l'authenticité d'un avis. | **L111-7-2**, avant-dernier alinéa | **B-miroir** |
| M4 | Mention de l'origine des données et du caractère indirect de la collecte, publiquement accessible, pour fonder l'exemption d'effort disproportionné. | RGPD art. 14.5 b) | **B appliqué** |
| M5 | Pour un contenu généré par IA destiné à un humain en interaction directe : information que l'interlocuteur est une IA, **au plus tard à la première interaction**. | Règlement IA **art. 50(1)** et **50(5)** | **B-miroir** |
| M6 | Marquage lisible par machine des sorties génératives — obligation du **fournisseur** du système. Si le modèle est tiers : engagement écrit du fournisseur, obtenu et archivé. | Règlement IA **art. 50(2)** | **B-miroir** |
| M7 | Droit de réponse outillé pour toute personne nommée ou désignée dans un service de communication au public en ligne. | LCEN **art. 6-IV** | **C** |

---

## 3. TRAVAIL 3 — Test de l'hypothèse : les outils à 0-80 €/mois tiennent-ils ces obligations ?

### 3.1 Résultat global, en une ligne

**L'hypothèse se vérifie sur l'affichage et sur la publication autonome. Elle se falsifie sur la
collecte et sur la vérification.** Le marché français bas de gamme est non conforme là où le document
ne regardait pas — l'affichage sélectif par la note — et il est **déjà conforme**, certifié même, là
où le document croyait trouver son avantage : la vérification de l'authenticité. La position de
différenciation existe, mais ce n'est pas celle qu'on croyait. Détail ci-dessous.

### 3.2 Produit par produit

**Meditrust** — le seul des trois dont le prix public soit dans la tranche nommée.
`meditrust.io/produit-afficher-avis/`, consulté le 2 octobre 2026. **Cran B** (page de l'éditeur).
Grille publique lue : **gratuit** (200 affichages/mois), **5,95 €/mois** widget seul illimité, packs
**34 €** et **69 €**, pack avancé **129 €/mois**.

Verbatim, et ce sont des arguments de vente, pas des aveux :

> « Le widget Meditrust affiche automatiquement **vos meilleurs avis** Google sur votre site »

> « ✅ **Tri par note (4★ et + par défaut)** »

> « 🧠 **Affichage intelligent : les bons avis, au bon endroit** […] Sur une page "épilation laser" →
> **uniquement des avis parlant de l'épilation laser** »

> « La version gratuite vous permet d'afficher **les 4 avis les plus récents** de votre fiche Google.
> Les versions payantes offrent plus de flexibilité, comme **l'affichage d'avis spécifiques** »

**Analyse.** Un widget qui republie des avis à destination des consommateurs sur le site d'un
professionnel est dans le champ de L111-7-2 (« diffuser ») sans discussion. Or :
— **P4 et M1 violés** : le tri par défaut est la note, pas la chronologie, et aucun critère de
classement n'est annoncé à l'écran. D111-17 1° c) exige l'inverse.
— **S1 et M1 violés** : rien n'indique que la date de l'expérience de consommation soit captée ni
affichée. Elle est de toute façon indisponible depuis Google (§ 2.2).
— **L121-4 28°** : filtrer à 4★ et plus « afin de promouvoir » est une sélection, pas une
modification d'avis. La qualification est discutable et je ne l'affirme pas. Mais la combinaison
« meilleurs avis » + « affichage d'avis spécifiques » + absence de toute mention de classement est
exactement ce que la DGCCRF cherche. **Cran : B pour les faits, D pour la qualification pénale.**
— Un point d'honnêteté : leur onboarding est un « Sign in With Google », c'est-à-dire **OAuth**. Je ne
leur reproche donc **pas** de collecter des identifiants. Sur ce point précis, ils font bien.

**Partoo** — prix non obtenu (**D11**). `partoo.co/fr/entreprises/review-management/`,
`partoo.co/fr/tarifs/`, `help.partoo.co/fr/articles/8006551`, `help.partoo.co/fr/articles/3606462`,
`help.partoo.co/fr/articles/11366556`, tous consultés le 2 octobre 2026. **Cran B** (pages et centre
d'aide de l'éditeur).

Verbatim, trois constats :

> « **L'agent ne se contente pas de suggérer une réponse : il la publie**, comme si vous aviez cliqué
> sur « Publier » dans Review Management. » *(à propos de leur MCP)*

> « La réponse automatique attendue sera affichée dès la réception de l'avis, avec l'heure prévue
> d'envoi et la mention **"Réponse automatique"**. » *(l'étiquette est dans l'interface Partoo ; rien
> n'indique qu'elle accompagne la réponse publiée côté consommateur)*

> « **Conservez sur la plateforme Partoo, les avis supprimés par les internautes** - par exemple un
> avis négatif auquel vous auriez répondu. »

**Analyse.**
— **P1 violé** : publication autonome par agent IA, sans porte humaine. C'est vendu comme la
fonctionnalité, et c'est aussi le cas pour les « réponses automatiques aux avis **avec**
commentaire ».
— **M5/M6 : non constaté.** Aucune mention d'un marquage ou d'une divulgation du caractère généré
côté consommateur. Mais voir ma correction du § 5.1 : l'art. 50(4) al. 2 ne couvre probablement pas
une réponse à avis, donc **je ne conclus pas à une violation du règlement IA ici**. Ce qui reste
entier, c'est l'absence de responsabilité éditoriale assumée, donc le risque LCEN/1881.
— **RGPD, et c'est le point le plus lourd** : conserver des avis que leur auteur a supprimés est une
conservation de données au-delà de la finalité, alors que la suppression par l'auteur est le signal
le plus clair possible d'une volonté de retrait. Art. 5.1.e, art. 17, art. 21. Je ne connais pas leur
base légale ni leur durée, donc je ne qualifie pas le manquement — mais c'est, verbatim sur leur
propre centre d'aide, une fonctionnalité qui a besoin d'une justification que je ne vois pas.
— **Et une question ouverte qui vaut un appel** : Partoo annonce répondre aux avis **TripAdvisor**.
Or TripAdvisor n'expose **aucun endpoint de réponse** (§ 1.1). Soit la réponse TripAdvisor est
manuelle et l'interface n'est qu'un presse-papier, soit elle passe par une voie non documentée. Je ne
sais pas. **Non vérifié**, et c'est la question la plus intéressante à leur poser.

**Guest Suite** — prix non obtenu (**D11**). `guest-suite.com/care-reply`,
`/outil-gestion-avis-google`, `/nos-apis`, `/offres`, consultés le 2 octobre 2026. **Cran B.**

Verbatim, et ici l'hypothèse se retourne :

> « **Certifié NF Service Avis en ligne (AFNOR)**, garantie d'avis authentiques et traçables »

> « **Aucune review-gating** : conforme aux règles Google et à la norme NF AFNOR » / « aucune
> sélection interdite : tout client peut être invité à publier »

> « L'API Experience permet à votre logiciel métier […] d'envoyer à Guest Suite les données
> nécessaires à l'envoi d'enquêtes : contact, contexte, **date d'expérience**. »

> « **Auto-Reply modéré** : Des réponses générées par l'IA, adaptées à chaque avis, **puis validées
> par nos équipes sous 48h pour garantir leur pertinence avant publication.** »

**Analyse — ce qui falsifie l'hypothèse.**
— **S1 tenu** : ils captent la **date d'expérience**, nommément, par API. Sur leurs avis collectés en
première main, la contrainte que je présentais comme un angle mort du marché est **déjà** outillée.
— **S4 et L121-4 27° tenus** : la certification NF Service Avis en ligne est précisément « avoir pris
les mesures nécessaires pour le vérifier ». Et l'absence de *review-gating* est l'inverse de la
sélection reprochée à Meditrust.
— **P1 tenu dans un de leurs modes** : l'Auto-Reply modéré fait relire par des humains avant
publication. C'est, en substance, ma spécification P1 — à ceci près que le relecteur est l'éditeur du
logiciel, ce qui déplace la responsabilité éditoriale sans la supprimer.

**Ce qui reste non conforme, ou non vérifié, chez Guest Suite.**
— **P1 violé dans l'autre mode** : « Auto-Reply par banque de réponses […] **Zéro action de votre
part** », publié sous 6 h. Pas de porte humaine.
— **P4 en tension** : « Un carrousel des derniers **verbatims 5★** pour rassurer sans effort » et
« rich snippets étoiles ». Un carrousel 5★ est une sélection par la note, le même défaut que
Meditrust, vendu avec les mêmes mots.
— **S10 : risque direct.** Ils annoncent Booking parmi les plateformes centralisées **et** la
diffusion des avis « sur votre site Internet via nos différents widgets ». Si des avis Booking
passent dans un widget public, c'est contraire à la clause Booking citée au § 1.4 a). **Je n'ai pas
vérifié** qu'ils le font. C'est le test à cent euros du § 6.3.

### 3.3 Ce que le test change pour la stratégie — la version défendable de l'hypothèse

La version du coordinateur — « les outils à 0-80 € ne tiennent probablement aucune de ces
obligations » — est **trop large et elle est fausse pour Guest Suite**. La version qui survient du
test est plus étroite, et bien meilleure :

> **La conformité est atteignable sur les avis que l'on collecte soi-même, et structurellement
> impossible sur les avis agrégés chez les plateformes** — parce que la date de l'expérience de
> consommation n'existe pas dans l'API de Google, parce que Booking interdit l'affichage public des
> siens, et parce que les conditions d'affichage de TripAdvisor sont incompatibles avec l'affichage
> loyal exigé en France.

Trois conséquences, et elles sont plus utiles que l'hypothèse de départ.

1. **Le marché s'est déjà réfugié dans la collecte première main**, et il a raison : c'est le seul
   terrain où la conformité est faisable. L'enquête post-séjour certifiée NF n'est pas un gadget
   commercial, c'est **la réponse d'ingénierie à L121-4 27° et à D111-17 1° b)**. Le document cible
   n'a pas d'organe de collecte première main. C'est, après le guichet, son deuxième manque.
2. **La non-conformité du marché est concentrée sur l'affichage**, pas sur la collecte : tri par la
   note par défaut, carrousels 5★, absence de critères de classement affichés, absence de date
   d'expérience sur les avis agrégés. C'est vérifiable depuis l'extérieur, en trente secondes, sur
   le site d'un client de n'importe lequel de ces outils. **Un manquement constatable depuis la rue
   est un manquement signalable par un concurrent.**
3. **Donc la position de différenciation n'est pas « la conformité » en général** — Guest Suite la
   vend déjà, avec un certificat AFNOR que nous n'avons pas. Elle est : **l'affichage loyal de l'avis
   agrégé, ou son refus assumé.** Dire à un hôtelier « votre widget actuel trie vos avis par la note
   et c'est une pratique que la DGCCRF sanctionne ; le mien affiche tout, en ordre chronologique, en
   disant d'où ça vient et ce qu'on ne sait pas » est une proposition qu'aucun acteur mondial ne
   portera, parce qu'elle réduit la flatterie qui fait vendre les widgets. **C'est le seul endroit du
   test où je trouve une position tenable et non occupée.**

---

## 4. TRAVAIL 4 — Dossier pour relecture par un juriste humain

Une ligne par référence. Colonne « ce qui en dépend » = la décision suspendue à la réponse.

| # | Référence à faire relire | Question précise à poser | Ce qui en dépend | Cran actuel |
|---|---|---|---|---|
| **J1** | **C. consom. art. L111-7-2**, rédaction en vigueur, et **art. 64 V de la loi n° 2024-449 du 21 mai 2024** (entrée en vigueur annoncée au 17 février 2024). | Quelle est la rédaction exacte en vigueur aujourd'hui, et qu'a changé la loi de 2024 ? | **Tout le § 2** de ce fichier. Si les obligations ont bougé, les champs S1-S12 bougent. | B-miroir |
| **J2** | **C. consom. art. D111-16 à D111-19** (décret n° 2017-1436). | Texte en vigueur. Et : la « date de l'expérience de consommation » doit-elle être affichée **même quand la source ne la fournit pas**, ou l'impossibilité est-elle une excuse ? | Le choix entre les trois sorties du § 2.2. **C'est la question la plus importante du dossier.** | B |
| **J3** | **C. consom. art. L131-4** et **art. L132-2**. | Montants et nature exacts des sanctions — administrative pour L111-7-2, pénale pour L121-4. | Le calibrage du risque et l'assurance RC professionnelle. | C |
| **J4** | **C. consom. art. L111-7-2**, champ d'application. | Un tableau de bord accessible **au seul professionnel**, sans aucune façade consommateur, relève-t-il de « collecter, modérer ou **diffuser** des avis en ligne » ? | La sortie n° 1 du § 2.2, c'est-à-dire la possibilité de lancer un produit B2B pur sans l'appareil d'affichage. | B appliqué |
| **J5** | **C. consom. art. L121-4 27°**. | Que sont « les mesures nécessaires pour le vérifier » ? La certification **NF Service Avis en ligne / NF Z74-501** suffit-elle, et est-elle exigible pour des avis **agrégés** qu'on n'a pas collectés ? | Si oui : il faut budgéter la certification. Si non : il faut une autre preuve de vérification. | B |
| **J6** | **RGPD art. 14.5 b)** — exemption d'effort disproportionné. | Un agrégateur d'avis peut-il s'en prévaloir pour ne pas informer individuellement chaque auteur d'avis, et à quelles conditions de mesures compensatoires ? | **L'existence du volet avis.** Si non : le volet agrégation s'arrête. | B appliqué |
| **J7** | **RGPD art. 6.1.f** + CNIL, *Réutilisateurs de données publiées sur Internet* (2024) et fiche moissonnage (19 juin 2025). | La balance d'intérêt légitime doit-elle être refaite **par source** ou une analyse par catégorie de source suffit-elle ? | Le coût de T1 et P2, donc le coût d'ajout d'une source. | B |
| **J8** | **RGPD art. 9** appliqué à des avis d'hôtel en texte libre, quadrilingues dont le créole. | Le filtrage automatique de données sensibles est-il exigible quand aucun outil de filtrage n'existe pour une des langues ? Que vaut la collecte « incidente et résiduelle » reconnue par la CNIL ? | La faisabilité de l'exigence « Langues » du § 3 du document. | B |
| **J9** | **RGPD art. 35** et liste CNIL des traitements à AIPD obligatoire. | AIPD obligatoire, oui ou non, pour ce traitement précis ? | Un délai et un coût en V0. | **D7** |
| **J10** | **CPI art. L218-2 et L211-3-1** (loi n° 2019-775 du 24 juillet 2019). | Un résumé de dépêche locale qui « dispense le lecteur de s'y référer » sort-il de l'exception de très courts extraits ? Et une autorisation est-elle requise même avec un flux RSS ouvert ? | **L'existence du volet veille presse.** | B-miroir |
| **J11** | **CPI art. L341-1, L342-1, L342-2, L342-3** — numérotation et rédaction en vigueur. | Vérifier les numéros ; et confirmer que « Toute clause contraire au 1° est nulle » figure bien au L342-3 actuel. | La contraposée du § F2 du premier fichier, c'est-à-dire la seule ouverture favorable que j'aie trouvée. | B-miroir |
| **J12** | **CPI, article de sanction pénale du droit du producteur** — L343-1 ou L343-4 selon les versions. | Quel est le bon numéro, et quels sont les peines en vigueur ? | Rien d'opérationnel, mais une citation fausse dans un document de décision décrédibilise le reste. | C |
| **J13** | **Cass. 1re civ., 5 octobre 2022, n° 21-16.307** (LBC France c/ Entreparticuliers.com). | Lire l'arrêt, pas les commentaires. Que dit exactement la Cour sur l'indexation accompagnée de la reprise des critères essentiels ? | La règle de conception « on cite, on résume, on lie » du degré 5b. | C |
| **J14** | **CJUE, C-30/14, 15 janvier 2015**, § 38-40 combinés à **CPI L342-3 1°**. | Un agrégateur accédant à une base d'avis protégée par le droit sui generis est-il un « utilisateur licite » au sens de l'art. 8, et peut-il donc opposer la nullité d'une clause d'interdiction pour les parties non substantielles ? | La seule voie qui permettrait de lire une base d'avis **sans** passer par un guichet. Enjeu maximal. | B appliqué |
| **J15** | **LCEN n° 2004-575 du 21 juin 2004, art. 6** et **art. 6-IV** ; **règlement (UE) 2022/2065**. | Un agrégateur qui sélectionne, classe et résume est-il éditeur ? Et le droit de réponse de l'art. 6-IV s'applique-t-il à un tableau de bord professionnel ? | Le régime de responsabilité, la prescription applicable, et l'outillage M7. | C |
| **J16** | **Règlement (UE) 2024/1689, art. 50(1), 50(2), 50(4) al. 2**, et **règlement (UE) 2026/1744**. | Trois questions. (a) Une réponse à un avis client est-elle un « texte publié dans le but d'informer le public sur des questions d'intérêt public » ? (b) Qui est fournisseur et qui est déployeur quand on intègre un modèle tiers ? (c) Le calendrier — art. 50 applicable depuis le 2 août 2026, marquage machine au 2 décembre 2026 — est-il exact ? | **La porte P1 et les mentions M5-M6.** Si la réponse à (a) est non, l'obligation d'étiquetage tombe sur les réponses à avis et ne reste que sur le blog. Voir ma correction § 5.1. | **D10** + B-miroir + C |
| **J17** | **Conditions d'affichage TripAdvisor** — *Review Implementation Policy* et *Display Requirements*. | Une clause contractuelle qui interdit de citer un avis en dessous de 5 bulles, et qui oblige à rendre le texte non indexable, est-elle opposable en France face à L111-7-2 et D111-17 ? Et une clause abusive ou illicite rend-elle la licence inexécutable ? | **L'inclusion ou l'exclusion de TripAdvisor du produit.** | B |
| **J18** | **Clause Booking** : « Guest reviews retrieved by this API may not be used on your public page. » | Portée exacte : un tableau de bord accessible par mot de passe au seul hôtelier est-il une « public page » ? | La frontière entre produit interne et façade, pour la plateforme n° 2. | B |
| **J19** | **Airbnb API Terms** (airbnb.com/help/article/3418), § 1.3 et § 2.B. | L'obligation d'« implementing all mandatory API features within 6 months of their release » et la soumission à des audits de sécurité à la demande d'Airbnb sont-elles tenables pour une structure de notre taille ? | L'inclusion d'Airbnb, qui est la plateforme majeure du locatif guadeloupéen. | B |
| **J20** | **Revente de données d'avis par un tiers** (type StayAPI pour Expedia). | Acheter à un tiers des avis extraits sans licence expose-t-il l'acheteur au même titre que l'extracteur ? | La tentation la plus forte du projet, et je pense qu'elle est fatale — voir § 4.1. | B appliqué |

### 4.1 Une alerte à passer au juriste avec le dossier

Un fournisseur de données tiers écrit, au sujet d'Expedia (`stayapi.com/blog/expedia-reviews-api`,
article daté du 23 juin 2026, consulté le 2 octobre 2026 — **cran C**, page commerciale d'un
vendeur), verbatim : « No official or reliable path exists for pulling Expedia review data
programmatically without a third-party provider » et « One API key covers Expedia alongside
Booking.com, Agoda, **TripAdvisor**, Airbnb, and Google Hotels. »

C'est la tentation maximale du projet : un seul contrat, six plateformes, aucune négociation. **Et
c'est exactement le montage qui a été condamné dans l'affaire leboncoin.** Entreparticuliers.com
n'extrayait pas elle-même : elle était abonnée au service de « pige » de Directannonces. La Cour
d'appel de Paris a écarté l'argument, verbatim : « le fait que cette extraction a été opérée à partir
d'un fichier "de la pige" de la société Directannonces est tout aussi inopérant, les notions
d'extraction et de réutilisation […] n'étant pas circonscrites aux cas d'extraction et de
réutilisation opérées directement à partir de la base d'origine, et ce **sous peine de laisser la
personne qui a constitué la base de données sans protection à l'égard d'actes non autorisés de
copiage opérés à partir d'une copie de sa base** » (CA Paris, pôle 5 ch. 1, 2 février 2021,
n° 17/17688, confirmé Cass. 1re civ. 5 octobre 2022 n° 21-16.307 — **cran B** pour l'arrêt d'appel).

**Acheter des avis scrapés à un revendeur est juridiquement identique à les scraper soi-même.** La
facture n'est pas une licence. À écrire en gras dans le dossier du juriste, et à relire le jour où
quelqu'un proposera ce raccourci, parce que quelqu'un le proposera.

### 4.2 La ligne distincte demandée — le guichet 6 reste-t-il valable pour les données ouvertes publiques et les communs documentaires ?

**Oui pour les données ouvertes publiques, et il est même plus solide que le document ne le disait.
Oui avec une réserve sérieuse pour les communs documentaires.** Je n'avais attaqué le guichet 6 que
sur la presse ; sur ces deux familles il tient.

**(a) Données ouvertes publiques : le droit sui generis est légalement désarmé.**

Le document fondait le guichet 6 sur la volonté de l'éditeur — « l'éditeur a **voulu** que
l'information soit reprise ». C'est un fondement faible, parce qu'une volonté se rétracte. Le vrai
fondement est bien plus fort : **une interdiction légale faite à l'administration d'opposer son
propre droit de producteur**.

**Code des relations entre le public et l'administration, art. L321-3**, créé par l'art. 11 de la loi
n° 2016-1321 du 7 octobre 2016 pour une République numérique. Texte lu sur
`legifrance.gouv.fr/codes/section_lc/LEGITEXT000031366350/LEGISCTA000031367750` (extrait de section
atteint) et corroboré mot pour mot par le texte de la loi sur `wipo.int/wipolex/en/legislation/details/16380`,
consultés le 2 octobre 2026. **Cran B-miroir.** Verbatim :

> « Sous réserve de droits de propriété intellectuelle détenus par des tiers, les droits des
> administrations mentionnées au premier alinéa de l'article L. 300-2 du présent code, **au titre des
> articles L. 342-1 et L. 342-2 du code de la propriété intellectuelle, ne peuvent faire obstacle à
> la réutilisation du contenu des bases de données que ces administrations publient** en application
> du 3° de l'article L. 312-1-1 du présent code.
> Le premier alinéa du présent article **n'est pas applicable aux bases de données produites ou
> reçues par les administrations […] dans l'exercice d'une mission de service public à caractère
> industriel ou commercial soumise à la concurrence.** »

Et la jurisprudence précède la loi dans le même sens : **Conseil d'État, 8 février 2017** (affaire du
département de la Vienne et de la réutilisation des archives départementales par une société de
généalogie) a jugé qu'un producteur public ne peut invoquer l'art. L342-1 CPI pour s'opposer à la
réutilisation d'informations publiques. Source : `eurojuris.fr/articles/...-37286.htm`, consulté le
2 octobre 2026 — **cran C**, commentaire d'avocat ; la décision elle-même n'a pas été lue, bases de
jurisprudence bloquées. **À ajouter au dossier juriste comme J21.**

**Donc, pour cette famille, le guichet 6 n'est pas une tolérance : c'est un droit.** Les deux
obstacles qui tuaient la presse — droit voisin, droit sui generis — sont ici inopérants : le droit
voisin ne concerne que les publications de presse, et le droit sui generis est expressément écarté.

**Les quatre réserves, et elles sont réelles.**
1. **« Sous réserve de droits de propriété intellectuelle détenus par des tiers »** — une base
   publique qui incorpore des photos, des textes ou des données sous droits de tiers n'est pas
   libérée pour cette part. Il faut lire le contenu, pas seulement la licence.
2. **L'exception SPIC** — une base produite dans une mission de service public industriel et
   commercial soumise à la concurrence reste protégée. À vérifier source par source : certaines bases
   d'opérateurs publics tombent ici.
3. **Le RGPD n'est pas touché.** L321-3 désarme le droit des bases, pas la protection des données.
   Une base ouverte contenant des données personnelles reste intégralement soumise aux obligations du
   § 2.3, et la CNIL le dit explicitement pour le « premier cas » de ses recommandations 2024.
4. **La licence commande encore l'attribution**, et CRPA art. L323-2 impose que la licence de
   réutilisation gratuite soit choisie dans une liste fixée par décret. Donc : lire la licence, citer
   la source, et vérifier qu'elle est bien l'une des licences homologuées.

**(b) Communs documentaires : oui, mais le partage à l'identique est un piège commercial.**

Le document les range au guichet 6 avec, en obligation, « Attribution, partage à l'identique selon les
cas ». C'est exact et c'est insuffisamment alarmant. Les communs ne reposent **pas** sur une
désactivation légale comme en (a) : ils reposent sur des **licences, c'est-à-dire des contrats**. Une
licence de base de données à partage à l'identique peut obliger à republier sous la même licence la
base dérivée — ce qui est incompatible avec un produit propriétaire dont la base est l'actif. Le
risque n'est pas d'être poursuivi pour contrefaçon : c'est d'être obligé d'ouvrir son propre index.

Je **n'ai pas lu** les textes de ces licences dans cette session. C'est donc **cran D** et cela doit
devenir une tâche V0 nommée : pour chaque commun envisagé, lire la licence et répondre à une seule
question — **la base dérivée doit-elle être publiée sous la même licence, oui ou non ?** Un « oui »
disqualifie la source pour l'index propriétaire, tout en la laissant utilisable pour de
l'enrichissement non redistribué.

**Conclusion de cette ligne.** Le guichet 6 survit, et il devient le **socle** du volet collecte — non
pas parce que personne ne peut le fermer, mais parce que **la loi interdit à l'administration de le
fermer**. C'est une différence de nature, et c'est la meilleure nouvelle de ces deux retours. À une
condition de vocabulaire : il faut cesser de l'appeler « accès ouvert **déclaré** ». La déclaration
n'est pas le fondement. Le fondement est légal. Appelez-le **guichet 6 — accès ouvert de droit**, et
ne mettez dedans que ce qui y est de droit : les bases publiées par les administrations au titre de
l'open data. Les flux RSS de presse et les communs sous partage à l'identique n'y sont pas.

---

## 5. Corrections à mon propre premier fichier

Un retour qui ne se corrige pas n'est pas un retour.

### 5.1 Correction majeure — j'ai sur-étendu l'art. 50(4) du règlement IA

Dans `01-juridique.md`, § M7 et § 5 condition 5, j'ai écrit que la relecture humaine était « la
condition légale d'exonération de l'art. 50(4) » pour le produit, et je l'ai appliqué sans distinction
aux réponses à avis.

**C'est probablement faux.** L'art. 50(4) al. 2 vise, verbatim, « les textes publiés **dans le but
d'informer le public sur des questions d'intérêt public** ». Une réponse commerciale à un avis de
client n'informe pas le public sur une question d'intérêt public : elle répond à un client. Mon
interprétation est en **cran D10**, déclarée en tête, et elle appelle la question (a) du **J16**.

**Ce qui change.** Si D10 est juste :
— **un billet de blog** généré sur l'actualité locale, produit par le volet V4, **est** probablement
  dans le champ de 50(4) al. 2, et la relecture humaine avec responsabilité éditoriale assumée
  l'exonère ;
— **une réponse à avis** n'y est pas. Restent applicables l'art. 50(1) si le système dialogue
  directement avec le client, et l'art. 50(2) qui pèse sur le **fournisseur** du modèle.

**Ce qui ne change pas, et c'est l'essentiel.** La porte humaine P1 reste obligatoire — mais son
fondement principal n'est pas le règlement IA, c'est **la responsabilité d'éditeur sous la LCEN et la
loi du 29 juillet 1881**. Un texte généré n'est pas un contenu de tiers ; il n'y a aucun abri
d'hébergeur ; celui qui le publie en répond. P1 tient sur un fondement plus solide que celui que je
lui avais donné. J'avais la bonne conclusion et le mauvais article.

### 5.2 Correction du verdict Google

`01-juridique.md`, § 5 condition 2, disait : « Google : ouvert dès maintenant au prix d'un onboarding
par client ». À remplacer par : **ouvert sur le papier ; selon trois témoignages concordants d'août
2026 sur le forum développeurs de Google, l'endpoint d'avis v4 est inatteignable pour un nouvel
entrant, derrière une liste blanche non documentée que l'agrément Basic API Access ne débloque pas**
(§ 1.2, cran C). À tester avant toute construction.

### 5.3 Précision sur le guichet 2

Mon premier fichier concluait que le guichet 2 devait être réécrit en guichet 3. Le travail 1 montre
que c'est vrai **pour trois plateformes sur sept**, et que pour Booking, TripAdvisor et Expedia la
réécriture correcte est **guichet 1**. La conclusion « le guichet 2 n'existe pas » est confirmée ; la
conclusion « c'est du guichet 3 » était trop optimiste.

---

## 6. Relance appliquée — avec la question corrigée par le coordinateur

### 6.1 Ce que j'ai réellement écarté — sans quota

Trois pistes, parce que j'en ai écarté trois, pas parce qu'il en fallait trois.

1. **Yelp, Trustpilot, PagesJaunes/Solocal et Agoda.** Écartés faute de temps après sept plateformes.
   Pour la Guadeloupe je pense que l'ordre d'importance est Google, Booking, Airbnb, TripAdvisor,
   Facebook, Expedia — et que Yelp est négligeable en France. **Mais c'est une opinion, cran D, et
   PagesJaunes mériterait d'être traité parce que Guest Suite l'intègre et qu'il est un acteur
   français.**
2. **Le contentieux des avis supprimés et la suppression d'avis illicites.** Guest Suite vend
   « surveillance et traitement des avis illicites », Partoo permet de signaler un avis à Google. Il y
   a là un sujet juridique entier — demande de retrait, diffamation, procédure — que je n'ai pas
   ouvert parce qu'il est en aval du périmètre d'accès qui m'était demandé. **C'est probablement le
   service pour lequel un hôtelier guadeloupéen paierait le plus cher**, et il n'est traité ni par le
   document ni par moi.
3. **Le règlement (UE) 2026/1744 lui-même.** Non lu, EUR-Lex partiellement bloqué. J'ai préféré
   marquer tout le calendrier du règlement IA en cran C plutôt que de retenter. C'est dans J16.

### 6.2 Ce que je n'ai pas pu vérifier

- La **clause des GDT Booking** sur la remise d'identifiants : toujours pas obtenue.
- **D8** : existe-t-il une mutation de réponse aux avis chez Airbnb.
- **D9** : la portée réelle de la dépréciation annoncée côté Meta.
- **D11** : les prix de Partoo et Guest Suite.
- Si **Guest Suite affiche réellement des avis Booking dans ses widgets publics** — le point qui
  déciderait de la conformité de la plateforme n° 2 chez le leader français.
- Par quelle voie **Partoo répond aux avis TripAdvisor**, puisqu'aucun endpoint de réponse n'existe.
- Le texte des **licences de communs documentaires** et leur clause de partage à l'identique.
- L'arrêt du **Conseil d'État du 8 février 2017**, lu par commentaire seulement.

### 6.3 Question corrigée — laquelle de mes conclusions, si elle est fausse, coûte le plus cher, et comment la tester pour moins de cent euros

**La conclusion la plus coûteuse si elle est fausse n'est pas juridique. C'est le § 1.2 : l'accès à
l'API d'avis de Google.**

Pourquoi elle domine toutes les autres. Google est la seule plateforme qui réunisse les trois
conditions du produit : volume d'avis le plus élevé pour un établissement guadeloupéen, lecture **et**
réponse par programme, et **autorisation portée par le client** — donc le seul endroit où la thèse de
la proximité du § 2.7 fonctionne réellement. Si l'accès est fermé, il ne reste que des guichets 1
(Booking, Expedia) qu'un acteur guadeloupéen de petite taille n'ouvrira pas au départ, et le produit
n'a plus de porte d'entrée. Toutes mes autres conclusions se négocient, se contournent, ou se
réparent par un juriste. Celle-là, non : elle est binaire, et elle est hors de notre contrôle.

Et symétriquement, si **je** me trompe — si l'accès s'obtient normalement et que les trois
développeurs du forum ont eu un problème particulier — alors j'ai découragé le projet sur un cran C.
C'est le coût de mon erreur, et il est aussi élevé que celui de la leur.

**Le test, et il coûte moins de cent euros.**

Deux à quatre semaines de calendrier, zéro euro d'infrastructure, un seul euro de domaine s'il en
faut un. Le coût réel est du temps, pas de l'argent — ce qui est précisément ce qu'il faut dépenser
avant d'écrire du code.

1. Créer un projet Google Cloud. **Gratuit.** Activer les trois API modernes. Observer le quota.
2. Tenter `gcloud services enable mybusiness.googleapis.com`. **Le résultat du jour 1 est déjà la
   moitié de la réponse** : si la commande échoue en `PERMISSION_DENIED` avec « not available to this
   consumer », le témoignage du forum est reproduit sur notre propre compte, et c'est une ligne
   **A-usage**, la plus haute du barème du document, obtenue en une commande.
3. Déposer la demande de *Basic API Access* via le formulaire Google Business Profile, en déclarant le
   cas d'usage réel — plateforme de gestion d'avis pour petites entreprises avec accès gestionnaire
   accordé par le commerçant. Noter la date et l'identifiant de dossier.
4. Faire accorder un accès **gestionnaire** par un seul hôtelier guadeloupéen volontaire sur sa fiche
   déjà vérifiée. Aucun paiement, aucun engagement de sa part, révocable d'un clic : c'est le même
   geste que lorsqu'il ajoute son neveu comme gestionnaire. **Ce geste teste aussi, gratuitement, le
   parcours d'onboarding que le § 6.3 du premier fichier proposait comme correctif économique.**
5. Appeler `reviews.list` sur sa fiche. Trois issues : ça répond — alors le § 1.2 est faux, Google est
   ouvert, et le produit a sa porte d'entrée. Ça répond `403 SERVICE_DISABLED` — alors le § 1.2 est
   confirmé et il faut relancer Google en citant le fil du 12 août 2026. Rien ne répond au bout de six
   semaines — alors le délai lui-même est la réponse, et il est incompatible avec un lancement.

**Et un second test, à vingt euros, qui vaut la peine d'être lancé en parallèle** parce qu'il teste
l'hypothèse commerciale pendant que le premier teste l'hypothèse technique : souscrire **un mois de
Meditrust à 5,95 €**, brancher le widget sur une page jetable, et constater par capture d'écran
horodatée que le tri par défaut est la note et qu'aucun critère de classement n'est affiché. Cela
transforme ma ligne B — « leur page de vente le dit » — en ligne **A-usage** : « je l'ai installé, et
voici la sortie ». C'est, dans tout ce que j'ai écrit sur deux fichiers, la seule affirmation qui
puisse atteindre le cran le plus haut du barème du document pour le prix d'un déjeuner. Et c'est aussi
la démonstration commerciale à montrer à un hôtelier.

---

## 7. Ce qui change dans les cinq colonnes depuis le premier fichier

**MCP à installer** — un ajout, et il monte en tête : **le MCP de Partoo**, que l'éditeur annonce
comme « disponible pour l'ensemble de nos clients » et dont il écrit que l'agent « ne se contente pas
de suggérer une réponse : **il la publie** ». C'est à la fois le concurrent le plus avancé sur
l'orchestration par agent et la démonstration vivante du risque P1. À connaître, pas nécessairement à
installer. Les trois MCP du premier fichier — Légifrance, EUR-Lex, Judilibre — restent la priorité, et
le travail 4 montre pourquoi : vingt lignes de dossier juriste au lieu de vingt lignes relues
directement.

**Logiciels manquants** — inchangé, et le blocage de sortie réseau a coûté, dans cette relance, le
texte des CGU TripAdvisor, l'arrêt du Conseil d'État du 8 février 2017 et le règlement 2026/1744.

**Outils déjà disponibles et non exploités** — `gcloud` **est installé dans cet environnement**. La
première étape du test du § 6.3 est donc exécutable sans rien installer. Je ne l'ai pas lancée : elle
exige un compte Google du projet, c'est-à-dire une décision de Laurent, pas une initiative d'agent.

**IA existantes qui font ce travail, et à quel prix** — le seul prix public établi dans deux fichiers :
**Meditrust, gratuit à 129 €/mois, widget seul à 5,95 €/mois**. Partoo et Guest Suite ne publient
aucune grille atteignable (**D11**). Les deux font de la génération et de la publication automatique
de réponses par IA ; Guest Suite est **certifié NF Service Avis en ligne (AFNOR)**, ce que nous ne
sommes pas et ce qui est, à ce jour, le seul avantage de conformité documenté du marché contre nous.

**Futurs possibles à douze mois ⏳** — deux ajouts aux cinq du premier fichier.
⏳ **La fermeture possible de l'accès tiers aux avis de Pages Facebook** (**D9**) : si elle se
confirme, une des trois plateformes en guichet 3 disparaît, et le périmètre du § 1.3 tombe à deux.
⏳ **La migration de l'API v4 de Google** : tous les endpoints d'avis vivent sur une API explicitement
qualifiée de *legacy*, dont les fonctions ont été réparties dans trois API modernes **qui n'ont reçu
aucun endpoint d'avis**. Soit Google les y portera — et il faudra réécrire —, soit il ne les portera
pas, et c'est un signal sur l'avenir de l'accès programmatique aux avis Google. Dans les deux cas,
aucune architecture ne doit supposer la stabilité de `mybusiness.googleapis.com/v4`.
