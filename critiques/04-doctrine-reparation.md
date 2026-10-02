# Réparation — cinq pièces prêtes à intégrer

Suite de `/home/user/moteurs-et-outils/critiques/04-doctrine.md`. Cible de la réparation : `00-PROMPT-DE-LANCEMENT.md` v4, non modifié ici. Aucun commit.

**Convention de lecture.** Le texte en bloc cité est écrit **dans la voix du document** et destiné à y être collé tel quel. Les encadrés *Note de réparation* sont ma voix, et ne font pas partie du texte à intégrer : ils disent ce que la pièce remplace, pourquoi, et ce qu'elle coûte. Les renvois `l. NNN` pointent la v4.

Placement des cinq pièces :

| Pièce | Où elle va | Ce qu'elle remplace |
|---|---|---|
| 1 — Barème à deux axes | section 4.1 et 4.2 | le barème à quatre crans et les trois règles de rejet |
| 2 — Cran E | nouvelle section 4.6 | rien — c'est un ajout, et il ne va **pas** dans le barème |
| 3 — Vagues V-2 et V-1 | en tête de section 8 | rien — V0 à V5 gardent leur nom et leur numéro |
| 4 — Relances refondées | section 7 entière | relances 1 et 2 |
| 5 — Désaccord, et corpus conforme | nouvelles sections 4.7 et 5bis | rien — deux trous comblés |

---

## Pièce 1 — Le barème à deux axes

> *Remplace les sections 4.1 et 4.2.*

### 4.1 Pourquoi deux axes, et pas quatre crans

Le barème à quatre crans mélangeait deux questions qui n'ont ni la même réponse ni le même usage.

**D'où vient ce fait ?** Je l'ai mesuré, je l'ai lu dans un document primaire, je l'ai pris dans un comparatif, je m'en souviens. C'est la **provenance**. Elle dit à qui en vouloir si le fait est faux.

**Combien peut-on poser dessus ?** Un tiers refait-il le chemin, l'échantillon est-il suffisant, le fait est-il daté, le corpus est-il nommé. C'est la **robustesse**. Elle dit si l'on peut engager du temps, de l'argent ou une signature.

Confondues sur une échelle unique, elles produisent des rangs faux : une mesure faite sur trois pages mal choisies dominait un texte de loi lu au Journal officiel. Et la règle de décision se branchait sur le mauvais axe — elle exigeait une **provenance** haute là où la question était une **robustesse** suffisante.

Le symptôme était visible dans le barème même : le cran A était dédoublé en A-mesure et A-usage. Ce n'étaient pas deux provenances. C'était **une provenance et deux robustesses** — dans les deux cas l'agent a fait tourner la chose ; dans un seul il peut nommer le corpus qui juge. Le dédoublement du A était le barème à un axe qui demandait un deuxième axe.

### 4.2 Axe 1 — la provenance, en lettres

| Lettre | Définition | Ce qu'elle exige, sans quoi elle tombe d'un cran |
|---|---|---|
| **A — mesuré** | L'agent a fait tourner la chose lui-même | La commande **et** la sortie collées. Version, environnement, date |
| **B — primaire** | Document primaire : fichier LICENSE du dépôt, documentation officielle de l'éditeur, texte de loi, décision de justice, conditions d'utilisation | L'URL et la date de consultation. Si la page peut bouger, une copie horodatée au dépôt |
| **C — secondaire** | Billet, comparatif, page marketing, résumé de moteur de recherche, parole de vendeur, dire d'un confrère | La source nommée, et ce qui en a été repris |
| **D — mémoire** | Ce que l'agent croit savoir, sans vérification dans la session | Rien à exiger. Il n'y a rien à vérifier : c'est le sens de la lettre |

Les lettres sont celles de l'ancien barème, et c'est voulu : la conversion des fiches existantes est mécanique. A-mesure et A-usage deviennent tous deux **A**, et se distinguent désormais sur le second axe.

**Pourquoi le D reste.** Pour la même raison qu'avant — c'est le cran qui a l'assurance du A et la fiabilité du C, et la connaissance d'un modèle porte une date de coupure. Mais la règle change : on ne demande plus à l'agent de **déclarer** ce qu'il croit savoir, parce qu'un agent ne sait pas de façon fiable d'où lui vient une phrase. On le constate de l'extérieur, mécaniquement : **toute affirmation sans URL consultée dans la session ni sortie de commande collée est D d'office**, quoi qu'en dise son auteur. Le critère cesse d'être une introspection et devient un contrôle.

### 4.3 Axe 2 — la robustesse, en chiffres

La question est une seule : **un tiers, avec ce qui est écrit, retrouve-t-il ce résultat ?**

| Chiffre | Définition | Exemple |
|---|---|---|
| **1 — rejouable** | Un tiers refait le chemin et obtient la même chose. Commande, version, environnement, date, corpus nommé et accessible — ou URL qui rend encore le même texte, copie horodatée au dépôt | Une mesure de rappel sur le corpus de jugement v1.2, script au dépôt |
| **2 — attesté** | Le fait est vérifiable mais le chemin ne se refait pas : compte d'essai expiré, démonstration vue une fois, page modifiée depuis. La trace est conservée, la source ne se rouvre pas | Les chiffres d'une démonstration, capturés et datés, chez un éditeur qui ne redonnera pas d'accès |
| **3 — étroit** | Vrai sur ce qui a été vu, et ce qui a été vu est trop petit, trop vieux ou trop particulier pour qu'on généralise. Échantillon non déclaré, un seul cas, corpus non guadeloupéen, fait non daté | Un taux d'extraction mesuré sur quatre pages, ou mesuré sur un corpus métropolitain |
| **4 — non étayé** | Rien ne permet au lecteur de refaire le chemin. Pas de n, pas de date, pas de corpus, pas de sortie | « L'outil tient la charge » |

