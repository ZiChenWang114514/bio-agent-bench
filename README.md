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

## Scoring

Default total: 100 points.

- Answer correctness: 50
- Evidence quality: 20
- Artifact presence: 15
- Process trace: 15

The public scorer is intentionally lightweight. Hidden scoring can use stricter
answer normalization and stronger artifact/log checks while preserving the same
JSON interface.
