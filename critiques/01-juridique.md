# Critique adversariale — angle droit et voies d'accès aux données

Cible : `00-PROMPT-DE-LANCEMENT.md` v4 du 2 octobre 2026, sections 2.1 à 2.7.
Lecteur : agent adversarial. Mandat : casser, pas valider.
Date de toutes les consultations citées : **2 octobre 2026**.

**Avertissement d'outillage, qui plafonne ce retour.** `legifrance.gouv.fr`, `curia.europa.eu`,
`eur-lex.europa.eu`, `bailii.org`, `tripadvisor.com` et `tripadvisor.mediaroom.com` sont **bloqués
en sortie réseau** pour l'outil de récupération directe de cette session. J'ai atteint EUR-Lex
uniquement par la récupération côté serveur du MCP EXA, et les textes du Code de la propriété
intellectuelle et du Code de la consommation par des miroirs (Doctrine, Pappers Justice, senat.fr,
culture.gouv.fr, hr-infos.fr pour le JO). **Conséquence opposable : tout numéro d'article et toute
date d'entrée en vigueur cités ici doivent être relus sur Légifrance avant signature.** Je le dis
en tête parce que c'est une limite de preuve, pas un détail.

---

## 1. Mes lignes en cran D — déclarées avant le contenu

Sept lignes. Aucune ne fonde une conclusion ; chacune est une piste.

| # | Affirmation | Pourquoi D |
|---|---|---|
| **D1** | Le parasitisme (art. 1240 C. civ.) est une action autonome qui survit à l'échec d'une action en droit sui generis : un demandeur débouté faute d'investissement substantiel peut encore gagner sur le terrain du « sillage ». | Proposition de droit civil français tirée de ma mémoire. **Aucune décision citée.** Je n'ai vérifié aucun arrêt de parasitisme pur sur du scraping. |
| **D2** | L'issue finale de *Ryanair c/ PR Aviation* devant le Hoge Raad après l'arrêt préjudiciel de 2015. | Je ne sais pas si Ryanair a finalement gagné sur le terrain contractuel. L'arrêt CJUE renvoyait au droit national. **Non vérifié.** Donc : « Ryanair a gagné » est une ligne que je n'écris pas. |
| **D3** | Les bases d'avis de Booking.com et de TripAdvisor satisfont au critère d'investissement substantiel de l'art. L341-1 CPI et sont donc protégées par le droit sui generis. | Très plausible par analogie avec l'arrêt leboncoin (lui en cran B), mais **jamais jugé pour ces plateformes** à ma connaissance. Piste forte, pas un fait. |
| **D4** | Les conditions d'utilisation de TripAdvisor interdisent l'extraction automatisée. | Les extraits de recherche suggèrent que le **partage de compte** est interdit. Je n'ai **jamais lu la clause**. Domaine bloqué en sortie. À ne pas utiliser, même comme C. |
| **D5** | Sanction des pratiques commerciales trompeuses : art. L132-2 C. consom., 2 ans d'emprisonnement et 300 000 € d'amende. | Mémoire, non corroborée dans cette session. |
| **D6** | Le droit moral de l'auteur d'un avis (art. L121-1 CPI) est inaliénable et perpétuel, et aucune CGU de plateforme ne peut le purger au profit d'un tiers republiant. | Doctrine française standard, de mémoire. **Article non lu de première main ici.** |
| **D7** | Une analyse d'impact (AIPD, art. 35 RGPD) est obligatoire pour ce traitement. | Mon raisonnement sur les critères, croisé avec la liste CNIL des traitements à AIPD obligatoire — **liste non ouverte**. |

Le reste de ce document est en A-usage, B ou C, et chaque ligne porte son cran.

---

## 2. Ce qui est **faux** dans le document

### F1 — « Le mandat du titulaire (guichet 2) est une voie licite » : faux comme décrit, et le document se trompe de mécanisme

Le document écrit (§2.2, ligne guichet 2) : « L'établissement possède l'accès à ses propres avis
par son extranet. Il mandate un prestataire. » Et §2.7 : « Il confie ses accès ». Et §6, organe
« Garde des accès confiés ». Et §V3 : « comment on détient les identifiants d'un client sans trahir
sa confiance ». La chaîne est claire : le guichet 2 du document = **remise des identifiants**.

**Première erreur, de structure contractuelle.** Le mandat (art. 1984 C. civ.) est licite *entre
l'hôtelier et le prestataire*. Mais un mandat entre A et B ne crée aucun droit contre C. Ce qui
décide si l'hôtelier *peut* ouvrir son accès à un tiers, c'est le contrat entre l'hôtelier et la
plateforme — *res inter alios acta*. Le document traite une question de droit des contrats avec la
plateforme comme si c'était une question de droit du mandat. Le guichet 2 n'est donc pas « une voie
licite » : c'est une voie dont la licéité dépend entièrement d'un document que le document n'a pas lu.

**Deuxième erreur, et elle est frontale : Google interdit explicitement ce que le guichet 2 décrit,
tout en ouvrant une autre porte que le document classe ailleurs.**

Source primaire — *Business Profile third-party policies*, Google,
<https://support.google.com/business/answer/7353941?hl=en>, consultée le 2 octobre 2026. **Cran B.**
Passages, verbatim :

> « You're responsible for ensuring the integrity and security of your end customers' account
> credentials. Here are some best practices […] If a client already has a Business Profile, ask them
> to invite you as a manager, not as an owner. **Do not share passwords with your clients.** »

> « all end customers must retain ownership or co-ownership of their Business Profile at all times. »

> « **To respond to reviews on behalf of the end customer, you must have an explicit approval.
> Verbal consent isn't sufficient.** If there's a conflict between the third-party and the merchant,
> you must provide a written or digital proof of consent. »

Source primaire — *Business Profile APIs policies*, Google,
<https://developers.google.com/my-business/content/policies>, consultée le 2 octobre 2026. **Cran B.**

> « You can only use the Business Profile APIs to create, manage, and report on business listings
> that you either own or are authorized to manage on behalf of the business owner »

> « **Any automatic or programmatic use of Business Profile by agencies or end-clients requires them
> to use their own Business Profile project. You cannot provide indirect access to your Business
> Profile project.** End users of your Business Profile APIs need to manually sign in to use it.
> They're not allowed automatic access to make manual or programmatic changes to their accounts. »

Source primaire — *Locations*, Google, <https://developers.google.com/my-business/content/locations>,
consultée le 2 octobre 2026. **Cran B.**

> « If a third party's client needs access to Business Profile APIs, **the third party shouldn't
> request access on their client's behalf. Instead, the client needs to apply for access themselves.** »

> « if you manage a large number of locations, **or you currently share your username and password
> with other users**, we recommend that you transition to use location groups as a safer way to work
> together. »

**Ce que cela fait au document.** La voie sanctionnée par Google est : l'hôtelier reste
propriétaire, invite le prestataire comme *manager*, et le prestataire accède par jeton OAuth. C'est
**le guichet 3 du document** (« API ouverte sur demande »), pas le guichet 2. Le guichet 2 — remise
d'identifiants — est précisément la pratique dont la politique de Google détourne les agences. Et
l'organe « Garde des accès confiés », que le document qualifie de « condition du guichet 2, donc de
tout le produit », est donc un organe construit pour détenir **ce qu'il ne faut pas détenir**. C'est
un budget d'ingénierie dépensé sur un anti-modèle contractuel. La correction n'est pas cosmétique :
l'organe doit devenir une **garde des autorisations déléguées** — garde de jetons, portée, rotation,
révocation, journal — ce qui est un objet technique différent, plus simple et moins risqué.

**Troisième erreur : chez Booking.com, il n'existe aucun emplacement contractuel pour un « mandat ».**

Source primaire — *General Delivery Terms*, Booking.com,
<https://admin.booking.com/hotelreg/terms-and-conditions.html>, consultée le 2 octobre 2026.
**Cran B.** Définitions, verbatim :

> « "Extranet" means the online systems of Booking.com **which can be accessed by the Accommodation**
> (after inputting its username and password), for, among other things, uploading, changing,
> verifying, updating and/or amending the Accommodation Information and reservations. »

> « "Connectivity Provider" means a professional software and service provider who offers
> Connectivity Services to Accommodations, and **who has concluded a valid and continuing
> connectivity partnership agreement with Booking.com**. »

Source primaire — *Managing contracting flow*, Booking.com Connectivity,
<https://developers.booking.com/connectivity/docs/contracting-api/managing-contracts>, consultée le
2 octobre 2026. **Cran B.** Le flux sanctionné, verbatim :

> « Send a request to `POST /partners/request_access` endpoint […] **Share the link received in the
> API response with the partner to login to their account and authorise the connection.** »

Source primaire — *Setting up and working with a connectivity provider*, Booking.com,
<https://partner.booking.com/en-us/help/channel-manager/setup/setting-and-working-connectivity-provider>,
consultée le 2 octobre 2026. **Cran B.** Le parcours réel : l'hôtelier cherche dans une liste de
fournisseurs **recommandés par Booking**, signe un accord avec lui, puis coche les conditions.

L'Extranet est, par définition contractuelle, accédé *par l'établissement*. La seule catégorie de
tiers nommée et outillée est le **Connectivity Provider**, qui doit avoir conclu un accord de
partenariat de connectivité **avec Booking.com**. Autrement dit : chez Booking, ce que le document
appelle guichet 1 (« hors de portée au départ. À réexaminer à trois ans ») est **la seule voie
structurée**, et le guichet 2 (« notre voie principale ») **n'existe pas comme catégorie**. Le
tableau §2.2 est donc inversé pour la plateforme la plus importante du secteur hôtelier.

**Ce que je n'ai pas trouvé, et je le dis.** Je n'ai **pas** mis la main sur une clause des GDT
interdisant expressément à l'hôtelier de communiquer ses identifiants Extranet à un tiers. Les GDT
complets ne sont délivrés, en PDF, qu'au contact contractuel qui les demande depuis l'Extranet
(source : <https://partner.booking.com/en-us/help/legal-security/terms-local-laws/about-our-accommodation-agreement-general-delivery-terms-gdt>,
consultée le 2 octobre 2026, cran B). Ce qui manque pour conclure : un hôtelier guadeloupéen
acceptant de demander son PDF. **Mais l'absence de cette clause ne sauve pas le guichet 2** : il
reste que le document a posé comme acquis (« l'établissement possède l'accès… il peut mandater ») ce
qui est une supposition non vérifiée, et que l'architecture contractuelle effective pointe ailleurs.

**Quatrième erreur, économique.** Le document chiffre le guichet 2 : « Faible — contrat de mandat ».
Faux sur deux points, sourcés ci-dessus : (a) Google impose que **le client lui-même** demande son
propre projet d'API — donc un onboarding par client, pas un mandat type signé une fois ; (b) Booking
impose un accord de partenariat de connectivité avec Booking — donc le coût du guichet 1. La ligne
« coût faible » est en cran C sans source et elle est la base du modèle économique.

**Ce que je n'ai pas qualifié du tout : TripAdvisor.** Domaines bloqués en sortie. Les *Hospitality
Master Terms and Schedules* et les CGU françaises n'ont pas été lues. TripAdvisor reste **non
qualifié**, et une plateforme non qualifiée ne peut pas figurer dans un tableau de guichets.

---

### F2 — *Ryanair c/ PR Aviation* : la décision existe, la référence manquait, et l'interprétation est fausse deux fois

**Référence exacte, obtenue en texte intégral.** Arrêt de la Cour (deuxième chambre) du
**15 janvier 2015**, affaire **C-30/14**, *Ryanair Ltd c. PR Aviation BV*, sur renvoi préjudiciel du
Hoge Raad der Nederlanden. Lu intégralement sur EUR-Lex, CELEX **62014CJ0030**,
<https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:62014CJ0030>, consulté le
2 octobre 2026. **Cran B.** Le document le citait de mémoire sans numéro d'affaire ni formation.

**Dispositif, verbatim :**

