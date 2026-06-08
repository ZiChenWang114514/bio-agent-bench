# bio-agent-bench

Small BioMysteryBench-inspired tasks for evaluating coding agents on practical
bioinformatics analysis with real public GEO processed data.

The benchmark gives an agent a compact biological dataset, asks it to inspect
the files from a terminal, write analysis code, generate QC/statistical
artifacts, and return a fixed `submission.json`. Scoring combines hidden
answers with lightweight checks on evidence, artifacts, and process logs.

This repository is public. Raw GEO downloads and hidden answer keys live under
gitignored local directories and are not committed.

## Task Families

### `geo_bulk_alms1_ko`

Input files:

- `counts.tsv`: raw counts from GSE209844, genes by blinded samples.
- `rlog.tsv`: DESeq2 rlog-normalized expression.
- `sample_sheet.tsv`: blinded sample group metadata.
- `gene_annotations.tsv`: Ensembl IDs and symbols.

Question:

> One blinded group is ALMS1 knockout and the other is wild type. Determine
> which blinded group is the knockout group.

Expected agent behavior:

- Load the matrix and metadata from the terminal.
- Run QC and at least one statistical comparison or variance/effect analysis.
- Save an analysis script and at least one plot or table.
- Emit `submission.json`.

### `geo_scrna_nec_inflammation`

Input files:

- `adata.h5ad`: blinded single-cell object from GSE178088.
- `metadata.tsv`: exported blinded cell metadata.
- `sample_sheet.tsv`: blinded sample-level cell counts.
- `gene_annotations.tsv`: gene symbols.

Question:

> Which blinded cohort shows the strongest inflammation-associated abnormality?

Expected agent behavior:

- Read the `.h5ad` file with `anndata`.
- Compute basic QC and group-level expression summaries.
- Save an analysis script and at least one plot or table.
- Emit `submission.json`.

## Install

Use an isolated environment. The default conda base on some machines may contain
mixed NumPy wheels, so a venv is safer.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
python -m pip install -e ".[dev]"
```

## Prepare GEO Data

Download raw GEO supplementary files into `data/raw_geo/`:

```bash
mkdir -p data/raw_geo/GSE209844 data/raw_geo/GSE178088
curl -L -o data/raw_geo/GSE209844/GSE209844_CountMatrixMerged.txt.gz \
  https://ftp.ncbi.nlm.nih.gov/geo/series/GSE209nnn/GSE209844/suppl/GSE209844_CountMatrixMerged.txt.gz
curl -L -o data/raw_geo/GSE209844/GSE209844_NormalizedCountMatrix_rlog.txt.gz \
  https://ftp.ncbi.nlm.nih.gov/geo/series/GSE209nnn/GSE209844/suppl/GSE209844_NormalizedCountMatrix_rlog.txt.gz
curl -L -o data/raw_geo/GSE209844/GSE209844_RNA-seq_results_DESeq2.txt.gz \
  https://ftp.ncbi.nlm.nih.gov/geo/series/GSE209nnn/GSE209844/suppl/GSE209844_RNA-seq_results_DESeq2.txt.gz
curl -L -o data/raw_geo/GSE178088/GSE178088_cluster3.h5ad.gz \
  https://ftp.ncbi.nlm.nih.gov/geo/series/GSE178nnn/GSE178088/suppl/GSE178088_cluster3.h5ad.gz
```

Prepare blinded public task packs and local hidden answer keys:

```bash
python scripts/prepare_geo_tasks.py
```

## Validate And Score

Validate a submission:

```bash
python scripts/validate_json.py \
  --submission examples/baseline_outputs/geo_bulk/submission.json
```

Score with a local hidden answer key:

```bash
python scripts/score_submission.py \
  --task-root tasks/geo_bulk_alms1_ko/data/public_geo \
  --submission examples/baseline_outputs/geo_bulk/submission.json \
  --answer .hidden/geo_answers/geo_bulk_alms1_ko_answer.hidden.json
