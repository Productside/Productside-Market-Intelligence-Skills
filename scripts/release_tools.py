#!/usr/bin/env python3
"""Shared validation and deterministic release helpers."""

from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import stat
import subprocess
import sys
import zipfile
from pathlib import Path, PurePosixPath

sys.path.insert(0, str(Path(__file__).resolve().parent))

from skill_metadata import openai_yaml, parse_skill, portable_skill  # noqa: E402


ROOT = Path(__file__).resolve().parents[1]
FIXED_TIME = (1980, 1, 1, 0, 0, 0)


def expected_skills(root: Path = ROOT) -> list[str]:
    """Every registered skill, discovered from the tree rather than restated here.

    validate-skills.py holds the authoritative registry of names, stages, and
    disciplines. Duplicating that list in the packaging pipeline would let the two
    drift, and a drifted release ships a skill the validator never checked.
    """
    return sorted(path.name for path in (root / "skills").glob("mi-*") if path.is_dir())

IGNORED_NAMES = {".DS_Store", "__pycache__", ".pytest_cache"}
IGNORED_SUFFIXES = {".pyc"}
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
SECRET_PATTERNS = {
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "GitHub token": re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b"),
    "OpenAI key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "local home path": re.compile(r"/Users/[A-Za-z0-9._-]+/"),
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(65536), b""):
            digest.update(block)
    return digest.hexdigest()


def read_public_entries(root: Path = ROOT) -> list[str]:
    manifest = root / "release" / "public-files.txt"
    return [
        line.strip()
        for line in manifest.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    ]


def is_ignored(path: Path) -> bool:
    return any(part in IGNORED_NAMES for part in path.parts) or path.suffix in IGNORED_SUFFIXES


def public_files(root: Path = ROOT) -> list[Path]:
    files: set[Path] = set()
    errors: list[str] = []
    for entry in read_public_entries(root):
        path = root / entry.rstrip("/")
        if entry.endswith("/"):
            if not path.is_dir():
                errors.append(f"allowlisted directory is missing: {entry}")
                continue
            files.update(item for item in path.rglob("*") if item.is_file() and not is_ignored(item))
        elif path.is_file():
            files.add(path)
        else:
            errors.append(f"allowlisted file is missing: {entry}")
    if errors:
        raise RuntimeError("\n".join(errors))
    return sorted(files, key=lambda item: item.relative_to(root).as_posix())


