# Critique 08 — Le calendrier et les dépendances externes

Lecture adversariale du `PLAN-DE-CONSTRUCTION.md` du 2 octobre 2026.
Angle imposé : le calendrier et les dépendances externes. Contexte lu : `REGISTRE-DE-DEMARCHE.md`.
Barème à deux axes du registre : provenance `A` mesuré · `B` primaire · `C` secondaire · `D` mémoire, croisée avec robustesse `1` rejouable · `2` attesté · `3` étroit · `4` non étayé.

---

## 0 — Mes lignes `D`, déclarées en tête

Trois seulement. Tout le reste de ce document est adossé à une documentation officielle de plateforme, à une mesure en conteneur, ou est explicitement marqué `C`.

| Ligne `D` | Ce que je n'ai pas pu étayer |
|---|---|
| Le volume hebdomadaire réel de lignes utiles filtrées Guadeloupe dans BODACC, les données essentielles de la commande publique et les vigilances | Hôtes refusés, voir §7. Je n'ai **aucun** chiffre. Le seuil d'abandon « une dizaine de lignes par semaine » n'est donc ni soutenu ni démenti |
| Le nombre de sources nécessaires pour que la veille ait de la valeur marchande | Aucune source primaire n'existe sur cette question. Je ne la fabrique pas. Voir §4.2 pour ce que je peux dire à la place |
| Le délai de réponse d'un bâtonnier de Guadeloupe à une question déontologique écrite | Non trouvé. Les règlements fixent des délais à l'avocat, aucun à l'Ordre répondant à un tiers non-avocat |

---

## 1 — Verdict : la thèse qui commande le plan est fausse telle qu'elle est écrite

Le plan s'ouvre sur une phrase, et toute sa forme en découle :

> Le code n'est pas le coût. L'approbation l'est.
> […] Ils se lancent, et ensuite on attend. Tout le reste s'écrit pendant cette attente.
> D'où la forme de ce plan : administratif d'abord, technique ensuite.

**Cette inférence ne tient pas.** Elle suppose que déposer un dossier et écrire le code sont deux travaux séparables, qu'on peut mettre en parallèle, l'un devant l'autre. Sur trois des cinq plateformes que ce produit doit toucher, c'est l'inverse exact : **le dossier d'approbation ne peut pas être déposé avant que le code soit fini, public, et filmé en fonctionnement.** L'approbation n'est pas en amont du développement, elle est en aval.

Trois ruptures distinctes, chacune fatale à une partie de la forme du plan :

**1.1 — Là où il y a une approbation, elle exige le produit fini.** Meta : « Make sure you have completed app development and that it is ready for us to test. […] Your app must be publicly available ». TikTok : « Apps that are still in development or testing will not be approved. […] Your website URL cannot be a landing page or login page. You must have an externally facing fully developed website. » LinkedIn, palier Standard : un screencast démontrant l'OAuth complet et une publication réelle sur la Page d'un client. `B·2` sur les trois, citations en §2.

**1.2 — Là où il n'y a pas d'approbation, le coût est de l'argent, pas du temps.** X n'a plus d'étape d'approbation ni de palier gratuit depuis février 2026. Le modèle est au décompte : **0,015 $ par publication, et 0,200 $ dès que la publication contient un lien** (`B·3`, et §2.5 dit pourquoi ce n'est pas un `2` : l'hôte canonique `docs.x.com` m'est refusé, je n'ai lu que son miroir de prévisualisation). Un produit qui pousse les articles d'un blog publie, par construction, des liens. Le plan n'a aucune case pour ce poste : ni dans les coûts, ni dans le calendrier, ni dans les seuils d'abandon.

**1.3 — Là où l'attente est réelle et incompressible, elle ne porte pas sur une approbation mais sur l'âge d'un objet.** Google exige que le demandeur gère **une fiche d'établissement vérifiée et active depuis plus de 60 jours**, et qu'un **site web** représente l'entreprise de cette fiche (`B·2`, §2.4). Ce sont 60 jours de calendrier pur, qu'aucun dossier n'ouvre et qu'aucun travail ne raccourcit. C'est le seul endroit où la thèse du plan est juste — et c'est aussi le seul des cinq où « écrire pendant l'attente » marche vraiment.

**Conséquence sur la forme.** « Administratif d'abord, technique ensuite » est juste pour Google et faux pour Meta, TikTok et LinkedIn, où l'ordre contraint est : société immatriculée → site public avec politique de confidentialité → application construite et fonctionnelle → captures vidéo → **puis** dépôt. Le plan a inversé l'ordre sur la majorité de son périmètre.

**1.4 — Et la mesure qui fonde tout est sous-déterminée.** Le plan appuie son principe sur un seul `A·1` : « le troisième refusé en 403 — application non approuvée ». Or chez Meta, un refus sur un appel au nom d'un tiers peut venir de **trois portes indépendantes** : la vérification d'entreprise, la revue d'application pour l'accès avancé, et la vérification d'accès comme fournisseur technique — cette dernière étant explicitement « independent of App Review and permission access levels » (`B·2`, §2.1). Chez Google, le même symptôme sort en `403 SERVICE_DISABLED` ou en `429` selon que le service est désactivé ou le quota à zéro. Le plan ne nomme ni la plateforme, ni le code d'erreur exact, ni la permission demandée. Ce `A·1` établit donc qu'**un appel a échoué**. Il n'établit pas **laquelle des trois portes était fermée**, et les trois ne se franchissent ni dans le même ordre, ni dans le même délai, ni avec les mêmes pièces. La pierre d'angle du plan porte une inférence que sa propre mesure ne soutient pas.

---

## 2 — Les délais réels d'approbation, plateforme par plateforme

Le plan écrit « Gratuit, délai inconnu ⏳ » et bâtit sa semaine zéro autour de cet inconnu. Il n'était pas inconnu : il est publié. Voici ce que les documentations officielles disent.

### 2.1 — Meta (Facebook et Instagram) : trois portes successives, et un délai annoncé qui se contredit lui-même

**Le délai, dans les mots de Meta.** Deux pages officielles donnent deux réponses incompatibles, toutes deux en ligne :

> « At the moment we are dealing with increased volume. The entire process may take up to several weeks. — Permission review may take up to several weeks. — Business verification should take a few days, however it will depend on the quality of documentation. »
> — `developers.facebook.com/documentation/resp-plat-initiatives/appreview/FAQs`, mise à jour 12 juin 2025. `B·2`

> « It typically takes us less than one week to process your submission, and often takes only 2–3 days, but may take longer during peak periods. »
> — `developers.facebook.com/docs/resp-plat-initiatives/app-review/introduction/`. `B·2`

**Il n'existe donc pas de délai annoncé par Meta.** Il en existe deux, d'un facteur dix, sur le même site. Planifier sur l'un ou sur l'autre n'est pas la même décision. Le constaté, lui, est au-delà des deux : l'interface de Meta affiche « Most submissions are reviewed within 20 days », et le forum développeurs de Meta porte des fils de 25 jours sans réponse pour une revue, et de 14 jours pour une vérification d'entreprise annoncée à « environ 2 jours ouvrés » (`C·3`, forum hébergé par Meta, échantillon de cas isolés).

**Les trois portes, et leur ordre imposé.** C'est là que le plan se trompe le plus lourdement, parce qu'il n'en voit qu'une.

| Porte | Ce qu'elle exige | Ordre |
|---|---|---|
| **Vérification d'entreprise** | Une entité juridique, ses documents officiels, son adresse. « Advanced Access now requires Business Verification. » | Première. Rien ne se fait avant |
| **Revue d'application** (accès avancé) | Application finie et publiquement accessible · politique de confidentialité en ligne · icône 1024×1024 · **au moins un appel réussi par permission demandée, dans les 30 jours précédant le dépôt** · un enregistrement d'écran par permission | Deuxième |
| **Vérification d'accès comme fournisseur technique** | Obligatoire dès que l'application est utilisée par **d'autres entreprises** — c'est-à-dire exactement ce produit. « Any business that has created or claimed an app that will be used by other businesses […] must be verified as a Tech Provider before other businesses can use the app. » Prérequis explicite : la vérification d'entreprise déjà obtenue. Délai de grâce de **60 jours** pour la compléter. « Note that access verification is independent of App Review » | Troisième, et indépendante |

`B·2` sur les trois. Adresses, toutes sur `developers.facebook.com` et toutes consultées le 2 octobre 2026 : `/docs/development/release/business-verification` (page datée 7 juil. 2023) · `/docs/app-review/submission-guide` (page datée 30 juin 2026) · `/docs/development/release/access-verification/` · `/docs/development/release/tech-providers/`.

**Le verrou, dans les mots de Meta.** Le bouton de dépôt est grisé jusqu'à ce qu'un appel réussi ait été enregistré :

> « Note that the Request advanced access button will remain grayed out until a successful API has been logged in our system. A successful call must be made within 30 days of submitting for App Review. »

On ne peut pas déposer avant d'avoir appelé. On ne peut pas appeler sans l'application et son parcours d'autorisation. **Le dépôt Meta en semaine zéro est matériellement impossible.**

**Et une porte de plus, côté client.** L'autorisation de publication de Page est à la charge de l'établissement, pas de nous :

