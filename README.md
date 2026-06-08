# bio-agent-bench

一个基于真实公开 GEO 已处理数据的小型生物信息学编程智能体评测。目标是测试智能体是否能在受控目录中读取数据、写脚本、做质控和统计分析、生成结果文件，并按固定 JSON 结构输出答案。

本仓库是公开仓库。原始 GEO 下载、隐藏答案和本地评分材料都放在被 `.gitignore` 忽略的目录中，不提交到 GitHub。

## 最直接的测试方法

当前已经预创建好 8 个正式运行目录。你可以直接进入对应 `workspace/` 启动智能体。

### 1. 进入某个工作目录

DeepSeek / bulk 任务：

```bash
cd /data2/zcwang/homeworks/bio-agent-bench/runs/ccsds_bulk_001/geo_bulk_alms1_ko/workspace
ccsds
```

Kimi / bulk 任务：

```bash
cd /data2/zcwang/homeworks/bio-agent-bench/runs/ccskm_bulk_001/geo_bulk_alms1_ko/workspace
ccskm
```

Claude / bulk 任务：

```bash
cd /data2/zcwang/homeworks/bio-agent-bench/runs/vvcc_bulk_001/geo_bulk_alms1_ko/workspace
vvcc
```

Codex / bulk 任务：

```bash
cd /data2/zcwang/homeworks/bio-agent-bench/runs/mycd_bulk_001/geo_bulk_alms1_ko/workspace
mycd
```

scRNA 任务对应工作目录：

```text
/data2/zcwang/homeworks/bio-agent-bench/runs/ccsds_scrna_001/geo_scrna_nec_inflammation/workspace
/data2/zcwang/homeworks/bio-agent-bench/runs/ccskm_scrna_001/geo_scrna_nec_inflammation/workspace
/data2/zcwang/homeworks/bio-agent-bench/runs/vvcc_scrna_001/geo_scrna_nec_inflammation/workspace
/data2/zcwang/homeworks/bio-agent-bench/runs/mycd_scrna_001/geo_scrna_nec_inflammation/workspace
```

### 2. 把这个提示词粘贴给智能体

```text
你正在一个闭卷生物信息学评测工作目录中工作。

请先阅读 ../task/prompt.md。只能使用 ../task 下的文件和当前工作目录。不要查看仓库根目录、docs、.hidden、data/raw_geo、git 历史，也不要使用互联网。不要根据 GEO 编号或数据来源说明推断标签；必须直接分析给定数据。

所有输出都写到当前目录。

你必须创建：
1. submission.json，并符合 ../task/expected_output.schema.json
2. 至少一个可运行的分析脚本
3. 至少一个非空的图或表结果文件，并在 submission.json 中列出

结束前请验证 submission.json 存在，并且 submission.json 中列出的每个结果文件路径都真实存在。
```

智能体完成后，`workspace/` 至少应有：

```text
analysis.py
submission.json
一个或多个 .png/.pdf/.tsv/.csv 结果文件
```

### 3. 回到仓库根目录评分

bulk 示例：

```bash
cd /data2/zcwang/homeworks/bio-agent-bench

scripts/score_run_container.sh \
  --task geo_bulk_alms1_ko \
  --run-id ccsds_bulk_001

cat runs/ccsds_bulk_001/geo_bulk_alms1_ko/workspace/score.json
```

scRNA 示例：

```bash
cd /data2/zcwang/homeworks/bio-agent-bench

scripts/score_run_container.sh \
  --task geo_scrna_nec_inflammation \
  --run-id ccsds_scrna_001

cat runs/ccsds_scrna_001/geo_scrna_nec_inflammation/workspace/score.json
```

只需要把 `--run-id` 换成对应模型即可，例如 `ccskm_bulk_001`、`vvcc_scrna_001`、`mycd_bulk_001`。

## 本机智能体命令

| 命令 | 实际用途 | 建议对比标签 |
|---|---|---|
| `ccsds` | 通过 DeepSeek V4 服务运行 Claude Code | `deepseek` |
| `ccskm` | 通过 Kimi/Moonshot 服务运行 Claude Code | `kimi` |
| `vvcc` | 通过本地 VVCC 代理运行 Claude Code | `claude` |
| `mycd` | Codex 命令行封装 | `codex` |

这些命令需要访问各自模型服务，所以不直接放进 `--network none` 的 Docker 智能体容器里跑。实际测试时使用 `runs/<run-id>/<task>/workspace` 作为干净工作目录，让智能体只能按提示使用 `../task` 和当前目录。

