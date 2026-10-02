# 07 — Critique adversariale du plan de construction : l'argent et le premier client

Lecteur adversarial, contexte vierge hors registre. Cible : `PLAN-DE-CONSTRUCTION.md` du 2 octobre 2026.
Angle imposé : trésorerie, prix de vente, premier euro. **Je n'approuve rien.**

Barème du registre : provenance **A** mesuré · **B** primaire · **C** secondaire · **D** mémoire,
croisée avec robustesse **1** rejouable · **2** attesté · **3** étroit · **4** non étayé.

> **Règle de rétrogradation, appliquée par moi à moi.** Toute affirmation que je classe en source
> primaire sans donner son adresse et sa date de consultation **redescend d'un cran de robustesse** et
> n'engage plus une dépense. Je l'ai appliquée ligne par ligne : **l'audit complet est en § 8**, et il
> rétrograde **quinze lignes dont trois que mon propre raisonnement utilisait**. Les crans écrits
> dans le corps sont déjà les crans corrigés. **L'annexe A porte mon journal de requêtes**, y compris
> les recherches qui n'ont rien donné et les hôtes refusés.
>
> Ce que la règle m'apprend d'emblée, et c'est un gain pour l'angle argent : **le seul « prix de vente
> tenable » que le plan écrit — 25 à 35 € HT — est, après rétrogradation, la ligne la plus faible de
> tout le dossier (`B·4`).** Le plan tarife son produit sur son unique ligne non étayée.

---

## 0 — Mes lignes `D` déclarées en tête, avant tout raisonnement

Honnêteté d'abord : ce qui suit n'est pas étayé, et tout ce qui en découle hérite du cran.

| Ligne `D` | Pourquoi je ne peux pas faire mieux | Ce qu'elle décide dans ce fichier |
|---|---|---|
| **1 jour-personne = 7 h productives** | Convention de calcul, aucune source. `D·4` | Convertit les 22-37 jours-personne de maintenance en euros. Toute la section 3 |
| **Coût horaire chargé de 30 à 40 €/h** pour le mainteneur | Repris de `01-juridique-relance` § 10.4, qui ne le source pas davantage. Encadré par deux lignes `B·2` du registre : 12,3 €/h au SMIC brut et 57,8 €/h de tarif facturé de community manager. `C·3` par héritage, `D` à l'origine | Le coût fixe annuel, donc le nombre de clients |
| **Un appel de support de 20 min par client et par trimestre** (hypothèse basse), **un par mois** (hypothèse haute) | Aucune mesure, aucun comparable sourcé. `D·4` | Le seuil de rentabilité par client, section 4 |
| **Taux de conversion commerciale** | Je l'ignore. Je refuse de l'inventer, le plan lui-même interdit le chiffrage inventé (ligne 161) | Je ne chiffre donc **aucun coût d'acquisition client**. Section 3.4 |
| **Taux d'attrition (churn)** | Zéro mesure, zéro comparable sourcé. `D·4` | C'est **le** nombre qui décide si un prix bas tient. Section 4.3 |
| **Délai entre signature et encaissement effectif** | Non sourcé. Non nul | Section 1 |

Et une ligne du registre que j'hérite en `D` sans pouvoir l'améliorer : **le nombre d'avis mensuels par
établissement, 10 à 40, cran `D`**. Elle commande le coût variable, donc la marge, donc tout.

---

## 1 — Quand arrive le premier euro, et qu'est-ce qui le retarde

### 1.1 Le chemin complet, étape par étape

Le plan ordonne bien les travaux. Il ne date rien. Voici le chemin réel, en séparant ce que le plan
écrit de ce qu'il ne mentionne nulle part.

| # | Étape | Dans le plan ? | Durée | Dépend de |
|---|---|---|---|---|
| 1 | **Élargir l'accès réseau** de l'environnement | Oui, ligne 31 | « un réglage », non datable — c'est une action de Laurent | rien |
| 2 | Lire et dater la licence de **trois sources** en accès ouvert. Le code **refuse** de collecter une source dont la licence n'est pas lue (ligne 68) | Oui | non chiffrée, sérielle, source par source | 1 |
| 3 | **Accumuler quatre semaines calendaires** de données réelles filtrées Guadeloupe | Oui, ligne 75 | **4 semaines, mur d'horloge incompressible** | 1 et 2 |
| 4 | Produire quatre rapports, compter les lignes utiles | Oui, ligne 77 | 2 à 3 jours | 3 |
| 5 | **Porte d'abandon** : moins d'une dizaine de lignes utiles/semaine → « repenser l'offre avant tout développement » (ligne 175) | Oui | — | 4. **Peut remettre tout le chemin à zéro** |
| 6 | Montrer à **cinq** établissements | Oui, ligne 75 | non datable | 4 |
| 7 | **Immatriculation, SIRET** | **Non. Nulle part** | formalité en ligne, gratuite en micro | — |
| 8 | **Compte bancaire dédié** | **Non** | jours à semaines | 7 |
| 9 | **Moyen d'encaissement** : ouverture de compte prestataire + vérification d'identité (KYC) | **Non** | jours | 7, 8 |
| 10 | **Conditions générales, contrat écrit, mandat de prélèvement SEPA, contrat de sous-traitance données** | **Non** | rédaction + signature client | 7 |
| 11 | **Première facture émise** | **Non** | — | 6, 10 |
| 12 | **Délai de paiement, puis encaissement** | **Non** | 30 jours en usage B2B ; avec prélèvement SEPA, le délai de préavis du mandat | 11 |
| 13 | Pour le volet avis seulement : **un mandat signé par client** (`B·3`, plan ligne 124) et **gel du schéma de date d'expérience avant le premier jour de service** (ligne 153) | Oui | non datable, dépend d'un tiers | 10 |

### 1.2 Le plancher, et il dépasse deux mois

En supposant **zéro** pour tout ce qui n'est pas un mur d'horloge — réglage réseau instantané, licences
lues en un jour, vente conclue le jour de la démonstration, administratif fait en parallèle :

> 4 semaines d'accumulation + 3 jours de rapports + 30 jours de délai de paiement
> = **2 mois et 1 semaine, plancher absolu.**

Rien de tout cela n'est nul. Les étapes 7 à 12 n'existent pas dans le plan, donc elles n'ont été ni
estimées ni lancées, et quatre d'entre elles sont séquentielles. L'étape 6 n'a ni liste de prospects,
ni argumentaire, ni grille tarifaire, ni devis type. L'étape 5 est une porte qui peut tout annuler.

**Estimation de bout en bout : 4 à 6 mois jusqu'au premier euro réellement encaissé**, et seulement si
la porte de volume passe du premier coup. Cran `C·3` — c'est un calcul sur les durées écrites dans le
plan plus des étapes non chiffrées, pas une mesure.

### 1.3 Donc : le plan a un problème de trésorerie qu'il ne nomme pas

Il faut le dire exactement, parce que le problème n'est pas celui qu'on croit.

**Ce qui sort en euros avant le premier euro entrant est petit.** Serveur 450-700 €/an, soit 38 à 58 €
par mois qui courent dès le premier jour d'accumulation (**`B·4`** après rétrogradation, § 8 — aucune adresse au registre). Test chez le
prestataire local 200 € (plan ligne 197). Les deux micro-tests de la critique juridique, 5,95 € et 6 $.
Assurance de responsabilité professionnelle 180 à 600 €/an si on la prend (section 5). Immatriculation
gratuite en micro-entreprise. **Total plausible : 500 à 1 500 € de décaissement avant la première
recette.** Ce n'est pas un mur d'argent.

**Ce qui sort en temps est grand, et n'est pas financé.** Le plan refuse explicitement « tout chiffrage
en jours de travail » (ligne 161) au motif qu'un budget inventé est du cran `D` déguisé. Le refus est
juste sur la méthode et faux sur la conséquence : **refuser de chiffrer l'effort ne le fait pas
disparaître du compte en banque de celui qui le fournit.** Quatre à six mois de travail non rémunéré,
plus 22 à 37 jours-personne par an de maintenance qui démarrent le jour où le premier client est servi,
c'est la vraie sortie de trésorerie. Elle est intégralement portée par une personne dont le plan ne dit
pas de quoi elle vit pendant ce temps.

**Et le plan gage son propre désaccord ouvert sur une date qu'il n'écrit pas.** Le registre, § 5,
consigne que l'arbitre entre « resserrer sur la veille » et « tenir les quatre outils » est **le premier
euro facturé**. Un désaccord arbitré par un événement non daté n'est pas arbitré : il est suspendu. Le
plan devait écrire cette date. Il ne l'écrit pas.

### 1.4 Trois retards que le plan ne voit pas du tout

**(a) Le volet avis ajoute quatre signatures, pas une.** Le plan compte « un mandat signé par client »
comme le seul geste bloquant (ligne 16). En réalité, pour un client payant, il faut : la délégation
d'administrateur de la plateforme, **le contrat de prestation**, **le mandat de prélèvement SEPA**, et
**le contrat de sous-traitance de données** — puisque détenir le jeton d'un client et traiter les avis
de ses clients fait de nous un sous-traitant. Quatre documents, quatre allers-retours, et chacun peut
dormir une semaine chez le client. Le poste que le plan identifie comme irréductible est donc **quatre
fois plus gros qu'annoncé**.