> « Directive 96/9/EC of the European Parliament and of the Council of 11 March 1996 on the legal
> protection of databases must be interpreted as meaning that **it is not applicable to a database
> which is not protected either by copyright or by the sui generis right** under that directive, so
> that Articles 6(1), 8 and 15 of that directive **do not preclude** the author of such a database
> from laying down contractual limitations on its use by third parties, **without prejudice to the
> applicable national law**. »

**Erreur n° 1 — le document transforme une décision négative en règle positive.**

Le document écrit : « Les conditions d'utilisation **suffisent à interdire**, même sans protection
légale sur le recueil. » La Cour n'a pas dit cela. Elle a dit que la directive **ne fait pas
obstacle** — formule négative — et elle a ajouté, deux fois, la réserve du droit national. §44,
verbatim :

> « as regards a database to which Directive 96/9 is not applicable, its author is not eligible for
> the system of legal protection instituted by that directive, so that **he may claim protection for
> his database only on the basis of the applicable national law**. »

Entre « rien en droit de l'Union ne vous empêche d'essayer » et « les CGU suffisent », il y a toute
la question de la formation du contrat, de l'opposabilité des CGU à un robot qui n'a rien accepté,
des clauses abusives, de la preuve de l'acceptation. Dans l'espèce, l'acceptation était **cochée**
(§16 : « Access to that website presupposes that the visitor to the site accepts the application of
Ryanair's general terms and conditions **by ticking a box** to that effect »). Le document a perdu
cette condition en route. Et son propre §4.2 dispose : « Aucun choix de guichet ne se prend sur un
cran D » — or le degré 5c est écarté en partie sur cette lecture.

**Erreur n° 2, la plus coûteuse — le document ne rapporte que la moitié du raisonnement, et la
moitié qu'il tait joue contre lui.**

Le raisonnement de la Cour est **symétrique**. §39-40, verbatim :

> « Articles 6(1), 8 and 15 thereof, **which establish mandatory rights for lawful users of
> databases**, are not applicable to a database which is not protected either by copyright or by the
> sui generis right »

> « Articles 6(1), 8 and 15 of Directive 96/9, which **confer rights on lawful users and, in so
> doing, limit those of the person who created the database**, are applicable only in respect of a
> database over which its author has rights to title »

Et §38, sur l'art. 15 : « any contractual provision contrary to it [is] null and void ».

**Lisez la contraposée.** Si une base **est** protégée par le droit sui generis, alors l'art. 8(1)
s'applique — en droit français, art. **L342-3 1° CPI** : le titulaire « ne peut interdire
l'extraction ou la réutilisation d'une partie non substantielle […] par la personne qui y a
licitement accès » — et l'article ajoute, verbatim : « **Toute clause contraire au 1° ci-dessus est
nulle.** » (texte lu sur <https://www.senat.fr/leg/pjl97-344.html>, travaux de transposition de la
directive 96/9, consulté le 2 octobre 2026, cran B ; numérotation actuelle à relire sur Légifrance.)

Conséquence directe : le document classe la protection sui generis **uniquement comme circonstance
aggravante** (§2.3, degré 5c : « ou recueil protégé par le droit sui generis »). Or elle est **aussi**
la source de droits impératifs de l'utilisateur licite, et une CGU qui prétend tout interdire à un
utilisateur licite est **nulle** pour les parties non substantielles. L'échelle de degrés du document
est construite sur **un seul axe** — ce que disent les CGU — et elle se trompe donc sur toute source
où les deux axes divergent. C'est un défaut de conception de la grille, pas une nuance.

Je ne surévalue pas cette ouverture : elle est étroite. L'art. 7(5) de la directive, art. **L342-2
CPI**, interdit « l'extraction ou la réutilisation **répétée et systématique** de parties […] non
substantielles […] lorsque ces opérations excèdent manifestement les conditions d'utilisation normale
de la base » — ce qui est la définition d'un collecteur continu (voir F5). Et la qualité
d'« utilisateur licite » est elle-même disputée. Mais une grille qui ne voit pas l'axe mis-trie.

**Erreur n° 3 — l'arrêt ne porte pas sur le degré 5b.** L'espèce concernait un site dont les CGU
**interdisaient expressément** le screen scraping commercial (§16, verbatim : « The use of automated
systems or software to extract data from this website […] for commercial purposes, ('screen
scraping') is prohibited unless the third party has directly concluded a written licence agreement
with Ryanair »). L'arrêt ne dit **rien** d'un site aux CGU muettes. Le document en fait l'épine
dorsale de la distinction 5b/5c ; l'arrêt n'y arrive pas.

---

### F3 — « Newspaper Licensing Agency contre Meltwater […] ils ne contournent pas, ils paient » : la ligne la plus fausse du document

**Références exactes et ce qu'elles disent vraiment.**

1. *The Newspaper Licensing Agency Ltd v Meltwater Holding BV*, High Court (Proudman J),
   **[2010] EWHC 3099 (Ch)**, 26 novembre 2010 : l'utilisateur final a besoin d'une licence.
2. Appel rejeté : **[2011] EWCA Civ 890**, 27 juillet 2011.
3. **Renversé sur le point central** : *Public Relations Consultants Association Ltd v The Newspaper
   Licensing Agency Ltd and others*, **[2013] UKSC 18**, **17 avril 2013**, Lord Sumption, décision
   unanime. Résumé de presse officiel de la Cour suprême,
   <https://supremecourt.uk/uploads/uksc_2011_0202_press_summary_7f48904085.pdf>, consulté le
   2 octobre 2026. **Cran B.** Verbatim :

   > « Proudman J held that the end-user needed a licence and the Court of Appeal agreed […] He
   > **rejects** the idea that article 5.1 does not apply to temporary copies generated by an
   > end-user of the internet. »

   > « It has never been an infringement of EU or English law to view or read an infringing article
   > in physical form. »

   > « **Nothing in article 5.1 stops Meltwater needing a licence to upload copyright material on
   > their website.** »

4. Renvoi à la CJUE : affaire **C-360/13**, *Public Relations Consultants Association*, arrêt du
   **5 juin 2014**, qui confirme. (Référence et date établies par sources concordantes, en-tête
   d'affaire non lue de première main : **cran C**.)

**Ce que le document en tire est l'inverse de ce que la saga décide.** Le document écrit : « un
acteur majeur de la veille média **a dû prendre licence** pour ses revues de presse. Réponse directe
à la question "comment font les outils de veille" : **ils ne contournent pas, ils paient**. » Or
l'industrie de la veille a **gagné** le point qui remontait jusqu'à la Cour suprême : les clients
n'avaient pas besoin de licence pour **consulter**. Ce qui restait — que Meltwater, le prestataire,
ait besoin d'une licence pour ses propres actes de copie et de mise en ligne — est dit en passant, et
découlait d'un engagement pris par Meltwater dès 2009 d'entrer dans la *Web Database Licence* en
attendant l'issue (source : ukscblog.com, commentaire d'arrêt, consulté le 2 octobre 2026, **cran C**).

Et trois défauts de méthode s'ajoutent :

- **Mauvaise juridiction.** Droit anglais. Ne dit rien du droit français.
- **Mauvais régime.** Droit d'auteur sur des titres et extraits, exception de copie transitoire de
  l'art. 5(1) de la directive 2001/29. Ni droit des bases de données, ni droit voisin de la presse,
  ni droit des contrats.
- **Mauvaise époque.** Pré-Brexit, et surtout **pré-2019** : le droit voisin des éditeurs de presse
  (F4) n'existait pas. C'est lui qui décide aujourd'hui en France, pas Meltwater.

Le document avait marqué cette ligne « ⏳ Citées de mémoire, cran D ». L'honnêteté du marquage est à
son crédit. Mon reproche est ailleurs : **le §2.6, qui écarte le degré 5c, est bâti sur deux lignes
déjà marquées D**, en violation du §4.2 du document lui-même (« Aucun choix de guichet ne se prend
sur un cran D »). La vérification ne confirme pas : elle falsifie l'inférence.

---

### F4 — « Guichet 6 — flux publiés exprès » et « le guichet 6 débloque la veille presse » : faux pour la presse française

Le document, §2.4, famille « Flux publiés exprès pour être consommés — Flux RSS et Atom de la presse
et des institutions », obligation subsistante : « Respect du cadre de citation, pas de republication
intégrale ». Et conclusion : « **Débloqué** : une part probablement importante du corpus guadeloupéen
institutionnel **et de presse** ». La moitié « institutionnel » est juste. La moitié « presse » est
fausse, et elle est fausse pour trois raisons cumulatives.

**(a) Le droit voisin des éditeurs et agences de presse — que le document ne mentionne nulle part.**

Loi n° **2019-775 du 24 juillet 2019**, JORF n° 172 du 26 juillet 2019, NOR MICX1902858L, créant le
chapitre VIII du titre unique du livre II de la première partie du CPI, **art. L218-1 à L218-5**, en
vigueur le **24 octobre 2019**. Texte lu sur
<https://www.culture.gouv.fr/mc/content/download/219602/pdf_file/Droit_voisin_agences_editeurs_presse.pdf>
et <https://www.senat.fr/leg/ppl18-582.html>, consultés le 2 octobre 2026. **Cran B.**

**Art. L218-2, verbatim :**

> « L'autorisation de l'éditeur de presse ou de l'agence de presse **est requise avant toute
> reproduction ou communication au public totale ou partielle de ses publications de presse sous une
> forme numérique par un service de communication au public en ligne**. »

**Art. L211-3-1, les exceptions, verbatim :**

> « Les bénéficiaires des droits ouverts à l'article L. 218-2 ne peuvent interdire : 1° Les actes
> d'hyperlien ; 2° L'utilisation de mots isolés ou de très courts extraits d'une publication de
> presse. **Cette exception ne peut affecter l'efficacité des droits ouverts au même article
> L. 218-2. Cette efficacité est notamment affectée lorsque l'utilisation de très courts extraits se
> substitue à la publication de presse elle-même ou dispense le lecteur de s'y référer.** »

**C'est la phrase qui tue le volet veille tel qu'il est conçu.** Le document raisonne en **longueur**
(« pas de republication intégrale », « on cite, on résume, on lie »). Le texte raisonne en
**substituabilité**. Un résumé qui dispense le lecteur d'aller à l'article sort de l'exception
**quelle que soit sa brièveté**. Or la proposition de valeur d'un moteur de « collecte vérifiée »
est exactement : *vous n'avez pas besoin de lire la presse locale, nous l'avons fait*. Le produit est
**par conception** du mauvais côté de cette ligne.

Deux précisions qui comptent pour le chiffrage : la durée des droits patrimoniaux est de **deux ans**
à compter du 1er janvier de l'année suivant la première publication (art. L211-4 V, même loi). Donc
le droit mord exactement sur l'actualité fraîche que la veille veut, et s'éteint sur l'archive dont
elle n'a pas besoin. Et la loi « ne s'applique pas aux publications de presse publiées pour la
première fois avant la date d'entrée en vigueur de la directive » (art. 14 de la loi).

Publier un flux RSS **n'est pas** délivrer l'autorisation de l'art. L218-2. Le document a confondu
« l'éditeur a rendu l'information techniquement consommable » avec « l'éditeur a autorisé la
réutilisation ». Ce sont deux actes juridiques distincts et le second ne se déduit pas du premier.

**(b) Le droit sui generis du site de presse, qui s'ajoute et ne se renonce pas davantage.**
Art. **L341-1 CPI**, verbatim : « Le producteur d'une base de données, entendu comme la personne qui
prend l'initiative et le risque des investissements correspondants, bénéficie d'une protection du
contenu de la base lorsque la constitution, la vérification ou la présentation de celui-ci atteste
d'un investissement financier, matériel ou humain substantiel. **Cette protection est indépendante et
s'exerce sans préjudice de celles résultant du droit d'auteur ou d'un autre droit sur la base de
données ou un de ses éléments constitutifs.** » (Légifrance,
<https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006279245/>, atteint via extraits
d'index, consulté le 2 octobre 2026, **cran B**.) Et la CJUE, C-30/14 §42, verbatim : « **the benefit
of that protection does not require any administrative formalities to be fulfilled or any prior
contractual arrangement.** » La protection naît de l'investissement, pas d'une déclaration.

**(c) Le marché a déjà tarifé exactement l'activité du document, ce qui prouve qu'elle n'est pas
ouverte.**

Source primaire — CFC, *Plateformes de veille d'information*,
<https://www.cfcopies.com/secteurs/entreprises-plateformes/plateformes-de-veille-d-information>,
consultée le 2 octobre 2026. **Cran B.** Verbatim :

> « **LICENCE VEILLE WEB** — Pour les **actes de crawling des sites de presse (extraction,
> reproduction et indexation, scraping)** et la mise à disposition de cette veille à des entreprises
> clientes, **sous forme de liens ou d'analyses des contenus** »

Lisez la description du produit du document dans cette ligne. « Crawling, extraction, indexation »,
puis « mise à disposition sous forme de **liens ou d'analyses** ». Si c'était du guichet 6, le CFC
n'aurait rien à vendre. **Le volet veille presse n'est pas du guichet 6 : c'est du guichet 4.**

Et le guichet 4 est **plus lourd** que le document ne le dit, sur trois points sourcés :

- **Deux licences, pas une.** Le CFC gère les rediffusions numériques « dans le cadre des mandats que
  lui apportent les éditeurs » (<https://www.cfcopies.com/le-cfc>, consultée le 2 octobre 2026, B) —
  c'est de la gestion collective **volontaire**, limitée à un **répertoire fini**. Le droit voisin de
  l'art. L218-2 est géré séparément par **DVP, Société des Droits Voisins de la Presse**,
  <https://www.dvpresse.fr/>, consultée le 2 octobre 2026, **cran B** : « DVP a été créé le
  26 octobre 2021 par 74 éditeurs et agences de presse pour gérer le nouveau droit voisin ». Deux
  guichets de paiement, deux négociations.
- **Une cascade de licences par client.** CFC, verbatim
  (<https://www.cfcopies.com/secteurs/entreprises-plateformes/entreprises-privees-et-publiques>,
  consultée le 2 octobre 2026, B) : « Concernant les sociétés de veille d'information, le CFC signe
  avec celles-ci des licences qui autorisent leur activité **jusqu'à la livraison des contenus à
  leurs clients. Si ces contenus sont ensuite rediffusés par l'entreprise destinataire, celle-ci doit
  à son tour obtenir du CFC une licence** couvrant ces usages. » → Un coût caché **chez le client**,
  et une raison pour un hôtelier guadeloupéen de refuser le module presse.
- **Une condition qui boucle sur le reste du document.** Licence CFC veille audiovisuelle, art. 3.2,
  verbatim (<https://www.cfcopies.com/media/949/download/CFC-LICENCE-VEILLE-AUDIOVISUELLE.pdf>,
  consultée le 2 octobre 2026, B) : « **Le cocontractant ne peut reproduire que les œuvres qu'il a
  licitement obtenues.** » La licence ne blanchit pas une collecte illicite en amont.

**La tâche V0 que le document n'a pas, et qui décide du périmètre :** les titres de presse
guadeloupéens sont-ils dans le répertoire du CFC ? Les répertoires sont publiés en xlsx sur
cfcopies.com. S'ils n'y sont pas, **aucune licence n'est disponible auprès du CFC** et il faut
contracter titre par titre. Je n'ai pas ouvert les répertoires : **non vérifié**.

---

### F5 — « Degré 5b — conditions d'utilisation muettes → Retenu sous conditions » : le degré est juridiquement incohérent, et la jurisprudence française a déjà jugé exactement le schéma qu'il autorise

Le silence des CGU lève **un** obstacle : la responsabilité contractuelle. Il ne lève ni le droit sui
generis (§F4-b), ni le droit voisin de la presse, ni le RGPD, ni le parasitisme. Un degré construit
sur l'axe contractuel ne peut donc pas porter un verdict de rétention.

Et les cinq « règles de conception » du 5b sont précisément la défense qui a été rejetée.

**Source primaire — CA Paris, pôle 5 ch. 1, 2 février 2021, n° 17/17688**, *LBC France c/
Entreparticuliers.com*, confirmé par **Cass. 1re civ., 5 octobre 2022, n° 21-16.307**. Texte de
l'arrêt d'appel lu sur
<https://www.legalis.net/jurisprudences/cour-dappel-de-paris-pole-5-ch-1-arret-du-2-fevrier-2021/>,
consulté le 2 octobre 2026. **Cran B.** Confirmation de cassation :
<https://presse.leboncoincorporate.com/actualites/la-cour-de-cassation-confirme-latteinte-aux-bases-de-donnees-du-site-leboncoin-par-entreparticuliers-com-c0bf-763e3.html>
et <https://www.lexbase.fr/article-juridique/88840418-...>, consultés le 2 octobre 2026 (**cran C**
pour ces deux-là ; le dispositif d'appel est en B).

Contre la règle du document « **on cite, on résume, on lie** » — verbatim de l'arrêt :

> « un onglet, mentionnant "repéré sur" ou "contact" sans autre précision, redirigeant vers la page
> du site leboncoin, **une telle indexation, faite en connaissance de cause, en tirant profit des
> investissements réalisés par la société LBC pour la constitution de sa sous-base de données, ne
> relevant pas de la liberté de lier sur internet, mais d'une extraction prohibée par l'article
> L. 342-1** »

Contre l'idée qu'une finalité propre protège — verbatim :

> « peu importe le but poursuivi par celui qui procède à l'extraction »

Contre la règle du document « **pas de reproduction substantielle** » — l'injonction de première
instance, confirmée, porte sur :

> « l'extraction ou la réutilisation **répétée et systématique de parties qualitativement ou
> quantitativement non substantielles** du contenu de la base de données »

C'est l'art. **L342-2 CPI**, verbatim : « le producteur peut également interdire l'extraction ou la
réutilisation répétée et systématique de parties qualitativement ou quantitativement non
substantielles du contenu de la base lorsque ces opérations excèdent manifestement les conditions
d'utilisation normale de la base de données ». **C'est la définition juridique d'un collecteur
continu.** Respecter le seuil de substantialité à chaque requête ne sert à rien quand la collecte est
permanente — et la fraîcheur en heures est, dans le document, un étalon de l'organe Découverte.

Deux aggravations que le document ignore :

- **La sous-base.** La cour a reconnu que la catégorie « immobilier » du site constitue une
  **sous-base de données protégée pour elle-même**. Transposé : « les avis de l'établissement X » ou
  « les avis des hôtels de Guadeloupe » peuvent être une sous-base protégée, et le seuil de
  substantialité se calcule alors sur un denominateur beaucoup plus petit — donc il est franchi
  beaucoup plus vite. La grille du document, qui qualifie « source par source », ne descend pas au
  niveau de la sous-base.
- **Le pénal.** L'atteinte aux droits définis à l'art. L342-1 est punie de **trois ans
  d'emprisonnement et 300 000 € d'amende**, et de sept ans et 750 000 € en bande organisée. Montants
  corroborés par trois sources secondaires concordantes (baumann-avocats.com, canevet.org,
  droit-technologie.org, consultées le 2 octobre 2026) : **cran C pour le montant**. L'existence
  d'une sanction pénale est en **cran B** (travaux de transposition, senat.fr, art. L343-1 d'origine).
  **Le numéro d'article a bougé** : le texte de sanction figure aujourd'hui sous **L343-4**, L343-1
  portant la saisie-contrefaçon. **À relire sur Légifrance** — je n'ai pas pu.

**Verdict sur 5b.** Les cinq conditions du document sont une **bonne éthique d'ingénierie** et un
**mauvais bouclier juridique**. Le document les présente comme le second (« Retenu sous conditions,
avec fiche de qualification »). Il faut retirer le verdict de rétention et le remplacer par : *5b =
écarté par défaut, retenu seulement après analyse positive des trois axes non contractuels — sui
generis, droit voisin, RGPD — documentée source par source.*

---

### F6 — « Un fichier robots permissif » = ouverture déclarée (degré 5a → guichet 6) : faux, et l'asymétrie est documentée

Un fichier `robots.txt` n'a **aucune valeur contractuelle** : pas d'offre, pas d'acceptation, pas de
parties identifiées, aucune volonté de s'obliger. Mais il est juridiquement **opérant**, et
**asymétriquement**, dans deux régimes distincts.

**Source primaire — CNIL, fiche « La base légale de l'intérêt légitime : fiche focus sur les mesures
à prendre en cas de collecte des données par moissonnage (web scraping) », publiée le 19 juin 2025,**
<https://www.cnil.fr/fr/focus-interet-legitime-collecte-par-moissonnage>, consultée le
2 octobre 2026. **Cran B.** Verbatim :

> « **La CNIL considère à cet égard que le traitement ne pourra pas entrer dans les attentes
> raisonnables des personnes si son responsable n'exclut pas de la collecte les sites qui s'opposent
> clairement au moissonnage par l'intermédiaire des protocoles d'exclusion robots.txt ou de
> CAPTCHA.** »

> « exclure de la collecte les sites qui s'opposent clairement au moissonnage de leur contenu […] par
> l'utilisation des protocoles d'exclusion robots.txt ou la mise en place de CAPTCHA »

Et sur l'opt-out de fouille de textes et de données, verbatim (version anglaise de la même fiche,
<https://www.cnil.fr/fr/node/165906>, consultée le 2 octobre 2026, B) :

> « it may be prohibited by other regulations (e.g. by terms and conditions of use based on database
> producer rights or copyright law) […] the « text and data mining » exception under the French
> Intellectual Property Code (Articles L122-5 and 122-5-3), **unless the rightholders have reserved
> their rights in an appropriate manner, in particular by machine-readable means** […] **This includes
> metadata and terms and conditions of a website** »

**L'asymétrie, nette.** Un `robots.txt` restrictif vous **coûte votre base légale** RGPD (attentes
raisonnables non remplies) **et** votre exception de fouille (réservation lisible par machine). Un
`robots.txt` permissif ou silencieux ne vous **donne rien** : aucune licence, aucun droit
d'extraction, aucune renonciation au droit sui generis. C'est un cliquet à sens unique.

Le degré 5a du document — « Atteignable, et ouverture déclarée — licence explicite, flux publié,
**fichier robots permissif** […] c'est du guichet 6 […] **Retenu** » — inverse ce cliquet. Il
convertit une **absence d'interdiction** en **ouverture déclarée**. C'est, à mon sens, la ligne la
plus dangereuse de la §2.3, parce qu'elle est écrite dans la colonne « Retenu » et qu'elle passera
sans discussion dans la fiche de qualification de chaque source.

---

## 3. Ce qui est fragile mais pas faux — et ce qu'il faudrait pour le solidifier

**§2.7, le retournement stratégique.** « La proximité est la clé du guichet 2. Aucun concurrent
mondial ne peut l'ouvrir. » L'intuition commerciale est défendable. Trois fragilités : (a) c'est une
affirmation de cran C/D sans mesure ; (b) si le guichet 2 n'est pas une voie (F1), la proximité est
un avantage sur une porte qui n'existe pas ; (c) la **reformulation qui sauve la thèse** : la
proximité est la clé pour obtenir du client qu'il **accorde un accès délégué de gestionnaire** et
qu'il **dépose sa propre demande de projet d'API**, friction qu'un vendeur à distance ne peut pas
porter. La thèse survit, mais elle déménage du guichet 2 au guichet 3, et le différenciateur devient
**du travail d'onboarding par client** — c'est-à-dire un coût, pas une douve, sauf s'il est
produitisé. *Pour solidifier : chronométrer l'onboarding réel sur trois clients guadeloupéens
volontaires, et le comparer au prix plafond local.*

**§2.2, guichet 4 et le CFC.** Le document marquait « ⏳ D ». La ligne passe en **B** et elle est
substantiellement juste. Fragilités à combler : deux licences (CFC + DVP), répertoire fini, cascade
chez le client, et le fait que l'agrément ministériel du CFC porte sur la reprographie et les usages
numériques pédagogiques — les licences de veille reposent sur des **mandats volontaires**, donc un
titre hors répertoire n'est pas couvert. *Pour solidifier : ouvrir les deux répertoires xlsx et
chercher les titres guadeloupéens ; demander une notice tarifaire Licence Veille Web.*

**§2.6, motifs d'affaires d'écarter le 5c.** Les quatre puces sont du bon raisonnement d'affaires et
je ne les attaque pas. Je note que la mention « parasitisme en droit français » est exacte mais non
développée, et que les décisions françaises réellement citables sont des décisions de **droit des
bases de données**, pas de parasitisme : dans leboncoin, le chef « préjudice d'image » n'a été indemnisé
qu'à hauteur de **20 000 €** (dispositif confirmé, B). *Pour solidifier : sourcer au moins une
décision de parasitisme pur sur de la collecte automatisée, sinon retirer le mot.*

**§3, ligne « Droit — Région ultrapériphérique de l'Union — RGPD plein, droit français ».** **Exact.**
Art. **349 TFUE** (EUR-Lex CELEX 12008E349,
<https://eur-lex.europa.eu/legal-content/FR/TXT/HTML/?uri=CELEX%3A12008E349>, consulté le
2 octobre 2026, **cran B**) nomme la Guadeloupe ; l'art. 355 §1 TFUE rend les traités applicables aux
RUP conformément à l'art. 349. Les mesures spécifiques possibles portent, verbatim, « notamment sur
les politiques douanières et commerciales, la politique fiscale, les zones franches, les politiques
dans les domaines de l'agriculture et de la pêche, les conditions d'approvisionnement […], les aides
d'État, et les conditions d'accès aux fonds structurels » — **la protection des données et les
services numériques n'y sont pas**. Et al. 3, verbatim : « sans nuire à l'intégrité et à la cohérence
de l'ordre juridique de l'Union, y compris le marché intérieur ».

**Donc, et c'est une fragilité d'un autre genre : il n'existe aucune obligation ni aucun allègement
propre aux RUP en matière de droit des données.** Le document a mis « Droit » dans le tableau
guadeloupéen comme s'il y avait une contrainte locale ; il n'y en a pas, il y a l'application pleine
du droit commun. Les vrais éléments spécifiquement guadeloupéens sont **économiques et fiscaux** —
octroi de mer sur le matériel et certaines prestations, éligibilité aux aides au fonctionnement non
dégressives et aux régimes d'aides d'État de l'art. 107 §3 a) TFUE — et ils sont **absents du
document**. *Pour solidifier : déplacer la ligne « Droit » du tableau §3 vers « rien de spécifique »
et ouvrir une ligne « fiscalité et aides d'État RUP » dans le chiffrage de V5.*

**§4.1, le barème lui-même.** Le barème est bon et je m'y suis plié. Une fragilité : il n'a pas de
cran pour **« source primaire inaccessible, lue sur miroir »**, qui est la situation de la moitié de
mes lignes de droit français. Un B obtenu sur Doctrine ou Pappers n'est pas un B obtenu sur
Légifrance : le miroir peut être périmé. *Pour solidifier : ajouter un cran **B-miroir**, ou une
mention obligatoire « miroir » accolée au B.*

---

## 4. Ce qui manque et qui peut tuer le projet

### M1 — Art. L111-7-2 du Code de la consommation : l'angle mort principal

Le document ne cite **jamais** le texte français qui régit nommément son activité.

**Source primaire — art. L111-7-2 C. consom.**, issu de l'art. 52 de la loi n° 2016-1321 du
7 octobre 2016 pour une République numérique. Verbatim :

> « Sans préjudice des obligations d'information prévues à l'article 19 de la loi n° 2004-575 du
> 21 juin 2004 pour la confiance dans l'économie numérique et à l'article L. 111-7 du présent code,
> **toute personne physique ou morale dont l'activité consiste, à titre principal ou accessoire, à
> collecter, à modérer ou à diffuser des avis en ligne provenant de consommateurs est tenue de
> délivrer aux utilisateurs une information loyale, claire et transparente sur les modalités de
> publication et de traitement des avis mis en ligne.** […] Elle met en place une **fonctionnalité
> gratuite** qui permet aux responsables des produits ou des services faisant l'objet d'un avis en
> ligne de lui signaler un doute sur l'authenticité de cet avis, à condition que ce signalement soit
> motivé. »

Texte lu sur <https://www.doctrine.fr/l/texts/codes/LEGITEXT000006069565/articles/LEGIARTI000033207118>,
consulté le 2 octobre 2026. **Cran B-miroir.** La même source indique « **Entrée en vigueur le
17 février 2024** » en application du V de l'art. 64 de la **loi n° 2024-449 du 21 mai 2024** — donc
la rédaction a changé récemment et **doit être relue sur Légifrance**.

**Décret d'application n° 2017-1436 du 29 septembre 2017**, JO n° 233 du 5 octobre 2017, créant les
art. **D111-16 à D111-19** C. consom., en vigueur le 1er janvier 2018. Texte du JO lu sur
<https://hr-infos.fr/wp-content/uploads/2017/10/joe_20171005_0233_0024.pdf>, consulté le
2 octobre 2026. **Cran B.** Verbatim, art. D111-17 :

> « 1° **A proximité des avis** : a) L'existence ou non d'une procédure de contrôle des avis ;
> b) **La date de publication de chaque avis, ainsi que celle de l'expérience de consommation
> concernée par l'avis** ; c) Les critères de classement des avis parmi lesquels figurent le
> classement chronologique. 2° **Dans une rubrique spécifique facilement accessible** : a) L'existence
> ou non de contrepartie fournie en échange du dépôt d'avis ; b) **Le délai maximum de publication et
> de conservation d'un avis.** »

