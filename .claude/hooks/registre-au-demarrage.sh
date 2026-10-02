#!/usr/bin/env bash
# Injecte le registre de démarche au démarrage d'une session.
# Claude n'a aucune mémoire d'une session à l'autre : ce crochet la lui rend
# sans que personne n'ait à le demander.
set -uo pipefail

RACINE="${CLAUDE_PROJECT_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)}"
REGISTRE="$RACINE/REGISTRE-DE-DEMARCHE.md"
[ -f "$REGISTRE" ] || exit 0

PLAFOND=40000
TAILLE=$(wc -c < "$REGISTRE" | tr -d ' ')

if [ "$TAILLE" -le "$PLAFOND" ]; then
  CORPS=$(cat "$REGISTRE")
  NOTE="Registre complet."
else
  CORPS=$(head -c "$PLAFOND" "$REGISTRE")
  NOTE="TRONQUÉ à $PLAFOND caractères sur $TAILLE. Lis $REGISTRE en entier avant tout travail sur ce projet."
fi

jq -n --arg corps "$CORPS" --arg note "$NOTE" '{
  hookSpecificOutput: {
    hookEventName: "SessionStart",
    additionalContext: ("MÉMOIRE DU PROJET — registre de démarche, à lire avant tout travail.\n\nRègle du registre : une assertion renversée n’est jamais effacée, elle est marquée renversée et par quoi. Ne recrois pas ce qui est tombé. Toute ligne porte un couple provenance·robustesse : 1 et 2 portent une décision, 3 est indicatif, 4 va au dépôt.\n\n" + $note + "\n\n" + $corps)
  },
  suppressOutput: true
}'
