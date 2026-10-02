# Prompt de lancement — Moteurs de collecte vérifiée et outils de publication
## Guadeloupe, cœur d'activité

Version 2 — 2 octobre 2026
Révision après deux décisions de Laurent Cieutat : **on construit ce qui n'existe pas en libre** … **la Guadeloupe est le cœur d'activité, pas une cible**.

---

## 1. Ce qui est tranché

| Décision | Conséquence |
|---|---|
| Quand aucun équivalent libre n'existe, **on construit** | Le propriétaire cesse d'être un obstacle : il devient un **étalon** à égaler de façon mesurée |
| La **Guadeloupe est le cœur** | Ses contraintes deviennent des exigences de conception, pas des adaptations ultérieures |
| La vérifiabilité est **notre couche**, pas un achat | Elle porte son propre étalon, à inventer — personne ne le vend |

---

## 2. Ce que ces décisions ne résolvent pas — les deux murs

Construire franchit un mur sur deux. Confondre les deux ferait perdre une vague entière.

| Mur | Nature | Franchi par la construction ? | Voie |
|---|---|---|---|
| **Technique** | Aucun outil libre ne fait le travail, ou le fait mal | **Oui** | Méthode d'ingénierie en six temps, section 4 |
| **Juridique et contractuel** | API fermée, conditions d'utilisation interdisant l'aspiration, droit européen des bases de données protégeant un recueil d'avis | **Non** — un collecteur reconstruit qui viole des conditions reste illicite | Trouver une voie d'accès licite, ou renoncer au volet |

**Cas des avis — l'ingénierie est juridique avant d'être technique.**
Reconstruire un collecteur ne crée aucun droit d'accès. La voie qui existe est d'une autre nature : **l'établissement a accès à ses propres avis** par son extranet de plateforme. Une collecte **mandatée par le client**, avec ses identifiants et son consentement écrit, relève de l'agrégation pour le compte du titulaire et non de l'aspiration de tiers.
⏳ À faire confirmer par un juriste en V1. Aucune ligne de code avant cette confirmation.

---

## 3. La Guadeloupe en cœur — six exigences non négociables

Ces exigences disqualifient directement des outils. Elles s'appliquent à chaque brique évaluée, et tout agent qui les ignore voit son retour rejeté.

| Exigence | Contenu | Ce qu'elle disqualifie |
|---|---|---|
| **Fuseau** | UTC-4 toute l'année, sans heure d'été — 5 h de décalage avec la métropole en hiver, 6 h en été | Tout outil de programmation raisonnant en heure métropolitaine |
| **Langues** | Français, créole guadeloupéen, anglais et espagnol dans les avis de croisiéristes | Tout moteur d'extraction ou d'analyse monolingue français |
| **Saisons** | Saison cyclonique du 1er juin au 30 novembre … carnaval de l'Épiphanie au Mercredi des Cendres … haute saison touristique ⏳ à confirmer | Un produit à charge constante — les pics de publication et de réponse aux avis sont saisonniers |
| **Sources locales** | Presse, institutions, chambres, collectivités — à recenser, absentes des corpus génériques | Tout moteur de découverte livré avec un corpus métropolitain |
| **Tissu économique** | Très petites entreprises en majorité ⏳ à confirmer en V0 | Tout produit exigeant un administrateur, ou dépassant le prix plafond local |
| **Droit** | Région ultrapériphérique de l'Union — RGPD plein, droit français | Tout hébergement ou traitement non conforme |

**L'avantage à défendre.** Aucun acteur mondial ne construit à cette échelle de marché. C'est précisément ce qui rend la position tenable, et ce qui interdit de copier un produit métropolitain.

---

## 4. La méthode d'ingénierie de reconstruction — six temps

S'applique à chaque organe pour lequel aucun équivalent libre n'est trouvé. Aucune construction ne démarre avant le temps 3.