Et art. D111-18, verbatim : « elle **veille à ce que les traitements de données à caractère personnel
réalisés dans ce cadre soient conformes** à la loi n° 78-17 du 6 janvier 1978 […] et précise […]
1° Les caractéristiques principales du contrôle des avis au moment de leur collecte, de leur
modération ou de leur diffusion ; 2° La possibilité, le cas échéant, de contacter le consommateur
auteur de l'avis ; 3° La possibilité ou non de modifier un avis […] ; 4° Les motifs justifiant un
refus de publication de l'avis. »

Et la définition, art. D111-16, verbatim : « un avis en ligne s'entend de l'expression de l'opinion
d'un consommateur sur son expérience de consommation […] **L'expérience de consommation s'entend que
le consommateur ait ou non acheté le bien ou le service** pour lequel il dépose un avis. »

Sanction : amende administrative, plafond annoncé à 75 000 € personne physique / 375 000 € personne
morale (art. L131-4 C. consom.) — **cran C**, montant repris de sources d'avocats concordantes
(ddg.fr, consultée le 2 octobre 2026), non lu sur Légifrance.

**Pourquoi c'est mortel et pas administratif.** Le champ est « collecter, **modérer** ou **diffuser**,
à titre **principal ou accessoire** ». Un agrégateur d'avis qui les affiche dans un tableau de bord
client est dedans sans discussion possible. Et deux obligations sont des **contraintes de collecte**,
pas d'affichage :

