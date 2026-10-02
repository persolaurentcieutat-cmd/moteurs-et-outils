---
name: conduite-par-vagues
description: Conduire un sujet neuf de bout en bout pour Laurent Cieutat, sans attendre ses relances — cadrer avant de répondre, instruire par vagues qui s'arrêtent sur validation, faire démolir chaque proposition par des lecteurs adversariaux à contexte vierge, relancer chacun sur ses trous déclarés jusqu'à épuisement, et clore sur ce qui attend une décision. Se déclenche sur la formule réservée « Conduite du sujet [X] » tapée par Laurent, où le sujet est toujours obligatoire ; et sans formule, sur une demande d'étude de faisabilité, un sujet neuf à instruire, ou la demande de reproduire la démarche d'un projet antérieur. Les tournures conversationnelles ne déclenchent jamais seules. Interdit de valider sa propre production, interdit de livrer sans avoir fait casser, interdit de laisser dormir une promesse non tenue.
---

# Conduite par vagues

## Le déclencheur

**« Conduite du sujet [X] »**, où le sujet est toujours obligatoire. Sans sujet nommé, ne pas déclencher.

Elle se déclenche aussi, sans formule, sur une demande d'étude de faisabilité ou de cadrage d'un sujet neuf. Mais les tournures conversationnelles — « regarde ça », « qu'est-ce que tu en penses » — ne déclenchent jamais seules : elles appellent une réponse, pas une conduite de six temps.

## Le principe

Une proposition non attaquée est une opinion. Cette compétence remplace les relances de Laurent par un mécanisme qui les déclenche tout seul — **sauf celles qui demandent une décision, qu'elle lui pose au lieu de les trancher.**

Elle existe parce que trois gestes ont rapporté davantage que tout le reste : cadrer avant de répondre, faire casser par un lecteur qui n'a pas produit, et relancer chaque lecteur sur les trous qu'il avoue lui-même.

## Les outils que cette compétence appelle au lieu de les refaire

Elle ne réécrit rien de ce que le système de Laurent tient déjà. Règle du loyer appliquée à elle-même.

| Besoin | Outil existant | Ce que cette compétence ajoute |
|---|---|---|
| Cadrer la demande avant d'y répondre | **`cadreur`**, marqueur « >>+ » | Rien. **L'appeler.** Elle fait déjà le dépliage, la reformulation et l'arrêt sur validation |
| Juger un artefact produit ailleurs | **`double-lecture`**, formule « DDCC », session neuve obligatoire | Rien, et surtout ne pas la contourner : la démolition par lecteurs internes **ne la remplace pas**, parce que la session qui produit ne peut pas être celle qui juge |
| Ouvrir et clore un projet du Container | **`ouverture-projet`** et **`fermeture-projet`** | Rien. Le registre de démarche est le **fichier** du dépôt ; ces skills tiennent les **tableaux Notion**. Les deux, pas l'un ou l'autre |
| Recadrer la posture en cours de route | **`rappel-determinants`**, marqueur « ***// » | Rien |
| Choisir le livrable à produire | **`proposer-modes`** | Rien |

## Temps 1 — Cadrer, et s'arrêter

Avant toute recherche, tout agent, tout fichier. **Appeler `cadreur`.** Si la demande est déjà nette, cette skill reste muette, et c'est le bon comportement.

Trois exigences propres à une conduite par vagues, qui s'ajoutent au cadrage :

1. **Un pourcentage de compréhension** par élément de la demande, et sa moyenne. Sous 80 %, on ne lance aucune vague
2. **Dire ce qui est incompatible dans la demande.** Le geste le plus utile et le plus désagréable : une demande contient souvent deux souhaits qui s'excluent, et le dire tôt économise une vague entière
3. **S'arrêter.** Un cadrage validé vaut dix heures de travail juste ; un cadrage supposé les perd

## Temps 2 — Instruire par vagues

Chaque vague s'arrête sur son livrable et attend validation. Une vague mal cadrée contamine les suivantes.

**La vague zéro n'est jamais la recherche.** Elle est : solder les nœuds restés ouverts, et obtenir **la première matière réelle** — un client, un document, un accès. Sans matière réelle, tout se mesure dans le vide.

**Fixer une date, jamais une condition.** Une condition se laisse attendre indéfiniment ; une date tranche. Passée la date, on bascule au périmètre réduit et on l'inscrit comme décision assumée.

## Temps 3 — Faire démolir

**Le geste central, et il se déclenche sans qu'on le demande.**

Lancer des lecteurs adversariaux à contexte vierge, un par angle, chacun chargé de **casser**. Formule à leur donner telle quelle : *un retour qui approuve l'essentiel est un échec de ta mission*.

Les angles qui ont payé, à adapter au sujet :

| Angle | Ce qu'il attaque |
|---|---|
| **Droit et accès** | Les voies d'accès supposées, les licences, ce qui est interdit et qu'on croyait permis |
| **Marché et concurrence** | L'existence du marché, son prix plafond, et surtout **les concurrents locaux**, toujours l'angle mort |
| **Méthode et faisabilité** | Le coût réel, en mesurant et non en estimant |
| **Cohérence interne** | Les contradictions du document lui-même, citées des deux côtés, et ses dépendances circulaires |
| **Technique et existant** | Ce qui existe déjà et qu'on allait reconstruire |

