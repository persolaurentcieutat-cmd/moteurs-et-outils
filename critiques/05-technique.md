# Critique 05 — La réalité technique

**Angle d'attaque** : le document parie, décision n°1, que « quand aucun équivalent libre n'existe, on construit ». J'attaque l'antécédent, pas le conséquent. La question n'est pas de savoir si on sait construire : c'est de savoir si l'hypothèse « aucun équivalent libre n'existe » tient organe par organe. Elle ne tient que pour un organe sur huit.

Lecteur : agent technique adversarial
Date de la session : **2026-10-02**
Conteneur : Python 3.11.15, Node 22.22, client PostgreSQL 16.14, git 2.43.0, curl 8.5.0, jq 1.7. Pandoc absent.
**Docker inutilisable** : le client 29.6.2 est présent mais il n'y a aucun démon (`dial unix /var/run/docker.sock: connect: no such file or directory`), et je n'ai pas le droit d'en démarrer un. Tout ce qui suit a donc tourné en binaire autonome, en paquet pip, ou pas du tout. Cela a écarté de mon banc tout ce qui ne se livre qu'en image : Onyx, Infisical, Mixpost, Postiz, Typesense.
**Sortie réseau filtrée** : le mandataire de sortie refuse par politique tous les hôtes guadeloupéens que j'ai tentés — `la1ere.francetvinfo.fr`, `www.rci.fm`, `www.franceantilles.fr`, `www.karibinfo.com`, `www.guadeloupe.cci.fr`, `www.meteofrance.gp` (403 au CONNECT), et aussi `developers.google.com`, `www.ovhcloud.com`, `huggingface.co`. Sont joignables : PyPI, npm, `raw.githubusercontent.com`, `github.com/.../releases/download`, le clonage git. **Conséquence lourde : je n'ai pas pu constituer un seul échantillon de page guadeloupéenne réelle.** Ce point n'est pas un détail d'intendance, il est traité en section 5.

---

## 1. Mes lignes en cran D — déclarées avant tout contenu

Conformément à la règle de la section 4.1 du document. Ces lignes sont des pistes, jamais des fondements.

| # | Affirmation en cran D | Pourquoi elle reste D | Ce qui la ferait monter |
|---|---|---|---|
| D1 | **Mes phrases en créole guadeloupéen sont écrites par moi, de mémoire.** « Sé on bèl kaz, moun-la té ka akèy nou byen », « Dlo-la pa té cho », etc. | Je n'ai atteint aucun corpus gcf attesté. Leur orthographe et leur idiomaticité ne sont vérifiées par personne. | Un corpus d'avis réels en créole, relu par un locuteur. C'est la tâche « Jeu d'épreuve » de V0 |
| D2 | GlotLID couvrirait `gcf` sur plus de 2 000 langues | HuggingFace injoignable (000 au CONNECT). Je n'ai pas pu charger le modèle | Télécharger `cis-lmu/glotlid` et le passer sur le même échantillon |
| D3 | Meilisearch serait passé de MIT pur à `MIT AND BUSL-1.1` à une date récente | J'ai lu l'état **actuel** du fichier LICENSE, pas son historique | `git log --follow LICENSE` sur le dépôt, que je n'ai pas exécuté |
| D4 | Les conditions d'utilisation de Booking et de TripAdvisor interdiraient la collecte de tiers | Non vérifiées. Je n'ai lu aucune de ces conditions dans cette session | Lecture des conditions, source par source, comme la section 2.3 l'exige |
| D5 | Taux d'abandon des projets libres d'infrastructure sur trois ans | Aucune mesure. Je n'ai que des intuitions de métier | Une base type Libraries.io ou une mesure maison sur un panier de dépôts |
| D6 | Les quotas de l'interface Google Business Profile, et sa procédure de validation | `developers.google.com` bloqué. Je n'ai qu'un résumé de moteur de recherche, donc du C au mieux | Lecture de la documentation primaire et dépôt d'une demande d'accès réelle |
| D7 | Le prix d'une licence de contenu auprès du CFC | Rien cherché, hors de mon angle | Devis réel, tâche de V1 |

**Ce que je ne déclare PAS en D, et pourquoi** : tout ce qui suit en section 2 porte une sortie de commande collée, ou la lecture d'un fichier LICENSE que j'ai ouvert moi-même dans cette session.

---

## 2. Fiches-organes

Gabarit de la section 4.4. Trois candidats tenus au maximum par organe, jamais un décompte pour montrer que j'ai cherché.

### Remarque préalable sur le gabarit lui-même

Le champ « Étalon mesuré — les chiffres obtenus au temps 2, sortie collée » est **vide sur mes huit fiches, et il le restera**. Le temps 2 exige d'instrumenter le modèle propriétaire « par version d'essai ou compte de démonstration ». Je n'ai ni carte bancaire, ni identité d'entreprise, ni accès réseau aux sites de ces éditeurs. Je le dis plutôt que de le combler : c'est un trou structurel, repris en section 5.

---

### Organe 1 — Découverte et collecte

| Champ | Contenu |
|---|---|
| **Organe visé** | Découverte et collecte (section 6, ligne 1) |
| **Modèle repéré** | Non instrumenté. Catégorie identifiée mais **aucun produit nommé avec sa version** : je refuse de nommer un modèle que je n'ai pas fait tourner, le document l'interdit au temps 1 |
| **Guichet emprunté par ce modèle** | **Inconnu.** Je ne suppose pas |
| **Étalon mesuré** | Néant — voir remarque préalable |
| **Équivalent libre trouvé** | **Scrapy 2.19.0** — licence **BSD-3-Clause**, lue dans `LICENSE` du dépôt (`Redistribution and use in source and binary forms…`) et confirmée par `License-Expression: BSD-3-Clause` des métadonnées du paquet. Dernier commit **2026-10-02T20:29:06+02:00**, 646 commits sur 12 mois, 73 auteurs distincts, **3 auteurs à 10 commits ou plus**, 11 564 commits d'historique. <br> **feedparser 6.0.14** — BSD-2-Clause (métadonnées du paquet). <br> **trafilatura.feeds 2.3.0** — Apache-2.0, voir organe 2 |
| **Écart à l'étalon** | Non chiffrable faute d'étalon. Ce que j'ai mesuré à la place : Scrapy **respecte `robots.txt` par défaut** (`ROBOTSTXT_OBEY=True`), compteur `robotstxt/forbidden: 1`, la page interdite n'a jamais été récupérée. Mais Scrapy **n'applique pas la directive `Crawl-delay`** : délais observés 1,63 s et 1,84 s pour un `Crawl-delay: 2` annoncé |
| **Tenue des six exigences** | **Fuseau — TENUE.** `feedparser` normalise `Tue, 29 Sep 2026 10:15:00 -0400` en `published_parsed` déjà converti en UTC (14:15) ; fraîcheur recalculée avec erreur **0,00 h**. <br> **Langues — TENUE** (organe agnostique au contenu). <br> **Saisons — à vérifier** : rien dans Scrapy ne module la charge ; c'est un ordonnanceur à écrire, pas un défaut de brique. <br> **Sources locales — NON TENUE, et par ma faute d'environnement** : je n'ai atteint aucune source guadeloupéenne. Le corpus local reste à recenser (tâche V0). <br> **Tissu économique — à vérifier** : Scrapy exige un développeur, pas un administrateur système ; acceptable si la collecte est opérée par le prestataire et non par le client. <br> **Droit — TENUE** : s'auto-héberge, aucune donnée ne sort |
| **Verdict** | **ADOPTER, avec une rustine de quelques heures.** Pas reconstruire |
| **Si reconstruire** | Le manquant exact : un intergiciel de téléchargement qui lit `Crawl-delay` dans `robots.txt` et le pousse dans `DOWNLOAD_DELAY` par domaine. **Coût : 0,5 jour.** C'est tout. La règle de conception du degré 5b du document — « débit de collecte respectueux » — n'est donc pas tenue par défaut, et c'est un correctif, pas un organe |
| **Coût réel à l'échelle visée** | Un cœur suffit largement : voir organe 2 pour le débit. Serveur partagé avec l'extraction |
| **Cran de preuve** | **A-usage** sur Scrapy, feedparser et la découverte de flux. **B** sur les licences |
| **Source** | Dépôts clonés et `LICENSE` lus le 2026-10-02 : `github.com/scrapy/scrapy`, `github.com/adbar/trafilatura`. Sorties collées en annexe A1, A5, A6 |

---

### Organe 2 — Extraction de contenu propre multilingue

| Champ | Contenu |
|---|---|
| **Organe visé** | Extraction (section 6, ligne 2) |
| **Modèle repéré** | Non instrumenté — voir remarque préalable |
| **Guichet** | **Inconnu** |
| **Étalon mesuré** | Néant côté propriétaire |
| **Équivalent libre trouvé** | **trafilatura 2.3.0** — licence **Apache-2.0**, texte lu dans `LICENSE`. Dernier commit **2026-10-02T18:53:21+02:00**, 70 commits sur 12 mois, 26 auteurs distincts, **1 seul auteur à 10 commits ou plus** (Adrien Barbaresi), 1 669 commits d'historique. <br> **htmldate 1.11.0**, **py3langid 0.4.0** (BSD-3-Clause, voir organe 7) |
| **Écart à l'étalon** | Pas d'étalon propriétaire, donc je mesure contre le seul jeu annoté que j'ai pu atteindre : les **990 pages annotées à la main du dépôt trafilatura**. Résultats que j'ai calculés moi-même : `fast` précision **0,9329**, rappel **0,9071**, F1 **0,9198**, 25,3 ms/page ; `fallback` précision **0,9458**, rappel **0,9065**, F1 **0,9257**, 35,3 ms/page ; **0 plantage sur 990 pages**. <br> **Et ce chiffre est inadmissible au sens de la section 9 du document.** Composition du corpus que j'ai comptée : **438 pages en `.de`, 240 en `.com`, 55 `.org`, 43 `.ch`, 37 `.at`, 13 seulement en `.fr`, et ZÉRO en `.gp`.** Le document refuse « une mesure sur un jeu d'épreuve non guadeloupéen ». Il a raison de le refuser, et c'est précisément pour cela que le F1 = 0,9198 ne décide de rien. Je le donne pour ce qu'il vaut : un ordre de grandeur, pas un étalon opposable |
| **Tenue des six exigences** | **Fuseau — NON TENUE PAR DÉFAUT, et réparable en heures.** La page portait `article:published_time = 2026-09-29T10:15:00-04:00`. trafilatura rend `date = '2026-09-29'` : **l'heure et le décalage UTC-4 sont perdus.** Pour la métrique de fraîcheur de l'organe 1, une date sans heure est inutilisable. Mais `htmldate`, qui est **déjà une dépendance de trafilatura**, rend `2026-09-29T10:15:00-0400` avec `outputformat="%Y-%m-%dT%H:%M:%S%z"`. Vérifié : aucune occurrence de `outputformat` dans le code de trafilatura, le format est figé en dur, non configurable. **Correctif : appeler `htmldate.find_date` soi-même. Quelques heures.** <br> **Langues — TENUE.** Sur ma page à quatre langues, les quatre phrases de corps sont conservées, dont la phrase créole et la phrase anglaise, rappel **4/4 = 100 %**, et **0 bloc de bruit sur 10** (bannière de cookies, navigation, publicité, infolettre, partage, articles liés, commentaires, mentions légales, pied de page). Le commentaire de lecteur est exclu. L'extracteur est agnostique à la langue, ce qui est exactement ce qu'il faut. <br> **Saisons — sans objet.** <br> **Sources locales — à vérifier**, aucune page `.gp` testée. <br> **Tissu économique — TENUE** : bibliothèque, pas de service à administrer. <br> **Droit — TENUE**, et mieux : `SLEEP_TIME = 5.0` et `SSRF_PROTECTION = on` sont les valeurs par défaut du fichier de réglages, que j'ai lu. La brique implémente déjà la règle de débit respectueux que le document écrit en section 2.3 |
| **Verdict** | **ADOPTER.** Reconstruire un extracteur serait de l'orgueil technique caractérisé |
| **Si reconstruire** | Rien à reconstruire. Deux rustines : l'horodatage complet (quelques heures), et un découpage par segment avant détection de langue (voir organe 7) |
| **Coût réel à l'échelle visée** | 25,3 ms/page mesuré, soit **39 pages/s sur un cœur, 3,4 millions de pages par jour.** Si la presse guadeloupéenne produit 200 articles par jour tous titres confondus, l'extraction de la journée coûte **5 secondes de processeur**. Le coût d'infrastructure de cet organe est, au sens propre, négligeable |
| **Cran de preuve** | **A-usage** (sortie collée) pour l'extraction, la mesure F1 et la perte d'horodatage. **B** pour la licence |
| **Source** | `github.com/adbar/trafilatura`, `LICENSE` et `tests/evaldata.json` lus le 2026-10-02. Annexe A2 |

---

### Organe 3 — Index et recherche

