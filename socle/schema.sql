-- =====================================================================
-- SOCLE — schéma de provenance et fondation des quatre outils
-- Périmètre tenu : veille à provenance prouvée + publication sociale
--                  + gestion des avis + blog
-- Version 1 — 2 octobre 2026
--
-- PRINCIPE DIRECTEUR : une capture est un FAIT IMMUABLE. Tout le reste
-- en dérive et se recalcule. On n'écrase jamais une capture, on en
-- ajoute une nouvelle. C'est ce qui rend une ligne rejouable un an plus tard.
--
-- RÈGLE ABSOLUE : aucun secret, aucun jeton, aucun mot de passe dans
-- cette base. Voir la table acces_confie : elle ne porte que des
-- RÉFÉRENCES vers un coffre loué.
-- =====================================================================

PRAGMA journal_mode = WAL;
PRAGMA foreign_keys = ON;

-- ---------------------------------------------------------------------
-- 0. CLIENTS — cloisonnement dès la première ligne
-- Même avec un seul client, la colonne existe. L'ajouter plus tard
-- impose de réécrire toutes les requêtes du produit.
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS client (
  id                INTEGER PRIMARY KEY,
  nom               TEXT    NOT NULL UNIQUE,
  siret             TEXT,
  fuseau            TEXT    NOT NULL DEFAULT 'America/Guadeloupe', -- UTC-4, sans heure d'été
  ts_cree_utc       TEXT    NOT NULL,
  actif             INTEGER NOT NULL DEFAULT 1
);

-- ---------------------------------------------------------------------
-- 1. SOURCES — la qualification guichet par guichet, SOURCE PAR SOURCE
-- Le registre de qualification vit ici, en base, pas dans un document
-- séparé qui se désynchronise.
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS source (
  id                INTEGER PRIMARY KEY,
  nom               TEXT    NOT NULL,
  url_base          TEXT    NOT NULL UNIQUE,
  -- guichet au sens de la section 2.2 du prompt de lancement
  guichet           TEXT    NOT NULL CHECK (guichet IN ('1','2','3','4','5a','5b','5c','6')),
  -- licence : identifiant SPDX quand il existe, sinon nom exact + URL
  licence_spdx      TEXT,
  licence_nom       TEXT,
  licence_url       TEXT,
  licence_lue_le    TEXT,       -- date de lecture EFFECTIVE du texte de licence
  attribution_texte TEXT,       -- la mention exacte à réafficher, mot pour mot
  cgu_url           TEXT,
  cgu_lues_le       TEXT,
  robots_lu_le      TEXT,
  debit_max_rps     REAL    NOT NULL DEFAULT 0.5,   -- plafond de politesse
  verdict           TEXT    NOT NULL CHECK (verdict IN ('retenu','retenu_sous_conditions','ecarte')),
  motif_verdict     TEXT    NOT NULL,
  -- une source non qualifiée ne doit JAMAIS être collectée
  ts_cree_utc       TEXT    NOT NULL,
  ts_modifie_utc    TEXT,
  actif             INTEGER NOT NULL DEFAULT 1
);

-- Garde-fou : on ne collecte pas une source écartée.
CREATE TRIGGER IF NOT EXISTS source_ecartee_inactive
AFTER UPDATE OF verdict ON source
WHEN NEW.verdict = 'ecarte'
BEGIN
  UPDATE source SET actif = 0 WHERE id = NEW.id;
END;

