---
id: note-competitors-scorecard-guide-001
type: reference
effective_date: 2026-09-03
confidence: direct
---

# Competitor scorecards — how these work

## The contract

| Layer | Mutable? | Rule |
|---|---|---|
| `evidence/competitors/**` | **No** — immutable, additive | One file per source/pass. Never rewrite to reflect a new opinion. Add `ev-comp-<slug>-00N`. |
| `notes/competitors/scorecard/*.md` | **Yes** — overwrite in place | Current best read per competitor. Always cites evidence IDs. |
| `beliefs/*.yaml` | Yes — living | Cross-competitor beliefs. Scorecards feed these; they are not a substitute. |
| `outputs/` | Generated | Never hand-edit. `refresh` renders it. |

So: **new evidence file every time; scorecard edited every time.**

## Status vocabulary (the point of the scorecard)

Every row carries a status. This is what keeps us from repeating the
"Aider rules are Karbon's agent model" mistake.

| Status | Means |
|---|---|
| `VERIFIED` | Observed firsthand — hands-on, screenshots, or product UI. |
| `DOCS` | In first-party docs/help. Specific enough to act on, not observed. |
| `CLAIMED` | Vendor marketing or exec quote. May be roadmap. Do not build on it. |
| `UNSEEN` | Not looked at yet. Say so instead of inferring. |
| `DISPUTED` | Sources conflict, or vendor claim contradicted by observation. |

Rules:

- Never upgrade a status without an evidence ID that justifies it.
- `CLAIMED` for one product area does **not** license conclusions about
  another. Rules/checklists are not evidence about an agent product.
- When a status changes, add a line to that scorecard's Changelog.

## Update procedure

1. New source → create the immutable evidence file first.
2. Open the scorecard. Edit the affected rows only.
3. Update `effective_date`, `Evidence on file`, and Changelog.
4. If it changes a cross-cutting belief, edit `beliefs/`.
5. Run:

```bash
PYTHONPATH=src python3 -m product_os.cli refresh   # validates + renders
PYTHONPATH=src python3 -m product_os.cli lock      # record new evidence hashes
```

## What is enforced mechanically

`validate` (and therefore `refresh`) fails on:

- A locked evidence file that was modified, renamed, or deleted.
- A competitor with evidence but no scorecard.
- A scorecard that does not cite every evidence ID for its competitor
  — this is what forces an update when evidence is added.
- A scorecard citing an evidence ID that does not exist.
- A status outside the vocabulary above.
- A missing `## Changelog` section, or frontmatter without
  `type: living_scorecard`, `competitor`, `effective_date`.

Cite IDs individually. Range shorthand like `ev-comp-x-001..003` is
not a valid citation and will fail.

Genuine corrections to a locked file (typo, bad citation) are allowed
via `lock --accept`, but record them in the Changelog. Do not use it
to rewrite an interpretation — that is what a new evidence file and a
scorecard edit are for.

Source of truth for these checks: `src/product_os/corpus_rules.py`.

## Dimensions

Chosen for the accounting-competitor question, not copied from the
agent-builder matrix (`notes/agent-builders/matrix/_dimension-guide.md`).

- **Stack position** — GL / practice layer / bolt-on. Which layer do
  they own, and what do they replace vs sit beside?
- **What the AI is** — the ledger itself, a role/employee, a rules
  checklist, a step inside a workflow.
- **Unit the user creates** — nothing (system is the agent), an agent,
  a brief, a workflow, a template. Ties to `ins-005`.
- **Cadence** — continuous vs period-end. When humans show up.
- **Autonomy vs control** — auto-post threshold, what needs sign-off.
- **Trust / audit** — verification, audit trail, undo, HITL.
- **Human workflow** — exception inbox vs queue vs chat. What the
  operator actually does daily.
- **Client interaction** — how questions/documents move client-side.
- **Model approach** — specialized ML, frontier LLM, rules, mix.
- **Benchmarks / metrics** — their numbers, with dataset caveats.
- **Xero relationship** — replaces, integrates, migrates off, partners.
- **Ecosystem / MCP** — open tool layer, partners, API.
- **Pricing** — plan shape and what gates what.
- **Scope claimed** — how much of the client lifecycle they say they cover.
- **Threat to XeroForce** — the one-line so-what.
- **Biggest unknown** — the next thing to go get.