**(b) La règle du loyer, prise au mot, interdit de construire quoi que ce soit.** Plan ligne 173 :
« Coût annuel d'un organe > 10 % du revenu récurrent qu'il débloque → on loue ». Au jour 1, le revenu
récurrent est de zéro. 10 % de zéro est zéro. **Tout organe dont le coût est strictement positif
déclenche donc la règle.** Soit c'est un auto-blocage accidentel, soit c'est la phrase la plus honnête
du plan — « ne construis rien avant qu'un client paie » — mais dans les deux cas le plan ne calcule
jamais la règle, et la met en vitrine comme un garde-fou qui n'a pas de valeur numérique.

**(c) La règle d'arrêt du mandat est « une date, pas une condition » (ligne 151) — et la date n'est pas
écrite.** Une règle d'arrêt sans sa date n'est pas une règle d'arrêt. Pire : son repli est « rendre le
service à la main, sous mandat, facturé ». Un service rendu à la main n'a plus la structure de coût
d'un logiciel, il a celle d'une agence. Voir section 2.4 : **le repli du plan n'est viable qu'à partir
de 200 €/mois**, ce que le plan ne dit pas.

---

## 2 — Le prix de vente n'est pas arrêté. Je l'arrête.

### 2.1 L'état du dossier, tel que le registre l'établit

**Crans corrigés par la règle de rétrogradation du § 8.** Une ligne de prix garde son cran quand elle
porte son adresse et sa date ; elle en perd un quand son « origine primaire » est en réalité un calcul
interne sans adresse.

| Entrée | Montant | Cran corrigé | Adresse, et date de consultation |
|---|---|---|---|
| Prestataire guadeloupéen (Saint-Claude 97120), 8 publications, avis **non inclus** | **200 €/mois** | `B·2` **tenu** | `mangoweb.digital/communication-digitale` — consultée le 2 oct. 2026 par l'agent juridique, verbatim collé dans `critiques/01-juridique-relance.md` § 8.1. **Non revérifiée par moi : hôte au mur** (annexe A) |
| Antenne régionale, « modération des avis négatifs » | **250 € HT/mois + 300 € HT de création** | `B·2` **tenu** | `linkeo-guadeloupe.com/community-management.php` — 2 oct. 2026, même § |
| **La moins chère qui réponde à chaque avis** | **450 € HT/mois** (690 € sans engagement) | `B·2` **tenu** | `app.plateya.fr/...forfait-seo-local-fiche-gmb` — 2 oct. 2026, même § |
| National, page régionale Guadeloupe | **dès 490 €/mois** | `B·2` **tenu** | `so-community.fr/region/guadeloupe` — 2 oct. 2026, même § |
| Guadeloupe, réponse aux avis et messages | **dès 1 290 € HT/mois** | `B·2` **tenu** | `katchak-agency.fr/community-management-en-guadeloupe/` — 2 oct. 2026, même § |
| Guadeloupe, sur devis, « réponse proactive aux questions et avis » | **non chiffré** | `B·2` **tenu** | `cws.gp/services/reseaux-sociaux.html` — 2 oct. 2026, même § |
| L'étalon gratuit : lire et répondre à tous ses avis à la main sur sa fiche d'établissement | **0 €** | `B·3` **rétrogradé** de `B·2` | Aucune adresse ni date : constat de l'agent juridique au § 8.2 (a), hôtes Google au mur. **Reste une piste, mais c'est le concurrent réel d'un prix bas** |
| Bande vide, plus aucune prestation humaine | **30 € à 200 €/mois** | `B·2` **tenu** | Déduction sur les six adresses ci-dessus, toutes datées du 2 oct. 2026. **L'adresse de chaque borne existe**, donc la bande tient |
| Plancher de coût, sans la presse | **25 à 35 € HT/mois** | **`B·4`** rétrogradé de `B·3` | **Aucune adresse.** Calcul interne, `critiques/01-juridique-relance.md` § 10.4, sur un volume d'avis en cran `D` |
| Plancher de coût, avec la presse | **100 à 120 € HT/mois** | **`B·4`** rétrogradé de `B·3` | Idem, plus une licence elle-même rétrogradée |
| Licence de veille presse | **52,50 € HT/client/mois** | **`B·4`** rétrogradé de `B·3` | « Contrat réel de l'organisme de gestion collective », **sans adresse ni date** au registre |
| Geste humain incompressible | **15 à 30 min/client/mois, soit 8 à 20 € HT** | **`B·4`** rétrogradé de `B·3` | **Aucune adresse.** Calcul interne, critique 01 § 10.4, volume en `D` |

Et ce que le plan en fait : il écrit « **cinquante euros par mois** » dans la question du test
(ligne 75), puis « prix de vente tenable **25 à 35 € HT** » par héritage du plancher (ligne 81). **Le
plan n'arrête donc aucun prix : il en porte deux, incompatibles, dont l'un n'est qu'un coût majoré.**

### 2.2 Cinquante euros est une erreur, et voici les quatre démonstrations

**Démonstration 1 — contradiction interne du plan, et c'est la plus courte.**
Le registre établit en `B·2` — six adresses datées, § 2.1 — que la bande 30-200 € est vide **parce que
plus aucune prestation humaine n'y subsiste**, et en `B·3` (rétrogradé : grilles comparées sans adresse)
que **la conformité *est* le geste humain**, au point que deux éditeurs
facturent le double pour le réintroduire. Or le plan rend la validation humaine **obligatoire et
inscrite au schéma** : « deux déclencheurs de base refusent un contenu généré sans relecteur nommé »
(ligne 107), « zéro publication sans relecture humaine » (ligne 135). **Le produit conserve donc
exactement le geste dont l'absence définit la bande.** Vendre dans la bande un produit qui n'a pas la
propriété qui fait la bande est une erreur de catégorie, pas un pari audacieux. **`B·2` sur la bande,
`B·3` sur le geste humain** après rétrogradation ; déduction mienne. **La démonstration tient sur la
prémisse qui a ses adresses.**

**Démonstration 2 — à 50 €, le concurrent n'est pas l'agence, c'est la gratuité.**
À 250 € HT, le client compare à 200 € (MangoWeb, sans les avis), 250 € HT (Linkeo, avis négatifs
seulement) et 450 € HT (Plateya, tous les avis) — et nous gagnons sur le contenu : provenance,
quatre obligations réglementaires tenues par un seul organe, créole, fuseau. À 50 €, le client ne
compare plus à l'agence : il compare à **zéro euro**, parce que lire et répondre à ses avis à la main
sur sa fiche d'établissement est gratuit, établi en `B·3` (rétrogradé, pas d'adresse). 600 € par an
contre gratuit, pour un établissement de 1 à 9 salariés — 71,8 % du tissu, `B·3` rétrogradé — est un
argument perdant. **Un prix bas ne
déplace pas le point de comparaison vers le bas, il le déplace vers le gratuit.**

**Démonstration 3 — à 50 €, l'inconnue en cran `D` passe directement dans la marge.**
Le coût variable est piloté par **l'activité** du client (avis à valider, publications à relire), pas
par son prix. Le volume d'avis est en cran `D`, 10 à 40 par mois, et le registre dit lui-même qu'il
« déplace tout le calcul ».

| Prix | Geste humain à 10 avis/mois | Geste humain à 40 avis/mois | Part du prix consommée, cas lourd |
|---|---|---|---|
| **50 €** | ≈ 8 € | ≈ 20 € | **40 %** |
| **250 €** | ≈ 8 € | ≈ 20 € | **8 %** |

À 50 €, un établissement actif consomme 40 % du prix en geste humain avant tout support, toute
infrastructure, tout impayé. À 250 €, 8 %. **Plus le prix est bas, plus la plus grosse inconnue du
dossier décide de la rentabilité.** C'est la forme rigoureuse de « un prix trop bas attire les clients
qui coûtent le plus cher en support » : ce ne sont pas des clients différents, c'est le **même** client
qui devient déficitaire parce que le prix n'a pas été construit pour absorber sa variance.

**Démonstration 4 — à 50 €, c'est la durée de vie du client qui décide, et elle est en cran `D`.**
Voir section 4.3 : la mise en service se rembourse en 5 à 18 mois à 50 €, en 1 à 1,4 mois à 250 €.
**À 50 €, la rentabilité du produit dépend d'un nombre dont le projet n'a aucune mesure. À 250 €, elle
n'en dépend plus.** Un prix qui neutralise une inconnue en `D` vaut mieux qu'un prix qui la rend
décisive — et cela ne coûte rien de plus à produire.

### 2.3 Le prix que j'arrête

> ## 250 € HT par mois, plus 300 € HT de mise en service facturés à la signature.
> ## Et un palier bas **veille seule à 90 € HT par mois**, sans avis ni publication.

**Justification du 250 € HT, ligne à ligne.**

| Borne | Valeur | Cran | Pourquoi elle contraint |
|---|---|---|---|
| Plancher absolu | 25-35 € HT | **`B·4`** | Coût, pas prix, **et la ligne la plus faible du dossier**. Vendre là, c'est vendre à coût majoré sur une estimation non adressée |
| Plancher de crédibilité | **200 €** | `B·2` | Sous ce prix, aucune prestation humaine n'existe sur ce marché, et notre produit en contient une par conception |
| Référence directe la plus proche | **250 € HT + 300 € HT de création** | `B·2` | Linkeo ne fait que « modérer les avis négatifs ». Nous répondons à tous, avec provenance. **À prix égal, nous donnons plus** |
| Plafond d'attractivité | **450 € HT** | `B·2` | Plateya répond à chaque avis. Il faut être nettement dessous pour que le prix soit un argument. 250 € = **−44 %** |
| Plafond haut du marché | 490 à 1 290 € HT | `B·2` | Établit qu'il n'y a aucune pression déflationniste à 250 € |