- **la date de l'expérience de consommation**, distincte de la date de publication. Si elle n'est pas
  captée au moment de la collecte, elle est **irrécupérable**.
- **le statut de la procédure de contrôle de la source**, à afficher à proximité de l'avis.

Or le gabarit de fiche-organe (§4.4) et l'étalon « Avis » (§6) ne contiennent **ni l'un ni l'autre**.
L'organe Provenance mesure « part datée » — mais datée de quoi ? La loi exige **deux** dates. C'est
un champ manquant dans le schéma de données, et c'est la définition d'une dette irrattrapable.

### M2 — Art. L121-4 27° et 28° C. consom. : deux pratiques réputées trompeuses qui visent le cœur du produit

**Source primaire — art. L121-4 C. consom.**, Légifrance,
<https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044563107>, consulté le 2 octobre 2026.
**Cran B.** En vigueur le 28 mai 2022 (art. 10 de l'ordonnance n° 2021-1734 du 22 décembre 2021,
transposant la directive « Omnibus » 2019/2161). Verbatim :

> « **27° D'affirmer que des avis sur un produit sont diffusés par des consommateurs qui ont
> effectivement utilisé ou acheté le produit sans avoir pris les mesures nécessaires pour le
> vérifier ;**
> **28° De diffuser ou faire diffuser par une autre personne morale ou physique des faux avis ou de
> fausses recommandations de consommateurs ou modifier des avis de consommateurs ou des
> recommandations afin de promouvoir des produits.** »

Ce sont des pratiques **réputées** trompeuses : irréfragables, le professionnel ne peut pas prouver
le contraire. Deux conséquences directes et lourdes :

- **27° est à la fois le risque principal et l'opportunité principale du projet.** Un produit dont la
  promesse est « la vérifiabilité est notre couche » et qui agrège des avis sans les vérifier tombe
  sous 27°. Mais c'est la seule obligation du lot que ce projet devrait être **content** de porter :
  elle transforme sa couche de vérification en obligation légale commune à tous ses concurrents.
  **Encore faut-il la mesurer.** L'étalon « Avis » du §6 mesure « part des avis captés sur ceux
  réellement présents … délai de détection … taux de réponse sous 24 h ». **Aucune métrique de
  vérification.** L'étalon mesure la quantité dans un régime juridique qui sanctionne le défaut de
  vérification. C'est le mauvais étalon pour le bon produit.
- **28° « modifier des avis » est une interdiction d'architecture.** Un outil qui détient un accès
  délégué et agit sur la plateforme doit être **structurellement incapable** d'éditer le texte d'un
  avis — pas « configuré pour ne pas le faire », incapable. Et il doit pouvoir le prouver par journal.
  Contrainte absente du document.

À quoi s'ajoute, en information précontractuelle, art. L121-3 : « lorsqu'un professionnel donne accès
à des avis de consommateurs sur des produits, les informations permettant d'établir **si et comment**
le professionnel garantit que les avis publiés émanent de consommateurs ayant effectivement utilisé
ou acheté le produit **sont réputées substantielles** » (Légifrance, section L121-1 à L121-24,
consultée le 2 octobre 2026, **cran B**). Omission = pratique trompeuse par omission.

### M3 — RGPD : la question 4 du cahier des charges, répondue en détail — et le projet ne survit pas sans une exemption nommée

Le document dit, en tout et pour tout : « au RGPD dès qu'un avis porte un prénom » (§2.6) et
« RGPD appliqué aux avis nominatifs » (agent V1). Voici la chaîne réelle pour un agrégateur en
**collecte indirecte** — il ne reçoit pas l'avis de son auteur.

**Base légale.** Intérêt légitime, art. 6.1.f, disponible mais conditionnel. **Source primaire —
CNIL, *Recommandations — Réutilisateurs de données publiées sur Internet*,**
<https://www.cnil.fr/sites/cnil/files/2024-06/recommandations_reutilisateurs_de_donnees_publiees_sur_internet.pdf>,
consultée le 2 octobre 2026. **Cran B.** La CNIL distingue trois cas ; un avis déposé sur une
plateforme relève du **troisième**, verbatim :

> « Troisième cas : des données personnelles ont été publiées sur internet mais ne l'ont pas été dans
> une perspective d'open data, mais simplement dans le cadre de l'activité du responsable de
> traitement (données figurant sur les réseaux sociaux, données d'articles de presse, données
> présentes sur un site de petites annonces etc.). […] **l'intérêt légitime du réutilisateur doit
> être apprécié au cas par cas.** »

Et parmi les critères de la mise en balance, verbatim : « **les éventuelles restrictions découlant
d'une licence de réutilisation ou des conditions générales d'utilisation d'un site web** (p. ex :
interdiction de procéder à des moissonnages de données en ligne à des fins de prospection
commerciale) ». → **La balance d'intérêt légitime doit être écrite source par source.** Elle manque
dans le gabarit §4.4.

