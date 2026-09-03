"""
Deterministic enforcement of the corpus contract.

Two rules, both mechanical:

1. Evidence is immutable and additive. Once an evidence file is locked,
   its bytes may not change. New sources become new files.
2. Competitor scorecards are living and must stay current. Every
   evidence file for a competitor must be cited by that competitor's
   scorecard, and every status must use the shared vocabulary.

Prose version: notes/competitors/scorecard/_scorecard-guide.md
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .evidence import load_markdown, sha256_text

LOCK_FILENAME = "evidence-lock.json"

# Single source of truth for scorecard status values.
STATUS_VOCAB = {"VERIFIED", "DOCS", "CLAIMED", "UNSEEN", "DISPUTED"}

# Cells that legitimately carry no status (e.g. derived "so what" rows).
STATUS_EMPTY_TOKENS = {"", "-", "—", "–", "n/a", "N/A"}

SCORECARD_DIR = Path("notes/competitors/scorecard")
COMPETITOR_EVIDENCE_DIR = Path("evidence/competitors")


@dataclass(frozen=True)
class RuleViolation:
    path: str
    message: str


def _rel(repo_root: Path, path: Path) -> str:
    try:
        return str(path.relative_to(repo_root))
    except ValueError:
        return str(path)


def evidence_markdown_files(repo_root: Path) -> list[Path]:
    evidence_dir = repo_root / "evidence"
    if not evidence_dir.exists():
        return []
    return sorted(
        p
        for p in evidence_dir.rglob("*.md")
        if p.is_file() and p.name.lower() != "readme.md"
    )


def lock_path(repo_root: Path) -> Path:
    return repo_root / LOCK_FILENAME


def read_lock(repo_root: Path) -> dict[str, str]:
    p = lock_path(repo_root)
    if not p.exists():
        return {}
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}
    files = data.get("files", {})
    return {str(k): str(v) for k, v in files.items()} if isinstance(files, dict) else {}


def write_lock(repo_root: Path, files: dict[str, str]) -> Path:
    p = lock_path(repo_root)
    payload = {
        "_comment": (
            "Immutability ledger for evidence/. Managed by "
            "`product-os lock`. Evidence is append-only: to revise an "
            "interpretation, add a new evidence file and update the "
            "relevant scorecard instead of editing a locked file."
        ),
        "files": dict(sorted(files.items())),
    }
    p.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return p


def current_evidence_hashes(repo_root: Path) -> dict[str, str]:
    return {
        _rel(repo_root, p): sha256_text(p.read_text(encoding="utf-8"))
        for p in evidence_markdown_files(repo_root)
    }


def check_evidence_immutable(repo_root: Path) -> list[RuleViolation]:
    """Locked evidence files may not be modified, renamed, or deleted."""
    locked = read_lock(repo_root)
    if not locked:
        return []

    violations: list[RuleViolation] = []
    current = current_evidence_hashes(repo_root)

    for rel, expected in locked.items():
        actual = current.get(rel)
        if actual is None:
            violations.append(
                RuleViolation(
                    path=rel,
                    message=(
                        "Locked evidence file is missing (deleted or renamed). "
                        "Evidence is append-only; restore it. If the removal is "
                        "intentional, re-run `lock --accept` and say why in the "
                        "scorecard Changelog."
                    ),
                )
            )
        elif actual != expected:
            violations.append(
                RuleViolation(
                    path=rel,
                    message=(
                        "Locked evidence file was modified. Raw evidence is "
                        "immutable — add a new ev-* file for the new source/pass "
                        "and update the scorecard instead. If this is a genuine "
                        "correction (typo, bad citation), run `lock --accept`."
                    ),
                )
            )

    return violations


def _competitor_slugs_with_evidence(repo_root: Path) -> dict[str, list[str]]:
    """slug -> sorted evidence ids found under evidence/competitors/<slug>/"""
    base = repo_root / COMPETITOR_EVIDENCE_DIR
    if not base.exists():
        return {}

    out: dict[str, list[str]] = {}
    for slug_dir in sorted(p for p in base.iterdir() if p.is_dir()):
        slug = slug_dir.name
        if slug.startswith("_"):
            continue
        ids: list[str] = []
        for p in sorted(slug_dir.glob("*.md")):
            if p.name.lower() == "readme.md":
                continue
            try:
                doc = load_markdown(p)
            except Exception:
                continue
            ev_id = str(doc.meta.get("id", "")).strip()
            if ev_id:
                ids.append(ev_id)
        if ids:
            out[slug] = sorted(ids)
    return out


def _table_status_tokens(body: str) -> list[tuple[int, str]]:
    """
    Extract tokens from the `Status` column of markdown tables.

    Returns (line_number, token) pairs. Only inspects tables that have a
    column literally headed "Status", so prose is never scanned.
    """
    tokens: list[tuple[int, str]] = []
    status_idx: int | None = None

    for lineno, line in enumerate(body.splitlines(), start=1):
        stripped = line.strip()
        if not stripped.startswith("|"):
            status_idx = None
            continue

        cells = [c.strip() for c in stripped.strip("|").split("|")]

        if status_idx is None:
            if any(c.lower() == "status" for c in cells):
                status_idx = next(i for i, c in enumerate(cells) if c.lower() == "status")
            continue

        # Skip the header separator row (|---|---|).
        if all(set(c) <= set("-: ") for c in cells if c):
            continue

        if status_idx >= len(cells):
            continue

        cell = cells[status_idx]
        for raw in cell.replace("/", " ").split():
            token = raw.strip("`*_ ")
            if token in STATUS_EMPTY_TOKENS:
                continue
            tokens.append((lineno, token))

    return tokens


def check_scorecards(repo_root: Path) -> list[RuleViolation]:
    """Every competitor with evidence needs a current, well-formed scorecard."""
    violations: list[RuleViolation] = []
    slugs = _competitor_slugs_with_evidence(repo_root)
    if not slugs:
        return []

    all_known_ids = {ev_id for ids in slugs.values() for ev_id in ids}
    scorecard_dir = repo_root / SCORECARD_DIR

    for slug, ev_ids in slugs.items():
        card = scorecard_dir / f"{slug}.md"
        card_rel = _rel(repo_root, card)

        if not card.exists():
            violations.append(
                RuleViolation(
                    path=card_rel,
                    message=(
                        f"Missing living scorecard for competitor '{slug}' "
                        f"({len(ev_ids)} evidence file(s) on disk). Create it "
                        f"per {SCORECARD_DIR}/_scorecard-guide.md."
                    ),
                )
            )
            continue

        try:
            doc = load_markdown(card)
        except Exception as e:
            violations.append(RuleViolation(path=card_rel, message=f"Failed to parse: {e}"))
            continue

        if str(doc.meta.get("type", "")).strip() != "living_scorecard":
            violations.append(
                RuleViolation(path=card_rel, message="Frontmatter `type` must be `living_scorecard`.")
            )

        for field in ("competitor", "effective_date"):
            if not str(doc.meta.get(field, "")).strip():
                violations.append(
                    RuleViolation(path=card_rel, message=f"Frontmatter missing `{field}`.")
                )

        if "## Changelog" not in doc.body:
            violations.append(
                RuleViolation(
                    path=card_rel,
                    message="Missing `## Changelog` section (status changes must be dated).",
                )
            )

        # Rule: adding evidence forces a scorecard update.
        uncited = [ev_id for ev_id in ev_ids if ev_id not in doc.body]
        if uncited:
            violations.append(
                RuleViolation(
                    path=card_rel,
                    message=(
                        "Scorecard is stale — evidence not cited: "
                        f"{', '.join(uncited)}. Update the affected rows, "
                        "`effective_date`, and Changelog."
                    ),
                )
            )

        # Catch citations of evidence that does not exist (typos).
        for token in _referenced_evidence_ids(doc.body):
            if token.startswith("ev-comp-") and token not in all_known_ids:
                violations.append(
                    RuleViolation(
                        path=card_rel,
                        message=f"Cites unknown evidence id `{token}`.",
                    )
                )

        for lineno, token in _table_status_tokens(doc.body):
            if token not in STATUS_VOCAB:
                violations.append(
                    RuleViolation(
                        path=card_rel,
                        message=(
                            f"line {lineno}: invalid status `{token}`. "
                            f"Allowed: {', '.join(sorted(STATUS_VOCAB))}."
                        ),
                    )
                )

    return violations


def _referenced_evidence_ids(body: str) -> set[str]:
    ids: set[str] = set()
    for raw in body.replace("`", " ").replace(",", " ").split():
        token = raw.strip(".;:()[]<>'\"")
        if token.startswith("ev-comp-"):
            ids.add(token)
    return ids


def check_corpus_rules(repo_root: Path) -> list[RuleViolation]:
    return [*check_evidence_immutable(repo_root), *check_scorecards(repo_root)]


def lock_evidence(repo_root: Path, *, accept: bool) -> tuple[int, dict[str, Any]]:
    """
    Record hashes for evidence files.

    New files are added automatically (append-only is the normal path).
    Changes to already-locked files are refused unless `accept` is set.
    """
    locked = read_lock(repo_root)
    current = current_evidence_hashes(repo_root)

    added = sorted(set(current) - set(locked))
    removed = sorted(set(locked) - set(current))
    changed = sorted(r for r in set(locked) & set(current) if locked[r] != current[r])

    stats = {"added": added, "changed": changed, "removed": removed}

    if (changed or removed) and not accept:
        return 1, stats

    write_lock(repo_root, current)
    return 0, stats