-- ---------------------------------------------------------------------
-- 2. CAPTURE — le fait immuable. C'EST LE CŒUR DE LA PROVENANCE.
--
-- Comment on rejoue une ligne un an plus tard :
--   1. sha256_corps identifie l'octet-à-octet reçu
--   2. chemin_archive pointe le fichier conservé, nommé par ce sha256
--   3. on recalcule le sha256 du fichier : s'il correspond, l'archive est intacte
--   4. ts_capture_utc dit QUAND, agent_utilisateur et version_collecteur disent AVEC QUOI
--   5. on relance l'extraction avec outil + version_outil + parametres_json
--      enregistrés dans la table extraction, et on compare texte_sha256
-- Si les deux empreintes tombent, la ligne est prouvée. Sinon, on sait
-- exactement laquelle des deux étapes a bougé.
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS capture (
  id                 INTEGER PRIMARY KEY,
  source_id          INTEGER NOT NULL REFERENCES source(id),
  url_demandee       TEXT    NOT NULL,
  url_finale         TEXT    NOT NULL,          -- après redirections
  ts_capture_utc     TEXT    NOT NULL,          -- ISO 8601 avec Z. Toujours UTC en stockage.
  http_statut        INTEGER NOT NULL,
  http_etag          TEXT,
  http_last_modified TEXT,
  type_mime          TEXT,
  encodage           TEXT,
  octets             INTEGER NOT NULL,
  sha256_corps       TEXT    NOT NULL,          -- empreinte de ce qui est RÉELLEMENT arrivé
  chemin_archive     TEXT    NOT NULL,          -- fichier .gz nommé par sha256_corps
  agent_utilisateur  TEXT    NOT NULL,
  version_collecteur TEXT    NOT NULL,
  UNIQUE (url_finale, sha256_corps)             -- une même page inchangée ne se duplique pas
);
CREATE INDEX IF NOT EXISTS idx_capture_source_ts ON capture(source_id, ts_capture_utc);
CREATE INDEX IF NOT EXISTS idx_capture_sha       ON capture(sha256_corps);

-- Une capture ne se modifie jamais.
CREATE TRIGGER IF NOT EXISTS capture_immuable
BEFORE UPDATE ON capture
BEGIN
  SELECT RAISE(ABORT, 'capture immuable : ajouter une nouvelle capture, jamais modifier');
END;

-- ---------------------------------------------------------------------
-- 3. EXTRACTION — dérivation re-calculable d'une capture
-- Plusieurs extractions par capture sont permises et souhaitables :
-- c'est ainsi qu'on compare deux extracteurs sur le même jeu figé.
--
-- langue_avant_normalisation : LEÇON MESURÉE le 2 octobre 2026.
-- Dépouiller les accents avant la détection de langue fait tomber la
-- reconnaissance du créole guadeloupéen de 10/10 à 6/10, et la marge
-- gcf contre créole haïtien de +56,6 à +1,1. Le français, l'anglais et
-- l'espagnol n'en souffrent pas. Ce champ atteste que la détection a
-- bien eu lieu sur le texte accentué.
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS extraction (
  id                  INTEGER PRIMARY KEY,
  capture_id          INTEGER NOT NULL REFERENCES capture(id),
  outil               TEXT    NOT NULL,
  version_outil       TEXT    NOT NULL,
  parametres_json     TEXT    NOT NULL DEFAULT '{}',
  ts_extraction_utc   TEXT    NOT NULL,
  titre               TEXT,
  auteur              TEXT,
  date_publication    TEXT,                     -- telle que DÉCLARÉE par la source
  texte               TEXT    NOT NULL,
  sha256_texte        TEXT    NOT NULL,
  langue_code         TEXT,                     -- fr / gcf / en / es / ht ...
  langue_marge        REAL,                     -- écart au second candidat
  langue_detecteur    TEXT,
  langue_avant_normalisation INTEGER NOT NULL DEFAULT 1
                      CHECK (langue_avant_normalisation = 1),
  UNIQUE (capture_id, outil, version_outil, parametres_json)
);
CREATE INDEX IF NOT EXISTS idx_extraction_capture ON extraction(capture_id);
CREATE INDEX IF NOT EXISTS idx_extraction_langue  ON extraction(langue_code);

-- ---------------------------------------------------------------------
-- 4. INDEX PLEIN TEXTE
-- remove_diacritics est volontairement ABSENT : on garde les accents.
-- C'est ce qui permet de chercher « manjé » et de ne pas détruire le
-- créole. La recherche sans accent se fait côté requête, pas côté index.
-- ---------------------------------------------------------------------
CREATE VIRTUAL TABLE IF NOT EXISTS texte_idx USING fts5 (
  titre, corps,
  extraction_id UNINDEXED,
  url           UNINDEXED,
  langue        UNINDEXED,
  tokenize = 'unicode61'
);

