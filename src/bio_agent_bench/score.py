"""Public scoring helpers for bio-agent-bench submissions."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from bio_agent_bench.validate import load_json, validate_submission


def _norm(value: object) -> str:
    text = str(value).strip().lower()
    text = re.sub(r"[^a-z0-9]+", "_", text)
    return text.strip("_")


def _artifact_exists(task_root: Path, submission_path: Path, artifact_path: str) -> bool:
    candidates = [
        submission_path.parent / artifact_path,
        task_root / artifact_path,
        Path(artifact_path),
    ]
    return any(path.exists() and path.is_file() and path.stat().st_size > 0 for path in candidates)


def score_submission(
    task_root: str | Path,
    submission_path: str | Path,
    answer_path: str | Path,
    process_log_path: str | Path | None = None,
) -> dict[str, Any]:
    """Score one submission against an answer key."""

    task_root = Path(task_root)
    submission_path = Path(submission_path)
    submission = validate_submission(submission_path)
    answer_key = load_json(answer_path)
    expected = answer_key["answer"]
    observed = submission["answer"]

    answer_score = 0
    if _norm(observed.get("anomaly_type")) == _norm(expected.get("anomaly_type")):
        answer_score += 25
    if _norm(observed.get("anomalous_group")) == _norm(expected.get("anomalous_group")):
        answer_score += 25

    evidence = submission.get("evidence", [])
    stats = observed.get("key_statistics", {})
    evidence_score = min(10, len(evidence) * 5)
    if isinstance(stats, dict) and stats:
        numeric_stats = sum(isinstance(value, (int, float)) for value in stats.values())
        evidence_score += min(10, numeric_stats * 4)

    artifacts = submission.get("artifacts", [])
    existing_artifacts = [
        item for item in artifacts if _artifact_exists(task_root, submission_path, item.get("path", ""))
    ]
    artifact_score = min(15, len(existing_artifacts) * 8)

    commands = "\n".join(submission.get("commands_summary", []))
    if process_log_path:
        log_path = Path(process_log_path)
        if log_path.exists():
            commands += "\n" + log_path.read_text(errors="replace")
    command_keywords = ["python", "read", "pandas", "anndata", "plot", "test", "qc", "pca"]
    keyword_hits = sum(keyword in commands.lower() for keyword in command_keywords)
    process_score = min(15, len(submission.get("commands_summary", [])) * 3 + keyword_hits)

    total = answer_score + evidence_score + artifact_score + process_score
    return {
        "total": int(total),
        "max_score": 100,
        "subscores": {
            "answer": int(answer_score),
            "evidence": int(evidence_score),
            "artifacts": int(artifact_score),
            "process": int(process_score),
        },
        "expected": {
            "anomaly_type": expected.get("anomaly_type"),
            "anomalous_group": expected.get("anomalous_group"),
        },
        "observed": {
            "anomaly_type": observed.get("anomaly_type"),
            "anomalous_group": observed.get("anomalous_group"),
        },
        "passed_schema": True,
        "existing_artifacts": [item.get("path") for item in existing_artifacts],
    }


def write_score(result: dict[str, Any], output_path: str | Path | None = None) -> None:
    text = json.dumps(result, indent=2) + "\n"
    if output_path:
        Path(output_path).write_text(text)
    else:
        print(text, end="")

