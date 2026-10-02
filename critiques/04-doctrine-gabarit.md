# Réparation, dernier tour — les deux gabarits, le corpus relu, la règle d'arrêt

Suite de `04-doctrine.md` et `04-doctrine-reparation.md`. Aucun fichier existant modifié, aucun commit.

Même convention : les blocs cités sont écrits **dans la voix du document**, prêts à coller. Les encadrés *Note* sont ma voix.

| Pièce | Où elle va | Ce qu'elle remplace |
|---|---|---|
| 6 — Les deux gabarits | section 4.4 | le gabarit unique de fiche-organe |
| 7 — Le corpus relu sous mandat | révise la section 5bis de la pièce 5b | ma propre pièce, corrigée en deux endroits |
| 8 — La règle d'arrêt de V-1 | dans V-1, pièce 3 | ma propre règle d'arrêt, dont la portée change |

---

## Pièce 6 — Les deux gabarits

> *Remplace la section 4.4 en entier.*

### 4.4 Pourquoi deux gabarits et non un

Un gabarit unique organisé par organe fait répondre huit fois à des questions qui n'ont qu'une réponse. Le fuseau horaire n'est pas une propriété de l'organe Extraction. Le coût d'hébergement à l'échelle visée n'est pas une propriété de l'organe Index : c'est une propriété de la pile, et la somme de huit parts arbitraires ne sera pas le coût du produit. Le guichet ne se qualifie ni par organe ni par plateforme mais **source par source**, ce qui est l'acquis de la v4.

Huit réponses réécrites divergeront, parce que des réponses réécrites divergent toujours. Et la divergence ne sera vue par personne, puisque chaque fiche est relue seule et paraît cohérente. C'est le faux vert à l'échelle du classeur : chaque pièce est verte, l'ensemble ne tient pas.

D'où la règle de maille :

> **Ce qui a une seule réponse pour tout le produit s'écrit une fois, dans la fiche de produit. Ce qui varie d'un organe à l'autre s'écrit dans la fiche d'organe. Une fiche d'organe ne recopie jamais la fiche de produit : elle la cite par sa version. Un renvoi ne divergera pas.**

### 4.4.1 La fiche de produit — remplie une fois, versionnée

| Champ | Exigence |
|---|---|
| **Version de la fiche** | Un numéro qui s'incrémente. C'est ce numéro que citent les fiches d'organe |
| **Date d'établissement** | La date du jour où les champs ont été renseignés |
| **Date de péremption** | Une date, pas une durée. Au-delà, voir 4.4.4 |
| **Périmètre produit** | Les outils tenus, nommés. Ce qui n'y est pas n'est pas à construire |
| **Capacité** | Personnes, et jours par semaine. Issue de V-2. Sans elle, aucun coût en jours ne devient une date |
| **Guichets retenus par volet** | Le volet et son guichet, **par renvoi au registre des sources qualifiées** — jamais une requalification faite ici. La fiche de produit enregistre le choix ; le registre porte la preuve, source par source |
| **Les six exigences guadeloupéennes** | Une ligne par exigence : l'énoncé, l'état — tenue, non tenue, à vérifier —, et **le seuil chiffré quand l'exigence en demande un** (prix plafond local, langues couvertes). Un seuil absent porte ⏳ **et une échéance datée**. Une exigence sans seuil ne disqualifie rien et ne doit pas prétendre le contraire |
| **Coût de pile à l'échelle visée** | Hébergement, quotas, licences de contenu, maintenance humaine — par an, avec la date du chiffrage et le couple provenance·robustesse de chaque ligne |
| **Corpus de jugement de référence** | Version courante, taille, date du gel, **taux de trous**. C'est l'unique référence que citent toutes les fiches d'organe |
| **Conformité** | Base légale du service ; base légale du corpus — distincte, voir 5bis ; responsable nommé ; procédure d'effacement ; date du dernier contrôle |
| **Décisions E ouvertes** | Par renvoi au registre des décisions, avec leur date de réexamen. Rappel du plafond de trois |
| **Carte de dépendance** | Pour chaque champ ci-dessus, la liste des fiches d'organe qui s'y appuient. Se remplit au fil de l'eau, en une ligne par fiche. C'est ce qui permet à une révision de ne réveiller que les fiches concernées |