```

## Submission Format

Agents must write a JSON object with these top-level fields:

- `task_id`
- `answer`
- `confidence`
- `evidence`
- `artifacts`
- `commands_summary`

See `tasks/*/expected_output.schema.json` for the exact schema.

## Docker Sandbox

Build the predefined agent/evaluator images:

```bash
scripts/build_docker_images.sh
```

Run a closed-book agent sandbox:

```bash
scripts/run_task_container.sh \
  --task geo_bulk_alms1_ko \
  --run-id model_a_bulk
```

Score the resulting `/workspace/submission.json` with hidden answers:

```bash
scripts/score_run_container.sh \
  --task geo_bulk_alms1_ko \
  --run-id model_a_bulk
```

The canonical sandbox settings are in `benchmark.yaml`; details are in
`docs/sandbox.md`.

## Running Local Coding Agents

This is the recommended workflow for local agent commands such as `ccsds`,
`ccskm`, `vvcc`, and `mycd`.

Do **not** launch these agents from the repository root. They can see the whole
working tree if started there, including docs, raw GEO downloads, and local
hidden files. Instead, first create a sanitized task bundle, then start the
agent from that run's writable workspace.

### Local Agent Commands

The commands used on this machine are:

| Command | Agent/Product | Intended comparison label |
|---|---|---|
| `ccsds` | Claude Code via DeepSeek V4 provider | `deepseek` |
| `ccskm` | Claude Code via Kimi/Moonshot provider | `kimi` |
| `vvcc` | Claude Code via the local VVCC proxy wrapper | `claude` |
| `mycd` | Codex CLI wrapper | `codex` |

These commands need outbound network access to their model providers. Therefore
they are not launched inside the `--network none` Docker agent container.
Instead, the benchmark scripts create a clean task directory under `runs/`, and
the agent is instructed to use only that directory.

### Step 1: Create A Sanitized Run Directory

From the repository root:

```bash
cd /data2/zcwang/homeworks/bio-agent-bench

scripts/run_task_container.sh \
  --task geo_bulk_alms1_ko \
  --run-id ccsds_bulk_001 \
  --command "true"
```

This creates:

```text
runs/ccsds_bulk_001/geo_bulk_alms1_ko/task/
runs/ccsds_bulk_001/geo_bulk_alms1_ko/workspace/
```

The `task/` directory contains only the closed-book task bundle:

```text
prompt.md
expected_output.schema.json
public_notes.md
data/
```

The `workspace/` directory is where the agent writes all outputs.

### Step 2: Start The Agent From The Workspace

For DeepSeek via Claude Code:

```bash
cd /data2/zcwang/homeworks/bio-agent-bench/runs/ccsds_bulk_001/geo_bulk_alms1_ko/workspace
ccsds
```

For Kimi via Claude Code:

```bash
cd /data2/zcwang/homeworks/bio-agent-bench
scripts/run_task_container.sh --task geo_bulk_alms1_ko --run-id ccskm_bulk_001 --command "true"
cd runs/ccskm_bulk_001/geo_bulk_alms1_ko/workspace
ccskm
```

For Claude Code through the VVCC wrapper:

```bash
cd /data2/zcwang/homeworks/bio-agent-bench
scripts/run_task_container.sh --task geo_bulk_alms1_ko --run-id vvcc_bulk_001 --command "true"
cd runs/vvcc_bulk_001/geo_bulk_alms1_ko/workspace
vvcc
```

For Codex:

```bash
cd /data2/zcwang/homeworks/bio-agent-bench
scripts/run_task_container.sh --task geo_bulk_alms1_ko --run-id mycd_bulk_001 --command "true"
cd runs/mycd_bulk_001/geo_bulk_alms1_ko/workspace
mycd
```

For the scRNA task, replace the task and run id:

```bash
scripts/run_task_container.sh \
  --task geo_scrna_nec_inflammation \
  --run-id ccsds_scrna_001 \
  --command "true"

cd runs/ccsds_scrna_001/geo_scrna_nec_inflammation/workspace
ccsds
```

### Step 3: Prompt To Give The Agent

Paste this into the coding agent:

```text
You are in a closed-book bioinformatics benchmark workspace.

Read ../task/prompt.md first. Use only files under ../task and the current
working directory. Do not inspect the repository root, docs, .hidden,
data/raw_geo, git history, or the internet. Do not infer labels from GEO
accessions or source provenance. Analyze the provided data directly.

Write all outputs in the current directory.

You must create:
1. submission.json following ../task/expected_output.schema.json
2. at least one runnable analysis script
3. at least one non-empty plot or table artifact listed in submission.json

Before finishing, verify that submission.json exists and every artifact path
listed in it exists.
```

The expected final workspace should look roughly like:

```text
analysis.py
submission.json
<one or more .png/.pdf/.tsv/.csv artifacts>
```

### Step 4: Score The Run

Return to the repository root and score with the evaluator sandbox:

```bash
cd /data2/zcwang/homeworks/bio-agent-bench

scripts/score_run_container.sh \
  --task geo_bulk_alms1_ko \
  --run-id ccsds_bulk_001
```

The score is written to:

```text
runs/ccsds_bulk_001/geo_bulk_alms1_ko/workspace/score.json
```

For scRNA:

```bash
scripts/score_run_container.sh \
  --task geo_scrna_nec_inflammation \
  --run-id ccsds_scrna_001
```

### Suggested Run Matrix

Use consistent run ids so model comparisons are easy to audit:

```bash
# bulk
scripts/run_task_container.sh --task geo_bulk_alms1_ko --run-id ccsds_bulk_001 --command "true"
scripts/run_task_container.sh --task geo_bulk_alms1_ko --run-id ccskm_bulk_001 --command "true"
scripts/run_task_container.sh --task geo_bulk_alms1_ko --run-id vvcc_bulk_001 --command "true"
scripts/run_task_container.sh --task geo_bulk_alms1_ko --run-id mycd_bulk_001 --command "true"

# scRNA
scripts/run_task_container.sh --task geo_scrna_nec_inflammation --run-id ccsds_scrna_001 --command "true"
scripts/run_task_container.sh --task geo_scrna_nec_inflammation --run-id ccskm_scrna_001 --command "true"
scripts/run_task_container.sh --task geo_scrna_nec_inflammation --run-id vvcc_scrna_001 --command "true"
scripts/run_task_container.sh --task geo_scrna_nec_inflammation --run-id mycd_scrna_001 --command "true"
```

Then enter each workspace and launch the corresponding agent command.

### Optional: Keep A Process Log

If the terminal supports it, record the interactive session with `script`:

```bash
cd runs/ccsds_bulk_001/geo_bulk_alms1_ko/workspace
script -q -f process.log -c "ccsds"
```

Then include the log in scoring:

```bash
scripts/score_run_container.sh \
  --task geo_bulk_alms1_ko \
  --run-id ccsds_bulk_001 \
  --process-log runs/ccsds_bulk_001/geo_bulk_alms1_ko/workspace/process.log
```

### Important Comparison Rules

- Use a fresh `--run-id` for each model and task.
- Do not launch agents from the repository root.
- Do not provide `.hidden/`, `data/raw_geo/`, or `docs/data_sources.md` to the
  agent.
- Do not mix closed-book and open-world runs in the same score table.
- Keep the same task bundle, timeout policy, scorer commit, and hidden answer
  file across all compared agents.
- If an agent refuses because it cannot access the internet, use the local
  wrapper command normally from the sanitized workspace; the agent may contact
  its model provider, but it should not browse external data sources.

## Scoring

Default total: 100 points.

- Answer correctness: 50
- Evidence quality: 20
- Artifact presence: 15
- Process trace: 15

The public scorer is intentionally lightweight. Hidden scoring can use stricter
answer normalization and stronger artifact/log checks while preserving the same
JSON interface.
