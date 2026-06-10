# bio-agent-bench

一个面向真实公开组学数据的闭卷智能体评测仓库。目标：让模型在只读任务包中读取数据、写脚本、产出可复核结果，再输出统一 `submission.json`。

本仓库公开；原始 GEO 下载、隐藏答案与 evaluator 数据在 `.gitignore` 排除的目录里（例如 `.hidden/`）。

## 最直接的测试方法（已更新为 3 个 BioMysteryBench 衍生任务）

### 当前状态

✅ 任务和运行目录已就绪：可直接开始测试。任务清单与 `benchmark.yaml` 已对齐。

### 推荐：先执行完整预检查

```bash
cd /data2/zcwang/homeworks/bio-agent-bench

# 1) 检查关键目录
test -d runs/ccsds_reci_001/reci6iglwiertmyyk/workspace && echo OK
test -d runs/ccskm_recy_001/recyolnajpygz2xeo/workspace && echo OK
test -d runs/vvcc_rec4k_001/rec4kcr3oroe3jc1j/workspace && echo OK

# 2) 检查任务包
test -f tasks/reci6iglwiertmyyk/prompt.md && echo OK
test -f tasks/recyolnajpygz2xeo/prompt.md && echo OK
test -f tasks/rec4kcr3oroe3jc1j/prompt.md && echo OK
```

任一命令报错则先修复对应目录/任务，再开始大规模测试。

### 1) 进入运行目录并启动模型（示例）

```bash
# ccsds
cd /data2/zcwang/homeworks/bio-agent-bench/runs/ccsds_reci_001/reci6iglwiertmyyk/workspace && ccsds
cd /data2/zcwang/homeworks/bio-agent-bench/runs/ccsds_recy_001/recyolnajpygz2xeo/workspace && ccsds
cd /data2/zcwang/homeworks/bio-agent-bench/runs/ccsds_rec4k_001/rec4kcr3oroe3jc1j/workspace && ccsds

# ccskm
cd /data2/zcwang/homeworks/bio-agent-bench/runs/ccskm_reci_001/reci6iglwiertmyyk/workspace && ccskm
cd /data2/zcwang/homeworks/bio-agent-bench/runs/ccskm_recy_001/recyolnajpygz2xeo/workspace && ccskm
cd /data2/zcwang/homeworks/bio-agent-bench/runs/ccskm_rec4k_001/rec4kcr3oroe3jc1j/workspace && ccskm

# vvcc
cd /data2/zcwang/homeworks/bio-agent-bench/runs/vvcc_reci_001/reci6iglwiertmyyk/workspace && vvcc
cd /data2/zcwang/homeworks/bio-agent-bench/runs/vvcc_recy_001/recyolnajpygz2xeo/workspace && vvcc
cd /data2/zcwang/homeworks/bio-agent-bench/runs/vvcc_rec4k_001/rec4kcr3oroe3jc1j/workspace && vvcc

# mycd
cd /data2/zcwang/homeworks/bio-agent-bench/runs/mycd_reci_001/reci6iglwiertmyyk/workspace && mycd
cd /data2/zcwang/homeworks/bio-agent-bench/runs/mycd_recy_001/recyolnajpygz2xeo/workspace && mycd
cd /data2/zcwang/homeworks/bio-agent-bench/runs/mycd_rec4k_001/rec4kcr3oroe3jc1j/workspace && mycd

# codex（如你的环境有对应 run-id，可用 codex 启动）
cd /data2/zcwang/homeworks/bio-agent-bench/runs/codex_reci_001/reci6iglwiertmyyk/workspace && codex
cd /data2/zcwang/homeworks/bio-agent-bench/runs/codex_recy_001/recyolnajpygz2xeo/workspace && codex
cd /data2/zcwang/homeworks/bio-agent-bench/runs/codex_rec4k_001/rec4kcr3oroe3jc1j/workspace && codex
```

> 说明：`codex` 为可选入口；如未有 `runs/codex_*` 目录，需先按任务重新创建再使用。