| Champ | Contenu |
|---|---|
| **Organe visé** | Index (section 6, ligne 3) |
| **Modèle repéré** | Non instrumenté |
| **Guichet** | **Inconnu** |
| **Étalon mesuré** | Néant côté propriétaire |
| **Équivalent libre trouvé** | **Meilisearch 1.24.0** — **attention, licence composite.** Le fichier `LICENSE` déclare lui-même `SPDX-License-Identifier: MIT AND BUSL-1.1`. J'ai lu `LICENSE-EE` : « Licensed Work: Any file explicitly marked as "Enterprise Edition (EE)" … residing in enterprise_editions modules/folders » ; « Additional Use Grant: You may use, modify, and distribute the Licensed Work for **non-production purposes only** » ; « Change License: MIT » ; « Change Date: Four years ». J'ai listé les fichiers EE : `milli/src/sharding`, `index-scheduler/.../network.rs`, `.../s3.rs`, `search/federated/network`, `routes/network`. **Donc : le mono-nœud est MIT, l'éclatement en partitions, la recherche fédérée en réseau et les instantanés S3 exigent un contrat commercial pour la production.** Dernier commit 2026-09-29T13:51:58Z, 2 051 commits sur 12 mois, 46 auteurs, **12 auteurs à 10 commits ou plus**. <br> **Typesense** — GPL-3.0, texte GNU GPL lu dans `LICENSE.txt`, dernier commit 2026-10-02T08:37:36+05:30, 201 commits/12 mois, 15 auteurs, 5 à 10 commits ou plus. Non lancé : ne se livre pas en binaire simple ici. <br> **Quickwit** — Apache-2.0, texte lu, dernier commit 2026-10-02T14:16:16Z, 473 commits/12 mois, 39 auteurs, **19 à 10 commits ou plus**. Non lancé |
| **Écart à l'étalon** | Pas d'étalon propriétaire. Mesures propres sur Meilisearch, 10 000 documents de presse réels (texte extrait des 990 pages, dupliqué pour tenir la pente) : indexation **375 documents/s**, **207,1 Mo sur disque**, soit **au plancher 20,7 Go par million de documents** — plancher et non plafond, parce que la duplication partage le vocabulaire et sous-estime l'index inversé sur un corpus réellement distinct. Latence sur 60 requêtes : **p50 = 1 ms, p95 = 2 ms, max = 3 ms** |
| **Tenue des six exigences** | **Fuseau — TENUE.** Tri sur un champ `date_utc` en UTC strict, ordre correct. Le fuseau est une affaire d'affichage, pas d'index. <br> **Langues — TENUE EN PARTIE, et c'est l'écart le plus intéressant de tout mon retour.** Ce qui marche : les requêtes créoles atteignent les avis créoles — `klimatizè` → avis gcf, `kaz` → avis gcf, `laplaj` → avis gcf, et `akey` sans accent trouve `akèy` (normalisation diacritique). La tolérance aux fautes marche : `climatisé` retrouve « climatisation ». Ce qui ne marche pas : `plaj` tronqué ne retrouve pas `laplaj` — **absence de segmenteur créole, que j'ai vérifiée directement** : l'API refuse la locale `gcf` et la locale `hat` en listant ses 70 locales valides, où **aucun créole ne figure**. Et surtout : **la recherche translingue échoue.** La requête `climatisation` ne remonte PAS l'avis créole n°2 qui décrit exactement la même panne (`klimatizè-la té kasé`). Pour un client qui cherche « climatisation » dans son tableau de bord, les avis créoles sont invisibles. C'est le vrai manquant de cet organe. <br> **Saisons — sans objet.** <br> **Sources locales — sans objet.** <br> **Tissu économique — TENUE** : un binaire de 133 Mo, un processus, aucun administrateur. <br> **Droit — TENUE** si auto-hébergé, et `--no-analytics` coupe la télémétrie |
| **Verdict** | **ADOPTER en mono-nœud** (noyau MIT), **ADAPTER** pour le pont translingue. Ne pas reconstruire un moteur d'index : ce serait l'orgueil technique le plus coûteux du projet |
| **Si reconstruire** | Rien. Le manquant exact est un **pont translingue fr ↔ gcf ↔ en ↔ es** : soit un champ de traduction calculé à l'indexation, soit un index vectoriel multilingue à côté du lexical. **Coût : 3 à 6 jours** pour la version « champ traduit à l'indexation », qui est la plus simple et la plus traçable — elle laisse une trace de provenance, ce que l'embarquement vectoriel ne fait pas |
| **Coût réel à l'échelle visée** | 20,7 Go/million au plancher. Un corpus guadeloupéen à 200 documents/jour sur 10 ans fait 730 000 documents, soit de l'ordre de **15 à 30 Go**. Tient sur un disque de 80 Go. Le piège n'est pas le volume, c'est **la licence si un jour on veut partitionner** : à ce moment-là, le prix n'est plus zéro et n'est pas public |
| **Cran de preuve** | **A-usage** (indexation, requêtes, latence, taille, refus de locale créole). **B** pour les licences et les paramètres BUSL |
| **Source** | Binaire officiel `github.com/meilisearch/meilisearch/releases/download/v1.24.0/meilisearch-linux-amd64`, exécuté le 2026-10-02 ; `LICENSE` et `LICENSE-EE` lus dans le dépôt cloné le 2026-10-02. Annexe A3 |

---

### Organe 4 — Chaîne de provenance et traçabilité

| Champ | Contenu |
|---|---|
| **Organe visé** | Provenance (section 6, ligne 4) |
| **Modèle repéré** | Aucun, et c'est cohérent avec le document : « elle porte son propre étalon, à inventer — personne ne le vend » |
| **Guichet** | Sans objet, organe interne |
| **Étalon mesuré** | Néant, il n'y a pas de modèle |
| **Équivalent libre trouvé** | **in-toto 3.1.0** — **Apache-2.0**, texte lu dans `LICENSE` (« Copyright 2018 New York University / Licensed under the Apache License, Version 2.0 »), et `License-Expression: Apache-2.0` des métadonnées. Dernier commit 2026-08-27T17:33:27-04:00, 64 commits sur 12 mois, 7 auteurs, **2 auteurs à 10 commits ou plus**, 2 479 commits d'historique. Dépend de `securesystemslib 1.5.1`, MIT. <br> **OpenLineage** — Apache-2.0, texte lu, dernier commit 2026-10-02T13:27:52+02:00, 559 commits/12 mois, 80 auteurs, 9 à 10 commits ou plus. Non lancé : orienté chaînes de données, pas assertion documentaire. <br> **c2pa-rs** — double **MIT / Apache-2.0** (`LICENSE-MIT` et `LICENSE-APACHE` présents, pas de `LICENSE` unique), dernier commit 2026-10-02T09:44:39-07:00, 715 commits/12 mois, 40 auteurs, 11 à 10 commits ou plus. Non lancé : orienté médias, pas texte |
| **Écart à l'étalon** | Pas d'étalon. Ce que j'ai prouvé à la place, sur la chaîne collecte → extraction : attestations signées en ed25519, **signatures VALIDES** aux deux maillons, **contrôle négatif concluant** (la clé du collecteur est refusée sur l'attestation de l'extracteur, `SignatureVerificationError`), et **falsification détectée** — après ajout d'une phrase au fichier extrait, l'empreinte attestée `861200b9…` ne correspond plus à l'empreinte réelle `8d4efb63…` |
| **Tenue des six exigences** | **Fuseau — TENUE**, les attestations portent l'instant en UTC ; j'ai inscrit `capte-le-2026-10-02T15:10:00-04:00-guichet-6` dans la commande attestée, donc le décalage figure dans la preuve. <br> **Langues — TENUE**, l'organe hache des octets, la langue lui est indifférente. <br> **Saisons — sans objet.** <br> **Sources locales — sans objet.** <br> **Tissu économique — TENUE**, invisible pour le client. <br> **Droit — TENUE**, et au-delà : la chaîne d'attestation est exactement la pièce qui documente « retrait sous demande de l'éditeur » et la licéité d'une collecte, donc elle sert directement le RGPD et les guichets 5b et 6 |
| **Verdict** | **ADAPTER.** in-toto donne l'infalsifiabilité et la rejouabilité au niveau des fichiers. Ce qu'il ne donne pas, c'est le grain **assertion** : « cette phrase de mon brouillon vient de cette page, à cette date, captée par ce guichet ». Mais c'est une couche de données par-dessus, pas un moteur cryptographique à réécrire |
| **Si reconstruire** | Le manquant exact : un modèle de données « assertion → source primaire → instant → guichet », et le rattachement de chaque assertion à l'attestation in-toto du fichier dont elle est tirée. **Coût : 5 à 8 jours.** C'est le seul endroit où je trouve que la revendication « notre couche propre » du document est à la fois vraie et modeste : la couche est mince, parce que la cryptographie et le format d'attestation sont déjà là |
| **Coût réel à l'échelle visée** | Signature ed25519 : microsecondes. Stockage : une attestation JSON par étape, quelques kilooctets. Négligeable. Le coût réel est **la garde des clés de signature**, qui retombe sur l'organe 8 |
| **Cran de preuve** | **A-usage** (attestations produites, vérifiées, contrôle négatif, falsification détectée). **B** pour les licences |
| **Source** | `in-toto 3.1.0` installé depuis PyPI et exécuté le 2026-10-02 ; `LICENSE` lus dans les dépôts clonés le 2026-10-02. Annexe A4 |

---

### Organe 5 — Rédaction assistée sourcée

| Champ | Contenu |
|---|---|
| **Organe visé** | Rédaction (section 6, ligne 5) |
| **Modèle repéré** | Non instrumenté. Voir colonne 4 de la fin de réponse pour les prix publics |
| **Guichet** | **Inconnu** pour les modèles propriétaires |
| **Étalon mesuré** | Néant |
| **Équivalent libre trouvé** | **Haystack** — Apache-2.0, texte lu dans `LICENSE`, dernier commit 2026-10-02T17:30:32+02:00, **2 111 commits sur 12 mois**, 214 auteurs, **15 auteurs à 10 commits ou plus**, 6 432 commits d'historique. Non lancé : ne sert à rien sans modèle de langue, que je ne peux pas héberger ici. <br> **Onyx** — **licence composite, piège**. Le `LICENSE` dit « All content that resides under "ee" directories … is licensed under the Onyx Enterprise License », et le `backend/ee/LICENSE` dit : « may only be used in production, if you … have agreed to … the Onyx Subscription Terms of Service ». Noyau MIT, parties « ee » payantes en production. Dernier commit 2026-10-02T19:14:44Z, **6 024 commits/12 mois**, 68 auteurs, 18 à 10 commits ou plus. Non lancé, Docker requis |
| **Écart à l'étalon** | Pas d'étalon. J'ai mesuré la **métrique que le document choisit lui-même** — « nombre d'affirmations non sourcées par texte » — avec un vérificateur d'ancrage que j'ai écrit en **32 lignes de Python**, adossé à l'index Meilisearch déjà en place. Sur un brouillon de 5 phrases : il attrape **2 affirmations non sourcées sur 5**, et ce sont exactement les deux bonnes — la note chiffrée inventée (« 4,8 sur 5 au classement régional 2026 ») et le superlatif (« le meilleur de Grande-Terre »). Les trois phrases appuyées sur des avis indexés sont validées avec leur identifiant de source |
| **Tenue des six exigences** | **Fuseau — à vérifier**, dépend de l'ordonnanceur de publication, pas du rédacteur. <br> **Langues — NON TENUE EN L'ÉTAT, et c'est le vrai sujet.** Ce n'est pas une question d'outil libre : c'est que **répondre à un avis en créole guadeloupéen suppose un modèle qui écrit le créole guadeloupéen**. Je n'ai pas pu en tester un seul. Détecter le gcf est résolu (organe 7) ; le **générer** ne l'est pas, et rien dans mon banc ne permet d'affirmer qu'un modèle libre en est capable. À mesurer en V0 sur le jeu d'épreuve, avant toute promesse au client. <br> **Saisons — à vérifier.** <br> **Sources locales — TENUE par construction** : le rédacteur ne cite que ce qui est dans l'index, donc ce qui vient des sources locales qualifiées. <br> **Tissu économique — NON TENUE si on héberge le modèle.** Un serveur à carte graphique coûte plus cher que tout le reste de la pile réunie. Une très petite entreprise guadeloupéenne ne paiera pas cela. Conséquence d'architecture : **le modèle est appelé chez un fournisseur, et alors la conformité RGPD du traitement redevient une question ouverte**, parce que les avis portent des prénoms. <br> **Droit — à vérifier**, et c'est le point dur : envoyer des avis nominatifs à un modèle hébergé hors Union européenne est un transfert. C'est une tâche de V1, pas une tâche d'outil |
| **Verdict** | **ADAPTER pour la plomberie, et SUSPENDRE le jugement sur la génération créole.** La moitié « retrouver, citer, vérifier » est de l'assemblage. La moitié « écrire juste, en quatre langues, sans inventer » n'est pas démontrée et ne doit pas être promise |
| **Si reconstruire** | Le manquant exact : le vérificateur d'ancrage de qualité production — le mien fait 32 lignes et attrape déjà les deux cas typiques, mais il lui manque le découpage en assertions (et non en phrases), le seuil de recouvrement, et le refus de publier. **Coût : 4 à 7 jours.** Le modèle de langue, lui, ne se reconstruit pas : il se choisit et se mesure |
| **Coût réel à l'échelle visée** | C'est le seul organe où le coût variable est réel. Appel à un modèle propriétaire : voir colonne 4. Hébergement propre : serveur à carte graphique, hors de portée du prix plafond local |
| **Cran de preuve** | **A-usage** pour le vérificateur d'ancrage. **B** pour les licences de Haystack et d'Onyx. **D** pour toute affirmation sur la qualité du créole généré — je n'en fais aucune |
| **Source** | Dépôts clonés et `LICENSE` lus le 2026-10-02. Annexe A7 |

