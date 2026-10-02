# Critique adversariale — doctrine de preuve, relances, enchaînement des vagues

Cible : `/home/user/moteurs-et-outils/00-PROMPT-DE-LANCEMENT.md`, version 4 du 2 octobre 2026, lue intégralement le 2 octobre 2026 (329 lignes, document non modifié).
Angle : section 4 (doctrine de preuve), section 7 (relances), section 8 (les six vagues), cohérence interne de l'ensemble.
Posture : chercher à casser. Un constat qui approuve n'est pas rapporté.

---

## 0. Déclaration des lignes en cran D — avant le contenu

Conformément à la règle de la ligne 135 du document attaqué.

| Ligne de ma critique | Pourquoi D |
|---|---|
| **Ryanair c. PR Aviation** — que l'arrêt soit de 2015, de la CJUE, et qu'il porte sur la protection contractuelle d'une base non protégée | Mémoire du modèle. Source primaire non consultée : l'accès réseau sortant est bloqué (voir § 6, relance 2) |
| **NLA c. Meltwater** — que ce soit une affaire de droit d'auteur sur titres et extraits, et non une affaire de contrat opposé à l'aspiration | Mémoire du modèle. C'est sur cette base que j'affirme en C8bis que la section 2.5 commet un glissement de catégorie. Non vérifié |
| **Booking, Google Business Profile, Centre français d'exploitation du droit de copie** — tout ce que je pourrais dire de leurs conditions réelles | Mémoire. Je ne dis donc rien de leur exactitude : je n'attaque que leur **statut dans le document**, ce qui est du cran B |
| **« les conditions d'accès aux plateformes changent tous les six mois »** | Reprise de la ligne 133 du document, non vérifiée par moi. Je l'utilise comme prémisse interne du document, pas comme fait |

Lignes en cran **C** (à verser au dépôt, pas au livrable) :

| Ligne | Pourquoi C |
|---|---|
| Le code Admiralty / OTAN (STANAG 2511, AJP-2.1) note séparément la **fiabilité de la source** (A–F) et la **crédibilité de l'information** (1–6) | Connu par résumé de moteur de recherche le 2 octobre 2026. Les deux sources primaires visées, `en.wikipedia.org/wiki/Admiralty_code` et `book.gradepro.org`, sont **bloquées par le proxy de sortie** (erreur `EGRESS_BLOCKED`), de même que `gradeworkinggroup.org` et `kravensecurity.com` (`CONNECT tunnel failed, 403`). Donc : pas de document primaire cité avec URL consultée → pas de B |
| GRADE sépare la **certitude de la preuve** de la **force de la recommandation**, et admet des recommandations fortes sur preuve de faible certitude dans des situations paradigmatiques nommées | Même raison. C. Le fond de l'argument tient sans lui — il tient par la logique interne du document — mais je ne le présente pas comme établi |

Lignes en cran **A-usage** (commandes passées dans la session, sorties collées en § 6) : les comptages mécaniques — 8 lignes d'organes en section 6, 17 occurrences de ⏳, et l'archéologie git v3 → v4.

Toutes les autres lignes de cette critique sont en **cran B** : document primaire unique, cité au passage exact, avec numéro de ligne.

**Déclaration supplémentaire, et elle gêne le barème du document.** Mon verdict final (§ 5) n'est ni A, ni B, ni C, ni D. C'est un **raisonnement**, pas un fait. Le barème de la section 4.1 ne sait classer que des faits. Or le gabarit de fiche-organe (ligne 163) exige un champ « Verdict — Adopter tel quel … adapter … reconstruire … renoncer » **et** un champ « Cran de preuve » (ligne 166) sur la même fiche. Le cran s'appliquera donc, dans les faits, au verdict lui-même : un jugement portera l'étiquette d'un fait mesuré. C'est le premier endroit où le barème fabrique exactement ce qu'il prétend interdire — du faux vert, ligne 133.

---

## 1. Les contradictions internes

Une par une, passage cité des deux côtés.

### C1 — Le verrou logique : le cran qui autorise à construire n'existe qu'après avoir construit

C'est la contradiction centrale. Elle suffit à elle seule à bloquer le programme.

Côté définition, ligne 127 :

> **A — mesure** | L'agent a mesuré contre l'étalon, sur le jeu d'épreuve figé, et **colle les chiffres des deux côtés**

« Des deux côtés » : le modèle repéré **et** le nôtre. Un A-mesure exige donc que notre composant existe et produise des chiffres.

Côté règle de décision, ligne 140 :

> — **Aucune décision de construire ne se prend sur un cran B ou moins.** Décider de reconstruire exige **un A-mesure sur le modèle repéré**

Et côté méthode, la construction est au temps 5 (ligne 189) tandis que la comparaison chiffrée des deux côtés est au temps 6 (ligne 190) :

> **6** | **Prouver sur le même jeu d'épreuve** — même entrée, même métrique, comparaison chiffrée

Mise bout à bout : pour décider de reconstruire (avant le temps 5) il faut un A-mesure, qui par définition n'est obtenable qu'au temps 6, après le temps 5. **La condition d'entrée dans la construction est une sortie de la construction.** Appliqué à la lettre, le document interdit d'atteindre son propre temps 5. Aucun organe ne peut jamais être reconstruit, c'est-à-dire que rien ne peut jamais être construit — alors que « on construit » est la première décision tranchée du document (ligne 16).

Il n'y a que trois issues, et le document n'en choisit aucune : soit « A-mesure sur le modèle repéré » signifie un A-mesure **à un seul côté**, et la définition de la ligne 127 est fausse ; soit la règle de la ligne 140 est inapplicable ; soit on la viole en silence au premier organe — et c'est ce qui arrivera.

**Même bullet, deux seuils incompatibles.** La première phrase de la ligne 140 interdit « un cran B ou moins » : dans la hiérarchie du tableau 4.1, A-usage est au-dessus de B, donc un A-usage suffit à décider de construire. La seconde phrase de la même ligne exige un A-mesure. Deux seuils pour le même acte, dans la même puce, à quatorze mots d'intervalle.

### C1bis — Le temps 2 est impraticable là où l'enjeu est le plus fort, et le document le sait

Ligne 186 :

> **2** | **Instrumenter le modèle** — le faire tourner sur un jeu d'épreuve réel guadeloupéen, **par version d'essai ou compte de démonstration**

Confronté au verdict du guichet 1, ligne 35 :

> Booking opère un programme partenaire connectivité ⏳ D … Coût d'entrée : **Élevé — contrat, certification, volume minimum** ⏳ … **Hors de portée au départ.** À réexaminer à trois ans

Et à la clause d'interdiction, ligne 186, colonne rejet :

> Rejet si : **Les chiffres viennent de la documentation du vendeur**

Exemple concret, l'organe le plus commercialement important. Étalon de l'organe **Avis**, ligne 210 :

> **Part des avis captés sur ceux réellement présents** … délai de détection … taux de réponse sous 24 h | **C'est ce que le client paie**

Pour mesurer cette part, il faut connaître le dénominateur : le nombre d'avis **réellement présents** sur la plateforme. Ce dénombrement exhaustif exige soit l'extranet du titulaire — guichet 2, donc un mandat, donc un client signé et le verdict juriste de V1 (ligne 261) — soit une lecture exhaustive de la plateforme, c'est-à-dire le degré 5c, **écarté** (ligne 50). Il n'existe pas de troisième voie.

Donc : la métrique dont le document dit « c'est ce que le client paie » est la seule qu'on ne peut mesurer ni sans client, ni sans commettre l'acte que le document écarte. Et sans cette mesure, pas de A-mesure, donc pas de décision de construire (ligne 140), donc pas de produit, donc pas de client. Le verrou C1 n'est pas théorique : il se referme sur l'organe central.

### C2 — « Cinq guichets » contre six, et la preuve que la passe de révision n'a pas été faite

Ligne 29, titre de section :

> ### 2.2 L'obstacle d'accès — **un péage à cinq guichets**

Ligne 31, corps du même paragraphe :

> il y a **cinq voies d'accès** licites ou risquées

Et le tableau qui suit immédiatement en compte six, jusqu'à la ligne 40 :

> | **6 — Accès ouvert déclaré** | … | **Notre voie principale pour la collecte d'informations** |

Confirmé par le gabarit, ligne 158 : « Lequel **des six** ».

Ce n'est pas une coquille isolée, et je peux le prouver. Diff v3 → v4 (`git diff 4c0858c 8070f2c`), sortie collée :

```
-— v3 : le mur juridique n'est pas un mur mais **un péage à cinq guichets** … ajout du cran de preuve D
+— v3 : le mur juridique n'est pas un mur mais **un péage à guichets** … ajout du cran de preuve D
-| **Guichet emprunté par ce modèle** | Lequel des cinq, et à quel coût — ou « inconnu », jamais une supposition |
+| **Guichet emprunté par ce modèle** | Lequel des six, degré précisé s'il s'agit du 5, et à quel coût — ou « inconnu », jamais une supposition |
```

La v4 a corrigé la ligne 7 et la ligne 158, et **a laissé le titre de la ligne 29 et son corps ligne 31**. La révision a donc été partielle, sans passe de cohérence. Un document dont la doctrine entière repose sur des contrôles qui refusent de produire (section 9) n'a pas appliqué à lui-même le plus élémentaire : compter les lignes de son propre tableau.

### C3 — Le degré 5a est une case qui se déclare vide, et la section 9 en exige l'usage

Ligne 48 :

> | **5a** | Atteignable, et **ouverture déclarée** … | **Ce n'est pas du guichet 5, c'est du guichet 6** | **Retenu** |

Une classe dont la définition du risque est « cette classe n'existe pas » et dont le verdict est pourtant « Retenu » : la taxonomie contient une case nulle. Et ligne 313, dans ce que le document refuse de produire :

> — L'étiquette « zone grise » employée **sans préciser le degré 5a, 5b ou 5c**

Le document rend donc obligatoire la mention d'un degré qu'il vient de dissoudre. Un agent qui classe correctement une source en guichet 6 sera formellement en faute s'il ne dit pas « 5a » ; s'il dit « 5a », il contredit la ligne 48. Le piège se referme dans les deux sens.

### C3bis — Le degré 5b est retenu sur une base de preuve que le document interdit

Ligne 49 :

> | **5b** | Atteignable sans restriction technique ni authentification, et conditions d'utilisation **muettes** sur la réutilisation | Faible à moyen | **Retenu sous conditions**, avec fiche de qualification |

