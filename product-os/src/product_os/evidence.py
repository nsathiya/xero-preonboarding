from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any

from .frontmatter import parse_frontmatter
from .simple_yaml import dumps


@dataclass(frozen=True)
class EvidenceFile:
    path: Path
    meta: dict[str, Any]
    body: str


DOMAIN_TO_BASE_PATH = {
    "agent_builder": Path("evidence/agent-builders"),
    "customer": Path("evidence/customers"),
    "competitor": Path("evidence/competitors"),
    "product_knowledge": Path("evidence/product-knowledge"),
}

DOMAIN_TO_ID_PREFIX = {
    "agent_builder": "ev-agent",
    "customer": "ev-customer",
    "competitor": "ev-competitor",
    "product_knowledge": "ev-knowledge",
}


def load_markdown(path: Path) -> EvidenceFile:
    text = path.read_text(encoding="utf-8")
    doc = parse_frontmatter(text)
    return EvidenceFile(path=path, meta=doc.meta, body=doc.body)


def dump_frontmatter(meta: dict[str, Any]) -> str:
    return dumps(meta).strip()


def sha256_text(text: str) -> str:
    h = hashlib.sha256()
    h.update(text.encode("utf-8"))
    return h.hexdigest()


def next_id_for_prefix(target_dir: Path, prefix: str, slug: str) -> str:
    """
    Generates IDs like: ev-agent-notion-001, ev-agent-notion-002 ...
    """
    target_dir.mkdir(parents=True, exist_ok=True)
    existing = []
    for p in target_dir.glob("*.md"):
        try:
            doc = load_markdown(p)
            ev_id = str(doc.meta.get("id", "")).strip()
            if ev_id.startswith(f"{prefix}-{slug}-"):
                existing.append(ev_id)
        except Exception:
            # ignore unreadable files for ID allocation
            continue

    max_n = 0
    for ev_id in existing:
        maybe_n = ev_id.rsplit("-", 1)[-1]
        if maybe_n.isdigit():
            max_n = max(max_n, int(maybe_n))

    return f"{prefix}-{slug}-{max_n + 1:03d}"


def evidence_target_dir(domain: str, slug: str | None) -> Path:
    base = DOMAIN_TO_BASE_PATH.get(domain)
    if base is None:
        raise ValueError(f"Unknown domain: {domain}")

    if domain == "agent_builder":
        return base / (slug or "_inbox")

    if domain == "competitor":
        return base / (slug or "_inbox")

    # customers and product-knowledge are flat for now
    return base


def new_evidence_markdown(
    *,
    evidence_id: str,
    domain: str,
    source_type: str,
    source_name: str,
    title: str,
    dt: date | None = None,
    url: str | None = None,
    artifact_path: str | None = None,
    author_or_customer: str | None = None,
    product_area: str | None = None,
    tags: list[str] | None = None,
    confidence: str = "direct",
) -> str:
    meta: dict[str, Any] = {
        "id": evidence_id,
        "domain": domain,
        "source_type": source_type,
        "source_name": source_name,
        "date": (dt or date.today()).isoformat(),
        "title": title,
        "confidence": confidence,
    }

    if url:
        meta["url"] = url
    if artifact_path:
        meta["artifact_path"] = artifact_path
    if author_or_customer:
        meta["author_or_customer"] = author_or_customer
    if product_area:
        meta["product_area"] = product_area
    if tags:
        meta["tags"] = tags

    fm = dump_frontmatter(meta)
    return (
        "---\n"
        f"{fm}\n"
        "---\n\n"
        f"# {title}\n\n"
        "## Raw evidence\n\n"
        "_Paste/record what the source actually says/shows. Keep it as close to original as practical._\n\n"
        "## Notes\n\n"
        "_Your commentary, interpretations, and follow-up questions (not treated as raw evidence)._"
        "\n"
    )


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