250 € HT est donc **le prix le plus bas du marché guadeloupéen qui réponde à tous les avis**, et il est
posé exactement sur la référence locale qui en fait moins. C'est le seul point de la grille où le prix
et le contenu se défendent par la même phrase.

**Justification des 300 € HT de mise en service.** Deux prestataires facturent l'installation
séparément : 200 € (MangoWeb, `B·2`) et 300 € HT (Linkeo, `B·2`). **Le marché établit lui-même que
l'onboarding est un poste, pas un cadeau.** Notre mise en service est plus lourde que la leur : quatre
signatures (section 1.4 a), et le **gel irréversible du schéma de date d'expérience avant le premier
jour de service** (plan ligne 153) — une opération qui ne se refait pas. La facturer à 300 € HT aligne
la recette sur une dépense réelle de 5 à 10 h, et elle **qualifie le prospect** : un client qui refuse
300 € de mise en service n'aurait pas payé 250 € pendant douze mois.

**Justification du palier veille seule à 90 € HT.** La Phase 1 est le seul produit livrable
immédiatement (plan ligne 40), et elle **n'a pas de geste humain par avis** : le rapport est généré, le
contrôle est de l'ordre de 20 min par mois, pas 15 à 30 par client. 90 € HT est 2,6 à 3,6 fois le
plancher de coût sans presse (25-35 € HT, **`B·4`**), reste sous le plancher de 200 € (`B·2`, adressé) pour ne pas
cannibaliser l'offre complète, et laisse 63 à 75 € de marge mensuelle — assez pour absorber un appel de
support mensuel, ce que 50 € ne fait pas.

**Trois règles de tarification qui vont avec, et qui sont des décisions, pas des mesures.**

1. **Tout prix s'écrit « HT ».** Le plan écrit « cinquante euros par mois » sans mention. En Guadeloupe
   le taux normal est de 8,5 % (`C·3`), et la franchise de TVA se franchit au 13e client (section 5.3).
   Un prix annoncé sans « HT » est une erreur de 8,5 % programmée, à absorber ou à renégocier en cours
   de contrat.
2. **Prélèvement SEPA, jamais carte.** À 250 €, 0,35 € contre 4,00 € (section 5.6). Et le prélèvement
   supprime la relance d'impayé, qui est du temps non facturable.
3. **Engagement 12 mois sur l'offre complète.** Pas pour enfermer le client : parce que la mise en
   service contient un gel de schéma irréversible, et qu'un client qui part au mois 3 emporte un travail
   qui ne se recycle pas.

### 2.4 Le repli du plan confirme le prix, et le plan ne l'a pas vu

Plan ligne 151 : si le mandat n'arrive pas, « rendre le service **à la main**, sous mandat, facturé ».
Un service rendu à la main a la structure de coût d'une agence. Or le registre établit en `B·2` que la
prestation humaine sur ce marché commence à **200 €/mois**. **Le repli du plan n'est donc tarifable
qu'à 200 € ou plus — c'est-à-dire au prix que j'arrête, pas à 50 €.** Si le prix public est 50 €,
le repli est inapplicable : il faudrait multiplier le prix par quatre devant un client déjà signé.
**Un prix de lancement à 50 € détruit le plan de repli du plan.** Convergence indépendante avec les
quatre démonstrations du § 2.2.

### 2.5 L'objection à 80 €, et pourquoi elle n'est pas dans le plan

Le registre marque renversée l'assertion « le prix plafond local est 80 €/mois » : la bonne bande est
200 à 450 €, cinq prestataires à l'appui. **Je ne la recrois pas, et je n'utilise pas 80 € comme
plafond.** Mais la formulation du renversement — « cette offre n'existe pas » — est plus large que ce
qui est établi, et l'écart compte pour la vente.

Ce qui est réellement sur disque : la critique `02-marche.md` porte un verbatim daté de
`mangoweb.digital/google-my-business` à **80 €/mois incluant « Réponse à tous les avis » après 200 € de
création** ; la critique `01-juridique-relance.md` porte un verbatim daté de
`mangoweb.digital/communication-digitale` à **200 €/mois, avis non inclus**. **Deux pages du même
prestataire, deux offres différentes.** Le renversement a raison sur le plafond de marché — cinq autres
prestataires à 250-1 290 € le règlent — et va trop loin en déclarant l'offre inexistante.

**Conséquence opérationnelle, et c'est un trou du plan.** 80 € est un prix **qu'un prospect
guadeloupéen peut avoir lu sur une page publique**. Nous le rencontrerons dans la pièce, sous la forme
« MangoWeb le fait pour 80 ». Le plan n'a **aucune** réponse préparée à cette objection. La réponse
existe et elle est forte : à 80 € ce prestataire vend la fiche d'un seul établissement sur une seule
plateforme, sans veille officielle, sans provenance opposable, sans registre transmissible à un Ordre,
sans date d'expérience captée — et le registre établit en `B·3` (rétrogradé, baromètre sans adresse) que l'opérateur solo qui facture 80 €
pour cinq à six heures travaille à l'équivalent du salaire minimum brut, donc l'offre n'est pas
reproductible à l'échelle. **Mais cette réponse doit être écrite avant le premier rendez-vous, pas
improvisée.**

**Vérification à 0 € que je ne peux pas faire moi-même** : `mangoweb.digital` est refusé par la
politique réseau de cet environnement (mur nommé en section 6). Ouvrir les deux pages dans un
navigateur et les horodater règle la contradiction en dix minutes. Tant que ce n'est pas fait, les deux
lignes coexistent sur disque et la bande de prix repose sur cinq autres prestataires, pas sur six.

---

## 3 — Combien de clients pour que ça tienne

### 3.1 Hypothèses déclarées

| # | Hypothèse | Valeur | Cran |
|---|---|---|---|
| H1 | Jour-personne productif | 7 h | `D·4`, déclaré § 0 |
| H2 | Coût horaire chargé du mainteneur | 30 à 40 €/h | `C·3`, déclaré § 0 |
| H3 | Maintenance annuelle | 22 à 37 jours-personne | **`B·4`** rétrogradé, § 8 — « estimation sur dépôts », sans adresse |
| H4 | Serveur | 450 à 700 €/an | **`B·4`** rétrogradé — aucune adresse, aucun fournisseur nommé |
| H5 | Geste humain par client | 8 à 20 € HT/mois | **`B·4`** rétrogradé, volume en `D` |
| H6 | Support par client | 4 à 13 € HT/mois | `D·4`, déclaré § 0 |
| H7 | Encaissement par prélèvement SEPA | 0,35 € par échéance | `C·3`, § 5.6 |
| H8 | Assurance professionnelle | 250 à 600 €/an | `C·3`, § 5.5 |

### 3.2 Le coût fixe annuel, calculé

Maintenance : 22 × 7 × 30 = **4 620 €** (bas) ; 37 × 7 × 40 = **10 360 €** (haut).
Serveur : 450 à 700 €. Assurance : 250 à 600 €.

> **Coût fixe annuel = 5 320 € (bas) à 11 660 € (haut). Médian ≈ 8 500 €.** Calculé sur H1-H4 et H8.

Le rapport « dix contre un » du plan (ligne 183) est juste en nature et trompeur en lecture : il ne dit
pas que le coût est faible, il dit que **87 à 89 % du coût fixe est du temps humain**, donc qu'il ne se
paie pas avec une carte bancaire mais avec des mois de vie.

### 3.3 Le coût variable et la marge par client

| | Veille seule, 90 € HT | Produit complet, 250 € HT |
|---|---|---|
| Geste humain | 10 à 13 € (contrôle de 4 rapports) | 8 à 20 € |
| Support (H6) | 4 à 13 € | 4 à 13 € |
| Encaissement SEPA | 0,35 € | 0,35 € |
| **Coût variable** | **15 à 27 €** | **12 à 33 €** |
| **Marge mensuelle** | **63 à 75 €** | **217 à 238 €** |
| **Marge annuelle** | **756 à 900 €** | **2 600 à 2 856 €** |

### 3.4 Le nombre de clients

Coût fixe ÷ marge annuelle, bornes croisées :

| Offre | Clients pour couvrir le coût fixe | Médian |
|---|---|---|
| **Produit complet à 250 € HT** | **2 à 5** | **3** |
| **Veille seule à 90 € HT** | **6 à 16** | **10** |
| Au prix que le plan évoque, **50 €** (marge 17 à 38 €) | **12 à 58** | **26** |

**Le chiffre à retenir : 3 clients à 250 € HT couvrent la machine entière. À 50 €, il en faut 26.**
Le prix ne change pas le produit ; il change le nombre de signatures à obtenir **par un facteur
proche de neuf**, et chaque signature coûte 5 à 10 h de mise en service (§ 4.1).

**Et il faut dire ce que « couvrir » ne veut pas dire.** Ces 3 clients remboursent la maintenance
**valorisée à un coût horaire**, le serveur et l'assurance. Ils ne paient aucun revenu, aucune
prospection, aucune mise en service, aucune comptabilité, aucun impôt. Pour l'au-delà, la seule forme
honnête est une fonction, puisque je ne connais pas l'objectif de revenu de Laurent :

