# Beliefs register (source of truth for interpretations)

`outputs/` is **rendered** from this folder. Do not hand-edit `outputs/`.

## What lives here

- `insights.yaml` — living insights (cross-run, cross-product)
- `hypotheses.yaml` — living testable beliefs

Evidence files stay in `evidence/`. These files are **interpretations**. New
evidence should update an existing card (strengthen / weaken / split /
supersede) instead of adding a per-file chapter.

## How synthesize uses this

`product-os synthesize` is deterministic:

1. Writes per-evidence extracts to `derived/raw-synthesis/` (no wall-clock).
2. Loads this register.
3. Resolves cited evidence IDs against the current corpus (titles, products, missing IDs).
4. Renders `outputs/` and a dated report.

Re-running on the same beliefs + same evidence produces the same `outputs/`
bytes (aside from the dated report filename).

## When to edit

After a research session, update the relevant insight/hypothesis here, then:

```bash
PYTHONPATH=src python3 -m product_os.cli refresh
```
