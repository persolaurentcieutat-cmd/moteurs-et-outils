# Prompt de lancement — Moteurs de collecte vérifiée et outils de publication
## Guadeloupe, cœur d'activité

Version 4 — 2 octobre 2026
Révisions successives après décisions de Laurent Cieutat :
— v2 : on construit ce qui n'existe pas en libre … la Guadeloupe est le cœur et non une cible
— v3 : le mur juridique n'est pas un mur mais **un péage à guichets** … ajout du cran de preuve D
— v4 : ajout du **guichet 6, l'accès ouvert déclaré**, oublié en v3 … le guichet 5 éclaté en trois degrés de risque … la qualification se fait **source par source**, non plateforme par plateforme

---

## 1. Ce qui est tranché

| Décision | Conséquence |
|---|---|
| Quand aucun équivalent libre n'existe, **on construit** | Le propriétaire cesse d'être un obstacle : il devient un **étalon** à égaler de façon mesurée |
| La **Guadeloupe est le cœur** | Ses contraintes deviennent des exigences de conception, pas des adaptations ultérieures |
| La vérifiabilité est **notre couche**, pas un achat | Elle porte son propre étalon, à inventer — personne ne le vend |
| L'accès aux données fermées passe par **un guichet, pas par la force** | La voie se choisit, se contractualise et se chiffre — elle ne se contourne pas |

---

## 2. Les deux obstacles — et ils ne sont pas de même nature

### 2.1 L'obstacle technique — franchi par la construction

Aucun outil libre ne fait le travail, ou le fait mal. C'est résolu par la méthode d'ingénierie en six temps, section 5.

### 2.2 L'obstacle d'accès — un péage à cinq guichets

Formulation corrigée en v3. Il n'y a pas de mur : il y a cinq voies d'accès licites ou risquées, et les acteurs du marché empruntent l'une d'elles. **Aucun ne passe à travers.** Choisir son guichet est une décision d'architecture et de modèle économique, prise en V1.

| Guichet | Mécanisme | Qui l'emprunte | Coût d'entrée | Verdict pour nous |
|---|---|---|---|---|
| **1 — Partenariat certifié** | La plateforme ouvre une connectivité officielle à des éditeurs validés, contractualisés, certifiés techniquement. Booking opère un programme partenaire connectivité ⏳ D | Gestionnaires d'avis et channel managers du secteur hôtelier ⏳ noms à établir en V1 | Élevé — contrat, certification, volume minimum ⏳ | **Hors de portée au départ.** À réexaminer à trois ans |
| **2 — Mandat du titulaire** | L'établissement possède l'accès à ses propres avis par son extranet. Il mandate un prestataire. Ce n'est pas de l'aspiration de tiers mais de l'agrégation pour le compte du propriétaire | Prestataires locaux, agences, consultants | Faible — contrat de mandat, et gestion rigoureuse des accès confiés | **Notre voie principale** |
| **3 — API ouverte sur demande** | La plateforme publie une interface, l'accès se demande et se valide. Google Business Profile fonctionne ainsi ⏳ D | Tout acteur, après validation | Gratuit à faible — délai et conformité à prévoir | **Retenue** |
| **4 — Licence de contenu** | On ne collecte pas gratuitement : on **paie le droit de collecter**. En France le Centre français d'exploitation du droit de copie gère les droits de panorama de presse ⏳ D | Plateformes de veille et de revue de presse ⏳ | Abonnement selon usage et diffusion ⏳ | **Retenue pour la veille presse** |
| **5 — Accès de fait, sans ouverture déclarée** | Collecter ce qui est atteignable sans que l'éditeur ait dit qu'on pouvait | Nombre d'acteurs, de toutes tailles | Nul à l'entrée | **Éclaté en trois degrés** — section 2.3 |
| **6 — Accès ouvert déclaré** | L'éditeur a **voulu** que l'information soit reprise : données ouvertes publiques, licence explicite, flux publié exprès, interface publique sans condition restrictive | Tout le monde | Nul — obligations d'attribution et de débit respectueux | **Notre voie principale pour la collecte d'informations** |

### 2.3 Le guichet 5 éclaté — trois degrés, trois risques

Correction de la v3 : « zone grise » était un fourre-tout qui mélangeait des situations sans rapport. La qualification se fait **source par source**, jamais plateforme par plateforme.

