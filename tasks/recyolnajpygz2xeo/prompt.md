你正在一个闭卷生物信息学评测工作目录中工作。

请先阅读 ../task/prompt.md。只能使用 ../task 下的文件和当前工作目录。
不要查看仓库根目录、docs、.hidden、data/raw_geo、git 历史，也不要使用互联网。

任务目标
- 你将收到 30 个匿名化的 BED 峰文件（`sample1.bed` ... `sample30.bed`）。
- 每个文件对应一次 ChIP 实验（TF 或组蛋白修饰），基因组为 hg19。
- 需要判断哪一个文件来自转录因子（TF）ChIP-seq 的实验。

必须产出
1. `submission.json`，并符合 `../task/expected_output.schema.json`
2. 至少一个可运行的分析脚本
3. 至少一个非空的图或表结果文件，并在 `submission.json` 的 `artifacts` 中列出

评分口径要求
- `answer.anomaly_type` 建议填写 `tf_chip`。
- `answer.anomalous_group` 填写你判断出的样本文件名（如 `Sample4.bed`）。

可选分析方向（任选）
- 统计每个样本的峰长度分布、峰位置信息、峰数量。
- 计算 `sample#.bed` 与 TSS 附近峰比例（需自己用 gene annotation 或自定义规则）。
- 结合 TF 结合常见峰形特征与组蛋白修饰峰特征区分。

请在 `submission.json` 的 `commands_summary` 中列出你的关键命令/分析步骤。最后再次检查：
- `submission.json` 存在
- 所有在 `submission.json.artifacts[].path` 中声明的文件真实存在且非空