def validate_plugins(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    version = (root / "VERSION").read_text(encoding="utf-8").strip()
    paths = [
        root / ".claude-plugin" / "plugin.json",
        root / ".claude-plugin" / "marketplace.json",
        root / ".codex-plugin" / "plugin.json",
    ]
    documents: dict[Path, dict] = {}
    for path in paths:
        # The Codex manifest ships in the generated Codex bundle, not the canonical
        # distribution, so validate it wherever it exists rather than requiring it.
        if path == paths[2] and not path.is_file():
            continue
        try:
            documents[path] = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{path.relative_to(root)}: {exc}")
    if errors:
        return errors

    claude = documents[paths[0]]
    marketplace = documents[paths[1]]
    plugin = marketplace.get("plugins", [{}])[0]
    checked = [("Claude", claude), ("marketplace", plugin)]
    if paths[2] in documents:
        codex = documents[paths[2]]
        checked.append(("Codex", codex))
        if codex.get("skills") != "./skills/":
            errors.append("Codex manifest must expose ./skills/")
    for label, data in checked:
        if data.get("name") != "mintel":
            errors.append(f"{label} manifest has an unexpected plugin name")
        if data.get("version") != version:
            errors.append(f"{label} manifest version does not match VERSION")
    if marketplace.get("metadata", {}).get("version") != version:
        errors.append("marketplace metadata version does not match VERSION")
    if plugin.get("source") != ".":
        errors.append("marketplace plugin source must be repository root")
    return errors


def validate_markdown_links(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    for path in public_files(root):
        if path.suffix.lower() != ".md":
            continue
        text = path.read_text(encoding="utf-8")
        for raw_target in MARKDOWN_LINK.findall(text):
            target = raw_target.strip().split(maxsplit=1)[0].strip("<>")
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            local = target.split("#", 1)[0]
            if local and not (path.parent / local).resolve().exists():
                errors.append(f"{path.relative_to(root)}: broken link {raw_target}")
    return errors


def validate_diagrams(root: Path = ROOT) -> list[str]:
    """Keep mermaid blocks out of the markdown-link scanner's way.

    validate_markdown_links scans raw text, fenced blocks included, so a node written
    as `id[Label](shape)` would be read as a broken relative link. Requiring quoted
    labels that never produce `](` keeps the two checks from fighting each other.
    """
    errors: list[str] = []
    for path in public_files(root):
        if path.suffix.lower() != ".md":
            continue
        text = path.read_text(encoding="utf-8")
        for block in re.findall(r"```mermaid\n(.*?)```", text, re.DOTALL):
            if "](" in block:
                errors.append(
                    f"{path.relative_to(root)}: mermaid label contains '](' and will be "
                    "misread as a markdown link; quote the label text"
                )
    return errors


def validate_public_surface(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    files = public_files(root)
    relative = {path.relative_to(root).as_posix() for path in files}
    if any(name == "sources" or name.startswith("sources/") for name in relative):
        errors.append("sources/ must not be present in the public allowlist")
    for required in ("LICENSE", "NOTICE.md", "SECURITY.md", "CONTRIBUTING.md", "CITATION.cff", "README.md"):
        if required not in relative:
            errors.append(f"public allowlist is missing {required}")
    for path in files:
        if path.suffix.lower() not in {".md", ".txt", ".json", ".yaml", ".yml", ".py", ".sh", ".cff", ""}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            errors.append(f"public text file is not UTF-8: {path.relative_to(root)}")
            continue
        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(text):
                errors.append(f"{path.relative_to(root)}: possible {label}")
    return errors


def run_canonical_checks(root: Path = ROOT) -> None:
    subprocess.run([sys.executable, "scripts/validate-skills.py"], cwd=root, check=True)
    errors = (
        validate_plugins(root)
        + validate_markdown_links(root)
        + validate_diagrams(root)
        + validate_public_surface(root)
    )
    if errors:
        raise RuntimeError("\n".join(errors))
    print(f"Validated plugin manifests, public allowlist, links, and diagrams across {len(public_files(root))} files.")


def safe_member(name: str, expected_root: str) -> bool:
    path = PurePosixPath(name)
    return not path.is_absolute() and ".." not in path.parts and len(path.parts) > 1 and path.parts[0] == expected_root


def deterministic_zip(
    source_root: Path,
    files: list[Path],
    archive: Path,
    archive_root: str,
    extra_files: dict[str, Path] | None = None,
) -> None:
    archive.parent.mkdir(parents=True, exist_ok=True)
    entries = [(path.relative_to(source_root).as_posix(), path) for path in files]
    entries.extend((name, path) for name, path in (extra_files or {}).items())
    with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as bundle:
        for relative, path in sorted(entries, key=lambda item: item[0]):
            info = zipfile.ZipInfo(f"{archive_root}/{relative}", FIXED_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            permissions = path.stat().st_mode & 0o777
            info.external_attr = (stat.S_IFREG | permissions) << 16
            bundle.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)


def verify_zip(archive: Path, expected_root: str) -> None:
    with zipfile.ZipFile(archive) as bundle:
        bad = bundle.testzip()
        if bad:
            raise RuntimeError(f"{archive.name}: corrupt member {bad}")
        unsafe = [name for name in bundle.namelist() if not safe_member(name, expected_root)]
        if unsafe:
            raise RuntimeError(f"{archive.name}: unsafe archive members: {unsafe}")
        if any(name.startswith(f"{expected_root}/sources/") for name in bundle.namelist()):
            raise RuntimeError(f"{archive.name}: sources/ must not be distributed")


PORTABLE_TOP_LEVEL = {"name", "description", "license", "allowed-tools", "metadata"}


def verify_archive_links(archive: Path) -> list[str]:
    """Resolve every relative Markdown link against the archive's own member list.

    validate_markdown_links checks the canonical working tree, where every target
    exists. That says nothing about a *packaged* subset: a bundle that ships skills
    without reference/ passes the canonical check and still hands an agent six dead
    links per skill. This closes that gap by checking the artifact actually shipped.
    """
    errors: list[str] = []
    with zipfile.ZipFile(archive) as bundle:
        members = set(bundle.namelist())
        for name in sorted(members):
            if not name.lower().endswith(".md"):
                continue
            text = bundle.read(name).decode("utf-8", errors="replace")
            base = PurePosixPath(name).parent
            for raw_target in MARKDOWN_LINK.findall(text):
                target = raw_target.strip().split(maxsplit=1)[0].strip("<>")
                if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                    continue
                local = target.split("#", 1)[0]
                if not local:
                    continue
                candidate = os.path.normpath(str(base / local))
                # A link may name a file or a directory. Archives store no directory
                # entries, so a directory is present when some member sits beneath it.
                if candidate in members:
                    continue
                if any(member.startswith(f"{candidate}/") for member in members):
                    continue
                errors.append(f"{archive.name}: {name} -> {target} is not in the archive")
    return errors


def verify_portable_archives(archives: list[Path], version: str) -> None:
    """Prove every Codex-facing archive carries strict frontmatter and generated metadata."""
    for archive in archives:
        if archive.name == f"market-intelligence-v{version}.zip":
            continue
        with zipfile.ZipFile(archive) as bundle:
            names = bundle.namelist()
            skill_files = [name for name in names if name.endswith("/SKILL.md")]
            if not skill_files:
                raise RuntimeError(f"{archive.name}: contains no SKILL.md")
            for name in skill_files:
                data, _ = parse_skill(bundle.read(name).decode("utf-8"))
                extra = sorted(set(data) - PORTABLE_TOP_LEVEL)
                if extra:
                    raise RuntimeError(f"{archive.name}: {name} has non-portable frontmatter keys {extra}")
                if not isinstance(data.get("metadata"), dict):
                    raise RuntimeError(f"{archive.name}: {name} lost its metadata map")
                generated = name.replace("/SKILL.md", "/agents/openai.yaml")
                if generated not in names:
                    raise RuntimeError(f"{archive.name}: {generated} was not generated")


def _write(path: Path, text: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    path.chmod(0o644)
    return path


OUTWARD_LINK = re.compile(r"\[([^\]]+)\]\(\.\./[^)]*\)")


def utility_skills(root: Path = ROOT) -> list[str]:
    """No utility tier in this Project. Every skill is a registered stage skill."""
    return []


def stage_portable_skill(
    skill: str, destination: Path, root: Path = ROOT, standalone: bool = False
) -> list[Path]:
    """Project one canonical skill onto the strict portable shape under `destination`.

    The canonical SKILL.md keeps rich list-shaped frontmatter for human review. Here it
    becomes the name/description/license/metadata form the portable standard accepts,
    and agents/openai.yaml is generated from the canonical interface block so the two
    can never drift.

    `standalone` additionally makes the skill self-contained. A single-skill archive is
    rooted at the skill itself, so `../../reference/...` escapes the archive and can
    never resolve. The shared contracts the skill actually needs at run time are copied
    in beside it and the links are repointed. Those copies then have their own outward
    links flattened to plain text, because following them would require shipping the
    rest of the Project.
    """
    source = root / "skills" / skill
    data, _ = parse_skill((source / "SKILL.md").read_text(encoding="utf-8"))
    if data["name"] != skill:
        raise RuntimeError(f"{skill}: frontmatter name does not match directory")

    body = portable_skill((source / "SKILL.md").read_text(encoding="utf-8"))
    if standalone:
        body = body.replace("../../reference/", "reference/")

    staged = [
        _write(destination / "SKILL.md", body),
        _write(destination / "agents" / "openai.yaml", openai_yaml(data)),
    ]

    if standalone:
        for path in sorted((root / "reference").glob("*.md")):
            staged.append(
                _write(
                    destination / "reference" / path.name,
                    OUTWARD_LINK.sub(r"\1", path.read_text(encoding="utf-8")),
                )
            )
    for path in sorted(source.rglob("*")):
        if not path.is_file() or is_ignored(path) or path.name == "SKILL.md":
            continue
        target = destination / path.relative_to(source)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(path, target)
        target.chmod(0o644)
        staged.append(target)
    return sorted(staged)


def build_archives(output_dir: Path, root: Path = ROOT) -> list[Path]:
    import tempfile

    version = (root / "VERSION").read_text(encoding="utf-8").strip()
    project_root = f"market-intelligence-v{version}"
    codex_root = f"market-intelligence-codex-v{version}"
    canonical = output_dir / f"{project_root}.zip"
    deterministic_zip(root, public_files(root), canonical, project_root)
    archives = [canonical]

    with tempfile.TemporaryDirectory(prefix="mintel-portable-") as staging_dir:
        staging = Path(staging_dir)
        codex_bundle = staging / "codex"

        # The Codex bundle carries the same public file set as the canonical archive,
        # differing only in skill frontmatter shape. It previously shipped skills alone,
        # which left every `../../reference/...` link in every SKILL.md pointing at a file
        # that was not in the archive -- 36 dead links that an agent hits at run time.
        for path in public_files(root):
            relative = path.relative_to(root)
            if relative.parts[0] == "skills":
                continue
            target = codex_bundle / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(path, target)
            target.chmod(0o644)

        # Stages and utilities are packaged identically. The distinction lives in the
        # frontmatter and the naming convention, not in how an archive is assembled.
        for skill in expected_skills(root) + utility_skills(root):
            stage_portable_skill(skill, codex_bundle / "skills" / skill, root)
            skill_staging = staging / "standalone" / skill
            files = stage_portable_skill(skill, skill_staging, root, standalone=True)
            archive = output_dir / f"{skill}-v{version}.zip"
            deterministic_zip(
                skill_staging,
                files,
                archive,
                skill,
                extra_files={"LICENSE": root / "LICENSE", "NOTICE.md": root / "NOTICE.md"},
            )
            archives.append(archive)

        codex_archive = output_dir / f"{codex_root}.zip"
        deterministic_zip(
            codex_bundle,
            sorted(path for path in codex_bundle.rglob("*") if path.is_file()),
            codex_archive,
            codex_root,
            # LICENSE, NOTICE.md, and README.md already arrive through the public file
            # set copied above; listing them again produced duplicate zip entries.
            # .codex-plugin/ is deliberately absent from the allowlist, so it is the
            # only member that still has to be added explicitly.
            extra_files={
                ".codex-plugin/plugin.json": root / ".codex-plugin" / "plugin.json",
            },
        )
        archives.append(codex_archive)

    for archive in archives:
        if archive == canonical:
            expected_root = project_root
        elif archive == codex_archive:
            expected_root = codex_root
        else:
            expected_root = archive.name.rsplit(f"-v{version}.zip", 1)[0]
        verify_zip(archive, expected_root)
    verify_portable_archives(archives, version)
    link_errors = [error for archive in archives for error in verify_archive_links(archive)]
    if link_errors:
        raise RuntimeError("\n".join(link_errors))
    checksums = output_dir / "SHA256SUMS"
    checksums.write_text("\n".join(f"{sha256(path)}  {path.name}" for path in archives) + "\n", encoding="utf-8")
    for line in checksums.read_text(encoding="utf-8").splitlines():
        expected, name = line.split("  ", 1)
        if sha256(output_dir / name) != expected:
            raise RuntimeError(f"checksum verification failed for {name}")
    return archives


def verify_reproducible(first: Path, second: Path) -> None:
    first_files = sorted(path.name for path in first.glob("*.zip"))
    second_files = sorted(path.name for path in second.glob("*.zip"))
    if first_files != second_files:
        raise RuntimeError("deterministic builds produced different archive sets")
    for name in first_files:
        if (first / name).read_bytes() != (second / name).read_bytes():
            raise RuntimeError(f"deterministic rebuild differs for {name}")


def verify_clean_extraction(canonical: Path, root: Path = ROOT) -> None:
    import tempfile

    version = (root / "VERSION").read_text(encoding="utf-8").strip()
    expected_root = f"market-intelligence-v{version}"
    with tempfile.TemporaryDirectory(prefix="mintel-release-") as temporary:
        destination = Path(temporary)
        with zipfile.ZipFile(canonical) as bundle:
            bundle.extractall(destination)
        extracted = destination / expected_root
        if (extracted / "sources").exists():
            raise RuntimeError("clean extraction unexpectedly contains sources/")
        subprocess.run([sys.executable, "scripts/test_library.py", "--canonical-only"], cwd=extracted, check=True)


def reset_directory(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True)
