from __future__ import annotations

import argparse
import sys
from datetime import date
from pathlib import Path

from .evidence import (
    DOMAIN_TO_ID_PREFIX,
    evidence_target_dir,
    new_evidence_markdown,
    next_id_for_prefix,
    sha256_text,
    write_json,
)
from .corpus_rules import lock_evidence
from .paths import find_repo_root
from .validate import validate_repo
from .extract import extract_repo
from .synthesize import synthesize_repo


def cmd_new_evidence(args: argparse.Namespace) -> int:
    repo_root = find_repo_root()
    target_rel = evidence_target_dir(args.domain, args.slug)
    target_dir = repo_root / target_rel

    prefix = DOMAIN_TO_ID_PREFIX.get(args.domain)
    if not prefix:
        print(f"Unknown domain: {args.domain}", file=sys.stderr)
        return 2

    slug = args.slug or "inbox"
    evidence_id = next_id_for_prefix(target_dir, prefix=prefix, slug=slug)
    md = new_evidence_markdown(
        evidence_id=evidence_id,
        domain=args.domain,
        source_type=args.source_type,
        source_name=args.source_name,
        title=args.title,
        dt=date.fromisoformat(args.date) if args.date else None,
        url=args.url,
        artifact_path=args.artifact_path,
        author_or_customer=args.author_or_customer,
        product_area=args.product_area,
        tags=args.tags or None,
        confidence=args.confidence,
    )

    out_path = target_dir / f"{evidence_id}.md"
    out_path.write_text(md, encoding="utf-8")
    print(str(out_path))
    return 0


def cmd_validate(_: argparse.Namespace) -> int:
    repo_root = find_repo_root()
    errors, stats = validate_repo(repo_root)
    if errors:
        for e in errors:
            print(f"[ERROR] {e.path}: {e.message}", file=sys.stderr)
        print(f"\nValidation failed ({stats['errors']} errors).", file=sys.stderr)
        return 1

    print(f"OK. evidence_files={stats['evidence_files']} context_files={stats['context_files']}")
    return 0


def cmd_lock(args: argparse.Namespace) -> int:
    repo_root = find_repo_root()
    rc, stats = lock_evidence(repo_root, accept=args.accept)

    for rel in stats["added"]:
        print(f"[added]   {rel}")
    for rel in stats["changed"]:
        print(f"[changed] {rel}")
    for rel in stats["removed"]:
        print(f"[removed] {rel}")

    if rc != 0:
        print(
            "\nRefusing to re-lock: evidence is immutable and additive.\n"
            "Add a new ev-* file for a new source or pass, and update the\n"
            "relevant scorecard. If this is a genuine correction, re-run with\n"
            "--accept and record it in the scorecard Changelog.",
            file=sys.stderr,
        )
        return rc

    if not any(stats.values()):
        print("Lock is current.")
    return 0


def cmd_build_index(_: argparse.Namespace) -> int:
    repo_root = find_repo_root()
    evidence_dir = repo_root / "evidence"
    evidence_files = sorted(
        [
            p
            for p in evidence_dir.rglob("*.md")
            if p.is_file() and p.name.lower() != "readme.md"
        ]
    )

    items = []
    for p in evidence_files:
        text = p.read_text(encoding="utf-8")
        items.append(
            {
                "path": str(p.relative_to(repo_root)),
                "sha256": sha256_text(text),
            }
        )

    write_json(repo_root / "derived" / "index" / "evidence.files.json", {"items": items})
    print(str(repo_root / "derived" / "index" / "evidence.files.json"))
    return 0


def cmd_extract(_: argparse.Namespace) -> int:
    repo_root = find_repo_root()
    results = extract_repo(repo_root)
    for r in results:
        print(f"{r.evidence_id}\t{r.out_path}")
    return 0


def cmd_synthesize(_: argparse.Namespace) -> int:
    repo_root = find_repo_root()
    paths = synthesize_repo(repo_root)
    for k, p in paths.items():
        print(f"{k}\t{p}")
    return 0


def cmd_refresh(_: argparse.Namespace) -> int:
    repo_root = find_repo_root()
    errors, stats = validate_repo(repo_root)
    if errors:
        for e in errors:
            print(f"[ERROR] {e.path}: {e.message}", file=sys.stderr)
        print(f"\nValidation failed ({stats['errors']} errors).", file=sys.stderr)
        return 1

    extract_repo(repo_root)
    synthesize_repo(repo_root)
    cmd_build_index(argparse.Namespace())
    print("OK")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="product-os", add_help=True)
    sp = p.add_subparsers(dest="cmd", required=True)

    p_new = sp.add_parser("new-evidence", help="Create a new evidence markdown file")
    p_new.add_argument("--domain", required=True, choices=list(DOMAIN_TO_ID_PREFIX.keys()))
    p_new.add_argument("--source_type", required=True)
    p_new.add_argument("--source_name", required=True)
    p_new.add_argument("--title", required=True)
    p_new.add_argument("--slug", required=False, help="Subfolder slug (e.g. notion, hubspot, digits)")
    p_new.add_argument("--date", required=False, help="ISO date (YYYY-MM-DD). Defaults to today.")
    p_new.add_argument("--url", required=False)
    p_new.add_argument("--artifact_path", required=False)
    p_new.add_argument("--author_or_customer", required=False)
    p_new.add_argument("--product_area", required=False)
    p_new.add_argument("--confidence", required=False, default="direct")
    p_new.add_argument("--tags", required=False, nargs="*")
    p_new.set_defaults(func=cmd_new_evidence)

    p_val = sp.add_parser(
        "validate",
        help="Validate frontmatter, evidence immutability, and scorecard currency",
    )
    p_val.set_defaults(func=cmd_validate)

    p_lock = sp.add_parser("lock", help="Record evidence hashes (append-only ledger)")
    p_lock.add_argument(
        "--accept",
        action="store_true",
        help="Allow re-locking modified/removed evidence (genuine corrections only)",
    )
    p_lock.set_defaults(func=cmd_lock)

    p_idx = sp.add_parser("build-index", help="Build a derived file index (sha256 per file)")
    p_idx.set_defaults(func=cmd_build_index)

    p_ext = sp.add_parser("extract", help="Extract derived observations from evidence")
    p_ext.set_defaults(func=cmd_extract)

    p_syn = sp.add_parser("synthesize", help="Generate outputs/ + a dated report from derived observations")
    p_syn.set_defaults(func=cmd_synthesize)

    p_ref = sp.add_parser("refresh", help="Validate, extract, synthesize, build-index")
    p_ref.set_defaults(func=cmd_refresh)

    return p


def main(argv: list[str] | None = None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)
    rc = args.func(args)
    raise SystemExit(rc)


if __name__ == "__main__":
    main()

