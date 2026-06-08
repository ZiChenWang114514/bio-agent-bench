from __future__ import annotations

import json
from pathlib import Path

from bio_agent_bench.score import score_submission


def test_public_scorer_minimal(tmp_path: Path) -> None:
    artifact = tmp_path / "artifact.tsv"
    artifact.write_text("x\ty\n")
    submission = {
        "task_id": "geo_bulk_alms1_ko",
        "answer": {
            "anomaly_type": "knockout_gene",
            "anomalous_group": "group_beta",
            "rationale": "ALMS1 expression is lower in group_beta than in group_alpha.",
            "key_statistics": {"effect": -1.1},
        },
        "confidence": 0.8,
        "evidence": [{"type": "target_gene", "description": "ALMS1 is reduced.", "value": -1.1}],
        "artifacts": [{"type": "table", "path": "artifact.tsv", "description": "A small table."}],
        "commands_summary": ["python analysis.py", "read rlog.tsv with pandas"],
    }
    answer = {
        "task_id": "geo_bulk_alms1_ko",
        "answer": {
            "anomaly_type": "knockout_gene",
            "anomalous_group": "group_beta",
            "rationale": "hidden answer",
        },
    }
    submission_path = tmp_path / "submission.json"
    answer_path = tmp_path / "answer.json"
    submission_path.write_text(json.dumps(submission))
    answer_path.write_text(json.dumps(answer))
    result = score_submission(tmp_path, submission_path, answer_path)
    assert result["subscores"]["answer"] == 50
    assert result["total"] >= 75