-- ---------------------------------------------------------------------
-- 5. ASSERTION — l'unité qui sera PUBLIÉE, et qui doit se défendre
-- Chaque assertion remonte à une extraction, donc à une capture, donc à
-- une source primaire datée et hachée. C'est l'étalon « part des
-- assertions remontées à une source primaire ».
--
-- Les champs légaux sont des CHAMPS, pas des promesses :
--   genere_par_ia / mention_ia_affichee : obligation de signaler un
--     contenu généré
--   relu_par_humain + relecteur + ts_relecture_utc : la trace de
--     relecture humaine AVANT publication. Irrécupérable après coup.
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS assertion (
  id                  INTEGER PRIMARY KEY,
  extraction_id       INTEGER NOT NULL REFERENCES extraction(id),
  client_id           INTEGER REFERENCES client(id),
  texte               TEXT    NOT NULL,         -- le fait tel qu'il sera publié
  citation_exacte     TEXT,                     -- l'extrait verbatim qui le fonde
  offset_debut        INTEGER,
  offset_fin          INTEGER,
  ts_assertion_utc    TEXT    NOT NULL,
  genere_par_ia       INTEGER NOT NULL DEFAULT 0,
  modele_ia           TEXT,
  version_modele_ia   TEXT,
  mention_ia_affichee INTEGER NOT NULL DEFAULT 0,
  relu_par_humain     INTEGER NOT NULL DEFAULT 0,
  relecteur           TEXT,
  ts_relecture_utc    TEXT,
  verdict_relecture   TEXT CHECK (verdict_relecture IN (NULL,'accepte','corrige','rejete'))
);
CREATE INDEX IF NOT EXISTS idx_assertion_extraction ON assertion(extraction_id);

-- Un contenu généré par IA ne peut pas être marqué relu sans relecteur nommé.
CREATE TRIGGER IF NOT EXISTS assertion_relecture_nommee
BEFORE INSERT ON assertion
WHEN NEW.relu_par_humain = 1 AND (NEW.relecteur IS NULL OR NEW.ts_relecture_utc IS NULL)
BEGIN
  SELECT RAISE(ABORT, 'relecture humaine declaree sans relecteur ni horodatage');
END;

-- ---------------------------------------------------------------------
-- 6. AVIS — volet 3 du périmètre. La table existe AUJOURD'HUI.
--
-- date_experience_consommation : CONTRAINTE JURIDIQUE IRRÉVERSIBLE.
-- Cette donnée n'est pas reconstituable après coup. Si on ne la capte
-- pas au moment de la collecte, elle est perdue pour toujours. Le champ
-- existe donc avant le volet avis, et le collecteur doit le remplir ou
-- déclarer explicitement qu'il est absent à la source.
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS avis (
  id                           INTEGER PRIMARY KEY,
  source_id                    INTEGER NOT NULL REFERENCES source(id),
  client_id                    INTEGER NOT NULL REFERENCES client(id),
  capture_id                   INTEGER REFERENCES capture(id),
  identifiant_plateforme       TEXT    NOT NULL,
  auteur_affiche               TEXT,
  note                         REAL,
  note_echelle_max             REAL,
  texte                        TEXT,
  langue_code                  TEXT,
  ts_publication_avis          TEXT,
  -- ---- irrécupérable si non capté à l'origine ----
  date_experience_consommation TEXT,
  date_experience_origine      TEXT NOT NULL
      CHECK (date_experience_origine IN ('champ_plateforme','declaratif_client','deduite','absente_a_la_source')),
  -- ------------------------------------------------
  ts_collecte_utc              TEXT    NOT NULL,
  motif_non_publication        TEXT,
  ts_moderation_utc            TEXT,
  reponse_texte                TEXT,
  reponse_genere_par_ia        INTEGER NOT NULL DEFAULT 0,
  reponse_relue_par            TEXT,
  reponse_ts_relecture_utc     TEXT,
  reponse_ts_envoi_utc         TEXT,
  UNIQUE (source_id, identifiant_plateforme)
);
CREATE INDEX IF NOT EXISTS idx_avis_client ON avis(client_id, ts_collecte_utc);