*Note. Le dernier champ paraît bureaucratique et c'est le plus utile. Sans lui, toute révision de la fiche de produit invalide les huit fiches d'organe, donc personne ne révise, donc la fiche de produit se périme en silence — ce qui est exactement le défaut qu'on répare.*

### 4.4.2 La fiche d'organe — remplie une fois par organe, huit fois en tout

| Champ | Exigence |
|---|---|
| **Organe visé** | Lequel des **huit** de la section 6 |
| **Fiche de produit citée** | Son numéro de version. Rien de son contenu n'est recopié ici |
| **Modèle repéré** | Nom, version, éditeur, licence ou statut propriétaire. Un produit, jamais une catégorie |
| **Guichet du modèle** | Par renvoi au registre, avec le degré s'il s'agit du 5 — ou « inconnu ». Jamais une requalification faite ici |
| **Étalon** | La métrique, le seuil, et **la version du corpus de jugement** sur laquelle le seuil est fixé |
| **Étalon de repli** | Le coût manuel du même travail, en minutes par unité, quand le modèle est hors de portée. Mesuré chez nous, en `A·1` |
| **Mesure du modèle** | Les chiffres, leur couple `provenance·robustesse`, la date, la version du corpus et son taux de trous |
| **Équivalent libre trouvé** | Nom, licence SPDX lue dans le fichier LICENSE, date du dernier commit, nombre de mainteneurs, couple de chaque ligne |
| **Écart à l'étalon** | Chiffré, sur la version de corpus nommée, avec son couple |
| **Le manquant exact** | Et son coût en jours, converti en date par la capacité de la fiche de produit |
| **Verdict** | Adopter tel quel … adapter … reconstruire … renoncer |
| **Verdict fondé sur** | **La liste des lignes de cette fiche sur lesquelles le verdict s'appuie, avec leur couple.** Le verdict lui-même ne porte pas de couple : un jugement n'a pas de provenance |
| **Remontées** | Toute contradiction constatée avec la fiche de produit. Voir 4.4.3. Vide est une réponse, « non vérifié » en est une autre, le silence n'en est pas une |
| **Décision E attachée** | S'il y en a une, son renvoi au registre et sa date de réexamen |
| **Date de péremption de la fiche** | Une date. Voir 4.4.4 |

*Note. Le champ « Verdict fondé sur » remplace l'ancien champ « Cran de preuve » de la fiche unique, et il le remplace parce que l'ancien était une faute : un cran de preuve apposé à un verdict fait passer un jugement pour un fait mesuré, et c'est la forme la plus discrète du faux vert puisqu'elle est inscrite dans le formulaire. Avec le nouveau champ, un relecteur vérifie mécaniquement une chose : les lignes citées à l'appui du verdict sont-elles porteuses — robustesse 1 ou 2 ? Si elles ne le sont pas, le verdict tombe ou devient une décision E proposée. On ne discute plus du verdict, on vérifie ses appuis.*

### 4.4.3 Quand une fiche d'organe contredit la fiche de produit

C'est là que le défaut de maille se révélera, donc c'est le seul endroit où le dispositif doit être précis.

> **La fiche de produit fait foi. Une fiche d'organe ne la corrige jamais sur place.** Elle inscrit une **remontée** : le champ en cause, la version de la fiche de produit citée, ce que cette fiche affirme, ce que l'organe a constaté, et le couple du constat.

Puis la remontée se tranche au niveau de la fiche de produit, jamais au niveau de l'organe. Trois issues, et une seule s'applique.

**Issue 1 — le constat est porteur et la fiche de produit a tort.** La fiche de produit est révisée, sa version s'incrémente, et **seules les fiches d'organe que la carte de dépendance rattache au champ modifié** sont marquées *à revalider*. Marquées, pas invalidées : elles restent lisibles, elles ne portent plus de décision jusqu'à revalidation.