---

### Organe 6 — Orchestration de publication multi-réseaux

| Champ | Contenu |
|---|---|
| **Organe visé** | Publication (section 6, ligne 6) |
| **Modèle repéré** | Non instrumenté |
| **Guichet** | Pour chaque réseau : à établir en V1. Postiz, lui, emprunte visiblement le **guichet 3** (interface ouverte sur demande) réseau par réseau, puisque chaque fournisseur porte ses propres portées OAuth |
| **Étalon mesuré** | Néant |
| **Équivalent libre trouvé** | **Postiz** — **AGPL-3.0**, texte GNU Affero lu dans `LICENSE`. Dernier commit **2026-10-02T20:46:19+07:00**, 1 278 commits sur 12 mois, 21 auteurs, **5 auteurs à 10 commits ou plus**, 3 186 commits d'historique. **36 implémentations de fournisseurs comptées dans l'arbre git lui-même**, pas dans une page marketing : bluesky, dev.to, discord, dribbble, facebook, farcaster, **gmb**, hashnode, instagram (+ standalone), kick, lemmy, linkedin (+ page), listmonk, mastodon (+ custom), medium, mewe, moltbook, nostr, pinterest, reddit, skool, slack, telegram, threads, tiktok (+ business), tumblr, twitch, vk, whop, wordpress, x, youtube. <br> **Mixpost** — MIT lu dans `LICENSE.md`, mais **dernier commit 2026-03-16T10:06:37Z**, soit **6 mois et demi d'immobilité**, 23 commits sur 12 mois, 2 auteurs, **1 seul à 10 commits ou plus**, 397 commits d'historique. **Disqualifié sur la vitalité**, pas sur la licence |
| **Écart à l'étalon** | Non mesuré : Postiz ne se lance pas sans Docker ici. Je ne lui attribue donc aucun chiffre |
| **Tenue des six exigences** | **Fuseau — TENUE PAR ACCIDENT, et il faut le savoir.** J'ai lu le schéma Prisma : `User.timezone` est de type **`Int`**, un décalage entier, pas un identifiant de zone IANA. Pour la Guadeloupe, qui n'a pas d'heure d'été, `-4` est juste **toute l'année** et le compte est bon. Mais c'est un champ **par utilisateur**, pas par établissement client, et un décalage entier serait faux pour tout client d'une zone à heure d'été. Si le produit sort un jour de Guadeloupe, ce champ casse. <br> **Langues — TENUE**, l'orchestrateur transporte du texte. <br> **Saisons — à vérifier** : il y a un ordonnanceur, reste à savoir s'il accepte des calendriers saisonniers. <br> **Sources locales — sans objet.** <br> **Tissu économique — NON TENUE EN L'ÉTAT** : Postiz se déploie en Docker Compose avec PostgreSQL et Redis. Un prestataire l'opère ; un gîte de cinq chambres ne l'opère pas. Cohérent avec le modèle sous mandat du document, mais c'est un coût d'exploitation à porter. <br> **Droit — ATTENTION, l'AGPL-3.0 est un vrai sujet ici.** C'est exactement le « piège du copyleft en service distant » que le document inscrit en V1. Si la façade professionnelle expose Postiz modifié par le réseau, la section 13 de l'AGPL impose d'offrir le code source correspondant aux utilisateurs distants. Ce n'est pas un interdit, c'est une obligation à tenir, et elle se décide avant d'écrire la première ligne de modification |
| **Verdict** | **ADOPTER ou ADAPTER, surtout ne pas reconstruire.** 36 intégrations de réseaux maintenues par 5 personnes actives : réécrire cela serait l'erreur la plus chère du projet. Reconstruire 36 fournisseurs OAuth, c'est des mois, et c'est une dette permanente puisque chaque réseau casse ses interfaces |
| **Si reconstruire** | Rien à reconstruire. À faire : un fuseau par établissement en identifiant IANA plutôt qu'en décalage entier (**1 jour**), et trancher la question AGPL (**0 jour de code, une décision**) |
| **Coût réel à l'échelle visée** | PostgreSQL + Redis + application : un serveur de 8 Go de mémoire. Voir section 5 |
| **Cran de preuve** | **B** — dépôt cloné, `LICENSE`, arbre des fournisseurs et schéma Prisma lus le 2026-10-02. **Pas de A-usage : Postiz n'a pas tourné**, Docker indisponible. Je ne le classe donc pas A |
| **Source** | `github.com/gitroomhq/postiz-app`, `github.com/inovector/mixpost`, clonés et lus le 2026-10-02 |

---

### Organe 7 — Collecte et réponse aux avis

| Champ | Contenu |
|---|---|
| **Organe visé** | Avis (section 6, ligne 7) |
| **Modèle repéré** | Non instrumenté. Je ne nomme aucun produit que je n'ai pas fait tourner |
| **Guichet** | Pour la lecture et la réponse sur Google : **guichet 3**, interface ouverte sur demande, portée OAuth `business.manage` — **je l'ai lue dans le code de Postiz, pas dans un billet**. Pour les autres plateformes : **guichet 2** selon le document, non vérifié par moi |
| **Étalon mesuré** | Néant |
| **Équivalent libre trouvé** | **C'est ici que la réponse est « presque rien », et c'est l'information la plus utile de mon retour.** Quatre candidats tenus, aucun retenu : <br> **1. `allenyan513/reviewsup.io`** — MIT lu dans `LICENSE`, mais **0 commit sur les 12 derniers mois**, dernier commit **2025-08-12**. **MORT.** <br> **2. `andimuskaj872/google-reviews-manager`** — MIT lu, **0 commit sur 12 mois**, dernier commit **2025-06-15**, 31 commits d'historique au total. **MORT.** <br> **3. `binesheb/google-review-autoreply`** — vivant en apparence (dernier commit 2026-09-30, 134 commits sur 12 mois) mais **1 seul auteur à 10 commits ou plus**, 139 commits d'historique, et surtout : **AUCUN FICHIER DE LICENCE NULLE PART DANS LE DÉPÔT**, vérifié sur l'arbre complet. Sans licence, tous droits réservés : **juridiquement inutilisable pour un produit commercial. Disqualifié.** <br> **4. `agenticadamdotdev/three-things-reviews`** — AGPL-3.0 lu, vivant (dernier commit 2026-09-27, 202 commits sur 12 mois, 2 auteurs à 10 commits ou plus) mais 202 commits d'historique au total, et **il ne fait pas le travail** : c'est un collecteur de témoignages par formulaire propre, pas un agrégateur d'avis de plateformes tierces. **Hors sujet.** |
| **Écart à l'étalon** | Non mesurable : il n'y a rien à mesurer |
| **Tenue des six exigences** | Sans objet, aucun candidat ne passe la porte de la licence ou de la vitalité. **Et il faut noter l'exigence que ces projets ignorent tous les quatre : le multilinguisme.** Un avis de croisiériste espagnol, un avis en créole, un avis en anglais — aucun de ces dépôts ne traite la question |
| **Verdict** | **RECONSTRUIRE — et c'est le seul organe des huit pour lequel je l'écris.** Mais pas de zéro, et c'est le point que le document ne voit pas |
| **Si reconstruire** | **Le manquant exact est beaucoup plus petit qu'il n'y paraît, et je peux le nommer précisément.** J'ai lu `gmb.provider.ts` de Postiz, 648 lignes : il porte déjà **la portée OAuth `https://www.googleapis.com/auth/business.manage`** — la portée exacte qui ouvre la lecture et la réponse aux avis —, le parcours OAuth complet, la vérification des portées obtenues (`checkScopes`), l'énumération des comptes (`mybusinessaccountmanagement.googleapis.com/v1/accounts`), l'énumération des établissements (`mybusinessbusinessinformation.googleapis.com/v1/{account}/locations`), la publication (`mybusiness.googleapis.com/v4/{id}/localPosts`) et les métriques (`businessprofileperformance.googleapis.com`). **Ce qu'il ne fait pas : les avis.** J'ai compté les occurrences de « review » dans ce fichier : **une seule, et c'est un message d'erreur** (« Please review the post content »). <br> Donc le manquant, pour Google, est : **deux appels HTTP de plus sur un fournisseur déjà écrit, déjà authentifié, déjà sous mandat** — la liste des avis et l'écriture de la réponse. **Coût : 2 à 4 jours, pas un organe.** <br> Ce qui reste un vrai chantier : **chaque autre plateforme d'avis**, une par une, avec son guichet propre, et c'est V1/V3 qui le dira. Plus le **tri multilingue des avis** (résolu, organe 7 ci-dessous), la **détection sous 24 h** et la **file de réponse**. Estimation pour un premier organe utilisable, Google seul : **12 à 20 jours.** Pour trois plateformes : à chiffrer après V1, je ne l'invente pas |
| **Coût réel à l'échelle visée** | Dominé par la maintenance, pas par le serveur : voir section 5. Risque de coupure élevé, puisque les points d'accès aux avis sont sur l'ancien hôte `mybusiness.googleapis.com/v4` tandis que les comptes et établissements sont déjà passés en `v1` sur des hôtes séparés — **j'ai observé cette coexistence dans le code**, et une migration de la `v4` est une rupture annoncée |
| **Cran de preuve** | **B** pour tout : licences lues, dates de commit mesurées, code du fournisseur GMB lu. **Aucun A-usage : je n'ai appelé aucune interface d'avis**, faute de compte et de réseau. Je ne prétends pas le contraire |
| **Source** | Dépôts clonés et lus le 2026-10-02. Pour l'existence des points d'accès de réponse aux avis : **cran C**, résumé de moteur de recherche, `developers.google.com` étant bloqué par le mandataire. Ce point doit passer en B en V1 par lecture de la documentation primaire |

---

### Organe 8 — Garde des accès confiés et gestion de secrets