**Trois chutes mécaniques, vérifiables par un tiers sans demander son avis à l'auteur.**
— Ligne en A sans commande **et** sortie collées : la provenance tombe en C.
— Fait sans date : la robustesse est plafonnée à 3.
— Mesure dont le corpus de jugement n'est pas nommé, versionné et accessible : robustesse 4, quelle que soit la provenance.

### 4.4 Comment se lit le couple

Chaque ligne d'un retour porte deux signes, séparés d'un point médian : `A·1`, `B·2`, `D·4`.

| | **1 rejouable** | **2 attesté** | **3 étroit** | **4 non étayé** |
|---|---|---|---|---|
| **A mesuré** | **Porteur** | **Porteur daté** | Indicatif | Rejeté — une mesure sans corpus n'est pas une mesure |
| **B primaire** | **Porteur** | **Porteur daté** | Indicatif | Au dépôt |
| **C secondaire** | **Porteur daté** | Indicatif | Au dépôt | Au dépôt |
| **D mémoire** | *n'existe pas* | *n'existe pas* | Piste, avec échéance | Piste, avec échéance |

**Porteur** — on peut engager dessus du temps de développement, de l'argent, une signature.
**Porteur daté** — on engage, et la ligne porte la date à laquelle il faut la revérifier.
**Indicatif** — oriente le travail, ne porte aucun engagement. Entre au livrable, marqué.
**Au dépôt** — ne sert pas à décider. Ne disparaît pas : se range.
**Piste, avec échéance** — un travail à faire, avec la date à laquelle il doit être fait ou abandonné.

Trois lectures de cette grille, qui disent ce que les deux axes font gagner.

**`C·1` vaut plus que `A·3`, et c'est voulu.** Un comparatif dont le script de mesure est publié et rejouable porte davantage qu'une mesure maison faite sur quatre pages non déclarées. L'ancien barème disait l'inverse. Celui-ci dit ce qui est vrai.

**`D·1` et `D·2` n'existent pas.** Un souvenir n'est pas rejouable et ne laisse pas de trace : il n'y a rien à rouvrir. Un agent qui écrit `D·1` a confondu « j'en suis sûr » avec « un tiers peut refaire ». C'est la seule case du barème qui soit une faute de raisonnement et pas une faiblesse de preuve.

**`A·4` est rejeté, pas rangé.** Une mesure dont on ne sait pas sur quoi elle a été faite n'est pas une mesure faible : c'est un chiffre sans objet, et un chiffre sans objet est plus nuisible qu'une absence de chiffre, parce qu'il circule.

### 4.5 La règle de charge — ce qui remplace « aucune décision sur un cran B ou moins »

> **On engage du temps, de l'argent ou une signature sur un fait porteur — robustesse 1 ou 2 — quelle que soit sa provenance. On ne l'engage jamais sur une robustesse 3 ou 4, quelle que soit sa provenance.**

Un chiffre mesuré sur un échantillon de trois pages ne porte pas davantage qu'un souvenir : il porte seulement mieux l'illusion.

**Décider de reconstruire un organe exige deux faits porteurs, et deux seulement :**

| Ce qu'il faut savoir | Forme admise |
|---|---|
| Ce que produit le modèle repéré, **sur le corpus de jugement nommé** | `A·1` si on a pu le faire tourner ; `A·2` si la démonstration ne se rouvre pas ; `B·1` ou `B·2` si l'engagement contractuel de l'éditeur est publié, daté et cité |
| Ce qu'il manque aux briques libres recensées pour l'atteindre, et ce que coûte le manquant en jours | `A·1` sur les briques installées et essayées ; `B·1` sur leurs licences et leur état de maintenance |

**Aucune mesure de notre propre composant n'est exigée pour décider.** Il n'existe pas encore. La comparaison des deux côtés sur le même jeu d'épreuve reste exigée au **temps 6, pour prouver** — pas au temps 3, pour décider. C'est le verrou de la v4 : elle demandait la preuve de la fin pour autoriser le début.

> **Le temps 6 prouve. Le temps 3 décide. Ce ne sont pas les mêmes exigences.**

**L'étalon de repli, quand le modèle est hors de portée.** Le temps 2 suppose une version d'essai ou un compte de démonstration. Un éditeur peut refuser, et un guichet 1 hors de portée (l. 35) ne se laisse pas instrumenter. Dans ce cas, on ne bloque pas et on ne suppose pas : on mesure **l'étalon manuel** — ce que coûte, chez nous, le même service rendu à la main sur le corpus de jugement, en minutes par unité. Il est obtenu en `A·1`, sans aucun compte propriétaire, et c'est le vrai seuil : la chose que l'automatisation devra battre pour mériter d'exister. Le modèle à égaler n'est pas toujours l'outil du concurrent. C'est souvent le travail d'une personne.

