你正在一个闭卷生物信息学评测工作目录中工作。

请先阅读 ../task/prompt.md。只能使用 ../task 下的文件和当前工作目录。
不要查看仓库根目录、docs、.hidden、data/raw_geo、git 历史，也不要使用互联网。

任务目标
- `RHYTHMIC.txt` 是一个去卷积后的表达时间序列文件，第一行为采样点（ZT0 到 ZT44，间隔 4h），每行一个基因表达轨迹（如 `GENE32`,`GENE15` ...）。
- 任务是找出哪一个基因显示出最强的 **24 小时节律（接近 24h 周期）**，给出该基因名。

必须产出
1. `submission.json`，并符合 `../task/expected_output.schema.json`
2. 至少一个可运行的分析脚本
3. 至少一个非空的图或表结果文件，并在 `submission.json` 的 `artifacts` 中列出

评分口径要求
- `answer.anomaly_type` 建议填写 `rhythmic_gene`。
- `answer.anomalous_group` 填写你判断出的目标基因名（如 `GENE15`）。

建议流程
- 对每个基因在时间轴上拟合正弦函数（可用 period=24h），或用谐波相关度/相关系数做排序。
- 输出每个基因的周期性得分表和前 10 候选基因的可视化。

请在 `submission.json` 的 `commands_summary` 中列出你的关键命令/分析步骤。最后再次检查：
- `submission.json` 存在
- 所有在 `submission.json.artifacts[].path` 中声明的文件真实存在且非空
