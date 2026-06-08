"""Submission schema shared by all task families."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


OUTPUT_SCHEMA: dict[str, Any] = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "bio-agent-bench submission",
    "type": "object",
    "additionalProperties": False,
    "required": [
        "task_id",
        "answer",
        "confidence",
        "evidence",
        "artifacts",
        "commands_summary",
    ],
    "properties": {
        "task_id": {"type": "string", "minLength": 1},
        "answer": {
            "type": "object",
            "additionalProperties": True,
            "required": ["anomaly_type", "anomalous_group", "rationale"],
            "properties": {
                "anomaly_type": {"type": "string", "minLength": 1},
                "anomalous_group": {"type": "string", "minLength": 1},
                "rationale": {"type": "string", "minLength": 20},
                "key_statistics": {
                    "type": "object",
                    "additionalProperties": {
                        "type": ["number", "integer", "string", "boolean", "null"]
                    },
                },
            },
        },
        "confidence": {"type": "number", "minimum": 0, "maximum": 1},
        "evidence": {
            "type": "array",
            "minItems": 1,
            "items": {
                "type": "object",
                "required": ["type", "description"],
                "additionalProperties": True,
                "properties": {
                    "type": {"type": "string", "minLength": 1},
                    "description": {"type": "string", "minLength": 10},
                    "value": {
                        "type": ["number", "integer", "string", "boolean", "null"]
                    },
                },
            },
        },
        "artifacts": {
            "type": "array",
            "minItems": 1,
            "items": {
                "type": "object",
                "required": ["type", "path", "description"],
                "additionalProperties": True,
                "properties": {
                    "type": {"type": "string", "minLength": 1},
                    "path": {"type": "string", "minLength": 1},
                    "description": {"type": "string", "minLength": 10},
                },
            },
        },
        "commands_summary": {
            "type": "array",
            "minItems": 1,
            "items": {"type": "string", "minLength": 3},
        },
    },
}


def write_schema(path: str | Path) -> None:
    """Write the shared schema to a JSON file."""

    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(OUTPUT_SCHEMA, indent=2) + "\n")