> 提示：启动前请确认你在对应 `runs/<agent>_<taskid>_<ver>/.../workspace`，不要从仓库根目录启动。

### 2) 通用提示词（每个任务都可复用）

```text
你正在一个闭卷生物信息学评测工作目录中工作。

请先阅读 ../task/prompt.md。只能使用 ../task 下的文件和当前工作目录。不要查看仓库根目录、docs、.hidden、data/raw_geo、git 历史，也不要使用互联网。

你必须创建：
1. submission.json，并符合 ../task/expected_output.schema.json
2. 至少一个可运行的分析脚本
3. 至少一个非空的图或表结果文件，并在 submission.json 中列出

结束前请验证 submission.json 存在，并且 submission.json 中列出的每个结果文件路径都真实存在。
```

### 3) 立刻评分（同一台机器可复用）

```bash
cd /data2/zcwang/homeworks/bio-agent-bench

scripts/score_run_container.sh --task reci6iglwiertmyyk --run-id ccsds_reci_001
scripts/score_run_container.sh --task recyolnajpygz2xeo --run-id ccskm_recy_001
scripts/score_run_container.sh --task rec4kcr3oroe3jc1j --run-id vvcc_rec4k_001

cat runs/ccsds_reci_001/reci6iglwiertmyyk/workspace/score.json
cat runs/ccskm_recy_001/recyolnajpygz2xeo/workspace/score.json
cat runs/vvcc_rec4k_001/rec4kcr3oroe3jc1j/workspace/score.json
```

### 4) 批量评分（推荐脚本）

```bash
cd /data2/zcwang/homeworks/bio-agent-bench

for run_id in \
  ccsds_reci_001 ccsds_recy_001 ccsds_rec4k_001 \
  ccskm_reci_001 ccskm_recy_001 ccskm_rec4k_001 \
  vvcc_reci_001 vvcc_recy_001 vvcc_rec4k_001 \
  mycd_reci_001 mycd_recy_001 mycd_rec4k_001 \
  codex_reci_001 codex_recy_001 codex_rec4k_001; do

  case "$run_id" in
    ccsds_reci_001|ccskm_reci_001|vvcc_reci_001|mycd_reci_001)
      task=reci6iglwiertmyyk
      subdir=$run_id/reci6iglwiertmyyk
      ;;
    ccsds_recy_001|ccskm_recy_001|vvcc_recy_001|mycd_recy_001)
      task=recyolnajpygz2xeo
      subdir=$run_id/recyolnajpygz2xeo
      ;;
    ccsds_rec4k_001|ccskm_rec4k_001|vvcc_rec4k_001|mycd_rec4k_001)
      task=rec4kcr3oroe3jc1j
      subdir=$run_id/rec4kcr3oroe3jc1j
      ;;
  esac

  if [ -d "runs/$subdir/workspace" ]; then
    scripts/score_run_container.sh --task "$task" --run-id "$run_id"
    echo "--- ${run_id} score ---"
    cat runs/$subdir/workspace/score.json
  else
    echo "skip ${run_id}: workspace missing"
  fi
done
```

```bash
cd /data2/zcwang/homeworks/bio-agent-bench

scripts/score_run_container.sh \
  --task reci6iglwiertmyyk \
  --run-id ccsds_reci_001

cat runs/ccsds_reci_001/reci6iglwiertmyyk/workspace/score.json
```

（同理可替换为 `recyolnajpygz2xeo`、`rec4kcr3oroe3jc1j`）

## 运行目录约定

本次主线已预创建 12 个 `workspace` 目录（4 个模型 × 3 个任务）：

- `runs/ccsds_reci_001/reci6iglwiertmyyk/`
- `runs/ccskm_reci_001/reci6iglwiertmyyk/`
- `runs/vvcc_reci_001/reci6iglwiertmyyk/`
- `runs/mycd_reci_001/reci6iglwiertmyyk/`

