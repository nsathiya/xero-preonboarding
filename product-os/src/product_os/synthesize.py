from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .simple_yaml import loads
from .evidence import write_json


def _read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _md(s: Any) -> str:
    return str(s or "").replace("\r\n", "\n").strip()


def _as_list(v: Any) -> list[str]:
    if v is None:
        return []
    if isinstance(v, list):
        return [str(x).strip() for x in v if str(x).strip()]
    return [str(v).strip()] if str(v).strip() else []


@dataclass(frozen=True)
class CorpusItem:
    evidence_id: str
    domain: str | None
    title: str | None
    source_name: str | None
    evidence_date: str | None
    artifact_path: str | None
    observations: list[dict[str, Any]]
    follow_ups: list[str]


def load_corpus(repo_root: Path) -> list[CorpusItem]:
    obs_dir = repo_root / "derived" / "observations"
    items: list[CorpusItem] = []
    if not obs_dir.exists():
        return items
    for p in sorted([x for x in obs_dir.glob("*.observations.json") if x.is_file()]):
        obj = _read_json(p)
        ev = obj.get("evidence", {})
        ev_id = str(ev.get("id") or "").strip()
        if not ev_id:
            continue
        items.append(
            CorpusItem(
                evidence_id=ev_id,
                domain=ev.get("domain"),
                title=ev.get("title"),
                source_name=ev.get("source_name"),
                evidence_date=ev.get("date"),
                artifact_path=ev.get("artifact_path"),
                observations=list(obj.get("observations") or []),
                follow_ups=list(obj.get("follow_ups") or []),
            )
        )
    return items


def load_beliefs(repo_root: Path) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    insights_path = repo_root / "beliefs" / "insights.yaml"
    hyps_path = repo_root / "beliefs" / "hypotheses.yaml"
    insights_obj = loads(insights_path.read_text(encoding="utf-8")) if insights_path.exists() else {}
    hyps_obj = loads(hyps_path.read_text(encoding="utf-8")) if hyps_path.exists() else {}
    insights = insights_obj.get("insights") if isinstance(insights_obj, dict) else []
    hyps = hyps_obj.get("hypotheses") if isinstance(hyps_obj, dict) else []
    return list(insights or []), list(hyps or [])


def _index_corpus(items: list[CorpusItem]) -> dict[str, CorpusItem]:
    return {it.evidence_id: it for it in items}


def _cite(ids: list[str], by_id: dict[str, CorpusItem]) -> tuple[list[str], list[str]]:
    found: list[str] = []
    missing: list[str] = []
    for ev_id in ids:
        it = by_id.get(ev_id)
        if it:
            found.append(f"`{ev_id}` — {_md(it.title)} ({_md(it.source_name)})")
        else:
            missing.append(ev_id)
    return found, missing


def _uncited_evidence(items: list[CorpusItem], insights: list[dict[str, Any]], hyps: list[dict[str, Any]]) -> list[CorpusItem]:
    cited: set[str] = set()
    for card in insights + hyps:
        cited.update(_as_list(card.get("supporting_evidence_ids")))
        cited.update(_as_list(card.get("counter_evidence_ids")))
    return [it for it in items if it.evidence_id not in cited]


def write_raw_synthesis(repo_root: Path, items: list[CorpusItem]) -> Path:
    """
    Deterministic per-evidence extract. No wall-clock timestamps.
    Same corpus => same JSON bytes.
    """
    out_dir = repo_root / "derived" / "raw-synthesis"
    out_dir.mkdir(parents=True, exist_ok=True)
    payload = {
        "generator_version": "v0.2-deterministic",
        "note": "Mechanical extract only. Living insights live in beliefs/ and outputs/.",
        "evidence": [
            {
                "id": it.evidence_id,
                "domain": it.domain,
                "source_name": it.source_name,
                "date": it.evidence_date,
                "title": it.title,
                "artifact_path": it.artifact_path,
                "observation_count": len(it.observations),
                "observations": it.observations,
                "follow_ups": it.follow_ups,
            }
            for it in items
        ],
    }
    path = out_dir / "per-evidence.json"
    write_json(path, payload)
    return path