| Champ | Contenu |
|---|---|
| **Organe visé** | Garde des accès confiés (section 6, ligne 8) |
| **Modèle repéré** | Non instrumenté |
| **Guichet** | Sans objet, organe interne. C'est la **condition** du guichet 2 |
| **Étalon mesuré** | Néant côté propriétaire, mais le document donne lui-même les métriques, et **je les ai toutes les quatre mesurées** |
| **Équivalent libre trouvé** | **OpenBao 2.4.3** — **MPL-2.0**, texte « Mozilla Public License, version 2.0 » lu dans `LICENSE`. Dernier commit **2026-10-02T13:51:28+02:00**, **1 350 commits sur 12 mois**, 123 auteurs distincts, **13 auteurs à 10 commits ou plus**, 21 191 commits d'historique. Binaire officiel, construit le 2025-10-22. <br> **SOPS** — MPL-2.0 lu, dernier commit 2026-09-21T22:03:16+02:00, 422 commits/12 mois, 29 auteurs, **3 à 10 commits ou plus**. Chiffre des fichiers, ne fait ni révocation ni journal : complémentaire, pas substituable. <br> **Infisical** — **licence composite, piège** : `LICENSE` dit « All content that resides under any "ee/" directory … licensed under the license defined in "ee/LICENSE" », reste en MIT Expat. Très vivant (13 762 commits/12 mois, 52 auteurs à 10 commits ou plus) mais **Docker requis, non lancé.** <br> **Teleport** — AGPL-3.0 lu, dernier commit 2026-08-25, 3 790 commits/12 mois, **73 auteurs à 10 commits ou plus**. Autre métier (accès aux infrastructures), non lancé |
| **Écart à l'étalon** | **Les quatre métriques du document, mesurées sur OpenBao 2.4.3 :** <br> **Chiffrement au repos — TENU, et prouvé par le test le plus brutal possible.** J'ai écrit un identifiant d'extranet avec le mot de passe `MOTDEPASSE_EN_CLAIR_XYZ789`, puis j'ai cherché cette chaîne dans **tous les fichiers du stockage disque** : **0 fichier sur 31**. Le login `hotel.deshaies` : **0 fichier sur 31**. Échantillon brut d'un fichier de stockage : `{"Value":"AAAAAQL02QZQyu4NijKMbHnIP56alYwS8LUzknneziKPIirx…` — du chiffré. Scellement Shamir 3 parts, seuil 2. <br> **Révocation effective en minutes — LARGEMENT TENUE : 123 ms** mesurés à l'horloge sur la révocation d'un jeton d'opérateur, et la relecture échoue immédiatement après. <br> **Journal d'accès complet — TENU, avec une friction réelle.** Le journal enregistre chaque opération avec son instant et son chemin. **Et les secrets y sont hachés, pas en clair** : 0 occurrence du mot de passe dans le journal, et le contenu apparaît en `"motdepasse":"hmac-sha256:9514469f3b61afdfe3e22ea34e98…"`. C'est exactement ce qu'un RGPD bien compris demande d'un journal. <br> **Cloisonnement entre clients — TENU.** Un espace KV par établissement, une politique par opérateur. Le jeton de l'opérateur de l'hôtel A lit son propre secret (`gbp-A-1234`) et **échoue** sur le client voisin |
| **Tenue des six exigences** | **Fuseau — TENUE**, le journal horodate en UTC avec nanosecondes (`2026-10-02T19:16:25.298214947Z`). <br> **Langues — sans objet.** <br> **Saisons — sans objet.** <br> **Sources locales — sans objet.** <br> **Tissu économique — NON TENUE côté client, TENUE côté prestataire.** Un coffre scellé par Shamir demande une procédure humaine de descellement après redémarrage. Aucune très petite entreprise ne fera cela ; le prestataire l'opère. Cohérent avec le mandat. <br> **Droit — TENUE**, auto-hébergeable intégralement, MPL-2.0 sans clause de service distant |
| **Verdict** | **ADOPTER TEL QUEL.** Le document écrit que cela « impose une gestion des accès confiés au niveau d'un établissement bancaire ». C'est vrai, et **cela existe, en MPL-2.0, maintenu par 13 personnes actives, et je viens de le faire tourner en huit minutes.** Reconstruire serait l'orgueil technique le plus dangereux des huit, parce qu'un coffre maison qui fuit tue le guichet 2, donc le produit |
| **Si reconstruire** | Rien. Deux frictions mesurées, à budgéter : **(a)** OpenBao 2.4.3 **refuse d'activer un dispositif d'audit par l'interface** — message exact : « cannot enable audit device via API; use declarative, config-based audit device management instead ». Le journal doit donc être déclaré dans le fichier de configuration du serveur, et non provisionné par client à chaud. **(b)** La syntaxe de cette déclaration m'a coûté **trois échecs successifs** avant que la documentation du dépôt ne la donne : il faut `audit "file" "nom" { options { file_path = … } }`, deux étiquettes et un bloc `options`. Deux pièges d'exploitation, **1 jour** pour les documenter et les figer en gabarit |
| **Coût réel à l'échelle visée** | Un processus, stockage fichier, mémoire modeste. Se co-héberge. **Le coût réel est humain** : procédure de descellement, garde des parts Shamir, rotation. **1 à 2 jours par an d'exploitation, et une astreinte**, parce qu'un coffre scellé bloque tout le produit |
| **Cran de preuve** | **A-usage** sur les quatre métriques, sorties collées. **B** pour la licence et la syntaxe d'audit |
| **Source** | Binaire officiel `github.com/openbao/openbao/releases/download/v2.4.3/bao_2.4.3_Linux_x86_64.tar.gz`, exécuté le 2026-10-02 ; `LICENSE` lu dans le dépôt cloné ; syntaxe d'audit lue dans `raw.githubusercontent.com/openbao/openbao/v2.4.3/website/content/docs/configuration/audit.mdx`, consulté le 2026-10-02. Annexe A8 |

---

### Organe transverse — Détection de langue, le verrou que le document croit bloquant

Le document fait du multilinguisme une exigence qui « disqualifie tout moteur d'extraction ou d'analyse monolingue français ». Il a raison sur le principe, et il se trompe sur la conséquence, parce qu'il n'a pas regardé.

| Champ | Contenu |
|---|---|
| **Équivalent libre trouvé** | **py3langid 0.4.0** — **BSD-3-Clause**, texte lu dans `LICENSE` (« py3langid - Language Identifier / BSD 3-Clause License / Modifications (fork): Copyright (c) 2021, Adrien Barbaresi ») et `License-Expression: BSD-3-Clause` des métadonnées. Modèle **embarqué dans le paquet**, aucun téléchargement réseau |
| **Mesure** | **Le modèle porte 142 langues, et `gcf`, `gcr` et `ht` en font partie.** Liste extraite du modèle lui-même. Sur mes trois phrases en créole guadeloupéen : **`gcf` en tête les trois fois**, suivi de `gcr` puis `ht` — exactement le bon voisinage linguistique. Sur le français, l'anglais et l'espagnol : **4/4 corrects**. Au niveau de la phrase, sur le texte extrait de la page de presse : `fr`, `fr`, **`gcf`**, `en` — **4/4** |
| **Le candidat disqualifié** | **lingua 2.1.1 — DISQUALIFIÉ sur l'exigence « Langues ».** 75 langues, **aucun créole**, vérifié par recherche sur la liste complète. Mes phrases créoles sortent en `FRENCH` (confiance 0,137), `TSONGA` (0,09) et `TSWANA` (0,172) — des langues bantoues. À comparer aux 0,987 et 0,998 obtenus sur le français. La seule chose exploitable est l'effondrement de la confiance, qui permettrait de router vers « langue inconnue » plutôt que de mentir |
| **Verdict** | **ADOPTER py3langid, avec une réserve de fragilité sérieuse.** La brique qui tient l'exigence la plus guadeloupéenne du document est un **fork à un seul mainteneur, 3 commits sur les 12 derniers mois**, dernier commit 2026-09-29. C'est le point de rupture le moins visible et le plus critique de toute la pile. **Atténuation à coût nul : le modèle est un fichier figé, on le verse au dépôt et on le fige.** 0,5 jour |
| **Cran de preuve** | **A-usage** (sorties collées pour les deux détecteurs). **B** pour les licences. **D** pour GlotLID, voir D2 |
| **Source** | Paquets PyPI installés et exécutés le 2026-10-02 ; `github.com/adbar/py3langid` cloné et `LICENSE` lu le 2026-10-02. Annexe A7 |

---

## 3. Les organes où construire est inutile — et où le document perd sa justification

La décision n°1 du document dit : « Quand aucun équivalent libre n'existe, on construit ». **Pour six organes sur huit, l'antécédent est faux.** Le document ne perd pas sa méthode, il perd sa justification sur ces six points.

| Organe | Briques libres vivantes trouvées | Verdict sur l'hypothèse de construction |
|---|---|---|
| **Découverte et collecte** | Scrapy (BSD-3-Clause, 646 commits/12 mois, 3 mainteneurs soutenus), feedparser (BSD-2-Clause), trafilatura.feeds (Apache-2.0) | **Construire = orgueil technique.** Il manque 0,5 jour de rustine sur `Crawl-delay` |
| **Extraction propre multilingue** | trafilatura (Apache-2.0, actif au jour même), htmldate (dépendance déjà présente), py3langid (BSD-3-Clause) | **Construire = orgueil technique.** F1 0,9198 mesuré, 0 plantage sur 990 pages, 25 ms/page. Il manque des heures sur l'horodatage |
| **Index et recherche** | Meilisearch noyau MIT (12 mainteneurs soutenus), Typesense GPL-3.0, Quickwit Apache-2.0 (19 mainteneurs soutenus) | **Construire un moteur = orgueil technique.** p50 = 1 ms. Il manque un pont translingue, 3 à 6 jours |
| **Provenance et traçabilité** | in-toto (Apache-2.0), OpenLineage (Apache-2.0), c2pa-rs (MIT/Apache-2.0) | **Construire la cryptographie = orgueil technique.** Chaîne signée et falsification détectée en une session. Il manque le modèle « assertion », 5 à 8 jours |
| **Orchestration de publication** | Postiz (AGPL-3.0, **36 fournisseurs**, 5 mainteneurs soutenus) | **Construire = l'erreur la plus chère du projet.** 36 fournisseurs OAuth à réécrire et à maintenir contre des interfaces qui bougent. Il manque 1 jour sur le fuseau par établissement et une décision AGPL |
| **Garde des accès confiés** | OpenBao (MPL-2.0, 13 mainteneurs soutenus), SOPS (MPL-2.0), Infisical noyau MIT | **Construire = l'orgueil le plus dangereux.** Les quatre métriques que le document pose lui-même sont tenues, mesurées, sortie collée. Il manque 1 jour de gabarit d'exploitation |

**Trois briques vivantes existent pour chacun de ces six organes.** Par la règle que le brief me donne, le document perd sa justification de construction sur ces six points.

**Et il faut aller plus loin que « inutile ».** Trois exigences guadeloupéennes que le document présente comme des disqualificateurs sont tenues par des briques existantes, sans une ligne de code :
— **Le fuseau UTC-4 sans heure d'été** n'est un problème pour personne. `zoneinfo`/`tzdata` donne `offset=-4:00, dst=0:00` toute l'année, écart de 5 h en janvier et 6 h en juillet avec Paris. `feedparser` normalise un `-0400` en UTC avec **0,00 h d'erreur** sur le calcul de fraîcheur. Ce n'est pas une exigence qui disqualifie des outils : c'est une ligne de configuration que des développeurs négligents ratent. Le document confond une exigence de **relecture** avec une exigence de **construction**.
— **Le créole guadeloupéen en détection** est déjà couvert par un paquet BSD de quelques mégaoctets, `gcf` en tête trois fois sur trois.
— **Le respect du `robots.txt`** — la première des règles de conception du degré 5b — est le comportement **par défaut** de Scrapy, et `SLEEP_TIME = 5.0` est la valeur par défaut de trafilatura.

---

## 4. Les organes où rien n'existe — le vrai périmètre de construction

C'est la partie que je considère comme la plus utile de ce retour, parce qu'elle est courte.

### 4.1 Le seul organe réellement vide : la collecte et la réponse aux avis

Quatre candidats tenus, quatre éliminés, et chacun pour un motif différent et net :
— **deux sont morts** : 0 commit sur 12 mois, l'un arrêté en août 2025, l'autre en juin 2025 avec 31 commits en tout ;
— **un est sans licence** : aucun fichier de licence dans tout l'arbre du dépôt, donc tous droits réservés, donc inutilisable commercialement, quelle que soit sa vitalité apparente ;
— **un ne fait pas le travail** : il collecte des témoignages par formulaire propre, il n'agrège pas les avis de plateformes tierces.

**Aucun des quatre ne traite le multilinguisme.** Aucun ne traite le fuseau. C'est un organe à écrire.

**Mais le périmètre de construction est plus petit que le document ne le suppose, et je peux le chiffrer** : la partie coûteuse — le parcours OAuth sous mandat, la vérification des portées, l'énumération des comptes et des établissements, le stockage des jetons — **est déjà écrite dans `gmb.provider.ts` de Postiz, en AGPL-3.0, avec la portée `business.manage` qui est exactement celle qu'il faut**. Ce fichier de 648 lignes ne contient pas un seul appel aux avis : le mot « review » y figure **une fois, dans un message d'erreur**. Le manquant, pour Google, est **deux appels HTTP**.

Périmètre de construction réel de cet organe :
| Pièce | Coût |
|---|---|
| Lecture et réponse aux avis Google, greffées sur le fournisseur GMB existant | 2 à 4 jours |
| Tri multilingue des avis à l'entrée | **déjà résolu** par py3langid, 0,5 jour d'intégration |
| Détection sous 24 h, file de réponse, journal | 5 à 8 jours |
| Les autres plateformes d'avis | **non chiffrable avant V1.** Je refuse de l'inventer |
| **Premier organe utilisable, Google seul** | **12 à 20 jours** |

### 4.2 Les deux demi-organes vides, et ils ne sont pas où le document les cherche

**Le pont translingue de l'index.** Mesuré : la requête `climatisation` ne remonte pas l'avis créole qui décrit la même panne. Vérifié à la source : **Meilisearch refuse les locales `gcf` et `hat`**, et sa liste de 70 locales valides ne contient aucun créole. Ce n'est ni Meilisearch, ni Typesense, ni Quickwit qui résoudront cela : aucun moteur lexical ne franchit la frontière de langue. **3 à 6 jours**, et c'est un composant, pas un organe.

**Le vérificateur d'ancrage de la rédaction.** Rien ne se vend et rien ne se trouve en libre qui refuse de publier une phrase non sourcée. Mon prototype de **32 lignes** attrape 2 affirmations non sourcées sur 5, et ce sont les deux bonnes. La version de production — découpage en assertions, seuil de recouvrement, refus de publier, rattachement à l'attestation in-toto — **4 à 7 jours**.

### 4.3 Et un trou que le document ne nomme pas du tout

**La génération en créole guadeloupéen.** Le document traite le multilinguisme comme un problème d'extraction et d'analyse. Il l'est, et c'est résolu. Mais l'organe « Avis » promet un **taux de réponse sous 24 h**, et répondre à un avis créole suppose d'**écrire** le créole. Détecter et écrire sont deux problèmes sans rapport. Je n'ai pu tester **aucun** générateur, et je ne fais donc aucune affirmation — mais le document n'a pas même posé la question, et elle est au cœur de sa promesse commerciale. C'est une tâche de mesure pour V0, et le risque qu'elle révèle un mur est réel.