**Issue 2 — le constat n'est pas porteur.** Robustesse 3 ou 4 : la remontée est inscrite comme piste, avec une échéance datée. La fiche de produit ne bouge pas, aucune fiche n'est réveillée. Une observation étroite ne doit pas faire tourner tout le classeur — c'est le prix à payer pour que l'issue 1 reste crédible.

**Issue 3 — les deux sont porteurs et se contredisent vraiment.** Ce n'est alors pas un problème de documentation : **c'est le signe que le champ n'est pas une propriété du produit.** Il varie par organe, par source ou par plateforme. On le **descend** dans la fiche d'organe, ou on le **sort** au registre des sources, avec une ligne disant pourquoi. La fiche de produit perd un champ et gagne en justesse.

> **Le compteur de remontées.** Chaque champ de la fiche de produit porte le nombre de remontées qu'il a reçues. **Un champ qui en reçoit trois est mal maillé, quelles qu'aient été les issues individuelles**, et se descend ou se sort sans autre discussion. C'est la seule mesure qui rende visible un défaut de maille — celui qui, sans elle, reste invisible parce que chaque fiche est relue seule.

> **Une contradiction non remontée est une faute plus grave qu'une mesure fausse.** Une mesure fausse est attrapée à la relecture. Une contradiction tue n'est attrapée par personne.

Et un contrôle de plus pour le relecteur de la relance 2, mécanique et gratuit : **la fiche cite-t-elle une version de la fiche de produit, et cette version est-elle la courante ?** Une fiche qui cite une version périmée se détecte en une seconde et signale une dérive avant qu'elle ne coûte.

### 4.4.4 La péremption

> **Une fiche périmée ne devient pas fausse. Elle cesse de porter.**

C'est une chute sur l'axe de la robustesse, jamais sur celui de la provenance : un fait mesuré reste un fait mesuré, mais un fait de l'an dernier sur un marché dont les conditions d'accès changent tous les six mois n'étaye plus un engagement. Concrètement, à la date de péremption :

— les lignes de la fiche passent en robustesse **3** d'office, sans relecture, et cessent donc d'être porteuses ;
— une **fiche de produit périmée gèle les fiches d'organe qui la citent** : elles restent lisibles, elles ne portent plus de décision ;
— le verdict d'une fiche d'organe périmée ne peut plus être invoqué dans un arbitrage, et V5 ne peut pas le consommer.

**Comment se fixe la date.** Au plus court des trois : la péremption des conditions d'accès du guichet concerné ; la date de retraite de la version du corpus de jugement citée ; un an. Elle se fixe **au moment de remplir la fiche**, pas au moment où l'on s'aperçoit qu'elle est vieille.

*Note. C'est la pièce qui répare l'horloge que le document avait identifiée sans la brancher : il énonce que les conditions d'accès changent tous les six mois, et ne met aucune date d'expiration sur la carte des guichets que trois vagues plus tard viennent consommer.*

---

## Pièce 7 — Le corpus relu à la lumière du mandat

> *Révise la section 5bis. Je dis d'abord ce qui change dans ma propre pièce, ensuite ce qui ne change pas, et je nomme la seule question qui reste au juriste.*

Les deux faits apportés — la délégation se fait par **jeton d'autorisation révocable et programmable**, non par mot de passe, sous mandat formel du titulaire ; et la réglementation sur les avis oblige à capter la **date de l'expérience de consommation dès l'origine**, faute de quoi elle est définitivement perdue — ne vont pas dans le même sens. Le premier allège, le second alourdit, et aucun des deux n'allège la pièce là où je la croyais faible.

### 7.1 Ce qui s'allège vraiment, et ce n'est pas le corpus

