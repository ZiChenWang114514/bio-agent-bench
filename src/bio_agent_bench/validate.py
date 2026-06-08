"""Validation helpers for submissions."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

from bio_agent_bench.schema import OUTPUT_SCHEMA


def load_json(path: str | Path) -> dict[str, Any]:
    with Path(path).open() as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return data


def validate_submission(path: str | Path) -> dict[str, Any]:
    submission = load_json(path)
    validator = Draft202012Validator(OUTPUT_SCHEMA)
    errors = sorted(validator.iter_errors(submission), key=lambda error: error.path)
    if errors:
        messages = []
        for error in errors:
            location = ".".join(str(part) for part in error.path) or "<root>"
            messages.append(f"{location}: {error.message}")
        raise ValueError("Submission schema validation failed:\n" + "\n".join(messages))
    return submission

