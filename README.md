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

## 使用本地 Coding Agent

本节说明如何用本机的 `ccsds`、`ccskm`、`vvcc`、`mycd` 跑这个 benchmark。

不要从仓库根目录直接启动这些 agent。它们如果在仓库根目录工作，理论上能看到整个工作树，包括 docs、raw GEO 下载和本地 hidden 文件。正确流程是：先创建一个干净的 task bundle，再从该 run 的 writable workspace 启动 agent。

### 本机 Agent 命令

本机可用于对比的命令如下：

| 命令 | Agent/Product | 建议对比标签 |
|---|---|---|
| `ccsds` | Claude Code via DeepSeek V4 provider | `deepseek` |
| `ccskm` | Claude Code via Kimi/Moonshot provider | `kimi` |
| `vvcc` | Claude Code via local VVCC proxy wrapper | `claude` |
| `mycd` | Codex CLI wrapper | `codex` |

这些命令需要访问各自的模型服务，因此不能直接放进 `--network none` 的 Docker agent 容器里运行。这里采用折中但可审计的方式：benchmark 脚本先在 `runs/` 下生成一个干净目录，agent 只在这个目录中工作。

### 第一步：创建干净 Run 目录

从仓库根目录执行：

```bash
cd /data2/zcwang/homeworks/bio-agent-bench

scripts/run_task_container.sh \
  --task geo_bulk_alms1_ko \
  --run-id ccsds_bulk_001 \
  --command "true"
```

这会创建：

```text
runs/ccsds_bulk_001/geo_bulk_alms1_ko/task/
runs/ccsds_bulk_001/geo_bulk_alms1_ko/workspace/
```

`task/` 目录只包含 closed-book task bundle：

```text
prompt.md
expected_output.schema.json
public_notes.md
data/
```

`workspace/` 是 agent 的工作目录，所有输出都应写到这里。

### 第二步：从 Workspace 启动 Agent

DeepSeek via Claude Code：

```bash
cd /data2/zcwang/homeworks/bio-agent-bench/runs/ccsds_bulk_001/geo_bulk_alms1_ko/workspace
ccsds
```

Kimi via Claude Code：

```bash
cd /data2/zcwang/homeworks/bio-agent-bench
scripts/run_task_container.sh --task geo_bulk_alms1_ko --run-id ccskm_bulk_001 --command "true"
cd runs/ccskm_bulk_001/geo_bulk_alms1_ko/workspace
ccskm
```

Claude Code via VVCC wrapper：

```bash
cd /data2/zcwang/homeworks/bio-agent-bench
scripts/run_task_container.sh --task geo_bulk_alms1_ko --run-id vvcc_bulk_001 --command "true"
cd runs/vvcc_bulk_001/geo_bulk_alms1_ko/workspace
vvcc
```

Codex：

```bash
cd /data2/zcwang/homeworks/bio-agent-bench
scripts/run_task_container.sh --task geo_bulk_alms1_ko --run-id mycd_bulk_001 --command "true"
cd runs/mycd_bulk_001/geo_bulk_alms1_ko/workspace
mycd
```

如果要跑 scRNA 任务，只替换 task 和 run id：

```bash
scripts/run_task_container.sh \
  --task geo_scrna_nec_inflammation \
  --run-id ccsds_scrna_001 \
  --command "true"

cd runs/ccsds_scrna_001/geo_scrna_nec_inflammation/workspace
ccsds
```

### 第三步：给 Agent 的统一 Prompt

启动 agent 后，把下面这段直接粘贴进去：

```text
你正在一个 closed-book bioinformatics benchmark workspace 中工作。

请先阅读 ../task/prompt.md。只能使用 ../task 下的文件和当前工作目录。不要查看仓库根目录、docs、.hidden、data/raw_geo、git history，也不要使用互联网。不要根据 GEO accession 或 source provenance 推断标签；必须直接分析给定数据。

所有输出都写到当前目录。

你必须创建：
1. submission.json，并符合 ../task/expected_output.schema.json
2. 至少一个可运行的分析脚本
3. 至少一个非空的图或表 artifact，并在 submission.json 中列出

结束前请验证 submission.json 存在，并且 submission.json 中列出的每个 artifact 路径都真实存在。
```

理想情况下，最终 workspace 至少包含：

```text
analysis.py
submission.json
<一个或多个 .png/.pdf/.tsv/.csv artifacts>
```

### 第四步：评分

agent 完成后，回到仓库根目录，用 evaluator sandbox 评分：

```bash
cd /data2/zcwang/homeworks/bio-agent-bench

scripts/score_run_container.sh \
  --task geo_bulk_alms1_ko \
  --run-id ccsds_bulk_001
```

分数会写到：

```text
runs/ccsds_bulk_001/geo_bulk_alms1_ko/workspace/score.json
```

scRNA 任务对应：

```bash
scripts/score_run_container.sh \
  --task geo_scrna_nec_inflammation \
  --run-id ccsds_scrna_001
```

### 建议 Run Matrix

建议使用统一的 run id，方便后续汇总和审计：

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

然后分别进入每个 workspace，启动对应的 agent 命令。

### 可选：记录 Process Log

如果终端支持，可以用 `script` 记录交互过程：

```bash
cd runs/ccsds_bulk_001/geo_bulk_alms1_ko/workspace
script -q -f process.log -c "ccsds"
```

评分时把 log 一起传入：

```bash
scripts/score_run_container.sh \
  --task geo_bulk_alms1_ko \
  --run-id ccsds_bulk_001 \
  --process-log runs/ccsds_bulk_001/geo_bulk_alms1_ko/workspace/process.log
```

### 重要对比规则

- 每个模型和任务使用一个新的 `--run-id`。
- 不要从仓库根目录启动 agent。
- 不要把 `.hidden/`、`data/raw_geo/`、`docs/data_sources.md` 提供给 agent。
- 不要把 closed-book 和 open-world run 混在同一张分数表里。
- 所有被比较的 agent 应使用同一份 task bundle、同一套 timeout 策略、同一个 scorer commit 和同一个 hidden answer 文件。
- 如果 agent 因为“不能访问互联网”而拒绝，仍然从 sanitized workspace 正常启动本地 wrapper；agent 可以访问自己的模型服务，但不应该浏览外部数据源。

## Scoring

Default total: 100 points.

- Answer correctness: 50
- Evidence quality: 20
- Artifact presence: 15
- Process trace: 15

The public scorer is intentionally lightweight. Hidden scoring can use stricter
answer normalization and stronger artifact/log checks while preserving the same
JSON interface.
