#!/usr/bin/env python3
"""Build and verify the public-preview release archives."""

from __future__ import annotations

from release_tools import ROOT, build_archives, reset_directory, run_canonical_checks, verify_clean_extraction


def main() -> int:
    output = ROOT / "dist" / "release"
    run_canonical_checks(ROOT)
    reset_directory(output)
    archives = build_archives(output, ROOT)
    verify_clean_extraction(archives[0], ROOT)
    print(f"Built and verified {len(archives)} archives plus {output / 'SHA256SUMS'}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