---

## 5. Ce que le document ne voit pas — coûts d'infrastructure et de maintenance

### 5.1 L'infrastructure n'est pas le problème, et les chiffres le disent

Tout ce que j'ai mesuré pointe dans le même sens : **la pile technique de ce produit tient sur un petit serveur.**

| Organe | Mesure que j'ai prise | Besoin déduit |
|---|---|---|
| Extraction | 25,3 ms/page, 39 pages/s, 1 cœur | 200 articles/jour = **5 secondes de processeur par jour** |
| Index | 20,7 Go par million de documents (plancher), 375 docs/s | 730 000 documents sur 10 ans = **15 à 30 Go** |
| Recherche | p50 1 ms, p95 2 ms, max 3 ms sur 10 000 documents | aucun besoin de montée en charge |
| Coffre | un processus, stockage fichier | mémoire modeste |
| Publication | PostgreSQL + Redis + application | le plus gourmand de la pile |

Ordre de grandeur d'hébergement conforme, **cran C et je l'assume** : les pages de tarifs d'OVHcloud et de Scaleway sont bloquées par le mandataire de sortie, je n'ai que des comparatifs de troisième main. Ce que j'en retiens, à vérifier en B : un serveur virtuel de 8 Go de mémoire chez un hébergeur français est de l'ordre de **24 € hors taxes par mois**, un second pour la séparation du coffre et des données clientes de l'ordre de **12 €**, soit **de l'ordre de 450 à 700 € par an**, sauvegardes non comprises. **Ces chiffres sont en cran C : ils ne fondent aucune décision**, et la hausse du prix de la mémoire signalée dans ces mêmes comparatifs les rend volatils.

**Conclusion sur l'infrastructure : elle ne mérite pas d'être un sujet.** Elle ne pèse rien devant une seule journée d'ingénieur. Si le projet échoue, ce ne sera pas pour le prix d'un serveur. Le document avait raison de ne pas en faire un nœud — mais alors il faut cesser de laisser croire que le « coût au million de documents » décide de la viabilité du modèle économique, comme l'écrit la section 6 : **à l'échelle guadeloupéenne, il ne décide de rien.**

### 5.2 Le coût que le document ignore vraiment, et qui est énorme : constituer son propre juge

C'est le trou le plus grave que je trouve, et il est entièrement dû à la rigueur du document, pas à son laxisme.

Le document exige, section 9, de refuser « une mesure sur un jeu d'épreuve non figé, ou non guadeloupéen ». Il exige, section 4.2, qu'« aucune décision de construire ne se prenne sur un cran B ou moins » et que « décider de reconstruire exige un A-mesure sur le modèle repéré ». Il exige, section 5 temps 3, que le jeu d'épreuve soit « figé avant toute construction ».

**Prenons ces trois règles au sérieux ensemble, et voici ce qui se passe.**

Le seul jeu annoté que j'ai pu atteindre pour l'extraction compte **990 pages annotées à la main**, dont **438 en allemand, 240 en `.com`, 13 en `.fr`, 0 en `.gp`**. Inadmissible. Pour obtenir l'équivalent guadeloupéen, il faut annoter des pages locales segment par segment. À six minutes par page, ce qui est optimiste pour une annotation de segments, **990 pages font 99 heures, soit 13 jours-personne**. Et ce n'est que l'organe « Extraction ». Ajoutez le corpus d'avis multilingues avec vérité de terrain pour le tri des langues et la qualité des réponses, les requêtes de référence pour l'index, les pages difficiles pour la provenance.

**Estimation du jeu d'épreuve guadeloupéen complet : 25 à 40 jours-personne, dont une part exige un locuteur du créole guadeloupéen.** Le document met cette tâche en V0, une ligne parmi quatre, sans aucun chiffre. **C'est le plus gros poste de coût du projet entier, et il est invisible dans le document.** Il est aussi non compressible : sans lui, les sections 4.2, 5 et 9 interdisent littéralement de décider quoi que ce soit.

### 5.3 Le verrou logique de la doctrine de preuve

Plus gênant encore. Le temps 2 exige d'instrumenter le modèle propriétaire « par version d'essai ou compte de démonstration », et le temps 1 interdit de nommer une catégorie à la place d'un produit. Le document interdit par ailleurs d'appeler gratuit ce qui est gratuit en version d'essai.

**Pour sept de mes huit organes, je n'ai pu nommer aucun modèle propriétaire avec sa version, et encore moins l'instrumenter.** Pas par négligence : parce que cela demande une carte bancaire, une identité d'entreprise, et un accès réseau que ce conteneur n'a pas. Donc le champ « Étalon mesuré » est vide partout. Donc, par la section 4.2, **aucune décision de construire ne peut être prise** — y compris pour l'organe « Avis », où j'ai pourtant établi en B que rien d'utilisable n'existe en libre.

Le document se donne un barème qui rend sa propre décision n°1 inapplicable. **Il faut une porte de sortie explicite**, et je propose celle-ci : quand l'absence d'équivalent libre est établie en B par lecture de licences et de dates de commit — comme je viens de le faire pour l'organe « Avis » : deux dépôts morts, un sans licence, un hors sujet — **l'absence d'étalon propriétaire ne doit pas bloquer la construction**. Sinon la règle protège contre l'orgueil technique au prix de la paralysie.

### 5.4 La maintenance, chiffrée par la mesure et non par l'intuition

Le brief me demande de chiffrer. Je chiffre ce que j'ai mesuré, et je marque le reste.

**Le rythme amont, mesuré sur les 12 derniers mois** : Onyx 6 024 commits, Infisical 13 762, Teleport 3 790, Haystack 2 111, Meilisearch 2 051, OpenBao 1 350, Postiz 1 278, Scrapy 646, trafilatura 70, py3langid 3. Une pile qui retient Scrapy, trafilatura, py3langid, feedparser, Meilisearch, OpenBao, in-toto et Postiz absorbe **de l'ordre de 5 500 commits amont par an**. On ne les lit pas, mais on en subit les versions majeures.

**La concentration des mainteneurs, mesurée** (auteurs à 10 commits ou plus sur 12 mois) : OpenBao 13, Meilisearch 12, Postiz 5, Scrapy 3, in-toto 2, **trafilatura 1**, **py3langid 0**.

**Le risque n'est donc pas où on l'attend.** Les gros — OpenBao, Meilisearch, Postiz — ont un collectif. Les deux briques qui tiennent les exigences **les plus spécifiquement guadeloupéennes** du document sont celles qui ont le moins de monde derrière :
— **trafilatura**, 1 seul mainteneur soutenu, qui tient l'extraction propre, l'organe où « les outils génériques échouent » selon le document ;
— **py3langid**, 0 mainteneur soutenu et 3 commits sur l'année, qui tient à lui seul le créole guadeloupéen.

**Et c'est un risque à coût d'atténuation quasi nul**, ce qui le rend impardonnable s'il n'est pas traité : le modèle de py3langid est un fichier figé embarqué dans le paquet, et trafilatura est de l'Apache-2.0 reprenable. **Verser les deux au dépôt et figer les versions : 0,5 jour, une fois.** C'est le meilleur rapport entre risque évité et coût de tout ce que j'ai à proposer.

**Coût de maintenance annuel, estimé — et je marque la part d'estimation :**
| Poste | Base | Coût annuel |
|---|---|---|
| Correctifs et montées de version de la pile (8 briques, ~5 500 commits amont mesurés) | mesuré en amont, converti en effort : **estimation** | 10 à 15 jours |
| Ruptures d'interfaces des réseaux sociaux et plateformes d'avis | **estimation**, mais ancrée sur un fait observé : les points d'accès aux avis sont en `v4` tandis que les comptes sont déjà en `v1` | 8 à 15 jours |
| Exploitation du coffre : descellement, parts Shamir, rotation, astreinte | ancré sur mes mesures (scellement 3/2, audit déclaratif non modifiable à chaud) | 1 à 2 jours + astreinte |
| Rafraîchissement du jeu d'épreuve guadeloupéen | dérivé du coût de constitution de 5.2 | 3 à 5 jours |
| Veille d'abandon et reprise éventuelle de trafilatura ou py3langid | **cran D**, voir D5 | non chiffré |
| **Total** | | **22 à 37 jours-personne par an** |

**À comparer aux 450 à 700 € de serveur.** Le coût de ce produit est **entièrement humain**, dans un rapport de l'ordre de dix contre un. Le document, qui demande en nœud ouvert « Qui construit ? », ne demande nulle part **qui maintient**. C'est la question qui tue les produits auto-hébergés, et elle n'est pas dans la section 10.

### 5.5 Trois dettes de licence que le document ne verra qu'en V1, et qui se décident avant

— **Postiz est en AGPL-3.0.** Le document inscrit en V1 les « pièges du copyleft en service distant ». Ce n'en est pas un piège : c'est une obligation nette. Exposer un Postiz modifié par le réseau oblige à offrir le source correspondant aux utilisateurs distants. À décider **avant** la première modification, pas après.
— **Meilisearch est `MIT AND BUSL-1.1`**, et son `Additional Use Grant` est « non-production purposes only » pour les modules Enterprise Edition : partitionnement, recherche fédérée en réseau, instantanés S3. Le mono-nœud est MIT et suffit à l'échelle guadeloupéenne — mais le jour où l'on partitionne, le prix n'est ni nul ni public.
— **Onyx et Infisical ont des licences composites** : noyau MIT, répertoires `ee/` sous licence propriétaire exigeant un abonnement pour la production. Le piège est qu'on peut les déployer entièrement sans s'en apercevoir, parce que rien ne bloque techniquement.

**Et un défaut de lecture à corriger dans le document lui-même** : la section 4.4 demande « lequel des **sept** de la section 6 », alors que la section 6 en liste **huit** — l'organe de garde des accès ajouté en v3 n'a pas été recompté. De même, le titre de la section 2.2 annonce « un péage à **cinq** guichets » alors que la v4 en a ajouté un sixième et que le tableau en compte six. Deux coutures non reprises après révision, dans un document qui exige la synchronisation de ses propres pièces.

---

## 6. Verdict — ce qui est à construire, ce qui est à assembler

| | Part | Détail |
|---|---|---|
| **À assembler, sans une ligne de code nouvelle** | **~55 %** | Découverte (Scrapy + feedparser), extraction (trafilatura), index mono-nœud (Meilisearch noyau MIT), signature de provenance (in-toto), garde des accès (OpenBao), orchestration de publication (Postiz, 36 fournisseurs), détection de langue dont le créole (py3langid) |
| **À raccorder — rustines et colle, jours et non semaines** | **~20 %** | `Crawl-delay` sur Scrapy 0,5 j · horodatage complet via htmldate quelques heures · fuseau IANA par établissement dans Postiz 1 j · gabarit d'exploitation du coffre 1 j · versement au dépôt de trafilatura et py3langid 0,5 j · intégration du tri de langue 0,5 j. **Total : 4 à 5 jours** |
| **À construire vraiment** | **~25 %** | Avis Google greffés sur le fournisseur GMB existant **12 à 20 j** · pont translingue de l'index **3 à 6 j** · modèle d'assertion de provenance **5 à 8 j** · vérificateur d'ancrage de la rédaction **4 à 7 j**. **Total : 24 à 41 jours** |

**Le périmètre de construction tient en un mois à un mois et demi de travail d'une personne.** Le document raisonne comme si huit organes étaient à bâtir ; il y en a **un seul** vide — les avis — et **trois composants** manquants dans des organes par ailleurs servis.

**Les deux inversions à faire dans le document.**

*Première inversion.* La décision n°1 — « quand aucun équivalent libre n'existe, on construit » — est juste mais mal orientée, parce que le document n'a pas vérifié l'antécédent. Six organes sur huit ont trois briques libres vivantes chacun. La formulation qui tient après mesure est : **« on assemble, et on construit la couture et le vide — le vide fait un organe sur huit »**.

*Seconde inversion, et c'est la plus importante.* Le document consacre sa section 3 à six exigences guadeloupéennes présentées comme des **disqualificateurs d'outils**. Après mesure, les deux premières — le fuseau UTC-4 et le multilinguisme créole — ne disqualifient **aucun** outil sérieux : elles sont tenues par `tzdata`, `feedparser` et un paquet BSD de quelques mégaoctets. En revanche, l'exigence qui disqualifie réellement, et que le document traite en une ligne de tableau — **« Sources locales : à recenser, absentes des corpus génériques »** — est celle que je n'ai pas pu entamer d'un pouce, et celle qui coûte **25 à 40 jours-personne** d'annotation.

**Le document se croit bloqué par la technique. Il est bloqué par le corpus.** Et son propre barème de preuve, en refusant toute mesure non guadeloupéenne, le dit sans le dire.

---

## Relance 1 — anti-oubli

### Qu'as-tu oublié — trois candidats écartés et pourquoi