-- ---------------------------------------------------------------------
-- 7. ACCÈS CONFIÉS — la table qui ne contient AUCUN secret
-- L'organe « garde des accès confiés » n'est PAS construit : 97,8
-- années-auteur mesurées sur OpenBao/Vault. On loue un coffre.
-- Cette table ne porte qu'une RÉFÉRENCE vers ce coffre, plus la trace
-- du mandat et le journal. Le garde-fou ci-dessous refuse tout ce qui
-- ressemble à un secret collé par erreur.
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS acces_confie (
  id                INTEGER PRIMARY KEY,
  client_id         INTEGER NOT NULL REFERENCES client(id),
  plateforme        TEXT    NOT NULL,
  reference_coffre  TEXT    NOT NULL,           -- ex: coffre://clients/42/google-business
  portee            TEXT    NOT NULL,           -- ce que le mandat autorise, en clair
  mandat_signe_le   TEXT    NOT NULL,
  mandat_piece      TEXT    NOT NULL,           -- référence du document signé
  ts_revoque_utc    TEXT,
  UNIQUE (client_id, plateforme),
  CHECK (reference_coffre LIKE 'coffre://%'),
  CHECK (length(reference_coffre) < 200),
  CHECK (reference_coffre NOT LIKE '%BEGIN%'),
  CHECK (reference_coffre NOT LIKE '%ya29.%'),
  CHECK (reference_coffre NOT LIKE '%Bearer %')
);

CREATE TABLE IF NOT EXISTS journal_acces (
  id            INTEGER PRIMARY KEY,
  acces_id      INTEGER NOT NULL REFERENCES acces_confie(id),
  ts_utc        TEXT    NOT NULL,
  acteur        TEXT    NOT NULL,               -- humain ou composant nommé
  action        TEXT    NOT NULL,               -- lecture_secret / publication / revocation
  resultat      TEXT    NOT NULL,
  detail        TEXT
);
CREATE INDEX IF NOT EXISTS idx_journal_acces ON journal_acces(acces_id, ts_utc);

-- ---------------------------------------------------------------------
-- 8. PUBLICATION SOCIALE — volet 2 du périmètre
-- Le fuseau est porté explicitement : UTC en stockage, rendu local
-- séparé. La Guadeloupe est à UTC-4 toute l'année ; un champ
-- ts_programme_local sans fuseau déclaré est un bogue de saison.
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS publication (
  id                  INTEGER PRIMARY KEY,
  client_id           INTEGER NOT NULL REFERENCES client(id),
  acces_id            INTEGER REFERENCES acces_confie(id),
  plateforme          TEXT    NOT NULL,
  contenu             TEXT    NOT NULL,
  sha256_contenu      TEXT    NOT NULL,
  assertions_json     TEXT    NOT NULL DEFAULT '[]',  -- ids des assertions qui fondent le contenu
  genere_par_ia       INTEGER NOT NULL DEFAULT 0,
  mention_ia_affichee INTEGER NOT NULL DEFAULT 0,
  -- trace de relecture humaine AVANT envoi : obligatoire si généré par IA
  relu_par_humain     INTEGER NOT NULL DEFAULT 0,
  relecteur           TEXT,
  ts_relecture_utc    TEXT,
  ts_programme_utc    TEXT,
  ts_programme_local  TEXT,
  fuseau              TEXT    NOT NULL DEFAULT 'America/Guadeloupe',
  ts_envoi_utc        TEXT,
  statut              TEXT    NOT NULL DEFAULT 'brouillon'
                      CHECK (statut IN ('brouillon','a_relire','programme','envoye','echec','annule')),
  identifiant_distant TEXT,
  code_erreur         TEXT,
  nb_tentatives       INTEGER NOT NULL DEFAULT 0
);
CREATE INDEX IF NOT EXISTS idx_publication_file ON publication(statut, ts_programme_utc);

-- Rien de généré par IA ne part sans relecture nommée.
CREATE TRIGGER IF NOT EXISTS publication_ia_relue
BEFORE UPDATE OF statut ON publication
WHEN NEW.statut IN ('programme','envoye')
 AND NEW.genere_par_ia = 1
 AND (NEW.relu_par_humain = 0 OR NEW.relecteur IS NULL)
BEGIN
  SELECT RAISE(ABORT, 'contenu genere par IA : relecture humaine nommee obligatoire avant envoi');
END;