| Temps | Geste | Sortie exigée | Rejet si |
|---|---|---|---|
| **1** | **Repérer le modèle** — le meilleur existant, propriétaire inclus | Un nom précis, une version, ce qu'il fait exactement | L'agent nomme une catégorie au lieu d'un produit |
| **2** | **Instrumenter le modèle** — le faire tourner sur un jeu d'épreuve réel guadeloupéen, par version d'essai ou compte de démonstration | Les chiffres observés, sortie collée | Les chiffres viennent de la documentation du vendeur |
| **3** | **Fixer l'étalon** — les métriques à égaler et le **jeu d'épreuve figé** qui jugera | Le contrat de mesure, écrit, daté, versionné | Le jeu d'épreuve n'est pas figé avant la construction |
| **4** | **Décomposer** — quels composants produisent ce résultat, lesquels existent en libre, lesquels manquent | La liste du manquant, et elle seule | L'agent propose de tout réécrire |
| **5** | **Reconstruire le manquant seul** — au plus petit qui tient l'étalon | Le composant, et son coût réel en jours | La construction dépasse le manquant |
| **6** | **Prouver sur le même jeu d'épreuve** — même entrée, même métrique, comparaison chiffrée | Égalé … dépassé … ou écart chiffré et assumé | La comparaison change de jeu d'épreuve en route |

**Le pivot de toute la méthode.** Le jeu d'épreuve doit être **guadeloupéen, réel, et figé avant toute construction**. Sans lui, « on fait aussi bien » est une opinion. Avec lui, c'est un chiffre opposable. Sa constitution est la première tâche du projet, en V0.

**Trois issues admises au temps 6, pas deux.** Égaler, dépasser, ou rester en dessous en chiffrant l'écart et en disant ce qu'il coûterait de le combler. Un écart avoué vaut mieux qu'un écart masqué, et il nourrit l'arbitrage.

---

## 5. Les étalons par organe

Métriques proposées. **Seuils à fixer en V0 sur le jeu d'épreuve réel** — les inventer maintenant serait de la fabulation.

| Organe | Métrique qui juge | Pourquoi celle-là |
|---|---|---|
| **Découverte** | Rappel sur corpus local figé … fraîcheur en heures entre publication et captation | Un moteur qui rate la presse locale est sans valeur ici |
| **Extraction** | Part de texte propre … taux d'erreur par champ sur les pages locales difficiles | C'est là que les outils génériques échouent |
| **Index** | Latence de réponse … pertinence sur requêtes figées … coût au million de documents | Le coût décide de la viabilité du modèle économique |
| **Provenance** | Part des assertions remontées à une source primaire … part datée … part rejouable à l'identique | Notre couche propre, donc notre étalon propre |
| **Rédaction** | Taux de reprise par un humain … nombre d'affirmations non sourcées par texte | Une seule affirmation fausse publiée détruit la confiance du client |
| **Publication** | Taux de publication réussie … délai … taux de rejet plateforme | Mesure la solidité réelle des prises |
| **Avis** | Part des avis captés sur ceux réellement présents … délai de détection … taux de réponse sous 24 h | C'est ce que le client paie |

---

## 6. Doctrine de preuve

### Le barème — trois crans, deux formes pour le premier

| Cran | Définition | Sort |
|---|---|---|
| **A — usage** | L'agent a installé ou appelé l'outil, et colle la sortie réelle | Entre au livrable |
| **A — mesure** | L'agent a mesuré contre l'étalon, sur le jeu d'épreuve figé, et colle les chiffres des deux côtés | Entre au livrable, c'est le cran le plus haut |
| **B** | Document primaire cité avec URL et date de consultation — fichier LICENSE du dépôt, documentation officielle, texte de loi | Entre au livrable, marqué B |
| **C** | Billet de blog, comparatif, page marketing, affirmation du vendeur | **Va au dépôt**, jamais au livrable |

Règle de rejet : tout retour sans ligne A ni B est relancé une fois. S'il revient en C, il tombe. Aucune exception.

Règle propre à la construction : **aucune décision de construire ne se prend sur un cran B.** Décider de reconstruire un organe exige un A-mesure sur le modèle repéré. On ne reconstruit pas ce qu'on n'a pas mesuré.

### Interdictions explicites