**Les deux règles de guichet, conservées, réécrites sur le bon axe.**
— Aucun choix de voie d'accès ne se prend sur un fait non porteur. Le guichet 2 exige en outre le verdict du juriste, qui est un `B·1` ou rien.
— Tout acteur cité comme faisant déjà ce travail porte son guichet, son degré s'il s'agit du 5, et la provenance de cette information. « Inconnu » est une réponse admise. Une supposition n'en est pas une.

**Les règles de rejet, conservées.**
— Tout retour sans aucune ligne porteuse est relancé une fois. S'il revient sans ligne porteuse **et sans trace de ce qui a empêché d'en produire**, il tombe. Un retour vide **qui colle son journal de recherche et ses messages d'erreur** ne tombe pas : c'est un résultat, et il dit à la vague suivante ce qu'il faut outiller.
— Les interdictions explicites de l'ancienne section 4.3 sont maintenues sans changement.

*Note de réparation.* L'ancienne règle « un retour honnêtement vide vaut mieux qu'un retour plein de C » (l. 317) était contredite par « s'il revient en C ou D, il tombe » (l. 139) : le vide n'a par construction aucune ligne haute, donc il tombait. La réécriture ci-dessus lève la contradiction en faisant porter le rejet sur **l'absence de trace**, non sur l'absence de résultat. Un agent qui n'a rien trouvé et le prouve a travaillé. Un agent qui n'a rien trouvé et ne le prouve pas n'a peut-être pas cherché — et c'est cela qu'on veut distinguer.

---

## Pièce 2 — Le cran E, décision assumée sous incertitude

> *Nouvelle section 4.6. Ne va pas dans le barème des sections 4.2 à 4.4, et le dire fait partie de la règle.*

### 4.6 Le cran E

**Ce que E n'est pas.** E n'est pas un cinquième cran de provenance, et pas un cinquième chiffre de robustesse. Ce n'est pas un cran de preuve du tout : **c'est un cran de décision.** Il ne se note sur aucune ligne de fiche et il ne se range pas au barème. Il se range au **registre des décisions**.

Le dire ainsi n'est pas une subtilité de classement. Si E devenait un cran de preuve, il deviendrait le cran où l'on range ce qu'on n'a pas vérifié mais qu'on assume — c'est-à-dire une blanchisserie : toute ligne faible y passerait pour en sortir décidée. **Une décision E ne repeint aucune ligne.** Le fait reste `D·4` au livrable, visible, avec son couple. C'est la décision qui est E, et elle porte une date.

**Définition.** On décide sous E quand la charge n'est pas atteinte — aucun fait porteur disponible — et que l'on choisit d'avancer quand même, pour l'un des deux motifs suivants, nommé :
— **l'attente coûte plus que l'erreur** : le retour en arrière est chiffré et supportable, le temps perdu à attendre ne l'est pas ;
— **la preuve est inatteignable** : démonstration refusée, source primaire inaccessible, guichet muet, juriste non encore consulté. On a essayé, et la trace de l'échec est collée.

Aucun troisième motif. En particulier, « il faut bien avancer » n'en est pas un : c'est la formulation du premier motif sans le chiffrage qui le rend recevable.

**Les cinq champs. Une décision E qui n'a pas les cinq n'est pas une décision E : c'est une décision non prise.**

| Champ | Exigence |
|---|---|
| **1 — Qui décide** | Un nom. Jamais « on ». Jamais un agent |
| **2 — Ce qui n'est pas su** | Le fait manquant, en une phrase, dans sa propre langue, avec le couple actuel de la ligne concernée — par exemple `D·4` |
| **3 — Ce qui la falsifierait** | L'observation précise qui, si elle survient, rend la décision fausse. Pas « si ça ne marche pas » : « si le rappel sur le corpus de jugement reste sous tel seuil », « si le juriste conclut que le mandat n'est pas cessible » |
| **4 — Ce que coûte le retour en arrière** | En jours et en euros, au jour de la décision. C'est le prix de l'option qu'on achète, et c'est ce qui rend le premier motif recevable ou non |
| **5 — La date de réexamen** | Une date. Pas « plus tard ». Passée cette date sans réexamen, la décision est **réputée non tenue**, et l'organe concerné repasse en attente |

**La mécanique de révision.** Le registre des décisions E est relu à la fin de chaque vague, et à chaque date de réexamen échue. Trois issues, et elles sont écrites :
— **confirmée** — la preuve est arrivée, la ligne du champ 2 est montée en robustesse 1 ou 2, et la décision cesse d'être E. On la raye du registre en notant le couple obtenu ;
— **infirmée** — le falsifieur du champ 3 est survenu. On exécute le retour en arrière chiffré au champ 4, sans rediscuter : il a été accepté au moment de décider ;
— **prorogée** — une fois, et une seule, avec un coût de retour en arrière **recalculé**, car il a augmenté. Une décision E prorogée deux fois n'a jamais été prise : elle a été subie.

**Qui peut invoquer E.**

> **Laurent seul invoque E.** C'est la seule chose que ce barème lui réserve en propre, et c'est normal : E engage du temps et de l'argent qui sont les siens.

> **Un agent ne peut jamais invoquer E. Il doit la proposer.** Il nomme qu'une décision sous incertitude est nécessaire, remplit les champs 2 à 5, laisse le champ 1 vide, et s'arrête là. Il ne produit pas « en attendant » la version que la preuve n'autorise pas.

Un agent qui s'autorise lui-même à décider sous incertitude a transformé une limite de preuve en permis de produire. C'est le faux vert à son dernier étage, et c'est le plus difficile à voir, parce qu'il se présente comme de la lucidité.

