# Prompt de lancement — Moteurs de collecte vérifiée et outils de publication (Guadeloupe)

État : **brouillon soumis à validation de Laurent Cieutat** — 2 octobre 2026
Rien n'est lancé tant que les quatre nœuds ne sont pas tranchés.

---

## 1. Les quatre nœuds à trancher avant lancement

### Nœud 1 — Ce que « 100 % libre de droit » veut dire

Trois lectures circulent, elles ne sont pas compatibles :

— **(a) logiciel libre auto-hébergeable** — code sous licence permissive ou copyleft, aucune redevance d'usage, on héberge soi-même
— **(b) contenus et médias sans droits à payer** — domaine public, CC0, polices et images libres
— **(c) gratuit** — ce qui n'est ni (a) ni (b) : un service peut être gratuit et totalement fermé

Position proposée : **(a) pour les moteurs et l'infrastructure, (b) pour les médias du site.** (c) est écarté comme critère, c'est un piège.

**Le point dur, à dire franchement.** Les volets 1 et 2 de la demande ne peuvent pas être libres de droit :

| Volet | Pourquoi le libre ne suffit pas | Statut |
|---|---|---|
| Publication automatique réseaux sociaux | Chaque plateforme impose son API propriétaire, sa validation d'app, ses quotas ; certaines un abonnement payant | ⏳ conditions exactes à confirmer en V1 |
| Avis Booking.com | Pas d'API publique d'avis ; l'accès passe par un accord partenaire | ⏳ à confirmer en V1 |

Conséquence d'architecture, pas de renoncement : **le cœur reste libre et auto-hébergé ; les plateformes fermées deviennent des prises isolées et interchangeables**, chacune avec son prix d'entrée documenté et son risque de coupure évalué. Une prise qui se ferme coûte une prise, pas le produit.

### Nœud 2 — Il n'existe pas de moteur qui livre de l'information vérifiée

Ce qui existe : des moteurs qui **gardent la trace de la source**. Le « vérifié » est un processus, pas un logiciel. La demande mélange quatre organes qu'aucun outil unique ne couvre :

| Organe | Ce qu'il fait | Ce qu'il ne fait pas |
|---|---|---|
| Découverte | Trouver les sources — recherche, crawl, flux | Juger de leur valeur |
| Extraction | Tirer le texte propre d'une page | Dire s'il est vrai |
| Index et stockage | Rendre interrogeable, en texte et en sémantique | Datater ni tracer |
| Chaîne de provenance | Qui a dit quoi, où, quand, et sous quelle forme on l'a capté | Rien d'automatique n'existe |

Position proposée : on cherche **quatre briques distinctes**. La chaîne de provenance est notre couche propre — c'est elle qui fera la valeur du produit, personne ne la vend telle quelle.

### Nœud 3 — Pro et grand public sont deux produits

Position proposée : **un moteur, deux façades, une seule construite au lancement — la professionnelle.** C'est elle qui paie. Le grand public se greffe après sur le même socle.

### Nœud 4 — Guadeloupe, marché ou périmètre de données

Position proposée : **les deux, à des titres distincts.**

— Marché — qui achète : hôtellerie, restauration, location, artisanat, professions libérales, collectivités
— Périmètre — ce qu'on indexe : sources locales, créole, saisonnalité touristique, acteurs institutionnels
— Contrainte : la Guadeloupe est dans l'Union européenne, donc RGPD plein — cela encadre la collecte d'avis nominatifs et impose un hébergement conforme

---

## 2. Doctrine de travail imposée à tous les agents

### Le barème de preuve — trois crans

| Cran | Définition | Sort |
|---|---|---|
| **A** | L'agent a installé ou appelé l'outil, et colle la sortie réelle | Entre au livrable |
| **B** | Document primaire cité avec URL et date de consultation — fichier LICENSE du dépôt, documentation officielle de l'API, dépôt source | Entre au livrable, marqué B |
| **C** | Billet de blog, comparatif, page marketing, affirmation du vendeur | **Va au dépôt**, jamais au livrable |

Règle de rejet : tout retour sans ligne A ni B est relancé une fois. S'il revient en C, il tombe. Aucune exception, aucun arbitrage au cas par cas.

Interdictions explicites :
— Ne jamais écrire « populaire », « largement utilisé », « référence du marché » — ce ne sont pas des faits
— Ne jamais donner un compte d'outils pour montrer qu'on a cherché — trois briques tenues valent mieux que quinze listées
— Ne jamais présenter comme gratuit ce qui est gratuit en version d'essai
— Tout fait porte sa date ou la marque « ⏳ à confirmer »

### Le gabarit de fiche-outil — une ligne par brique, sans colonne vide