**Information des personnes — c'est ici que le projet se joue.** Art. 14 RGPD, collecte indirecte.
**Source primaire — CNIL, *La réutilisation des données publiquement accessibles en ligne à des fins
de démarchage commercial*,** <https://cnil.fr/fr/la-reutilisation-des-donnees-publiquement-accessibles-en-ligne-des-fins-de-demarchage-commercial>,
publiée le 30 avril 2020, consultée le 2 octobre 2026. **Cran B.** Verbatim :

> « il est primordial que la société utilisant le logiciel d'aspiration de données fournisse, **au
> plus tard au moment de la première communication avec les personnes** dont les données sont
> traitées, **les informations prévues à l'article 14 du RGPD et notamment celle relative à la source
> des données**. »

Et, verbatim, sur l'erreur fondatrice que le document commet implicitement :

> « Ces données, bien que publiquement accessibles, sont des données personnelles. Dès lors, **elles
> ne sont pas librement réutilisables** par tout responsable de traitement et ne peuvent être
> réexploitées à l'insu de la personne concernée. »

Informer **chaque auteur d'avis** est inexécutable à l'échelle. L'issue est l'exemption de l'art.
**14.5.b** RGPD — effort disproportionné, sous condition de mesures appropriées dont la mise à
disposition publique de l'information. **Le document ne nomme jamais cette exemption.** Or c'est
elle, et non la question du mandat, qui décide si le volet avis existe. *C'est la question
n° 1 à poser au juriste, avant celle du mandat que le §10 met en tête.*

**Durée de conservation.** Art. 5.1.e : aucune durée dans la loi, une durée à définir et à justifier
par finalité. Tension non nommée dans le document : l'étalon de l'organe Index (« coût au million de
documents ») pousse à accumuler ; l'art. 5.1.e pousse à purger. Un produit dont le besoin opérationnel
est court (détecter, répondre sous 24 h) et la tentation commerciale longue (tendance historique) doit
trancher **avant** de dimensionner l'index.

**Droit d'opposition.** Art. 21.1, toujours ouvert quand la base est l'intérêt légitime. Et la CNIL va
plus loin, verbatim (fiche moissonnage 19 juin 2025, **cran B**) :

> « prévoir un **droit d'opposition discrétionnaire et préalable** afin de renforcer le contrôle des
> personnes sur leurs données. […] des mécanismes de « **liste repoussoir** » pourraient par exemple
> être mis en œuvre […] Cela permettrait au responsable du traitement de respecter l'opposition des
> personnes **en s'abstenant de collecter** les données de ces dernières »

→ Une liste repoussoir indexée sur les pseudonymes d'auteurs, honorée **avant** collecte. C'est un
organe. Il n'est pas dans la §6.

**Données sensibles — et la §3 du document aggrave le problème sans le voir.** Art. 9 RGPD. Un avis
d'hôtel révèle couramment la santé (accessibilité, allergies), la religion (régime alimentaire),
l'orientation sexuelle (couples), le handicap. CNIL, fiche moissonnage, verbatim : « Le responsable du
traitement **est tenu de mettre en œuvre toutes les mesures permettant d'exclure automatiquement la
collecte de données sensibles non pertinentes** notamment en appliquant des filtres ». Un corpus
d'avis en texte libre est un risque art. 9 **structurel** — et l'exigence « Langues » du document
(français, créole guadeloupéen, anglais, espagnol) **multiplie par quatre** le coût de filtrage, sur
une langue, le créole, pour laquelle aucun filtre de données sensibles prêt à l'emploi n'existe
probablement. Le document traite le multilinguisme comme une exigence d'extraction ; c'est aussi une
exigence de conformité, et c'est la plus chère.

**AIPD.** Probablement obligatoire — **cran D7**, déclaré en tête.

### M4 — Droit d'auteur sur les avis eux-mêmes

Le document s'inquiète du droit d'auteur sur la presse (implicitement, via le CFC) et jamais du droit
d'auteur **sur les avis**. Un avis d'une certaine longueur est une œuvre de l'esprit ; son auteur est
titulaire du droit patrimonial **et du droit moral**. Les CGU des plateformes prennent une licence
auprès de l'auteur — TripAdvisor évoque une « Restricted Licence » couvrant le contenu « that you or
another on your behalf […] make available on or in connection with the Services » (extrait de
recherche, **non lu de première main, domaine bloqué — ne pas utiliser comme source**). Cette licence
court **au profit de la plateforme, pas au vôtre**.

Conséquence : republier verbatim le texte d'un avis dans un tableau de bord client est un acte de
reproduction qui a besoin d'un titre. L'organe « Avis » du document suppose la captation et
l'affichage ; il ne demande jamais **à quel titre** il affiche. Et le droit moral (**cran D6**) n'est
de toute façon pas purgeable par CGU.

### M5 — Parasitisme et concurrence déloyale

Art. 1240 C. civ. Le document le nomme une fois, comme risque du 5c. C'est plus que cela : le
parasitisme est **autonome de tout droit de propriété intellectuelle** et survit à l'échec de l'action
en droit sui generis — **cran D1, déclaré**. Ce qui est en **cran B** : dans l'affaire leboncoin, le
chef de préjudice d'image a été indemnisé à 20 000 €, montant modeste. Ce qui rend le risque réel pour
une TPE guadeloupéenne, ce n'est pas le montant, c'est le **coût de la défense** et la **mesure de
publication** que la cour a ordonnée (dispositif confirmé, B).

### M6 — Responsabilité en cas de publication automatique d'un contenu diffamatoire ou faux : le document n'a rien

**Le régime.** Loi n° **2004-575 du 21 juin 2004** pour la confiance dans l'économie numérique, art. 6.
Distinction hébergeur (6-I-2) / éditeur (6-III-1). Le critère de partage, formulé par le Conseil
constitutionnel dans ses *Nouveaux Cahiers*,
<https://read-only.conseil-constitutionnel.fr/nouveaux-cahiers-du-conseil-constitutionnel/contenus-illicites-sur-internet-et-hebergeurs>,
consulté le 2 octobre 2026 — site officiel mais article doctrinal, **cran C**. Verbatim :

> « la ligne de partage est nette, qui distingue les éditeurs, **qui ont un rôle actif sur les
> contenus qu'ils mettent en ligne**, des hébergeurs, dont la tâche consiste à rendre accessibles les
> contenus mis en ligne par des tiers sans avoir, à l'égard de ces contenus, un rôle actif. En
> d'autres termes, **le contrôle ou l'absence de contrôle sur le contenu accessible sur le site est le
> critère départageur**. »

**Trois conséquences que le document ne tire pas.**

1. **Le produit est du côté éditeur, par construction et par argumentaire de vente.** Il sélectionne,
   classe, résume, vérifie et republie. Un produit dont le différenciateur est le contrôle éditorial
   ne peut pas plaider l'absence de rôle actif. Conséquence : responsabilité pleine sous la loi du
   29 juillet 1881 pour la diffamation, prescription de trois mois, **et aucun abri de notification
   et retrait**. L'organe de vérification est, juridiquement, ce qui vous fait perdre le statut
   d'hébergeur.
2. **Pour l'organe Rédaction, il n'y a même pas de débat.** Un texte **généré** n'est pas un contenu
   de tiers. Il n'existe aucun argument d'hébergeur. Celui qui publie une réponse à avis rédigée par
   IA et qui diffame un client est éditeur, point. L'étalon §6 « nombre d'affirmations non sourcées
   par texte » mesure le symptôme ; la règle de responsabilité n'est pas nommée.
3. **Droit de réponse.** LCEN art. 6-IV, verbatim (version consolidée au 11 juillet 2024, lue sur
   <https://www.cornucopiae.fr/2004-575_Mai_2024.pdf>, consulté le 2 octobre 2026, **cran C** —
   miroir PDF, à confirmer sur Légifrance) : « **Toute personne nommée ou désignée dans un service de
   communication au public en ligne dispose d'un droit de réponse** ». Toute façade grand public qui
   republie des avis nominatifs doit outiller ce droit.