**Le plafond.** **Trois décisions E ouvertes au maximum à un instant donné, toutes vagues confondues.** Au-delà, on ne décide plus sous incertitude : on navigue à vue, et il faut s'arrêter pour aller chercher de la preuve au lieu d'en emprunter. Le plafond est le seul dispositif qui empêche E de devenir la voie normale — et le **nombre de E ouvertes est le baromètre du projet**. Zéro pendant six mois : le barème est trop serré, ou personne ne décide. Trois en permanence : on construit sur du sable, et on le sait.

---

## Pièce 3 — Les deux vagues amont

> *Se place en tête de la section 8, avant V0. V0 à V5 gardent leur nom et leur numéro : rien d'autre n'est à renuméroter.*

### V-2 — Les nœuds soldés

Objet : fermer les cinq questions de la section 10 **avant** que la première vague ne s'ouvre. Deux d'entre elles changent le périmètre de V0, et une vague mal cadrée contamine les suivantes.

Pas d'agents : il n'y a rien à chercher, tout à trancher. Cinq gestes, et chacun produit une ligne écrite.

— **Mandat** — oui ou non. Si oui, la section 2.7 est confirmée et l'organe de garde des accès confiés existe. Si non, le volet avis tombe, et il faut retirer de ce document un organe, un agent de V3, un étalon et un pan de la section 2.7. Le document v4 avait déjà tiré toutes les conséquences du oui : cette vague les assume ou les défait.
— **Licences de contenu** — payer un droit de collecte pour la presse, ou bâtir le volet veille sur le guichet 6 seul au départ. La réponse fixe le périmètre de V0, donc elle se donne avant V0.
— **Façades** — professionnelle d'abord, grand public ensuite, ou les deux. La réponse « les deux » n'est recevable qu'accompagnée du budget qui la paie, puisqu'elle double le périmètre.
— **Qui construit** — un nombre de personnes, et un nombre de jours par semaine. Sans ces deux nombres, aucun coût en jours (temps 5) ne devient une date, et « le périmètre tenable en quatre-vingt-dix jours » de V5 est incalculable.
— **Budget temps, budget argent, et critère d'abandon** — trois chiffres : l'horizon de la première version utilisable, la somme engageable, et **le montant dépensé sans premier euro encaissé au-delà duquel on arrête**. Le troisième est le seul qui manque entièrement à la v4, et c'est celui qui protège les quatre autres.

Règle : chaque nœud se solde par une ligne au registre des décisions. Un nœud soldé sans preuve est une décision E, avec ses cinq champs, et compte dans le plafond de trois.

Livrable : **le cadre fermé** — cinq réponses écrites et datées, plus les décisions E ouvertes s'il y en a.

### V-1 — Le premier mandat

Objet : obtenir, d'**un seul** établissement guadeloupéen, le mandat qui est à la fois la première recette et le seul moyen licite d'accéder aux avis. Ce n'est pas une vague commerciale placée en tête par prudence de gestion. C'est une vague d'**approvisionnement en matière** : sans elle, le corpus d'avis de V0 n'existe pas, et l'étalon de l'organe Avis non plus.

Gestes :

— **Le service rendu à la main** — un établissement, un mois, facturé. Une personne lit les avis dans l'extranet du titulaire, rédige les réponses, les publie sous mandat. Aucune ligne de code. *Rejet si* : on construit un outil avant d'avoir rendu le service une fois.
— **Les pièces du mandat** — contrat, périmètre exact des accès confiés, procédure de révocation, journal des accès. C'est la première épreuve réelle de l'organe « garde des accès confiés », et elle arrive au bon moment : on détient des identifiants dès le premier jour, donc la garde se tient **par procédure écrite avant d'être tenue par outil**. C'est aussi la seule façon de traiter cet organe, que la méthode en six temps ne sait pas prendre : on ne repère pas « le meilleur chiffrement au repos du marché », on tient une procédure et on la vérifie.
— **Le relevé du coût manuel** — minutes par avis, par langue, par type de réponse, sur un mois plein. C'est l'étalon de repli de la section 4.5 : la chose à battre, mesurée chez nous, en `A·1`, sans aucun compte d'essai propriétaire.
— **Le versement au corpus** — les avis réellement reçus pendant le mois, avec leur date, leur langue et leur plateforme, versés au jeu d'épreuve sous le régime de la section 5bis.
— **La preuve du guichet** — ce que l'extranet du titulaire donne réellement : les avis sont-ils lisibles en entier, la réponse est-elle possible, l'export existe-t-il, un prestataire mandaté est-il admis par les conditions de la plateforme. Chacun de ces quatre points en `A·1` ou `B·1`, parce qu'ils décident de la faisabilité du volet entier et que la v4 les supposait.

Livrable : **le mandat tenu** — un contrat signé, une facture encaissée, un relevé de coût manuel en `A·1`, la preuve du guichet, et le premier versement du corpus d'avis.

**Ce qui bloque si cette vague échoue.** Il faut l'écrire, parce que c'est le point de rupture du programme entier.

Pas de mandat → pas d'avis réels → pas de corpus d'avis en V0 → pas d'étalon pour l'organe Avis, dont la métrique exige de connaître les avis **réellement présents**, ce que seul l'extranet du titulaire donne → aucune mesure possible au temps 6 → le volet avis ne se prouve jamais.

