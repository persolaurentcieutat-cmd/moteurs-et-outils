# Plan de construction

2 octobre 2026 — tient le périmètre décidé par Laurent Cieutat : **les quatre outils**, veille, blog, publication, avis.
Ce plan les **ordonne**, il n'en retire aucun.

**Règle de lecture.** Chaque ligne porte son couple provenance·robustesse. `1` et `2` portent une décision ; `3` est indicatif et **n'engage aucune dépense avant son test**. Les notions employées sont au lexique du registre de démarche.

---

## 0 — Le principe qui commande tout le reste

> Le code n'est pas le coût. L'approbation l'est.

Mesuré : `A·1`. Un orchestrateur de publication écrit et exécuté, deux envois réussis, **le troisième refusé en 403 — application non approuvée**.

Trois postes ne se raccourcissent pas en travaillant plus : **l'approbation de chaque application par chaque plateforme**, **un mandat signé par client**, **la lecture des licences source par source**. Ils se lancent, et ensuite on attend. Tout le reste s'écrit pendant cette attente.

D'où la forme de ce plan : **administratif d'abord, technique ensuite.**

---

## Semaine 0 — Ce qui ne se rattrape pas

À engager immédiatement, avant toute ligne de code. Trois des quatre sont gratuites.

| Geste | Coût | Pourquoi maintenant | Cran |
|---|---|---|---|
| **Déposer les dossiers d'approbation** sur chaque plateforme sociale visée | Gratuit, délai inconnu ⏳ | Le refus 403 est mesuré. Le délai d'une plateforme ne se rattrape jamais | `A·1` pour le refus, `D` pour les délais |
| **Tester l'accès aux avis Google** | Un compte, une heure | Si cet accès est cassé, **le volet avis n'a aucune plateforme praticable**. Trois témoignages de forum le disent, aucune source primaire | `C·3` — à monter en `A·1` |
| **Question au bâtonnier de Guadeloupe** — quatre points rédigés | Gratuit | Les textes ne nomment jamais « avis en ligne ». Toute l'analyse du segment avocat applique des règles générales à un objet non nommé | `B·2` sur les textes, réserve assumée |
| **Élargir l'accès réseau de l'environnement** | Un réglage | Aucune mesure guadeloupéenne réelle n'a été possible. Zéro page locale captée | constaté |
| **Verser au dépôt les deux briques fragiles** | Une demi-journée | Elles tiennent le créole et la fraîcheur, et ont **un** mainteneur soutenu et **zéro** | `A·1` |

**Porte de sortie.** Si le test Google revient négatif, le volet avis attend une autre plateforme et les phases 1 à 3 ne changent pas d'un jour.

---

## Phase 1 — La veille officielle

Le seul produit vendable sans attendre personne. **Le socle existe déjà** : 1 183 lignes, installation en 7,1 secondes, **21 assertions sur 21 prouvées**, rejouables à un an sans réseau — `A·1`.

### Ce qu'on vend

Pas une revue de presse. Une **veille officielle et économique** : qui s'est créé, qui a cédé, qui a liquidé, quel marché public a été attribué, quelle vigilance est active. Un rapport hebdomadaire où **chaque ligne porte son adresse, son horodatage et son empreinte**.

### Pourquoi ce socle est inattaquable

| Propriété | Fondement | Cran |
|---|---|---|
| Risque de coupure **structurellement nul** | Ces publications sont **obligatoires par la loi** | `B·2` |
| Aucun droit à payer | Le droit des producteurs de bases est **cédé par écrit** dans la licence | `B·2` |
| L'administration ne peut pas s'y opposer | C'est un droit, pas une tolérance | `B·2` |
| Valeur ajoutée maximale | **Donnée ouverte mais illisible** — le client ne la lira jamais seul | jugement, assumé |

### Ce que la provenance sert quatre fois

Un seul organe, quatre obligations réglementaires que personne ne traite :

| Obligation | Ce que la provenance en fait |
|---|---|
| Mentionner source et date de mise à jour, quel que soit le support | Le champ existe, mesuré à 100 % |
| Transmettre à l'Ordre toute publicité et modification | Le journal **est** le registre transmissible |
| Surveiller les liens sortants et les retirer sans délai | La trace **est** l'inventaire des liens |
| Prouver qu'un témoignage n'est pas fabriqué | La rejouabilité par empreinte **est** la preuve |