— Jamais « populaire », « largement utilisé », « référence du marché » — ce ne sont pas des faits
— Jamais un compte d'outils pour montrer qu'on a cherché — trois briques tenues valent quinze listées
— Jamais « gratuit » pour ce qui est gratuit en version d'essai
— Jamais une évaluation d'outil sans la confronter aux six exigences guadeloupéennes de la section 3
— Tout fait porte sa date, ou la marque ⏳ à confirmer

### Le gabarit de fiche-organe

| Champ | Exigence |
|---|---|
| Organe visé | Lequel des sept de la section 5 |
| Modèle repéré | Nom, version, éditeur, licence ou statut propriétaire |
| Étalon mesuré | Les chiffres obtenus au temps 2, sortie collée |
| Équivalent libre trouvé | Nom, licence SPDX lue dans le fichier LICENSE, date du dernier commit, nombre de mainteneurs |
| Écart à l'étalon | Chiffré, sur le jeu d'épreuve figé |
| Tenue des six exigences guadeloupéennes | Une ligne par exigence — tenue, non tenue, ou à vérifier |
| Verdict | Adopter tel quel … adapter … reconstruire … renoncer |
| Si reconstruire | Le manquant exact, et son coût en jours |
| Coût réel à l'échelle visée | Serveur, quotas, licence, maintenance humaine |
| Cran de preuve | A-mesure, A-usage, B ou C |
| Source | URL et date de consultation |

### Les cinq colonnes de fin de réponse — obligatoires, sans exception

1. **MCP à installer** — nom, ce qu'il débloque, prérequis
2. **Logiciels manquants** — ce qu'il faut installer pour avancer
3. **Outils déjà disponibles** — ce qui est là et non exploité
4. **IA existantes** — ce qui fait déjà le travail aujourd'hui, et à quel prix
5. **Futurs possibles à douze mois** — ce qui arrive, marqué ⏳ puisque non advenu

---

## 7. Les relances automatiques

Parties avec chaque agent en fin de recherche, sans intervention.

### Relance 1 — anti-oubli

> Tu viens de rendre. Avant que je lise, réponds à trois questions, en nommant des objets, pas des intentions.
> Qu'as-tu oublié — cite trois candidats que tu as écartés et dis pourquoi.
> Que n'as-tu pas vu — nomme ce que tu n'as pas pu vérifier et ce qui t'a manqué pour le faire.
> Qu'est-ce qui rendrait ce produit plus profitable — nomme l'endroit exact où il perd de l'argent aujourd'hui, et le geste qui le corrige.
> Si tu n'as rien, écris « rien » et assume-le.

### Relance 2 — preuve et étalon

> Pour chaque ligne de ton retour : as-tu testé ? Avec quoi exactement — version, commande, environnement, date.
> Qu'as-tu obtenu — colle la sortie, pas ton résumé.
> Qu'as-tu validé par toi-même et qu'as-tu recopié d'ailleurs.
> Ton étalon est-il opposable — le jeu d'épreuve était-il figé avant la mesure, est-il guadeloupéen, et un tiers pourrait-il rejouer ta mesure à l'identique ?
> Reclasse chaque ligne en A-mesure, A-usage, B ou C. Toute ligne classée A sans sortie collée redescend en C. Tout étalon non rejouable redescend en B.

---

## 8. Les six vagues

Chaque vague s'arrête sur son livrable et attend validation. Pas d'enchaînement automatique : une vague mal cadrée contamine les suivantes.

### V0 — Le terrain guadeloupéen et le jeu d'épreuve

Objet : savoir pour qui on construit, et se donner le juge de toutes les mesures à venir. Sans cette vague, tout le reste se mesure dans le vide.

Agents :
— **Marché** — qui achète, combien ils sont, ce qu'ils utilisent déjà, ce qu'ils paient aujourd'hui pour publier et gérer leurs avis
— **Sources locales** — recenser la presse, les institutions, les chambres, les collectivités, et les plateformes d'avis réellement utilisées en Guadeloupe
— **Jeu d'épreuve** — constituer le corpus figé : pages locales réelles, avis réels multilingues, requêtes types. Le versionner et le geler

