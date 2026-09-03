from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .simple_yaml import loads


@dataclass(frozen=True)
class FrontmatterDoc:
    meta: dict[str, Any]
    body: str


def parse_frontmatter(markdown_text: str) -> FrontmatterDoc:
    """
    Minimal YAML-frontmatter parser.

    Expects:
    ---
    <yaml>
    ---
    <body>
    """
    text = markdown_text.replace("\r\n", "\n")
    if not text.startswith("---\n"):
        return FrontmatterDoc(meta={}, body=text)

    end = text.find("\n---\n", 4)
    if end == -1:
        return FrontmatterDoc(meta={}, body=text)

    yaml_block = text[4:end]
    body = text[end + 5 :].lstrip("\n")

    meta = loads(yaml_block) or {}
    if not isinstance(meta, dict):
        meta = {}

    return FrontmatterDoc(meta=meta, body=body)