-- ---------------------------------------------------------------------
-- 9. BLOG — volet 4 du périmètre
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS article (
  id                  INTEGER PRIMARY KEY,
  client_id           INTEGER NOT NULL REFERENCES client(id),
  titre               TEXT    NOT NULL,
  corps               TEXT    NOT NULL,
  sha256_corps        TEXT    NOT NULL,
  assertions_json     TEXT    NOT NULL DEFAULT '[]',
  langue_code         TEXT    NOT NULL DEFAULT 'fr',
  genere_par_ia       INTEGER NOT NULL DEFAULT 0,
  mention_ia_affichee INTEGER NOT NULL DEFAULT 0,
  relu_par_humain     INTEGER NOT NULL DEFAULT 0,
  relecteur           TEXT,
  ts_relecture_utc    TEXT,
  statut              TEXT    NOT NULL DEFAULT 'brouillon'
                      CHECK (statut IN ('brouillon','a_relire','publie','retire')),
  ts_publication_utc  TEXT,
  url_publiee         TEXT
);

-- ---------------------------------------------------------------------
-- 10. MESURE — la doctrine de preuve vit en base
-- Un étalon sans n, sans intervalle et sans empreinte de jeu d'épreuve
-- n'est pas opposable. La table refuse de l'enregistrer autrement.
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS mesure (
  id                INTEGER PRIMARY KEY,
  organe            TEXT    NOT NULL,
  metrique          TEXT    NOT NULL,
  valeur            REAL    NOT NULL,
  n                 INTEGER NOT NULL,
  ic95_bas          REAL    NOT NULL,
  ic95_haut         REAL    NOT NULL,
  sha256_jeu        TEXT    NOT NULL,       -- empreinte du jeu d'épreuve, figé AVANT la mesure
  jeu_fige_le       TEXT    NOT NULL,
  outil             TEXT    NOT NULL,
  version_outil     TEXT    NOT NULL,
  cran_preuve       TEXT    NOT NULL CHECK (cran_preuve IN ('A-mesure','A-usage','B','C','D')),
  ts_mesure_utc     TEXT    NOT NULL,
  CHECK (jeu_fige_le <= ts_mesure_utc)      -- le jeu est figé avant, pas après
);

-- ---------------------------------------------------------------------
-- 11. DEMANDE DE RETRAIT — obligation du 2.3 du prompt de lancement
-- « Retrait sous demande de l'éditeur, procédure écrite et tenue. »
-- Une procédure sans table est une promesse.
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS demande_retrait (
  id                INTEGER PRIMARY KEY,
  source_id         INTEGER REFERENCES source(id),
  url_visee         TEXT,
  demandeur         TEXT    NOT NULL,
  ts_recue_utc      TEXT    NOT NULL,
  ts_traitee_utc    TEXT,
  action            TEXT CHECK (action IN (NULL,'retire','refuse','sans_objet')),
  detail            TEXT
);

-- ---------------------------------------------------------------------
-- VUES de contrôle — les étalons de provenance se lisent directement
-- ---------------------------------------------------------------------
CREATE VIEW IF NOT EXISTS v_etalon_provenance AS
SELECT
  (SELECT count(*) FROM assertion)                                      AS assertions,
  (SELECT count(*) FROM assertion a JOIN extraction e ON e.id=a.extraction_id
                   JOIN capture c ON c.id=e.capture_id)                 AS remontables,
  (SELECT count(*) FROM assertion a JOIN extraction e ON e.id=a.extraction_id
                   JOIN capture c ON c.id=e.capture_id
                   WHERE c.ts_capture_utc IS NOT NULL)                  AS datees,
  (SELECT count(*) FROM assertion a JOIN extraction e ON e.id=a.extraction_id
                   JOIN capture c ON c.id=e.capture_id
                   WHERE c.sha256_corps IS NOT NULL
                     AND c.chemin_archive IS NOT NULL)                  AS rejouables;

CREATE VIEW IF NOT EXISTS v_sources_actives AS
SELECT id, nom, url_base, guichet, licence_spdx, licence_nom, licence_url,
       licence_lue_le, attribution_texte, cgu_lues_le, verdict, motif_verdict,
       debit_max_rps
FROM source WHERE actif = 1 AND verdict <> 'ecarte';