| Degré | Situation | Risque | Verdict |
|---|---|---|---|
| **5a** | Atteignable, et **ouverture déclarée** — licence explicite, flux publié, fichier robots permissif | Ce n'est pas du guichet 5, c'est du **guichet 6** | **Retenu** |
| **5b** | Atteignable sans restriction technique ni authentification, et conditions d'utilisation **muettes** sur la réutilisation | Faible à moyen — à qualifier source par source | **Retenu sous conditions**, avec fiche de qualification |
| **5c** | Atteignable, mais conditions d'utilisation **interdisant** la réutilisation, ou recueil protégé par le droit sui generis, ou authentification et blocage à franchir | Fort | **Écarté** |

**Les conditions du 5b sont des règles de conception de notre collecteur, non des promesses.**
— Débit de collecte respectueux, jamais au point de nuire au service visé
— Aucun contournement de protection technique, d'authentification ni de limitation
— Pas de reproduction substantielle : on cite, on résume, on lie — on ne republie pas le recueil
— Provenance conservée sur chaque élément capté, et rejouable
— Retrait sous demande de l'éditeur, procédure écrite et tenue

### 2.4 Le guichet 6 — ce que la v3 avait oublié

C'est l'angle mort corrigé en v4, et il change le volet collecte d'informations.

Des sources **veulent** être reprises et le déclarent. Elles ne relèvent d'aucune zone grise :

| Famille | Exemples à établir en V0 | Ce qui subsiste comme obligation |
|---|---|---|
| Données ouvertes publiques | Portails d'État et de collectivités, institut national de la statistique, portails des collectivités guadeloupéennes ⏳ D | Attribution selon la licence |
| Licences explicites de réutilisation | Creative Commons, Licence Ouverte française ⏳ D | Attribution, parfois partage à l'identique |
| Flux publiés exprès pour être consommés | Flux RSS et Atom de la presse et des institutions | Respect du cadre de citation, pas de republication intégrale |
| Interfaces publiques sans condition restrictive | À établir source par source | Débit, et lecture des conditions |
| Communs documentaires | Encyclopédies et bases cartographiques libres ⏳ D | Attribution, partage à l'identique selon les cas |

**Ce que cela débloque, et ce que cela ne débloque pas.**
— **Débloqué** : une part probablement importante du corpus guadeloupéen institutionnel et de presse pour le volet veille et collecte vérifiée ⏳ proportion à établir en V0. C'est le cœur des moteurs, donc c'est décisif
— **Non débloqué** : les avis de plateformes. Ils relèvent du 5c, donc le **guichet 2, le mandat du titulaire, reste la seule voie** pour ce volet

Autrement dit : la correction de la v4 ouvre largement le volet moteurs de collecte, et laisse le volet avis exactement où il était.

### 2.5 Les deux décisions qui expliquent pourquoi le degré 5c est un pari

⏳ Citées de mémoire, cran D. Vérification sur source primaire obligatoire en V1.

**Ryanair contre PR Aviation**, Cour de justice de l'Union européenne, 2015 — une base de données non protégée par le droit d'auteur ni par le droit sui generis peut **tout de même être protégée par le contrat**. Les conditions d'utilisation suffisent à interdire, même sans protection légale sur le recueil. Cet arrêt ferme l'argument « ces données sont publiques donc libres ».

**Newspaper Licensing Agency contre Meltwater**, Royaume-Uni, début des années 2010 — un acteur majeur de la veille média a dû prendre licence pour ses revues de presse. Réponse directe à la question « comment font les outils de veille » : **ils ne contournent pas, ils paient.**

### 2.6 Pourquoi le degré 5c est écarté — motifs d'affaires, non de morale

— Un socle illicite ne passe aucune revue de diligence, ne se vend pas à un groupe hôtelier, ne se revend pas
— Il casse le jour où une plateforme modifie ses défenses techniques, sans préavis et sans recours
— Il expose à la responsabilité contractuelle, au droit sui generis des bases, au RGPD dès qu'un avis porte un prénom, et au parasitisme en droit français
— Il nous met dans la catégorie des aspirateurs, exactement celle dont nous voulons nous distinguer

### 2.7 Le retournement stratégique — l'accès licite est notre avantage

Les grands acteurs aspirent parce qu'ils **n'ont pas de relation client**. Ils vendent à distance à des milliers de comptes qu'ils ne rencontreront jamais : demander un mandat créerait une friction qui les tuerait.

