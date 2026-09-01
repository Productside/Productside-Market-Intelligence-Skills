#!/usr/bin/env python3
"""Validate the canonical skill contract and its portable projection.

The library is a network, not a chain. A market-intelligence run instantiates,
collects across independent disciplines, fuses, acts, and then schedules the next
diff -- and a Product Manager can enter at any of those five stages. So this
validator does not check a linear dependency order the way a staged method would.
It checks that every skill declares which stage it belongs to, which collection
discipline it speaks for, and that its body honors the doctrine rule its stage
exists to enforce.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from skill_metadata import (  # noqa: E402
    PORTABLE_METADATA_ORDER,
    SkillFormatError,
    as_list,
    openai_yaml,
    parse_skill,
    portable_frontmatter,
)

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"

FUSION = "All-Source Fusion"
DISCIPLINES = {
    "OSINT",
    "FININT",
    "GEOINT/DEMOINT",
    "TECHINT",
    "HUMINT",
    "SIGINT",
    "MASINT",
    FUSION,
}

# The motion: instantiate -> collect -> fuse -> act -> monitor. Each stage pins the
# `type` a skill may declare, because a monitor that calls itself an investigation
# will be scheduled like one and will re-collect instead of diffing.
STAGE_TYPES = {
    "instantiate": "router",
    "collect": "investigation",
    "fuse": "analysis",
    "act": "analysis",
    "monitor": "monitor",
}

# name -> (stage, discipline it speaks for)
SKILL_REGISTRY = {
    "mi-router-market-intelligence": ("instantiate", FUSION),
    "mi-sweep-full-spectrum": ("collect", FUSION),
    "mi-collect-osint": ("collect", "OSINT"),
    "mi-collect-finint": ("collect", "FININT"),
    "mi-collect-geoint-demoint": ("collect", "GEOINT/DEMOINT"),
    "mi-collect-techint": ("collect", "TECHINT"),
    "mi-collect-humint": ("collect", "HUMINT"),
    "mi-collect-sigint": ("collect", "SIGINT"),
    "mi-collect-masint": ("collect", "MASINT"),
    "mi-scan-market-landscape": ("collect", "OSINT"),
    "mi-snapshot-competitors": ("collect", "OSINT"),
    "mi-mine-voice-of-customer": ("collect", "OSINT"),
    "mi-fuse-all-source": ("fuse", FUSION),
    "mi-analyze-swot": ("act", FUSION),
    "mi-analyze-five-forces": ("act", FUSION),
    "mi-analyze-ansoff": ("act", FUSION),
    "mi-size-tam-sam-som": ("act", "GEOINT/DEMOINT"),
    "mi-build-battle-card": ("act", FUSION),
    "mi-watch-competitors": ("monitor", "SIGINT"),
    "mi-monitor-pricing-packaging": ("monitor", "SIGINT"),
    "mi-monitor-pestel-delta": ("monitor", FUSION),
    "mi-refresh-earnings-signals": ("monitor", "FININT"),
}
EXPECTED_SKILLS = sorted(SKILL_REGISTRY)

# Every collection discipline needs a skill that speaks for it, or the sweep order
# in reference/sweep-playbooks.md points at a channel nobody can actually run.
COLLECTION_DISCIPLINES = DISCIPLINES - {FUSION}

REQUIRED_SECTIONS = [
    "# ",
    "## Purpose",
    "## When to Use It",
    "## Input",
    "## Key Concepts",
    "## Guided Context Capture",
    "## What It Produces",
    "## Workflow",
    "## Human Decision Gate",
    "## Evidence and Attribution Rules",
    "## Common Failure Modes",
    "## Assets and Examples",
    "## Sources",
]
REQUIRED_FRONTMATTER = {
    "name",
    "description",
    "license",
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
    "interface",
}
# Keys authored as lists so the canonical source stays readable and diffable.
LIST_FIELDS = {
    "operating-level": 1,
    "audience": 3,
    "best-for": 3,
    "scenarios": 2,
    "evidence-required": 3,
    "produces": 3,
    "consumes": 0,
    "combine-with": 1,
    "source-basis": 2,
    "sources": 1,
}
REQUIRED_INTERFACE = [
    "display_name",
    "short_description",
    "brand_color",
    "default_prompt",
    "allow_implicit_invocation",
]
BRAND_COLOR = "#00E874"
THEME = "market-competitive-intelligence"

# Doctrine each stage must state in its own body, phrased so a reader can find it.
# These are the rules the library exists to enforce; a skill that omits its rule
# will be run by someone who never learns it.
STAGE_DOCTRINE = {
    "collect": [
        ("Collection is not fusion", "a sweep gathers and labels; it does not rate confidence"),
        ("search plan", "every collection run shows its search plan before researching"),
    ],
    "fuse": [
        ("independence test", "confidence may not be stacked before shared sources are collapsed"),
        ("Confidence stacking", "the core rule that separates action from anecdote"),
    ],
    "act": [
        ("no evidence found", "an unevidenced cell is named, never filled with a plausible sentence"),
    ],
    "monitor": [
        (("materiality bar", "materiality threshold"), "what separates a monitor from a newsfeed"),
        (
            ("Prior run", "Prior capture", "Prior baseline", "Prior profile"),
            "a delta report must name what it diffed against",
        ),
    ],
    "instantiate": [
        ("Route Table", "the router's job is to send the run somewhere, not to run it"),
        ("DECISION", "research without a decision is a hobby"),
    ],
}


def check_frontmatter(name: str, data: dict) -> list[str]:
    errors: list[str] = []
    stage, discipline = SKILL_REGISTRY[name]

    missing = sorted(REQUIRED_FRONTMATTER - set(data))
    extra = sorted(set(data) - REQUIRED_FRONTMATTER)
    if missing:
        errors.append(f"{name}: frontmatter missing {missing}")
    if extra:
        errors.append(f"{name}: unsupported frontmatter fields {extra}")

    if data.get("name") != name:
        errors.append(f"{name}: frontmatter name does not match directory")
    description = str(data.get("description", ""))
    if not description or len(description) > 200:
        errors.append(f"{name}: description must contain 1-200 characters")
    if data.get("license") != "CC-BY-NC-ND-4.0":
        errors.append(f"{name}: license must be CC-BY-NC-ND-4.0")
    if data.get("theme") != THEME:
        errors.append(f"{name}: theme must be {THEME}")
    if data.get("status") != "active":
        errors.append(f"{name}: status must be active")
    if data.get("stage") != stage:
        errors.append(f"{name}: stage must be {stage}")
    if data.get("discipline") != discipline:
        errors.append(f"{name}: discipline must be {discipline}")
    if data.get("type") != STAGE_TYPES[stage]:
        errors.append(f"{name}: a {stage} skill must declare type {STAGE_TYPES[stage]}")
    if len(str(data.get("intent", ""))) < 80:
        errors.append(f"{name}: intent must explain the job in at least 80 characters")

    for key, minimum in LIST_FIELDS.items():
        value = data.get(key, [])
        if not isinstance(value, list):
            errors.append(f"{name}: {key} must be authored as a YAML list, not a flattened string")
            continue
        if len(value) < minimum:
            errors.append(f"{name}: {key} needs at least {minimum} entries")

    # The library is a network, so `consumes` and `combine-with` are the only record
    # of how a run moves through it. A pointer at a skill that does not exist is a
    # handoff into nothing.
    for key in ("consumes", "combine-with"):
        for target in as_list(data.get(key)):
            if target not in SKILL_REGISTRY:
                errors.append(f"{name}: {key} references unknown skill {target}")
            if target == name:
                errors.append(f"{name}: {key} must not reference itself")
    for url in as_list(data.get("sources")):
        if not url.startswith("https://"):
            errors.append(f"{name}: sources entries must be https URLs, found {url}")

    interface = data.get("interface")
    if not isinstance(interface, dict):
        errors.append(f"{name}: interface block is missing or malformed")
        return errors
    for key in REQUIRED_INTERFACE:
        if key not in interface:
            errors.append(f"{name}: interface missing {key}")
    if errors:
        return errors
    short = str(interface["short_description"])
    if not 25 <= len(short) <= 64:
        errors.append(f"{name}: interface short_description must be 25-64 characters, found {len(short)}")
    if interface["brand_color"] != BRAND_COLOR:
        errors.append(f"{name}: interface brand_color must be {BRAND_COLOR}")
    if f"${name}" not in str(interface["default_prompt"]):
        errors.append(f"{name}: interface default_prompt must name ${name}")
    if len(str(interface["default_prompt"])) < 80:
        errors.append(f"{name}: interface default_prompt must describe work, artifact, and stopping behavior")
    if not isinstance(interface["allow_implicit_invocation"], bool):
        errors.append(f"{name}: interface allow_implicit_invocation must be true or false")
    return errors


def check_portable_projection(name: str, data: dict) -> list[str]:
    """The transform is only trustworthy if its output re-parses and stays complete."""
    errors: list[str] = []
    try:
        projected, _ = parse_skill(portable_frontmatter(data) + "\n# Body\n")
    except SkillFormatError as exc:
        return [f"{name}: portable projection does not re-parse: {exc}"]
    if sorted(projected) != sorted(["name", "description", "license", "metadata"]):
        errors.append(f"{name}: portable projection must expose only name, description, license, metadata")
    metadata = projected.get("metadata", {})
    missing = [key for key in PORTABLE_METADATA_ORDER if key not in metadata]
    if missing:
        errors.append(f"{name}: portable metadata missing {missing}")
    for key, value in metadata.items():
        if not isinstance(value, str) or not value:
            errors.append(f"{name}: portable metadata {key} must be a non-empty string")
    try:
        openai_yaml(data)
    except (SkillFormatError, KeyError) as exc:
        errors.append(f"{name}: agents/openai.yaml cannot be generated: {exc}")
    return errors


def check_body(name: str, body: str) -> list[str]:
    """Enforce the tradecraft every run honors, plus the rule this stage owns."""
    errors: list[str] = []
    stage, _ = SKILL_REGISTRY[name]

    cursor = 0
    for section in REQUIRED_SECTIONS:
        position = body.find(section, cursor)
        if position < 0:
            errors.append(f"{name}: missing or misordered section {section.strip()}")
            break
        cursor = position + len(section)

    # The three evidence labels are the contract. A brief that does not distinguish
    # them lets a working guess be repeated out loud as a fact.
    for label in ("Fact", "Inference", "Assumption"):
        if label not in body:
            errors.append(f"{name}: must teach the {label} evidence label")
    if "Do not invent" not in body:
        errors.append(f"{name}: must carry a do-not-invent list naming this run's fabrication risks")
    if "## Final Step" not in body and "Final Step block" not in body:
        errors.append(f"{name}: must end every run with the four-option Final Step block")

    for phrase in ("Guided", "Context dump", "Best guess", "Adaptive Decision Ladder"):
        if phrase not in body:
            errors.append(f"{name}: guided context behavior missing {phrase}")
    if "Anything supplied" not in body:
        errors.append(f"{name}: must explicitly reuse supplied context")

    for phrase, rule in STAGE_DOCTRINE[stage]:
        # A doctrine entry may accept any of several equivalent phrasings, so a
        # pricing tracker can say "Prior capture" where a watch says "Prior run".
        accepted = (phrase,) if isinstance(phrase, str) else phrase
        if not any(option.lower() in body.lower() for option in accepted):
            errors.append(
                f"{name}: a {stage} skill must state its doctrine -- {rule} "
                f"(missing {' / '.join(repr(option) for option in accepted)})"
            )

    # Key Concepts must teach, not gloss: every concept states how to notice it broken.
    concepts = body.partition("## Key Concepts")[2].partition("## Guided Context Capture")[0]
    signals = concepts.count("*Violation signal:*")
    if signals < 5:
        errors.append(
            f"{name}: Key Concepts needs at least 5 concepts with a *Violation signal:* line, found {signals}"
        )
    return errors


def check_skill(name: str) -> list[str]:
    skill_dir = SKILLS_DIR / name
    required_files = [
        skill_dir / "SKILL.md",
        skill_dir / "template.md",
        skill_dir / "examples" / "worked-example.md",
        skill_dir / "examples" / "weak-example.md",
    ]
    missing = [f"{name}: missing {path.relative_to(ROOT)}" for path in required_files if not path.is_file()]
    if missing:
        return missing
    if (skill_dir / "agents" / "openai.yaml").exists():
        return [f"{name}: agents/openai.yaml is generated at build time and must not be committed"]

    try:
        data, body = parse_skill((skill_dir / "SKILL.md").read_text(encoding="utf-8"))
    except SkillFormatError as exc:
        return [f"{name}: {exc}"]

    errors = check_frontmatter(name, data)
    errors.extend(check_portable_projection(name, data))
    errors.extend(check_body(name, body))

    for path in required_files:
        if "TODO" in path.read_text(encoding="utf-8"):
            errors.append(f"{name}: unresolved TODO in {path.relative_to(ROOT)}")

    # Skill files are read by an agent at inference time, where a diagram costs tokens,
    # restates the Workflow section, and renders as raw source in most skill viewers.
    for path in sorted(skill_dir.rglob("*.md")):
        if "```mermaid" in path.read_text(encoding="utf-8"):
            errors.append(f"{name}: {path.relative_to(ROOT)} must teach in prose, not a mermaid diagram")

    worked = (skill_dir / "examples" / "worked-example.md").read_text(encoding="utf-8").lower()
    weak = (skill_dir / "examples" / "weak-example.md").read_text(encoding="utf-8").lower()
    if "synthetic" not in worked:
        errors.append(f"{name}: worked example must label synthetic content")
    if "anti-pattern" not in weak:
        errors.append(f"{name}: weak example must identify itself as an anti-pattern")
    # An obviously bad example teaches nothing. The failure must be plausible, and the
    # file must show why a reviewer would let it through before explaining what is wrong.
    for marker, requirement in (
        ("## why it passes", "must show why the artifact survives a quick review"),
        ("## why it fails", "must diagnose the failure"),
        ("## repair", "must state the repair"),
    ):
        if marker not in weak:
            errors.append(f"{name}: weak example {requirement} ({marker.strip('# ')})")
    return errors


def check_shared_examples() -> list[str]:
    """The interaction contract needs a visible failure case, not only a happy path."""
    errors: list[str] = []
    transcript = ROOT / "examples" / "guided-context-capture-transcript.md"
    if not transcript.is_file():
        return [f"missing {transcript.relative_to(ROOT)}"]
    text = transcript.read_text(encoding="utf-8").lower()
    if "anti-pattern" not in text:
        errors.append("guided context transcript must contrast the happy path with an anti-pattern")
    for phrase in ("guided", "context dump", "best guess"):
        if phrase not in text:
            errors.append(f"guided context transcript must demonstrate {phrase}")
    return errors


def check_coverage() -> list[str]:
    """Every collection discipline needs a skill, or the sweep order points at nothing."""
    covered = {
        discipline
        for name, (stage, discipline) in SKILL_REGISTRY.items()
        if stage == "collect" and discipline != FUSION
    }
    uncovered = sorted(COLLECTION_DISCIPLINES - covered)
    return [f"no collection skill speaks for {discipline}" for discipline in uncovered]


def main() -> int:
    errors: list[str] = []
    actual = sorted(path.name for path in SKILLS_DIR.glob("mi-*") if path.is_dir())
    if actual != EXPECTED_SKILLS:
        unexpected = sorted(set(actual) - set(EXPECTED_SKILLS))
        absent = sorted(set(EXPECTED_SKILLS) - set(actual))
        if unexpected:
            errors.append(f"unregistered skill directories {unexpected}: add them to SKILL_REGISTRY or remove them")
        if absent:
            errors.append(f"registered skills with no directory {absent}")
    for name in EXPECTED_SKILLS:
        if name in actual:
            errors.extend(check_skill(name))

    errors.extend(check_coverage())
    errors.extend(check_shared_examples())

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    stages: dict[str, int] = {}
    for stage, _ in SKILL_REGISTRY.values():
        stages[stage] = stages.get(stage, 0) + 1
    breakdown = ", ".join(f"{count} {stage}" for stage, count in sorted(stages.items()))
    print(
        f"Validated {len(EXPECTED_SKILLS)} skills ({breakdown}): rich frontmatter, "
        "portable projection, stage doctrine, templates, and examples."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