Ligne 141 :

> — **Aucun choix de guichet ne se prend sur un cran D.** Le choix de la voie d'accès exige **un B minimum**

Le cran B, ligne 129, c'est « Document primaire cité avec URL et date de consultation ». Or le fait caractéristique du 5b est un **silence** : l'absence de clause. Un silence n'est pas un document primaire ; aucune URL n'atteste qu'une permission existe. La fiche de qualification du 5b ne pourra jamais enregistrer qu'une absence, c'est-à-dire au mieux un B sur l'état d'un texte à une date, jamais un B sur la licéité de la réutilisation. Le 5b est donc retenu sur une inférence — exactement ce que la ligne 141 veut proscrire.

Et ligne 52, une phrase qui se réfute elle-même :

> **Les conditions du 5b sont des règles de conception de notre collecteur, non des promesses.**

suivie quatre lignes plus bas, ligne 57, de :

> — **Retrait sous demande de l'éditeur, procédure écrite et tenue**

Une procédure écrite et tenue envers un tiers **est** une promesse. C'est même la seule des cinq puces qui ne soit pas une règle de conception.

### C4 — « Sept organes » contre huit, erreur conservée depuis v3

Ligne 156, gabarit de fiche-organe :

> | Organe visé | Lequel **des sept** de la section 6 |

La section 6 en compte huit. Comptage mécanique, sortie collée :

```
$ sed -n '202,212p' 00-PROMPT-DE-LANCEMENT.md | grep -c '^| \*\*'
8
```

Découverte, Extraction, Index, Provenance, Rédaction, Publication, Avis, et ligne 211 :

> | **Garde des accès confiés** | … | **Nouveau en v3 : c'est la condition du guichet 2, donc de tout le produit** |

Et la v3 comptait déjà huit lignes en section 6 (`git show 4c0858c … | grep -c` → 8) tout en écrivant « sept ». L'erreur a traversé deux révisions sans être vue. Elle n'est pas cosmétique : elle est dans le **gabarit**, c'est-à-dire dans la pièce que chaque agent recopiera. Chaque fiche produite portera un renvoi faux.

