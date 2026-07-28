# Contributing

The most valuable contribution is a **new slop tell** — a concrete, recognizable pattern that marks output as AI-generated.

## What makes a good contribution

A pattern entry should be:

- **Concrete.** "Purple→indigo gradient hero" is actionable. "Bad color choices" is not.
- **Recognizable.** Someone should be able to spot it in a screenshot in under two seconds.
- **Explained.** Say *why* it became a default — the library, template, or tutorial it cascaded from.
- **Paired with a replacement.** A ban with no alternative just makes the agent hesitant.

## Format

Follow the shape of the existing entries in `skills/anti-slop-design/references/`:

```markdown
### <Pattern name>

**Tell:** what you see.
**Origin:** where the default came from.
**Why it's slop:** the reasoning.
**Instead:** the specific replacement.
```

## Rules

1. **`SKILL.md` stays small.** It is loaded on every trigger. Detail belongs in `references/`. CI enforces a size budget.
2. **Frontmatter is `name` + `description` only** (plus `license`). The `description` must say both *what* the skill does and *when* to use it.
3. **No dead links.** CI checks them.
4. **One pattern per PR** where practical — it makes review and revert clean.
5. **No screenshots of other people's sites** in the repo. Describe the pattern instead.

## Local checks

```bash
python3 scripts/validate_skill.py
```

## Adding a new module

New modules go in `references/NN-name.md`, get a row in the `SKILL.md` references table, and a row in the README module list. Bump the version in `CHANGELOG.md`.

## Releases

Merging to `main` with a `CHANGELOG.md` version bump triggers a tagged release and a `.zip` bundle. You do not need to tag manually.