**Le service s'allège, et beaucoup.** Si l'accès est un jeton délégué sous mandat formel, alors pour les avis des établissements de nos mandants, **le titulaire est responsable du traitement et nous sommes sous-traitant**. La question que je posais en premier — « quelle est notre base légale pour collecter ces avis » — n'est plus la nôtre : nous agissons sur instructions documentées. Ce que V1 doit produire n'est plus la recherche d'un fondement, c'est la rédaction d'un contrat de sous-traitance. C'est un travail connu, borné, et bien moins incertain que ce que je supposais.

**L'organe de garde des accès confiés s'allège aussi, et je dois corriger un de mes propres constats.** J'avais écrit que la méthode en six temps ne sait pas traiter cet organe, parce qu'on ne repère pas « le meilleur chiffrement au repos du marché ». Avec un jeton, c'est partiellement faux, et je le retire : la révocation devient **mesurable**. On révoque, on rappelle l'interface, on observe le refus, on chronomètre — c'est un `A·1`, obtenu chez nous, sans aucun compte propriétaire. L'étalon « révocation effective en minutes » cesse d'être une intention et devient un chiffre. Mieux : une part de la révocation passe du côté de la plateforme, puisque le client peut révoquer dans son propre compte sans nous demander — et une garantie que le client peut exercer sans nous vaut mieux qu'une procédure que nous promettons.

Ce qui reste entier : un jeton est un secret porteur. Chiffrement au repos, rotation, journalisation, cloisonnement par client demeurent. Le rayon du dommage se réduit, il ne disparaît pas.

### 7.2 Ce qui ne s'allège pas — et devient plus net, donc un peu plus sévère

Voici le point, et c'est l'inverse d'un allègement.

> **Un sous-traitant ne traite que pour les finalités du responsable.** Répondre aux avis de l'établissement X, pour X, est la finalité de X. **Constituer un corpus de jugement figé, conservé chez nous, réutilisé dans le temps et à travers plusieurs clients, pour mesurer nos propres composants, est notre finalité à nous.** Pour ce traitement-là, nous ne sommes pas sous-traitant : nous sommes responsable.

Le mandat légitime donc le **service** et ne couvre pas le **corpus**. Ma conclusion ne s'allège pas : elle se localise. Et en se localisant elle devient un peu plus sévère, parce qu'avant je cherchais une base légale incertaine pour un ensemble flou, et que maintenant je sais exactement quelle pièce n'est pas couverte, et par quel raisonnement elle ne l'est pas.

Deux circonstances aggravent légèrement, et il faut les écrire plutôt que les laisser apparaître plus tard.

**Les auteurs des avis ne sont partie à rien.** Ils n'ont aucune relation avec nous, aucune attente que leur avis séjourne dans un banc d'essai versionné d'un prestataire guadeloupéen, et le titulaire qui nous autorise n'autorise pas en leur nom pour **notre** finalité.

**La date de l'expérience de consommation est une donnée de plus, obligatoire, et plus identifiante qu'elle n'en a l'air.** Elle localise une personne à une date et dans un lieu. Elle doit être captée à l'origine sous peine d'être perdue — c'est donc une captation qu'on ne peut pas repousser —, mais elle est exigée pour **le service**, pas pour nos mesures. Elle doit donc rester du côté du responsable, et ne jamais entrer dans ce que nous conservons.

### 7.3 La construction en deux couches tient, et se durcit

Elle tient, et les deux faits la poussent à sa forme franche, que je n'avais pas osée :

> **On ne constitue pas de corpus d'avis chez nous. On mesure chez le titulaire, et on n'emporte que le juge et les chiffres.**

| Ce qui reste dans le périmètre du responsable | Ce que nous emportons |
|---|---|
| Les avis verbatim, la date d'expérience, l'identité et le pseudonyme de l'auteur, le fil de réponse | La **couche de jugement** — champs attendus, pertinence attendue, réponse acceptable, écrits en références et en valeurs, jamais en verbatim — et les **chiffres** produits par la mesure, avec la version et le taux de trous |