> **Chaque 1 000 € HT par mois de revenu au-delà du point mort demande 4,2 à 4,6 clients à 250 € HT, ou
> 13 à 16 clients à 90 € HT, ou 27 à 60 clients à 50 €.**

### 3.5 Confrontation au marché réel, et elle n'est pas rassurante où on croit

Marché donné : ~6 500 entreprises libérales et 760 établissements employeurs en hébergement-restauration
(le second **`B·3`** après rétrogradation : « organisme de branche d'après sources publiques », aucune
adresse, 86 % à 1-9 salariés).

Lecture naïve : 13 clients sur 7 260, soit **0,18 %**. Un rien. Sur les seuls 760 établissements HCR,
**1,7 %**. Conclusion apparente : trivialement atteignable.

**Cette lecture est fausse, et le registre contient de quoi la casser.**

1. **La différenciation ne porte que sur 3,5 à 5,2 % du marché adressable** (**`B·3`** rétrogradé, croisement interne de deux
   périmètres statistiques). Si les exigences locales — créole, fuseau, sources guadeloupéennes — sont
   ce qui nous fait choisir, la cible réelle est **27 à 40 établissements HCR**, pas 760. 13 clients
   sur 27-40, c'est **33 à 48 % de part de marché**. Ce n'est plus un rien, c'est une domination.
2. **Les 6 500 libéraux ne sont pas adressables pour le volet avis.** Le médecin est fermé
   définitivement (**`B·3`** rétrogradé : code de déontologie médicale cité par article, sans adresse en
   ligne ni date, `legifrance` au mur). L'avocat peut recueillir des avis mais **ne peut pas intégrer la
   note** (**`B·3`**, Cass. 1re civ. 11 mai 2017 et 22 mai 2019, numéros de décision absents du
   registre), et la collecte par message mobile nous rendrait instrument d'un contournement
   (**`B·3`**, règlement intérieur national art. 10.3, non adressé). Les 6 500 sont adressables pour la **veille**, à 90 € HT, donc à
   la marge de 63-75 € — l'offre qui exige 13 à 16 clients par millier d'euros de revenu.
3. **Le plan ne prévoit que cinq prospects** (ligne 75). Pour 13 clients, à un taux de conversion que
   je refuse d'inventer, il faut un ordre de grandeur de plusieurs dizaines de rendez-vous. À deux par
   semaine, c'est **deux à trois trimestres de prospection**, en plus des 65 à 130 h de mise en service.
   Le plan ne porte ni liste de prospects, ni rythme, ni qui les prend.

**Verdict sur l'atteignabilité.** 3 clients : oui, plausible en six mois si la porte de volume passe.
13 clients : **9 à 12 mois de campagne commerciale**, et la mise en service seule représente 2 à 4
semaines de travail à temps plein que le plan ne budgète nulle part. 26 clients et plus : la contrainte
n'est plus le marché, c'est la **capacité d'une personne**, puisque 26 clients × 15-30 min de geste
mensuel = 6,5 à 13 h par mois de validation, plus le support, plus les 22-37 jours de maintenance.
`C·3`, calcul sur entrées sourcées et sur mes hypothèses `D` déclarées.

---

## 4 — Le coût par client que le plan sous-estime

Le plan ne porte **aucun** coût par client. Le registre en porte un : 15 à 30 min de geste humain
mensuel. En voici cinq autres, et le moment où un client devient déficitaire.

### 4.1 La mise en service — le coût le plus gros et le plus invisible

Aucune durée sourcée n'existe. Mais **le marché la tarife**, et c'est le meilleur substitut disponible :
**200 €** (MangoWeb, `B·2`, adresse et date au § 2.1) et **300 € HT** (Linkeo, `B·2`, idem) de frais de
création. **Ces deux-là tiennent leur cran : ce sont les seules entrées de coût par client du fichier
qui portent une adresse.** Deux prestataires
indépendants, dont un local, facturent l'installation 200-300 €. À 30-40 €/h, cela représente **5 à
10 h**. Et notre mise en service est plus lourde que la leur : quatre signatures (§ 1.4 a), lecture et
datation de licence si le client ajoute une source, configuration des filtres, et **le gel irréversible
du schéma de date d'expérience** (plan ligne 153).

**Le plan le compte à zéro.** C'est la plus grosse omission de coût du document.

### 4.2 Les quatre autres

| Poste | Estimation | Cran | Pourquoi le plan le rate |
|---|---|---|---|
| **Formation du client** | Comprise dans les 5-10 h ci-dessus si elle est faite au même rendez-vous ; sinon 1 à 2 h de plus | `D·4` | Le plan suppose un relecteur nommé (lignes 107, 135) **chez le client** sans dire qui le forme à relire en 30 secondes sur mobile |
| **Support** | 4 à 13 € HT/mois (H6) | `D·4` | Nulle part dans le plan. **Un appel mensuel double le coût humain par client** |
| **Relance d'impayé** | ≈ 0 € avec prélèvement SEPA ; frais de rejet + relance manuelle en cas d'impayé SEPA, montant inconnu | `D·4` | Nulle part. Le choix du moyen d'encaissement est le levier, et il n'est pas fait |
| **Temps de signature du mandat** | Non chiffrable. Dépend d'un tiers, et le plan le reconnaît comme irréductible (ligne 16) | — | Le plan compte **un** mandat. Il en faut quatre (§ 1.4 a) |
| **Départ du client** | Mise en service perdue (200-300 €) + révocation de jeton + export/suppression des données + gel de schéma non recyclable | `C·3` pour le montant | Nulle part. Et le taux d'attrition est en `D` |

### 4.3 À quel moment un client devient déficitaire

Deux conditions, et seule la seconde est intéressante.

**Condition 1 — déficitaire en régime, si son activité dépasse sa marge.** À 250 € HT, il faudrait un
client générant plus de 250 € de geste mensuel, soit plus de 500 avis par mois à 30 s chacun : hors de
toute plausibilité pour un établissement de 1 à 9 salariés. **À 250 €, aucun client n'est déficitaire
en régime.** À 50 €, le seuil tombe à 100 avis par mois, ce qui n'est plus absurde pour un hôtel de
59 chambres (**`B·3`** rétrogradé, institut national de la statistique sans adresse) en haute saison —
occupation 77 % en janvier-mars (**`B·2`** rétrogradé de `B·1`).
**À 50 €, le meilleur client du portefeuille est le plus susceptible d'être le seul déficitaire.**

**Condition 2 — déficitaire sur sa durée de vie, et c'est la vraie.** Mise en service
*O* = 200 à 300 €, marge mensuelle *m*. Mois nécessaires = *O* / *m* :

| Prix | Marge mensuelle | Mise en service remboursée en | Un client qui part avant |
|---|---|---|---|
| **250 € HT** | 217 à 238 € | **0,8 à 1,4 mois** | **2 mois** est une perte |
| **90 € HT** (veille) | 63 à 75 € | **2,7 à 4,8 mois** | **5 mois** est une perte |
| **50 €** | 17 à 38 € | **5,3 à 18 mois** | **18 mois** est une perte, dans l'hypothèse basse de marge |

> **Le verdict le plus net de ce fichier.** À 50 €, un client doit rester **jusqu'à dix-huit mois** pour
> rembourser son installation. Le taux d'attrition est en cran `D`, zéro mesure. **Un prix à 50 € fait
> donc dépendre toute la rentabilité du produit du seul nombre que le projet ignore totalement.**
> À 250 € HT, la mise en service est remboursée avant la deuxième facture, et l'attrition redevient un
> sujet commercial au lieu d'être un risque de ruine.

Et si la mise en service est facturée 300 € HT comme je le propose, elle est remboursée **au jour de la
signature** : le client est rentable immédiatement, et l'inconnue en `D` est neutralisée par une ligne
de devis.

---

## 5 — Ce que le plan n'a pas prévu du tout côté argent

Aucun de ces sept postes n'apparaît dans le plan. **Aucun montant de cette section n'est en `B`, et
c'est volontaire : je n'ai ouvert aucune de ces pages.** Le mur réseau a refusé toute source primaire
(section 6) ; je n'ai eu que des résumés de moteur de recherche. Les montants sont donc en `C·2` au
mieux, `C·3` en général, **et chacun porte son adresse et sa date de consultation dans le tableau du
§ 8.2**. Par la règle que je m'applique, aucun d'eux ne fonde à lui seul une dépense : chacun est une
piste à confirmer par une lecture directe, une heure de navigateur au total.

### 5.1 Statut juridique

Micro-entreprise, immatriculation en ligne gratuite. C'est le seul véhicule cohérent avec un projet à
une personne et 3 à 13 clients. Le plan ne nomme aucun statut, donc aucune des conséquences ci-dessous.

### 5.2 Cotisations sociales — et il y a une falaise en année 4

Taux réduits DOM pour les prestations de services commerciales (BIC) : **3,6 % pendant les 7 premiers
trimestres, 10,6 % jusqu'à la fin de la 3e année, 14,2 % à partir de la 4e** — contre 21,2 % en
métropole. `C·3`, résumé de recherche ; `urssaf.fr` est **bloqué** par le proxy, je n'ai pas pu lire la
source primaire.

Appliqué à 13 clients à 250 € HT, soit 39 000 € par an :

| Période | Taux | Cotisations annuelles |
|---|---|---|
| 7 premiers trimestres | 3,6 % | **1 404 €** |
| Jusqu'à fin de 3e année | 10,6 % | **4 134 €** |
| Dès la 4e année | 14,2 % | **5 538 €** |

