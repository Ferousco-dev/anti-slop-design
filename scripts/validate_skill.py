#!/usr/bin/env python3
"""Validate every skill in skills/ against the Agent Skills spec + this repo's budgets.

Checks:
  - SKILL.md exists, has YAML frontmatter delimited by ---
  - required keys: name, description
  - name is kebab-case, <= 64 chars, and matches its directory name
  - description is 20..1024 chars and says both what and when
  - no unexpected frontmatter keys
  - SKILL.md body stays under the context budget (progressive disclosure)
  - every relative markdown link resolves on disk
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"

ALLOWED_KEYS = {"name", "description", "license", "allowed-tools", "metadata", "version"}
REQUIRED_KEYS = {"name", "description"}
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
BODY_WORD_BUDGET = 3500  # ~5k tokens

errors: list[str] = []
warnings: list[str] = []


def parse_frontmatter(text: str) -> tuple[dict[str, str], str] | tuple[None, None]:
    if not text.startswith("---"):
        return None, None
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, None
    data: dict[str, str] = {}
    key = None
    for line in parts[1].splitlines():
        if not line.strip():
            continue
        if re.match(r"^\s+", line) and key:
            data[key] += " " + line.strip()
            continue
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        data[key] = value.strip().strip('"').strip("'")
    return data, parts[2]


def check_links(md: Path, body: str) -> None:
    for target in LINK_RE.findall(body):
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        resolved = (md.parent / target.split("#", 1)[0]).resolve()
        if not resolved.exists():
            errors.append(f"{md.relative_to(ROOT)}: broken relative link -> {target}")


def validate(skill_dir: Path) -> None:
    rel = skill_dir.relative_to(ROOT)
    md = skill_dir / "SKILL.md"
    if not md.exists():
        errors.append(f"{rel}: missing SKILL.md")
        return

    fm, body = parse_frontmatter(md.read_text(encoding="utf-8"))
    if fm is None:
        errors.append(f"{rel}/SKILL.md: missing or malformed YAML frontmatter")
        return

    for missing in REQUIRED_KEYS - fm.keys():
        errors.append(f"{rel}/SKILL.md: frontmatter missing required key '{missing}'")

    for extra in fm.keys() - ALLOWED_KEYS:
        errors.append(f"{rel}/SKILL.md: unexpected frontmatter key '{extra}'")

    name = fm.get("name", "")
    if name and not NAME_RE.match(name):
        errors.append(f"{rel}/SKILL.md: name '{name}' must be kebab-case")
    if len(name) > 64:
        errors.append(f"{rel}/SKILL.md: name exceeds 64 chars")
    if name and name != skill_dir.name:
        errors.append(f"{rel}/SKILL.md: name '{name}' != directory '{skill_dir.name}'")

    desc = fm.get("description", "")
    if not 20 <= len(desc) <= 1024:
        errors.append(f"{rel}/SKILL.md: description must be 20-1024 chars (is {len(desc)})")
    if desc and not re.search(r"\b(use|when|whenever|before|after)\b", desc, re.I):
        warnings.append(
            f"{rel}/SKILL.md: description should state WHEN to use the skill, not just what it does"
        )

    words = len((body or "").split())
    if words > BODY_WORD_BUDGET:
        errors.append(
            f"{rel}/SKILL.md: body is {words} words, over the {BODY_WORD_BUDGET}-word budget. "
            "Move detail into references/."
        )

    for doc in skill_dir.rglob("*.md"):
        check_links(doc, doc.read_text(encoding="utf-8"))

    print(f"  checked {rel}  ({words} words in body)")


def check_plugin_version() -> None:
    """plugin.json version must match the top CHANGELOG entry.

    Claude Code only ships an update to installed users when this field
    changes. A stale version means a silent no-op release."""
    manifest = ROOT / ".claude-plugin" / "plugin.json"
    changelog = ROOT / "CHANGELOG.md"
    if not manifest.exists() or not changelog.exists():
        return
    import json as _json

    version = _json.loads(manifest.read_text()).get("version")
    m = re.search(r"^## \[(\d+\.\d+\.\d+)\]", changelog.read_text(), re.M)
    latest = m.group(1) if m else None
    if version != latest:
        errors.append(
            f".claude-plugin/plugin.json version '{version}' != CHANGELOG '{latest}'. "
            "Installed users only get updates when this field is bumped."
        )
    else:
        print(f"  plugin version {version} matches CHANGELOG")


def main() -> int:
    if not SKILLS_DIR.is_dir():
        print("no skills/ directory found", file=sys.stderr)
        return 1

    found = [d for d in sorted(SKILLS_DIR.iterdir()) if d.is_dir()]
    if not found:
        print("no skills found under skills/", file=sys.stderr)
        return 1

    print(f"validating {len(found)} skill(s)")
    for skill in found:
        validate(skill)

    check_plugin_version()

    for w in warnings:
        print(f"warning: {w}")
    for e in errors:
        print(f"error: {e}", file=sys.stderr)

    if errors:
        print(f"\n{len(errors)} error(s)", file=sys.stderr)
        return 1
    print("\nall checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
