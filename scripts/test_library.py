#!/usr/bin/env python3
"""Run the canonical and clean-distribution release gate."""

from __future__ import annotations

import argparse
import tempfile
from pathlib import Path

from release_tools import ROOT, build_archives, run_canonical_checks, verify_clean_extraction, verify_reproducible


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--canonical-only", action="store_true", help="skip archive rebuild and extraction checks")
    args = parser.parse_args()

    run_canonical_checks(ROOT)
    if args.canonical_only:
        print("Canonical repository checks passed.")
        return 0

    with tempfile.TemporaryDirectory(prefix="mintel-build-a-") as first_tmp, tempfile.TemporaryDirectory(
        prefix="mintel-build-b-"
    ) as second_tmp:
        first = Path(first_tmp)
        second = Path(second_tmp)
        archives = build_archives(first, ROOT)
        build_archives(second, ROOT)
        verify_reproducible(first, second)
        verify_clean_extraction(archives[0], ROOT)

    print("Release gate passed: canonical checks, deterministic archives, and clean extraction.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