Notre position est l'inverse. En Guadeloupe, le client nous connaît, ou connaît quelqu'un qui nous connaît. Il confie ses accès parce que nous sommes son prestataire local et non une adresse web. **La proximité est la clé du guichet 2.** Aucun concurrent mondial ne peut l'ouvrir.

Conséquence de conception : le produit est **nativement un outil sous mandat**. Cela impose une gestion des accès confiés au niveau d'un établissement bancaire — chiffrement, révocation, journalisation, cloisonnement par client. Ce n'est pas une option, c'est le socle de la confiance qui nous donne l'accès.

---

## 3. La Guadeloupe en cœur — six exigences non négociables

Elles disqualifient directement des outils. Tout agent qui les ignore voit son retour rejeté.

| Exigence | Contenu | Ce qu'elle disqualifie |
|---|---|---|
| **Fuseau** | UTC-4 toute l'année, sans heure d'été — 5 h de décalage avec la métropole en hiver, 6 h en été | Tout outil de programmation raisonnant en heure métropolitaine |
| **Langues** | Français, créole guadeloupéen, anglais et espagnol dans les avis de croisiéristes | Tout moteur d'extraction ou d'analyse monolingue français |
| **Saisons** | Saison cyclonique du 1er juin au 30 novembre … carnaval de l'Épiphanie au Mercredi des Cendres … haute saison touristique ⏳ à confirmer | Un produit à charge constante — les pics de publication et de réponse aux avis sont saisonniers |
| **Sources locales** | Presse, institutions, chambres, collectivités — à recenser, absentes des corpus génériques | Tout moteur de découverte livré avec un corpus métropolitain |
| **Tissu économique** | Très petites entreprises en majorité ⏳ à confirmer en V0 | Tout produit exigeant un administrateur, ou dépassant le prix plafond local |
| **Droit** | Région ultrapériphérique de l'Union — RGPD plein, droit français | Tout hébergement ou traitement non conforme |

**L'avantage à défendre.** Aucun acteur mondial ne construit à cette échelle de marché, et aucun ne peut ouvrir le guichet 2. C'est ce qui rend la position tenable, et ce qui interdit de copier un produit métropolitain.

---

## 4. Doctrine de preuve

### 4.1 Le barème — quatre crans

| Cran | Définition | Sort |
|---|---|---|
| **A — mesure** | L'agent a mesuré contre l'étalon, sur le jeu d'épreuve figé, et colle les chiffres des deux côtés | Cran le plus haut. Entre au livrable |
| **A — usage** | L'agent a installé ou appelé l'outil, et colle la sortie réelle | Entre au livrable |
| **B** | Document primaire cité avec URL et date de consultation — fichier LICENSE du dépôt, documentation officielle, texte de loi, décision de justice | Entre au livrable, marqué B |
| **C** | Billet de blog, comparatif, page marketing, affirmation du vendeur | **Va au dépôt** |
| **D — mémoire du modèle** | Ce que l'agent croit savoir, sans vérification dans la session | **Piste de recherche uniquement.** Interdit en livrable. Jamais fondement d'une décision |

**Pourquoi le cran D existe.** C'est le cran le plus dangereux du barème : il a l'assurance du A et la fiabilité du C. La connaissance d'un modèle porte une date de coupure, et les conditions d'accès aux plateformes changent tous les six mois. Un agent qui restitue sa mémoire sans la marquer D fabrique du faux vert.

Règle : **tout agent déclare ses lignes D en tête de retour, avant le contenu.** Un retour qui n'en déclare aucune est suspect et relancé.

### 4.2 Règles de rejet

— Tout retour sans ligne A ni B est relancé une fois. S'il revient en C ou D, il tombe
— **Aucune décision de construire ne se prend sur un cran B ou moins.** Décider de reconstruire exige un A-mesure sur le modèle repéré
— **Aucun choix de guichet ne se prend sur un cran D.** Le choix de la voie d'accès exige un B minimum, confirmé par un juriste pour le guichet 2

### 4.3 Interdictions explicites

