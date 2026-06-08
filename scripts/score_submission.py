#!/usr/bin/env python
"""Score a bio-agent-bench submission."""

from __future__ import annotations

import argparse

from bio_agent_bench.score import score_submission, write_score


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--task-root", required=True)
    parser.add_argument("--submission", required=True)
    parser.add_argument("--answer", required=True)
    parser.add_argument("--process-log")
    parser.add_argument("--out")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    result = score_submission(
        task_root=args.task_root,
        submission_path=args.submission,
        answer_path=args.answer,
        process_log_path=args.process_log,
    )
    write_score(result, args.out)


if __name__ == "__main__":
    main()