不要从仓库根目录启动智能体。否则智能体可能看到 `docs/`、原始 GEO 下载、本地隐藏答案或 git 历史。

## 已预创建的运行目录

bulk 任务：

```text
runs/ccsds_bulk_001/geo_bulk_alms1_ko/
runs/ccskm_bulk_001/geo_bulk_alms1_ko/
runs/vvcc_bulk_001/geo_bulk_alms1_ko/
runs/mycd_bulk_001/geo_bulk_alms1_ko/
```

scRNA 任务：

```text
runs/ccsds_scrna_001/geo_scrna_nec_inflammation/
runs/ccskm_scrna_001/geo_scrna_nec_inflammation/
runs/vvcc_scrna_001/geo_scrna_nec_inflammation/
runs/mycd_scrna_001/geo_scrna_nec_inflammation/
```

每个运行目录下都有：

```text
task/
workspace/
```

`task/` 是只读任务包，包含：

```text
prompt.md
expected_output.schema.json
public_notes.md
data/
```

`workspace/` 是智能体输出目录。正式运行的 `workspace/` 初始为空。

## 重新创建运行目录

如果要重新生成某个运行目录，使用：

```bash
cd /data2/zcwang/homeworks/bio-agent-bench

scripts/run_task_container.sh \
  --task geo_bulk_alms1_ko \
  --run-id ccsds_bulk_001 \
  --command "true"
```

scRNA：

```bash
scripts/run_task_container.sh \
  --task geo_scrna_nec_inflammation \
  --run-id ccsds_scrna_001 \
  --command "true"
```

注意：这个命令会重建该运行的 `task/` 任务包；`workspace/` 目录会保留，应手动确认是否需要清空旧输出。

## 建议运行矩阵

```bash
# bulk 任务
scripts/run_task_container.sh --task geo_bulk_alms1_ko --run-id ccsds_bulk_001 --command "true"
scripts/run_task_container.sh --task geo_bulk_alms1_ko --run-id ccskm_bulk_001 --command "true"
scripts/run_task_container.sh --task geo_bulk_alms1_ko --run-id vvcc_bulk_001 --command "true"
scripts/run_task_container.sh --task geo_bulk_alms1_ko --run-id mycd_bulk_001 --command "true"

# scRNA 任务
scripts/run_task_container.sh --task geo_scrna_nec_inflammation --run-id ccsds_scrna_001 --command "true"
scripts/run_task_container.sh --task geo_scrna_nec_inflammation --run-id ccskm_scrna_001 --command "true"
scripts/run_task_container.sh --task geo_scrna_nec_inflammation --run-id vvcc_scrna_001 --command "true"
scripts/run_task_container.sh --task geo_scrna_nec_inflammation --run-id mycd_scrna_001 --command "true"
```

然后分别进入每个 `workspace/` 启动对应智能体。

## 任务列表

### `geo_bulk_alms1_ko`

数据来自 GEO 系列 GSE209844 的已处理 bulk RNA-seq 文件。任务包中样本标签已盲化。

输入文件：

- `counts.tsv`：原始计数矩阵，基因 × 盲化样本。
- `rlog.tsv`：DESeq2 rlog 归一化表达矩阵。
- `sample_sheet.tsv`：盲化样本组和重复编号。
- `gene_annotations.tsv`：Ensembl 基因 ID 和基因符号。

问题：

> 两个盲化组中，一个是 ALMS1 敲除组，一个是野生型组。判断哪个 `blinded_group` 是 ALMS1 敲除组。

期望智能体行为：

- 用终端读取表达矩阵和元数据。
- 写分析脚本。
- 比较 ALMS1 表达或组间差异。
- 生成至少一个 QC/统计结果文件。
- 输出符合 JSON 结构约束的 `submission.json`。

### `geo_scrna_nec_inflammation`

数据来自 GEO 系列 GSE178088 的已处理 `.h5ad` 文件。原始样本和队列名称已盲化。

输入文件：

- `adata.h5ad`：单细胞表达对象。
- `metadata.tsv`：从 `adata.obs` 导出的细胞级元数据。
- `sample_sheet.tsv`：盲化样本的细胞数汇总。
- `gene_annotations.tsv`：基因符号。

问题：

> 哪个盲化队列表现出最强的炎症相关异常？

期望智能体行为：