— Jamais « populaire », « largement utilisé », « référence du marché » — ce ne sont pas des faits
— Jamais un compte d'outils pour montrer qu'on a cherché — trois briques tenues valent quinze listées
— Jamais « gratuit » pour ce qui est gratuit en version d'essai
— Jamais une évaluation d'outil sans confrontation aux six exigences guadeloupéennes
— Jamais « tel concurrent le fait donc c'est permis » — nommer son guichet, ou constater qu'il prend un risque
— Tout fait porte sa date, ou la marque ⏳ à confirmer

### 4.4 Le gabarit de fiche-organe

| Champ | Exigence |
|---|---|
| Organe visé | Lequel des sept de la section 6 |
| Modèle repéré | Nom, version, éditeur, licence ou statut propriétaire |
| **Guichet emprunté par ce modèle** | Lequel des six, degré précisé s'il s'agit du 5, et à quel coût — ou « inconnu », jamais une supposition |
| Étalon mesuré | Les chiffres obtenus au temps 2, sortie collée |
| Équivalent libre trouvé | Nom, licence SPDX lue dans le fichier LICENSE, date du dernier commit, nombre de mainteneurs |
| Écart à l'étalon | Chiffré, sur le jeu d'épreuve figé |
| Tenue des six exigences guadeloupéennes | Une ligne par exigence — tenue, non tenue, à vérifier |
| Verdict | Adopter tel quel … adapter … reconstruire … renoncer |
| Si reconstruire | Le manquant exact, et son coût en jours |
| Coût réel à l'échelle visée | Serveur, quotas, licence de contenu, maintenance humaine |
| Cran de preuve | A-mesure, A-usage, B, C ou D |
| Source | URL et date de consultation |

### 4.5 Les cinq colonnes de fin de réponse — obligatoires, sans exception

1. **MCP à installer** — nom, ce qu'il débloque, prérequis
2. **Logiciels manquants** — ce qu'il faut installer pour avancer
3. **Outils déjà disponibles** — ce qui est là et non exploité
4. **IA existantes** — ce qui fait déjà le travail aujourd'hui, et à quel prix
5. **Futurs possibles à douze mois** — ce qui arrive, marqué ⏳ puisque non advenu

---

## 5. La méthode d'ingénierie de reconstruction — six temps

S'applique à chaque organe sans équivalent libre. Aucune construction avant le temps 3.

| Temps | Geste | Sortie exigée | Rejet si |
|---|---|---|---|
| **1** | **Repérer le modèle** — le meilleur existant, propriétaire inclus | Un nom précis, une version, ce qu'il fait exactement, **et son guichet d'accès** | L'agent nomme une catégorie au lieu d'un produit |
| **2** | **Instrumenter le modèle** — le faire tourner sur un jeu d'épreuve réel guadeloupéen, par version d'essai ou compte de démonstration | Les chiffres observés, sortie collée | Les chiffres viennent de la documentation du vendeur |
| **3** | **Fixer l'étalon** — les métriques à égaler et le **jeu d'épreuve figé** qui jugera | Le contrat de mesure, écrit, daté, versionné | Le jeu d'épreuve n'est pas figé avant la construction |
| **4** | **Décomposer** — quels composants produisent ce résultat, lesquels existent libres, lesquels manquent | La liste du manquant, et elle seule | L'agent propose de tout réécrire |
| **5** | **Reconstruire le manquant seul** — au plus petit qui tient l'étalon | Le composant, et son coût réel en jours | La construction dépasse le manquant |
| **6** | **Prouver sur le même jeu d'épreuve** — même entrée, même métrique, comparaison chiffrée | Égalé … dépassé … ou écart chiffré et assumé | La comparaison change de jeu d'épreuve en route |

**Le pivot.** Le jeu d'épreuve doit être **guadeloupéen, réel, et figé avant toute construction**. Sans lui, « on fait aussi bien » est une opinion. Avec lui, c'est un chiffre opposable. Sa constitution est la première tâche du projet, en V0.

**Trois issues admises au temps 6.** Égaler, dépasser, ou rester en dessous en chiffrant l'écart et en disant ce qu'il coûterait de le combler. Un écart avoué nourrit l'arbitrage ; un écart masqué tue le produit.

---

## 6. Les étalons par organe

Seuils à fixer en V0 sur le jeu d'épreuve réel — les inventer maintenant serait de la fabulation.

