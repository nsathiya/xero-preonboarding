from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class EvidenceSections:
    """
    Very small markdown splitter for our evidence format.

    We only care about the two top-level sections:
    - "## Raw evidence"
    - "## Notes"
    """

    raw_evidence: str
    notes: str


def _extract_after_heading(text: str, heading: str) -> str:
    """
    Returns the content after a heading line until the next '## ' heading.
    """
    lines = text.replace("\r\n", "\n").split("\n")
    start = None
    for i, line in enumerate(lines):
        if line.strip().lower() == heading.strip().lower():
            start = i + 1
            break
    if start is None:
        return ""

    out: list[str] = []
    for j in range(start, len(lines)):
        if lines[j].startswith("## "):
            break
        out.append(lines[j])
    return "\n".join(out).strip()


def split_evidence_sections(body_markdown: str) -> EvidenceSections:
    raw = _extract_after_heading(body_markdown, "## Raw evidence")
    notes = _extract_after_heading(body_markdown, "## Notes")
    return EvidenceSections(raw_evidence=raw, notes=notes)


def extract_bullets(text: str) -> list[str]:
    """
    Extracts simple '-' bullets (single line) from text.
    """
    bullets: list[str] = []
    for line in text.replace("\r\n", "\n").split("\n"):
        s = line.strip()
        if s.startswith("- "):
            bullets.append(s[2:].strip())
    return bullets


def extract_h3_blocks(text: str) -> list[tuple[str, str]]:
    """
    Extract (### Heading, content-until-next-###) blocks.
    """
    lines = text.replace("\r\n", "\n").split("\n")
    blocks: list[tuple[str, str]] = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith("### "):
            title = line[4:].strip()
            i += 1
            content: list[str] = []
            while i < len(lines) and not lines[i].strip().startswith("### "):
                content.append(lines[i])
                i += 1
            blocks.append((title, "\n".join(content).strip()))
            continue
        i += 1
    return blocks