- `runs/ccsds_recy_001/recyolnajpygz2xeo/`
- `runs/ccskm_recy_001/recyolnajpygz2xeo/`
- `runs/vvcc_recy_001/recyolnajpygz2xeo/`
- `runs/mycd_recy_001/recyolnajpygz2xeo/`

- `runs/ccsds_rec4k_001/rec4kcr3oroe3jc1j/`
- `runs/ccskm_rec4k_001/rec4kcr3oroe3jc1j/`
- `runs/vvcc_rec4k_001/rec4kcr3oroe3jc1j/`
- `runs/mycd_rec4k_001/rec4kcr3oroe3jc1j/`

每个目录包含：

```text
task/
workspace/
```

`task/` 为只读输入包；`workspace/` 用于输出。

### 重新创建某个运行目录

```bash
scripts/run_task_container.sh --task reci6iglwiertmyyk --run-id ccsds_reci_001 --command "true"
scripts/run_task_container.sh --task recyolnajpygz2xeo --run-id ccsds_recy_001 --command "true"
scripts/run_task_container.sh --task rec4kcr3oroe3jc1j --run-id ccsds_rec4k_001 --command "true"
```

## 本机智能体命令

| 命令 | 用途 |
|---|---|
| `ccsds` | DeepSeek（当前绑定） |
| `ccskm` | Kimi/Moonshot |
| `vvcc` | 本地 VVCC |
| `mycd` | Codex |
| `codex` | OpenAI Codex |

## 任务清单（当前主线）

### `reci6iglwiertmyyk`

- 数据：`tasks/reci6iglwiertmyyk/data/public_geo/matrixTpm_anonymized.tsv`
- 类型：RNA-seq 敲低样本识别
- 目标：识别哪一个 sample 是 32 个敲低样本中的目标样本（仅可从数据中推断）

### `recyolnajpygz2xeo`

- 数据：`tasks/recyolnajpygz2xeo/data/public_geo/sample*.bed`
- 类型：ChIP-seq 峰文件归因
- 目标：识别 30 个匿名峰集里哪一个属于转录因子（TF）ChIP

### `rec4kcr3oroe3jc1j`

- 数据：`tasks/rec4kcr3oroe3jc1j/data/public_geo/RHYTHMIC.txt`
- 类型：周期性基因识别
- 目标：识别 24h 周期性最强的基因

> 说明：仓库还保留了原始的 GEO 课程任务文件（`geo_bulk_alms1_ko`, `geo_scrna_nec_inflammation`）用于兼容性参考；当前 `benchmark.yaml` 任务入口已切到上面三条。

## 提交格式

`submission.json` 顶层至少包含：

- `task_id`
- `answer`（含 `anomaly_type`, `anomalous_group`, `rationale`）
- `confidence`
- `evidence`
- `artifacts`
- `commands_summary`

结构定义见各任务目录下 `expected_output.schema.json`。

## 评分

默认总分 100（见 `src/bio_agent_bench/score.py`）：

- `answer`（50）
- `evidence`（20）
- `artifacts`（15）
- `process`（15）

```bash
scripts/score_run_container.sh --task reci6iglwiertmyyk --run-id ccsds_reci_001
```

带过程日志时可加 `--process-log`。

## 评测入口（示例）

```bash
scripts/run_task_container.sh --task reci6iglwiertmyyk --run-id model_a --command "true"
scripts/run_task_container.sh --task recyolnajpygz2xeo --run-id model_b --command "true"
scripts/run_task_container.sh --task rec4kcr3oroe3jc1j --run-id model_c --command "true"
```

## BioMysteryBench 参考与扩展

- `docs/biomysterybench_full_task_guide_cn.md`：99 题题面与评分提示（基于 `/data3/zcwang/biomysterybench/full/problems.csv`）。
- 若要对任务集继续扩容，可继续从 `problems.csv` 按现有 task 模板新增。

## Docker

```bash
scripts/build_docker_images.sh
scripts/run_task_container.sh --task reci6iglwiertmyyk --run-id model_a
scripts/score_run_container.sh --task reci6iglwiertmyyk --run-id model_a
```