### Travaux

— Trois sources en accès ouvert déclaré, licence lue et datée. **Règle inscrite dans le code : ne pas collecter une source dont la licence n'a pas été lue**
— Le rapport hebdomadaire, format arrêté
— Le pont translingue reste ouvert : une panne décrite en créole ne remonte pas sur le mot français ⏳
— **Interdiction absolue : dépouiller les accents avant la détection de langue.** Rapport de 933 entre les données d'entraînement du créole guadeloupéen et de l'haïtien — `A·1`

### Le test qui décide, et il est gratuit

Quatre semaines de données réelles filtrées Guadeloupe, quatre rapports produits, **compter les lignes utiles par semaine**. Sous une dizaine, ça ne se vend pas. Puis les montrer à cinq établissements : « cinquante euros par mois pour recevoir ceci chaque lundi ? »

**Deux à trois jours. Décisif dans les deux sens.**

### Prix

La bande entre **30 € et 200 € par mois est vide** — plus aucune prestation humaine, seulement des outils en libre-service (`B·2`). Plancher de coût : **25 à 35 € HT sans la presse** (`B·3`).

**La veille presse ne tient pas sous 100 €** : 52,50 € HT par client et par mois de licence (`B·3`). Elle attend la phase 1 bis, et seulement si un client la demande.

---

## Phase 2 — Le blog

Le moins cher des quatre. **Le blog est le rendu de la table des articles** — l'organe existe.

Ce qu'il ajoute, et que personne ne vend : **un article dont chaque affirmation remonte à une source primaire datée et rejouable.** C'est la provenance appliquée à la rédaction.

Obligations portées : responsabilité éditoriale assumée et nommée, aucun abri d'hébergeur, droit de réponse, mentions légales.

---

## Phase 3 — La publication automatique

**Le code est fait** — 215 lignes pour trois plateformes, environ 70 par plateforme supplémentaire, exécuté (`A·1`). Cette phase **n'attend pas du développement, elle attend les approbations déposées en semaine 0.**

### Le piège de licence, tranché

L'orchestrateur couvrant trente plateformes est sous copyleft réseau. Sa clause s'ouvre sur « si vous modifiez le programme » — **et les exigences guadeloupéennes obligent à modifier**. Il faudrait donc livrer notre code à chaque client payant. Aucune brique permissive équivalente n'existe. **Verdict : construire le minimum, trois plateformes, pas trente** (`B·2`).

### Ce qui est inscrit dans le schéma, pas promis

— **Validation humaine obligatoire avant tout envoi.** Deux déclencheurs de base refusent un contenu généré sans relecteur nommé, vérifié en exécution (`A·1`)
— Mention du contenu généré, champ dédié
— Programmation sur l'heure locale du client, UTC-4 sans heure d'été, **0,00 h d'erreur** mesurée (`A·1`)

### Ce qui est retiré du périmètre, et c'est une économie

**Republier un article de presse sur un réseau social : 50 à 150 € HT par article, compté double.** Économiquement mort (`B·2`). On publie nos propres textes, jamais de la presse reprise.

---

## Phase 4 — Les avis

En dernier, et pour trois raisons mesurées, non par prudence.

| Raison | Cran |
|---|---|
| **Seul organe sans équivalent libre** — quatre candidats, quatre éliminés | `A·1` |
| **Seul à exiger un mandat signé** par client, donc le seul bloqué par un tiers | `B·2` |
| **Aucune plateforme n'offre un accès délégué complet.** Google seul, et son accès avis est douteux | `B·2` / `C·3` |

Mais le manquant est minuscule : l'orchestrateur porte déjà le parcours d'autorisation et l'énumération des établissements. **Manquant réel : deux appels réseau** (`A·1`).

### Les cinq conditions cumulatives

1. Accès par **jeton délégué, jamais d'identifiants détenus**
2. Faisabilité tranchée **plateforme par plateforme** — une plateforme sans accès délégué est hors du produit
3. Date d'expérience de consommation **captée dès l'origine**. Le schéma la porte déjà, et une absence doit être **déclarée** au lieu d'être silencieuse (`A·1`)
4. Aucun avis non vérifié diffusé, aucun avis modifié
5. **Zéro publication sans relecture humaine**, responsabilité éditoriale nommée