**DSA.** Règlement (UE) **2022/2065** du 19 octobre 2022. La LCEN renvoie désormais à ses définitions
(« On entend par "services intermédiaires" les services de la société de l'information définis au
paragraphe g de l'article 3 du règlement (UE) 2022/2065 », version consolidée lue, **cran C**). Les
obligations propres aux plateformes exemptent largement les micro et petites entreprises ; les règles
de responsabilité des intermédiaires s'appliquent sans seuil. Non nommé dans le document.

### M7 — Règlement sur l'intelligence artificielle : applicable **depuis deux mois**, et le document l'ignore

Règlement (UE) **2024/1689** du 13 juin 2024, **art. 50**. Texte de l'article lu intégralement sur
<https://www.doctrine.fr/l/texts/eu/reglements/EULEGF8920448E9AB22DA048D/articles/EULEGARTI9D006C9B214ECB1D48D7>,
consulté le 2 octobre 2026 — reproduction du texte du règlement, **cran B-miroir** (EUR-Lex bloqué
pour ce texte en FR, atteint seulement pour les considérants).

Trois alinéas visent directement ce projet.

**50(1), fournisseur, verbatim :** « Les fournisseurs veillent à ce que les systèmes d'IA destinés à
interagir directement avec des personnes physiques soient conçus et développés de manière que les
personnes physiques concernées soient informées qu'elles interagissent avec un système d'IA ». → Un
agent qui répond aux clients d'un hôtel est exactement cela.

**50(2), fournisseur, verbatim :** « Les fournisseurs de systèmes d'IA […] qui génèrent des contenus de
synthèse de type audio, image, vidéo **ou texte**, veillent à ce que les sorties des systèmes d'IA
soient **marquées dans un format lisible par machine** et identifiables comme ayant été générées ou
manipulées par une IA. […] Cette obligation ne s'applique pas dans la mesure où les systèmes d'IA
remplissent une fonction d'assistance pour la mise en forme standard **ou ne modifient pas de manière
substantielle les données d'entrée** ». → Un organe de rédaction modifie substantiellement. Il est
dans le champ.

**50(4) al. 2, déployeur, verbatim — et c'est ici que se trouve la porte de sortie du projet :**

> « Les déployeurs d'un système d'IA qui génère ou manipule des textes publiés dans le but d'informer
> le public sur des questions d'intérêt public indiquent que le texte a été généré ou manipulé par une
> IA. Cette obligation ne s'applique pas […] **lorsque le contenu généré par l'IA a fait l'objet d'un
> processus d'examen humain ou de contrôle éditorial et lorsqu'une personne physique ou morale assume
> la responsabilité éditoriale de la publication du contenu.** »

**Conséquence de conception, et c'est la plus utile de tout ce retour.** L'étalon « Taux de reprise par
un humain » de la §6 n'est pas une métrique de qualité : **c'est la condition légale d'exonération** de
l'art. 50(4), et c'est aussi la réponse au M6 sur la responsabilité éditoriale. Il faut le promouvoir
de métrique en **porte de conformité** : zéro publication non relue, journalisée, avec un responsable
éditorial nommé. Le document a la bonne mesure pour la mauvaise raison.

**Calendrier et sanctions — cran C, et je le signale fortement.** Quatre sources françaises
concordantes consultées le 2 octobre 2026 (maconformite.fr/ressources/article-50-transparence,
donneespersonnelles.fr/transparence-ia-article-50-ai-act, rgpdkit.fr/blog/article-50-ai-act-transparence-rgpd,
gdroit.fr/droit-et-ia/reglement-ia/obligations-transparence) indiquent : art. 50 **applicable depuis
le 2 août 2026** (art. 113) ; un règlement (UE) **2026/1744** dit « Digital Omnibus IA », publié au
JOUE le 24 juillet 2026 et en vigueur le 27 juillet 2026, **n'a pas reporté l'art. 50** mais seulement
le haut risque (annexe III au 2 décembre 2027, annexe I au 2 août 2028) ; une transition de l'art.
111(4) porte le marquage lisible par machine au **2 décembre 2026** pour les systèmes mis sur le marché
avant le 2 août 2026 ; sanctions de l'art. 99(4) jusqu'à **15 M€ ou 3 % du chiffre d'affaires mondial**.
**Je n'ai pas pu atteindre EUR-Lex pour le règlement 2026/1744. Tout ce paragraphe est en cran C et
doit être confirmé sur source primaire avant d'être opposé à quiconque.** Ce qui est en **cran B**,
c'est le texte de l'art. 50 cité plus haut.

Nous sommes le 2 octobre 2026. Si le calendrier C est exact, **l'art. 50 s'applique depuis deux mois**
et un document de lancement daté du même jour ne le mentionne pas. C'est la seule omission du document
qui soit déjà, aujourd'hui, une non-conformité et non un risque futur.

### M8 — L'organe manquant : le registre juridique

Le document a sept organes plus la garde des accès. Il n'a **aucun organe** qui tienne, par source et
par client : la licence applicable et sa date, la version des CGU lue et sa date, la balance d'intérêt
légitime écrite, la liste repoussoir, l'horloge de conservation, la date de l'expérience de
consommation, le statut de la procédure de contrôle de la source, le titre au nom duquel chaque texte
est affiché, et le nom du responsable éditorial de chaque publication.

**Chacune de ces obligations est une métadonnée par source ou par avis.** Si l'organe de collecte ne
l'émet pas, aucun organe en aval ne peut l'inventer. C'est l'ajout le moins cher en V0 et le plus
coûteux à rattraper ensuite. C'est aussi, accessoirement, la seule chose du projet qui ressemble à la
« couche de vérifiabilité à inventer » que le §1 revendique comme avantage propre : un registre
juridique rejouable **est** un étalon de vérifiabilité, et personne ne le vend.

---

## 5. Verdict : le volet avis est-il viable, et sous quelle condition exacte

**Non, pas tel qu'il est décrit.** Le volet avis repose sur un guichet 2 qui n'est pas une voie
d'accès : c'est une hypothèse non vérifiée sur un contrat que le document n'a pas lu, et les deux
plateformes dont j'ai pu lire les documents contractuels de première main orientent toutes deux
ailleurs — Google vers l'accès délégué de gestionnaire avec interdiction expresse du partage de mots de
passe, Booking vers un accord de partenariat de connectivité conclu avec Booking, c'est-à-dire vers le
guichet 1 que le document avait mis hors de portée. Un produit dont l'organe fondateur est la garde
des identifiants de ses clients est bâti sur l'anti-modèle de son principal fournisseur d'accès.

**Oui, viable, sous cinq conditions cumulatives, et aucune n'est négociable.**

1. **Le guichet 2 est réécrit en guichet 3.** Accès délégué, jamais d'identifiants : accès
   *gestionnaire* et jeton OAuth chez Google, accord de connectivité chez Booking. L'organe « Garde des
   accès confiés » devient « **Garde des autorisations déléguées** » — garde de jetons, portée minimale,
   rotation, révocation en minutes, journal d'accès, cloisonnement. Objet technique différent, plus
   simple, et conforme.
2. **La faisabilité est tranchée plateforme par plateforme avant toute construction.** Google : ouvert
   dès maintenant au prix d'un onboarding par client, chaque client devant déposer sa propre demande de
   projet d'API. Booking : guichet 1 ou rien. TripAdvisor : **non qualifié**, les CGU n'ont pas été
   lues, et une plateforme non qualifiée ne figure pas dans le plan.
3. **L111-7-2 / D111-16 à D111-19 et L121-4 27°-28° sont traités comme spécification produit**, pas
   comme conformité d'après-coup. Concrètement : capter la **date de l'expérience de consommation** et
   le **statut de vérification** au moment de la collecte ; rendre le texte d'un avis
   **architecturalement immuable** ; ajouter au moins une métrique de vérification à l'étalon « Avis »,
   qui n'en a aucune.
4. **L'exemption de l'art. 14.5.b RGPD est sécurisée par écrit par un juriste avant qu'un seul avis
   nominatif soit stocké**, avec sa notice d'information publique et son mécanisme d'opposition
   préalable — liste repoussoir honorée avant collecte. C'est la question n° 1 du juriste, devant celle
   du mandat que le §10 met en tête.
5. **Rien n'est publié sans relecture humaine et sans responsabilité éditoriale assumée et nommée.**
   C'est à la fois la condition d'exonération de l'art. 50(4) du règlement IA et la seule réponse
   tenable à la responsabilité d'éditeur sous la LCEN et la loi de 1881.

**Et le volet veille presse n'est pas viable au guichet 6, à aucune condition.** C'est du guichet 4 :
licence CFC Veille Web **plus** une autorisation au titre du droit voisin de l'art. L218-2, avec une
cascade de licences chez chaque client destinataire. Le nœud du §10 — « es-tu prêt à payer un droit de
collecte pour la veille presse » — n'est donc pas une préférence stratégique : c'est la seule réponse
licite. La vraie question V0, que le document n'a pas, est : **les titres guadeloupéens sont-ils dans le
répertoire du CFC ?** S'ils n'y sont pas, il n'y a pas de licence à acheter et il faut contracter titre
par titre — ce qui, pour une presse locale de quelques titres, est peut-être la bonne nouvelle cachée
de ce retour.

---

---

# RELANCE 1 — anti-oubli

## Qu'as-tu oublié — trois pistes écartées, et pourquoi

**1. L'exception de fouille de textes et de données (art. L122-5-3 CPI, art. 4 de la directive
2019/790) comme fondement du moteur de collecte.** Écartée pour deux raisons. D'abord parce que c'est
une exception au droit d'auteur et au droit des bases de données pour la **fouille**, c'est-à-dire pour
l'extraction d'informations à partir d'un corpus — alors que la sortie de ce produit est la
**republication du contenu lui-même** (extraits, résumés, avis affichés), pas un résultat de fouille.
Ensuite parce que l'opt-out est lisible par machine et que la presse l'a exercé : la CNIL confirme,
verbatim, que l'exception joue « unless the rightholders have reserved their rights in an appropriate
manner, in particular by machine-readable means ». **À réexaminer** si et seulement si une sortie du
produit devient purement statistique — un indicateur de climat d'opinion sans extrait reproduit. Ce
serait un produit différent, et il serait peut-être le seul licite sans licence.

**2. Yelp, Meta/Facebook, Expedia, Google Maps comme sources distinctes.** Écartées par manque de
temps : je n'ai lu de première main que les documents de Google et de Booking. C'est un trou réel, et
il contredit l'exigence V3 du document (« recensement **exhaustif** des plateformes pertinentes en
Guadeloupe »). J'ai couvert deux plateformes sur un paysage que je n'ai pas cartographié. Je ne liste
pas les autres pour faire nombre : le §4.3 du document l'interdit et il a raison.

**3. L'économie du contentieux — qui poursuit réellement un prestataire guadeloupéen à dix clients.**
Écartée parce que ce n'est pas une question de droit et parce que la plaider serait exactement le
« tel concurrent le fait donc c'est permis » que le §4.3 proscrit. Mais c'est la raison honnête pour
laquelle le risque est plus faible en pratique qu'au tableau, et quelqu'un devrait le **chiffrer**
plutôt que de le nier : probabilité d'action, coût de défense, coût d'une mesure de publication,
assurance responsabilité civile professionnelle couvrant la contrefaçon. Un risque chiffré nourrit
l'arbitrage ; un risque masqué tue le produit — c'est la phrase du document, appliquée à lui-même.

## Que n'as-tu pas vu — ce que je n'ai pas pu vérifier, et ce qui m'a manqué

- **La clause des GDT Booking.com sur l'accès d'un tiers à l'Extranet.** Les GDT complets ne sont
  délivrés qu'en PDF, au contact contractuel, sur demande depuis l'Extranet. *Il m'a manqué un
  hôtelier volontaire.*
- **Les CGU de TripAdvisor** (*Hospitality Master Terms and Schedules*, CGU françaises). *Il m'a manqué
  l'ouverture réseau de `tripadvisor.com` et `tripadvisor.mediaroom.com`.*
- **Légifrance, curia.europa.eu, bailii.org, et EUR-Lex en accès direct.** Tous bloqués en sortie. EUR-Lex
  n'a été atteint que par la récupération côté serveur d'EXA. *Il m'a manqué une autorisation de sortie
  réseau, ou un MCP Légifrance.* Conséquence : les textes du CPI et du Code de la consommation sont
  lus sur miroirs, et **tout numéro d'article peut être périmé**.
- **Le règlement (UE) 2026/1744 « Digital Omnibus IA »** et le calendrier de l'art. 50 : sources
  secondaires seulement, cran C.
- **Les répertoires CFC (xlsx)** : jamais ouverts. Donc la question décisive — les titres guadeloupéens
  y sont-ils — reste sans réponse. *Il m'a manqué d'utiliser la compétence tableur disponible dans
  cette session.*
- **Le texte intégral de Cass. 1re civ., 5 octobre 2022, n° 21-16.307** : lu par le dispositif d'appel
  et deux commentaires, pas par l'arrêt. *Il m'a manqué Judilibre.*
- **Les montants de sanction** de L131-4 et L132-2 C. consom. : sources secondaires concordantes, cran C.
- **L'arrêt C-360/13 du 5 juin 2014** : référence et date établies par concordance, en-tête non lu.
- **L'issue finale de Ryanair devant le Hoge Raad** : inconnue (D2).

## Qu'est-ce qui rendrait ce produit plus profitable — l'endroit exact où il perd de l'argent, et le geste

**L'endroit exact : l'onboarding par client.** Trois textes lus dans ce retour l'imposent et il est
irréductible. Google : « the client needs to apply for access themselves » — chaque client doit
déposer sa propre demande de projet d'API, et vous accorder manuellement l'accès gestionnaire. CFC :
« si ces contenus sont ensuite rediffusés par l'entreprise destinataire, celle-ci doit à son tour
obtenir du CFC une licence » — chaque client qui rediffuse doit prendre sa licence. RGPD et L111-7-2 :
un dossier juridique par source, et une notice par client. Sur un marché de très petites entreprises
avec un prix plafond local, **trois heures de travail humain d'onboarding par client mangent la marge
de la première année**, et comme ce travail ne se capitalise pas d'un client à l'autre, la marge ne
s'améliore pas avec l'échelle. C'est le défaut structurel du modèle, pas un coût de démarrage.

**Le geste qui corrige, en deux mouvements.**

