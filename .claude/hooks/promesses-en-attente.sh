#!/usr/bin/env bash
# Signale, en fin de tour, les promesses qui dorment dans le registre.
# Né d'une faute réelle : une compétence annoncée et jamais écrite, que
# Laurent a dû venir réclamer lui-même.
set -uo pipefail

RACINE="${CLAUDE_PROJECT_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)}"
REGISTRE="$RACINE/REGISTRE-DE-DEMARCHE.md"
[ -f "$REGISTRE" ] || exit 0

SECTION=$(awk '/^## 8 — Promesses/,0' "$REGISTRE")
[ -n "$SECTION" ] || exit 0

DUES=$(printf '%s\n' "$SECTION" | grep '⏳' || true)
[ -n "$DUES" ] || exit 0

NOMBRE=$(printf '%s\n' "$DUES" | grep -c . )
# On lit la colonne « Objet promis » du tableau, jamais une coupe à l'aveugle :
# couper des caractères accentués à l'octet produit du charabia.
LISTE=$(printf '%s\n' "$DUES" | awk -F'|' 'NF>2 {o=$2; e=$4; gsub(/\*\*/,"",o); gsub(/\*\*/,"",e); gsub(/^ +| +$/,"",o); gsub(/^ +| +$/,"",e); print "  — " o " (" e ")"}')

jq -n --arg n "$NOMBRE" --arg l "$LISTE" '{
  systemMessage: ("Promesses non tenues dans le registre : " + $n + ".\n" + $l + "\nTenir, ou dire pourquoi non et le porter au registre.")
}'