Et il n'existe aucun contournement dans ce document : le degré 5c est écarté, et le guichet 6 ne porte pas les avis de plateformes.

> **Règle d'arrêt. Si le premier mandat n'est pas signé, on ne lance pas le volet avis.** On lance le volet veille et collecte vérifiée, qui tient sur le guichet 6 et ne dépend d'aucun mandat, et on le lance seul. C'est un périmètre plus petit. C'est un périmètre qui existe.

Ce qu'on ne fait pas : dérouler V0 à V5 sur le volet avis en espérant que le client arrive au bout. Il est au début, ou il n'y a pas de volet avis.

---

## Pièce 4 — Les relances refondées sur la trace

> *Remplace la section 7 en entier.*

### 7. Les relances

Trois vices de la version précédente, nommés pour qu'on ne les refasse pas. Elle demandait **trois** candidats écartés — un cardinal fixe demandé à un agent qui sait nommer trois objets plausibles en quelques secondes, donc une incitation à l'invention. Elle demandait où le produit **perd de l'argent aujourd'hui** — alors qu'il n'y a ni produit, ni client, ni recette : une question à présupposition fausse ne peut recevoir qu'une réponse inventée. Et elle était **auto-administrée** : l'agent qui avait écrit les lignes reclassait ses propres lignes, dans le même contexte, alors que le même document exige par ailleurs qu'un tiers puisse rejouer une mesure.

Les deux relances qui suivent portent sur ce que l'agent a réellement fait, et la seconde ne lui est pas adressée.

### Relance 1 — la trace. Part avec chaque agent, en fin de recherche.

> Tu viens de rendre. Avant que je lise, colle quatre traces. Pas des intentions, pas des nombres choisis : ce que tu as fait.
>
> **Ton journal de recherche.** Les requêtes exactes, dans l'ordre, avec leur date, le nombre de résultats et le filtre appliqué. Les requêtes qui n'ont rien donné comptent autant que les autres : elles disent où il n'y a rien.
>
> **Les candidats que tu as ouverts et laissés.** Pour chacun : son URL, la date de consultation, et **laquelle des six exigences de la section 3** le disqualifie, citée dans ses mots. S'il n'y en a aucun, écris « aucun ». Zéro candidat écarté avec un journal complet est une réponse valable ; un nom sans URL est un retour rejeté. Aucun nombre n'est attendu — ni trois, ni dix.
>
> **Ce que tu n'as pas pu faire.** La commande qui a échoué, le compte refusé, la page bloquée, le document inaccessible, le délai qui t'a manqué : colle le message d'erreur. C'est souvent la partie la plus utile de ton retour, parce qu'elle dit ce que la vague suivante doit outiller avant de recommencer.
>
> **Où ce plan dépense sans acheter de décision.** Nomme la mesure de ton retour qui a coûté le plus de temps pour la décision la plus faible, et ce que tu supprimerais sans perdre une décision. Tant qu'aucun euro n'est encaissé, cette question porte sur le plan et non sur un produit : il n'y a pas de produit, et une question posée sur un produit inexistant ne peut recevoir qu'une réponse inventée.
>
> Rien à coller sur l'un des quatre points : écris « rien » et dis en une ligne pourquoi il n'y avait rien à faire.

### Relance 2 — la relecture. Ne part pas avec l'agent.

**Elle est appliquée au retour par quelqu'un qui ne l'a pas écrit** — Laurent, ou une session neuve ouverte pour cela, sans l'historique de la recherche. Un agent qui reclasse ses propres lignes n'est pas un contrôle : c'est le contrôlé qui tient le crayon.

Le relecteur note lui-même, sans demander son avis à l'auteur. Pour chaque ligne du retour :

> **Provenance.** La commande et la sortie sont-elles collées — `A` ? L'URL est-elle là, avec sa date, et rend-elle encore ce texte — `B` ? Est-ce un résumé, un comparatif, une parole de vendeur — `C` ? N'y a-t-il rien à quoi se raccrocher — `D` ?
>
> **Robustesse.** Un tiers refait-il le chemin avec ce qui est écrit — `1` ? La trace existe-t-elle alors que la source ne se rouvre plus — `2` ? L'échantillon, la date ou le corpus manquent-ils, ou sont-ils trop étroits — `3` ? Rien ne permet-il de refaire le chemin — `4` ?
>
> **Corpus.** Toute mesure nomme-t-elle son corpus de jugement, sa version et sa taille ? Sans cela, la ligne est `4`, quelle que soit sa provenance.
>
> **Guichet.** Pour chaque acteur cité comme faisant déjà ce travail : le guichet est nommé, avec son degré s'il s'agit du 5, et la provenance de cette information. « Inconnu » est accepté. Une supposition est rejetée.
>
> **Charge.** Chaque décision prise dans ce retour s'appuie-t-elle sur une ligne porteuse — robustesse 1 ou 2 ? Sinon : soit la décision tombe, soit elle devient une décision E proposée, champs 2 à 5 remplis, et elle attend Laurent.

Puis le relecteur écrit une chose de plus, et c'est la raison d'être de la relance : **l'écart**. Le couple qu'il a noté, contre celui que l'agent s'était donné, ligne par ligne, et le nombre de lignes où les deux diffèrent.

