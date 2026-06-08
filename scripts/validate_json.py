#!/usr/bin/env python
"""Validate a bio-agent-bench submission JSON."""

from __future__ import annotations

import argparse

from bio_agent_bench.validate import validate_submission


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--submission", required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    validate_submission(args.submission)
    print("OK: submission matches schema")


if __name__ == "__main__":
    main()