Livrable : **le terrain et le juge** — la carte du marché, et le jeu d'épreuve figé.

### V1 — Les deux murs

Objet : séparer ce qui se reconstruit de ce qui se heurte au droit.

Agents :
— **Licences** — familles de licences et ce qu'elles permettent pour un produit commercial hébergé ; pièges du copyleft en service distant
— **Murs juridiques** — pour chaque plateforme sociale et chaque plateforme d'avis : condition d'accès, conditions d'utilisation, protection du recueil de données, et **la voie licite s'il en existe une**
— **Mandat client** — la collecte mandatée par le titulaire est-elle licite, sous quelles conditions, avec quelles pièces à signer ⏳ confirmation juriste requise
— **Conformité** — RGPD appliqué aux avis nominatifs et à l'indexation de contenus tiers ; hébergement conforme

Livrable : **la carte des deux murs** — reconstructible, accessible autrement, ou interdit.

### V2 — Les organes de collecte et leurs étalons

Objet : pour chacun des quatre organes de collecte, appliquer les six temps.

Agents, un par organe : découverte … extraction … index et stockage … chaîne de provenance.

Consigne : trois candidats tenus au maximum, mesurés contre l'étalon sur le jeu d'épreuve de V0, confrontés aux six exigences. Pas de panorama.

Livrable : **le banc d'essai chiffré** — ce qui tient l'étalon, ce qui s'adapte, ce qui se reconstruit, avec le coût en jours.

### V3 — Les prises et leurs substituts construits

Objet : publication sociale et avis, plateforme par plateforme, après le verdict juridique de V1.

Agents :
— **Publication sociale** — plateformes réellement atteignables, briques libres d'orchestration, et ce qu'il faut construire pour les manquantes
— **Avis** — recensement exhaustif des plateformes pertinentes en Guadeloupe ; pour chacune : avis lisibles, réponse possible, à quelle condition, par quelle voie licite

Livrable : **le tableau des prises** — une ligne par plateforme, voie d'accès, prix d'entrée, risque de coupure, substitut à construire.

### V4 — Rédaction, blog, façade

Objet : la pile qui transforme la collecte en publication, sous les six exigences.

Agents : rédaction assistée et sourcée … blog et site … application professionnelle … hébergement conforme.

Livrable : **la pile technique**, avec son écart à l'étalon pour chaque organe reconstruit.

### V5 — Assemblage et arbitrage

Objet : décider ce qui se construit d'abord, et le chiffrer.

Sorties : l'architecture retenue … la chaîne MCP à installer … le chiffrage à un an … le périmètre tenable en quatre-vingt-dix jours … **l'ordre de construction**, puisqu'on ne construit pas tout … ce qui part au dépôt et pourquoi.

Livrable : **l'architecture arbitrée**.

---

## 9. Ce que ce prompt refuse de produire

— Un panorama d'outils sans mesure
— Une décision de construire sans étalon mesuré sur le modèle repéré
— Une mesure sur un jeu d'épreuve non figé, ou non guadeloupéen
— Une évaluation d'outil sans confrontation aux six exigences
— Une architecture avant la carte des deux murs
— Un chiffrage avant le banc d'essai

Si la matière manque, l'agent le dit avant de produire. Un retour honnêtement vide vaut mieux qu'un retour plein de C.

---

## 10. Nœuds encore ouverts — décisions attendues de Laurent

| Nœud | Question | Pourquoi c'est bloquant |
|---|---|---|
| **Façades** | Façade professionnelle d'abord, grand public ensuite ? Ou les deux en parallèle ? | Les deux en parallèle double le périmètre |
| **Qui construit** | Toi seul avec moi ? Une équipe ? Un budget de développement ? | Détermine ce qui est tenable — reconstruire un organe se compte en semaines |
| **Budget temps** | Quel horizon pour la première version utilisable par un vrai client ? | Fixe l'ordre de construction de V5 |
| **Voie des avis** | Si le mandat client est la seule voie licite, acceptes-tu que le produit exige les identifiants du client ? | Change le produit : il devient un outil sous mandat, avec les obligations qui vont avec |
