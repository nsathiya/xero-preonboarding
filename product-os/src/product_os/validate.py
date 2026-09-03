from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .corpus_rules import check_corpus_rules
from .evidence import load_markdown
from .simple_yaml import loads


@dataclass(frozen=True)
class ValidationError:
    path: str
    message: str


def load_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    obj = loads(path.read_text(encoding="utf-8")) or {}
    return obj if isinstance(obj, dict) else {}


def required_fields_from_config(repo_root: Path) -> tuple[list[str], list[str]]:
    cfg = load_yaml(repo_root / "config" / "synthesis.yaml")
    validation = cfg.get("validation", {})
    require_fields = validation.get("require_fields", {})
    evidence_fields = require_fields.get("evidence", []) or []
    context_fields = require_fields.get("context", []) or []
    return list(evidence_fields), list(context_fields)


def validate_frontmatter(meta: dict[str, Any], required_fields: list[str]) -> list[str]:
    missing = []
    for k in required_fields:
        v = meta.get(k)
        if v is None:
            missing.append(k)
            continue
        if isinstance(v, str) and not v.strip():
            missing.append(k)
            continue
        if isinstance(v, list) and len(v) == 0:
            # allow empty tags lists? treat as missing only if explicitly required
            missing.append(k)
    return missing


def iter_markdown_files(root: Path) -> list[Path]:
    if not root.exists():
        return []
    files = []
    for p in root.rglob("*.md"):
        if not p.is_file():
            continue
        if p.name.lower() == "readme.md":
            continue
        files.append(p)
    return sorted(files)


def validate_repo(repo_root: Path) -> tuple[list[ValidationError], dict[str, Any]]:
    evidence_required, context_required = required_fields_from_config(repo_root)
    errors: list[ValidationError] = []

    evidence_dir = repo_root / "evidence"
    context_dir = repo_root / "context"

    evidence_count = 0
    context_count = 0

    for p in iter_markdown_files(evidence_dir):
        evidence_count += 1
        try:
            doc = load_markdown(p)
        except Exception as e:
            errors.append(ValidationError(path=str(p), message=f"Failed to parse: {e}"))
            continue

        missing = validate_frontmatter(doc.meta, evidence_required)
        if missing:
            errors.append(
                ValidationError(
                    path=str(p),
                    message=f"Missing required frontmatter fields: {', '.join(missing)}",
                )
            )

    for p in iter_markdown_files(context_dir):
        context_count += 1
        try:
            doc = load_markdown(p)
        except Exception as e:
            errors.append(ValidationError(path=str(p), message=f"Failed to parse: {e}"))
            continue

        missing = validate_frontmatter(doc.meta, context_required)
        if missing:
            errors.append(
                ValidationError(
                    path=str(p),
                    message=f"Missing required frontmatter fields: {', '.join(missing)}",
                )
            )

    for v in check_corpus_rules(repo_root):
        errors.append(ValidationError(path=v.path, message=v.message))

    stats = {
        "evidence_files": evidence_count,
        "context_files": context_count,
        "errors": len(errors),
    }
    return errors, stats