- 用 `anndata` 或等价方法读取 `.h5ad`。
- 按 `blinded_cohort` 汇总 QC 和标记基因表达。
- 使用炎症标记基因，例如 `IL1B`、`CXCL8`、`S100A8`、`S100A9`、`TREM1`。
- 生成至少一个 QC/统计结果文件。
- 输出符合 JSON 结构约束的 `submission.json`。

## 提交格式

智能体必须写出一个 JSON 对象，文件名为：

```text
submission.json
```

顶层字段固定为：

- `task_id`
- `answer`
- `confidence`
- `evidence`
- `artifacts`
- `commands_summary`

每个任务的完整 JSON 结构约束在：

```text
tasks/<task_id>/expected_output.schema.json
```

## 评分方法

评分是程序化隐藏答案评分，不使用 LLM 裁判。

默认总分 100：

- `answer`：50 分
  - `anomaly_type` 正确：25 分
  - `anomalous_group` 正确：25 分
- `evidence`：20 分
  - `evidence` 条目数量和 `key_statistics` 数值统计量。
- `artifacts`：15 分
  - 检查 `submission.json` 中列出的结果文件是否真实存在且非空。
- `process`：15 分
  - 检查 `commands_summary` 和可选过程日志中是否有实际分析痕迹。

评分脚本：

```bash
scripts/score_run_container.sh \
  --task geo_bulk_alms1_ko \
  --run-id ccsds_bulk_001
```

直接调用评分器也可以：

```bash
python scripts/score_submission.py \
  --task-root tasks/geo_bulk_alms1_ko/data/public_geo \
  --submission examples/baseline_outputs/geo_bulk/submission.json \
  --answer .hidden/geo_answers/geo_bulk_alms1_ko_answer.hidden.json
```

隐藏答案位于 `.hidden/geo_answers/`，不会提交到 GitHub，也不会挂载给智能体。

## 可选：记录过程日志

如果终端支持，可以用 `script` 记录交互过程：

```bash
cd runs/ccsds_bulk_001/geo_bulk_alms1_ko/workspace
script -q -f process.log -c "ccsds"
```

评分时传入过程日志：

```bash
cd /data2/zcwang/homeworks/bio-agent-bench

scripts/score_run_container.sh \
  --task geo_bulk_alms1_ko \
  --run-id ccsds_bulk_001 \
  --process-log runs/ccsds_bulk_001/geo_bulk_alms1_ko/workspace/process.log
```

## Docker 沙箱

构建智能体和评分器镜像：

```bash
scripts/build_docker_images.sh
```

生成闭卷任务包：

```bash
scripts/run_task_container.sh \
  --task geo_bulk_alms1_ko \
  --run-id model_a_bulk \
  --command "true"
```

如果只想进入 Docker 智能体沙箱：

```bash
scripts/run_task_container.sh \
  --task geo_bulk_alms1_ko \
  --run-id model_a_bulk
```

评分：

```bash
scripts/score_run_container.sh \
  --task geo_bulk_alms1_ko \
  --run-id model_a_bulk
```

规范配置在：

```text
benchmark.yaml
docs/sandbox.md
```

## 安装本地 Python 环境

建议使用隔离环境。某些 conda base 环境可能有 NumPy ABI 混用问题。

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
python -m pip install -e ".[dev]"
```

运行测试：

```bash
.venv/bin/python -m pytest
```

## 准备 GEO 数据

仓库已经提交了处理后的盲化公开任务数据。只有在你要从原始 GEO 补充文件重新生成任务包时，才需要执行本节。

下载原始 GEO 补充文件到 `data/raw_geo/`：

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

重新生成盲化任务数据和本地隐藏答案：

```bash
python scripts/prepare_geo_tasks.py
```

`data/raw_geo/` 和 `.hidden/` 都被 gitignore，不会提交。

## 重要对比规则

- 每个模型和任务使用一个新的 `--run-id`。
- 不要从仓库根目录启动智能体。
- 不要把 `.hidden/`、`data/raw_geo/`、`docs/data_sources.md` 提供给智能体。
- 不要把闭卷运行和开放世界运行混在同一张分数表里。
- 所有被比较的智能体应使用同一份任务包、同一套超时策略、同一个评分脚本提交版本和同一个隐藏答案文件。
- 智能体可以访问自己的模型服务，但不应该浏览外部数据源。
- 如果要测允许联网检索的开放世界智能体，应单独建立排行榜。