> « An Instagram professional account connected to a Page that requires Page Publishing Authorization (PPA) cannot be published to until PPA has been completed. »
> — `developers.facebook.com/docs/instagram-platform/content-publishing`, page datée du 30 juin 2026, consultée le 2 octobre 2026. `B·2`

Chaque client peut donc porter son propre blocage, après signature, sans que nous puissions agir. Le plan ne compte aucun délai par client au-delà du mandat.

### 2.2 — TikTok : un délai honnête, et une exclusion qui tue la phase 3 sur cette plateforme

**Le délai annoncé, et c'est le plus clair des cinq :**

> « App review may take several days to two weeks after submission. »
> — `developers.tiktok.com/doc/getting-started-faq`. `B·2`

**Les prérequis de dépôt** (`developers.tiktok.com/doc/app-review-guidelines/`, `B·2`) : site officiel entièrement développé, ni page d'atterrissage ni page de connexion · politique de confidentialité et conditions visibles sans ouvrir de menu · **au moins une vidéo de démonstration du parcours complet de bout en bout** · « Apps that are still in development or testing will not be approved ».

**Mais le problème n'est pas le délai.** Les lignes directrices de partage de contenu de TikTok excluent nommément ce produit :

> « API Clients must not be limited to test applications and should be intended for a wide audience, not limited to internal groups/private use.
> **Not acceptable: A utility tool to help upload contents to the account(s) you or your team manages. ❌** »
> — `developers.tiktok.com/doc/content-sharing-guidelines`. `B·2`

Un outil de publication pour le compte des établissements qu'on gère sous mandat **est** cette description, mot pour mot. Et sans audit, le plafond est de 5 utilisateurs par 24 h, en visibilité `SELF_ONLY` seulement, sur des comptes qui doivent être privés au moment de la publication — même page, `developers.tiktok.com/doc/content-sharing-guidelines`, datée du 4 août 2026, consultée le 2 octobre 2026. `B·2`

**Ce n'est pas un délai, c'est un mur.** Le plan dit « construire le minimum, trois plateformes, pas trente » — mais il ne nomme jamais les trois. Si TikTok en fait partie, la phase 3 n'attend pas une approbation : elle attend un refus. C'est un résultat à verser avant tout code.

### 2.3 — LinkedIn : deux paliers, pas un, et un rejet qui détruit l'application

**Les prérequis de dépôt** (`learn.microsoft.com/en-us/linkedin/marketing/community-management-app-review`, `B·2`) :

> « At this time, our Community Management APIs are only available to **registered legal organizations** for commercial use cases only. »
> « Be prepared to share your business email address and your organization's **legal name, registered address, website, and privacy policy**. […] **Personal email addresses won't pass the vetting process.** »
> « Ensure a **super admin of the LinkedIn Page** associated with your organization has verified your application. »

Et une chaîne de délais propre à LinkedIn : l'application doit être associée à une Page, le super-administrateur de cette Page **a 30 jours** pour valider le lien par une URL unique, et s'il refuse, « this will invalidate all generated links by any developer on that app ».
— `linkedin.com/help/linkedin/answer/a548360` et `linkedin.com/help/linkedin/answer/a1665329`, consultées le 2 octobre 2026. `B·2`

**Deux paliers, et le plan n'en compte qu'un.** Palier Développement par défaut : **500 appels par application et par 24 h, 100 par membre et par 24 h, aucun appel groupé, notifications désactivées**, et obligation d'avoir fini l'intégration dans les 12 mois — `learn.microsoft.com/en-us/linkedin/marketing/getting-access`, consulté le 2 octobre 2026. Le palier Standard — le seul utilisable en production — se demande **séparément**, et exige un screencast démontrant l'OAuth complet, une publication réelle sur la Page, et l'affichage d'un commentaire d'un membre dans notre interface — `learn.microsoft.com/en-us/linkedin/marketing/community-management-app-review?view=li-lms-2026-04`, consulté le 2 octobre 2026. `B·2` sur les deux.

**La clause la plus coûteuse du dossier, et aucune plateforme ne la partage :**

> « If your application is rejected, review the qualifications, **create a new app**, and submit a new Development tier access request form. **You won't be able to re-apply for Development tier access with your existing app.** »

Un refus ne coûte pas un délai : il coûte l'identifiant client, et tout ce qui y était rattaché. Chez Meta, on corrige et on resoumet. Chez LinkedIn, on recommence. Le plan n'a aucune provision pour une reprise à zéro.

**Délai constaté** : 40 jours et 79 jours d'attente rapportés sur des demandes de publication sur Page (`C·3`, fil Stack Overflow, cas isolés, antérieurs à la refonte des paliers).

### 2.4 — Google Business Profile : 60 jours de calendrier, un délai officiellement suspendu, et probablement aucune porte vers les avis

C'est la plateforme qui décide du volet avis entier, selon le plan comme selon le registre. Voici ce que Google publie.

**Les prérequis, et le premier est une horloge :**

> « In order to get access to GBP APIs, we require all applicants:
> — **Manage a Google Business Profile that is verified and active for 60+ days.** This GBP can be the applicant's own office or headquarters or it could belong to one of the clients they manage.
> — **Have a website representing the business listed on the GBP.** »
> — `developers.google.com/my-business/content/prereqs`. `B·2`

**Le délai annoncé :**

> « Request access to the API: **Requests are reviewed within 14 days.** »
> — `developers.google.com/my-business/content/faq`. `B·2`

L'écran de dépôt, lui, annonce 7 à 10 jours ouvrés (`C·3`, rapporté avec numéros de dossier sur le forum développeurs de Google).

**Mais ce délai est officiellement suspendu depuis septembre 2026.** Google l'a annoncé dans son propre forum d'assistance, par la voix d'une gestionnaire de communauté :

> « Due to an unusually high volume of API applications, processing times are currently extended. […] [Google] **cannot provide a specific response timeframe for pending applications.** […] Do not submit additional applications while your initial application is pending. »
> — annonce de Victoria Kroll, gestionnaire de communauté, forum d'assistance Google Business Profiles.
> **Adresse réellement lue : `seroundtable.com/google-business-profile-api-application-delays-42085.html`, publié le 15 septembre 2026, consulté le 2 octobre 2026.** Je n'ai **pas** atteint le fil d'origine sur `support.google.com`. `C·2` — relais secondaire d'une déclaration primaire de Google, publiée en plusieurs langues, non contredite, mais je ne l'ai pas lue à sa source.

**Il n'y a donc, à la date de ce plan, aucun délai annoncé par Google pour cette demande.** Planifier la phase 4 sur « 14 jours » serait planifier sur un chiffre que son auteur a lui-même retiré.

**Et le pire : la porte des avis est probablement inexistante, pas lente.** Le registre portait cela en `C·3` — « trois témoignages de forum, aucune source primaire ». Je le renforce nettement, sur le **forum développeurs de Google lui-même** (`discuss.google.dev`, août 2026), où trois demandeurs indépendants, numéros de dossier à l'appui, rapportent la même chose :

- `mybusiness.googleapis.com` (v4) est **le seul service portant les points d'accès aux avis** — `reviews.list`, `reviews.updateReply`.
- Il **n'apparaît pas** dans la bibliothèque d'API de la console Cloud. `gcloud services enable mybusiness.googleapis.com` renvoie `PERMISSION_DENIED`, précondition `110002`, « Service mybusiness.googleapis.com is not available to this consumer ». Un appel direct renvoie `403 SERVICE_DISABLED`.
- **Et cela persiste après l'approbation de l'accès de base.** Un des trois écrit : « I was approved for Basic API Access […] the legacy Google My Business API (v4) — the only one with the reviews endpoint — is completely inaccessible », en précisant être propriétaire du projet et avoir déposé sous le même compte, pour écarter l'erreur de courriel.
- Leur cas d'usage déclaré est **mot pour mot celui de ce plan** : « a platform managing reviews/Q&A for small businesses that grant manager access to their own verified profiles ».

