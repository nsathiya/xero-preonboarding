---
id: note-backlog-001
type: reference
effective_date: 2026-09-03
confidence: direct
---

# Backlog — harness and research debt

Deferred work on the harness itself. Research questions live in
`outputs/experiments.md` (generated from `beliefs/`), not here.

## Harness

### Extend scorecards to agent builders

**Status:** TODO. Deferred 2026-09-03.

Competitors have living scorecards with deterministic enforcement
(`src/product_os/corpus_rules.py`): a competitor with evidence but no
scorecard fails validation, and a scorecard that does not cite all of
its evidence fails as stale.

Agent builders have none of that. They use the older observation
matrix (`notes/agent-builders/matrix/*.md`), which is:

- free-form against `_dimension-guide.md` — no status vocabulary, so
  there is no mechanical difference between "we saw this" and "their
  docs say this";
- not staleness-checked — new Notion/Viktor/Zapier evidence can land
  without the matrix moving;
- inconsistent in coverage (Zapier has one pass; HubSpot is skipped).

What to do:

1. Decide whether the matrix becomes a scorecard or gains a scorecard
   beside it. The matrix is a capture template; a scorecard is a
   current read. They are not the same artifact.
2. Add `VERIFIED` / `DOCS` / `CLAIMED` / `UNSEEN` / `DISPUTED` per row.
   Notion is the case for it: help docs claim activity logs
   (`DOCS`), the product did not show them (`DISPUTED`).
3. Generalize `check_scorecards()` in `corpus_rules.py` — it currently
   hardcodes `evidence/competitors/**` and
   `notes/competitors/scorecard/`. Make the domain → scorecard-dir
   mapping a table so agent builders, and later customers, opt in.

Also open: no scorecard or staleness rule exists for the `customer`
domain, which is the next corpus to fill. Worth solving both at once.

### Minor: list items containing a colon render as dicts

`outputs/experiments.md` shows entries like
`{'Counter-evidence': 'firms with highly custom close processes'}`.
`next_evidence` strings with a colon are parsed as YAML maps. Either
quote them at the source or coerce dicts to `k: v` when rendering.