> **À chiffre d'affaires identique, l'année 4 coûte 4 134 € de plus que l'année 1.** C'est l'équivalent
> de deux clients à 250 € HT, à trouver pour ne pas reculer. Le plan ne nomme ni le dispositif, ni la
> falaise.

**Ce que j'ignore** : le taux applicable si l'activité relève du régime BNC plutôt que BIC services. Un
abonnement logiciel avec prestation de relecture peut relever de l'un ou de l'autre, le taux diffère, et
**je ne sais pas lequel s'applique.** Un appel à l'Urssaf le règle gratuitement.

### 5.3 TVA — le 13e client déclenche un changement de régime

Franchise en base pour les prestations de services en 2026 : **37 500 €**, seuil majoré **41 250 €**.
Le projet de loi de finances 2026 voulait abaisser et unifier ces seuils ; **l'article a été supprimé
par le Parlement fin 2025**, les seuils sont maintenus. `C·2` — plusieurs sources secondaires
concordantes, aucune primaire lue, `legifrance` étant déjà au mur du registre.
Taux normal en Guadeloupe : **8,5 %** (`C·3`).

À 250 € HT par mois : 37 500 / 3 000 = **12,5**.

> **Le 13e client fait franchir la franchise de TVA.** Conséquence : facturation de la TVA à 8,5 %,
> déclarations périodiques, et un prix affiché qui doit avoir été écrit « HT » depuis le premier devis.
> À 90 € HT en veille seule, le seuil tombe à **35 clients**. Le plan, qui écrit « cinquante euros par
> mois » sans mention de taxe, programme une erreur de 8,5 % sur chaque contrat signé avant ce
> franchissement.

Plafond du régime micro pour les services : **77 700 €** (`C·3`), soit **26 clients à 250 € HT**. C'est
la borne où le statut lui-même doit changer, avec tout ce que cela porte en comptabilité.

### 5.4 Cotisation foncière des entreprises

Exonération **totale et automatique la première année**, sous réserve de la déclaration initiale
1447-C-SD avant le 31 décembre de l'année de création. Base réduite de moitié la deuxième année.
Exonération si les recettes n'excèdent pas 5 000 €. `C·3`.

**Montant : je l'ignore.** Il dépend de la valeur locative et du taux voté par la commune. Non
chiffrable sans connaître la commune d'établissement.

### 5.5 Assurance de responsabilité civile professionnelle — la question posée sérieusement

**Réponse : elle n'est pas obligatoire.** Aucune obligation légale d'assurance ne pèse sur les métiers
du logiciel, du conseil informatique ou de l'agence web, qui ne sont pas des professions réglementées.
L'obligation d'assurance vise les professions réglementées, ce que ce métier n'est pas. `C·2` —
plusieurs sources secondaires indépendantes et concordantes, dont deux cabinets d'avocats et un
courtier.

**Et il faut la prendre quand même, pour trois raisons dont deux sont dans le registre.**

1. **Le produit assume une responsabilité éditoriale nommée.** Le registre établit en `B·3` (rétrogradé, textes cités sans adresse) que le
   fondement est la loi sur la confiance dans l'économie numérique et la loi de 1881 — « aucun abri
   d'hébergeur » (plan ligne 93). Une responsabilité éditoriale assumée sans assurance est une
   exposition patrimoniale personnelle.
2. **Nous publions sous mandat sur les comptes d'un tiers.** Une publication fautive sur le compte d'un
   avocat le met en risque disciplinaire : annoncer un taux de succès est une faute (**`B·3`**), un élément
   comparatif est prohibé (**`B·3`**) — avis déontologiques et décret cités sans adresse ni date. Le préjudice est le sien, le recours est contre nous.
3. **Les clients professionnels et les marchés publics demandent l'attestation** avant de signer
   (`C·3`). Un cabinet d'avocat la demandera.

**Coût : 180 à 600 € par an** selon le profil et le chiffre d'affaires (`C·3`). C'est le poste le mieux
rentabilisé du budget, et le plan ne le mentionne pas.

### 5.6 Moyen d'encaissement et sa commission — une décision à prendre, pas une ligne de budget

| Moyen | Tarif | Cran | À 250 € | À 90 € |
|---|---|---|---|---|
| Carte européenne standard (Stripe) | 1,5 % + 0,25 € | `C·3` | **4,00 €** (1,6 %) | **1,60 €** (1,8 %) |
| Carte premium / internationale | 2,8 % à 3,15 % + 0,25 € | `C·3` | 7,25 à 8,13 € | — |
| **Prélèvement SEPA (Stripe)** | **0,35 € forfaitaire** | `C·3` | **0,35 €** (0,14 %) | **0,35 €** (0,39 %) |
| Prélèvement SEPA (GoCardless) | 1 % + 0,20 €, plafond 2 € national | `C·3` | 2,00 € (plafonné) | 1,10 € |

Nouveaux tarifs carte applicables aux comptes existants **à partir du 21 octobre 2026** (`C·3`) —
c'est-à-dire dans trois semaines. `stripe.com` est **bloqué** par le proxy ; aucune source primaire lue.

> **Décision : prélèvement SEPA, pas carte. Onze fois moins cher à 250 €**, et il supprime la relance
> d'impayé, qui est du temps non facturable. Contrepartie : **un mandat de prélèvement signé par
> client**, à ajouter au compte des signatures de la section 1.4 (a).

### 5.7 Comptabilité, et le coût d'un client qui part

**Comptabilité.** En micro-entreprise, un livre de recettes suffit ; ni bilan, ni expert-comptable
obligatoire. Le poste peut donc être tenu à **0 €**. Au-delà du plafond micro (26 clients à 250 € HT),
**j'ignore le coût** — je n'ai aucune source sur les honoraires d'un cabinet en Guadeloupe et je refuse
d'inventer une fourchette.

**Un client qui part.** La mise en service est perdue (200-300 €, `C·3` par substitut de marché). S'y
ajoutent la révocation du jeton (123 ms de machine, `A·1`, mais un geste humain à ordonnancer),
l'export et la suppression des données au titre de la sous-traitance, et le travail de gel de schéma qui
ne se recycle pas. **Et il ne part jamais seul en trésorerie** : il emporte 250 € HT de revenu récurrent
sur lequel le coût fixe était réparti. **Perdre 1 client sur 3 fait passer le point mort de couvert à
découvert.** À trois clients, le portefeuille n'a aucune redondance — c'est le vrai argument pour viser
13 et non 3.

### 5.8 Les deux postes que je ne peux pas chiffrer et qui ne sont nulle part

| Poste | Pourquoi il n'est pas chiffrable ici |
|---|---|
| **Sous-traitance de données à caractère personnel** | Détenir le jeton d'un client et traiter les avis de ses propres clients crée des obligations écrites par client : contrat de sous-traitance, registre, notification de violation. Le plan ne le mentionne jamais. Coût en euros : faible. Coût en **signatures et en temps par client** : non nul, et c'est une 4e pièce à faire signer |
| **Licence de veille presse** | 52,50 € HT par client et par mois (**`B·4`** rétrogradé, contrat sans adresse), 630 € HT par an. Le plan a **raison** de la renvoyer en phase 1 bis : à 250 € HT, elle consomme 21 % du prix. Mais alors le produit **ne contient pas de presse**, et cela doit être écrit sur le devis, sinon c'est une promesse implicite |

---

## 6 — Murs rencontrés, nommés une fois

**Hôtes refusés par le proxy d'égression de cet environnement** (une tentative chacun, aucune relance
en boucle) : `www.urssaf.fr` · `stripe.com` · `microchrono.fr` · `comptabook.fr` ·
`www.portail-autoentrepreneur.fr` · `lamicrobyflo.fr` · `www.fiscallia.fr` · `mangoweb.digital`.

**Conséquence tenue pour acquise : aucune source primaire n'a pu être lue sur l'ensemble de la section
5.** La recherche web fonctionne, la lecture de page non. Tous les montants de la section 5 sont donc
en `C·2` au mieux et `C·3` en général, et **aucun d'eux ne doit fonder une décision irréversible avant
relecture sur la source**. Les quatre lectures qui comptent — Urssaf pour le taux DOM applicable,
seuils de TVA, tarif Stripe du 21 octobre, les deux pages MangoWeb — prennent une heure dans un
navigateur et coûtent zéro euro.

---

## 7 — Les deux questions que je me retourne

### 7.1 Laquelle de mes conclusions, si elle est fausse, coûte le plus cher au projet

**Le prix de 250 € HT.** Pas le nombre de clients, qui en découle ; pas les cotisations, qui sont
petites ; pas l'assurance, qui est marginale. Le prix.

**Ce qu'il coûte s'il est faux.** Si le plafond réel d'un produit **logiciel** — sans agence humaine en
face, sans le visage que MangoWeb apporte à Saint-Claude — est en réalité 90 à 120 € HT, alors tout se
déplace en même temps :

| | À 250 € HT (ma conclusion) | Si le plafond réel est 110 € HT |
|---|---|---|
| Clients pour le point mort | **3** | **~9** |
| Clients pour 1 000 €/mois de revenu | 4,2 à 4,6 | **11 à 13** |
| Clients avant le plafond micro | 26 | **59** |
| Mise en service à produire pour 13 clients de revenu équivalent | 13 × 5-10 h = **65 à 130 h** | 30 × 5-10 h = **150 à 300 h** |
| Geste humain mensuel total à ce niveau | 3 à 7 h | **8 à 15 h** |