La mesure tourne dans le périmètre où la donnée est licitement présente, au bénéfice du service dû à ce client, et ce qui en sort n'est plus un corpus de personnes : c'est une grille d'attentes et un nombre. Cela ne rend pas le problème nul — une annotation rattachée à un avis reste liée à une personne tant que l'avis existe — mais cela effondre l'essentiel de l'exposition, et cela supprime la contradiction que je décrivais comme insoluble : **il n'y a plus d'objet à la fois immuable et effaçable, parce que ce qui est gelé chez nous n'est plus ce qui porte des droits.**

Le mécanisme du **taux de trous** reste nécessaire, pour une raison déplacée : non plus parce que nous effaçons, mais parce que le corpus du titulaire bouge sous nous — un auteur supprime son avis, une plateforme le retire. L'attrition n'est plus la nôtre, elle est subie, et elle doit être déclarée de la même façon. Le seuil de retraite d'une version reste ⏳ : je n'ai toujours aucune base pour l'inventer.

### 7.4 Le plafond de robustesse se raffine au lieu de se lever

J'avais écrit que pour le volet avis la robustesse 1 n'était atteignable qu'en audit sous accord, et que le public plafonnait à 2. C'était trop grossier, et le fait du jeton ouvre une possibilité que je n'avais pas vue.

> **`1†` — rejouable par un tiers admis au périmètre.** Un auditeur sous accord, et surtout **le titulaire lui-même** : il détient la position de responsable et l'accès, donc il peut rejouer notre mesure sur ses propres données et vérifier notre chiffre.

C'est, commercialement, une opposabilité plus forte que la reproductibilité publique : celui qui peut vérifier est celui qui paie. Convention d'écriture : `A·1†` se lit « mesuré, rejouable dans le périmètre », et une ligne `1†` est **porteuse** au même titre qu'une `1`, à condition que la fiche nomme qui peut rejouer et comment.

Le volet veille, lui, tient sur le guichet 6, son corpus est publiable, et ses mesures atteignent `1` sans dague. C'est une raison de plus de commencer par là.

*Note sur le coût. J'ajoute un signe à un barème dont je disais que le coût d'adoption est ma deuxième inquiétude. Je l'assume parce que l'alternative — tout aplatir à 2 — sous-déclare une opposabilité réelle, et que le barème à deux axes existe précisément pour arrêter de confondre. Mais c'est la seule exception, elle ne vaut que pour une donnée qui ne peut pas sortir de son périmètre, et elle ne doit pas en engendrer d'autres.*

### 7.5 La seule question qui reste au juriste

Elle tient en une phrase, et c'est le gain net de cette relecture : avant, je ne savais pas laquelle poser en premier.

> **Le corpus de jugement constitué à partir des avis de nos clients mandants, conservé par nous, versionné et réutilisé pour mesurer nos propres composants à travers plusieurs clients : sommes-nous sous-traitant du titulaire pour ce traitement, ou responsable d'un traitement distinct ? Et si distinct, sur quelle base, les auteurs des avis n'ayant aucune relation avec nous ?**

Si la réponse est « sous-traitant », la pièce 5b s'allège d'un coup et la mesure chez le titulaire devient un confort et non une nécessité. Si la réponse est « responsable distinct », la forme de 7.3 n'est pas une précaution : c'est la seule forme praticable. **Je ne peux pas trancher cette question, et je ne vais pas faire semblant** : mon raisonnement sur la finalité est solide en logique et il reste du `D` en droit. C'est la première question de V1, avant la cessibilité du mandat.

### 7.6 Deux corrections à mes propres pièces

**À la pièce 3, vague V-1.** J'écrivais « le versement au corpus … sous le régime de la section 5bis », sans dire que le schéma devait préexister. La date d'expérience de consommation ne se rattrape pas : **le schéma de captation doit être écrit avant le premier jour du service manuel**, sinon le premier mois de matière est définitivement incomplet. V-1 gagne donc un geste, placé en tête : *écrire le schéma de captation — champs obligatoires, dont la date d'expérience — et le geler avant la première lecture d'avis.*

