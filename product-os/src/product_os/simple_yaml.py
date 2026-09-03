from __future__ import annotations

from dataclasses import dataclass
from typing import Any


class SimpleYamlError(ValueError):
    pass


def _parse_scalar(raw: str) -> Any:
    s = raw.strip()
    if s == "":
        return ""
    if s in {"true", "True"}:
        return True
    if s in {"false", "False"}:
        return False
    if s in {"null", "None", "none"}:
        return None
    if s == "[]":
        return []
    if s == "{}":
        return {}
    # numbers
    try:
        if "." in s:
            return float(s)
        return int(s)
    except Exception:
        pass
    # quoted string
    if (s.startswith('"') and s.endswith('"')) or (s.startswith("'") and s.endswith("'")):
        return s[1:-1]
    return s


@dataclass
class _Line:
    indent: int
    text: str


def _tokenize(text: str) -> list[_Line]:
    lines: list[_Line] = []
    for raw in text.replace("\r\n", "\n").split("\n"):
        if raw.strip() == "" or raw.lstrip().startswith("#"):
            continue
        indent = len(raw) - len(raw.lstrip(" "))
        if raw[:indent].replace(" ", "") != "":
            raise SimpleYamlError("Only space indentation is supported")
        lines.append(_Line(indent=indent, text=raw.lstrip(" ")))
    return lines


def loads(text: str) -> Any:
    """
    Minimal YAML subset loader.

    Supports:
    - dicts with indentation
    - lists with "- " items
    - scalars (string/int/float/bool/null)

    Limitations:
    - no multiline scalars
    - no anchors/refs
    - no complex keys
    """
    toks = _tokenize(text)
    if not toks:
        return {}

    idx = 0

    def parse_block(expected_indent: int) -> Any:
        nonlocal idx
        # Decide list vs dict by next token
        if idx >= len(toks):
            return {}

        if toks[idx].indent < expected_indent:
            return {}

        # list
        if toks[idx].indent == expected_indent and toks[idx].text.startswith("- "):
            out_list: list[Any] = []
            while idx < len(toks) and toks[idx].indent == expected_indent and toks[idx].text.startswith("- "):
                item_text = toks[idx].text[2:].strip()
                idx += 1
                if item_text == "":
                    out_list.append(parse_block(expected_indent + 2))
                elif ":" in item_text and not (
                    (item_text.startswith('"') and item_text.endswith('"'))
                    or (item_text.startswith("'") and item_text.endswith("'"))
                ):
                    # "- key: value" starts a mapping; remaining keys are indented
                    key, rest = item_text.split(":", 1)
                    mapping: dict[str, Any] = {}
                    rest = rest.strip()
                    mapping[key.strip()] = parse_block(expected_indent + 2) if rest == "" else _parse_scalar(rest)
                    nested = parse_block(expected_indent + 2)
                    if isinstance(nested, dict):
                        mapping.update(nested)
                    out_list.append(mapping)
                else:
                    out_list.append(_parse_scalar(item_text))
            return out_list

        # dict
        out_dict: dict[str, Any] = {}
        while idx < len(toks) and toks[idx].indent == expected_indent and not toks[idx].text.startswith("- "):
            line = toks[idx].text
            if ":" not in line:
                raise SimpleYamlError(f"Invalid mapping line: {line}")
            key, rest = line.split(":", 1)
            key = key.strip()
            rest = rest.strip()
            idx += 1
            if rest == "":
                out_dict[key] = parse_block(expected_indent + 2)
            else:
                out_dict[key] = _parse_scalar(rest)
        return out_dict

    idx = 0
    return parse_block(toks[0].indent)


def dumps(obj: Any, *, indent: int = 0) -> str:
    """
    Minimal YAML subset dumper (dicts/lists/scalars).
    """
    sp = " " * indent

    if obj is None:
        return "null"
    if obj is True:
        return "true"
    if obj is False:
        return "false"
    if isinstance(obj, (int, float)):
        return str(obj)
    if isinstance(obj, str):
        return obj
    if isinstance(obj, list):
        lines: list[str] = []
        for item in obj:
            if isinstance(item, (dict, list)):
                lines.append(f"{sp}-")
                lines.append(dumps(item, indent=indent + 2))
            else:
                lines.append(f"{sp}- {dumps(item, indent=0)}")
        return "\n".join(lines)
    if isinstance(obj, dict):
        lines = []
        for k, v in obj.items():
            if isinstance(v, (dict, list)):
                lines.append(f"{sp}{k}:")
                lines.append(dumps(v, indent=indent + 2))
            else:
                lines.append(f"{sp}{k}: {dumps(v, indent=0)}")
        return "\n".join(lines)

    raise SimpleYamlError(f"Unsupported type: {type(obj)}")

