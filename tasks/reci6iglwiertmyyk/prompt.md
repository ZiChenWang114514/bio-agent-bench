你正在一个闭卷生物信息学评测工作目录中工作。

请先阅读 ../task/prompt.md。只能使用 ../task 下的文件和当前工作目录。
不要查看仓库根目录、docs、.hidden、data/raw_geo、git 历史，也不要使用互联网。

任务目标
- 这是一个 RNA-seq 表达矩阵脱敏任务。`matrixTpm_anonymized.tsv` 含 32 个匿名样本（Sample1~Sample32）与 59,526 个基因的 TPM 表达。
- 实验为 32 条 siRNA 样本的单基因敲低筛选。
- 你需要判断哪一个 `Sample` 是被敲低样本（Knockdown 样本）。

必须产出
1. `submission.json`，并符合 `../task/expected_output.schema.json`
2. 至少一个可运行的分析脚本
3. 至少一个非空的图或表结果文件，并在 `submission.json` 的 `artifacts` 中列出

评分口径要求
- `answer.anomaly_type` 建议填写 `knockdown_sample`。
- `answer.anomalous_group` 填写你判断出的样本编号（如 Sample25）。

请在 `submission.json` 的 `commands_summary` 中列出你的关键命令/分析步骤。最后再次检查：
- `submission.json` 存在
- 所有在 `submission.json.artifacts[].path` 中声明的文件真实存在且非空