**Correction d'une des pistes qui m'ont été données.** Il m'a été suggéré que la section 8 ne tiendrait pas compte du huitième organe. C'est faux, et je le dis : la ligne 285 lui donne un agent en V3 (« **Garde des accès confiés** — l'organe nouveau de la v3 »). L'oubli est en 4.4, et en section 5 — voir C5.

### C5 — La méthode en six temps est inapplicable au huitième organe, alors qu'elle se déclare universelle

Ligne 181 :

> S'applique **à chaque organe** sans équivalent libre. Aucune construction avant le temps 3.

Ligne 185, temps 1 :

> **Repérer le modèle** — le meilleur existant, propriétaire inclus | Un nom précis, une version, ce qu'il fait exactement, **et son guichet d'accès** | Rejet si : L'agent nomme une catégorie au lieu d'un produit

Appliquons-le à l'organe de la ligne 211 :

> Chiffrement au repos … révocation effective en minutes … journal d'accès complet … cloisonnement entre clients

Quel est « le meilleur existant, propriétaire inclus », d'un **chiffrement au repos** ? Quelle « version » a une révocation en minutes ? Quel « guichet d'accès » emprunte un cloisonnement entre clients ? Ce ne sont pas des produits, ce sont des **propriétés**. Le temps 1 exige un produit sous peine de rejet, le temps 2 exige de le faire tourner sur un corpus de pages et d'avis guadeloupéens — ce qui est dépourvu de sens pour une propriété de sécurité. Donc l'organe que la ligne 211 déclare « la condition … de tout le produit » est précisément celui que la méthode ne sait pas traiter, et il est le seul des huit dont les seuils ne pourront pas être « fixés en V0 sur le jeu d'épreuve réel » (ligne 200) puisqu'un jeu d'épreuve documentaire ne juge pas une révocation.

### C6 — Le mandat est tranché en 2.7 et redemandé en 10

Ligne 100 :

> Conséquence de conception : le produit est **nativement un outil sous mandat**. Cela impose une gestion des accès confiés au niveau d'un établissement bancaire … **Ce n'est pas une option**, c'est le socle de la confiance qui nous donne l'accès.

Ligne 325, premier nœud ouvert, « décisions attendues de Laurent » :

> | **Produit sous mandat** | Le guichet 2 fait du produit un outil qui détient les accès de ses clients. **L'acceptes-tu**, avec les obligations de garde que cela impose ? | Cela change la nature du produit et **ajoute un organe à construire** |

La décision est à la fois prise (« ce n'est pas une option ») et à prendre (« l'acceptes-tu ? »). Pire : la colonne « pourquoi c'est bloquant » annonce au futur une conséquence déjà exécutée au passé — l'organe est **déjà** ajouté en section 6 ligne 211 et **déjà** doté d'un agent en V3 ligne 285. On demande à Laurent d'arbitrer un sujet dont le document a déjà tiré toutes les conséquences dans son architecture. Si Laurent répond non, il faut retirer un organe de la section 6, un agent de V3, un étalon, et le socle de 2.7. Le nœud n'est pas ouvert : il est verrouillé et présenté comme ouvert.

Et ligne 36, dans le tableau des guichets, le même choix est déjà fait une troisième fois :

> | **2 — Mandat du titulaire** | … | **Notre voie principale** |

### C6bis — Deux « voies principales », et c'est la mineure qui façonne le produit

Ligne 36 : guichet 2, « **Notre voie principale** ». Ligne 40 : guichet 6, « **Notre voie principale pour la collecte d'informations** ». Deux portes principales, sans hiérarchie déclarée. Or ligne 74 :

> — **Débloqué** : une part probablement importante du corpus guadeloupéen institutionnel et de presse pour le volet veille et collecte vérifiée ⏳ proportion à établir en V0. **C'est le cœur des moteurs, donc c'est décisif**

Le guichet 6 sert « le cœur des moteurs ». Le guichet 2 sert le volet avis. Et c'est le guichet 2 qui, en 2.7, impose « nativement » la forme du produit entier et un organe de sécurité « au niveau d'un établissement bancaire » (ligne 100). Le document fait donc porter le coût de conception le plus lourd par la porte qui ne dessert pas son cœur déclaré. Ce n'est pas une contradiction formelle, c'est une incohérence d'arbitrage — et elle n'est nulle part discutée.

### C7 — Le cran D est interdit en livrable, et la doctrine elle-même roule sur du D

Ligne 131 :

> | **D — mémoire du modèle** | Ce que l'agent croit savoir, sans vérification dans la session | **Piste de recherche uniquement. Interdit en livrable. Jamais fondement d'une décision** |

Ligne 141 :

> — **Aucun choix de guichet ne se prend sur un cran D.**

Relevé mécanique des lignes marquées D dans le document, sortie collée (`grep -n 'cran D\|⏳ D'`) — six lignes de contenu, plus la déclaration de 2.5 :

- ligne 35 : « Booking opère un programme partenaire connectivité **⏳ D** » → verdict rendu sur cette ligne : « Hors de portée au départ »
- ligne 37 : « Google Business Profile fonctionne ainsi **⏳ D** » → verdict : « **Retenue** »
- ligne 38 : « le Centre français d'exploitation du droit de copie gère les droits de panorama de presse **⏳ D** » → verdict : « **Retenue pour la veille presse** »
- lignes 67, 68, 71 : les trois familles du guichet 6, **⏳ D** → ce sont les exemples qui fondent « notre voie principale pour la collecte d'informations »
- ligne 81 : « **⏳ Citées de mémoire, cran D.** Vérification sur source primaire obligatoire en V1 »

Trois **choix de guichet** sont donc rendus sur des lignes explicitement marquées D : retenir le 3, retenir le 4, écarter le 1. Et l'écartement du 5c, ligne 50, est motivé par la section 2.6, dont les quatre motifs reposent sur la jurisprudence de la section 2.5, déclarée D à la ligne 81. Le document viole sa propre règle la plus dure quatre fois, dans son propre texte, sur les décisions les plus structurantes qu'il prenne.

On peut objecter que ce document est un prompt de lancement, pas un livrable d'agent. L'objection ne tient pas : la ligne 131 écrit « Jamais fondement d'une décision », sans réserve d'auteur, et le document prend les décisions. Et la ligne 16 de la section 1 présente ces choix comme « ce qui est tranché ».

**Et la forme n'est pas tenue non plus.** Ligne 135 :

> Règle : **tout agent déclare ses lignes D en tête de retour, avant le contenu.** Un retour qui n'en déclare aucune est suspect et relancé.

Le document ne déclare aucune ligne D en tête. Ses marques D sont dispersées en cellules de tableaux, aux lignes 35 à 81, et la seule déclaration groupée (ligne 81) arrive en page intérieure et ne couvre que deux arrêts. Le gabarit n'est pas appliqué par celui qui l'impose, ce qui est la façon la plus rapide de rendre une règle facultative.

### C8 — Le retour honnêtement vide est préféré en section 9 et tué en section 4.2

Ligne 317 :

> Si la matière manque, l'agent le dit avant de produire. **Un retour honnêtement vide vaut mieux qu'un retour plein de C.**

Ligne 139 :

> — **Tout retour sans ligne A ni B est relancé une fois. S'il revient en C ou D, il tombe**

Un retour honnêtement vide n'a par construction ni ligne A ni ligne B. Il est donc relancé. Relancé, il revient vide — l'honnêteté n'ayant pas fait apparaître de matière entre-temps. Et il tombe. La section 9 recommande le comportement que la section 4.2 sanctionne. Un agent qui lit les deux sections comprend, correctement, que l'aveu de vide est puni et que la production de C est au moins relancée : l'incitation nette pousse à **habiller du C en B**, c'est-à-dire à accrocher une URL plausible sur une affirmation de mémoire. Le dispositif produit mécaniquement ce qu'il veut interdire.

**Et « il tombe » n'est défini nulle part.** Le retour tombe ? L'agent tombe ? Le sujet est abandonné ? Qui reprend, avec quel mandat, sous quel délai ? Une règle de rejet sans procédure de reprise n'est pas une règle de qualité, c'est un cul-de-sac.

### C8bis — La section 2.5 fait dire à Meltwater autre chose que ce qu'elle dit (cran D, assumé)

Ligne 79, titre :

> ### 2.5 Les deux décisions qui expliquent pourquoi **le degré 5c** est un pari

Ligne 85 :

> **Newspaper Licensing Agency contre Meltwater** … un acteur majeur de la veille média a dû prendre licence pour ses revues de presse. Réponse directe à la question « comment font les outils de veille » : **ils ne contournent pas, ils paient.**

Les deux arrêts ne soutiennent pas la même proposition. Ryanair, s'il dit bien ce que la ligne 83 lui fait dire, porte sur le **contrat** opposable malgré l'absence de protection légale — c'est l'argument du 5c. Meltwater, à ma connaissance (**cran D**, non vérifié, accès réseau bloqué), porte sur le **droit d'auteur** attaché aux titres et extraits de presse et sur la licence des utilisateurs finaux : c'est l'argument du **guichet 4**, la licence de contenu, ligne 38 — pas celui du 5c. Les grouper sous « les deux décisions qui expliquent pourquoi le degré 5c est un pari » mélange deux fondements juridiques distincts pour renforcer une conclusion déjà prise. C'est exactement la faute que la ligne 149 interdit sous une autre forme : raisonner sur la pratique d'un acteur sans nommer précisément son guichet.

Je classe cette attaque en D et je ne la compte pas comme acquise. Mais elle désigne un contrôle à faire en V1 qui n'est pas prévu : vérifier non seulement que les arrêts existent, mais **qu'ils disent ce qu'on leur fait dire, et au bénéfice de quel guichet**.

### C9 — La section 9 interdit le chiffrage avant le banc d'essai, et V0 comme V1 chiffrent

Ligne 315, parmi les refus :

> — **Un chiffrage avant le banc d'essai**

Le banc d'essai est le livrable de V2 (ligne 276). Or, en amont :

- V0, agent Marché, ligne 247 : « qui achète, combien ils sont, ce qu'ils utilisent déjà, **ce qu'ils paient aujourd'hui** »
- V1, agent Cartographie, ligne 259 : « lesquels sont ouverts à un acteur de notre taille, **à quel coût**, avec quel délai »
- V1, agent Licences de contenu, ligne 262 : « **ce que coûte** le droit de collecter la presse, et auprès de qui »
- V1, livrable, ligne 266 : « la carte des guichets — guichet retenu par plateforme, **coût, délai**, pièces contractuelles »

Le refus de la ligne 315 interdit donc trois des agents de V0–V1 et le livrable même de V1. Soit « chiffrage » désigne autre chose — le chiffrage du produit, pas des coûts d'accès — et le mot n'est pas défini ; soit la section 9 interdit les deux premières vagues du programme.

### C10 — Trois endroits différents fixent l'étalon, et deux jeux d'épreuve concurrents jugent

Où se fixe l'étalon ? Trois réponses incompatibles.

Ligne 200, section 6 :

> **Seuils à fixer en V0** sur le jeu d'épreuve réel — les inventer maintenant serait de la fabulation.

Ligne 187, section 5, temps 3 — donc après les temps 1 et 2, qui sont le travail de V2 :

> **3** | **Fixer l'étalon** — les métriques à égaler et le **jeu d'épreuve figé** qui jugera | Le contrat de mesure, écrit, daté, versionné

Ligne 268, titre de V2 :

> ### V2 — Les organes de collecte **et leurs étalons**

V0 fixe les seuils, le temps 3 fixe l'étalon, V2 s'intitule « et leurs étalons ». Trois propriétaires pour une seule pièce, et aucune phrase qui dise lequel l'emporte.

Même désordre sur le jeu d'épreuve. Ligne 192 :

> Le jeu d'épreuve doit être guadeloupéen, réel, et figé avant toute construction … **Sa constitution est la première tâche du projet, en V0.**

Ligne 187, temps 3 : « **le** jeu d'épreuve figé **qui jugera** », à fixer par organe, après le temps 2. Il y a donc soit un corpus global gelé en V0, soit un corpus par organe gelé au temps 3 — et la clause de rejet du temps 3 (« Le jeu d'épreuve n'est pas figé avant la construction ») ne permet pas de trancher. La relance 2, ligne 232, demande alors :

> le jeu d'épreuve était-il figé avant la mesure, est-il guadeloupéen, et un tiers pourrait-il rejouer ta mesure à l'identique ?

Sans dire **lequel**. Un agent peut répondre oui en toute bonne foi sur un corpus qu'il a gelé lui-même au temps 3, et la mesure ne sera pas comparable à celle d'un autre organe. Le « chiffre opposable » de la ligne 192 n'est opposable qu'à l'intérieur d'un organe.

### C11 — Trois horizons de temps incompatibles, et une péremption que le document connaît sans la traiter

Ligne 35 : « **À réexaminer à trois ans** ». Ligne 299 : « le périmètre tenable en **quatre-vingt-dix jours** ». Ligne 329, nœud ouvert : « **Quel horizon** pour une première version utilisable par un vrai client guadeloupéen ? ». Trois échelles, aucune conversion, et le nœud qui les arbitre est le dernier d'une liste de cinq.

Le plus grave est la péremption, que le document énonce lui-même, ligne 133 :

> La connaissance d'un modèle porte une date de coupure, et **les conditions d'accès aux plateformes changent tous les six mois**.

Appliqué au document lui-même : le livrable de V1 est « la carte des guichets » (ligne 266). V3 se fait « **après le verdict de V1** » (ligne 280). V5 consomme tout (ligne 299). Six vagues « chacune s'arrête sur son livrable et attend validation » (ligne 240) prendront plus de six mois — rien dans le document ne dit le contraire, aucune durée n'est fixée. Donc, par la propre prémisse du document, **la carte des guichets sera périmée avant d'être consommée**, et les décisions d'architecture de V5 reposeront sur un état du monde révolu. Aucune clause de revalidation, aucune date d'expiration sur un livrable, aucun propriétaire du rafraîchissement. Le document a identifié l'horloge et ne l'a pas branchée sur son propre plan.

### C12 — La section 3 impose des disqualifications contre des seuils inconnus

Ligne 106 :

> Elles disqualifient directement des outils. **Tout agent qui les ignore voit son retour rejeté.**

Ligne 148 :

> — Jamais une évaluation d'outil **sans confrontation aux six exigences** guadeloupéennes

Mais deux des six exigences ne sont pas encore connues. Ligne 112 : « haute saison touristique **⏳ à confirmer** ». Ligne 114 : « Très petites entreprises en majorité **⏳ à confirmer en V0** », et sa colonne de disqualification : « Tout produit exigeant un administrateur, ou **dépassant le prix plafond local** » — un plafond nulle part chiffré, nulle part daté, nulle part attribué à une vague.

Un agent de V2 doit donc rejeter un outil pour dépassement d'un plafond qui n'existe pas, sous peine de voir son propre retour rejeté s'il ne le fait pas. Le verdict qu'il produira sera infalsifiable : personne ne pourra ni le confirmer ni le contredire. Et le gabarit, ligne 162, en fait une ligne de fiche obligatoire : « Une ligne par exigence — tenue, non tenue, **à vérifier** ». La troisième valeur, « à vérifier », est la seule honnête, et elle videra la colonne de son pouvoir disqualifiant — ce qui est exactement le faux vert de la ligne 133, cette fois institutionnalisé par le gabarit.

---

## 2. Les dépendances circulaires entre vagues

### D1 — V0 ↔ V1 : le jeu d'épreuve exige un accès que seule V1 autorise. C'est la tâche numéro un du projet.

Ligne 249, agent Jeu d'épreuve de V0 :

> **Jeu d'épreuve** — constituer le corpus figé : pages locales réelles, **avis réels multilingues**, requêtes types. Le versionner et le geler

Ligne 192 :

> **Sa constitution est la première tâche du projet, en V0.**

D'où viennent des « avis réels » ? Le document ne laisse que deux portes. Ligne 75 :

> — **Non débloqué** : les avis de plateformes. Ils relèvent du 5c, donc le **guichet 2, le mandat du titulaire, reste la seule voie** pour ce volet

Le 5c est écarté (ligne 50). Le guichet 2 exige un mandat, dont la licéité et les pièces sont le travail de V1 avec « **⏳ confirmation juriste obligatoire** » (ligne 261), et exige en outre un établissement client signé — ce qu'aucune vague ne produit.

**Donc la première tâche du projet est, dans le cadre du document, licitement impossible avant la vague suivante.** Et tout V2 en dépend : « mesurés contre l'étalon **sur le jeu d'épreuve de V0** » (ligne 274). Le cycle est : V0 → besoin d'avis → guichet 2 → V1 + client → mais V1 est après V0, et le client est après le produit. Aucune des six vagues ne coupe ce cycle.

Il existe une sortie, que le document ne voit pas : constituer le corpus V0 **uniquement sur le guichet 6** (presse par flux RSS, portails de données ouvertes, institutions — lignes 67 à 71), et reporter le corpus d'avis à une vague ultérieure, après le premier mandat signé. Cela découpe V0 en deux et change l'ordre des vagues. Le document ne propose rien de tel : il gèle un corpus unique qui contient les deux matières.

### D2 — V0 ↔ V1 : V0 rend des verdicts de guichet que seule V1 a le droit de rendre

Ligne 250, agent Qualification des sources de V0 :

> Pour chaque source locale recensée : son guichet, son degré s'il s'agit du 5, sa licence, ses conditions d'utilisation lues, et **le verdict retenu ou écarté**

Ligne 141 :

> — **Aucun choix de guichet ne se prend sur un cran D.** Le choix de la voie d'accès exige un B minimum, **confirmé par un juriste pour le guichet 2**

Le juriste est un agent de V1 (ligne 261). V0 doit donc rendre des verdicts de guichet, source par source, avant que l'instance qui valide les verdicts de guichet n'existe. Et le livrable de V0 s'appelle « **le registre des sources qualifiées** » (ligne 252), c'est-à-dire un registre de décisions non autorisées.

### D3 — V0 ↔ V2 : il faut connaître les mesures pour construire le corpus, et le corpus est gelé avant

C'est la dépendance que la consigne me demandait de chercher, et elle est réelle.

Ligne 205, étalon de l'organe Extraction :

> Part de texte propre … **taux d'erreur par champ** sur les pages locales difficiles

Ligne 206, organe Index :

> Latence de réponse … **pertinence sur requêtes figées** … coût au million de documents

Un taux d'erreur **par champ** exige une vérité de terrain annotée champ par champ : quels champs ? Le schéma des champs est une propriété de l'organe Extraction, dont la décomposition est le temps 4 du travail de V2 (ligne 188 : « quels composants produisent ce résultat »). Une « pertinence sur requêtes figées » exige un jugement de pertinence par requête et par document — une annotation de jugement, dont le barème dépend de ce que l'index est censé servir, c'est-à-dire de l'organe Rédaction, qui est en V4.

V0 doit donc geler un corpus dont le schéma d'annotation sera défini en V2 et en V4. Et il ne pourra pas le rouvrir, puisque le temps 3 rejette tout ce qui n'est pas gelé avant construction (ligne 187) et que la relance 2 exige que le gel précède la mesure (ligne 232). Deux issues : V0 devine le schéma — et le corpus sera mal annoté, les étalons porteront sur ce qu'on savait mesurer en V0, pas sur ce qui compte ; ou V2 rouvre le corpus — et l'opposabilité, seule justification du gel, disparaît. La boucle V0 → V2 → V0 n'est pas franchissable en l'état.

### D4 — V0 ↔ V3 : les plateformes d'avis sont recensées deux fois, et l'étalon est fixé avant le recensement

Ligne 248, V0 : « **Sources locales** — … et **plateformes d'avis réellement utilisées en Guadeloupe** ».
Ligne 284, V3 : « **Avis** — **recensement exhaustif des plateformes pertinentes en Guadeloupe** ».

Double propriété, sans partage de périmètre. Et ligne 200 impose de fixer les seuils de l'organe Avis en V0 — donc de fixer un seuil de « part des avis captés sur ceux réellement présents » (ligne 210) sur un ensemble de plateformes dont le recensement exhaustif est trois vagues plus loin. Le dénominateur de l'étalon est fixé avant que la liste des plateformes qui le composent ne soit connue.

### D5 — L'étalon de l'organe Avis ↔ le degré 5c : la mesure exige l'acte écarté

Déjà démontré en C1bis. Je le compte comme circularité à part entière parce qu'il est structurel et non résoluble par réordonnancement : pas de mesure sans client, pas de décision de construire sans mesure (ligne 140), pas de client sans produit, pas de produit sans décision de construire. Les quatre maillons sont dans le document ; aucune vague n'en casse un.

### D6 — Section 10 ↔ V0 : les nœuds « ouverts » sont en amont de la vague zéro

Ligne 326 :

> | **Licences de contenu** | Es-tu prêt à payer un droit de collecte pour la veille presse, ou renonce-t-on à la presse locale au départ ? | **Change le chiffrage et le périmètre de V0** |

Une décision présentée comme « attendue » change le périmètre de la **première** vague. Donc V0 ne peut pas commencer avant que la section 10 ne soit soldée — or la section 10 est la dernière du document, intitulée « décisions attendues », et deux de ses cinq nœuds (produit sous mandat, licences de contenu) sont des préalables à V0, pas des arbitrages de parcours. Et le nœud « Façades » (ligne 327) comme le nœud « Qui construit » (ligne 328) conditionnent le périmètre de V4 et de V5 sans qu'aucune vague ne soit chargée de les instruire. Il manque une vague V-1 : solder les nœuds.

**Bilan des cycles.** Six dépendances, dont trois bloquantes dès la première tâche du projet (D1, D2, D6). L'enchaînement V0 → V5 est présenté comme linéaire (« Une vague mal cadrée contamine les suivantes », ligne 240) alors qu'il est cyclique en trois endroits. L'ordre n'est pas juste : il manque une vague de solde des nœuds en amont, et il manque la séparation du corpus V0 en deux matières aux régimes d'accès opposés.

---

## 3. Les règles décoratives

Une règle décorative donne l'apparence du contrôle sans produire de contrôle. Elle est **pire** que l'absence de règle, parce qu'elle fait baisser la garde : on croit la question traitée.

### R1 — L'auto-déclaration du cran D

Ligne 135 : « tout agent déclare ses lignes D en tête de retour ». Ligne 234 : « **Toute affirmation issue de ta seule mémoire redescend en D** ».

Ces deux règles demandent à un modèle de langage de distinguer, dans sa propre production, ce qui vient de ses paramètres de ce qui vient d'un document lu. Cette introspection n'est pas fiable : le texte produit ne porte pas d'étiquette de provenance, et une affirmation de mémoire habillée d'une URL plausible est indiscernable d'une affirmation lue, **pour l'auteur comme pour le lecteur**. La frontière est poreuse, et le document ne fournit aucun contrôle extérieur : la relance 2 demande à l'agent de reclasser ses propres lignes.

Comparer les sous-règles de la ligne 234 est instructif :

> Toute ligne classée A sans sortie collée redescend en C. Tout étalon non rejouable redescend en B. Toute affirmation issue de ta seule mémoire redescend en D.

La première est **vérifiable mécaniquement** : la sortie est là ou elle n'est pas là. La deuxième est vérifiable par un tiers qui rejoue. La troisième n'est vérifiable par personne. Les deux premières sont des contrôles ; la troisième est une déclaration d'intention. Le document les met sur la même ligne et leur donne le même poids.

L'incitation est perverse. Ligne 135 : « Un retour qui n'en déclare aucune est **suspect et relancé** ». La conformité la moins chère est donc de déclarer quelques lignes D sur des points secondaires — des leurres qui prouvent la bonne foi — pendant que les affirmations de mémoire qui portent les décisions passent en B avec une URL trouvée après coup. Le dispositif récompense le théâtre et ne détecte pas la fraude. Et il y a un précédent dans le document même : les lignes 35, 37, 38 portent ⏳ D depuis la v3 ou la v4 et n'ont jamais été vérifiées ; la marque a servi de permis de circuler, pas de dette à solder.

**Et le barème a un vice de construction qui explique le verrou C1 : il est à une seule dimension.** Il mélange sur une même échelle ordinale **la provenance** (j'ai mesuré / j'ai lu un document primaire / je me souviens) et **la robustesse** (la mesure est-elle rejouable, l'échantillon suffisant, le fait daté). D'où des absurdités de rang : une mesure A faite sur un corpus minuscule et biaisé domine un texte de loi lu au Journal officiel classé B. Et la règle de décision de la ligne 140 porte sur la mauvaise dimension : elle exige un **niveau de provenance** (A-mesure) là où la question réelle est un **niveau de robustesse** (ce chiffre est-il assez solide pour engager des semaines de développement ?).

À titre de comparaison — **cran C**, résumé de moteur de recherche, sources primaires inaccessibles depuis cette session : la pratique du renseignement (code Admiralty, STANAG 2511 / AJP-2.1) note **séparément** la fiabilité de la source en A–F et la crédibilité de l'information en 1–6, précisément pour qu'une source sûre tenant un propos invraisemblable reste distinguable d'une source douteuse tenant un propos corroboré. Et GRADE sépare la **certitude de la preuve** de la **force de la recommandation**, en admettant explicitement qu'on puisse recommander fortement sur preuve de faible certitude dans des situations nommées. Je ne donne pas ces deux points comme établis. Mais le document attaqué ne fait ni l'un ni l'autre : un seul axe, et la décision collée sur l'axe de la provenance. C'est de là que vient le blocage C1.

**Correction, trois gestes.**
1. Deux axes. Provenance : *mesuré / observé / document primaire / secondaire / mémoire*. Robustesse : *rejouable par un tiers / échantillon et marge déclarés / daté avec péremption*. Un fait s'écrit « primaire · rejouable » ou « mesuré · non rejouable ».
2. La règle de décision porte sur l'axe robustesse, pas sur l'axe provenance. « On engage du développement sur un chiffre rejouable par un tiers, quelle que soit sa provenance » est applicable ; « il faut un A-mesure » ne l'est pas.
3. Pour le D : cesser de demander une introspection. La demander par l'**absence** d'artefact. Règle applicable : toute affirmation sans URL consultée dans la session **ni** sortie de commande collée est D d'office, sans que l'agent ait à dire d'où elle vient. Le critère devient mécanique, donc contrôlable par un tiers, donc réel.

### R2 — Le quota de trois candidats écartés (relance 1)

Ligne 222 :

> Qu'as-tu oublié — **cite trois candidats** que tu as écartés et dis pourquoi.

Vice de conception : un **cardinal fixe** demandé à un générateur de texte fluide. Nommer trois outils plausibles avec trois motifs plausibles coûte quelques secondes et ne peut être contredit par rien, puisque rien n'est demandé qui soit vérifiable — ni URL, ni date, ni requête. La forme est satisfaite ; l'information est nulle. Et la soupape, ligne 225, est placée **à la fin du bloc de trois questions** :

> Si tu n'as rien, écris « rien » et assume-le.

Elle se lit comme couvrant la troisième question, pas comme une permission, question par question, de rendre zéro. Un agent prudent produira trois noms. Le document a donc installé une incitation à l'invention dans le dispositif censé la combattre.

**Correction.** Remplacer le compte par la **trace**, et déplacer la charge de la preuve sur un artefact :
- « Colle ton journal de recherche : les requêtes exactes, les dates, le nombre de résultats, le filtre appliqué. »
- « Pour chaque candidat écarté : son URL, et **laquelle des six exigences de la section 3** le disqualifie, citée dans ses mots. »
- « Zéro candidat écarté avec un journal complet est une réponse valable. Trois noms sans URL est un retour rejeté. »

Un nom inventé échoue alors sur un contrôle qui coûte dix secondes. Et la question cesse de mesurer la docilité pour mesurer le travail.

### R3 — La question « où perd-il de l'argent aujourd'hui » (relance 1)

Ligne 224 :

> Qu'est-ce qui rendrait ce produit plus profitable — nomme **l'endroit exact où il perd de l'argent aujourd'hui**, et le geste qui le corrige.

La présupposition est fausse. Il n'y a pas de produit : la ligne 328 demande encore « Qui construit — **toi seul avec moi ? une équipe ?** », la ligne 329 demande « quel horizon pour une première version utilisable par un **vrai client** ». Aucun client, aucun revenu, aucun compte d'exploitation n'existe. « L'endroit exact où il perd de l'argent aujourd'hui » n'a pas de référent.

Une question à présupposition fausse, posée en obligation, ne peut recevoir qu'une réponse inventée. C'est un **générateur d'hallucination installé dans la partie obligatoire du protocole**, au cœur du document dont la raison d'être affichée est d'empêcher le faux vert (ligne 133). C'est la règle la plus activement nuisible des deux relances : les autres sont inopérantes, celle-là produit du faux.

**Correction.** Poser la question sur ce qui existe — le plan — et non sur ce qui n'existe pas — le produit. « Nomme l'endroit où **ce plan** dépense sans acheter de preuve : quelle vague coûte le plus pour la décision la plus faible, et que supprimerais-tu sans perdre une décision ? » La question reste mordante, devient répondable, et porte sur un objet dont l'agent a la matière sous les yeux.

### R4 — La relance automatique auto-administrée

Ligne 217 :

> Parties avec chaque agent en fin de recherche, **sans intervention**.

L'agent qui a écrit les lignes répond aux relances sur ses propres lignes, dans le même contexte, avec sous les yeux son propre texte et tout intérêt à conserver ses A. Un contrôle dont le contrôleur est le contrôlé n'est pas un contrôle. Et le document en est conscient ailleurs, puisque la relance 2 exige du jeu d'épreuve exactement ce qu'elle ne s'impose pas, ligne 232 :

> **un tiers pourrait-il rejouer ta mesure à l'identique ?**

Le document exige la vérifiabilité par un tiers pour les mesures et n'en prévoit aucune pour la conformité à sa propre doctrine. Il n'y a nulle part un second lecteur, un audit par échantillon, une relecture indépendante. La présente critique en est une — mais le document ne l'institue pas, elle vient d'ailleurs.

**Correction, une ligne à ajouter en section 7.** « Un retour sur N est relu par un lecteur qui ne l'a pas produit, avec pour seul mandat de le casser. L'**écart entre l'autoclassement et le classement de l'audit** est lui-même un chiffre suivi. » C'est la seule mesure qui dirait si le barème fonctionne. En son absence, personne ne saura jamais si la doctrine de preuve a amélioré quoi que ce soit.

### R5 — Le marqueur ⏳, quatre sens pour un signe

17 occurrences dans 329 lignes (comptage mécanique, sortie en § 6), pour quatre choses différentes :
- un fait non daté : ligne 150, « Tout fait porte sa date, **ou la marque ⏳ à confirmer** »
- un fait à confirmer sur le terrain : lignes 112, 114
- une mémoire à vérifier sur source primaire : ligne 81
- un avenir qui n'a pas eu lieu : ligne 175, « marqué ⏳ **puisque non advenu** »

Un marqueur qui veut dire à la fois « non daté », « non confirmé », « non vérifié » et « pas encore existant » ne marque rien. Toute affirmation peut le porter et continuer de circuler — et c'est ce qui s'est produit : les lignes 35, 37, 38 portent ⏳ D à travers les révisions sans jamais devenir B, tout en portant des verdicts de guichet.

**Correction.** Un signe, un sens, et **une date de péremption attachée** : ⏳ suivi de la date à laquelle l'affirmation doit être passée en B ou supprimée. Sans échéance, le marqueur est un permis de séjour indéfini pour une affirmation non vérifiée, c'est-à-dire l'inverse de son intention.

### R6 — « Chiffre opposable » : le gel garantit la reproductibilité, pas la validité

Ligne 192 :

> Sans lui, « on fait aussi bien » est une opinion. **Avec lui, c'est un chiffre opposable.**

Un corpus unique, gelé, sans portion réservée, sans taille d'échantillon, sans marge d'erreur, et qui sert à la fois à construire (temps 5) et à juger (temps 6) garantit le contraire de ce qui est annoncé : tout ce qui est bâti après le temps 3 est ajusté sur le seul corpus qui le juge. Le gel rend la mesure **reproductible**. Il ne la rend pas **valide**. Le mot « opposable » fait passer la validité en contrebande derrière la reproductibilité — et personne ne le verra, puisque le chiffre sera, lui, parfaitement reproductible.

À quoi s'ajoute que la fraîcheur est elle-même une métrique (ligne 204, « fraîcheur en heures entre publication et captation ») : un corpus gelé vieillit, et un étalon de fraîcheur mesuré sur un corpus de l'an dernier ne veut rien dire.

**Correction.** Couper le corpus en V0 : une part de développement, publique à l'équipe, et une part de jugement **scellée**, ouverte au temps 6 seulement. Déclarer n et la marge. Dater le corpus et fixer sa durée de validité.

### R7 — Les nombres sans justification, dans un document qui les interdit

Ligne 146 : « **trois briques** tenues valent quinze listées ». Ligne 274 : « **trois candidats** tenus au maximum ». Ligne 222 : « cite **trois** candidats que tu as écartés ».

Trois est partout, et nulle part justifié. Or ligne 200 : « les inventer maintenant serait de la **fabulation** ». La règle contre les nombres inventés ne s'applique pas aux nombres de la règle. Mineur, mais c'est la même faute, et elle discrédite la plus importante : un plafond de trois candidats fixé avant de savoir combien il en existe peut écarter le seul qui tenait.

### R8 — Le « Cran de preuve » apposé à un « Verdict »

Déjà signalé en § 0. Le gabarit (lignes 163 et 166) demande sur une même fiche un **Verdict** — adopter, adapter, reconstruire, renoncer — et un **Cran de preuve**. Un verdict est un jugement ; le barème ne classe que des faits. En pratique, le cran du fait le plus fort de la fiche sera lu comme le cran du verdict. Un verdict « reconstruire » porté par une fiche contenant un A-usage passera pour « décidé en A », alors que la décision, elle, n'a été ni mesurée ni vérifiée : elle a été raisonnée. C'est la forme la plus discrète de faux vert, et elle est **inscrite dans le gabarit**.

---

## 4. Ce qui manque — du plus grave au moins grave

### M1 — Aucune gouvernance du désaccord entre Laurent et l'agent. C'est le manque le plus grave.

Le document donne à l'agent un droit de veto : « Tout agent qui les ignore voit son retour rejeté » (ligne 106), « il tombe » (ligne 139), « Ce que ce prompt refuse de produire » (ligne 305). Il donne à Laurent toutes les décisions (section 10). Et il ne dit **nulle part** ce qui se passe quand les deux s'opposent : quand la règle dit « pas de A-mesure, donc pas de décision » et que l'homme dit « on construit quand même ».

Or ce cas n'est pas un cas d'école : par C1, c'est le cas **normal**. Les deux issues sans procédure sont également mauvaises. Soit la règle est tenue et rien n'est construit. Soit elle est enfreinte une fois, en silence, pour avancer — et le barème entier perd sa force au premier manquement, parce qu'une doctrine de preuve sans procédure d'exception documentée est une doctrine qu'on abandonne sans le dire. C'est le manque le plus grave parce que c'est lui qui décidera réellement de l'issue, et pas les six vagues.

**Ce qu'il faut ajouter, et c'est court.** Un cran **E — décision assumée sous incertitude**, avec quatre champs obligatoires : qui décide, ce qui n'était pas su, **ce qui la falsifierait**, et la date de réexamen. Il transforme le blocage en risque tracé, il rend l'exception visible au lieu de clandestine, et il dissout le verrou C1 sans affaiblir le barème — au contraire : une exception comptée est une exception qui se compte.

### M2 — Aucun premier client, aucune vague commerciale. Et c'est un prérequis technique, pas un objectif.

Toute la stratégie repose sur le guichet 2 (lignes 36, 75, 100), le guichet 2 repose sur un mandat, un mandat repose sur un client signé. Et le seul actif revendiqué est une relation, ligne 98 :

> En Guadeloupe, le client nous connaît, ou connaît quelqu'un qui nous connaît. Il confie ses accès parce que nous sommes son prestataire local … **La proximité est la clé du guichet 2.** Aucun concurrent mondial ne peut l'ouvrir.

Cet actif n'est acquis par aucune des six vagues. V0 à V5 sont six vagues de recherche ; aucune ne va voir un hôtelier. Et par D1 et D5, le mandat n'est pas seulement l'objectif commercial : il est le **seul moyen licite** d'obtenir les avis réels du jeu d'épreuve de V0 et la vérité de terrain de l'étalon Avis. L'acte commercial est le premier prérequis technique du programme, et il est absent de la séquence.

### M3 — Aucune définition du produit minimal

Nulle part n'est écrit ce que le plus petit client guadeloupéen paierait. Le périmètre est renvoyé à la dernière vague, ligne 299 : « le périmètre tenable en quatre-vingt-dix jours » — c'est-à-dire après toute la dépense de recherche. Entre-temps, huit organes sont ouverts simultanément (section 6), et tous les huit portent un étalon, donc tous les huit doivent être mesurés avant que quoi que ce soit ne sorte. Le document n'autorise aucun chemin étroit.

### M4 — Aucun critère d'arrêt, ni par vague ni pour le projet

Ligne 240 :

> Chaque vague s'arrête sur son livrable et **attend validation**.

Validation par qui, contre quel test d'acceptation, dans quel délai, et que se passe-t-il en cas de refus ? Rien. Pas de budget par vague, pas de durée maximale, pas de critère d'abandon — par exemple : « si le juriste de V1 conclut que le mandat n'est pas praticable, alors … ». Le nœud « Budget temps » (ligne 329) est adressé à Laurent et sa réponse n'est consommée que par « l'ordre de construction de V5 ». Un programme sans critère d'arrêt consomme tout le temps disponible, et le document n'a aucun mécanisme pour s'en apercevoir.

### M5 — Aucun jalon de revenu, aucun prix, un seul côté du grand livre instrumenté

Le gabarit exige de chaque organe « Coût réel à l'échelle visée — serveur, quotas, licence de contenu, maintenance humaine » (ligne 165). Côté recettes : rien, sauf un « prix plafond local » inconnu (ligne 114) et « ce qu'ils paient aujourd'hui » dans V0 (ligne 247). Pas de prix cible, pas d'économie unitaire, pas de seuil de rentabilité, pas de date de première facture. Une doctrine qui mesure les coûts avec rigueur et les recettes pas du tout produira une perte parfaitement documentée.

### M6 — La péremption n'est pas gouvernée (et non : la maintenance n'est pas absente)

Il m'a été suggéré qu'aucune mention du coût de maintenance ne figurait. **C'est faux, et je le corrige** : la ligne 165 inscrit « maintenance humaine » dans le coût réel de chaque organe. Le manque est ailleurs, et il est plus grave : aucune obligation de **revalidation** des livrables. Le document sait que les conditions d'accès changent tous les six mois (ligne 133) et ne met de date d'expiration ni sur la carte des guichets de V1, ni sur les étalons de V2, ni sur le registre des sources de V0 — alors que V3 et V5 les consomment plus tard (C11). Il manque, par livrable : une date de validité, un propriétaire du rafraîchissement, et un coût de rafraîchissement annuel distinct du coût de construction.

### M7 — Le jeu d'épreuve est lui-même un traitement de données personnelles, non traité

V0 gèle « avis réels multilingues » (ligne 249). Le document sait que le RGPD s'applique, ligne 91 :

> Il expose à la responsabilité contractuelle, au droit sui generis des bases, **au RGPD dès qu'un avis porte un prénom**

Et il place l'examen du RGPD en V1 (ligne 264), **après** que V0 a constitué et gelé le corpus. Il manque : la base légale du corpus, sa durée de conservation, sa minimisation, et une procédure d'effacement — qui est en tension directe avec un corpus **gelé** et versionné, puisqu'un corpus figé ne peut pas honorer une demande de suppression sans cesser d'être figé, c'est-à-dire sans détruire l'opposabilité de toutes les mesures déjà faites. La première tâche du projet crée le problème de conformité que la vague suivante est censée prévenir, et le conflit gel / effacement n'est nulle part posé.

### M8 — Aucune capacité, donc aucune conversion des coûts en dates

Temps 5, ligne 189 : le coût du manquant « **en jours** ». Section 10, ligne 328 : « Reconstruire un organe se compte **en semaines** ». Jours contre semaines, et « Qui construit » reste ouvert. Sans capacité déclarée — combien de personnes, combien de jours par semaine — aucun coût en jours ne devient une date, et « le périmètre tenable en quatre-vingt-dix jours » (ligne 299) est incalculable.

### M9 — Pas de registre de risques, pas de plan de repli par organe

Les seules alternatives admises sont les trois issues du temps 6 (ligne 194). Rien pour « le guichet se ferme », alors que le document nomme le scénario — ligne 90, « Il casse le jour où une plateforme modifie ses défenses techniques, sans préavis et sans recours » — uniquement pour disqualifier le 5c, jamais pour examiner la fragilité propre du guichet 2 : un client peut révoquer un mandat, une plateforme peut interdire l'accès délégué dans les conditions de son extranet. Le risque central du modèle retenu n'est pas inscrit.

### M10 — Aucune taille d'échantillon, aucune marge

Déjà en R6. Les métriques de la section 6 sont des taux et des parts sans n, sans intervalle de confiance, sans part réservée. Un écart de trois points entre notre composant et l'étalon sera traité comme un fait, sans qu'on sache s'il est distinguable du bruit.

**Avertissement d'honnêteté sur cette liste.** Tout ce qui précède sont des manques **de ce document**. Le dépôt ne contient qu'un seul fichier : je n'ai pas pu vérifier s'il existe ailleurs un plan commercial, un budget ou un carnet de clients qui combleraient M2 et M5. Si cela existe, il manque alors seulement le lien — ce qui, pour un document qui s'intitule « prompt de lancement » et prétend cadrer tout le travail des agents, reste un défaut, mais un défaut moins grave.

---

## 5. Verdict — instrument de travail, ou armure

**Armure.** Et une armure dont la visière est soudée.

Le test est simple, et il ne dépend d'aucune appréciation de ma part : appliqué à la lettre, ce document **ne peut produire aucune décision de construire**. La démonstration tient en trois lignes citées — le A-mesure exige des chiffres « des deux côtés » (ligne 127), la décision de reconstruire exige un A-mesure (ligne 140), les chiffres des deux côtés n'existent qu'au temps 6 (ligne 190), après la construction. Un dispositif dont la condition d'entrée est sa propre sortie ne se franchit pas : il se contourne ou il arrête. Et il ne prévoit pas son contournement (M1).

À quoi s'ajoutent deux blocages indépendants, l'un et l'autre suffisants. La première tâche du projet — le corpus d'avis réels de V0, ligne 249 — est licitement inatteignable avant V1 et avant un client qu'aucune vague n'acquiert (D1, M2). Et l'étalon de l'organe dont le document dit « c'est ce que le client paie » (ligne 210) exige un dénombrement qui passe soit par le mandat, soit par l'acte écarté (C1bis, D5). Trois verrous, trois endroits, aucune clé dans le document.

Le reste est de l'armure au sens strict : des dispositifs qui protègent celui qui les porte contre le reproche, sans augmenter sa portance. Le cran D auto-déclaré ne détecte rien que son propre déclarant veuille cacher (R1). La relance 2 fait relire l'agent par l'agent (R4). La relance 1 demande trois noms, donc produira trois noms (R2), et demande où un produit inexistant perd de l'argent, donc produira une fabulation (R3) — dans le document dont la raison d'être est d'empêcher la fabulation. Le ⏳ excuse tout et n'engage à rien (R5). Et « chiffre opposable » (ligne 192) nomme comme validité ce qui n'est que reproductibilité (R6). Chacune de ces règles donne le sentiment que la question est traitée. Aucune ne la traite. C'est précisément ce que le document lui-même appelle du faux vert (ligne 133) — appliqué non à un fait, mais à sa propre méthode.

Dernière charge, et c'est celle qui me décide. La v4 a corrigé « cinq » en « six » à deux endroits et l'a laissé au titre de la section 2.2 (C2, prouvé par le diff git) ; et « sept organes » figure au gabarit depuis la v3 alors que la section 6 en compte huit depuis la v3 (C4, prouvé par comptage). Un document qui institue neuf refus de produire (section 9) et deux relances obligatoires n'a pas appliqué à lui-même le contrôle le plus élémentaire qu'il impose aux autres : compter les lignes de son propre tableau. **Une armure qu'on n'inspecte pas est un cercueil qui marche.**

**Ce qui n'est pas de l'armure, et qu'il faut garder.** Trois pièces travaillent vraiment, et je le dis pour que la réparation ne les emporte pas. La typologie des six guichets avec les trois degrés du 5 (2.2 à 2.4) est un classificateur net, opératoire, et son exigence de qualifier **source par source et non plateforme par plateforme** (ligne 44) est juste et rare. Le gabarit de fiche-organe (4.4) est un bon formulaire : il force à nommer un produit, une licence lue, un coût à l'échelle. Et l'enchaînement des six temps, débarrassé de la règle 4.2, est une discipline utile contre le « on fera aussi bien ».

**Quatre corrections, et le document redevient un instrument.** Toutes petites, toutes dans le texte.
1. **Cran E — décision assumée sous incertitude**, avec propriétaire, falsifieur et date de réexamen ; et A-mesure redéfini à un seul côté pour le modèle repéré. Lève C1 et M1.
2. **Deux vagues insérées en amont** : V-1, solder les cinq nœuds de la section 10 (ils conditionnent V0, D6) ; et V0bis, **un mandat signé avec un établissement**, qui est le seul moyen licite d'obtenir la matière de V0 et la vérité de terrain de l'étalon Avis. Lève D1, D5, M2.
3. **Barème à deux axes** — provenance × robustesse — et règle de décision portée sur la robustesse. Lève R1 et le vice de rang.
4. **Relances réécrites** : la trace au lieu du quota, la question posée sur le plan et non sur un produit inexistant, et un retour sur N relu par quelqu'un qui ne l'a pas écrit. Lève R2, R3, R4.

En l'état, non : ce n'est pas un instrument de travail. C'est un document qui a confondu la rigueur avec le nombre d'interdits, et qui a atteint le point où l'interdit le plus strict protège surtout de l'obligation de produire. Avec ces quatre corrections, il redevient ce qu'il voulait être.

---

## 6. Les deux relances, appliquées à moi-même

### RELANCE 1 — anti-oubli

**Qu'as-tu oublié — trois candidats écartés et pourquoi.**

Je nomme des objets, et je dis ce que l'écartement m'a coûté.

1. **L'archéologie complète des versions v1 → v4.** Écartée après l'avoir commencée. Je ne l'ai menée que sur deux points (le « cinq guichets » et le comptage des organes), parce que c'était cheap et que ça payait immédiatement — et ça a payé : c'est devenu la preuve que la passe de révision n'est pas faite (C2). Je n'ai pas remonté les quatre commits ligne à ligne. Ce que j'y aurais trouvé : quelles contradictions sont nées de quelle révision, donc lesquelles sont des oublis de relecture — réparables en dix minutes — et lesquelles sont des désaccords de fond jamais tranchés. Cette distinction aurait classé mes contradictions par coût de réparation, ce que ma critique ne fait pas. C'est le manque le plus réel de ce travail.
2. **La réécriture complète du barème en tableau.** Écartée volontairement. J'en ai donné les deux axes et la règle de décision (R1), pas la grille finie. Motif : une critique qui réécrit sa cible cesse d'être une critique et devient une v5 concurrente, que personne n'a demandée et que Laurent n'a pas arbitrée. Les quatre corrections du § 5 sont donc des gestes, pas des livrables. Si on en veut un, c'est un autre travail, et il doit être commandé.
3. **La vérification des arrêts Ryanair et Meltwater sur source primaire.** Écartée par impossibilité, pas par choix — voir ci-dessous. Conséquence : ma charge C8bis contre la section 2.5 reste en D, donc par la doctrine attaquée elle-même, elle n'est qu'une piste de recherche. Je l'assume comme telle et je ne la compte pas dans les contradictions acquises.

**Que n'as-tu pas vu — ce que tu n'as pas pu vérifier et ce qui t'a manqué.**

- **Les deux arrêts.** `en.wikipedia.org` et `book.gradepro.org` sont rendus par le proxy avec `EGRESS_BLOCKED` ; `gradeworkinggroup.org` et `kravensecurity.com` avec `CONNECT tunnel failed, response 403`. Le réseau sortant est quasi fermé dans cette session. Constat qui dépasse ma critique et qui vaut pour le projet : **la ligne 81 du document — « Vérification sur source primaire obligatoire en V1 » — n'est peut-être pas exécutable dans cet environnement.** Si les agents de V1 travaillent derrière le même proxy, la doctrine exige d'eux un cran B qu'ils ne pourront pas atteindre, et ils rendront du D marqué B ou ils tomberont (ligne 139). À vérifier avant de lancer V1. Ce qui m'a manqué : une liste de domaines autorisés, ou un MCP d'accès documentaire.
- **Le terrain guadeloupéen.** Je n'ai aucun moyen de savoir si le guichet 6 porte réellement le corpus que la ligne 74 espère (« une part probablement importante … ⏳ proportion à établir »). Donc ma sortie de secours pour D1 — bâtir V0 sur le guichet 6 seul — est une hypothèse, pas une solution vérifiée. Si les portails guadeloupéens sont pauvres, elle tombe et D1 reste entier.
- **Le hors-document.** Le dépôt ne contient que ce fichier (`ls -la` : un seul `.md`). Je ne sais pas s'il existe ailleurs un plan commercial, un budget, un carnet de clients. Mes manques M2 et M5 sont donc des manques **du document**, et je l'ai écrit en tête de la liste. Ce qui m'a manqué : savoir si Laurent a déjà des clients. Si oui, M2 change de nature — il devient un défaut de liaison, pas un trou.
- **L'intention d'usage.** Je ne sais pas si ce document est un cadre contraignant pour des agents automatiques ou un manifeste que Laurent lit lui-même avant de décider. Ma critique suppose le premier, parce que le document le dit (« Parties avec chaque agent … sans intervention », ligne 217). Si c'est le second, la gravité de R1 à R4 baisse d'un cran : une règle décorative lue par un humain lucide reste un rappel utile. Le verrou C1 et la circularité D1, eux, ne bougent pas.

**Qu'est-ce qui rendrait ce produit plus profitable — l'endroit exact où il perd de l'argent, et le geste qui le corrige.**

Je refuse la question telle qu'elle est posée, et c'est le constat R3 appliqué à moi : **le produit ne perd pas d'argent aujourd'hui, parce qu'il n'y a pas de produit.** Toute réponse à la question littérale serait inventée. Je réponds à la version répondable.

**Où le plan perd de l'argent :** six vagues de recherche, huit organes, chacun à instrumenter contre un modèle propriétaire, avant le premier euro facturé. Et l'instrumentation du temps 2 (ligne 186, « par version d'essai ou compte de démonstration ») suppose des comptes d'essai que des éditeurs B2B refusent à cette taille ou n'accordent qu'au terme d'un cycle de vente. On va donc payer en semaines des démonstrations qu'on n'obtiendra pas, pour produire un A-mesure qui, de toute façon, ne débloque rien (C1).

**Le geste qui corrige, un seul, et il inverse l'ordre :** signer **un** mandat avec **un** hôtelier guadeloupéen pour un service rendu **à la main** — quelqu'un lit les avis, rédige les réponses, facture au mois. Aucune ligne de code. Ce geste paie trois choses que les six vagues ne peuvent pas acheter. Il encaisse, donc il finance la suite. Il fournit, licitement et gratuitement, le corpus d'avis réels de V0 (D1) et la vérité de terrain du dénominateur de l'étalon Avis (D5) — les deux impasses dures du document. Et il mesure, sans instrumenter aucun modèle propriétaire, l'étalon qui compte vraiment : combien d'heures coûte une réponse à la main, puisque c'est **ça** que l'automatisation devra battre. Le vrai étalon n'est pas l'outil du concurrent : c'est le coût humain du service rendu. Le document ne l'a pas vu parce qu'il cherche son modèle chez les éditeurs (ligne 185, « le meilleur existant, propriétaire inclus ») alors que le modèle à battre est le travail manuel du premier client.

Le premier client n'est pas le résultat des six vagues. C'est l'instrument de la vague zéro.

### RELANCE 2 — preuve, étalon et guichet

Ligne par ligne. Ce que j'ai vérifié, avec quoi, quel passage, quelle date. Ce que j'ai obtenu, cité et non résumé. Ce que j'ai validé moi-même et ce que j'ai recopié. Reclassement.

**Sorties collées, comme exigé ligne 230.** Commandes passées le 2 octobre 2026 dans `/home/user/moteurs-et-outils`, environnement Linux 6.18.44, shell bash.

```
$ wc -l 00-PROMPT-DE-LANCEMENT.md
329 00-PROMPT-DE-LANCEMENT.md

$ grep -o '⏳' 00-PROMPT-DE-LANCEMENT.md | wc -l
17

$ sed -n '202,212p' 00-PROMPT-DE-LANCEMENT.md | grep -c '^| \*\*'
8

$ grep -n 'cinq guichet\|des six\|des sept' 00-PROMPT-DE-LANCEMENT.md
29:### 2.2 L'obstacle d'accès — un péage à cinq guichets
156:| Organe visé | Lequel des sept de la section 6 |
158:| **Guichet emprunté par ce modèle** | Lequel des six, degré précisé s'il s'agit du 5, et à quel coût — ou « inconnu », jamais une supposition |

$ git show 4c0858c:00-PROMPT-DE-LANCEMENT.md | sed -n '/## 6\./,/## 7\./p' | grep -c '^| \*\*'
8

$ git diff 4c0858c 8070f2c -- 00-PROMPT-DE-LANCEMENT.md | grep -E '^[+-].*(péage|Lequel des)' -i
-— v3 : le mur juridique n'est pas un mur mais **un péage à cinq guichets** … ajout du cran de preuve D
+— v3 : le mur juridique n'est pas un mur mais **un péage à guichets** … ajout du cran de preuve D
-| **Guichet emprunté par ce modèle** | Lequel des cinq, et à quel coût — ou « inconnu », jamais une supposition |
+| **Guichet emprunté par ce modèle** | Lequel des six, degré précisé s'il s'agit du 5, et à quel coût — ou « inconnu », jamais une supposition |

$ curl -sS -o /dev/null -w "%{http_code}\n" https://www.gradeworkinggroup.org/
curl: (56) CONNECT tunnel failed, response 403
```

| Ligne de ma critique | Vérifié avec quoi | Passage du document | Validé par moi / recopié | Cran |
|---|---|---|---|---|
| **C1** verrou du A-mesure | Lecture du document, confrontation de trois passages | l. 127, l. 140, l. 189-190 | Validé : le raisonnement est le mien, les trois citations sont vérifiées au fichier | **B** |
| **C1bis** temps 2 impraticable, étalon Avis non mesurable | Lecture | l. 186, l. 35, l. 210, l. 50, l. 75 | Validé. Aucune source externe n'intervient | **B** |
| **C2** cinq guichets contre six | `grep -n`, `git diff 4c0858c 8070f2c`, sorties collées ci-dessus | l. 29, l. 31, l. 40, l. 158 | Validé par commande, pas recopié | **A-usage** |
| **C3** le degré 5a vide / exigé | Lecture | l. 48, l. 313 | Validé | **B** |
| **C3bis** 5b non qualifiable en B ; « non des promesses » réfuté | Lecture | l. 49, l. 141, l. 129, l. 52, l. 57 | Validé | **B** |
| **C4** sept organes contre huit, depuis v3 | `sed … | grep -c` → 8 ; `git show 4c0858c … | grep -c` → 8 | l. 156, l. 202-211 | Validé par commande | **A-usage** |
| **C5** six temps inapplicables à la garde des accès | Lecture | l. 181, l. 185-186, l. 211, l. 200 | Validé | **B** |
| **C6** mandat tranché et redemandé | Lecture | l. 100, l. 325, l. 36, l. 285, l. 211 | Validé | **B** |
| **C6bis** deux voies principales | Lecture | l. 36, l. 40, l. 74, l. 100 | Validé. La part d'arbitrage (« incohérence d'arbitrage ») est mon jugement, non un fait | **B** pour les citations, jugement pour la conclusion |
| **C7** la doctrine roule sur du D | `grep -n 'cran D\|⏳ D'`, sortie relevée | l. 131, l. 141, l. 35, l. 37, l. 38, l. 67, l. 68, l. 71, l. 81, l. 135 | Validé par commande + lecture | **A-usage** pour le relevé, **B** pour la contradiction |
| **C8** vide préféré et puni ; « il tombe » indéfini | Lecture | l. 317, l. 139 | Validé | **B** |
| **C8bis** Meltwater mal employé | **Rien.** Mémoire du modèle. Fetch bloqué (sortie collée) | l. 79, l. 85, l. 38 | **Recopié de ma mémoire.** Non validé | **D** |
| **C9** chiffrage interdit et exigé | Lecture | l. 315, l. 247, l. 259, l. 262, l. 266, l. 276 | Validé | **B** |
| **C10** trois propriétaires de l'étalon, deux jeux d'épreuve | Lecture | l. 200, l. 187, l. 268, l. 192, l. 232 | Validé | **B** |
| **C11** horizons incompatibles, péremption non branchée | Lecture | l. 35, l. 299, l. 329, l. 133, l. 240, l. 266, l. 280 | Validé pour les citations. Que six vagues dépassent six mois est une **inférence** : aucune durée n'est écrite | **B** pour les citations, inférence déclarée pour la conclusion |
| **C12** seuils inconnus et disqualifiants | Lecture | l. 106, l. 148, l. 112, l. 114, l. 162 | Validé | **B** |
| **D1** V0 ↔ V1, corpus d'avis | Lecture | l. 249, l. 192, l. 75, l. 50, l. 261, l. 274 | Validé. Ma sortie de secours (guichet 6 seul) est une **hypothèse non vérifiée** | **B** pour le cycle, **D** pour la faisabilité de la sortie |
| **D2** V0 rend des verdicts non autorisés | Lecture | l. 250, l. 141, l. 261, l. 252 | Validé | **B** |
| **D3** V0 ↔ V2, schéma d'annotation | Lecture | l. 205, l. 206, l. 188, l. 187, l. 232 | Validé. Que « taux d'erreur par champ » exige une annotation par champ est une **inférence méthodologique** de ma part, solide mais non citée du document | **B** |
| **D4** V0 ↔ V3, double recensement | Lecture | l. 248, l. 284, l. 200, l. 210 | Validé | **B** |
| **D5** étalon Avis ↔ 5c | Lecture | l. 210, l. 50, l. 75, l. 140 | Validé | **B** |
| **D6** section 10 en amont de V0 | Lecture | l. 326, l. 327, l. 328, l. 329 | Validé | **B** |
| **R1** cran D décoratif, barème à un axe | Lecture pour le document ; **résumé de moteur de recherche** pour Admiralty et GRADE, fetch des sources primaires bloqué | l. 135, l. 234, l. 131 | Le raisonnement sur le document : validé, **B**. Admiralty / GRADE : **recopié d'un résumé**, sources primaires inaccessibles | **B** pour l'attaque, **C** pour la comparaison externe |
| **R2** quota de trois | Lecture | l. 222, l. 225 | Validé. Que le modèle produira trois noms est une **prédiction** sur le comportement d'un modèle, non un fait mesuré | **B** pour le vice de forme, **D** pour la prédiction de comportement |
| **R3** question à présupposition fausse | Lecture | l. 224, l. 328, l. 329 | Validé : l'absence de produit est établie par le document lui-même | **B** |
| **R4** relance auto-administrée | Lecture | l. 217, l. 232 | Validé | **B** |
| **R5** ⏳ polysémique, 17 occurrences | `grep -o '⏳' | wc -l` → 17, sortie collée | l. 150, l. 112, l. 114, l. 81, l. 175 | Validé par commande | **A-usage** |
| **R6** gel ≠ validité | Lecture | l. 192, l. 187, l. 204 | L'attaque sur le mot « opposable » : validée au texte, **B**. Que l'ajustement sur corpus unique dégrade la validité est une **connaissance méthodologique générale** non vérifiée en session | **B** pour la citation, **D** pour le principe invoqué |
| **R7** nombres non justifiés | Lecture | l. 146, l. 274, l. 222, l. 200 | Validé | **B** |
| **R8** cran apposé à un verdict | Lecture | l. 163, l. 166 | Validé | **B** |
| **M1 à M10** | Lecture exhaustive des 329 lignes, recherche d'absence | absence constatée ; M6 corrigé par l. 165 | Validé, avec la réserve écrite : absence **dans ce document**, le dépôt ne contenant qu'un fichier (`ls -la`) | **B** (constat d'absence sur source primaire complète) |
| **Hiérarchie de gravité des manques** | — | — | **Mon jugement.** Aucun cran ne s'applique | jugement |
| **Verdict « armure »** | — | — | **Mon jugement**, bâti sur C1, D1, D5 et R1-R4 | jugement, non classable au barème — voir § 0 |

**Mon étalon est-il opposable ?** Partiellement, et je le dis net. Pour tout ce qui concerne le document, oui : le jeu d'épreuve est un fichier unique, versionné en git, figé au commit `8070f2c` avant ma lecture, et un tiers peut rejouer chacune de mes commandes et retrouver chaque numéro de ligne. C'est rejouable à l'identique. Pour la comparaison aux pratiques établies, non : mes sources sont des résumés, le fetch primaire est bloqué, un tiers obtiendra peut-être autre chose. Et pour mes jugements — la hiérarchie des manques, le verdict — il n'y a pas d'étalon du tout, et le barème du document n'en prévoit pas, ce qui est l'un de mes constats.

**Par quel guichet j'accède à ma matière.** Guichet 6, accès ouvert déclaré, degré sans objet : un fichier du système de fichiers de Laurent, ouvert en lecture, non modifié. Pour les deux résumés externes : moteur de recherche public, usage de citation, aucun contournement — et les sources primaires que j'aurais voulu lire me sont refusées par le proxy, ce que j'ai déclaré plutôt que de prétendre les avoir lues.

**Reclassement net.** 21 lignes en B. 4 en A-usage. 1 en C. 4 en D, dont une entière (C8bis) et trois partielles (D1-sortie, R2-prédiction, R6-principe). 2 jugements non classables. **Aucune ligne en A-mesure** : je n'ai mesuré ce document contre aucun étalon, parce qu'il n'en existe pas pour juger une doctrine — ce qui est, soit dit en passant, le trou que la ligne 207 du document désigne pour l'organe Provenance et qu'il ne comble pas pour lui-même.

---

## 7. Les cinq colonnes

### 1. MCP à installer

| MCP | Ce qu'il débloque | Prérequis |
|---|---|---|
| **MCP d'accès documentaire juridique** — EUR-Lex, Légifrance, BAILII | Fait passer la section 2.5 de D à B sans dépendre du proxy web. C'est la pièce qui manque le plus pour V1 : en l'état, « vérification sur source primaire obligatoire en V1 » n'est pas exécutable ici | Aucun MCP officiel connu à ma connaissance ⏳. À construire ou à remplacer par une liste de domaines autorisés dans le proxy |
| **MCP de flux RSS / Atom** | Le guichet 6, ligne 69, est le cœur du corpus V0 praticable. Un lecteur de flux instrumenté donne du A-usage sur fraîcheur et découverte, immédiatement, sans compte d'essai propriétaire | Liste des flux de la presse et des institutions guadeloupéennes — travail de l'agent Sources locales de V0 |
| **MCP de données ouvertes** — data.gouv.fr, portails de collectivités | Instrumente les lignes 67 à 71 et chiffre la « proportion à établir en V0 » de la ligne 74, la seule inconnue qui décide si le volet moteurs est faisable sans mandat | API publiques, clés gratuites |
| **MCP de gestion de secrets** — coffre, rotation, journal | L'organe de la ligne 211 — chiffrement, révocation, journalisation, cloisonnement. C'est le seul des huit organes qu'on peut tenir par configuration plutôt que par construction | Décision du nœud « Produit sous mandat », ligne 325 |
| **MCP Git / revue de cohérence sur le dépôt** | Empêche la récidive de C2 et C4 : un contrôle de comptage sur les tableaux du prompt à chaque commit | Déjà disponible en partie — voir colonne 3 |

### 2. Logiciels manquants

- **Un vérificateur de cohérence du prompt**, en une centaine de lignes : il compte les lignes des tableaux et les compare aux renvois textuels (« des six », « des sept »), vérifie que chaque ⏳ porte une échéance, et que chaque cran D déclaré est repris dans une déclaration de tête. C2 et C4 auraient été attrapés par un `grep` dans un hook de pré-commit. Le moins cher de tous les gestes de cette critique.
- **Un outil d'annotation de corpus** avec schéma versionné et part scellée, pour R6 et D3 : sans lui, le jeu d'épreuve de V0 ne pourra ni porter des taux d'erreur par champ ni garder une portion de jugement.
- **Un registre de preuve** — une table, pas un document : une ligne par affirmation, avec provenance, robustesse, URL, date de consultation, date de péremption, et l'organe concerné. C'est l'outil qui rend le barème opérant au lieu de déclaratif.
- **Un outil de mesure de latence et de coût au million de documents** pour la ligne 206, avant tout choix d'index.

### 3. Outils déjà disponibles et non exploités

- **Git, déjà en place** (quatre commits). Non exploité comme instrument de doctrine : aucun hook, aucune revue de cohérence, et c'est précisément ce qui a laissé passer C2 et C4 à travers deux révisions. Le document versionne sa doctrine sans la contrôler.
- **La recherche web de cette session** : suffit à produire du C, documenté comme tel. Utile pour cadrer, insuffisant pour V1.
- **Les vingt-cinq skills présentes dans cet environnement**, dont `cadrer-cockpit-veille`, `conduite-de-recherche` et `double-lecture`. Cette dernière est exactement le dispositif qui manque à la section 7 : une relecture adversariale par un lecteur qui n'a pas produit l'artefact, en session neuve. Le document réinvente des relances auto-administrées alors que l'outil d'indépendance existe déjà à côté de lui, non branché.
- **Le dépôt git lui-même comme jeu d'épreuve figé** : c'est ce que j'ai utilisé, et c'est la seule mesure rejouable de cette critique.

### 4. IA existantes qui font ce travail, et à quel prix

Je ne nomme ni produit ni prix. **Motif, et il est de doctrine** : je n'ai pu consulter aucune page officielle de tarification (proxy fermé, sorties collées en § 6), et la ligne 147 du document interdit « gratuit » pour ce qui est gratuit en version d'essai tandis que la ligne 145 interdit « référence du marché ». Tout ce que je pourrais écrire ici serait du **D habillé en C** : des noms et des prix de mémoire, périmés par construction, sur un marché dont le document lui-même dit que les conditions changent tous les six mois (ligne 133).

Ce que je peux dire sans mentir : la catégorie existe — gestion d'avis et réponse assistée, veille média sous licence, orchestration de publication sociale — et le document en a déjà nommé deux occupants par leur guichet (gestionnaires d'avis et channel managers en guichet 1, ligne 35 ; plateformes de veille sous licence en guichet 4, ligne 38), ce qui est la bonne façon de les traiter. Les nommer et les chiffrer est le travail de l'agent « Acteurs en place et leur guichet » de V1 (ligne 260), avec sa règle, qui est la bonne : « soit c'est documenté, soit c'est déclaré inconnu ». Je déclare inconnu.

### 5. Futurs possibles à douze mois ⏳

- ⏳ **Ouverture d'un accès délégué standardisé aux avis** par une ou plusieurs grandes plateformes, sous pression réglementaire européenne sur l'accès aux données et l'interopérabilité. Transformerait le guichet 2 de voie contractuelle artisanale en guichet 3. Effet : le seul avantage défendable du document (ligne 98, « aucun concurrent mondial ne peut l'ouvrir ») s'évapore. **C'est le risque stratégique numéro un et il n'est nulle part au document.**
- ⏳ **Durcissement de l'accès automatisé** au contraire, avec authentification généralisée : le 5b de la ligne 49 se vide, et le guichet 6 reste seul praticable sans contrat. Renforce la justesse de 2.4 et rend urgent de bâtir V0 sur le guichet 6.
- ⏳ **Modèles multilingues locaux de qualité suffisante pour le créole guadeloupéen**, exécutables sur machine modeste. Attaquerait directement l'exigence Langues de la ligne 111, aujourd'hui disqualifiante pour les outils génériques — donc l'un des quatre avantages de conception du document.
- ⏳ **Offres de licence de contenu de presse à l'échelle d'une très petite entreprise**, par guichet unique régional. Solderait le nœud ouvert de la ligne 326 sans renoncer à la presse locale.
- ⏳ **Agents de vérification de preuve** — outils qui tracent automatiquement la provenance d'une affirmation jusqu'à une URL consultée et datent chaque assertion. C'est la couche que la ligne 18 déclare « à inventer, personne ne la vend ». Si cela arrive dans les douze mois, l'étalon de l'organe Provenance (ligne 207) cesse d'être notre couche propre et redevient un achat. **Deuxième risque stratégique absent du document.**

---

*Critique produite le 2 octobre 2026. Jeu d'épreuve : le fichier `00-PROMPT-DE-LANCEMENT.md` au commit `8070f2c`, non modifié. Aucun commit git effectué.*