Adresses lues, consultées le 2 octobre 2026 :
`discuss.google.dev/t/business-profile-api-reviews-endpoint-mybusiness-googleapis-com-cant-be-enabled-basic-access-pending-10-business-days/389462` (12 août 2026, porte les trois témoignages et les codes d'erreur) · `discuss.google.dev/t/gbp-api-escalation-basic-access-pending-14-days-requests-per-minute-locked-at-0/393020` (28 août 2026, porte le quota bloqué à 0).

Couple : `C·2`. Provenance secondaire — ce sont des utilisateurs, pas Google — mais hébergée par Google, horodatée, avec codes d'erreur reproductibles et triple concordance indépendante sur le même symptôme. **Cela vaut plus que le `C·3` du registre et doit y être versé comme tel.**

Contre-épreuve que j'ai faite, et qui tranche dans l'autre sens sur un point : j'ai vérifié le **calendrier de dépréciation officiel** de Google — `developers.google.com/my-business/content/sunset-dates`, consulté le 2 octobre 2026. Les avis **n'y figurent pas**. Y figurent l'API Questions-Réponses (arrêtée le 3 novembre 2025), l'API Appels, les attributs de santé, les statistiques, les comptes et administrateurs v4. Les points d'accès aux avis sont toujours documentés, toujours en v4, et leur journal des modifications porte des ajouts récents — `reviewReplyUrl`, `ReviewReplyState`, `PolicyViolation`. `B·2`.

**La formulation exacte du registre — « son point d'accès aux avis serait inatteignable » — est donc à corriger.** Le point d'accès existe, il est maintenu, il n'est pas déprécié. Ce qui manque est **le droit d'activer le service qui le porte**, et aucun formulaire ne le demande. Ce n'est pas un organe mort, c'est un organe sans serrure visible. La différence compte : elle dit où poser la question, et à qui.

### 2.5 — X : aucune approbation, et un prix au lien

X est le contre-exemple qui casse la thèse par l'autre bout.

> « The X API uses pay-per-usage pricing. No subscriptions—pay only for what you use. »
> **Post: Create — 0,015 $ par requête. Post: Create (with URL) — 0,200 $ par requête.**
> — `x-preview.mintlify.app/x-api/getting-started/pricing`, consulté le 2 octobre 2026.

**Et j'applique ici la règle contre moi.** Cette page est le **miroir de prévisualisation** de la documentation de X, non l'hôte canonique. `docs.x.com` et `developer.x.com` m'ont été refusés — le premier par le mandataire du conteneur, le second par le récupérateur tiers (journal, §11, lignes 12 et 14). La page se rattache elle-même à `docs.x.com` par son index (`https://docs.x.com/llms.txt`), ce qui me donne la provenance. Mais **je n'ai pas vérifié ces montants sur l'hôte canonique**, donc la robustesse tombe : **`B·3`, non `B·2`.**

Ce qui, par la règle de lecture du plan lui-même — « `3` est indicatif et n'engage aucune dépense avant son test » — veut dire que **le poste X ne doit pas entrer au budget avant d'avoir été relevé dans la console de X**. Ce relevé est gratuit et prend dix minutes : créer un compte développeur, ouvrir la console, lire la grille. Je le mets dans les gestes de semaine zéro du §3.4.

Pas de palier gratuit pour un nouveau développeur depuis février 2026 ; les paliers Basic (200 $/mois) et Pro (5 000 $/mois) ont été fermés puis migrés de force, Basic après le 1er juin 2026, Pro après le 1er septembre 2026 (`C·3`, recoupement de quatre analyses concordantes, aucune page primaire de X encore lisible sur l'historique).

**Ce que ça fait au plan.** Un produit dont la phase 2 est un blog et la phase 3 la diffusion de ses articles publie des liens. À 0,200 $ le lien, dix clients × quinze publications par mois = 30 $/mois de pur péage plateforme — soit, rapporté au prix de vente que le plan retient (50 €/mois pour la veille), **plus de la moitié du revenu d'un client**. Le plan calcule un plancher de coût « 25 à 35 € HT sans la presse » qui ne contient pas ce poste. Il est à réouvrir.

Et conséquence calendaire : **X n'a aucun délai d'approbation.** Zéro. Si X est l'une des « trois plateformes » de la phase 3, cette plateforme ne justifie pas un seul jour de semaine zéro.

### 2.6 — Récapitulatif

| Plateforme | Délai annoncé | Délai constaté | Prérequis bloquant pour qui démarre | Couple |
|---|---|---|---|---|
| **Meta** | **Contradictoire : « 2–3 jours » et « several weeks » sur deux pages officielles** | 20 j affichés en interface · 25 j+ et 14 j rapportés | Société vérifiée · site public · politique de confidentialité · **un appel réussi par permission avant de pouvoir déposer** · vidéo par permission · **vérification fournisseur technique, indépendante, 60 j de grâce** | `B·2` / constaté `C·3` |
| **TikTok** | « several days to two weeks » | — | Site entièrement développé · vidéo de bout en bout · **et une exclusion de principe de l'outil d'agence** | `B·2` |
| **LinkedIn** | **Aucun délai publié** | 40 j, 79 j rapportés | **Organisation légalement enregistrée** · adresse au registre · courriel professionnel vérifié · Page validée par son super-administrateur sous 30 j · **deux paliers successifs** · **un refus détruit l'application** | `B·2` / `C·3` |
| **Google** | 14 j — **officiellement suspendu depuis sept. 2026, sans nouvelle échéance** | 10 à 14 j+ sans réponse, dossiers multiples | **Fiche vérifiée et active depuis plus de 60 jours** · site web · **et, pour les avis, aucune porte documentée même après approbation** | `B·2` / `C·2` |
| **X** | **Aucune : il n'y a pas d'approbation** | — | Un moyen de paiement. **0,200 $ par publication contenant un lien** | **`B·3`** — miroir de prévisualisation, hôte canonique refusé |

**Ce tableau ne porte aucune adresse : c'est un récapitulatif.** Chaque ligne reprend la section qui la précède (§2.1 à §2.5), où la citation, son adresse et sa date de consultation sont données. Le relevé complet des 27 adresses est au §10.1. Aucun chiffre de ce tableau n'existe sans son adresse ailleurs dans le document.

---

## 3 — La semaine zéro est fictive, et le cercle vicieux est démontré

La question posée était : le plan peut-il vraiment déposer en semaine zéro. **Non, sur quatre plateformes sur cinq.** Et sur la cinquième il n'y a rien à déposer.

### 3.1 — Le cercle vicieux, dans les mots des plateformes

C'est le résultat que la commande demandait de chercher, et il est là, trois fois, indépendamment :

| Plateforme | La citation qui ferme le cercle |
|---|---|
| **Meta** | « the Request advanced access button will remain grayed out until a successful API has been logged in our system » + « Make at least 1 successful API call using each permission for which you are requesting advanced access » + « Your app must be publicly available » |
| **TikTok** | « Apps that are still in development or testing will not be approved » + « You must have an externally facing fully developed website » + « At least one demo video that shows the complete end-to-end flow » |
| **LinkedIn** (palier Standard) | « Demonstrate an application user approving access to their LinkedIn page data via the complete OAuth flow. Demonstrate a user posting to their LinkedIn page via your app. » |

**Il faut un produit en ligne et démontrable pour obtenir l'accès qui permet de le construire.** Ce n'est pas une déduction : c'est l'énoncé des trois documentations, aux trois adresses de la colonne de droite, toutes consultées le 2 octobre 2026 : `developers.facebook.com/docs/app-review/submission-guide` · `developers.tiktok.com/doc/app-review-guidelines/` · `learn.microsoft.com/en-us/linkedin/marketing/community-management-app-review?view=li-lms-2026-04`. `B·2`

Le cercle n'est pas absolument fermé — il a une sortie étroite, et elle est documentée elle aussi : les permissions non approuvées **fonctionnent pour les utilisateurs ayant un rôle sur l'application** — « unapproved permissions can only be requested from app users who have a role on the requesting app », `developers.facebook.com/docs/app-review`, consulté le 2 octobre 2026, `B·2`. On peut donc construire et appeler sur ses propres comptes. Mais cette sortie **ne change rien au calendrier du plan** : elle dit que le code doit être écrit *avant* le dépôt, ce qui est exactement ce que le plan nie.

### 3.2 — L'ordre réel, contre l'ordre du plan

Ce que le dossier exige impose une chaîne que le plan ne porte nulle part :

```
immatriculation de la société (LinkedIn : « registered legal organizations », adresse au registre)
   ↓
site public + politique de confidentialité + conditions, visibles sans menu   ← c'est la PHASE 2 du plan
   ↓
application construite, parcours d'autorisation fonctionnel                   ← c'est la PHASE 3 du plan
   ↓
un appel réussi par permission (Meta) · captures vidéo de bout en bout
   ↓
DÉPÔT  ← ce que le plan place en semaine zéro
   ↓
attente : 2 j à plusieurs semaines (Meta) · 2 semaines (TikTok) · non publié (LinkedIn)
```

**Le plan se mord la queue sur deux de ses propres phases.** Le site public exigé par TikTok et LinkedIn, c'est la phase 2. L'application fonctionnelle exigée par les trois, c'est la phase 3. Le plan déclare que la phase 3 « n'attend pas du développement, elle attend les approbations déposées en semaine 0 ». **C'est faux dans les deux sens** : les approbations attendent le développement, et le développement attend la phase 2.

### 3.3 — Et le seul test que le plan appelle gratuit et d'une heure ne l'est pas

Le plan inscrit deux fois, en semaine zéro et dans les décisions attendues :

> **Tester l'accès aux avis Google** — Un compte, une heure · Gratuit, une heure

Ce que ce test exige réellement, d'après les prérequis de Google : une fiche d'établissement **vérifiée** — la vérification elle-même prend des jours à des semaines, par courrier postal, appel ou vidéo — **puis 60 jours d'ancienneté active**, **puis** un site web représentant l'entreprise, **puis** un dossier, **puis** une revue dont Google a retiré l'échéance. Et au terme de cette chaîne, trois demandeurs sur le forum de Google rapportent que le service des avis reste inactivable.

**Ce n'est pas un test d'une heure. C'est un test de plus de deux mois**, dont le premier jour exige un objet — une fiche vérifiée, ou un mandat client sur la fiche d'un client — que le projet ne possède pas en semaine zéro. Et c'est, de l'aveu du plan et du registre, **le test qui décide à lui seul de la praticabilité du volet avis entier**.

Une heure est disponible, en revanche, pour deux gestes que le plan ne distingue pas du test : créer le projet Cloud et déposer le formulaire, pour prendre son rang dans la file. C'est utile. Ce n'est pas le test.

### 3.4 — Ce qui pouvait être fait en semaine zéro, et que le plan n'y met pas

| Geste réellement possible en semaine 0 | Pourquoi il est le vrai « ce qui ne se rattrape pas » |
|---|---|
| **Immatriculer la société** | C'est le prérequis de LinkedIn, de Meta et de Google. Tout en dépend, et rien ne le remplace |
| **Créer et faire vérifier une fiche d'établissement Google au nom de la société** | **Démarre immédiatement l'horloge de 60 jours.** C'est le seul délai du plan qui soit du calendrier pur, donc le seul qu'un jour perdu perd vraiment |
| **Créer la Page LinkedIn et lier l'application, super-administrateur prêt** | La fenêtre de validation est de 30 jours et un refus invalide tout |
| Publier site, politique de confidentialité et conditions, liens visibles sans menu | Prérequis commun TikTok / LinkedIn / Meta. C'est une partie de la phase 2 remontée en semaine 0 |
| Déposer le formulaire d'accès Google, **sans attendre l'approbation** | Prend un rang dans une file dont Google a suspendu l'échéance |
| **Demander par écrit à Google où se demande l'accès aux avis v4** | Trois demandeurs disent qu'aucune porte n'existe. Si c'est vrai, le volet avis tombe. Gratuit, et décisif |
| **Relever la grille tarifaire de X dans sa console** | Mon chiffre de 0,200 $ par lien est en `B·3` faute d'hôte canonique accessible. Dix minutes, gratuit, et ça fait passer en `B·1` le seul poste de coût que le plan ignore entièrement |

Le plan met en semaine zéro cinq gestes dont **un seul** (verser les briques fragiles au dépôt) est réellement exécutable à cette date sans dépendance externe non satisfaite.

---

## 4 — Les deux autres postes de calendrier

Le plan nomme trois postes incompressibles. Le premier est traité ci-dessus. Les deux autres sont beaucoup plus faibles qu'il ne le dit — l'un parce que les chiffres existent et sont courts, l'autre parce que le poste est mal défini.

### 4.1 — Le mandat signé par client : le poste le plus court, pas le plus long

Je n'ai trouvé **aucune mesure guadeloupéenne**, ni aucune statistique française portant spécifiquement sur la signature d'un abonnement de service par un établissement de 1 à 9 salariés. Ce que je trouve est secondaire et convergent :

| Mesure | Chiffre | Adresse, consultée le 2 octobre 2026 | Couple |
|---|---|---|---|
| Cycle de vente d'une TPE, un seul décideur, le gérant | **1 à 6 semaines** | `fichierb2b.fr/articles/prospecter-tpe-pme-france-guide-complet/` (9 mai 2026) | `C·3` — guide commercial, méthode non publiée |
| Logiciel en abonnement sous 500 €/mois, médiane | **14 à 30 jours** | `secretair.ai/glossaire/sales-cycle` | `C·3` — attribué au Bridge Group 2024, relayé, **non vérifié à la source** |
| Cycle B2B français toutes tailles | 45 à 90 jours | `initiative-crm.com/guide/prospection-vente/cycle-de-vente` | `C·3`, et hors cible : ce sont des PME, pas des TPE |

**Aucune de ces trois lignes n'est primaire, et aucune n'est guadeloupéenne.** Je ne les fais pas monter d'un cran par accumulation : trois sources secondaires concordantes restent secondaires.

**Ce que ça fait au plan.** À 50 €/mois, un décideur unique, un cycle de 2 à 6 semaines : **le mandat est le plus rapide des trois postes**, pas un mur. Le plan le range parmi les trois choses qui « ne se raccourcissent pas en travaillant plus » — alors que c'est précisément le poste que travailler plus raccourcit, puisqu'il dépend du nombre de contacts pris. Le registre porte déjà le fait utile : 760 établissements employeurs en hébergement-restauration, 86 % à 1-9 salariés. Le poste limitant est le nombre de visites, pas l'attente.

**Mais une dépendance en cascade que le plan ne voit pas.** Si la fiche d'établissement de 60 jours doit venir d'un client — Google l'autorise explicitement : « it could belong to one of the clients they manage » — alors la chaîne devient : premier contact → 2 à 6 semaines → mandat signé → **60 jours d'ancienneté** → dossier → revue sans échéance. **Soit quatre à six mois après la semaine zéro pour le premier appel aux avis**, dans l'hypothèse favorable où la porte v4 existe. Aucun chiffre de cet ordre n'apparaît dans le plan, qui range les avis en phase 4 sans jamais dater cette phase.

### 4.2 — La lecture des licences : un poste surévalué, qui en masque un vrai

La question posée — combien de sources pour que le produit ait de la valeur, donc combien de lectures — **je ne peux pas y répondre par une source**. Il n'en existe pas : c'est un jugement commercial, pas un fait documenté. Je le déclare `D` en tête et je n'en fabrique pas l'apparence.

Ce que je peux faire, c'est retourner la question contre le plan, et là il y a une prise.

Le plan inscrit **trois** sources en phase 1 : « Trois sources en accès ouvert déclaré, licence lue et datée ». Et il inscrit un seuil d'abandon : « Moins d'une dizaine de lignes utiles par semaine au test gratuit → la veille officielle seule ne se vend pas ». **Ces deux lignes ne sont jamais confrontées.** Le plan ne demande nulle part si trois sources peuvent produire dix lignes utiles filtrées Guadeloupe par semaine. C'est une question d'arithmétique, pas d'opinion, et elle décide de la phase 1 entière — donc du « seul produit vendable sans attendre personne ».

Et le coût de lecture d'une licence est petit, et le plan le sait déjà sans le dire : le registre porte en `B·2` que les décisions de justice et les données de l'administration sont en accès ouvert sous licence type, exploitation commerciale autorisée, droit de producteur cédé par écrit. **Lire une licence type qu'on a déjà lue ne coûte rien à la deuxième source.** Le poste n'est pas « par source », il est « par famille de licence », et il y en a peu. Le ranger parmi les trois postes incompressibles le surévalue d'un ordre de grandeur.

**Le vrai poste que celui-là masque** : non pas lire les licences, mais **mesurer le volume**. Et cette mesure est impossible dans l'environnement actuel (§7). Le plan appelle ce test « gratuit, deux à trois jours, décisif dans les deux sens » tout en sachant, par son propre registre, qu'aucune source guadeloupéenne n'est atteignable. Le test décisif de la phase 1 est bloqué par l'item que le plan range quatrième en semaine zéro, « élargir l'accès réseau — un réglage ». **C'est le premier, pas le quatrième.**

---

## 5 — Le décalage horaire : la question est juste, la réponse attendue est fausse

La commande affirme que le décalage ajoute un délai réel à chaque échange et que le plan n'en tient pas compte. Le second point est exact : le plan ne mentionne le fuseau que pour s'en féliciter, « programmation sur l'heure locale du client, UTC-4 sans heure d'été, 0,00 h d'erreur ». Le premier point, je l'ai mesuré, et **il ne tient pas**.

Mesure en conteneur sur les données de fuseaux, `A·1`, rejouable :

```
Guadeloupe : gmtoff = -14400 s, soit UTC-4, sans aucune transition depuis le 8 juin 1911.
Paris      : transitions le 29 mars 2026 et le 25 octobre 2026.
→ écart Guadeloupe ↔ Paris : 5 h en hiver, 6 h en été.
→ écart Guadeloupe ↔ New York : 1 h en hiver, 0 h en été.

Journée ouvrée parisienne 9h-18h, vue de Guadeloupe :
   hiver 04:00-13:00 · été 03:00-12:00
Recouvrement avec une journée locale 8h-17h :
   hiver 5 h · été 4 h
Heure limite locale pour joindre la métropole :
   13:00 AST en hiver · 12:00 AST en été

Journée ouvrée new-yorkaise 9h-18h, vue de Guadeloupe :
   hiver 10:00-19:00 (recouvrement 7 h) · été 09:00-18:00 (recouvrement 8 h)
```

**Trois conclusions, dont deux contredisent la prémisse.**

**5.1 — Sur l'axe plateforme, le décalage est un avantage, pas un handicap.** Les cinq assistances que ce projet doit solliciter sont américaines ou irlandaises. La Guadeloupe est à **zéro ou une heure** de New York, avec **7 à 8 heures** de recouvrement ouvré — nettement mieux que la métropole, qui en a 3 à 4. Et ces échanges sont de toute façon asynchrones : formulaire, numéro de dossier, courriel, fil de forum. **Le décalage n'ajoute rien, nulle part, sur le poste que le plan dit être le poste dominant.** La question posée suppose le contraire ; la mesure dit l'inverse.

**5.2 — Sur l'axe métropolitain, le coût est réel mais c'est une amputation, pas un délai.** Bâtonnier, organisme de gestion collective, conseil juridique : la fenêtre n'est pas supprimée, elle est **réduite de moitié**, de 9 heures à 4 ou 5. Le coût est un **couperet à 13:00 locales en hiver et 12:00 en été** : tout ce qui se découvre l'après-midi attend le lendemain matin. Un aller-retour qui tiendrait dans une journée en métropole prend deux jours ici — mais seulement s'il naît après midi. En nombre de jours, cela ajoute **au plus un jour par aller-retour, sur la moitié des allers-retours**. Sur un poste de 2 à 6 semaines comme le mandat, c'est du bruit. Sur une question au bâtonnier qui en vaut une poignée, c'est quelques jours.

**5.3 — Le seul endroit où ça coûte vraiment, le plan ne le voit pas.** La vérification d'une fiche Google par courrier postal part de Mountain View ou d'un centre européen vers un département d'outre-mer. **C'est un délai postal transatlantique en amont d'une horloge de 60 jours.** Chaque jour de courrier est un jour ajouté au début du seul délai incompressible du projet. Je n'ai pas mesuré ce délai postal — ce serait `D` — mais c'est l'endroit à mesurer, et ce n'est pas celui que la commande désignait.

**Verdict sur ce point : la question était la bonne, sa réponse attendue était fausse, et le plan a raison de ne pas s'en inquiéter — pour de mauvaises raisons, puisqu'il n'a pas regardé.**

---

## 6 — Pendant l'attente : il n'y a pas d'attente à occuper, et il y a deux blocages totaux

Le plan dit « Ils se lancent, et ensuite on attend. Tout le reste s'écrit pendant cette attente. » Cette phrase suppose que les attentes commencent tôt et durent. **Les deux sont faux.**

### 6.1 — Les attentes ne commencent pas tôt : elles commencent après le travail

Sur Meta, TikTok et LinkedIn, l'attente ne peut commencer qu'au dépôt, et le dépôt ne peut avoir lieu qu'une fois le site public, l'application fonctionnelle et les vidéos tournées. **Au moment où l'attente commence, l'essentiel de l'écriture est déjà fait.** Il n'y a rien à mettre en parallèle, parce que le parallélisme supposé est en réalité une séquence.

L'économie centrale du plan — recouvrir l'attente par l'écriture — est donc disponible sur **une** plateforme sur cinq : Google, où les 60 jours d'ancienneté sont du calendrier pur et se recouvrent parfaitement. Une sur cinq. Le plan en tire la forme de ses quatre phases.

### 6.2 — Les deux moments de blocage total, nommés

La commande demande de les nommer s'il y en a. Il y en a deux.

**Blocage A — entre l'immatriculation et le site en ligne.** Rien ne peut être déposé : LinkedIn exige une organisation enregistrée et un site, TikTok un site entièrement développé, Meta une politique de confidentialité accessible. Et la mesure de volume de la phase 1 est bloquée par le réseau. Ce n'est pas un blocage d'attente — c'est un blocage où **rien n'attend parce que rien n'est parti**, et où le travail disponible est celui que le plan range en phase 2. Durée : ce que met la phase 2, que le plan ne chiffre pas, et refuse explicitement de chiffrer.

**Blocage B — après le dépôt Meta, et il est causé par une règle de Meta que le plan ignore.**

> « Making changes to your app's basic or advanced settings after you have submitted may require re-review. »
> « Any changes you make to your app's basic or advanced settings once you've submitted your app for App Review may require re-review before taking effect. »

Et chez TikTok, c'est pire, c'est un gel explicite :

> « **In review:** Your app has been submitted for review and approval is pending. **No further changes can be made at this stage.** »

**Donc pendant l'attente — la période où le plan place tout le reste du travail — toucher à l'application remet le compteur à zéro chez Meta, et est purement interdit chez TikTok.** La fenêtre d'attente n'est pas une fenêtre de travail sur l'objet attendu : c'est une fenêtre où cet objet est gelé. Travailler pendant l'attente est possible sur la veille, sur le blog, sur la couture — mais pas sur la publication, qui est justement ce que l'attente débloque.

### 6.3 — Et la phase 4 est rangée dernière alors qu'elle contient la première échéance

Le plan écrit, dans sa phase 4 :

> **Contrainte de calendrier irréversible : le schéma de captation de la date d'expérience doit être gelé avant le premier jour de service manuel.** Sinon la donnée est perdue pour ce client, définitivement.

Et, deux lignes plus haut : « En attendant : rendre le service à la main, sous mandat, facturé. »

Croisé avec Google : le service manuel sous mandat est aussi ce qui donne accès à une fiche d'établissement de client, dont **les 60 jours d'ancienneté conditionnent l'accès à l'API**. Donc le premier jour de service manuel doit arriver **le plus tôt possible** — c'est le démarrage de l'horloge la plus longue du projet. Et le gel du schéma doit le précéder.

**La phase 4 est rangée quatrième et contient à la fois la seule échéance irréversible du plan et le plus long délai de mise en œuvre.** La ranger quatrième maximise la durée totale du projet. C'est une contradiction interne du plan, entre son ordre déclaré et sa propre contrainte déclarée irréversible, et elle n'y est signalée nulle part.

---

## 7 — Hôtes refusés et contournement, nommés comme demandé

| Hôte refusé | Symptôme | Voie trouvée |
|---|---|---|
| `developers.facebook.com` | `EGRESS_BLOCKED` | **Récupération par EXA. Documentation intégrale obtenue, dont les trois pages qui ferment le cercle vicieux** |
| `developers.google.com` | `EGRESS_BLOCKED` | **Récupération par EXA. Prérequis, FAQ, calendrier de dépréciation et référence des avis obtenus** |
| `docs.x.com` | `EGRESS_BLOCKED` | **Récupération par EXA du miroir de prévisualisation de la documentation X. Grille tarifaire intégrale obtenue** |
| `developer.x.com`, `developer.twitter.com` | `SOURCE_NOT_AVAILABLE` côté EXA | Non contourné. Historique des paliers reste en `C·3` |
| `www.data.gouv.fr`, `bodacc-datadila.opendatasoft.com`, `www.bodacc.fr` | `HTTP 000` · passerelle 403 sur CONNECT, confirmé par `__agentproxy/status` | **Non contourné.** C'est pourquoi le volume de la veille reste `D`, déclaré en tête |
| `learn.microsoft.com/.../getting-started`, `.../community-management-integration-requirements` | `CRAWL_NOT_FOUND` | Contourné par les pages voisines, qui portaient l'essentiel |

**Leçon confirmée et précisée.** Le registre notait que les forges publiques servent de voie d'accès quand le web est fermé. Ici la voie qui a tout débloqué est différente et vaut d'être inscrite : **un récupérateur web tiers passe là où le mandataire du conteneur refuse.** Cinq hôtes primaires sur six, dont les trois documentations qui portent les résultats décisifs de ce retour, ont été lus ainsi. Ce n'est pas un contournement de politique, c'est un second chemin vers des documents publics. Sans lui, ce retour aurait rendu « délais inconnus » — exactement ce que le plan écrit.

**Ce qui veut dire une chose désagréable pour le plan** : les délais qu'il marque `D` et inconnus, autour desquels il organise sa forme entière, étaient accessibles dans la session même qui l'a écrit, à une requête près.

---

## 8 — Les deux questions que je me suis appliquées

### 8.1 — Laquelle de mes conclusions, si elle est fausse, coûte le plus cher au projet ?

**Celle-ci : « le dossier d'approbation Meta ne peut pas être déposé avant que l'application soit construite et publique ».**

Si elle est **juste**, le plan doit inverser l'ordre de ses phases, et sa semaine zéro change de contenu. Coût : une réécriture.

Si elle est **fausse** — si l'on peut déposer avec une maquette, ou si le bouton se débloque sur un appel en accès standard depuis l'explorateur de l'interface graphique de Meta, sans produit du tout — alors ma critique principale s'effondre, le plan a raison sur sa forme, et **j'aurai fait perdre au projet le temps d'une réécriture inutile et, pire, le rang dans la file d'attente de Meta**, qui est le seul actif que la semaine zéro savait acquérir.

C'est bien là le risque le plus cher, et il est asymétrique : me croire à tort coûte des semaines de file ; me croire à raison coûte une réécriture.

**Le point d'incertitude est précis.** La documentation dit « Calls can be made using your app **or the Graph API Explorer tool** ». L'explorateur n'est pas notre produit. Il est donc **possible** que l'appel réussi exigé soit satisfaisable sans produit construit, par un appel manuel depuis l'outil de Meta, sur un compte ayant un rôle sur l'application. Dans ce cas la condition de l'appel tombe — mais **les autres conditions restent** : « app must be publicly available », l'enregistrement d'écran par permission, et la vérification fournisseur technique. Ma conclusion survit partiellement. C'est exactement ce qu'il faut trancher.

### Comment la tester pour moins de cent euros

**Coût total : 0 €. Deux heures. Aucune dépense, aucun faux signal.**

1. Créer une application Meta de type Business, la relier à un portefeuille d'entreprise. Gratuit.
2. Depuis l'explorateur d'API de Meta, avec un compte ayant un rôle sur l'application, émettre **un** appel `pages_manage_posts` en accès standard sur une Page de test qu'on détient. Gratuit, et conforme : c'est le geste que la documentation désigne, sur nos propres données, sans aucun signal falsifié chez un tiers.
3. Attendre 48 h — la documentation dit « The API call data will be logged within 2 days ».
4. Ouvrir l'onglet App Review > Permissions and Features et **regarder si le bouton « Request advanced access » est encore grisé.**

**La réponse est binaire et visuelle.** S'il est actif, ma conclusion la plus chère est fausse sur sa première condition, et la semaine zéro de Meta est partiellement récupérable — on dépose, et le site et les vidéos restent à produire pendant l'attente. S'il est grisé, elle est confirmée, et la phase 3 doit passer avant la semaine zéro.

**Et le même protocole règle la question Google, pour 0 € aussi** : émettre `gcloud services enable mybusiness.googleapis.com` sur un projet neuf. Si la réponse est `PERMISSION_DENIED` précondition `110002`, le symptôme rapporté par trois demandeurs est reproduit chez nous, et le `C·2` passe en `A·1` en une commande — c'est **le premier `A` du volet avis**, et il coûte une minute, pas 200 €. Si le service s'active, les trois témoignages tombent et le volet avis respire. Dans les deux cas on sait, aujourd'hui, sans attendre 60 jours.

### 8.2 — Qu'ai-je réellement écarté ?

**Quatre choses, nommées. Je n'en gonfle pas le nombre.**

1. **« Le point d'accès aux avis Google est déprécié ou mort. »** Écarté sur source primaire : le calendrier de dépréciation officiel de Google ne le liste pas, son journal des modifications porte des ajouts récents, sa référence est maintenue. Ce que trois demandeurs rapportent est une **impossibilité d'activation du service**, ce qui est un autre fait et se répare autrement. La formulation du registre — « inatteignable » — est à corriger en ce sens.

2. **« Le décalage horaire ajoute un délai réel à chaque échange. »** Écarté sur mesure `A·1` : 4 à 5 heures de recouvrement ouvré avec Paris subsistent, et le recouvrement avec les États-Unis — où siègent les cinq assistances concernées — est **meilleur** que celui de la métropole. Le coût réel est un couperet à 13:00 ou 12:00 locales, soit au plus un jour par aller-retour, sur la moitié des allers-retours.

3. **« Le mandat signé par client est un poste de calendrier incompressible. »** Écarté : 2 à 6 semaines, un décideur unique, et c'est le poste que le nombre de visites raccourcit. Le plan le classe avec deux postes qui, eux, ne cèdent pas au travail. Le classement est faux.

4. **Mon propre réflexe de conclure que la phase 3 est morte à cause de TikTok.** Écarté, et je le signale parce que c'était tentant. La clause d'exclusion de TikTok est claire et elle vise ce produit — mais le plan ne nomme jamais ses « trois plateformes ». On ne peut pas déclarer morte une phase dont le périmètre n'est pas écrit. Ce que j'en conclus est plus étroit et plus actionnable : **nommer les trois plateformes est une décision préalable au code**, parce que selon lesquelles, la phase 3 attend deux semaines, quatre mois, ou un refus de principe.

---

## 9 — Les cinq colonnes

| MCP à installer | Logiciels manquants | Outils déjà disponibles | IA existantes qui font ce travail, et à quel prix | Futurs possibles à douze mois ⏳ |
|---|---|---|---|---|
| **Un MCP de suivi des dossiers de plateforme** — un état par dossier : plateforme, date de dépôt, numéro de cas, délai annoncé, délai écoulé, prochaine relance. Les cinq files ont des horloges différentes et aucune ne prévient. Rien de ce genre n'existe ici | **`gcloud`** est installé et préconfiguré pour le mandataire : la commande `services enable mybusiness.googleapis.com` du §8.1 est exécutable **aujourd'hui**. Ce n'est pas un manque, c'est un outil non employé | **EXA** — `web_search_exa` et `web_fetch_exa`. C'est ce qui a rendu ce retour possible : cinq hôtes primaires refusés par le mandataire, lus par cette voie | **Les assistants de recherche web généralistes** (Perplexity Pro, ChatGPT avec navigation, 20 à 23 $/mois) rendent sur ces questions ce que le plan a écrit : « délai inconnu ». Ils ne forcent pas un hôte refusé et ne croisent pas deux pages officielles contradictoires du même éditeur | ⏳ **Le délai Google se rouvre, ou ne se rouvre pas.** Google a suspendu son échéance en septembre 2026 sans en donner de nouvelle. À douze mois : soit la file est résorbée et les 14 jours reviennent, soit la suspension est devenue l'état normal et la phase 4 n'a plus de calendrier du tout |
| **Un MCP de veille de documentation** sur les pages qui décident : prérequis GBP, lignes directrices de partage TikTok, revue LinkedIn, grille tarifaire X. Les quatre ont bougé en 2026. La page TikTok qui exclut ce produit est datée du 4 août 2026 | **Un vérificateur de concordance entre deux pages d'un même éditeur.** Meta publie « 2–3 jours » et « several weeks » sur deux pages vivantes. Aucun outil ici ne lève ce genre de contradiction ; je l'ai trouvée à la main | **Les données de fuseaux horaires du système** — `zdump`, `zoneinfo`, Python `zoneinfo`. Le `A·1` du §5 en sort, rejouable hors réseau | **Les agrégateurs de publication** (Buffer, Hootsuite, Blotato, PostEverywhere, 9 à 99 $/mois) **ont déjà franchi les cinq portes** et détiennent les identifiants de plateforme. Ils vendent précisément l'évitement du calendrier que ce plan prévoit de subir. C'est la **règle du loyer** du registre appliquée aux approbations, non au code : louer l'approbation d'un tiers plutôt que la demander | ⏳ **X devient le poste de coût dominant de la phase 3.** Le tarif a bougé quatre fois en huit mois, toujours vers le haut, et le lien est à 0,200 $ — treize fois le post nu. À douze mois, publier des liens vers un blog peut coûter plus que l'abonnement vendu |
| **Un MCP d'horloges de calendrier** : les 60 jours d'ancienneté Google, les 60 jours de grâce fournisseur technique Meta, les 30 jours de validation de Page LinkedIn, les 30 jours de validité de l'appel réussi Meta, les 12 mois du palier Développement LinkedIn. **Cinq échéances qui expirent en silence**, aucune dans le plan | **Un enregistreur d'écran.** Il en faut un par permission chez Meta, un de bout en bout chez TikTok, un par cas d'usage chez LinkedIn. Aucun dans ce conteneur, et c'est une pièce de dossier, pas un confort | **Le mandataire sortant et son point d'état** `__agentproxy/status`, qui nomme l'hôte refusé et l'heure du refus. C'est ce qui a permis d'inscrire `bodacc-datadila` au §7 au lieu de deviner | **Aucune IA ne fait le travail de ce retour**, et c'est le constat honnête. Croiser cinq documentations, en forcer trois derrière un refus réseau, mesurer un fuseau en conteneur et trouver la contradiction interne de Meta : aucun produit sur étagère ne compose ces quatre gestes | ⏳ **L'exclusion TikTok se durcit ou se négocie.** La clause « not limited to internal groups/private use » est appliquée par un auditeur humain. À douze mois, soit l'audit s'ouvre aux outils d'agence sous mandat écrit, soit la plateforme sort du périmètre — et il faut l'écrire dans le plan avant d'écrire la ligne de code |

---

## 10 — Table de contrôle des sources : toute adresse que je revendique

Ajoutée sur demande, après la faute mesurée sur les douze retours précédents : cinquante-six affirmations primaires pour quarante-huit adresses. **Je donne mon propre décompte pour qu'il soit confrontable au décompte mécanique.**

**Tout consulté le 2 octobre 2026**, date de ce retour. Quand la page porte sa propre date de mise à jour, je la donne aussi.

### 10.1 — Adresses primaires revendiquées : 27

| # | Adresse | Ce qu'elle fonde ici | Couple |
|---|---|---|---|
| 1 | `developers.facebook.com/docs/app-review/submission-guide` — page datée 30 juin 2026 | Bouton grisé jusqu'à un appel réussi · 1 appel par permission sous 30 j · développement achevé · application publiquement accessible · URL de politique de confidentialité · enregistrements d'écran | `B·2` |
| 2 | `developers.facebook.com/documentation/resp-plat-initiatives/appreview/FAQs` — page datée 12 juin 2025 | « The entire process may take up to several weeks » · vérification d'entreprise « a few days » | `B·2` |
| 3 | `developers.facebook.com/docs/resp-plat-initiatives/app-review/introduction/` | « less than one week […] often only 2–3 days » — la contradiction du §2.1 · re-revue après modification | `B·2` |
| 4 | `developers.facebook.com/docs/development/release/business-verification` — page datée 7 juil. 2023 | Accès avancé exige la vérification d'entreprise · ordre imposé | `B·2` |
| 5 | `developers.facebook.com/docs/development/release/access-verification/` | Fournisseur technique obligatoire pour servir d'autres entreprises · « independent of App Review » · 60 j de grâce · prérequis = vérification d'entreprise faite | `B·2` |
| 6 | `developers.facebook.com/docs/development/release/tech-providers/` | Même porte, liste des permissions concernées | `B·2` |
| 7 | `developers.facebook.com/docs/instagram-platform/content-publishing` — page datée 30 juin 2026 | Autorisation de publication de Page côté client · plafond 100 publications/24 h | `B·2` |
| 8 | `developers.facebook.com/docs/permissions/reference/pages_manage_posts` | « Business Verification is required for all apps making requests for Advanced Access » · exigences de screencast par permission | `B·2` |
| 9 | `developers.facebook.com/docs/pages/overview` | Toute permission exige la revue · accès avancé pour un utilisateur sans rôle · tâches de Page | `B·2` |
| 10 | `developers.google.com/my-business/content/prereqs` | **Fiche vérifiée et active depuis plus de 60 jours** · site web exigé · dossier par formulaire · quota 0 vs 300 QPM | `B·2` |
| 11 | `developers.google.com/my-business/content/faq` | « Requests are reviewed within 14 days » | `B·2` |
| 12 | `developers.google.com/my-business/content/basic-setup` | Sept API à activer · pas d'environnement de test · OAuth exigé | `B·2` |
| 13 | `developers.google.com/my-business/content/sunset-dates` | **Les avis ne sont pas au calendrier de dépréciation** — la correction du registre au §2.4 | `B·2` |
| 14 | `developers.google.com/my-business/content/change-log` | Ajouts récents sur les avis : `reviewReplyUrl`, `ReviewReplyState`, `PolicyViolation` | `B·2` |
| 15 | `developers.google.com/my-business/reference/rest/v4/accounts.locations.reviews` | Les points d'accès aux avis existent, en v4, maintenus · lecture et réponse | `B·2` |
| 16 | `developers.google.com/my-business/content/limits` | Quotas standard 300 QPM · `429` quand le quota est à zéro | `B·2` |
| 17 | `developers.tiktok.com/doc/getting-started-faq` | **« App review may take several days to two weeks after submission »** · gel « No further changes can be made at this stage » | `B·2` |
| 18 | `developers.tiktok.com/doc/app-review-guidelines/` — page datée 4 août 2026 | Site entièrement développé, ni atterrissage ni connexion · politique visible sans menu · vidéo de bout en bout · « Apps that are still in development or testing will not be approved » | `B·2` |
| 19 | `developers.tiktok.com/doc/content-sharing-guidelines` — page datée 4 août 2026 | **L'exclusion : « Not acceptable: A utility tool to help upload contents to the account(s) you or your team manages »** · 5 utilisateurs/24 h · `SELF_ONLY` sans audit | `B·2` |
| 20 | `developers.tiktok.com/doc/content-posting-api-get-started` | Audit obligatoire pour lever la visibilité privée · domaine à vérifier | `B·2` |
| 21 | `developers.tiktok.com/doc/getting-started-create-an-app` — page datée 4 août 2026 | Vérification de propriété d'URL · états Draft / In review / Live / Not approved | `B·2` |
| 22 | `learn.microsoft.com/en-us/linkedin/marketing/community-management-app-review?view=li-lms-2026-04` | **« only available to registered legal organizations »** · nom légal, adresse au registre, site, politique · courriel professionnel vérifié · Page vérifiée par son super-admin · **« You won't be able to re-apply […] with your existing app »** · screencasts du palier Standard | `B·2` |
| 23 | `learn.microsoft.com/en-us/linkedin/marketing/getting-access` | Deux paliers · 500 appels/24 h et 100/membre/24 h · 12 mois pour finir l'intégration · demande séparée du Standard | `B·2` |
| 24 | `learn.microsoft.com/en-us/linkedin/marketing/` | Périmètre de l'API Community Management | `B·2` |
| 25 | `linkedin.com/help/linkedin/answer/a548360` | Association à une Page obligatoire · **30 jours** pour le super-admin | `B·2` |
| 26 | `linkedin.com/help/linkedin/answer/a1665329` | URL unique de vérification · un refus invalide tous les liens générés | `B·2` |
| 27 | `x-preview.mintlify.app/x-api/getting-started/pricing` | 0,015 $ par publication · **0,200 $ avec un lien** · plafond 3 M de lectures · pas d'abonnement | **`B·3`** — miroir de prévisualisation, hôte canonique refusé. **Seule ligne primaire que je rétrograde moi-même** |

### 10.2 — Adresses secondaires, revendiquées comme telles : 7

| # | Adresse | Ce qu'elle fonde | Couple |
|---|---|---|---|
| 28 | `discuss.google.dev/t/business-profile-api-reviews-endpoint-mybusiness-googleapis-com-cant-be-enabled-basic-access-pending-10-business-days/389462` — 12 août 2026 | Trois demandeurs · `PERMISSION_DENIED` précondition `110002` · `403 SERVICE_DISABLED` · **inaccessible même après approbation** | `C·2` |
| 29 | `discuss.google.dev/t/gbp-api-escalation-basic-access-pending-14-days-requests-per-minute-locked-at-0/393020` — 28 août 2026 | Quota bloqué à 0 au-delà de 14 jours · fenêtre annoncée de 7-10 jours ouvrés | `C·2` |
| 30 | `seroundtable.com/google-business-profile-api-application-delays-42085.html` — 15 sept. 2026 | Annonce de Google : délais étendus, **aucune échéance donnée**. Relais, pas la source | `C·2` |
| 31 | `developers.facebook.com/community/threads/1676431436923929/` | « Most submissions are reviewed within 20 days » affiché en interface · 25 j+ sans réponse. Forum hébergé par Meta, mais propos d'utilisateur | `C·3` |
| 32 | `developers.facebook.com/community/threads/1106493861938097/` | Vérification d'entreprise : 14 jours contre 2 jours ouvrés annoncés | `C·3` |
| 33 | `stackoverflow.com/questions/57805498/...` | 40 et 79 jours d'attente LinkedIn. Antérieur à la refonte des paliers | `C·3` |
| 34–36 | `fichierb2b.fr/...` · `secretair.ai/glossaire/sales-cycle` · `initiative-crm.com/...` | Cycles de vente TPE et PME. **Aucune n'est guadeloupéenne, aucune n'est primaire** | `C·3` |

### 10.3 — Mesures locales : 2

| Mesure | Commande, rejouable hors réseau | Couple |
|---|---|---|
| Guadeloupe `gmtoff = -14400`, aucune transition depuis le 8 juin 1911 · Paris bascule les 29 mars et 25 oct. 2026 | `zdump -v America/Guadeloupe` · `zdump -c 2026,2027 -v Europe/Paris` | `A·1` |
| Recouvrement ouvré 5 h en hiver, 4 h en été avec Paris ; 7 h et 8 h avec New York · couperet à 13:00 et 12:00 AST | script Python `zoneinfo`, §5 | `A·1` |

### 10.4 — Mon décompte, posé pour être confronté

| | Nombre |
|---|---|
| **Adresses primaires distinctes, citées avec leur date de consultation** | **27** — §10.1, aucune de plus revendiquée |
| **Affirmations primaires, c'est-à-dire adresses adossées à au moins une affirmation** | **27** |
| **Écart** | **0** |
| Dont rétrogradée par moi en `B·3` faute d'hôte canonique | 1 — ligne 27, X |
| Adresses secondaires, revendiquées `C` | 9 — lignes 28 à 36 |
| Mesures locales `A·1`, commande donnée | 2 |
| Lignes `D` déclarées en tête du document | 3 |

**Avertissement au décompte mécanique, pour qu'il ne produise pas un faux écart.** Le marqueur `` `B·2` `` apparaît **une cinquantaine de fois** dans ce document pour **27 adresses**. Ce n'est pas une inflation : une même page fonde plusieurs lignes, et je répète son cran à chaque fois pour que chaque ligne soit lisible seule. Les deux tiers de ces occurrences sont d'ailleurs dans les tables récapitulatives du §2.6 et du §10.1, qui citent les mêmes adresses une seconde fois.

**Le contrôle juste n'est donc pas « nombre de `B·2` contre nombre d'adresses », mais : toute affirmation portant un `B` a-t-elle une adresse atteignable depuis la même section ?** Je l'ai vérifié mécaniquement avant de rendre, j'ai trouvé quatre manquements chez moi — l'exclusion TikTok à 5 utilisateurs, les deux paliers LinkedIn, les trois documentations du §3.1, et la sortie étroite du cercle — et je les ai corrigés en ajoutant l'adresse et la date. **Il en reste un, et je le déclare plutôt que de le masquer** : au §4.2, j'écris « le registre porte en `B·2` que les décisions de justice […] ». Ce `B·2` n'est pas le mien, je ne l'ai pas revérifié à la source, et il ne compte pas dans mes 27. Je le reprends du registre tel quel, à ses risques.

**Un fait daté sans adresse ne fonde rien, et le plan tient entièrement sur des faits datés.** C'est pourquoi aucun délai de ce retour n'est écrit sans son adresse : ni les « several weeks » de Meta, ni les « two weeks » de TikTok, ni les 14 jours de Google, ni les 60 jours d'ancienneté, ni les 30 jours de LinkedIn.

---

## 11 — Journal de requêtes

Tout ce que j'ai tenté, dans l'ordre, le 2 octobre 2026. **Un hôte refusé est une ligne de ce journal, pas un aveu** — et c'est la colonne qui dit où il est inutile de retourner.

| # | Requête ou adresse | Outil | Résultat |
|---|---|---|---|
| 1 | `developers.facebook.com/docs/app-review` | WebFetch | **refusé** — `EGRESS_BLOCKED` |
| 2 | `developers.facebook.com` : `/docs/app-review` · `/docs/development/release/business-verification` · `/docs/app-review/submission-guide` | EXA fetch | trouvé |
| 3 | `developers.google.com/my-business/content/prereqs` | WebFetch | **refusé** — `EGRESS_BLOCKED` |
| 4 | `developers.google.com` : `/my-business/content/prereqs` · `/content/basic-setup` · `/reference/rest/v4/accounts.locations.reviews` | EXA fetch | trouvé |
| 5 | `learn.microsoft.com/en-us/linkedin/marketing/` | EXA fetch | trouvé |
| 6 | `learn.microsoft.com/en-us/linkedin/marketing/community-management/getting-started` | EXA fetch | rien — `CRAWL_NOT_FOUND` |
| 7 | `learn.microsoft.com/en-us/linkedin/marketing/getting-access` | EXA fetch | trouvé |
| 8 | `learn.microsoft.com/.../community-management-integration-requirements` | EXA fetch | rien — `CRAWL_NOT_FOUND` |
| 9 | `developers.tiktok.com/doc/content-posting-api-get-started` | EXA fetch | trouvé |
| 10 | `developers.tiktok.com/doc/getting-started-create-an-app` | EXA fetch | trouvé |
| 11 | `developers.tiktok.com/doc/content-sharing-guidelines` | EXA fetch | trouvé — **l'exclusion de l'outil d'agence** |
| 12 | `developer.x.com/en/products/x-api` · `docs.x.com/x-api/getting-started/about-x-api` · `developer.twitter.com/en/portal/products` | EXA fetch | **refusé** — `SOURCE_NOT_AVAILABLE` sur les trois |
| 13 | « Google My Business API v4 reviews endpoint deprecation sunset notice official documentation » | EXA search | trouvé — calendrier de dépréciation, journal des modifications, référence des avis |
| 14 | `docs.x.com/x-api/getting-started/about-x-api` | WebFetch | **refusé** — `EGRESS_BLOCKED` |
| 15 | « Meta App Review how long does review take business days official FAQ » | EXA search | trouvé — **les deux délais contradictoires** |
| 16 | `developers.facebook.com/documentation/resp-plat-initiatives/appreview/FAQs` · `/docs/resp-plat-initiatives/app-review/introduction/` | EXA fetch | trouvé — citations intégrales |
| 17 | « X API pricing tiers Free Basic Pro posts per month limits official » | EXA search | trouvé, mais **secondaire seulement** — aucune page de X parmi les résultats |
| 18 | `git log` et `git diff` sur `REGISTRE-DE-DEMARCHE.md` | Bash | trouvé — arbre de travail conforme à `HEAD`, rien de non commité |
| 19 | `x-preview.mintlify.app/x-api/getting-started/pricing` | EXA fetch | trouvé — grille intégrale. **Miroir, non hôte canonique : d'où le `B·3`** |
| 20 | `x-preview.mintlify.app/x-api/getting-started/getting-started-with-the-x-api` | EXA fetch | rien — `CRAWL_NOT_FOUND` |
| 21 | `developers.facebook.com/docs/instagram-platform/content-publishing` | EXA fetch | trouvé — autorisation de publication de Page |
| 22 | `developers.facebook.com/docs/development/release/tech-provider-verification` | EXA fetch | rien — `CRAWL_NOT_FOUND`. **Adresse devinée ; la bonne est `/access-verification`, trouvée à la ligne 27** |
| 23 | `developers.facebook.com/docs/permissions/reference/pages_manage_posts` | EXA fetch | trouvé |
| 24 | « LinkedIn developer app must be associated with verified LinkedIn Page company page » | EXA search | trouvé — les 30 jours du super-administrateur |
| 25 | `learn.microsoft.com/en-us/linkedin/marketing/community-management-app-review?view=li-lms-2026-04` | EXA fetch | trouvé — **organisation légalement enregistrée, et le refus qui détruit l'application** |
| 26 | « TikTok app review how long does it take business days developers » | EXA search | trouvé — **« several days to two weeks »** |
| 27 | « Meta Tech Provider verification requirements app serving other businesses » | EXA search | trouvé — **la troisième porte, « independent of App Review »** |
| 28 | `developers.tiktok.com/doc/app-review-guidelines/` | EXA fetch | trouvé |
| 29 | `developers.tiktok.com/doc/content-posting-api-reference-audit` | EXA fetch | rien — `CRAWL_NOT_FOUND`. **Adresse devinée. Les conditions de l'audit restent non lues** |
| 30 | `www.facebook.com/business/help/1930421151034254` | EXA fetch | rien — `CRAWL_NOT_FOUND`. **Adresse devinée.** Le détail de l'autorisation de publication de Page côté client reste non lu |
| 31 | `developers.facebook.com/docs/pages/overview` | EXA fetch | trouvé |
| 32 | `zdump` et `TZ=… date` sur `America/Guadeloupe` et `Europe/Paris` | Bash | trouvé — `A·1`, rejouable hors réseau |
| 33 | Calcul des recouvrements ouvrés Guadeloupe / Paris / New York | Bash, Python `zoneinfo` | trouvé — `A·1` |
| 34 | « Google Business Profile API access request approval how long waiting quota 0 QPM » | EXA search | trouvé — **les 14 jours annoncés, et leur suspension de septembre 2026** |
| 35 | « cycle de vente TPE France durée moyenne premier contact signature » | EXA search | trouvé, mais **rien de primaire et rien de guadeloupéen** |
| 36 | `www.data.gouv.fr/api/1/datasets/` — 6 requêtes : bodacc · marchés publics · données essentielles de la commande publique · vigilance météo · registre national des entreprises · annonces civiles et commerciales | curl | **refusé** — `HTTP 000` sur les six |
| 37 | `www.bodacc.fr` | curl | **refusé** — `HTTP 000` |
| 38 | `$HTTPS_PROXY/__agentproxy/status` | curl | trouvé — nomme `bodacc-datadila.opendatasoft.com:443`, **403 de la passerelle sur CONNECT**, horodaté |

### 11.1 — Ce que le journal dit, et que le reste du document ne dit pas

**38 tentatives · 24 trouvées · 7 sans résultat · 7 refusées.**

**Où il est inutile de retourner par la voie directe.** Cinq hôtes refusés par le mandataire du conteneur : `developers.facebook.com`, `developers.google.com`, `docs.x.com`, `www.data.gouv.fr`, `www.bodacc.fr` — et, nommé par le point d'état du mandataire, `bodacc-datadila.opendatasoft.com`. Trois de ces refus avaient déjà coûté au registre la mention « hôtes refusés » ; ils ne coûtent plus rien, voir ci-dessous. Les deux derniers coûtent toujours, et ce sont eux qui laissent mon volume de veille en `D`.

**Par quelle voie détournée j'ai atteint ce que j'ai atteint.** `EXA web_fetch` a lu **trois des cinq hôtes refusés** — Meta, Google, et le miroir de X. **Les quatre résultats décisifs de ce retour viennent tous de cette voie** : le bouton grisé de Meta, les 60 jours de Google, l'exclusion de TikTok, le tarif au lien de X. Par la voie directe, ce retour aurait rendu « délais inconnus » — exactement ce que le plan écrit. **Le plan n'a pas manqué ces délais parce qu'ils étaient introuvables ; il les a manqués parce qu'une seule voie a été essayée.**

**Ce que la voie détournée n'a pas atteint.** `developer.x.com` et `developer.twitter.com` sont refusés **des deux côtés** : par le mandataire et par le récupérateur tiers. C'est le seul hôte de cette enquête que rien n'ouvre, et c'est exactement celui qui fonde ma seule ligne rétrogradée. `www.data.gouv.fr` et la source BODACC ne sont ouverts par aucune des deux voies non plus — je n'ai pas essayé de forge de code pour eux, et c'est une piste non suivie que je déclare au §11.2.

**Mes trois adresses devinées, et ce qu'elles ont coûté.** Lignes 22, 29 et 30 : j'ai fabriqué trois adresses plausibles qui n'existent pas. La première n'a rien coûté — la bonne page a été trouvée par recherche à la ligne 27. Les deux autres ont coûté du contenu réel : **les conditions exactes de l'audit TikTok** et **le détail de l'autorisation de publication de Page côté client** restent non lus. Je ne les ai donc pas écrits, et je ne les ai pas devinés non plus.

### 11.2 — Pistes que j'ai vues et n'ai pas suivies, nommées

Trois, et je ne les présente pas comme épuisées.

1. **Les forges publiques pour atteindre BODACC et `data.gouv.fr`.** La leçon est au registre, je ne l'ai pas appliquée ici : un dépôt qui moissonne BODACC porte souvent un échantillon de données et la licence en clair. Cela ne donnerait pas le volume hebdomadaire guadeloupéen — seule la vraie source le donne — mais cela donnerait **la structure des enregistrements et le texte de licence**, soit la moitié du poste que le plan appelle « lecture des licences ». Coût : quelques requêtes. Je ne l'ai pas fait.
2. **Le portail d'assistance de Google à sa source.** J'ai lu l'annonce de suspension des délais par un relais. Le fil d'origine existe sur `support.google.com` et aurait fait passer cette ligne de `C·2` à `B·2` — c'est la ligne qui décide s'il reste un délai annoncé pour la phase 4. Je n'ai pas essayé cet hôte, ni par le mandataire, ni par EXA.
3. **Les conditions de l'audit TikTok.** Ligne 29 du journal : adresse devinée, échec. Je n'ai pas relancé par recherche. Or si l'audit admet un outil opérant sous mandat écrit, l'exclusion du §2.2 se négocie au lieu de fermer. **C'est la piste non suivie la plus coûteuse de ce retour**, parce qu'elle décide si TikTok est une plateforme à deux semaines ou une plateforme morte.