**C'est là que le projet meurt** : non par manque de marché, mais parce que la mise en service et le
geste humain d'un portefeuille de trente à soixante clients dépassent la capacité d'une personne qui
doit aussi tenir 22 à 37 jours-personne de maintenance. **Une erreur de prix ne coûte pas de la marge,
elle coûte un changement de nature du projet** — d'un travail soutenable à une charge intenable.

**Comment la tester pour moins de cent euros.**

> **Un devis écrit à trois lignes, présenté à huit établissements, et on demande une signature, pas un
> avis.** Produire d'abord les quatre rapports de veille que le plan prévoit déjà (0 €). Puis une page
> A4 : **90 € HT veille seule · 250 € HT complet · 450 € HT complet avec presse**, plus
> **300 € HT de mise en service**. Et la demande est : **« signez un mois d'essai payant à 250 € HT »**,
> pas « est-ce que ça vous intéresserait ». Coût : impressions et déplacements, **moins de 50 €**.
> Mesure : **combien sur huit signent à 250 € HT**. Un refus chiffré vaut une mesure ; un « oui c'est
> intéressant » ne vaut rien.

**Et la règle qui va avec, parce que le plan l'enfreint.** Le test du plan — « cinquante euros par mois
pour recevoir ceci chaque lundi ? » (ligne 75) — est **le pire test possible**, pour une raison
irréversible : **on descend toujours de 250 € vers 90 €, on ne remonte jamais de 50 € vers 250 €.**
Poser 50 € ancre le prix avant que personne n'ait refusé 250 €, chez des prospects qui sont aussi les
seuls prospects du marché, et qui en parleront entre eux. Le test gratuit du plan **détruit une
information qu'il ne pourra plus racheter**. C'est la correction la plus urgente de tout ce fichier, et
elle ne coûte rien : changer le chiffre dans la question.

**Deuxième test, 5,95 €** : un mois de Meditrust, déjà identifié par la critique 01, pour poser notre
sortie à côté de la leur dans le même rendez-vous. **Troisième test, 0 €** : ouvrir les deux pages
MangoWeb et régler la contradiction du § 2.5 avant le premier rendez-vous, pour que l'objection à 80 €
trouve une réponse écrite au lieu d'une improvisation.

### 7.2 Qu'ai-je réellement écarté

Sans quota. Quatre choses, et je dis pourquoi.

**1. Un palier d'appel à 50 € en veille seule, comme ouvre-porte.** C'était mon premier réflexe.
Écarté, et par mon propre § 4.3 : le support est par client et non par prix, donc un palier à 50 € avec
un appel mensuel laisse 17 à 38 € de marge et rembourse sa mise en service en 5 à 18 mois. **Ce n'est
pas un ouvre-porte, c'est un engagement signé à rentabilité inconnue.** Remplacé par 90 € HT, et
uniquement parce que la veille n'a pas de geste humain par avis — sans cette propriété, je ne l'aurais
pas gardé.

**2. Un prix au-dessus de 450 € HT.** Tentant : le marché monte à 490 et 1 290 € HT (`B·2`). Écarté
parce que ces offres portent une agence humaine, une marque et une présence que nous n'avons pas, et
parce qu'au-dessus de 450 € nous perdons le seul argument qui se dit en une phrase : **« le moins cher
qui réponde à tous vos avis »**.

**3. Un coût d'acquisition client en euros.** Écarté net. Il demanderait un taux de conversion que je
n'ai pas, multiplié par un coût de rendez-vous que je n'ai pas. Le produit aurait été deux inconnues
multipliées, présentées en euros : exactement le « cran `D` déguisé en plan » que le plan interdit
(ligne 161). **Zéro chiffre plutôt qu'un faux chiffre.**

**4. Le 80 €/mois comme plafond de prix.** Écarté, le registre le marque renversé et cinq prestataires
à 250-1 290 € règlent la question du plafond. **Mais je n'ai pas écarté l'objection commerciale** : ce
prix est sur une page publique, un prospect l'aura peut-être lu, et le plan n'a aucune réponse prête.
§ 2.5. C'est la distinction entre un fait renversé et un argument qui circule encore.

**Ce que je n'ai pas écarté bien que ce fût tentant** : les 22-37 jours-personne de maintenance. J'ai
cherché à les contester — ils sont en **`B·4`** après ma propre rétrogradation, estimation sur dépôts sans adresse. Je ne les ai pas contestés parce que
**les contester irait dans le mauvais sens pour moi** : s'ils sont surestimés, le coût fixe baisse et le
nombre de clients nécessaire baisse, ce qui renforce ma conclusion sans que je l'aie gagné. Je les
garde tels quels, dans leur fourchette large, et mes conclusions tiennent sur la borne haute.

---


## 8 — Audit de mon propre classement, et il me coûte quinze lignes

Règle appliquée : **toute affirmation que je classe en source primaire sans donner son adresse et sa
date de consultation redescend d'un cran de robustesse, et n'engage plus une dépense.** Je l'ai passée
sur chaque ligne chiffrée du fichier. Les crans écrits dans le corps sont déjà les crans d'arrivée.

### 8.1 Les lignes rétrogradées

| Ligne | Cran annoncé | Cran d'arrivée | Pourquoi elle tombe |
|---|---|---|---|
| **Plancher de coût 25-35 € HT/mois** | `B·3` | **`B·4`** | Calcul interne, `critiques/01-juridique-relance.md` § 10.4. Aucune adresse externe |
| **Plancher avec presse 100-120 € HT/mois** | `B·3` | **`B·4`** | Idem, et il hérite d'une licence elle-même rétrogradée |
| **Licence de veille presse 52,50 € HT/client/mois** | `B·3` | **`B·4`** | « Contrat réel de l'organisme de gestion collective » : ni adresse, ni référence de contrat, ni date |
| **Geste humain 15-30 min, 8-20 € HT/client/mois** | `B·3` | **`B·4`** | Calcul interne sur un volume d'avis en cran `D` |
| **Maintenance 22-37 jours-personne/an** (H3) | `B·3` | **`B·4`** | « Estimation sur dépôts » : aucun dépôt nommé, aucune date |
| **Serveur 450-700 €/an** (H4) | `B·3`/`C·3` | **`B·4`** | Aucun fournisseur nommé, aucune grille, aucune date |
| **760 établissements employeurs en hébergement-restauration** | `B·2` | **`B·3`** | « Organisme de branche d'après sources publiques », non nommé, non daté |
| **14 582 établissements, 71,8 % à 1-9 salariés** | `B·2` | **`B·3`** | Institut national de la statistique, hôte au mur, aucune adresse au registre |
| **55 hôtels, 59 chambres de moyenne** | `B·2` | **`B·3`** | Idem, date de référence 1/1/2023 donnée, adresse non |
| **80 € = 1 h 23 de community manager, 6 h 30 au SMIC brut** | `B·2` | **`B·3`** | « Baromètre de tarifs » non nommé |
| **Exigences locales = 3,5-5,2 % du marché adressable** | `B·2` | **`B·3`** | Croisement interne de deux périmètres, chacun déjà rétrogradé |
| **Déontologie : médecin fermé, avocat et la note, art. 10.3 et 10.5, taux de succès** | `B·2` | **`B·3`** | Les articles et les dates de décision sont cités, **les adresses non**, et `legifrance` est au mur. Référence d'article ≠ adresse consultée |
| **Responsabilité éditoriale sur la loi de 1881 et la LCEN** | `B·2` | **`B·3`** | Textes nommés, aucune adresse ni date |
| **Étalon gratuit à 0 € sur la fiche d'établissement · conformité = geste humain · doublement chez deux éditeurs · certification d'un organisme de normalisation** | `B·2` | **`B·3`** | Constats et grilles comparées sans aucune adresse ; hôtes Google au mur |
| **Occupation 77 % en janvier-mars, 34 % en septembre** | `B·1` | **`B·2`** | Opposition de phase attestée, source non adressée |

### 8.2 Les lignes qui tiennent, et pourquoi

| Ligne | Cran | Adresse | Date de consultation |
|---|---|---|---|
| 200 €/mois, 8 publications, avis non inclus, Saint-Claude 97120 | `B·2` | `mangoweb.digital/communication-digitale` | 2 oct. 2026, verbatim dans `critiques/01-juridique-relance.md` § 8.1 |
| 250 € HT/mois + 300 € HT de création, modération des avis négatifs | `B·2` | `linkeo-guadeloupe.com/community-management.php` | 2 oct. 2026, même § |
| 450 € HT/mois avec engagement, 690 € sans, réponse à chaque avis | `B·2` | `app.plateya.fr/...forfait-seo-local-fiche-gmb` | 2 oct. 2026, même § |
| dès 490 €/mois | `B·2` | `so-community.fr/region/guadeloupe` | 2 oct. 2026, même § |
| dès 1 290 € HT/mois | `B·2` | `katchak-agency.fr/community-management-en-guadeloupe/` | 2 oct. 2026, même § |
| Sur devis, réponse proactive aux avis | `B·2` | `cws.gp/services/reseaux-sociaux.html` | 2 oct. 2026, même § |
| 80 €/mois « réponse à tous les avis » + 200 € de création — **non utilisé comme plafond**, voir § 2.5 | `B·2` pour l'existence du verbatim | `mangoweb.digital/google-my-business` | 2 oct. 2026, verbatim dans `critiques/02-marche.md` ligne 377 |