| Champ | Exigence |
|---|---|
| Nom et nature | Ce que c'est, en une phrase, pas la phrase du site officiel |
| Licence SPDX exacte | Lue dans le fichier LICENSE du dépôt, pas devinée |
| Vivant ou mort | Date du dernier commit, nombre de mainteneurs actifs |
| Ce qu'il fait vraiment | Pas la promesse — ce que l'agent a constaté |
| Ce qu'il ne fait pas | Obligatoire, c'est là qu'est l'information |
| Auto-hébergeable | Oui, non, ou à quelles conditions |
| Coût réel à l'échelle visée | Serveur, quotas, licence, maintenance humaine |
| Testé | Comment, avec quoi, quelle sortie |
| Cran de preuve | A, B ou C |
| Source | URL et date de consultation |

### Les cinq colonnes de fin de réponse — obligatoires sur chaque retour

1. **MCP à installer** — nom, ce qu'il débloque, prérequis
2. **Logiciels manquants** — ce qu'il faut installer sur la machine pour avancer
3. **Outils déjà disponibles** — ce qui est là et non exploité
4. **IA existantes** — ce qui fait déjà le travail aujourd'hui, et à quel prix
5. **Futurs possibles à douze mois** — ce qui arrive, marqué ⏳ puisque non advenu

### Relance 1 — anti-oubli, automatique à chaque fin de recherche

> Tu viens de rendre. Avant que je lise, réponds à trois questions, en nommant des objets, pas des intentions.
> Qu'as-tu oublié — cite trois candidats que tu as écartés et dis pourquoi.
> Que n'as-tu pas vu — nomme ce que tu n'as pas pu vérifier et ce qui t'a manqué pour le faire.
> Qu'est-ce qui rendrait ce produit plus profitable — nomme l'endroit exact où il perd de l'argent aujourd'hui, et le geste qui le corrige.
> Si tu n'as rien, écris « rien » et assume-le.

### Relance 2 — preuve de test, automatique sur le même schéma

> Pour chaque ligne de ton retour : as-tu testé ? Avec quoi exactement — version, commande, environnement, date.
> Qu'as-tu obtenu — colle la sortie, pas ton résumé.
> Qu'as-tu validé par toi-même et qu'as-tu recopié d'ailleurs.
> Reclasse chaque ligne en A, B ou C. Toute ligne classée A sans sortie collée redescend en C.

---

## 3. Les cinq vagues

Chaque vague s'arrête sur son livrable et attend validation. Pas d'enchaînement automatique : une vague mal cadrée contamine les quatre suivantes.

### V1 — Le sol

Objet : établir ce que « libre de droit » autorise réellement, et où sont les murs.

Agents :
— **Licences** — cartographier les familles de licences et ce qu'elles permettent pour un produit commercial ; nommer les pièges connus du copyleft en service hébergé
— **Murs des plateformes** — pour chaque réseau social et chaque plateforme d'avis visés : condition d'accès à l'API, coût, quota, délai de validation, risque documenté de fermeture
— **Conformité** — RGPD appliqué à la collecte d'avis nominatifs et à l'indexation de contenus tiers en Guadeloupe ; hébergement conforme

Livrable : **la carte des murs** — ce qui est faisable libre, ce qui exige une prise propriétaire, ce qui est interdit.

### V2 — Les quatre organes de collecte

Objet : trouver les briques, les tester, les classer. Un organe à la fois, pas de moteur miracle.

Agents, un par organe : découverte … extraction … index et stockage … chaîne de provenance.

Consigne commune : chaque agent rend au maximum trois candidats tenus, testés, avec sortie collée. Pas de panorama.

Livrable : **le banc d'essai des moteurs** — ce qui tourne, ce que ça coûte, ce qui manque.

### V3 — Les prises

Objet : plateforme par plateforme, la prise de publication et la prise d'avis.

Agents :
— **Publication sociale** — recenser les plateformes réellement atteignables par API, et les briques libres d'orchestration de publication
— **Avis** — recenser exhaustivement les plateformes d'avis pertinentes pour la Guadeloupe, et dire pour chacune si les avis sont lisibles, si on peut y répondre par API, et à quelle condition

Livrable : **le tableau des prises** — une ligne par plateforme, avec le prix d'entrée et le risque.

### V4 — Rédaction, blog, façade

Objet : la pile qui transforme la collecte en publication.

Agents : rédaction assistée … blog et site … application professionnelle … hébergement souverain.

Livrable : **la pile technique**.

### V5 — Assemblage

Objet : arbitrer, chiffrer, décider ce qui se construit d'abord.

Sorties : l'architecture retenue … la chaîne MCP à installer … le chiffrage à un an … le périmètre tenable en quatre-vingt-dix jours … ce qui part au dépôt et pourquoi.

Livrable : **l'architecture arbitrée**.

---

## 4. Ce que ce prompt refuse de produire

— Un panorama d'outils sans test
— Une liste de plateformes sans leur condition d'accès réelle
— Une architecture avant la carte des murs
— Un chiffrage avant le banc d'essai

Si la matière manque, l'agent le dit avant de produire. Un retour honnêtement vide vaut mieux qu'un retour plein de C.
