# Evaluation Protocol

This protocol is meant for comparing coding agents on the same real
GEO-derived bioinformatics task pack.

## Agent Setup

Give each agent:

- One task directory containing public inputs only.
- The corresponding `prompt.md`.
- The shared `expected_output.schema.json`.
- Permission to use a terminal, write scripts, install Python packages if
  needed, and generate artifacts.

Do not give the agent:

- hidden answer JSON files.
- `.hidden/` content.
- Previous submissions or scorer output.

## Required Output

The agent must produce:

- `submission.json`
- At least one runnable analysis script.
- At least one artifact, usually a plot or score table.
- A process log or command summary.

`submission.json` is the only required machine-readable answer.

## Default Scoring

Total: 100 points.

- 50 answer correctness: anomaly type and anomalous group.
- 20 evidence quality: interpretable statistics and biological/QC rationale.
- 15 artifacts: non-empty files listed in `submission.json`.
- 15 process: terminal/tool usage, code execution, and data inspection traces.

For model comparisons, use the same hidden pack, same wall-clock limit, same
tool permissions, and same scoring script.

## Failure Modes To Record

Record these separately from numeric score:

- Did not run code.
- Submitted invalid JSON.
- Guessed answer without inspecting data.
- Rewrote or ignored task files.
- Produced artifacts that do not exist.
- Correct answer but unsupported evidence.
- Good analysis but wrong final JSON field names.

## Making The Benchmark Harder

When models become stronger, increase realism before increasing dataset size:

- Add multiple real GEO cohorts with weak confounders.
- Add hidden corrupted or low-quality samples.
- Add synonymous group labels requiring normalization.
- Add one misleading QC effect that is not the true anomaly.
- Require compatibility with a fixed output schema.
- Add process-log checks for actual data loading and script execution.