| Organe | Métrique qui juge | Pourquoi celle-là |
|---|---|---|
| **Découverte** | Rappel sur corpus local figé … fraîcheur en heures entre publication et captation | Un moteur qui rate la presse locale est sans valeur ici |
| **Extraction** | Part de texte propre … taux d'erreur par champ sur les pages locales difficiles | C'est là que les outils génériques échouent |
| **Index** | Latence de réponse … pertinence sur requêtes figées … coût au million de documents | Le coût décide de la viabilité du modèle économique |
| **Provenance** | Part des assertions remontées à une source primaire … part datée … part rejouable à l'identique | Notre couche propre, donc notre étalon propre |
| **Rédaction** | Taux de reprise par un humain … nombre d'affirmations non sourcées par texte | Une seule affirmation fausse publiée détruit la confiance du client |
| **Publication** | Taux de publication réussie … délai … taux de rejet plateforme | Mesure la solidité réelle des prises |
| **Avis** | Part des avis captés sur ceux réellement présents … délai de détection … taux de réponse sous 24 h | C'est ce que le client paie |
| **Garde des accès confiés** | Chiffrement au repos … révocation effective en minutes … journal d'accès complet … cloisonnement entre clients | Nouveau en v3 : c'est la condition du guichet 2, donc de tout le produit |

---

## 7. Les relances automatiques

Parties avec chaque agent en fin de recherche, sans intervention.

### Relance 1 — anti-oubli

> Tu viens de rendre. Avant que je lise, réponds à trois questions, en nommant des objets, pas des intentions.
> Qu'as-tu oublié — cite trois candidats que tu as écartés et dis pourquoi.
> Que n'as-tu pas vu — nomme ce que tu n'as pas pu vérifier et ce qui t'a manqué pour le faire.
> Qu'est-ce qui rendrait ce produit plus profitable — nomme l'endroit exact où il perd de l'argent aujourd'hui, et le geste qui le corrige.
> Si tu n'as rien, écris « rien » et assume-le.

### Relance 2 — preuve, étalon et guichet

> Pour chaque ligne de ton retour : as-tu testé ? Avec quoi exactement — version, commande, environnement, date.
> Qu'as-tu obtenu — colle la sortie, pas ton résumé.
> Qu'as-tu validé par toi-même et qu'as-tu recopié d'ailleurs.
> Ton étalon est-il opposable — le jeu d'épreuve était-il figé avant la mesure, est-il guadeloupéen, et un tiers pourrait-il rejouer ta mesure à l'identique ?
> Pour chaque acteur que tu cites comme faisant déjà ce travail : par quel guichet accède-t-il à la donnée, à quel degré s'il s'agit du guichet 5, et comment le sais-tu ? Si tu ne le sais pas, écris-le.
> Reclasse chaque ligne en A-mesure, A-usage, B, C ou D. Toute ligne classée A sans sortie collée redescend en C. Tout étalon non rejouable redescend en B. Toute affirmation issue de ta seule mémoire redescend en D.

---

## 8. Les six vagues

Chaque vague s'arrête sur son livrable et attend validation. Une vague mal cadrée contamine les suivantes.

### V0 — Le terrain guadeloupéen et le jeu d'épreuve

Objet : savoir pour qui on construit, et se donner le juge de toutes les mesures à venir.

Agents :
— **Marché** — qui achète, combien ils sont, ce qu'ils utilisent déjà, ce qu'ils paient aujourd'hui
— **Sources locales** — presse, institutions, chambres, collectivités, et plateformes d'avis réellement utilisées en Guadeloupe
— **Jeu d'épreuve** — constituer le corpus figé : pages locales réelles, avis réels multilingues, requêtes types. Le versionner et le geler
— **Qualification des sources** — nouveau en v4. Pour chaque source locale recensée : son guichet, son degré s'il s'agit du 5, sa licence, ses conditions d'utilisation lues, et le verdict retenu ou écarté. Une fiche par source, pas par plateforme

Livrable : **le terrain, le juge, et le registre des sources qualifiées**.

### V1 — Les guichets, le droit, les licences

Vague la plus lourde en v3. Elle décide de la forme du produit.

