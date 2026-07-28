#!/usr/bin/env bash
# Install the anti-slop-design Claude Agent Skill.
#   curl -fsSL https://raw.githubusercontent.com/Ferousco-dev/anti-slop-design/main/install.sh | bash
#   ... | bash -s -- --project   # install into ./.claude/skills instead of ~/.claude/skills
set -euo pipefail

REPO="https://github.com/Ferousco-dev/anti-slop-design.git"
SKILL="anti-slop-design"
DEST="$HOME/.claude/skills"

for arg in "$@"; do
  case "$arg" in
    --project) DEST=".claude/skills" ;;
    --dest=*)  DEST="${arg#--dest=}" ;;
    -h|--help) sed -n '2,4p' "$0"; exit 0 ;;
    *) echo "unknown option: $arg" >&2; exit 1 ;;
  esac
done

command -v git >/dev/null || { echo "git is required" >&2; exit 1; }

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

echo "→ fetching $SKILL"
git clone --depth 1 --quiet "$REPO" "$TMP/repo"

mkdir -p "$DEST"
if [ -d "$DEST/$SKILL" ]; then
  echo "→ replacing existing install at $DEST/$SKILL"
  rm -rf "$DEST/$SKILL"
fi
cp -R "$TMP/repo/skills/$SKILL" "$DEST/$SKILL"

echo "✓ installed to $DEST/$SKILL"
echo "  Run /skills in Claude Code to confirm it is loaded."
