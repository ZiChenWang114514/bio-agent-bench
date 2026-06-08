#!/usr/bin/env python
"""Prepare public task packs from downloaded GEO supplementary files."""

from __future__ import annotations

from pathlib import Path

from bio_agent_bench.geo import decompress_h5ad_if_needed, prepare_all_geo_tasks


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    decompress_h5ad_if_needed(root)
    prepare_all_geo_tasks(root)
    print("Prepared GEO task packs.")


if __name__ == "__main__":
    main()

