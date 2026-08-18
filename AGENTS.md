# Agents

See [`CLAUDE.md`](CLAUDE.md) for the working contract, and [`CONSTITUTION.md`](CONSTITUTION.md) for the rules that override it.

The short version:

1. **Never invent evidence.** Not a figure, a quote, a price, a patent, a filing, or a URL. In any file, including examples.
2. **Read [`docs/SKILL-SPEC.md`](docs/SKILL-SPEC.md)** before touching anything under `skills/`.
3. **Run `./scripts/test-library.sh`** and get it green before you are done.
4. **Edit `SKILL_REGISTRY`** in `scripts/validate-skills.py` first when adding a skill.
5. **ASCII only, no emojis, no mermaid** under `skills/` and `prompts/`.
6. **Every example is synthetic**, says so at the top, and uses `example.invalid` URLs.
7. **This is not software.** It is instructional material. Use the language in `CLAUDE.md`.