**Ce que l'écart mesure.** Pas l'agent : **le barème**. Si l'écart est nul sur dix retours, la relecture peut passer à un retour sur trois. S'il grandit, c'est que le barème est mal écrit ou mal compris, et c'est le barème qu'on corrige — pas l'agent qu'on sermonne. C'est le seul chiffre qui dira un jour si cette doctrine de preuve a servi à quelque chose. Il se tient au dépôt, daté.

**Ce qui est relu, et ce qui ne l'est pas.** Tout relire coûterait plus que produire. Donc : **tout retour qui porte une décision est relu en entier** ; tout retour qui se donne au moins une ligne porteuse est relu en entier ; les autres par échantillon, un sur N, N fixé à la fin de V-2 et révisé selon l'écart.

---

## Pièce 5a — La gouvernance du désaccord

> *Nouvelle section 4.7.*

### 4.7 Quand nous ne sommes pas d'accord

> **Laurent décide. L'agent objecte.** Les deux ne sont pas symétriques, et aucun des deux n'est facultatif. Un agent qui n'objecte pas manque à sa tâche autant qu'un agent qui refuse d'exécuter.

Trois cas, et il faut dire lequel on est en train de vivre avant de discuter.

**Cas 1 — désaccord de fait.** L'agent soutient que ce que Laurent tient pour vrai ne l'est pas, ou ne porte pas. **La preuve tranche, pas l'autorité.** On va voir : une commande, une page, un document primaire. Celui qui avait tort le note, et la ligne prend son couple. Si on ne peut pas aller voir — source inaccessible, compte refusé, juriste non consulté — on n'est plus dans le cas 1 : on est dans le cas 3, et il faut le dire au lieu de continuer à argumenter.

**Cas 2 — désaccord de méthode.** L'agent soutient que le geste demandé ne tiendra pas la doctrine : mesurer sur un corpus non figé, décider sur une robustesse 3, citer un acteur sans son guichet, livrer une ligne `D·4` sans son couple.

> **Devoir d'objection.** L'agent ne produit pas. Il dit laquelle des règles est en cause et où elle est écrite ; ce qu'il faudrait pour la tenir, et ce que cela coûte en jours ; et **la plus petite variante qui tient** — c'est cette troisième partie qui distingue une objection d'un refus. Il ne produit pas « en attendant » la version que la règle n'autorise pas, parce qu'une version provisoire livrée devient définitive par usage.

L'objection se fait **une fois**. Si Laurent maintient après l'avoir lue, on passe au cas 3. Un agent qui objecte deux fois la même chose ne contrôle plus : il résiste.

**Cas 3 — désaccord d'arbitrage.** Laurent veut avancer sans la preuve. **L'agent s'exécute**, et le prix de l'exécution est une décision E : l'agent la rédige, champs 2 à 5 ; Laurent remplit le champ 1 de son nom. Puis l'agent produit, en marquant au livrable chaque ligne dont la robustesse est insuffisante — non pour se couvrir, mais pour que le réexamen de la date de réexamen sache où regarder.

**Ce qui n'est jamais un désaccord d'arbitrage.** Trois choses, où l'agent ne s'exécute pas, même sous E, même sur instruction répétée :
— franchir une protection technique, une authentification ou une limitation — le degré 5c ;
— affirmer au livrable un fait en `D` en le présentant autrement qu'en `D` ;
— produire une mesure en nommant un corpus qui n'est pas celui qui a servi.

Motif, et il n'est pas moral : les deux premières exposent à un dommage que le champ 4 d'une décision E ne sait pas chiffrer, parce qu'un retour en arrière ne le répare pas. La troisième détruit l'instrument qui sert à tout le reste — un corpus dont on ne peut plus croire le nom ne juge plus rien, et toutes les mesures passées tombent avec lui. **Un refus sur ces trois points n'est pas une objection : c'est une limite**, et elle ne se négocie pas davantage que le fuseau horaire de la Guadeloupe.

**La consignation.** Tout désaccord laisse une ligne au **registre des désaccords**, au dépôt, à côté du registre des décisions : la date, l'objet en une phrase, le cas — fait, méthode, arbitrage —, ce que l'agent a soutenu, ce que Laurent a tranché, et le renvoi à la décision E s'il y en a une. Deux lignes par désaccord suffisent.

Ce registre n'est pas un tribunal. Il sert à une seule chose : savoir, au bout de six mois, **qui avait raison et sur quoi**. C'est la seule façon de régler la confiance au bon niveau. Si l'agent a eu raison trois fois sur la méthode, on l'écoute plus tôt et on gagne du temps. S'il a bloqué trois fois pour rien, le barème est trop serré et c'est lui qu'on desserre. Sans ce registre, le désaccord se règle à la fatigue, et c'est toujours la même partie qui gagne.

---

## Pièce 5b — Le jeu d'épreuve et les données personnelles

> *Nouvelle section 5bis, après la méthode en six temps.*

### 5bis. Constituer un corpus de jugement qui reste conforme

**Le problème, posé net.** Le corpus de jugement doit être figé, parce que c'est son immobilité qui rend les mesures comparables. Il contient des avis réels, donc des données personnelles — un avis porte un prénom, souvent un pseudonyme rattachable, parfois un récit qui identifie son auteur mieux que son nom. Et les données personnelles portent un droit à l'effacement et un droit à la rectification, qui sont des droits à **modifier le corpus**.

Un objet qui doit être immuable et qui doit pouvoir être modifié n'existe pas.

