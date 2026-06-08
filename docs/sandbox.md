# Sandbox And Docker Protocol

The default evaluation mode is **closed-book**. The agent should analyze the
provided data, not browse GEO pages or inspect hidden answer keys.

## Two Sandboxes

### Agent Sandbox

The agent sandbox contains only:

- `/task/prompt.md`
- `/task/expected_output.schema.json`
- `/task/public_notes.md`
- `/task/data/*`
- `/workspace`, a writable output directory

The agent sandbox does not contain:

- `.hidden/`
- raw GEO downloads
- scorer output
- repository documentation with source accessions
- network access

Default limits:

- network: disabled
- CPU: 4
- memory: 16 GB
- writable paths: `/workspace`, `/tmp`
- root filesystem: read-only
- required output: `/workspace/submission.json`

The container runs as root inside the sandbox so bind-mounted workspaces remain
writable across Docker daemons with user namespace remapping. The root
filesystem is still read-only, Linux capabilities are dropped, network is
disabled, and writes are limited to mounted workspace paths.

### Evaluator Sandbox

The evaluator sandbox contains:

- the agent's `/workspace`
- the sanitized `/task` bundle
- one hidden answer file mounted as `/hidden/answer.json`

The evaluator writes `/workspace/score.json`.

## Build Images

```bash
scripts/build_docker_images.sh
```

This builds:

- `bio-agent-bench-agent:latest`
- `bio-agent-bench-evaluator:latest`

## Run A Task

```bash
scripts/run_task_container.sh \
  --task geo_bulk_alms1_ko \
  --run-id model_a_bulk \
  --timeout-seconds 1800
```

Inside the container:

```bash
ls /task
ls /task/data
python analysis.py
```

In practice, the coding agent should work in `/workspace`, read data from
`/task/data`, and write:

```text
/workspace/submission.json
/workspace/<analysis scripts, plots, tables>
```

To run a non-interactive command:

```bash
scripts/run_task_container.sh \
  --task geo_scrna_nec_inflammation \
  --run-id smoke_scrna \
  --command "python -V && ls /task/data"
```

## Score A Run

```bash
scripts/score_run_container.sh \
  --task geo_bulk_alms1_ko \
  --run-id model_a_bulk
```

This reads:

```text
runs/model_a_bulk/geo_bulk_alms1_ko/workspace/submission.json
.hidden/geo_answers/geo_bulk_alms1_ko_answer.hidden.json
```

and writes:

```text
runs/model_a_bulk/geo_bulk_alms1_ko/workspace/score.json
```

If you have a real shell transcript:

```bash
scripts/score_run_container.sh \
  --task geo_bulk_alms1_ko \
  --run-id model_a_bulk \
  --process-log runs/model_a_bulk/geo_bulk_alms1_ko/workspace/process.log
```

## Recommended Comparison Rules

Use the same settings for every model:

- same task bundle
- same Docker image
- same CPU/memory limits
- same timeout
- same network setting
- same hidden answer file
- same scorer commit

Record separately:

- invalid JSON
- missing artifacts
- no code execution evidence
- process timeout
- out-of-memory failure
- correct answer with weak evidence

## Open-World Variant

If you want to evaluate web-enabled agents, make it a separate track. Enable
network access and keep the GEO provenance visible, then report results as
`open_world`. Do not mix open-world and closed-book scores.