Règles de lancement, toutes apprises à leurs dépens :

— Chaque lecteur écrit dans son propre fichier, sous `critiques/`, et **ne commite jamais** — c'est le conducteur qui commite
— Aucun lecteur ne touche au document attaqué
— Leur imposer le couple de preuve, et leur demander de **déclarer en tête ce qui ne vient que de leur mémoire**
— Leur interdire les quotas : *cite ce que tu as réellement écarté, zéro compris*
— Ne jamais leur demander « où ce produit perd-il de l'argent » si le produit n'existe pas : la présupposition est fausse et elle fabrique de l'invention. Demander à la place : **quelle conclusion, si elle est fausse, coûte le plus cher, et comment la tester pour moins de cent euros**

## Temps 4 — Relancer, et c'est là que tout se gagne

**Un premier retour n'est jamais le retour.** Chaque lecteur avoue des trous — c'est le signe qu'il travaille bien. Le relancer dessus, et recommencer jusqu'à ce qu'il n'avoue plus de trou ou qu'il bute sur un mur qu'il nomme.

Ce qui sort d'une relance, constaté : un agent corrige son propre verdict de marché d'un facteur dix-huit ; un autre trouve un bogue silencieux dans son propre code ; un troisième refuse de convertir un effort en jours et explique pourquoi c'est le mauvais chiffre.

Deux gestes qui doublent le rendement d'une relance :

— **Croiser les lecteurs.** Transmettre à l'un ce qu'un autre a établi, et lui demander si sa conclusion tient à cette lumière. Deux lecteurs indépendants qui convergent sur un point font le fait le plus solide qu'on puisse obtenir sans mesure
— **Accepter ce qui tombe, sans le défendre.** Le dire dans la relance : *ton retour est accepté, y compris les erreurs que tu me mets sur le dos et que j'assume*. Un lecteur qui sent une défense argumente au lieu de chercher

## Temps 5 — Le registre des promesses

**Ce registre existe parce que Laurent a dû demander « où en est la compétence ».** C'est le seul rappel de sa part qui était une faute pure de conduite.

Toute annonce faite dans une réponse — *je vais écrire*, *je propose de*, *je le ferai dès que* — entre dans une liste, à la fin du registre de démarche. Elle en sort quand l'objet existe sur disque. **Avant chaque clôture, relire cette liste.** Une promesse qui dort depuis deux réponses est signalée d'elle-même.

## Temps 6 — Clore

— Verser au registre de démarche, par la compétence `registre-de-demarche` : les renversements, les faits, les décisions, les désaccords, les murs, le lexique
— Si le sujet est un projet du Container, appeler **`fermeture-projet`** pour les tableaux Notion. Le fichier et les tableaux ne se remplacent pas
— Lister **ce qui attend une décision, trié par coût croissant.** Les actions gratuites en tête : ce sont celles qui dorment, et ce sont souvent les plus décisives
— Committer et pousser. Un conteneur est éphémère

## Temps 7 — Le juge extérieur

La démolition du temps 3 est faite par des lecteurs que cette session a lancés. Ils sont à contexte vierge, mais ils travaillent sous la consigne de celui qui a produit — donc ils ne sont pas indépendants au sens plein.

**Avant toute décision lourde, demander à Laurent de lancer un `DDCC` en session neuve** sur le livrable. C'est la seule lecture dont l'indépendance est entière, et sa condition de validité est qu'elle ne soit pas déclenchée par le producteur. Ne jamais l'invoquer soi-même : ce serait détruire ce qui fait sa valeur.

## Ce que cette compétence refuse

— **Valider sa propre production.** Le lecteur n'est jamais le producteur. Cette règle n'a pas d'exception, pas même pour gagner du temps
— **Livrer sans avoir fait casser**
— **Trancher à la place de Laurent.** Donner un avis net, oui. Décider, non. Quand une décision est requise, s'arrêter et la poser, en disant ce que chaque branche coûte
— **Produire une mesure en falsifiant un signal chez un tiers** : ni faux avis, ni faux compte, ni faux clic. Aucune exception, aucune décision ne la lève
— **Convertir un effort en jours sans l'avoir chronométré**
— **Laisser dormir une promesse non tenue**

## Deux leçons de terrain à ne pas réapprendre

**Le chemin critique n'est pas un effort, c'est un calendrier.** Les approbations d'une plateforme, un contrat à signer, une licence à lire ne se raccourcissent pas en travaillant plus. Les engager au plus tôt, pendant que le reste se construit.

**Quand le web est fermé, les forges de code restent une voie d'accès aux documents primaires.** Les dépôts publics contiennent les licences, les textes officiels republiés, les corpus. C'est de là que sont venues les meilleures preuves d'une session où presque tous les hôtes utiles étaient refusés.

## Ce qui restera toujours à Laurent

Trancher le périmètre. Décider une dépense. Arbitrer contre un avis donné. Et apporter la correction qu'aucun lecteur ne trouve, parce qu'elle vient de sa connaissance du terrain et non d'une source.

Cette compétence supprime les relances de rappel. Elle ne remplace pas les relances de jugement, et ne doit pas prétendre le faire.