**1. Apache Tika.** Écarté délibérément pour l'organe « Extraction ». `JAVA_HOME` est dans l'environnement, j'aurais pu le lancer. Je ne l'ai pas fait parce que Tika résout un autre problème — extraire du texte de formats hétérogènes, PDF, DOCX, images — et non celui qui est posé, qui est **séparer le corps d'une page web de son habillage**. Le document dit « c'est là que les outils génériques échouent » : Tika est précisément l'outil générique, il n'a pas de modèle de ce qu'est un article. **Mais c'est un oubli réel pour un sous-besoin que le document ne nomme pas** : les délibérations de collectivités et les communiqués institutionnels guadeloupéens arrivent en PDF, et trafilatura ne les lit pas. Tika ou Docling sont à instrumenter en V2 pour ce cas, qui n'est pas dans la section 6.

**2. OpenSearch, et toute la famille Lucene.** Écarté pour l'organe « Index » au profit de Meilisearch, Typesense et Quickwit, parce que la règle de trois candidats tenus me l'imposait et que je voulais une brique **lançable sans Docker**. Mais c'est l'écart le plus discutable de mon retour, pour une raison précise : les analyseurs Lucene se **surchargent** — on y ajoute une liste de mots et un segmenteur pour une langue absente. Là où Meilisearch m'a répondu « Unknown value `gcf` » et m'a fermé la porte, OpenSearch aurait permis de **déclarer un analyseur créole** avec une liste de mots vides et des règles de dérivation maison. Le pont translingue que je chiffre à 3-6 jours serait peut-être partiellement remplacé par un analyseur déclaratif. **À instrumenter en V2 avant d'écrire une ligne de pont.**

**3. Chatwoot.** Écarté pour l'organe « Avis ». C'est la brique libre qui gère le plus proprement une file de conversations entrantes multicanal avec assignation, états et délais de réponse — exactement la mécanique que l'organe « Avis » demande autour des avis. Je l'ai écarté parce qu'il ne **collecte** pas les avis de plateformes, qui est le trou dur, et parce que Docker m'était fermé. **C'est peut-être une erreur d'arbitrage** : la file de réponse que je chiffre à 5-8 jours est sans doute 80 % de Chatwoot, et le manquant retomberait sur les deux appels HTTP de l'organe 7. À tenir en V3.

### Que n'as-tu pas vu — ce que tu n'as pas pu vérifier, et ce qui t'a manqué

**Ce que je n'ai pas pu vérifier, et qui change le sens de mon retour :**

1. **Aucune page guadeloupéenne réelle.** Six hôtes locaux refusés au CONNECT par le mandataire. Tous mes tests d'extraction portent sur une page que **j'ai écrite moi-même** en y plaçant les pièges structurels que je crois typiques, et sur un corpus annoté allemand à 44 %. Mon rappel de 100 % et mon F1 de 0,9198 ne sont **pas** des mesures guadeloupéennes, et la section 9 du document a raison de les refuser.
2. **Aucun avis réel, dans aucune langue.** Mes cinq avis de test sont fabriqués, et les trois créoles sont de ma mémoire — ligne D1. Toute ma démonstration sur Meilisearch et le créole repose sur du créole que je ne peux pas certifier idiomatique.
3. **Aucun modèle propriétaire instrumenté.** Le temps 2 de la méthode en six temps est resté vide sur mes huit fiches. Aucun étalon, donc aucune décision de construire valide au sens de la section 4.2.
4. **Aucune interface d'avis appelée.** Je n'ai pas appelé une seule fois Google Business Profile. Tout ce que je dis de la lecture et de la réponse aux avis est, au mieux, du B tiré du code de Postiz et du C tiré d'un résumé de moteur de recherche — la documentation primaire de Google est bloquée.
5. **Rien lancé qui exige Docker** : Postiz, Onyx, Infisical, Mixpost, Typesense. Cinq briques dont je parle sans les avoir vues tourner, et je les ai toutes maintenues en B pour cette raison.
6. **Aucune génération de texte testée**, donc aucune idée de ce que vaut un modèle libre en créole guadeloupéen. C'est au cœur de la promesse du produit.
7. **Aucun prix d'hébergement vérifié à la source.** Les deux hébergeurs français sont bloqués. Mes chiffres de serveur sont en C et ne fondent rien.

**Ce qui m'a manqué, nommément :** un démon Docker ; une sortie réseau vers les hôtes guadeloupéens, vers `developers.google.com` et vers HuggingFace ; un corpus gcf attesté ; un compte de démonstration sur un gestionnaire d'avis. **Les deux premiers sont des réglages d'environnement et débloqueraient la moitié de ce qui manque.**

### Qu'est-ce qui rendrait ce produit plus profitable — l'endroit exact où il perd de l'argent, et le geste qui le corrige

**L'endroit exact : le jeu d'épreuve guadeloupéen, tâche numéro trois de la vague V0.** Le document le pose comme « le juge de toutes les mesures à venir » et lui donne une ligne. Mes chiffres disent **25 à 40 jours-personne**, dont une part exige un locuteur du créole. C'est plus que tout le périmètre de construction réel que j'établis en section 6 — 24 à 41 jours. **Le projet paie son juge plus cher que son produit, et il entre en V0 sans le savoir.** Pire : les sections 4.2, 5 et 9 interdisent d'avancer avant qu'il existe. Le projet va donc dépenser son premier mois et demi à annoter des pages, avec un fondateur qui croit construire un produit.

**Le geste qui corrige, et il est précis : faire du jeu d'épreuve un produit vendu, et non un coût interne.**

Le registre des sources locales qualifiées — guichet, degré, licence, conditions lues, verdict, une fiche par source — que la V0 produit de toute façon, **a une valeur marchande propre, pour les mêmes clients et sans aucun des organes à construire**. Toute agence, tout office de tourisme, tout service de communication d'une collectivité guadeloupéenne a besoin de savoir quelles sources locales existent et ce qu'il est licite d'en faire. Ce registre se vend en abonnement, il se tient à jour par le même geste qui nourrit le corpus, et il **finance l'annotation au lieu de la subir**.

Trois effets mesurables :
1. **La trésorerie entre pendant V0**, c'est-à-dire pendant les 25 à 40 jours où le produit ne produit rien.
2. **Le guichet 2 s'ouvre plus tôt.** Le document dit que la proximité est la clé du mandat, et qu'« il confie ses accès parce que nous sommes son prestataire local ». On ne devient pas prestataire local avec une promesse : on le devient avec une première facture. Le registre est la facture la plus précoce possible, et elle précède de plusieurs mois le premier organe livrable.
3. **L'annotation devient du travail facturé.** Chaque fiche de qualification de source produit, dans le même mouvement, une entrée du corpus. C'est le même geste payé deux fois.

**Et le second geste, à 0,5 jour, le meilleur rapport de tout ce retour :** verser au dépôt et figer `trafilatura` et le modèle de `py3langid`. Un mainteneur soutenu pour l'un, zéro et trois commits sur l'année pour l'autre. Ce sont les deux briques qui tiennent les exigences les plus guadeloupéennes du document. Leur abandon coûterait des semaines ; s'en prémunir coûte une demi-journée.

**Je n'ai rien d'autre.** Je ne vois pas de troisième levier de rentabilité que je puisse défendre avec des chiffres de cette session.

---

## Relance 2 — preuve, étalon et guichet, ligne par ligne

### A. Lignes que j'ai testées moi-même — environnement, commande, version, date, sortie

Environnement commun : conteneur Linux 6.18.44, Python 3.11.15 en environnement virtuel créé le 2026-10-02, **toutes les exécutions datées du 2026-10-02 entre 19:10 et 19:35 UTC**. Pas de Docker. Un tiers rejoue tout ceci avec les commandes ci-dessous ; les binaires sont des publications officielles désignées par leur étiquette de version.

---

**A1 — Fuseau UTC-4 · `zoneinfo`/`tzdata` du système · A-usage**
Commande : `./venv/bin/python tz_test.py` (`ZoneInfo("America/Guadeloupe")` contre `Europe/Paris`)
```
2026-01-15T12:00:00 GP offset=-1 day, 20:00:00 dst=0:00:00 | Paris=2026-01-15T17:00:00+01:00 ecart=5:00:00
2026-07-15T12:00:00 GP offset=-1 day, 20:00:00 dst=0:00:00 | Paris=2026-07-15T18:00:00+02:00 ecart=6:00:00
2026-06-01T06:00:00 GP offset=-1 day, 20:00:00 dst=0:00:00 | Paris=2026-06-01T12:00:00+02:00 ecart=6:00:00
2026-11-30T23:00:00 GP offset=-1 day, 20:00:00 dst=0:00:00 | Paris=2026-12-01T04:00:00+01:00 ecart=5:00:00
```
Validé par moi : UTC-4 constant, `dst=0` aux quatre dates, écart 5 h/6 h conforme au document. **A-usage.**

---

**A2 — Extraction · trafilatura 2.3.0 · A-usage**
Commande : `./venv/bin/python extract_test.py` sur `pages/presse-locale.html`
```
--- texte extrait ---
Le conseil départemental de la Guadeloupe a voté mardi une enveloppe de 2,4 millions d'euros pour la réfection des routes du Nord Basse-Terre.
Les travaux démarreront après la fin de la saison cyclonique, soit après le 30 novembre, précise la collectivité.
Sé on bon nouvèl pou tout moun ki ka rédé an Nò Bastè, deklaré on konséyé.
The works will affect the RN2 between Sainte-Rose and Deshaies, local officials said.
--- metadonnees ---
  title = "Routes du Nord Basse-Terre : 2,4 millions d'euros votés"
  author = 'Rédaction locale'
  date = '2026-09-29'
--- mesure sur la page ---
  phrases de corps conservees : 4/4  (rappel 100%)
  blocs de bruit laisses       : 0/10  (part de texte propre : 100%)
  phrase creole conservee      : OUI
  phrase anglaise conservee    : OUI
  commentaire lecteur exclu    : OUI
```
Mesure comparative, commande : `./venv/bin/python tests/eval_gate.py` puis calcul propre de la matrice de confusion sur les 990 pages annotées du dépôt
```
     fast: F1=0.9198 (floor 0.9198)
 fallback: F1=0.9257 (floor 0.9257)

corpus : 990 pages reelles annotees a la main (jeu figé par le depot)
  [fast    ] precision=0.9329 rappel=0.9071 F1=0.9198  plantages=0
             tp=2753 fn=282 fp=198 tn=2684 | 25.0s pour 990 pages = 25.3 ms/page
  [fallback] precision=0.9458 rappel=0.9065 F1=0.9257  plantages=0
             tp=2791 fn=288 fp=160 tn=2678 | 34.9s pour 990 pages = 35.3 ms/page

TLD representes : [('de',438),('com',240),('org',55),('ch',43),('at',37),('net',21),('pl',18),('fr',13),('eu',11),('info',9),('uk',8),('it',5)]
pages sur domaine .gp ou guadeloupeen : 0
```
Horodatage, commande : `./venv/bin/python date_test.py`
```
source meta        : article:published_time = 2026-09-29T10:15:00-04:00  (UTC-4 Guadeloupe)
find_date defaut   : 2026-09-29
outputformat %Y-%m-%dT%H:%M:%S%z         : 2026-09-29T10:15:00-0400
trafilatura date   : '2026-09-29'
```
Validé par moi. **Étalon non opposable** : le jeu est figé par le dépôt et rejouable par un tiers, mais il **n'est pas guadeloupéen** (0 page `.gp`) et il est **le jeu d'évaluation de l'auteur de l'outil**, dont `eval_gate.py` épingle les planchers — c'est une barrière anti-régression, pas une évaluation indépendante. **A-usage pour la sortie. L'étalon redescend en B**, par la règle de la relance 2 : il n'est pas opposable.

---