**À la section 6, étalons par organe.** L'organe Avis gagne une métrique, et elle est de la meilleure espèce — binaire, mesurable, et dont l'échec est irréversible : **taux de captation de la date d'expérience à l'origine**. Cible 100 %. Tout ce qui est manqué est perdu pour toujours, ce qui en fait le seul étalon du document qu'on ne peut pas rattraper par un effort ultérieur.

---

## Pièce 8 — La règle d'arrêt de V-1, réécrite au périmètre décidé

> *Remplace la règle d'arrêt de la vague V-1. Le périmètre est tranché : les quatre outils sont tenus en entier — veille, publication automatique sur réseaux sociaux, gestion des avis, blog.*

### Ce que le mandat commande réellement — et ce n'est pas un quart

Il faut corriger la portée avant d'écrire la règle. La délégation par jeton n'est pas le moyen d'accès du volet avis seulement : **publier sur les comptes sociaux d'un client exige la même délégation par le même mécanisme.** Le mandat commande donc les deux **prises** du produit, non une.

| Outil | Dépend du mandat ? | Ce qui l'alimente |
|---|---|---|
| **Veille** | Non | Guichet 6 — données ouvertes, flux publiés, communs documentaires |
| **Blog** | Non | Notre propre bien, ou le site du client |
| **Gestion des avis** | **Oui** | Jeton délégué sous mandat du titulaire |
| **Publication sur réseaux sociaux** | **Oui** | Jeton délégué sur les comptes du client |

Sans mandat, ce n'est pas un quart du produit qui tombe : **c'est la moitié, et c'est la moitié qui agit.** Il reste les deux outils qui informent, il ne reste aucun outil qui opère.

### Les deux portes, qui ne s'ouvrent pas du même côté

Un mandat signé ne suffit pas, et le confondre avec l'accès ferait perdre un mois.

— **Porte client** : le titulaire signe le mandat et délègue le jeton. C'est notre côté, c'est commercial, et c'est la proximité guadeloupéenne qui l'ouvre.
— **Porte plateforme** : les conditions de la plateforme admettent qu'un prestataire mandaté agisse par délégation. C'est leur côté, c'est contractuel, et aucune relation locale ne l'ouvre.

Les deux sont nécessaires, **par plateforme**. Un mandat signé sur une plateforme qui interdit l'accès délégué aux prestataires ne vaut rien pour cette plateforme — et il vaut toujours pour les autres. C'est pourquoi la preuve du guichet de V-1 se fait plateforme par plateforme, et pourquoi un échec partiel n'est pas un échec.

### La règle d'arrêt

> **V-1 est franchie quand un mandat est signé, un jeton délégué obtenu, et une action réussie sur au moins une plateforme — une réponse publiée, ou un message posté — avec sa trace collée.** Un contrat signé sans action réussie n'est pas un franchissement : c'est une promesse.
>
> **Tant que V-1 n'est pas franchie :** on construit les deux outils qui n'en dépendent pas — veille sur le guichet 6, blog — et on rend les deux autres **à la main**, sous mandat, facturés. Le service manuel n'est pas une attente : c'est la voie d'acquisition, le relevé de l'étalon manuel, et la seule source licite de matière. On ne chiffre pas les prises, on ne fige pas d'étalon d'avis, on n'engage pas de développement sur les deux organes de prise.
>
> **Ce qu'on ne fait pas :** dérouler V0 à V5 sur les deux prises en espérant que le client arrive au bout. Il est au début, ou il n'y a pas de prises.
>
> **La date.** V-2 fixe, en même temps que le critère d'abandon, **la date** à laquelle on cesse d'attendre. Une date, pas une condition : « quand on aura un client » n'est pas une échéance. Passée cette date sans mandat franchi, on bascule au périmètre réduit — veille et blog — et la bascule est une décision E, avec ses cinq champs, dont le coût du retour en arrière.
>
> **Le franchissement minimal admis.** À défaut de mandat payant, un **mandat d'essai** suffit à franchir V-1 : un établissement, une plateforme, un mois, gratuit ou quasi. Il ne prouve pas le marché, et ce n'est pas ce qu'on lui demande : il prouve que la délégation fonctionne, que la plateforme admet le prestataire mandaté, et il capte la date d'expérience dès l'origine — ce qui ne se rattrape pas. Un mandat d'essai franchit la porte technique ; il ne solde pas le nœud commercial, et il faut écrire lequel des deux on a franchi.