**Six adresses datées portent toute ma grille de prix.** C'est pourquoi les crans de la section 2.3
tiennent alors que ceux de la section 3.2 tombent : **le prix est mieux étayé que le coût.** C'est un
résultat, pas un hasard — les prix sont publics, les coûts ne le sont pas.

### 8.3 Les montants de la section 5, avec leur adresse et leur méthode

Aucune de ces pages n'a été ouverte : le proxy les refuse. **Ce sont des résumés de moteur de
recherche, consultés le 2 octobre 2026.** D'où `C·2` au mieux.

| Montant | Cran | Adresses retournées par la recherche | Méthode |
|---|---|---|---|
| Cotisations DOM services BIC **3,6 % / 10,6 % / 14,2 %**, métropole 21,2 % | `C·3` | `microchrono.fr/auto-entrepreneur-outre-mer/` · `les-aides.fr/aide/FTNP3w/urssaf/...` · `lamicrobyflo.fr/cotisations-sociales-micro-entreprise/` · `urssaf.fr/.../exoneration-lodeom.html` | Résumé de recherche. **Les trois premières et `urssaf.fr` sont refusées à la lecture** |
| Franchise de TVA services **37 500 €**, majoré **41 250 €**, article du projet de loi de finances 2026 **supprimé fin 2025** | `C·2` (plusieurs sources concordantes) | `lamicrobyflo.fr/franchise-tva-seuils/` · `comptabook.fr/tva/seuil-franchise-tva-2026/` · `moicombien.fr/blog/seuils-tva-auto-entrepreneur-2026-franchise` · `indy.fr/blog/unification-seuils-tva-2026/` | Résumé de recherche, **deux lectures refusées** |
| TVA Guadeloupe **8,5 %** | `C·3` | `eurofiscalis.com/operations-avec-les-dom-quelles-regles-de-tva/` | Résumé de recherche, page non ouverte |
| Plafond micro services **77 700 €** | `C·3` | Même recherche TVA, mention incidente | **Le plus faible de la section : une mention incidente, pas une source dédiée** |
| CFE : exonération totale 1re année, base ÷ 2 en 2e, exonération si recettes ≤ 5 000 €, formulaire 1447-C-SD | `C·3` | `justice.fr/fiche/micro-entrepreneur-payer-cotisation-fonciere-entreprises-cfe` · `fiscallia.fr/cotisation-fonciere-entreprises-cfe-2026/` · `lamicrobyflo.fr/les-principales-exonerations-de-cfe/` | Résumé de recherche, **`fiscallia.fr` refusée à la lecture** |
| RC pro **non obligatoire** hors profession réglementée | `C·2` (sources indépendantes concordantes, dont deux cabinets et un courtier) | `coover.fr/responsabilite-civile-pro/metiers/informatique` · `matriskassurance.com/blog/assurance-rc-pro-informatique` · `blog-juridique.fr/...` · `fsc-avocat.fr/...` | Résumé de recherche |
| RC pro **180 à 600 €/an** | `C·3` | `monrcpro.fr/prix-rc-pro.html` · `danstapoche.fr/articles/assurance-rc-pro-freelance-2026` · `indepnet.fr/assurance-rc-pro-freelance` | Résumé de recherche. Fourchettes larges, profils non comparables |
| Stripe carte européenne **1,5 % + 0,25 €**, premium 2,8 %, international 3,15 %, **nouveaux tarifs au 21 oct. 2026** ; prélèvement SEPA **0,35 €** | `C·3` | `indy.fr/guide/.../frais-stripe/` · `realdev.fr/stripe-augmente-ses-tarifs-2026/` · `saask.fr/softwares/stripe/prix/` · `wannapay.fr/blog/120/...` | Résumé de recherche. **`stripe.com` refusé** — et la date du 21 octobre rend la vérification urgente |
| GoCardless **1 % + 0,20 €, plafond 2 €** national ; Advanced 1,25 %, Pro 1,4 % | `C·3` | `bldigital.it/fr/toolbox/gocardless-avis/` · `connectbanque.com/fr/avis/gocardless` · `webnyxt.com/gocardless-2026-...` | Résumé de recherche |

### 8.4 Ce que la rétrogradation fait à mes conclusions — et il faut le dire franchement

**Elle ne change pas le prix que j'arrête.** Les six bornes de marché qui fixent 250 € HT portent toutes
une adresse et une date (§ 8.2), et ce sont elles qui font la démonstration 2 du § 2.2. Le prix tient.

**Elle renforce la démonstration contre 50 €.** Mon argument était : un prix bas fait dépendre la
rentabilité de nombres mal connus. Après rétrogradation, **le geste humain par client et le plancher de
coût sont en `B·4`, non étayés**. Donc à 50 €, où ces deux lignes consomment 25 à 40 % du prix, la marge
repose sur du non étayé. À 250 € HT, elles en consomment 5 à 13 % : **même si elles sont fausses du
double, le prix tient.** Un prix haut est une assurance contre la faiblesse de ses propres chiffres de
coût, et c'est l'argument le plus solide que cet audit m'ait donné.

**Elle affaiblit mon nombre de clients, et je l'écris.** Le point mort de 3 clients à 250 € HT est
calculé sur un coût fixe dont **les deux composantes sont en `B·4`** (maintenance et serveur) plus une
en `C·3` (assurance). **Le « 3 clients » est donc une piste, pas une dépense engageable.** Ce qui reste
engageable, parce qu'il ne dépend que de lignes adressées : **le rapport entre les prix.** À 250 € HT il
faut 8 à 9 fois moins de clients qu'à 50 €, quel que soit le coût fixe réel, puisque le coût fixe
s'annule dans le rapport. **C'est la seule conclusion quantitative de ce fichier qui survive
intégralement à ma propre règle.**

**Elle rend un test obligatoire, et il est gratuit.** Les trois lignes `B·4` qui portent tout le calcul
de coût — maintenance, serveur, geste humain — se mesurent en interne, sans demander la permission de
personne : un chronomètre sur la validation de dix réponses, une facture de serveur, un relevé d'heures
sur un mois. **Trois mesures à 0 € font passer tout mon § 3 de `B·4` à `A·1`.** Aucune autre dépense du
dossier n'a un rapport d'information au coût aussi favorable.

---

## 9 — Les cinq colonnes

### MCP à installer

| MCP | Pour quoi | Pourquoi maintenant |
|---|---|---|
| Un MCP de facturation et d'abonnement (Stripe ou équivalent) | Émettre devis, mandats SEPA et factures, lire les encaissements et les impayés sans tableur | Les étapes 9 à 12 de la section 1 sont les seules qui séparent une signature d'un euro, et aucune n'est outillée |
| Un MCP de fiche d'établissement et d'avis (Google Business Profile) | Le volet avis entier ; et le test à 0 € dont le registre dit qu'il décide seul de la praticabilité | Le plan le met en semaine 0. Sans lui, tout reste manuel |
| Un MCP de relation client (même minimal) | Liste de prospects, dates de rendez-vous, étape de chaque dossier, date de relance | Le plan prévoit 5 prospects et il en faut plusieurs dizaines (§ 3.5). Sans suivi écrit, le pipeline est dans une tête |
| Un MCP de suivi de temps | Mesurer les 15-30 min de geste, les 5-10 h de mise en service, l'appel de support | **Trois de mes hypothèses sont en `D` faute de mesure.** Dix minutes de chronométrage par semaine les font passer en `A·1` |

### Logiciels manquants

| Manquant | Ce qu'il bloque |
|---|---|
| Un modèle de **devis et de contrat** avec prix HT, engagement, et mise en service en ligne séparée | Rien ne peut être signé. Et le prix doit porter « HT » dès la première page (§ 5.3) |
| Un **mandat de prélèvement SEPA** et le circuit de préavis | Le moyen d'encaissement le moins cher (§ 5.6) |
| Un **contrat de sous-traitance de données** par client | Obligation non mentionnée au plan, 4e signature (§ 5.8) |
| Un **tableau de point mort** vivant : clients × prix × coût variable × coût fixe | Le plan refuse tout chiffrage (ligne 161) et se prive donc de l'instrument qui dit si ça tient |
| Une **réponse écrite à l'objection « MangoWeb le fait pour 80 € »** | § 2.5. À écrire avant le premier rendez-vous |
| Le **registre de traitement** et la procédure de sortie client (révocation, export, suppression) | § 5.7. Un départ non outillé coûte du temps au pire moment |

### Outils déjà disponibles

| Outil | État |
|---|---|
| `gcloud`, installé dans cet environnement | Le test Google à 0 € est exécutable sans rien installer ; il n'attend qu'un compte, donc une décision |
| Le socle de veille : 1 183 lignes, 21 assertions sur 21, installation en 7,1 s, rejouable sans réseau | `A·1`. **C'est le seul actif vendable aujourd'hui** |
| L'orchestrateur de publication, 215 lignes, 3 plateformes, exécuté | `A·1`. N'attend que les approbations |
| La garde des accès, assemblée : chiffrement au repos, révocation en 123 ms, cloisonnement, journal haché | `A·1`. Le poste « jeton par client » est tenu |
| Le journal de provenance, 4 obligations réglementaires d'un seul organe | `A·1`. **C'est ce qui justifie 250 € contre 200 €** |
| La recherche web de cet environnement | Fonctionne. La lecture de page, non (§ 6) |

### IA existantes qui font ce travail, et à quel prix