**A3 — Index multilingue · Meilisearch 1.24.0 · A-usage**
Binaire : `github.com/meilisearch/meilisearch/releases/download/v1.24.0/meilisearch-linux-amd64`, `./bin/meilisearch --version` → `meilisearch 1.24.0`
```
requete                 langue cible  hits  ids trouves     ms
--------------------------------------------------------------------------
climatisation           fr            1     [(1, 'fr')]     1
climatisé               fr (variante) 1     [(1, 'fr')]     1
klimatizè               gcf           1     [(2, 'gcf')]    16
chanm prop              gcf           1     [(5, 'gcf')]    0
laplaj                  gcf           1     [(2, 'gcf')]    0
plaj                    gcf (tronque) 0     []              0
air conditioning        en            1     [(3, 'en')]     0
aire acondicionado      es            1     [(4, 'es')]     0
habitacion              es (sans accent)1   [(4, 'es')]     0
akey                    gcf (sans accent)1  [(2, 'gcf')]    0
kaz                     gcf           1     [(2, 'gcf')]    0

--- requete inter-langue ---
  'climatisation' -> [(1, 'fr')] | l'avis gcf #2 parle du meme defaut : NON RETROUVE
```
Refus de locale créole, commande `curl -X PATCH … -d '{"localizedAttributes":[{"attributePatterns":["texte"],"locales":["gcf"]}]}'`
```
{"message":"Unknown value `gcf` at `.localizedAttributes[0].locales[0]`: expected one of `af`, `ak`, `am`, `ar`, `az`, `be`, `bn`, `bg`, `ca`, `cs`, `da`, `de`, `el`, `en`, `eo`, `et`, `fi`, `fr`, `gu`, `he`, `hi`, `hr`, `hu`, `hy`, `id`, `it`, `jv`, `ja`, `kn`, `ka`, `km`, `ko`, `la`, `lv`, `lt`, `ml`, `mr`, `mk`, `my`, `ne`, `nl`, `nb`, `or`, `pa`, `fa`, `pl`, `pt`, `ro`, `ru`, `si`, `sk`, `sl`, `sn`, `es`, `sr`, `sv`, `ta`, `te`, `tl`, `th`, `tk`, `tr`, `uk`, `ur`, `uz`, `vi`, `yi`, `zh`, `zu`, …
```
Idem pour `hat`. **Aucun créole dans la liste.** Coût et latence, commande `./venv/bin/python index_cost.py`
```
documents reels extraits et indexables : 987
corpus de mesure : 10000 documents (le reel duplique x11 pour tenir la pente)
indexation : succeeded en 26.7 s  -> 375 docs/s
documents indexes : 10000
taille sur disque de la base Meilisearch entiere : 207.1 Mo
  -> extrapolation a 1 000 000 de documents : 20714 Mo  (pente lineaire supposee)
latence sur 60 requetes : p50=1.0 ms  p95=2 ms  max=3 ms
```
Validé par moi. **Réserve que je porte moi-même : les 10 000 documents sont 987 documents réels dupliqués 11 fois.** La duplication partage le vocabulaire, donc **20,7 Go/million est un plancher, pas une estimation.** Rejouable par un tiers : oui, mêmes commandes, même binaire étiqueté. Guadeloupéen : non. **A-usage pour les sorties ; l'extrapolation à un million est une projection, pas une mesure.**

---

**A4 — Provenance · in-toto 3.1.0 · A-usage**
Commandes : `in-toto-run --step-name collecte --signing-key collecteur.pem --materials … --products …`, puis vérification
```
=== attestations produites ===
collecte.5fd79b3c.link
extraction.0b89bd81.link
=== contenu d'une attestation ===
 step      : extraction
 materials : {'page-captee.html': '5c047bf7cae7d960f39e..'}
 products  : {'texte-propre.txt': '861200b924215fd9577b..'}
 keyid     : 0b89bd8176a81bbe0d11e73e00437210..
 signature : c26eb10c94f8020844d3c25a36cf05ef364647861a1da433018fe725..

  collecte.5fd79b3c.link       signature VALIDE  (role collecteur)
  extraction.0b89bd81.link     signature VALIDE  (role extracteur)
  controle negatif : cle collecteur REFUSEE sur l'attestation extraction -> SignatureVerificationError

  -- test de falsification --
  sha256 atteste : 861200b924215fd9577beefd66fa0d9944fbe84f..
  sha256 reel    : 8d4efb63f63d447ae080453dced2e46bb5464abe..
  alteration detectee : OUI - la chaine de provenance casse
```
Validé par moi, avec contrôle négatif. **A-usage.**

---

**A5 — Débit respectueux et `robots.txt` · Scrapy 2.19.0 · A-usage**
Commande : `./venv/bin/python spider.py` contre un serveur local servant un `robots.txt` avec `Crawl-delay: 2` et `Disallow: /prive/`
```
 'robotstxt/forbidden': 1,
 'robotstxt/request_count': 1,
 'downloader/response_count': 4,

=== pages effectivement recuperees ===
  t+ 4.29s  200  http://127.0.0.1:8099/
  t+ 5.92s  200  http://127.0.0.1:8099/article-2.html
  t+ 7.76s  200  http://127.0.0.1:8099/article-1.html

  /prive/secret.html interdit par robots.txt -> JAMAIS RECUPERE (robots respecte)
  delais observes entre requetes : [1.63, 1.84]  | Crawl-delay annonce = 2 s
  debit respectueux (>= 2 s) : NON — Crawl-delay NON applique par defaut
```
Validé par moi. **A-usage.**

---

**A6 — Fraîcheur et découverte de flux · feedparser 6.0.14, trafilatura.feeds · A-usage, avec une autocorrection**
```
  - Routes du Nord
      pubDate brut      : Tue, 29 Sep 2026 10:15:00 -0400
      published_parsed  : time.struct_time(tm_year=2026, tm_mon=9, tm_mday=29, tm_hour=14, tm_min=15, …)
      FRAICHEUR calculee avec published_parsed : 77.25 h
      FRAICHEUR calculee avec le vrai instant  : 77.25 h
      ECART d'erreur : 0.00 h
```
```
determine_feed (HTML d'accueil, <link rel=alternate>) -> ['https://presse.example.gp/flux.xml']
```
**Autocorrection que je signale comme telle** : mon premier essai, `find_feed_urls("http://127.0.0.1:8099/")`, a rendu `[]` et j'ai failli en conclure que la découverte de flux échouait. C'était faux. `courlan.check_url("http://127.0.0.1:8099/")` rend `None` : la protection contre les requêtes vers les adresses non publiques refuse `127.0.0.1`. La découverte fonctionne, et je l'ai prouvée sur un domaine public fictif. **A-usage, après correction d'une erreur d'interprétation qui m'était imputable.**

---

**A7 — Créole guadeloupéen · py3langid 0.4.0 contre lingua 2.1.1 · A-usage**
lingua 2.1.1 :
```
nombre de langues supportees : 75
  recherche 'CREOLE' -> ABSENT
  recherche 'HAITIAN' -> ABSENT
[fr] -> fr    OK                     top3=[('FRENCH', 0.987), ('LATIN', 0.007), ('YORUBA', 0.001)]
[gcf] -> fr   N/A-gcf-non-supporte   top3=[('FRENCH', 0.137), ('SHONA', 0.123), ('YORUBA', 0.113)]
[gcf] -> ts   N/A-gcf-non-supporte   top3=[('TSONGA', 0.09), ('YORUBA', 0.083), ('SWAHILI', 0.058)]
[gcf] -> tn   N/A-gcf-non-supporte   top3=[('TSWANA', 0.172), ('SHONA', 0.169), ('SOTHO', 0.127)]
```
py3langid 0.4.0 :
```
nombre de langues du modele : 142
codes creoles presents : ['gcf', 'gcr', 'ht']
--- ranking sur une phrase creole ---
[('gcf', -368.02), ('gcr', -403.66), ('ht', -439.85), ('wa', -494.79), ('jv', -502.97), ('cs', -505.17)]
--- ranking sur une phrase francaise ---
[('fr', -285.11), ('wa', -350.39), ('ext', -354.35), ('oc', -356.46), ('es', -359.09), ('gcf', -362.98)]
[fr] -> fr  OK | [gcf] -> gcf OK | [gcf] -> gcf OK | [gcf] -> gcf OK | [en] -> en OK | [es] -> es OK
```
Au niveau de la phrase sur le texte extrait : `fr`, `fr`, `gcf`, `en` — 4/4.
**J'ai validé moi-même l'appartenance de `gcf` au modèle** en extrayant la liste des 142 classes, pas en me fiant au résultat d'un classement. **A-usage. Mais les phrases créoles sont de ma mémoire — ligne D1 — donc la justesse du détecteur est démontrée sur un échantillon dont je ne peux pas certifier l'authenticité.**

Vérificateur d'ancrage, commande `./venv/bin/python grounding.py` :
```
  1. Plusieurs clients ont signalé une panne de climatisation en septem SOURCE [(1, 'fr')]
  2. Nos chambres sont jugées propres par la clientèle.                 SOURCE [(1, 'fr')]
  3. La plage est à proximité immédiate de l'établissement.             SOURCE [(1, 'fr')]
  4. Nous avons obtenu la note de 4,8 sur 5 au classement régional 2026 AUCUNE SOURCE -> a retirer
  5. Notre restaurant est le meilleur de Grande-Terre.                  AUCUNE SOURCE -> a retirer
  affirmations non sourcees : 2/5
  cout du verificateur : 32 lignes de python, index deja en place.
```
**A-usage**, mais **sur un brouillon que j'ai écrit moi-même en y plaçant les deux cas à attraper.** C'est une démonstration de faisabilité, pas une mesure de performance. Un tiers la rejoue ; elle ne prouve pas un taux.

---

**A8 — Garde des accès confiés · OpenBao 2.4.3 · A-usage**
Binaire : `github.com/openbao/openbao/releases/download/v2.4.3/bao_2.4.3_Linux_x86_64.tar.gz`, `./bin/bao version` → `OpenBao v2.4.3 (ef854342df72dba6ecfbdd3f130e251941ba7dca), built 2025-10-22T20:21:42Z`

Cloisonnement et révocation, serveur en mode développement sur 127.0.0.1:8200 :
```
=== 1. audit log activation ===
* cannot enable audit device via API; use declarative, config-based audit device management instead
=== 2. cloisonnement par client ===
Success! Enabled the kv-v2 secrets engine at: client-gwada-hotel-A/
Success! Enabled the kv-v2 secrets engine at: client-gwada-gite-B/
=== 5. jeton operateur + preuve de cloisonnement ===
-- lecture AUTORISEE sur son propre client: gbp-A-1234
-- lecture du client voisin (doit echouer): Error making API request.
=== 6. revocation effective : chronometre ===
revocation API: 123 ms
-- relecture apres revocation: Error making API request.
```
Chiffrement au repos et journal, serveur en stockage fichier sur 127.0.0.1:8201 avec `audit "file" "journal-mandats" { options { file_path = "./bao-audit.log" } }` :
```
=== init : scellement Shamir 3 parts / seuil 2 ===
part0=tQP4aXtAPHtdar... part1=4a2VdQVx50PR6n... part2=aTvmKMm0QPk9J8...
Sealed          false
Storage Type    file
=== PREUVE chiffrement au repos ===
fichiers disque contenant le mot de passe en clair : 0
fichiers disque contenant le login en clair       : 0
total fichiers de stockage                        : 31
-- echantillon brut :
{"Value":"AAAAAQL02QZQyu4NijKMbHnIP56alYwS8LUzknneziKPIirxIXzf2pIrwX8MMuuQDJHgnDGtBf1ZTs/kYKfO5Tztz/GMKIDdZaddAihtmAfRreUsfiFIn2YZ5917Gsrz7ahJt9Ub1C8DDdy/eHDXEFwmSsCTOPQ4GRUoWnagug
=== journal d'acces declaratif ===
7 bao-audit.log
2026-10-02T19:16:25.298214947Z	update	sys/mounts/client-A
2026-10-02T19:16:25.412685155Z	create	client-A/data/booking-extranet
secret en clair dans le journal ? occurrences = 0
login hache : {"data":{"login":"hmac-sha256:5a25c4a69d0dd56c3076bf99c04e520f017b40deb8291a45b45fa28d5890aa4e","motdepasse":"hmac-sha256:9514469f3b61afdfe3e22ea34e98
```
Validé par moi, les quatre métriques du document. **A-usage.** La syntaxe du bloc d'audit m'a demandé **trois échecs** (`audit type must be specified`, puis `audit path must be specified`, puis `file_path is required`) avant que je lise la documentation du dépôt — friction réelle, et je la rapporte comme telle.

---

### B. Lignes en cran B — document primaire lu, avec URL et date, mais rien lancé

Toutes consultées le **2026-10-02**. Les dates de commit et les comptes d'auteurs sont **mesurés par moi** avec `git log` sur des clones faits dans cette session, et non recopiés d'une page de dépôt.

| Ligne | Ce que j'ai lu | Ce que je n'ai pas fait |
|---|---|---|
| Scrapy BSD-3-Clause ; trafilatura Apache-2.0 ; feedparser BSD-2-Clause ; py3langid BSD-3-Clause ; in-toto Apache-2.0 ; OpenBao MPL-2.0 ; SOPS MPL-2.0 ; Typesense GPL-3.0 ; Quickwit Apache-2.0 ; OpenLineage Apache-2.0 ; c2pa-rs MIT/Apache-2.0 ; Haystack Apache-2.0 ; Teleport AGPL-3.0 ; Postiz AGPL-3.0 ; Mixpost MIT | Texte du fichier `LICENSE` ouvert dans chaque dépôt cloné | — |
| Meilisearch `MIT AND BUSL-1.1` ; grant « non-production purposes only » ; Change License MIT ; Change Date 4 ans ; modules EE = sharding, network, S3 | `LICENSE` et `LICENSE-EE`, plus la liste des fichiers `enterprise_edition` dans l'arbre | — |
| Onyx noyau MIT + Onyx Enterprise License sur `ee/` ; Infisical noyau MIT + `ee/LICENSE` | `LICENSE` et `backend/ee/LICENSE` | **Non lancés**, Docker |
| Postiz : 36 fournisseurs, `gmb.provider.ts` porte `business.manage`, les hôtes `mybusinessaccountmanagement/v1`, `mybusinessbusinessinformation/v1`, `mybusiness/v4/localPosts`, `businessprofileperformance/v1` ; **1 seule occurrence de « review », dans un message d'erreur** ; `User.timezone` de type `Int` | Arbre git, code du fournisseur, schéma Prisma | **Non lancé** |
| Avis : reviewsup.io 0 commit/12 mois ; google-reviews-manager 0 commit/12 mois ; **google-review-autoreply sans aucun fichier de licence dans tout l'arbre** ; three-things-reviews AGPL-3.0 mais collecteur de témoignages | `git log --since`, `git ls-tree -r` sur l'arbre complet | **Aucun lancé** |
| Syntaxe du bloc d'audit OpenBao | `raw.githubusercontent.com/openbao/openbao/v2.4.3/website/content/docs/configuration/audit.mdx` | — |

