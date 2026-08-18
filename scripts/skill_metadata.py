#!/usr/bin/env python3
"""Parse canonical skill frontmatter and project it onto portable platform shapes.

The canonical `skills/<name>/SKILL.md` carries rich, list-shaped frontmatter so the
metadata stays readable and reviewable. Strict consumers such as the Codex portable
skill standard accept only `name`, `description`, `license`, `allowed-tools`, and a
string-to-string `metadata` map at the top level. Rather than degrading the canonical
source to satisfy the strictest consumer, the packaging pipeline transforms it here.

Only the YAML subset the canonical skills actually use is supported: scalars, folded
block scalars, block sequences, inline empty sequences, and one level of nested map.
"""

from __future__ import annotations

import re
from typing import Any


FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
KEY = re.compile(r"^([A-Za-z0-9_-]+):(?:\s(.*))?$")

# Ordered so the generated portable metadata map is deterministic.
PORTABLE_METADATA_ORDER = [
    "argument-hint",
    "intent",
    "type",
    "theme",
    "stage",
    "discipline",
    "status",
    "operating-level",
    "audience",
    "best-for",
    "scenarios",
    "evidence-required",
    "produces",
    "estimated-time",
    "group-size",
    "consumes",
    "combine-with",
    "source-basis",
    "sources",
]


class SkillFormatError(ValueError):
    """Raised when a SKILL.md frontmatter block cannot be parsed."""


def _parse_scalar(raw: str) -> Any:
    value = raw.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1]
    if value == "[]":
        return []
    if value in {"true", "false"}:
        return value == "true"
    return value


def _parse_block(lines: list[str], indent: int) -> dict[str, Any]:
    data: dict[str, Any] = {}
    index = 0
    while index < len(lines):
        line = lines[index]
        if not line.strip() or line.lstrip().startswith("#"):
            index += 1
            continue
        if len(line) - len(line.lstrip(" ")) != indent:
            raise SkillFormatError(f"unexpected indentation: {line!r}")
        match = KEY.match(line.strip())
        if not match:
            raise SkillFormatError(f"expected 'key: value', found: {line!r}")
        key, inline = match.group(1), (match.group(2) or "").strip()

        cursor = index + 1
        children: list[str] = []
        while cursor < len(lines):
            candidate = lines[cursor]
            if candidate.strip() and len(candidate) - len(candidate.lstrip(" ")) <= indent:
                break
            children.append(candidate)
            cursor += 1
        while children and not children[-1].strip():
            children.pop()

        if inline in {">-", ">", "|", "|-"}:
            data[key] = " ".join(child.strip() for child in children if child.strip())
        elif inline:
            data[key] = _parse_scalar(inline)
        elif children and children[0].strip().startswith("- "):
            data[key] = [_parse_scalar(child.strip()[2:]) for child in children if child.strip()]
        elif children:
            data[key] = _parse_block(children, indent + 2)
        else:
            data[key] = ""
        index = cursor
    return data


def parse_skill(text: str) -> tuple[dict[str, Any], str]:
    """Split SKILL.md into its parsed frontmatter mapping and its Markdown body."""
    match = FRONTMATTER.match(text)
    if not match:
        raise SkillFormatError("SKILL.md must open with a --- frontmatter block")
    return _parse_block(match.group(1).splitlines(), 0), text[match.end() :]


def as_list(value: Any) -> list[str]:
    if isinstance(value, list):
        return [str(item) for item in value]
    if value in ("", None):
        return []
    return [str(value)]


def _quote(value: str) -> str:
    return '"' + str(value).replace("\\", "\\\\").replace('"', '\\"') + '"'


def flatten(value: Any) -> str:
    """Collapse a canonical value into the pipe-separated portable string form."""
    if isinstance(value, list):
        return " | ".join(str(item) for item in value) if value else "none"
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def portable_frontmatter(data: dict[str, Any]) -> str:
    """Render the strict portable frontmatter accepted by the Codex skill standard."""
    lines = [
        "---",
        f"name: {data['name']}",
        f"description: {data['description']}",
        f"license: {data['license']}",
        "metadata:",
    ]
    for key in PORTABLE_METADATA_ORDER:
        if key in data:
            lines.append(f"  {key}: {_quote(flatten(data[key]))}")
    lines.extend(["---", ""])
    return "\n".join(lines)


def openai_yaml(data: dict[str, Any]) -> str:
    """Render agents/openai.yaml from the canonical interface block."""
    interface = data.get("interface") or {}
    if not isinstance(interface, dict):
        raise SkillFormatError("interface must be a mapping")
    return "\n".join(
        [
            f"# Generated from skills/{data['name']}/SKILL.md by scripts/release_tools.py.",
            "# Do not edit by hand; edit the canonical frontmatter instead.",
            "interface:",
            f"  display_name: {_quote(interface['display_name'])}",
            f"  short_description: {_quote(interface['short_description'])}",
            f"  brand_color: {_quote(interface['brand_color'])}",
            f"  default_prompt: {_quote(interface['default_prompt'])}",
            "policy:",
            f"  allow_implicit_invocation: {flatten(interface['allow_implicit_invocation'])}",
            "",
        ]
    )


def portable_skill(text: str) -> str:
    """Transform a canonical SKILL.md into its portable equivalent."""
    data, body = parse_skill(text)
    return portable_frontmatter(data) + body