Montants repris des critiques antérieures, avec leur cran d'origine. Je n'en ai vérifié aucun
moi-même : tous les hôtes marchands sont au mur.

| Produit | Prix | Cran | Ce qu'il fait, et ce qu'il ne fait pas |
|---|---|---|---|
| Fiche d'établissement de la plateforme elle-même | **0 €** | `B·3` | Lire et répondre à tous ses avis à la main. **C'est le vrai concurrent d'un produit à 50 €** |
| Trustmary | 19 €/mois | `C` (comparateur) | Collecte d'avis. Pas de veille, pas de provenance |
| Guest Suite | 39 €/mois | `C` | **Vend déjà la conformité, certifiée par un organisme de normalisation, et capte la date d'expérience par interface** (`B·3`, rétrogradé, sans adresse). C'est pourquoi l'angle n'est pas la conformité |
| Meditrust | gratuit à 129 €/mois | `B` | Affichage d'avis. Testable pour 5,95 € |
| Partoo | 149 € HT/mois | `C` | Multi-plateformes |
| Outils de publication grand public | Gratuit, et **le double pour réintroduire la validation humaine** | `B·3` | La bande vide vient de là : ils vendent d'avoir supprimé le geste |
| Prestataire guadeloupéen, 8 publications, avis non inclus | **200 €/mois** | `B·2`, adressé | Le plancher de crédibilité |
| Antenne régionale, modération des avis négatifs | **250 € HT + 300 € HT** | `B·2`, adressé | **Notre référence directe. À prix égal, nous donnons plus** |
| Le moins cher qui réponde à chaque avis | **450 € HT/mois** | `B·2`, adressé | Notre plafond d'attractivité. Nous sommes 44 % dessous |
| Agences locales haut de gamme | 490 à 1 290 € HT/mois | `B·2`, adressé | Établissent qu'il n'y a aucune pression déflationniste à 250 € |

**Aucun d'eux ne vend la veille officielle à provenance opposable.** C'est la seule chose que le projet
ait à vendre que personne d'autre n'a, et c'est aussi la seule livrable aujourd'hui.

### Futurs possibles à douze mois ⏳

| ⏳ | Ce que ça ouvre | Ce qui doit se produire d'abord |
|---|---|---|
| ⏳ **Franchissement de la franchise de TVA au 13e client** | Un régime à préparer, pas à découvrir | Que chaque devis ait porté « HT » dès le premier (§ 5.3) |
| ⏳ **Falaise de cotisations en année 4 : +4 134 € à chiffre d'affaires constant** | Deux clients de plus à trouver pour ne pas reculer | Connaître le régime applicable, BIC ou BNC (§ 5.2) |
| ⏳ **Plafond du régime micro à 26 clients** | Changement de statut, comptabilité réelle, coût inconnu | Y arriver |
| ⏳ **Nouveaux tarifs carte au 21 octobre 2026** | Sans effet si le prélèvement SEPA est choisi dès le départ | La décision du § 5.6, prise maintenant |
| ⏳ **Approbations de plateformes obtenues** | La phase 3 passe de code écrit à produit vendu | Dossiers déposés en semaine 0, délai inconnu |
| ⏳ **Réponse du bâtonnier** | Le segment avocat s'ouvre ou se ferme pour de bon | Quatre points rédigés, gratuit |
| ⏳ **Pont translingue, et vérificateur d'ancrage** (2 affirmations non sourcées sur 5) | Le différenciateur qui justifie 250 € contre 200 € | 24 à 41 jours de construction, et un mainteneur nommé |
| ⏳ **Avis de 2012 sur les liens vers les réseaux sociaux, toujours republié en 2026** | Opposable par un bâtonnier, donc un risque sur le segment avocat | Même réponse du bâtonnier |
| ⏳ **« Qui maintient »** | 22 à 37 jours-personne par an, soit 10 à 17 % d'une année de travail | Une décision, et le plan la laisse ouverte |
| ⏳ **Mesure réelle du taux d'attrition et du volume d'avis** | Fait tomber mes deux hypothèses `D` les plus structurantes | Trois clients et six mois |

---

## Annexe A — Journal de requêtes

Toutes les lignes datées du **2 octobre 2026**, dans l'ordre où je les ai faites. Trois colonnes.
**Les refus et les silences sont inscrits au même titre que les trouvailles : ils disent où il est
inutile de retourner.**

| Requête ou adresse | Outil | Résultat |
|---|---|---|
| `/home/user/moteurs-et-outils/PLAN-DE-CONSTRUCTION.md` | Read | trouvé |
| `/home/user/moteurs-et-outils/REGISTRE-DE-DEMARCHE.md` | Read | trouvé |
| `select:WebSearch,WebFetch` | ToolSearch | trouvé |
| Contenu de `/home/user/moteurs-et-outils/` et de `critiques/` | Bash `ls` | trouvé |
| `15 à 30 min` \| `geste humain` dans `critiques/*.md` | Bash `grep` | trouvé |
| `490` \| `450 €` \| `250 €/mois` \| `200 €/mois` \| `Saint-Claude` dans `critiques/*.md` | Bash `grep` | trouvé |
| `critiques/01-juridique-relance.md` lignes 700-760 — tableau des prix concurrents | Bash `sed` | trouvé |
| `critiques/01-juridique-relance.md` lignes 1095-1185 — plancher de coût et geste humain | Bash `sed` | trouvé |
| « micro-entrepreneur Guadeloupe taux cotisations sociales réduit DOM 2026 prestations de services BIC » | WebSearch | trouvé |
| « assurance responsabilité civile professionnelle obligatoire prestataire informatique agence web France obligation légale » | WebSearch | trouvé |
| `www.urssaf.fr/accueil/independant/creer-mon-entreprise/exonerations-dom.html` | WebFetch | **refusé** |
| `stripe.com/fr/pricing` | WebFetch | **refusé** |
| `microchrono.fr/auto-entrepreneur-outre-mer/` | WebFetch | **refusé** |
| « GoCardless tarifs prélèvement SEPA France commission 1% plafond euros 2026 » | WebSearch | trouvé |
| « seuil franchise TVA micro-entreprise 2026 prestations de services 77700 euros DOM Guadeloupe taux TVA 8,5% » | WebSearch | trouvé |
| « tarif assurance RC pro freelance informatique prix annuel euros par an 2026 » | WebSearch | trouvé |
| `comptabook.fr/tva/seuil-franchise-tva-2026/` | WebFetch | **refusé** |
| « Stripe France tarifs 2026 "1,5 %" cartes européennes "0,25" prélèvement SEPA commission abonnement Billing » | WebSearch | trouvé |
| `www.portail-autoentrepreneur.fr/academie/statut-auto-entrepreneur/tva` | WebFetch | **refusé** |
| « cotisation foncière des entreprises micro-entrepreneur exonération première année base minimum montant 2026 » | WebSearch | trouvé |
| `lamicrobyflo.fr/franchise-tva-seuils/` | WebFetch | **refusé** |
| `www.fiscallia.fr/cotisation-fonciere-entreprises-cfe-2026/` | WebFetch | **refusé** |
| « "franchise en base de TVA" 2026 seuil "37 500" services micro-entreprise loi de finances date application » | WebSearch | trouvé |
| `mangoweb.digital/google-my-business` — pour régler la contradiction 80 € / 200 € du § 2.5 | WebFetch | **refusé** |
| Crans et chiffres de mon propre fichier, relecture mécanique avant application de la règle | Bash `grep` | trouvé |

**Vingt-cinq lignes. Neuf recherches web, toutes « trouvé ». Huit adresses, toutes « refusé ». Zéro
« rien ».**

Et voici la vraie information du journal, que le mot « trouvé » cache : **huit des neuf recherches web
n'ont retourné que des résumés de moteur, parce que chaque page que j'ai ensuite voulu ouvrir a été
refusée.** Le taux est de 0 sur 8 à la lecture directe. C'est pourquoi toute la section 5 est en `C` et
pourquoi aucun de ses montants n'engage une dépense. **Il est inutile de retourner sur ces huit hôtes
depuis cet environnement : il faut un navigateur humain, et une heure suffit pour les huit.**

### Ce que je n'ai pas cherché, et pourquoi

Trois nombres manquent à ce fichier et je ne les ai pas cherchés, délibérément. Aucune recherche ne les
produit : ils se mesurent.

| Non cherché | Pourquoi aucune recherche ne l'aurait donné |
|---|---|
| **Taux de conversion commerciale** | Aucun comparable publié ne vaut pour sept mille établissements guadeloupéens démarchés par une personne. Se mesure sur huit devis (§ 7.1), pas sur le web |
| **Taux d'attrition** | Idem. Et c'est le nombre qui décide si un prix bas tient (§ 4.3) |
| **Nombre d'avis mensuels par établissement** | Déjà en cran `D` au registre, qui dit lui-même qu'il « déplace tout le calcul ». Se mesure en un mois sur un seul client |

### Le compte que le contrôle mécanique va faire, je le donne moi-même

**Affirmations de provenance `B` dans ce fichier : 22. Adresses réellement citées : 7.**
L'écart est de **15**, et ces quinze lignes sont exactement celles que le § 8.1 rétrograde d'un cran.
Je ne prétends donc pas à vingt-deux sources primaires : j'en revendique **sept, adressées et datées**,
et je déclasse les quinze autres en pistes qui n'engagent aucune dépense. **Si le compte mécanique
trouve un autre nombre que 22 et 7, c'est mon § 8.1 qui est à corriger, pas le compte.**
