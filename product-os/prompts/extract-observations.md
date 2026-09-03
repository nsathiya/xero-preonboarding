## Task

Extract structured **observations** from the provided evidence items.

## Rules

- Use only the provided evidence text.
- Do not invent provenance, IDs, dates, or claims not supported by evidence.
- Separate observation vs. interpretation.
- If unknown, write "unknown".

## Output format

Return JSON (not Markdown) as:

```json
{
  "observations": [
    {
      "id": "obs-...",
      "evidence_ids": ["ev-..."],
      "statement": "...",
      "dimension": "...",
      "entities": [],
      "sentiment": null,
      "intensity": null,
      "problem": null,
      "job_to_be_done": null,
      "product_area": null,
      "tags": [],
      "confidence": "low|medium|high"
    }
  ]
}
```