### Deux pièges qui nous visent

**Vendre à un avocat la collecte d'avis par message mobile ferait de nous l'instrument d'un contournement** — interdit par son règlement intérieur (`B·2`). Fonction phare de trois concurrents, interdite pour nous sur ce segment.

**Un générateur de texte sans garde-fous métier produit une faute disciplinaire** : annoncer un taux de succès est sanctionné (`B·2`).

### Ce qui est fermé, définitivement

**La santé.** Le code de déontologie médicale proscrit les témoignages de tiers et les comparaisons. On ne vend pas de gestion d'avis à un médecin (`B·2`).

**L'intégration de la note chez l'avocat.** Il peut solliciter et recueillir des avis ; il ne peut pas reprendre la note — mention comparative prohibée. Ce qui est sanctionné est **le faux témoignage, pas le témoignage** (`B·2`).

### Règle d'arrêt

**Une date, pas une condition.** Passée cette date sans mandat signé, bascule au périmètre réduit, consignée comme décision assumée. En attendant : **rendre le service à la main, sous mandat, facturé.** Ce n'est pas de l'attente — c'est l'acquisition du client, la mesure de l'étalon manuel et la seule matière licite.

**Contrainte de calendrier irréversible : le schéma de captation de la date d'expérience doit être gelé avant le premier jour de service manuel.** Sinon la donnée est perdue pour ce client, définitivement.

---

## Ce que ce plan refuse d'inscrire

**Le jeu d'épreuve guadeloupéen à 25-40 jours-personne d'annotation.** C'était ma conception, et elle ferait **payer le juge plus cher que le produit** (`B·2`). Les étalons de provenance se mesurent à 100 % sans aucune annotation humaine (`A·1`). Le plan prend ceux-là, et seulement ceux-là.

**Tout chiffrage en jours de travail.** Un budget inventé est du cran `D` déguisé en plan. Les trois postes de calendrier décident, pas l'effort.

**Toute mesure obtenue en falsifiant un signal chez un tiers** : ni faux avis, ni faux compte, ni faux clic. Aucune décision ne lève cette règle.

---

## Les seuils d'abandon

Un plan sans porte de sortie est un tunnel.

| Seuil | Déclencheur | Conséquence |
|---|---|---|
| **Règle du loyer** | Coût annuel d'un organe > 10 % du revenu récurrent qu'il débloque | On loue, on n'écrit pas |
| **Barrière de l'étalon** | Un composant n'atteint pas 80 % de l'étalon après dix jours, sur 30 à 50 pages | Abandon du composant |
| **Volume de veille** | Moins d'une dizaine de lignes utiles par semaine au test gratuit | La veille officielle seule ne se vend pas → repenser l'offre avant tout développement |
| **Mandat** | Date dépassée sans signature | Périmètre réduit, décision assumée consignée |
| **Trois interdictions permanentes** | — | Jamais reconstruire de la cryptographie · jamais un organe déjà tenu par le libre · jamais un organe qu'aucun client n'a payé |

---

## La question que personne n'a posée

Le coût réel est humain, dans un rapport de **dix contre un** : 22 à 37 jours-personne par an de maintenance, contre 450 à 700 € de serveur (`B·3`).

**Qui maintient ?** Décision attendue. Elle commande ce qui est tenable bien plus que « qui construit ».

---

## Ce qui attend une décision de Laurent

| Objet | Coût | Ce que ça débloque |
|---|---|---|
| **Test de l'accès aux avis Google** | Gratuit, une heure | La praticabilité du volet avis entier |
| **Question au bâtonnier** | Gratuit | La seule réserve du segment avocat |
| **Test de la veille sur quatre semaines réelles** | Gratuit, deux à trois jours | Si le produit se vend, dans les deux sens |
| Élargissement du réseau | Un réglage | Toute mesure guadeloupéenne |
| Test chez le prestataire local | **200 €**, non 80 | Le premier `A` sur le marché et le jeu d'épreuve local |
| **Qui maintient** | Une décision | Ce qui est tenable |
| Licence de veille presse | 52,50 € HT par client et par mois | La presse dans le produit, ou son renvoi |