def render_current_insights(insights: list[dict[str, Any]], by_id: dict[str, CorpusItem]) -> str:
    lines = [
        "# Current insights (living)",
        "",
        "Beliefs that span runs (and later, products). Evidence IDs are citations, not chapters.",
        "Source of truth: `beliefs/insights.yaml`. Re-run `refresh` after editing that file.",
        "",
    ]
    if not insights:
        lines.append("No insights in `beliefs/insights.yaml` yet.")
        lines.append("")
        return "\n".join(lines)

    for card in insights:
        cid = _md(card.get("id"))
        title = _md(card.get("title") or cid)
        lines.append(f"## {title}")
        lines.append("")
        lines.append(f"- **ID**: `{cid}`")
        lines.append(f"- **Status**: {_md(card.get('status') or 'emerging')}")
        lines.append(f"- **Confidence**: {_md(card.get('confidence') or 'low')}")
        products = _as_list(card.get("products"))
        if products:
            lines.append(f"- **Products**: {', '.join(products)}")
        lines.append("")
        lines.append(_md(card.get("statement")))
        lines.append("")
        if card.get("why_it_matters"):
            lines.append(f"**Why it might matter:** {_md(card.get('why_it_matters'))}")
            lines.append("")

        support_ids = _as_list(card.get("supporting_evidence_ids"))
        cited, missing = _cite(support_ids, by_id)
        lines.append(f"**Supporting evidence** ({len(cited)} in corpus):")
        for row in cited:
            lines.append(f"- {row}")
        if missing:
            lines.append(f"- Missing from corpus: {', '.join(f'`{x}`' for x in missing)}")
        lines.append("")

        counter_ids = _as_list(card.get("counter_evidence_ids"))
        if counter_ids:
            ccited, cmissing = _cite(counter_ids, by_id)
            lines.append("**Counter-evidence:**")
            for row in ccited:
                lines.append(f"- {row}")
            if cmissing:
                lines.append(f"- Missing from corpus: {', '.join(f'`{x}`' for x in cmissing)}")
            lines.append("")
        else:
            lines.append("**Counter-evidence:** none yet")
            lines.append("")

        nxt = _as_list(card.get("next_evidence"))
        if nxt:
            lines.append("**Next evidence to seek:**")
            for row in nxt:
                lines.append(f"- {row}")
            lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def render_hypotheses(hyps: list[dict[str, Any]], by_id: dict[str, CorpusItem]) -> str:
    lines = [
        "# Hypothesis register (living)",
        "",
        "Testable beliefs. Update the same card as new evidence arrives.",
        "Source of truth: `beliefs/hypotheses.yaml`.",
        "",
    ]
    if not hyps:
        lines.append("No hypotheses in `beliefs/hypotheses.yaml` yet.")
        lines.append("")
        return "\n".join(lines)

    for card in hyps:
        cid = _md(card.get("id"))
        title = _md(card.get("title") or cid)
        lines.append(f"## {title}")
        lines.append("")
        lines.append(f"- **ID**: `{cid}`")
        lines.append(f"- **Status**: {_md(card.get('status') or 'proposed')}")
        lines.append(f"- **Confidence**: {_md(card.get('confidence') or 'low')}")
        insight_ids = _as_list(card.get("insight_ids"))
        if insight_ids:
            lines.append(f"- **Derived from**: {', '.join(f'`{x}`' for x in insight_ids)}")
        lines.append("")
        lines.append(_md(card.get("statement")))
        lines.append("")

        support_ids = _as_list(card.get("supporting_evidence_ids"))
        cited, missing = _cite(support_ids, by_id)
        lines.append(f"**Supporting evidence** ({len(cited)} in corpus):")
        for row in cited:
            lines.append(f"- {row}")
        if missing:
            lines.append(f"- Missing from corpus: {', '.join(f'`{x}`' for x in missing)}")
        lines.append("")

        assumptions = _as_list(card.get("assumptions"))
        if assumptions:
            lines.append("**Assumptions:**")
            for row in assumptions:
                lines.append(f"- {row}")
            lines.append("")

        strengthen = _as_list(card.get("what_would_strengthen"))
        if strengthen:
            lines.append("**What would strengthen:**")
            for row in strengthen:
                lines.append(f"- {row}")
            lines.append("")

        falsify = _as_list(card.get("what_would_falsify"))
        if falsify:
            lines.append("**What would falsify:**")
            for row in falsify:
                lines.append(f"- {row}")
            lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def render_implications(insights: list[dict[str, Any]]) -> str:
    lines = [
        "# Implications (living)",
        "",
        "Interpretation, not evidence. Pulled from each insight's “why it might matter.”",
        "",
    ]
    if not insights:
        lines.append("No insights yet.")
        lines.append("")
        return "\n".join(lines)

    for card in insights:
        title = _md(card.get("title") or card.get("id"))
        why = _md(card.get("why_it_matters"))
        if not why:
            continue
        lines.append(f"## {title}")
        lines.append("")
        lines.append(why)
        lines.append("")
        lines.append(f"_From `{_md(card.get('id'))}`._")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def render_experiments(insights: list[dict[str, Any]], hyps: list[dict[str, Any]]) -> str:
    lines = [
        "# Experiments / questions (living)",
        "",
        "Highest-value next evidence, from the living insight and hypothesis cards.",
        "",
    ]
    for card in insights:
        nxt = _as_list(card.get("next_evidence"))
        if not nxt:
            continue
        lines.append(f"## From insight `{_md(card.get('id'))}` — {_md(card.get('title'))}")
        lines.append("")
        for row in nxt:
            lines.append(f"- {row}")
        lines.append("")

    for card in hyps:
        rows = _as_list(card.get("what_would_strengthen")) + _as_list(card.get("what_would_falsify"))
        if not rows:
            continue
        lines.append(f"## From hypothesis `{_md(card.get('id'))}` — {_md(card.get('title'))}")
        lines.append("")
        for row in rows:
            lines.append(f"- {row}")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def render_report(
    items: list[CorpusItem],
    insights: list[dict[str, Any]],
    hyps: list[dict[str, Any]],
    uncited: list[CorpusItem],
) -> str:
    lines = [
        "# Synthesis report",
        "",
        "Deterministic render of the living belief register plus corpus coverage.",
        "",
        "## Evidence in corpus",
        "",
    ]
    for it in items:
        lines.append(f"- `{it.evidence_id}` — {_md(it.title)} ({_md(it.source_name)})")
    if not items:
        lines.append("- (none)")
    lines.append("")

    lines.append("## Current insights")
    lines.append("")
    for card in insights:
        lines.append(f"### {_md(card.get('title') or card.get('id'))}")
        lines.append("")
        lines.append(_md(card.get("statement")))
        lines.append("")
        lines.append(f"- Status: {_md(card.get('status'))} · Confidence: {_md(card.get('confidence'))}")
        lines.append(f"- Evidence: {', '.join(f'`{x}`' for x in _as_list(card.get('supporting_evidence_ids')))}")
        lines.append("")

    lines.append("## Current hypotheses")
    lines.append("")
    for card in hyps:
        lines.append(f"### {_md(card.get('title') or card.get('id'))}")
        lines.append("")
        lines.append(_md(card.get("statement")))
        lines.append("")
        falsify = _as_list(card.get("what_would_falsify"))
        if falsify:
            lines.append("Would falsify:")
            for row in falsify:
                lines.append(f"- {row}")
            lines.append("")

    lines.append("## Uncited evidence")
    lines.append("")
    if uncited:
        lines.append("These files are in the corpus but not cited on any living insight/hypothesis. Update `beliefs/` if they should change a belief.")
        lines.append("")
        for it in uncited:
            lines.append(f"- `{it.evidence_id}` — {_md(it.title)}")
    else:
        lines.append("All current evidence IDs are cited on at least one living card.")
    lines.append("")

    lines.append("## Contradictions / uncertainty")
    lines.append("")
    any_counter = False
    for card in insights:
        counters = _as_list(card.get("counter_evidence_ids"))
        if counters:
            any_counter = True
            lines.append(f"- `{_md(card.get('id'))}` cites counter-evidence: {', '.join(f'`{x}`' for x in counters)}")
    if not any_counter:
        lines.append("- No counter-evidence IDs recorded on living insights yet.")
    lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def synthesize_repo(repo_root: Path) -> dict[str, Path]:
    items = load_corpus(repo_root)
    by_id = _index_corpus(items)
    insights, hyps = load_beliefs(repo_root)
    uncited = _uncited_evidence(items, insights, hyps)

    outputs_dir = repo_root / "outputs"
    reports_dir = repo_root / "reports"
    outputs_dir.mkdir(parents=True, exist_ok=True)
    reports_dir.mkdir(parents=True, exist_ok=True)

    paths: dict[str, Path] = {}
    paths["raw_synthesis"] = write_raw_synthesis(repo_root, items)

    p_insights = outputs_dir / "current-insights.md"
    p_insights.write_text(render_current_insights(insights, by_id), encoding="utf-8")
    paths["current_insights"] = p_insights

    p_hyp = outputs_dir / "hypotheses.md"
    p_hyp.write_text(render_hypotheses(hyps, by_id), encoding="utf-8")
    paths["hypotheses"] = p_hyp

    p_impl = outputs_dir / "implications.md"
    p_impl.write_text(render_implications(insights), encoding="utf-8")
    paths["implications"] = p_impl

    p_exp = outputs_dir / "experiments.md"
    p_exp.write_text(render_experiments(insights, hyps), encoding="utf-8")
    paths["experiments"] = p_exp

    # Stable filename: overwrite the latest snapshot instead of a clock-dated file.
    rpt = reports_dir / "latest-synthesis.md"
    rpt.write_text(render_report(items, insights, hyps, uncited), encoding="utf-8")
    paths["report"] = rpt

    return paths