**Et il n'y a pas d'échappatoire par l'anonymisation.** Retirer le prénom ne rend pas un avis anonyme : le texte lui-même est l'identifiant, puisqu'il est publié et qu'une recherche sur une phrase exacte retrouve son auteur. Or c'est précisément le texte qu'il faut garder, puisque les métriques d'extraction, de langue et de rédaction portent sur lui. **Un corpus d'avis verbatim est irréductiblement un corpus de données personnelles**, aussi longtemps qu'il est utile. ⏳ Qualification juridique à confirmer par le juriste de V1 : le raisonnement est tenu ici en `B·1` sur la logique, pas en `B·1` sur le droit.

**Ce que cela donne comme résultat, et c'est un résultat et non un échec :** il n'existe pas de corpus d'avis à la fois pleinement figé et pleinement conforme. Ce qu'on peut construire, c'est un corpus **dont l'attrition est déclarée**. Le document possède déjà le principe qui le permet, au temps 6 :

> Un écart avoué nourrit l'arbitrage ; un écart masqué tue le produit.

Appliqué au corpus : une perte avouée nourrit la mesure ; une perte masquée tue l'étalon.

**La mécanique, en quatre règles.**

**1 — Deux couches, et une seule est gelée.**

| Couche | Contenu | Régime |
|---|---|---|
| **La couche de jugement** | Les attentes : pour ce document, les champs attendus et leurs valeurs ; pour cette requête, les documents pertinents ; pour cet avis, la réponse acceptable. Écrite en **références et en valeurs attendues**, jamais en verbatim | **Gelée, versionnée, publiable.** Ne contient pas de données personnelles si elle est écrite ainsi. C'est elle, le juge |
| **La couche de matière** | Les textes eux-mêmes : pages, avis | **Effaçable, et l'effacement est consigné.** Conservée au périmètre du mandat, jamais publiée |

Le juge n'est pas le texte. Le juge est la grille d'attentes qui porte sur le texte. C'est cette distinction qui rend le problème soluble en partie : on gèle ce qui doit l'être, et c'est justement la partie qui n'a pas de titulaire de droits.

**2 — L'effacement laisse un trou déclaré, pas une cicatrice invisible.** Quand un avis est supprimé sur demande, le corpus ne redevient pas entier : il garde une **pierre tombale** — identifiant interne, date de l'effacement, langue, plateforme, et la liste des mesures auxquelles cet élément contribuait. Rien du contenu. On sait qu'il y avait là quelque chose, et de quelle sorte.

**3 — Toute mesure porte le taux de trous de la version sur laquelle elle a tourné.** « Rappel de 0,78 sur le corpus de jugement v1.0, taux de trous 0 % » et « 0,74 sur v1.3, taux de trous 2,1 % » sont comparables, avec la réserve écrite. Une mesure qui ne déclare pas le taux de trous de sa version est en robustesse 4.

**4 — Au-delà d'un seuil de trous, la version est retirée et une nouvelle version de référence est coupée**, sur laquelle les étalons sont remesurés. Le seuil se fixe à la fin de V-2, **avant le gel** — pas à la première demande d'effacement, parce qu'un seuil fixé sous la pression d'un cas est un seuil choisi pour ce cas. ⏳ Valeur à fixer : je n'ai aucune base pour l'inventer, et au-delà duquel un corpus cesse de juger n'est pas une question que ce document peut trancher de mémoire.

**Le reste du régime, en cinq lignes.**
— **Base légale** : le mandat du titulaire pour les avis de ses propres établissements. ⏳ Qualification exacte par le juriste de V1 — c'est la première question à lui poser, avant même la cessibilité du mandat.
— **Minimisation** : du verbatim, rien que ce que la mesure exige. Pas de profil, pas de photo, pas d'identifiant de compte, pas d'historique d'auteur. Ce qui n'entre pas au corpus n'a pas à en sortir.
— **Durée** : une durée de conservation par version de corpus. La retraite d'une version est une **suppression**, pas un archivage perpétuel « au cas où ».
— **Procédure d'effacement** : écrite, avec un délai, un responsable nommé et un journal. C'est la même exigence que la garde des accès confiés, donc le même organe la porte, et elle se tient par procédure dès V-1.
— **Périmètre** : le corpus de matière **ne sort jamais du périmètre du mandat**. On ne le publie pas pour prouver quoi que ce soit à un tiers. On publie la couche de jugement et les chiffres, et on offre de rejouer la mesure chez nous, sous accord.

**La conséquence sur le barème, et elle est désagréable, donc elle s'écrit.** Pour le volet avis, la robustesse `1` — rejouable par un tiers — n'est atteignable **qu'en audit sous accord**, par un tiers admis au périmètre. Pour un lecteur extérieur, une mesure sur avis réels plafonne à `2` : la trace existe, le chemin ne se refait pas publiquement. Ce n'est pas une faiblesse de notre travail, c'est une propriété du matériau. L'écrire évite deux erreurs symétriques : croire qu'on a du `1` quand on a du `2`, et renoncer à mesurer parce qu'on ne peut pas publier le corpus.

Le volet veille, lui, tient sur le guichet 6 — données ouvertes, flux publiés, communs documentaires. Son corpus est publiable, donc ses mesures atteignent `1` pour de vrai. **C'est une raison de plus de commencer par là.**

---

## Les deux questions que tu m'as posées

### Laquelle des cinq livraisons je suis le moins sûr de tenir

**La pièce 5b, le corpus conforme.** Sans hésitation, et pour trois raisons de nature différente.