### C. Lignes en cran C — je les isole et elles ne fondent rien

| Ligne | Pourquoi C | Ce qui la ferait monter en B |
|---|---|---|
| Points d'accès de lecture et de réponse aux avis Google (`accounts.locations.reviews`, `updateReply`), portées OAuth, processus de validation | **Résumé de moteur de recherche.** `developers.google.com` bloqué par le mandataire. La seule confirmation de première main que j'aie est la portée `business.manage` lue dans le code de Postiz, ce qui est cohérent mais ne vaut pas la documentation | Lecture de la documentation primaire, et dépôt d'une demande d'accès réelle en V1 |
| Prix d'hébergement français : ~24 €/mois pour 8 Go, ~12 € pour 4 Go, dédié à partir de 49 €, hausse mémoire de 30 % | **Comparatifs de blogs.** `www.ovhcloud.com` et les pages de tarifs sont bloquées | Pages de tarifs des hébergeurs, ou un devis |
| « Postiz prend en charge plus de 30 réseaux » | Page marketing et billets | **Déjà remplacé par mon propre comptage en B : 36 fichiers de fournisseur dans l'arbre git.** La ligne C est périmée, je la garde pour mémoire |

### D. Reclassement final, ligne par ligne

| Ligne | Classement | Sortie collée ? | Note |
|---|---|---|---|
| Fuseau UTC-4, écarts 5 h/6 h | **A-usage** | oui, A1 | |
| trafilatura : rappel 4/4, 0/10 bruit, créole conservé | **A-usage** | oui, A2 | page écrite par moi |
| trafilatura : précision 0,9329 / rappel 0,9071 / F1 0,9198 / 25,3 ms/page | **A-usage** pour la sortie, **B** pour l'étalon | oui, A2 | **étalon non opposable : 0 page `.gp`, et c'est le jeu de l'auteur de l'outil. Redescendu en B par la règle de la relance 2** |
| Composition du corpus : 438 `.de`, 13 `.fr`, 0 `.gp` | **A-usage** | oui, A2 | compté par moi |
| Perte du décalage UTC-4 par trafilatura, récupérable via htmldate | **A-usage** | oui, A2 | |
| Meilisearch : créole lexical oui, `plaj` non, translingue non | **A-usage** | oui, A3 | |
| Meilisearch : aucune locale créole dans les 70 valides | **A-usage** | oui, A3 | |
| Meilisearch : 375 docs/s, 207,1 Mo pour 10 000, p50 1 ms | **A-usage** | oui, A3 | |
| Meilisearch : 20,7 Go par million | **projection, pas mesure** — je la laisse en A-usage adossée à une réserve explicite | oui, A3 | plancher, corpus dupliqué |
| in-toto : signatures valides, contrôle négatif, falsification détectée | **A-usage** | oui, A4 | |
| Scrapy : robots respecté, `Crawl-delay` non appliqué | **A-usage** | oui, A5 | |
| feedparser : fraîcheur à 0,00 h d'erreur | **A-usage** | oui, A6 | |
| `determine_feed` découvre le flux ; le `[]` initial venait de la protection SSRF | **A-usage** | oui, A6 | autocorrection signalée |
| lingua : 75 langues, aucun créole, gcf → FRENCH/TSONGA/TSWANA | **A-usage** | oui, A7 | |
| py3langid : 142 langues, `gcf` présent, gcf 3/3 | **A-usage** | oui, A7 | échantillon créole de ma mémoire, D1 |
| Vérificateur d'ancrage : 2/5 non sourcées attrapées, 32 lignes | **A-usage** | oui, A7 | brouillon écrit par moi : faisabilité, pas taux |
| OpenBao : chiffrement au repos 0/31, révocation 123 ms, cloisonnement, journal haché | **A-usage** | oui, A8 | |
| OpenBao : audit non activable par l'interface | **A-usage** pour le message, **B** pour la syntaxe correcte | oui, A8 | |
| Toutes les licences SPDX, dates de dernier commit, comptes d'auteurs | **B** | sorties de `git log` collées dans les fiches | lues et mesurées par moi dans la session |
| Postiz : 36 fournisseurs, `business.manage`, 1 « review » en message d'erreur, `timezone Int` | **B** | oui dans les fiches | **non lancé, donc jamais A** |
| Les quatre candidats de l'organe « Avis » : morts, sans licence, hors sujet | **B** | oui dans la fiche | |
| Points d'accès avis Google, prix d'hébergement | **C** | non | isolées, ne fondent rien |
| D1 à D7 | **D** | non | déclarées en tête |

**Aucune ligne classée A ne l'est sans sortie collée.** Les deux cas discutables — le F1 de trafilatura et l'extrapolation du Go par million — je les ai **moi-même rétrogradés ou assortis d'une réserve écrite**, sans attendre la relance.

### Pour chaque acteur cité comme faisant déjà le travail : par quel guichet ?

**Je n'en cite aucun.** Le document interdit de nommer un acteur sans nommer son guichet ou le déclarer inconnu, et interdit de nommer une catégorie à la place d'un produit. N'ayant instrumenté aucun produit propriétaire, je n'en nomme aucun, et le champ « Étalon mesuré » est vide sur mes huit fiches. La seule chose que je puisse dire est **documentée et non supposée** : Postiz accède à Google Business Profile par le **guichet 3**, interface ouverte sur demande, et je le sais parce que **j'ai lu les portées OAuth et les hôtes appelés dans son code source**, pas parce que je le suppose.

---

## Les cinq colonnes de fin de réponse

### 1. MCP à installer

| MCP | Ce qu'il débloque | Prérequis |
|---|---|---|
| Un serveur MCP de récupération web avec sortie **brute**, non résumée | Le trou n°1 de cette session : constituer le jeu d'épreuve guadeloupéen. `WebFetch` rend du texte interprété par un modèle, inutilisable pour mesurer un extracteur. Il faut l'octet d'origine | **Levée du filtrage de sortie sur les hôtes guadeloupéens.** Sans cela, aucun MCP ne sert |
| MCP Docker, ou un démon Docker accessible | Postiz, Onyx, Infisical, Mixpost, Typesense, Chatwoot — cinq briques que j'ai dû laisser en B | Socket Docker, et le droit de lancer des conteneurs |
| MCP PostgreSQL | Le client 16.14 est présent sans serveur. Postiz et Infisical en ont besoin | Un serveur PostgreSQL |
| MCP Google Business Profile, ou un client authentifié | Les deux appels manquants de l'organe « Avis ». Rien ne sera mesurable sans compte | Compte Google Business vérifié, portée `business.manage`, validation d'accès |

### 2. Logiciels manquants

| Manquant | Pourquoi il bloque |
|---|---|
| **Démon Docker** | A bloqué cinq briques. Le manque le plus coûteux de la session |
| **Serveur PostgreSQL** | Client seul, aucun serveur |
| **Pandoc** | Absent, confirmé. Non bloquant pour mon angle |
| **Accès réseau aux hôtes guadeloupéens, `developers.google.com`, `huggingface.co`** | Pas un logiciel, une politique. Mais c'est le vrai blocage : il rend le jeu d'épreuve guadeloupéen inaccessible, donc rend inapplicables les sections 4.2, 5 et 9 du document |
| **Un corpus de créole guadeloupéen attesté** | Tout mon créole est de ma mémoire, ligne D1 |

### 3. Outils déjà disponibles et non exploités

| Disponible | Ce qu'il débloquerait |
|---|---|
| **Java**, `JAVA_HOME` défini | Apache Tika pour les PDF institutionnels et les délibérations de collectivités — un besoin réel que la section 6 du document ne nomme pas |
| **Node 22.22** | Les fournisseurs de Postiz en TypeScript s'exécutent unitairement sans Docker. Le fournisseur GMB se teste en isolation, avec des jetons factices, avant de décider de construire |
| **`git` avec clone partiel** | `--filter=blob:none` m'a donné licences, dates de commit et comptes de mainteneurs en secondes. **C'est l'outil de qualification de vitalité le plus rentable de la session, et il devrait être la première commande de chaque fiche-organe de V2** |
| **`py3langid`, déjà installé et éprouvé** | Tient à lui seul l'exigence « Langues » du document |
| **`in-toto` + `securesystemslib`** | La chaîne de provenance peut être branchée dès V0 sur la constitution du jeu d'épreuve, et pas en V2. Chaque page annotée arriverait attestée — le jeu d'épreuve serait alors lui-même rejouable, ce que la section 5 exige sans dire comment |

### 4. IA existantes qui font ce travail, et à quel prix

**Toute cette colonne est en cran C ou D, et je le marque.** Je n'ai souscrit à rien, appelé aucune interface payante, et le document interdit d'appeler gratuit ce qui est gratuit en version d'essai.

| Ce qui fait le travail aujourd'hui | Prix | Cran |
|---|---|---|
| Modèles de langue propriétaires pour la rédaction sourcée et la réponse aux avis, facturés au million de jetons | **Non vérifié dans cette session.** Je ne cite aucun chiffre que je n'ai pas lu aujourd'hui | **D** |
| Gestionnaires d'avis en logiciel-service, qui empruntent vraisemblablement le guichet 1 ou le guichet 2 | **Prix inconnu, guichet inconnu.** Le document interdit de supposer : je déclare inconnu | **D** |
| Services de collecte web facturés à l'appel | Non vérifié | **D** |
| **Ce qui fait réellement le travail, et que j'ai mesuré** : py3langid pour la détection, trafilatura pour l'extraction, Meilisearch pour l'index, OpenBao pour la garde | **0 €** de licence, licences libres lues dans les fichiers, auto-hébergeables. Coût réel = **22 à 37 jours-personne par an** de maintenance, section 5.4 | **A-usage** et **B** |

**La vraie réponse de cette colonne** : pour sept organes sur huit, ce qui fait le travail aujourd'hui n'est pas une intelligence artificielle facturée, c'est une bibliothèque libre que personne n'a pris la peine d'assembler pour la Guadeloupe. Le prix n'est pas un abonnement, c'est un mois et demi de travail d'assemblage et 22 à 37 jours par an d'entretien.

### 5. Futurs possibles à douze mois ⏳

| ⏳ | Ce qui pourrait arriver | Pourquoi j'en parle, et avec quelle réserve |
|---|---|---|
| ⏳ | **Meilisearch élargit son périmètre Enterprise Edition** et fait glisser sous BUSL des fonctions aujourd'hui MIT | Le mécanisme est déjà en place, les paramètres BUSL sont écrits et la frontière est fixée par un simple marquage de fichier. Rien n'annonce ce glissement, je ne le prédis pas : je signale qu'il ne coûterait rien à l'éditeur. **Parade mesurée : Quickwit, Apache-2.0, 19 mainteneurs soutenus** |
| ⏳ | **Retrait de l'ancien hôte `mybusiness.googleapis.com/v4`**, qui porte les avis | **Fait observé** dans le code de Postiz : comptes et établissements sont déjà passés en `v1` sur des hôtes séparés, les avis et la publication restent en `v4`. Une migration de la `v4` casserait l'organe « Avis » le jour de son arrivée |
| ⏳ | **Abandon ou mise en sommeil de `py3langid`** | **0 mainteneur soutenu, 3 commits sur 12 mois** — c'est mesuré, pas supposé. La brique qui tient le créole guadeloupéen est la plus fragile de la pile. Parade à 0,5 jour : verser le modèle au dépôt |
| ⏳ | **Un détecteur ou un segmenteur créole arrive en libre**, par exemple issu de GlotLID | Ligne D2, invérifiable ici. S'il arrive, le pont translingue de l'index se simplifie et les 3 à 6 jours tombent |
| ⏳ | **Mixpost quitte l'état de quasi-arrêt, ou le confirme** | 23 commits sur 12 mois, dernier commit 2026-03-16 : à six mois, le verdict sera clair dans un sens ou dans l'autre. À reclasser alors |
| ⏳ | **Un modèle libre capable d'écrire le créole guadeloupéen de façon publiable** | C'est le pari caché du produit, et il n'est nulle part dans le document. Je n'ai aucune donnée. **À mesurer en V0, avant toute promesse commerciale sur le taux de réponse sous 24 h** |
