from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .evidence import EvidenceFile, load_markdown, sha256_text, write_json
from .markdown_sections import extract_bullets, extract_h3_blocks, split_evidence_sections


@dataclass(frozen=True)
class ExtractResult:
    evidence_id: str
    out_path: Path


def _safe_str(v: Any) -> str:
    return "" if v is None else str(v)


def derive_observations_from_evidence(doc: EvidenceFile) -> dict[str, Any]:
    """
    Deterministic extraction:
    - Split raw evidence vs notes
    - For each ### block in Raw evidence, treat bullets/lines as observations
    - Pull follow-ups from Notes (bullets under Notes) into 'follow_ups'
    """
    ev_id = _safe_str(doc.meta.get("id")).strip()
    sections = split_evidence_sections(doc.body)

    obs: list[dict[str, Any]] = []
    for h, content in extract_h3_blocks(sections.raw_evidence):
        bullets = extract_bullets(content)
        if bullets:
            for b in bullets:
                obs.append(
                    {
                        "statement": b,
                        "dimension_hint": h,
                    }
                )
        else:
            # fallback: keep non-empty lines as atomic observations
            for line in [ln.strip() for ln in content.split("\n")]:
                if not line:
                    continue
                if line.startswith("_") and line.endswith("_"):
                    continue
                obs.append({"statement": line, "dimension_hint": h})

    # If there are no ### blocks, fallback to bullets from entire raw evidence
    if not obs:
        for b in extract_bullets(sections.raw_evidence):
            obs.append({"statement": b, "dimension_hint": None})

    follow_ups = extract_bullets(sections.notes)

    payload = {
        "generator_version": "v0.2-deterministic",
        "evidence": {
            "id": ev_id,
            "domain": doc.meta.get("domain"),
            "source_type": doc.meta.get("source_type"),
            "source_name": doc.meta.get("source_name"),
            "date": doc.meta.get("date"),
            "title": doc.meta.get("title"),
            "artifact_path": doc.meta.get("artifact_path"),
        },
        "observations": obs,
        "follow_ups": follow_ups,
    }
    payload["content_sha256"] = sha256_text(json.dumps(payload, sort_keys=True, ensure_ascii=False))
    return payload


def extract_repo(repo_root: Path) -> list[ExtractResult]:
    evidence_dir = repo_root / "evidence"
    out_dir = repo_root / "derived" / "observations"
    out_dir.mkdir(parents=True, exist_ok=True)

    results: list[ExtractResult] = []
    for md_path in sorted([p for p in evidence_dir.rglob("*.md") if p.is_file() and p.name.lower() != "readme.md"]):
        doc = load_markdown(md_path)
        ev_id = _safe_str(doc.meta.get("id")).strip()
        if not ev_id:
            continue

        out = derive_observations_from_evidence(doc)
        out_path = out_dir / f"{ev_id}.observations.json"
        write_json(out_path, out)
        results.append(ExtractResult(evidence_id=ev_id, out_path=out_path))

    return results

