## Task

Given a set of observations (each linked to evidence IDs), propose patterns/themes.

## Rules

- Patterns must cite constituent observation IDs and evidence IDs.
- Include contradictions/counter-evidence if present.
- Avoid superficial keyword clustering.

## Output format

Return JSON:

```json
{
  "patterns": [
    {
      "id": "pat-...",
      "title": "...",
      "description": "...",
      "observation_ids": ["obs-..."],
      "evidence_ids": ["ev-..."],
      "domains": ["agent_builder"],
      "support_count": 0,
      "contradicting_evidence_ids": [],
      "confidence": "low|medium|high"
    }
  ]
}
```