D'abord, sa prémisse est juridique et je ne suis pas juriste : j'affirme qu'un corpus d'avis verbatim est irréductiblement du traitement de données personnelles parce que le texte est son propre identifiant. C'est un raisonnement, pas un constat sur source primaire — et le juriste de V1 peut renverser la prémisse, par exemple en qualifiant une pseudonymisation suffisante dans un périmètre fermé. Si la prémisse tombe, la pièce entière devient inutilement lourde.

Ensuite, le mécanisme du taux de trous est une conception que j'ai faite dans cette session et que je n'ai jamais vue tourner. Je ne sais pas à quel taux d'attrition un corpus cesse d'être un juge, et je n'ai pas de base pour le fixer — j'ai marqué le seuil ⏳ plutôt que de l'inventer, mais un dispositif dont le paramètre décisif est inconnu n'est pas encore un dispositif. C'est une direction.

Enfin, c'est la seule des cinq pièces dont je ne sais pas nommer le mode de panne. Pour les quatre autres, je peux dire comment elles casseront : le barème à deux axes cassera par bureaucratie si noter un couple sur chaque ligne devient plus long que produire la ligne ; le cran E cassera si le plafond de trois n'est pas tenu ; les vagues amont casseront si V-1 est lancée sans que V-2 ait fermé le nœud du mandat ; les relances casseront si personne ne fait la relecture, et il n'y a alors plus de relance 2 du tout, seulement une relance 1. Pour la pièce 5b, je ne sais pas par où elle lâchera — ce qui veut dire que je ne l'ai pas assez éprouvée.

**Deuxième moins sûre, et je la nomme parce que l'écart est faible : le coût d'adoption du barème à deux axes.** La conception tient, et la conversion de l'existant est mécanique — c'est pour cela que j'ai gardé tes lettres. Mais je ne l'ai testé sur aucune fiche-organe réelle. Je ne sais pas si noter deux signes sur chaque ligne reste supportable au bout de la cinquantième ligne, ni si les agents convergeront sur la frontière entre `2` et `3`, qui est la plus floue des quatre — « la trace existe mais la source ne se rouvre pas » contre « l'échantillon est trop étroit » se recouvrent dans les cas réels. Le chiffre de l'écart de la relance 2 est précisément là pour le mesurer, mais il n'existera qu'après dix retours. D'ici là, c'est une promesse.

### Quelle pièce déclarée saine mérite un second regard

J'avais déclaré saines trois pièces : les six guichets, le gabarit de fiche-organe, les six temps. Celle qui mérite le second regard est **le gabarit de fiche-organe**, et je n'avais vu de lui que ses défauts internes — le renvoi « des sept » faux, et le « Cran de preuve » apposé à un « Verdict ». Je n'ai pas posé la vraie question, qui est celle de sa **maille**.

Le gabarit est organisé **par organe**. Or la plupart des champs qu'il demande ne sont pas des propriétés d'organe.

Le **guichet** se qualifie source par source — c'est la correction centrale de ta v4, l. 44 — et plateforme par plateforme en V1. Il ne se qualifie pas par organe : l'organe Extraction n'a pas de guichet, les sources qu'il traite en ont.

Le **coût réel à l'échelle visée** est une propriété de la pile entière : un serveur, des quotas, une licence de contenu et une maintenance humaine ne se découpent pas en huit parts sans arbitraire, et la somme des huit coûts d'organes ne sera pas le coût du produit.

Les **six exigences guadeloupéennes** sont, pour quatre d'entre elles au moins, des propriétés du produit et non d'un organe. Le fuseau horaire n'appartient pas à « extraction ». Le droit non plus. Le tissu économique encore moins.

Conséquence, et elle est invisible dans le dispositif actuel : le gabarit fait **répondre huit fois à des questions qui ont une seule réponse**. Huit fois le fuseau, huit fois le droit, huit fois le coût d'hébergement — par huit agents différents, dans huit fiches lues séparément. Les huit réponses divergeront, parce que des réponses réécrites divergent toujours, et **la divergence ne sera vue par personne**, puisque chaque fiche est relue seule et paraît cohérente. C'est le faux vert à l'échelle du classeur : chaque pièce est verte, l'ensemble ne tient pas.

Deux manques s'y ajoutent, du même ordre et que je n'avais pas relevés. La fiche n'a **pas de champ de péremption** — aucune date à laquelle il faut la refaire, alors que le document sait que les conditions d'accès changent tous les six mois. Et elle n'a **pas de champ pour la version du corpus** sur laquelle l'écart à l'étalon a été mesuré, ce qui rend deux fiches d'organes différents non comparables sans qu'on puisse le détecter.

La réparation est courte et je la laisse en l'état, parce qu'elle sort du périmètre que tu m'as donné : scinder le gabarit en deux formulaires. Une **fiche de produit**, remplie une fois, qui porte le fuseau, le droit, l'hébergement, le tissu économique, le coût de pile et les guichets retenus. Une **fiche d'organe**, remplie huit fois, qui ne porte que ce qui varie d'un organe à l'autre — le modèle repéré, l'étalon, le manquant, l'écart chiffré, la version du corpus, la date de péremption — et qui **renvoie** à la fiche de produit au lieu de la recopier. Un renvoi ne divergera pas.

---

*Réparation écrite le 2 octobre 2026. Premier fichier de critique et document cible non modifiés. Aucun commit.*