Agents :
— **Cartographie des guichets** — pour chaque plateforme sociale et chaque plateforme d'avis : quels guichets existent, lesquels sont ouverts à un acteur de notre taille, à quel coût, avec quel délai
— **Acteurs en place et leur guichet** — identifier qui fait déjà ce travail, et **par quelle voie chacun accède à la donnée**. Interdiction de supposer : soit c'est documenté, soit c'est déclaré inconnu
— **Mandat du titulaire** — licéité, conditions, pièces à signer, obligations de garde des accès ⏳ confirmation juriste obligatoire
— **Licences de contenu** — ce que coûte le droit de collecter la presse, et auprès de qui
— **Licences logicielles** — familles de licences et ce qu'elles permettent pour un produit commercial hébergé ; pièges du copyleft en service distant
— **Conformité** — RGPD appliqué aux avis nominatifs et à l'indexation de contenus tiers ; hébergement conforme

Livrable : **la carte des guichets** — guichet retenu par plateforme, coût, délai, pièces contractuelles, et le verdict juriste sur le mandat.

### V2 — Les organes de collecte et leurs étalons

Objet : appliquer les six temps à chacun des quatre organes de collecte.

Agents, un par organe : découverte … extraction … index et stockage … chaîne de provenance.

Consigne : trois candidats tenus au maximum, mesurés contre l'étalon sur le jeu d'épreuve de V0, confrontés aux six exigences.

Livrable : **le banc d'essai chiffré**.

### V3 — Les prises et leurs substituts construits

Objet : publication sociale et avis, plateforme par plateforme, **après le verdict de V1**.

Agents :
— **Publication sociale** — plateformes atteignables par guichet retenu, briques libres d'orchestration, et ce qu'il faut construire pour les manquantes
— **Avis** — recensement exhaustif des plateformes pertinentes en Guadeloupe ; pour chacune : avis lisibles, réponse possible, par quel guichet
— **Garde des accès confiés** — l'organe nouveau de la v3 : comment on détient les identifiants d'un client sans trahir sa confiance

Livrable : **le tableau des prises** — plateforme, guichet, prix d'entrée, risque de coupure, substitut à construire.

### V4 — Rédaction, blog, façade

Objet : la pile qui transforme la collecte en publication, sous les six exigences.

Agents : rédaction assistée et sourcée … blog et site … application professionnelle … hébergement conforme.

Livrable : **la pile technique**, avec son écart à l'étalon pour chaque organe reconstruit.

### V5 — Assemblage et arbitrage

Sorties : l'architecture retenue … la chaîne MCP … le chiffrage à un an, **licences de contenu incluses** … le périmètre tenable en quatre-vingt-dix jours … **l'ordre de construction** … ce qui part au dépôt et pourquoi.

Livrable : **l'architecture arbitrée**.

---

## 9. Ce que ce prompt refuse de produire

— Un panorama d'outils sans mesure
— Une décision de construire sans étalon mesuré sur le modèle repéré
— Une mesure sur un jeu d'épreuve non figé, ou non guadeloupéen
— Une évaluation d'outil sans confrontation aux six exigences
— Un acteur cité comme référence sans que son guichet d'accès soit nommé ou déclaré inconnu
— Une source qualifiée en bloc avec sa plateforme, au lieu d'être qualifiée pour elle-même
— L'étiquette « zone grise » employée sans préciser le degré 5a, 5b ou 5c
— Une architecture avant la carte des guichets
— Un chiffrage avant le banc d'essai

Si la matière manque, l'agent le dit avant de produire. Un retour honnêtement vide vaut mieux qu'un retour plein de C.

---

## 10. Nœuds encore ouverts — décisions attendues de Laurent

| Nœud | Question | Pourquoi c'est bloquant |
|---|---|---|
| **Produit sous mandat** | Le guichet 2 fait du produit un outil qui détient les accès de ses clients. L'acceptes-tu, avec les obligations de garde que cela impose ? | Cela change la nature du produit et ajoute un organe à construire |
| **Licences de contenu** | Es-tu prêt à payer un droit de collecte pour la veille presse, ou renonce-t-on à la presse locale au départ ? | Change le chiffrage et le périmètre de V0 |
| **Façades** | Façade professionnelle d'abord, grand public ensuite ? Ou les deux en parallèle ? | Les deux en parallèle double le périmètre |
| **Qui construit** | Toi seul avec moi ? Une équipe ? Un budget de développement ? | Reconstruire un organe se compte en semaines — fixe ce qui est tenable |
| **Budget temps** | Quel horizon pour une première version utilisable par un vrai client guadeloupéen ? | Fixe l'ordre de construction de V5 |