*Premier mouvement :* faire exécuter l'onboarding **par le client lui-même**, dans son propre compte,
par un parcours guidé en libre-service — liste séquencée, liens profonds vers les écrans exacts de
Google, captures, et un rappel automatique qui vérifie que l'accès gestionnaire est bien arrivé avant
de laisser le produit démarrer. Le travail ne disparaît pas, il change de payeur, et il devient un
**filtre de qualification** : un client qui ne finit pas le parcours n'était pas un client. Accessoirement,
c'est aussi la preuve écrite du consentement explicite que la politique de Google exige pour répondre
aux avis en son nom (« Verbal consent isn't sufficient »), donc le parcours produit son propre dossier.

*Second mouvement :* sortir la veille presse du produit de base et en faire une **option payante
distincte**, qui ne s'active que lorsque la référence de la licence CFC du client est saisie dans
l'outil. La cascade de licences cesse d'être un coût caché subi et devient un second article au
catalogue, avec sa propre marge et son propre refus possible. Deux centres de coût deviennent un filtre
et une seconde ligne de facturation.

---

# RELANCE 2 — preuve, étalon et guichet

## Ligne par ligne : vérifié avec quoi, obtenu quoi, validé ou recopié, cran reclassé

| # | Ligne | Vérifiée avec quoi — URL, date | Obtenu — passage, pas résumé | Validé par moi / recopié | Cran |
|---|---|---|---|---|---|
| 1 | Google interdit le partage de mots de passe et exige un accord explicite écrit pour répondre aux avis au nom du client | support.google.com/business/answer/7353941 — 2 oct. 2026 | « **Do not share passwords with your clients.** » ; « **To respond to reviews on behalf of the end customer, you must have an explicit approval. Verbal consent isn't sufficient.** » | Lu de première main, passages cités verbatim. Non testé en usage. | **B** |
| 2 | Google interdit l'accès indirect et exige que le client dépose sa propre demande | developers.google.com/my-business/content/policies et /locations — 2 oct. 2026 | « **You cannot provide indirect access to your Business Profile project.** » ; « **the client needs to apply for access themselves.** » | Lu de première main. | **B** |
| 3 | L'Extranet Booking est défini comme accédé par l'établissement ; la seule catégorie de tiers est le Connectivity Provider sous accord avec Booking | admin.booking.com/hotelreg/terms-and-conditions.html — 2 oct. 2026 | « "Extranet" means the online systems of Booking.com **which can be accessed by the Accommodation** (after inputting its username and password) » ; « **who has concluded a valid and continuing connectivity partnership agreement with Booking.com** » | Lu de première main (version d'enregistrement des GDT). | **B** |
| 4 | Le flux Booking sanctionné est une autorisation déléguée par lien, pas une remise d'identifiants | developers.booking.com/connectivity/docs/contracting-api/managing-contracts — 2 oct. 2026 | « **Share the link received in the API response with the partner to login to their account and authorise the connection.** » | Lu de première main. Non appelé. | **B** |
| 5 | Les GDT contiennent-ils une interdiction expresse de communiquer les identifiants à un tiers | — | **Non trouvé.** GDT complets délivrés en PDF au seul contact contractuel. | Rien recopié. | **non vérifié** |
| 6 | CGU TripAdvisor | domaines bloqués en sortie | **Non lu.** | Extraits de moteur seulement — écartés. | **D4, déclaré** |
| 7 | C-30/14, Ryanair c/ PR Aviation, 15 janv. 2015, dispositif et §30-45 | eur-lex.europa.eu CELEX 62014CJ0030, via récupération côté serveur EXA — 2 oct. 2026 | « it **is not applicable** to a database which is not protected either by copyright or by the sui generis right […] **do not preclude** […] **without prejudice to the applicable national law.** » ; §39 « which **establish mandatory rights for lawful users** » ; §42 « the benefit of that protection **does not require** any […] prior contractual arrangement » | **Texte intégral lu et cité verbatim.** Contraposée du §39-40 : mon raisonnement, pas celui de la Cour — je le signale comme tel. | **B** (texte) ; le raisonnement par contraposée : **B appliqué**, à faire confirmer par un juriste |
| 8 | Saga Meltwater : [2010] EWHC 3099 (Ch), [2011] EWCA Civ 890, [2013] UKSC 18 du 17 avril 2013, renvoi C-360/13 | supremecourt.uk/uploads/uksc_2011_0202_press_summary_7f48904085.pdf — 2 oct. 2026 | « Proudman J held that the end-user needed a licence and the Court of Appeal agreed […] He **rejects** the idea that article 5.1 does not apply […] **Nothing in article 5.1 stops Meltwater needing a licence to upload** » | Résumé de presse officiel lu de première main. **Arrêt non lu** (bailii bloqué). C-360/13 : non lu. | **B** pour UKSC 18 ; **C** pour C-360/13 |
| 9 | Droit voisin presse, L218-1 à L218-5 et L211-3-1, loi 2019-775 du 24 juill. 2019 | culture.gouv.fr/mc/content/download/219602 et senat.fr/leg/ppl18-582.html — 2 oct. 2026 | « **L'autorisation de l'éditeur de presse ou de l'agence de presse est requise avant toute reproduction ou communication au public totale ou partielle** » ; « **Cette efficacité est notamment affectée lorsque l'utilisation de très courts extraits se substitue à la publication de presse elle-même ou dispense le lecteur de s'y référer.** » | Texte de loi lu sur site ministériel et travaux parlementaires. **Pas sur Légifrance.** | **B-miroir** |
| 10 | Le CFC vend une Licence Veille Web couvrant crawling, scraping, indexation et mise à disposition sous forme de liens ou d'analyses | cfcopies.com/secteurs/entreprises-plateformes/plateformes-de-veille-d-information — 2 oct. 2026 | « **LICENCE VEILLE WEB** — Pour les actes de crawling des sites de presse (extraction, reproduction et indexation, scraping) et la mise à disposition de cette veille à des entreprises clientes, sous forme de liens ou d'analyses des contenus » | Lu de première main sur le site de l'OGC. **Aucun tarif obtenu.** | **B** (existence et périmètre) ; prix : **non vérifié** |
| 11 | Cascade de licences chez le client | cfcopies.com/secteurs/entreprises-plateformes/entreprises-privees-et-publiques — 2 oct. 2026 | « le CFC signe avec celles-ci des licences qui autorisent leur activité **jusqu'à la livraison des contenus à leurs clients. Si ces contenus sont ensuite rediffusés par l'entreprise destinataire, celle-ci doit à son tour obtenir du CFC une licence** » | Lu de première main. | **B** |
| 12 | DVP est l'OGC du droit voisin de la presse, créé le 26 oct. 2021 par 74 éditeurs et agences | dvpresse.fr — 2 oct. 2026 | « DVP a été créé le **26 octobre 2021 par 74 éditeurs et agences de presse** pour gérer le nouveau droit voisin » | Lu de première main. **Aucun tarif, aucune pratique à l'égard d'un service de veille.** | **B** (existence) ; pratique tarifaire : **non vérifié** |
| 13 | Leboncoin / Entreparticuliers : indexation avec reprise des critères essentiels = extraction prohibée ; finalité indifférente ; sous-base protégée ; injonction visant l'extraction répétée et systématique de parties non substantielles | legalis.net, CA Paris pôle 5 ch. 1, 2 févr. 2021 n° 17/17688 — 2 oct. 2026 ; cassation 5 oct. 2022 n° 21-16.307 par presse.leboncoincorporate.com et lexbase.fr | « **ne relevant pas de la liberté de lier sur internet, mais d'une extraction prohibée par l'article L. 342-1** » ; « **peu importe le but poursuivi par celui qui procède à l'extraction** » ; « extraction ou la réutilisation **répétée et systématique de parties qualitativement ou quantitativement non substantielles** » | Dispositif et motifs d'appel lus de première main sur legalis. **Arrêt de cassation non lu** — deux commentaires concordants. | **B** pour l'appel ; **C** pour la cassation |
| 14 | L341-1, L342-1, L342-2, L342-3 CPI | legifrance (extrait d'index), senat.fr/leg/pjl97-344.html, doctrine.fr — 2 oct. 2026 | L341-1 : « **investissement financier, matériel ou humain substantiel** […] Cette protection est indépendante et s'exerce **sans préjudice** » ; L342-3 1° et « **Toute clause contraire au 1° ci-dessus est nulle.** » | Travaux de transposition + miroirs. **Numérotation actuelle non confirmée sur Légifrance.** | **B-miroir** |
| 15 | Sanction pénale, 3 ans / 300 000 €, article L343-4 (ex-L343-1) | baumann-avocats.com, canevet.org, droit-technologie.org — 2 oct. 2026 | « Est puni de **trois ans d'emprisonnement et de 300 000 euros d'amende** le fait de porter atteinte aux droits du producteur d'une base de données tels que définis à l'article L. 342-1. » | Trois sources secondaires concordantes. **Numéro d'article incertain** (L343-1 porte aujourd'hui la saisie-contrefaçon). | **C** |
| 16 | robots.txt : un fichier restrictif détruit la base légale RGPD et l'exception de fouille ; un fichier permissif ne donne rien | cnil.fr/fr/focus-interet-legitime-collecte-par-moissonnage (19 juin 2025) et cnil.fr/fr/node/165906 — 2 oct. 2026 | « **le traitement ne pourra pas entrer dans les attentes raisonnables des personnes si son responsable n'exclut pas de la collecte les sites qui s'opposent clairement au moissonnage** par l'intermédiaire des protocoles d'exclusion robots.txt ou de CAPTCHA » ; « **unless the rightholders have reserved their rights in an appropriate manner, in particular by machine-readable means** […] This includes metadata and terms and conditions of a website » | Fiche CNIL lue de première main, deux versions linguistiques. **L'asymétrie est ma lecture**, la CNIL ne la formule pas en ces termes. | **B** (passages) ; asymétrie : **B appliqué** |
| 17 | L111-7-2 C. consom. et décret 2017-1436, art. D111-16 à D111-19 | hr-infos.fr PDF du JO n° 233 du 5 oct. 2017 ; doctrine.fr pour L111-7-2 — 2 oct. 2026 | « **à titre principal ou accessoire, à collecter, à modérer ou à diffuser des avis en ligne** » ; « **La date de publication de chaque avis, ainsi que celle de l'expérience de consommation concernée par l'avis** » ; « **Le délai maximum de publication et de conservation d'un avis** » | **Texte du JO lu de première main.** L111-7-2 sur miroir, avec mention d'une modification en vigueur au 17 févr. 2024 (loi 2024-449) **non vérifiée**. | **B** pour le décret ; **B-miroir** pour L111-7-2, rédaction actuelle **non vérifiée** |
| 18 | L121-4 27° et 28° C. consom. | legifrance.gouv.fr/codes/article_lc/LEGIARTI000044563107 — 2 oct. 2026 | « **27° D'affirmer que des avis sur un produit sont diffusés par des consommateurs qui ont effectivement utilisé ou acheté le produit sans avoir pris les mesures nécessaires pour le vérifier ; 28° […] ou modifier des avis de consommateurs** » | Extrait Légifrance obtenu, verbatim. | **B** |
| 19 | RGPD : intérêt légitime au cas par cas en cas 3 ; art. 14 et source des données ; opposition préalable et liste repoussoir ; art. 9 | cnil.fr PDF recommandations réutilisateurs (2024) ; cnil.fr page du 30 avril 2020 ; fiche moissonnage du 19 juin 2025 — 2 oct. 2026 | « **l'intérêt légitime du réutilisateur doit être apprécié au cas par cas** » ; « les informations prévues à l'**article 14 du RGPD et notamment celle relative à la source des données** » ; « prévoir un **droit d'opposition discrétionnaire et préalable** […] mécanismes de « **liste repoussoir** » » ; « **exclure automatiquement la collecte de données sensibles non pertinentes** » | Trois documents CNIL lus de première main. **L'art. 14.5.b est mon apport** : la CNIL ne le cite pas dans ces pages. | **B** pour les passages ; art. 14.5.b : **B appliqué**, à confirmer par un juriste |
| 20 | LCEN art. 6, critère éditeur/hébergeur, et droit de réponse art. 6-IV | conseil-constitutionnel.fr (Nouveaux Cahiers) ; cornucopiae.fr PDF version consolidée au 11 juill. 2024 — 2 oct. 2026 | « **le contrôle ou l'absence de contrôle sur le contenu accessible sur le site est le critère départageur** » ; « **Toute personne nommée ou désignée dans un service de communication au public en ligne dispose d'un droit de réponse** » | Article doctrinal sur site officiel + PDF miroir de la loi. **Loi non lue sur Légifrance.** | **C** |
| 21 | Règlement IA, art. 50(1)(2)(4) | doctrine.fr, reproduction du règlement 2024/1689 — 2 oct. 2026 | « **marquées dans un format lisible par machine** » ; « ne modifient pas de manière substantielle les données d'entrée » ; « **lorsque le contenu généré par l'IA a fait l'objet d'un processus d'examen humain ou de contrôle éditorial et lorsqu'une personne physique ou morale assume la responsabilité éditoriale** » | Texte de l'article lu intégralement sur miroir. EUR-Lex FR atteint pour les considérants seulement. | **B-miroir** |
| 22 | Calendrier art. 50 (2 août 2026), règlement 2026/1744, transition du 2 déc. 2026, sanctions art. 99(4) | maconformite.fr, donneespersonnelles.fr, rgpdkit.fr, gdroit.fr — 2 oct. 2026 | « L'article 50 est applicable depuis le 2 août 2026 […] Le règlement (UE) 2026/1744 […] n'a pas reporté cette date » ; « jusqu'à 15 millions d'euros ou 3 % du chiffre d'affaires annuel mondial » | Quatre sources secondaires concordantes. **Règlement 2026/1744 non lu.** | **C** |
| 23 | Art. 349 TFUE, Guadeloupe RUP, champs des mesures spécifiques | eur-lex.europa.eu CELEX 12008E349 — 2 oct. 2026 | « Compte tenu de la situation économique et sociale structurelle de la **Guadeloupe** […] le Conseil […] arrête des mesures spécifiques » ; « **sans nuire à l'intégrité et à la cohérence de l'ordre juridique de l'Union, y compris le marché intérieur** » | Texte du traité lu de première main. | **B** |

## Pour chaque acteur cité comme faisant déjà ce travail : par quel guichet, à quel degré, et comment je le sais

| Acteur | Guichet | Degré si 5 | Comment je le sais | Cran |
|---|---|---|---|---|
| **Meltwater** (veille média) | **4 — licence de contenu** | — | Résumé de presse UKSC [2013] UKSC 18 : Meltwater s'était engagé à entrer dans la *Web Database Licence* de la NLA ; et l'arrêt dit verbatim « Nothing in article 5.1 stops Meltwater needing a licence to upload copyright material on their website ». | **B** |
| **Les plateformes de veille françaises** (non nommées) | **4** | — | Le CFC publie et vend trois licences de veille, dont la Licence Veille Web, et déclare signer « avec celles-ci » des licences. L'existence de l'offre établit le guichet du secteur ; **je n'ai nommé aucune société** et je ne le ferai pas faute de l'avoir vérifié société par société. | **B** pour le guichet du secteur ; **inconnu** par société |
| **Entreparticuliers.com** | **5c** — et il a perdu | 5c | CA Paris 2 févr. 2021 n° 17/17688, confirmé Cass. 1re civ. 5 oct. 2022 n° 21-16.307 : atteinte au droit du producteur, extraction prohibée malgré l'hyperlien. | **B** (appel) / **C** (cassation) |
| **PR Aviation BV** | **5c** | 5c | C-30/14 : a perdu l'argument selon lequel la directive 96/9 ferait obstacle aux limitations contractuelles. **Mais l'issue finale au fond, devant le Hoge Raad, m'est inconnue** — voir D2. Donc « a perdu » n'est établi que sur le moyen préjudiciel. | **B** sur le moyen ; **D2** sur l'issue |
| **Agences tierces sur Google Business Profile** | **3 — API avec autorisation déléguée** | — | Politiques Google lues de première main : accès gestionnaire + OAuth, projet d'API au nom du client, interdiction de l'accès indirect. Ce n'est pas le guichet 2 du document. | **B** |
| **Connectivity Providers Booking.com** | **1 — partenariat certifié** | — | GDT, définition de « Connectivity Provider » : accord de partenariat de connectivité conclu avec Booking.com. Flux d'autorisation par lien dans l'API de contractualisation. | **B** |
| **Gestionnaires d'avis et channel managers du secteur hôtelier** (le document écrit « ⏳ noms à établir en V1 ») | **inconnu** | — | **Je n'en ai établi aucun.** Je ne fournis pas de liste : le §4.3 interdit le compte d'outils, et une liste non vérifiée serait du C déguisé en B. | **inconnu** |

## Reclassement final de chaque conclusion de ce retour

| Conclusion | Cran |
|---|---|
| F1 — le guichet 2 tel que décrit n'est pas la voie sanctionnée par Google ni par Booking | **B** |
| F1 — les GDT Booking interdisent expressément la remise d'identifiants | **non vérifié** |
| F2 — le dispositif de C-30/14 est négatif et réservé au droit national ; le document le sur-lit | **B** |
| F2 — la contraposée du §39-40 ouvre des droits impératifs d'utilisateur licite | **B appliqué**, confirmation juriste requise |
| F3 — la ligne Meltwater du document est fausse : l'utilisateur final a gagné | **B** |
| F4 — le droit voisin L218-2 et le test de substituabilité font tomber « guichet 6 » pour la presse | **B-miroir** |
| F4 — l'activité relève de la Licence Veille Web du CFC | **B** |
| F5 — « on cite, on résume, on lie » a été jugé insuffisant | **B** (appel) |
| F6 — l'asymétrie du robots.txt | **B** (passages CNIL) + **B appliqué** |
| M1 — L111-7-2 et D111-17 imposent la date de l'expérience de consommation | **B** pour le décret, **B-miroir** pour la loi, rédaction 2024 **non vérifiée** |
| M2 — L121-4 27° et 28° | **B** |
| M3 — chaîne RGPD complète | **B** pour les passages, **B appliqué** pour l'art. 14.5.b, **D7** pour l'AIPD |
| M4 — droit d'auteur et droit moral sur les avis | **D6** |
| M5 — parasitisme autonome | **D1** |
| M6 — qualification d'éditeur et responsabilité 1881 | **C** |
| M7 — art. 50 du règlement IA, contenu | **B-miroir** ; calendrier et sanctions **C** |
| M8 — organe registre juridique manquant | **A-usage** (constat de lecture du document lui-même) |
| Verdict et ses cinq conditions | **B appliqué** — construit sur des lignes B, à valider par un juriste avant tout engagement |

---

## Les cinq colonnes

### 1. MCP à installer

| MCP | Ce qu'il débloque | Prérequis |
|---|---|---|
| **MCP Légifrance / API DILA (PISTE)** | La lecture de première main du CPI, du Code de la consommation et de la LCEN, avec les **numéros d'article et dates d'entrée en vigueur en vigueur**. C'est le manque qui a forcé neuf de mes lignes en « B-miroir » ou en C. Débloque aussi la rédaction actuelle de L111-7-2 depuis la loi 2024-449. | Compte PISTE et clé OAuth. Autorisation de sortie vers `legifrance.gouv.fr` / `api.piste.gouv.fr`. |
| **MCP EUR-Lex / CELEX** | Le texte verbatim des règlements et arrêts sans intermédiaire : règlement 2024/1689 en FR, règlement 2026/1744 (non lu), directive 96/9, directive 2019/790, arrêt C-360/13. | Ouverture de sortie vers `eur-lex.europa.eu`. Aucun compte. |
| **MCP Judilibre (Cour de cassation, open data)** | Le texte intégral de Cass. 1re civ. 5 oct. 2022 n° 21-16.307, et la recherche systématique de la jurisprudence de scraping et de parasitisme — qui est exactement la ligne D1 que je n'ai pas pu sortir du cran D. | Clé API Judilibre via PISTE. |

### 2. Logiciels manquants

Rien d'exotique. Ce qui a plafonné ce retour n'est pas l'outillage, c'est le **blocage de sortie
réseau**. Il faut, par ordre d'importance : l'ouverture de `legifrance.gouv.fr`,
`eur-lex.europa.eu`, `curia.europa.eu`, `bailii.org`, `tripadvisor.com`,
`tripadvisor.mediaroom.com`, `partner.booking.com`. Sans cela, aucun agent de cette chaîne ne
produira un B sur le droit français, et le §4.2 du document (« aucune décision sur un cran B ou
moins ») restera inapplicable à la vague V1 tout entière.

### 3. Outils déjà disponibles et non exploités

- **La récupération côté serveur du MCP EXA** : c'est la seule route qui a atteint EUR-Lex dans cette
  session, et je ne l'ai essayée **qu'après** trois échecs de récupération directe. À faire en premier,
  pas en dernier, pour tout domaine institutionnel.
- **La compétence tableur** (`xlsx`) : les répertoires du CFC sont des xlsx publics. Je ne les ai pas
  ouverts. C'est la réponse à la question V0 décisive — les titres guadeloupéens sont-ils couverts.
- **La compétence PDF** : le JO du décret 2017-1436, les notices tarifaires du CFC et les contrats de
  licence CFC sont des PDF. Je n'ai lu la licence veille audiovisuelle que par extraits de moteur.
  Les **tarifs** du guichet 4 — c'est-à-dire le chiffrage du volet presse — sont dans ces PDF.

### 4. IA existantes qui font déjà ce travail, et à quel prix

**Aucun prix dans cette colonne, et c'est une décision assumée.** Le §4.3 du document interdit
« gratuit » pour ce qui est gratuit en essai, et toute somme que j'avancerais ici serait du C. Ce que
je peux dire, sourcé :

- **Veille presse** : les titulaires du marché sont les plateformes de veille sous licence CFC. Le
  **prix du droit d'accès** — pas celui de l'outil — se lit dans les notices tarifaires publiées par le
  CFC sur `cfcopies.com`. C'est le premier chiffre à aller chercher, parce qu'il décide du périmètre
  avant tout banc d'essai.
- **Avis, côté Google** : le **rapport de performance Business Profile** est fourni par Google et est
  l'étalon naturel de l'organe Avis. La politique tierce de Google impose même, verbatim, que tout outil
  agrégeant des données multi-plateformes « must also separately provide the Google Business Profile
  location performance report and its required fields » (support.google.com/business/answer/7353941,
  2 oct. 2026, **B**). Autrement dit : l'étalon est obligatoire, pas optionnel. Il faut le mesurer en V2
  avant de reconstruire quoi que ce soit.
- **Rédaction assistée** : je n'ai rien mesuré, donc je ne nomme rien. Ce que j'apporte à la place est
  une **contrainte de sélection** que le document n'avait pas : tout fournisseur retenu doit s'engager
  **par écrit** à marquer ses sorties en format lisible par machine au sens de l'art. 50(2) du règlement
  IA. Cet engagement écrit vaut diligence et conditionne le choix du modèle. C'est un critère d'achat,
  pas un critère de performance.

### 5. Futurs possibles à douze mois

- ⏳ **2 décembre 2026 — marquage lisible par machine de l'art. 50(2)** pour les systèmes génératifs mis
  sur le marché avant le 2 août 2026 (art. 111(4), issu du règlement 2026/1744 — **cran C, à confirmer
  sur EUR-Lex**). Si l'organe Rédaction s'appuie sur un modèle tiers, obtenir l'engagement de marquage
  du fournisseur **maintenant**, par écrit.
- ⏳ **2 décembre 2027 et 2 août 2028 — annexes haut risque** reportées (annexe III puis annexe I,
  **cran C**). Ne concerne ce projet **que si** le produit se met à noter ou profiler des personnes —
  auteurs d'avis, clients. Décision d'architecture à prendre consciemment, pas par dérive.
- ⏳ **Rédaction de L111-7-2 C. consom.** modifiée en vigueur au 17 février 2024 par la loi 2024-449, et
  susceptible d'évoluer au prochain texte DDADUE. À relire **chaque année** sur Légifrance ; la
  fonctionnalité gratuite de signalement d'authenticité est la partie la plus récente et la plus
  instable.
- ⏳ **Pratique tarifaire de DVP à l'égard des services en ligne autres que les moteurs de recherche.**
  DVP s'est constituée en 2021 face aux grandes plateformes ; un service de veille commerciale est une
  cible plausible et non encore éprouvée. Mieux vaut aller au-devant d'une demande que de la découvrir.
- ⏳ **Suites annoncées par la CNIL** : recommandations sur le statut d'un modèle d'IA au regard du RGPD,
  sur la sécurité du développement, et sur l'annotation des données (annoncées dans la publication du
  19 juin 2025, **B**). Elles porteront directement sur l'organe Provenance et sur la question de la
  conservation laissée ouverte en M3.
- ⏳ **Le registre juridique comme produit.** Si les obligations de M1, M2, M3 et M7 se durcissent — et
  tout indique qu'elles se durcissent — l'organe de registre juridique décrit en M8 cesse d'être un coût
  de conformité et devient ce que le §1 du document cherche : une couche de vérifiabilité que personne
  ne vend, avec son étalon propre et son client propre.