### Ce qui est perdu si le mandat ne vient jamais

Il faut l'écrire en entier, parce que c'est une perte de position et pas seulement de périmètre.

— **Les deux prises sont perdues**, donc le produit cesse d'être un outil qui agit pour devenir un produit qui informe. La veille et le blog se vendent, mais ils se vendent moins cher et se remplacent plus facilement.
— **L'étalon de l'organe Avis devient inatteignable à jamais**, puisque le dénombrement des avis réellement présents ne s'obtient que par l'extranet du titulaire, et que le degré 5c est écarté. Non pas « non mesuré » : non mesurable.
— **L'avantage stratégique perd son objet.** Le document soutient que la proximité est la clé du guichet 2 et qu'aucun concurrent mondial ne peut l'ouvrir. Sans mandat, cette clé n'ouvre rien : il reste un vendeur local de veille et de blog, sur un marché où les outils génériques fonctionnent, et l'argument « la Guadeloupe est le cœur » se réduit aux langues et aux sources locales. Ce sont deux vrais avantages. Ce ne sont plus des avantages imprenables.

> **Donc la conclusion de portée, qui n'est pas celle du périmètre décidé mais celle de l'ordre :** les quatre outils sont tenus, et deux d'entre eux dépendent d'une signature. **Celle-là se cherche avant de construire, pas après.** Un seul mandat franchi suffit à débloquer les deux prises ; zéro mandat ne laisse que la moitié du produit, et la moitié la moins défendable.

---

## Ce que je retire ou corrige de mes propres constats

Tenu au clair, parce qu'une critique qui ne révise rien d'elle-même ne vaut pas plus que ce qu'elle attaque.

| Constat antérieur | Sort |
|---|---|
| « La méthode en six temps ne sait pas traiter l'organe de garde des accès » (C5) | **Affaibli, à moitié retiré.** Avec un jeton révocable, la révocation est mesurable en `A·1`. Ce qui reste vrai : les temps 1 et 2 n'ont toujours pas de « modèle repéré » à instrumenter pour le chiffrement au repos et le cloisonnement, qui se tiennent par procédure et par audit, non par mesure contre un concurrent |
| « Il n'existe pas de corpus d'avis à la fois figé et conforme » (pièce 5b) | **Tient, mais se déplace.** La contradiction immuable/effaçable disparaît si le corpus verbatim ne vient jamais chez nous. Ce qui reste : le corpus est notre finalité et non celle du mandant, donc le mandat ne le couvre pas — et cela, je ne peux pas le trancher sans juriste |
| « Pour le volet avis, le public plafonne à robustesse 2 » | **Trop grossier, raffiné en `1†`.** Rejouable par le titulaire lui-même, ce qui est commercialement plus fort que rejouable publiquement |
| « V-1 verse les avis au corpus » (pièce 3) | **Incomplet.** Le schéma de captation doit être gelé **avant** le premier jour, la date d'expérience ne se rattrapant jamais |
| « Le gabarit de fiche-organe est sain » (premier rapport) | **Retiré, et remplacé par la pièce 6.** Il était sain dans ses champs et faux dans sa maille |
| « Sans mandat, le volet avis est reporté » (pièce 3) | **Portée corrigée.** Sans mandat, ce sont les deux prises — avis et publication sociale — donc la moitié du produit décidé, et la moitié qui agit |

---

*Écrit le 2 octobre 2026. `00-PROMPT-DE-LANCEMENT.md`, `04-doctrine.md` et `04-doctrine-reparation.md` non modifiés. Aucun commit.*
