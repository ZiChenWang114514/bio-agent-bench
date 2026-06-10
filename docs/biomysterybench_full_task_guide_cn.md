# BioMysteryBench-full 任务手册（agent 测试）

> 版本：BIO-MB Full 99 题（本地下载于 /data3/zcwang/biomysterybench/full）

## 用法说明
- 该文档用于把 `problems.csv` 的每个任务转成可直接分配给智能体的执行说明。
- 每个任务在下文都保留原始问题与评分规则要点，避免误用题号外推标签。
- 任务包文件位于：`/data3/zcwang/biomysterybench/full/extracted/<task_id>/`，对应 `data/<id>.zip`。

## 全局元信息
- 任务总数：99
- `human_solvable=yes`：76，`human_solvable=no`：23
- 评分规则：全局 99/99 任务包含 `all or nothing credit` 的有 96 条，`95%` 容错项有 3 条（其余按严格命中/文本标准）。
- 允许联网域名：统一为 `conda/anaconda`、`ncbi`、`ensembl`、`ucsc`、`ebi` 等公共数据库域，详见 `problems.csv` 的 `allowed_domains` 列。

## 快速分组索引
| 任务类型 | 数量 |
|---|---:|
| 样本标签识别 | 18 |
| 组织/来源推断 | 17 |
| 微生物/宏基因组来源判定 | 10 |
| 基因缺失/敲除/靶基因定位 | 9 |
| 遗传变异/结构变异判定 | 8 |
| 测序实验元数据提取 | 7 |
| 参考基因组或比对参数推断 | 6 |
| 亲本/家系关系推断 | 6 |
| 扩增子引物/marker 区域识别 | 5 |
| 疾病/表型判定 | 4 |
| 多模态生信推断 | 3 |
| 样本性别推断 | 3 |
| 分群/群体/标签聚类 | 2 |
| 基因表达/基因识别 | 1 |

## hb001
- **任务类型**：组织/来源推断
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/hb001.zip` -> `extracted/hb001/`
- **可读文件（Top-level）**：cells.tsv.gz, counts.mtx.gz, genes.tsv.gz
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> Which human organ is this cell type single-cell RNA-seq dataset derived from?

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 输出为单项答案（词名/符号/ID），仍建议做大小写和同义名归一化。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## hb002
- **任务类型**：微生物/宏基因组来源判定
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/hb002.zip` -> `extracted/hb002/`
- **可读文件（Top-level）**：anonymized_genome_1_.fasta
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> What bacteria is found in this sequenced dataset? Provide the bacteria's scientific name as the answer.

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 输出为单项答案（词名/符号/ID），仍建议做大小写和同义名归一化。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## hb003
- **任务类型**：基因缺失/敲除/靶基因定位
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/hb003.zip` -> `extracted/hb003/`
- **可读文件（Top-level）**：gene_info.gz, norm_counts_TPM.tsv, raw_counts.tsv
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> Name one gene that was knocked out in the experimental sample compared to the control samples. Provide the
gene symbol.

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 回答有显式格式要求，按题目中的示例逐字段输出。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## hb004
- **任务类型**：微生物/宏基因组来源判定
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/hb004.zip` -> `extracted/hb004/`
- **可读文件（Top-level）**：reads_1.fastq, reads_2.fastq
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> Which eukaryotic host organism was this metagenomic sample taken from? Provide the scientific species name
(e.g., Homo sapiens).

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 输出为单项答案（词名/符号/ID），仍建议做大小写和同义名归一化。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## hb006
- **任务类型**：疾病/表型判定
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/hb006.zip` -> `extracted/hb006/`
- **可读文件（Top-level）**：data2.csv, processed_disease_data.csv
- **任务标签**：human_solvable = no（建议在成绩分层里作为难度指标）

### 任务题面
> In this human intestinal biopsy RNA-seq dataset generated using Illumina HiSeq 2000 platform with strand-
specific mRNA library preparation, which samples were collected from patients diagnosed with ulcerative
colitis? Provide your answer as a list of sample identifiers (e.g., sample_1, sample_2, etc.).

### 评分规则（要点）
- 需达到 95% 及以上正确率判为正确（否则为 0 分）；无部分分。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 回答有显式格式要求，按题目中的示例逐字段输出。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 此题目为公开评测中人工未解题，优先记录关键特征（如 QC、主成分、聚类、富集项）后再给出最可能答案。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## hb008
- **任务类型**：参考基因组或比对参数推断
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/hb008.zip` -> `extracted/hb008/`
- **可读文件（Top-level）**：archive.tar.gz.part-aa, archive.tar.gz.part-ab, archive.tar.gz.part-ac, archive.tar.gz.part-ad, archive.tar.gz.part-ae, archive.tar.gz.part-af
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> What mouse reference genome were the RNA-seq reads aligned to? Provide the genome assembly name (e.g., UCSC-
style name such as mm10 or GRC name such as GRCm38).

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 输出为单项答案（词名/符号/ID），仍建议做大小写和同义名归一化。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## hb009
- **任务类型**：疾病/表型判定
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/hb009.zip` -> `extracted/hb009/`
- **可读文件（Top-level）**：counts_tpm-2019-12-06.csv
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> What genetic disease does Sample_02 have? Provide the common name of the genetic disease.

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 输出为单项答案（词名/符号/ID），仍建议做大小写和同义名归一化。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## hb010
- **任务类型**：扩增子引物/marker 区域识别
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/hb010.zip` -> `extracted/hb010/`
- **可读文件（Top-level）**：hb010-sequences.fasta
- **任务标签**：human_solvable = no（建议在成绩分层里作为难度指标）

### 任务题面
> What amplicon sequencing primer(s) was/were used to characterize the microbial community of this dataset? List
the target marker gene region(s) (e.g., 16S, 18S, ITS) used for amplicon sequencing.

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 回答有显式格式要求，按题目中的示例逐字段输出。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 此题目为公开评测中人工未解题，优先记录关键特征（如 QC、主成分、聚类、富集项）后再给出最可能答案。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## hb011
- **任务类型**：测序实验元数据提取
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/hb011.zip` -> `extracted/hb011/`
- **可读文件（Top-level）**：hb011.zip
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> This human RNA‑seq dataset has an unknown sequencing setup. Using only the raw FASTQ file(s), determine: the
read length (in base pairs) whether the data are single-end or paired-end the sequencing depth (number of
reads, or read pairs if paired-end)Provide your answer in the following format (exactly): read length (integer
in bp), configuration (e.g. single) and depth (in millions, rounded to 2 decimal places, e.g. 15.50M). If
paired end configuration provide the two read lengths as follow R1(READ LENGHT bp)/R2 (READ LENGHT bp). Format
your answer exactly as: 'R1 (XXXbp)/R2 (XXXbp), paired, XX.XXM' for paired-end or 'XXX bp, single, XX.XXM' for
single-end.

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 回答有显式格式要求，按题目中的示例逐字段输出。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## hb012
- **任务类型**：亲本/家系关系推断
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/hb012.zip` -> `extracted/hb012/`
- **可读文件（Top-level）**：Sample_01.vcf.gz, Sample_01.vcf.gz.tbi, Sample_02.vcf.gz, Sample_02.vcf.gz.tbi, Sample_03.vcf.gz, Sample_03.vcf.gz.tbi, Sample_04.vcf.gz, Sample_04.vcf.gz.tbi, Sample_05.vcf.gz, Sample_05.vcf.gz.tbi, Sample_06.vcf.gz, Sample_06.vcf.gz.tbi, Sample_07.vcf.gz, Sample_07.vcf.gz.tbi, Sample_08.vcf.gz, Sample_08.vcf.gz.tbi, Sample_09.vcf.gz, Sample_09.vcf.gz.tbi, Sample_10.vcf.gz, Sample_10.vcf.gz.tbi
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> What sample is the mother of sample X? What sample is the father? Answer should be comma separated: mother
comes first, father comes second.

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 输出为单项答案（词名/符号/ID），仍建议做大小写和同义名归一化。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## hb013
- **任务类型**：样本标签识别
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/hb013.zip` -> `extracted/hb013/`
- **可读文件（Top-level）**：Dataset1.csv
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> Using HGVS nomenclature, what is the name of the human gene being evaluated in this data set? Provide the
official gene symbol.

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 输出为单项答案（词名/符号/ID），仍建议做大小写和同义名归一化。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## hb014
- **任务类型**：分群/群体/标签聚类
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/hb014.zip` -> `extracted/hb014/`
- **可读文件（Top-level）**：read_1.fastq.gz, read_2.fastq.gz, reference_anonymized.fasta
- **任务标签**：human_solvable = no（建议在成绩分层里作为难度指标）

### 任务题面
> What is the mitochondrial haplogroup of this patient/sample?

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 输出为单项答案（词名/符号/ID），仍建议做大小写和同义名归一化。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 此题目为公开评测中人工未解题，优先记录关键特征（如 QC、主成分、聚类、富集项）后再给出最可能答案。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## hb015
- **任务类型**：多模态生信推断
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/hb015.zip` -> `extracted/hb015/`
- **可读文件（Top-level）**：cleaned_genotypes.vcf.gz
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> Which sample is SAMPLE_02's offspring?

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 输出为单项答案（词名/符号/ID），仍建议做大小写和同义名归一化。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## hb016
- **任务类型**：扩增子引物/marker 区域识别
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/hb016.zip` -> `extracted/hb016/`
- **可读文件（Top-level）**：butterfly_data.csv
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> In this Bicyclus anynana (butterfly) RNA-seq dataset, samples were collected across five distinct
developmental time points. To verify the developmental chronology, order the stages from earliest to latest.
For each stage, group together the sample IDs of all biological replicates.  Format your answer as a list
where each line contains the developmental stage name followed by its replicate sample IDs in square brackets
(Stage_0: [Sample_01, Sample_02] Stage_1: [Sample_03, Sample_04, Sample_05])

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 回答有显式格式要求，按题目中的示例逐字段输出。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## hb017
- **任务类型**：测序实验元数据提取
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/hb017.zip` -> `extracted/hb017/`
- **可读文件（Top-level）**：cleaned_counts.csv
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> This RNA-sequencing dataset contains gene expression profiles from mouse tibial muscle collected across
multiple timepoints after injury. Each sample has been anonymized and assigned to one of two genetic groups:
Group_1 and Group_2. One group represents Wild-Type (WT) mice, and the other represents a transgenic NSE-BMP4
mouse model. Which samples belong to the transgenic mouse model group? Format your answer as a list of sample
IDs in square brackets (e.g., [Sample_01, Sample_02, Sample_17]).

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 回答有显式格式要求，按题目中的示例逐字段输出。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## hb018
- **任务类型**：参考基因组或比对参数推断
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/hb018.zip` -> `extracted/hb018/`
- **可读文件（Top-level）**：archive.tar.gz.part-aa, archive.tar.gz.part-ab, archive.tar.gz.part-ac, archive.tar.gz.part-ad, archive.tar.gz.part-ae, archive.tar.gz.part-af
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> What mouse reference genome were the RNA-seq reads aligned to? Provide the reference genome name using the
UCSC-style identifier (e.g., mm9, mm10).

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 输出为单项答案（词名/符号/ID），仍建议做大小写和同义名归一化。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## hb019
- **任务类型**：样本标签识别
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/hb019.zip` -> `extracted/hb019/`
- **可读文件（Top-level）**：hb019_subsampled_data.fastq
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> What viral species is the human patient infected with? Provide the answer using ICTV viral abbreviations (e.g.
ZIKV, YFV, HCV, etc).

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 输出为单项答案（词名/符号/ID），仍建议做大小写和同义名归一化。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## hb020
- **任务类型**：组织/来源推断
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/hb020.zip` -> `extracted/hb020/`
- **可读文件（Top-level）**：data_scrubbed.cif
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> What organism does this crystal structure belong to? Provide the answer using binomial nomenclature (e.g.
Canis lupus, Mus musculus, Danio rerio, etc).

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 输出为单项答案（词名/符号/ID），仍建议做大小写和同义名归一化。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## hb021
- **任务类型**：扩增子引物/marker 区域识别
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/hb021.zip` -> `extracted/hb021/`
- **可读文件（Top-level）**：processed_methylation_matrix.csv
- **任务标签**：human_solvable = no（建议在成绩分层里作为难度指标）

### 任务题面
> This human dataset contains DNA methylation profiles generated using the Illumina 450k array across multiple
tissues. Each tissue exhibits a distinct, tissue-specific methylation signature. Based on these patterns,
determine which internal organ the following anonymized sample IDs belong to (replicates): Sample IDs:
[Sample_01, Sample_02, Sample_03, Sample_04]. Provide your answer as the name of a single organ.

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 按题目文本给定的字段/单值格式返回。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 此题目为公开评测中人工未解题，优先记录关键特征（如 QC、主成分、聚类、富集项）后再给出最可能答案。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## hb022
- **任务类型**：疾病/表型判定
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/hb022.zip` -> `extracted/hb022/`
- **可读文件（Top-level）**：anonymized_expression_matrix.csv
- **任务标签**：human_solvable = no（建议在成绩分层里作为难度指标）

### 任务题面
> This dataset contains gene expression profiles from human pancreatic cancer cell lines. The samples have been
anonymized as Sample_01, Sample_02, ... and divided into two experimental conditions: Condition_X and
Condition_Y. One of these conditions represents cells treated with the drug Erastin, which is known to induce
metabolic stress. Which samples correspond to the Erastin-treated group? Format the answer as a list of sample
identifiers exactly matching those in the dataset (e.g., [Sample_01, Sample_02, ...]).

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 回答有显式格式要求，按题目中的示例逐字段输出。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 此题目为公开评测中人工未解题，优先记录关键特征（如 QC、主成分、聚类、富集项）后再给出最可能答案。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## hb023
- **任务类型**：样本标签识别
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/hb023.zip` -> `extracted/hb023/`
- **可读文件（Top-level）**：data.csv
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> From the data provided, which samples out of the total correspond to being derived from seawater and which to
sediment? Format the answer as a list of which samples (and their IDs) are seawater and which are sediment
(e.g. Seawater (#X): 1, 2,... Sediment (#Y): ...)

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 回答有显式格式要求，按题目中的示例逐字段输出。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## hb024
- **任务类型**：微生物/宏基因组来源判定
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/hb024.zip` -> `extracted/hb024/`
- **可读文件（Top-level）**：1.fasta, 10.fasta, 11.fasta, 12.fasta, 13.fasta, 14.fasta, 15.fasta, 16.fasta, 17.fasta, 18.fasta, 2.fasta, 3.fasta, 4.fasta, 5.fasta, 6.fasta, 7.fasta, 8.fasta, 9.fasta
- **任务标签**：human_solvable = no（建议在成绩分层里作为难度指标）

### 任务题面
> This dataset involves microbial communities from tissues of non-human species. How many tissue groups are
collected, and from how many different species? If possible, additionally address which host species and from
what tissues. Provide counts as integers, species as scientific names, and list tissues explicitly.

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 回答有显式格式要求，按题目中的示例逐字段输出。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 此题目为公开评测中人工未解题，优先记录关键特征（如 QC、主成分、聚类、富集项）后再给出最可能答案。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## hb025
- **任务类型**：基因缺失/敲除/靶基因定位
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/hb025.zip` -> `extracted/hb025/`
- **可读文件（Top-level）**：clone_seq.csv
- **任务标签**：human_solvable = no（建议在成绩分层里作为难度指标）

### 任务题面
> Using columns 3 and 4, which genes are the subject of single-locus modification, as indicated by a vector
where the NCBI RefSeq identifier for the 5' arm is identical to the NCBI RefSeq identifier for the 3' arm
regardless of whether the specific vector listed is a CRISPR or Targeting vector? Provide the answer as a list
of official gene symbols.

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 回答有显式格式要求，按题目中的示例逐字段输出。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 此题目为公开评测中人工未解题，优先记录关键特征（如 QC、主成分、聚类、富集项）后再给出最可能答案。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## hb026
- **任务类型**：组织/来源推断
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/hb026.zip` -> `extracted/hb026/`
- **可读文件（Top-level）**：hb026_subsampled_data.tsv
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> From this adult mouse snATAC-seq fragments file, what major organ does the sample derive from? Provide the
answer as the organ name within the set of all primary organs part of an organ system, as described by the MGI
- Adult Mouse Anatomy Browser (e.g. lung, brain, blood, liver, etc).

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 按题目文本给定的字段/单值格式返回。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## hb027
- **任务类型**：组织/来源推断
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/hb027.zip` -> `extracted/hb027/`
- **可读文件（Top-level）**：expression_matrix.tsv
- **任务标签**：human_solvable = no（建议在成绩分层里作为难度指标）

### 任务题面
> Based on the gene expression profiles in this anonymized microarray dataset derived from human ovarian tissue,
determine the number of tumor samples vs normal samples. Report the counts as 'X tumor samples and Y normal
samples' where X and Y are integers.

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 输出为单项答案（词名/符号/ID），仍建议做大小写和同义名归一化。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 此题目为公开评测中人工未解题，优先记录关键特征（如 QC、主成分、聚类、富集项）后再给出最可能答案。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## hb028
- **任务类型**：疾病/表型判定
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/hb028.zip` -> `extracted/hb028/`
- **可读文件（Top-level）**：Metabolomics_Data_Set.xlsx
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> What disease do these samples have in common? Provide the common disease name.

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 输出为单项答案（词名/符号/ID），仍建议做大小写和同义名归一化。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## hb029
- **任务类型**：样本标签识别
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/hb029.zip` -> `extracted/hb029/`
- **可读文件（Top-level）**：hb029_counts_cleaned.csv
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> Which of the hippocampus RNA-seq samples came from sleep deprived mice? List the sample names (e.g., sample1,
sample2) for the sleep deprived mice.

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 回答有显式格式要求，按题目中的示例逐字段输出。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## hb030
- **任务类型**：组织/来源推断
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/hb030.zip` -> `extracted/hb030/`
- **可读文件（Top-level）**：GeneExpression_tropicalis.txt, Xtropicalisv9.0.Named.primaryTrs.gff3, rsem_v9_counts.txt
- **任务标签**：human_solvable = no（建议在成绩分层里作为难度指标）

### 任务题面
> Which embryonic cell types are the following RNA-seq experiments from, in order of the counts file? There are
2 replicates from 5 different tissues in Xenopus tropicalis. Provide the answers as Xenopus gastrula fate-map
region names (e.g., Animal Cap, Marginal Zone, Organizer).

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 输出为单项答案（词名/符号/ID），仍建议做大小写和同义名归一化。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 此题目为公开评测中人工未解题，优先记录关键特征（如 QC、主成分、聚类、富集项）后再给出最可能答案。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## hb031
- **任务类型**：组织/来源推断
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/hb031.zip` -> `extracted/hb031/`
- **可读文件（Top-level）**：datafiles_reduced.zip
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> RNA-seq analysis of these human intestinal organoid samples (virus_rep1, virus_rep2, virus_rep3) infected with
an RNA virus shows viral reads. Which viral species infected these samples? Provide your answer as the
complete species name from NCBI Taxonomy (e.g., Hepatitis A virus, Rotavirus A, Human astrovirus)

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 按题目文本给定的字段/单值格式返回。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## hb032
- **任务类型**：遗传变异/结构变异判定
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/hb032.zip` -> `extracted/hb032/`
- **可读文件（Top-level）**：data.csv
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> What genetic abnormality does sample X have when compared to samples Y and Z? Provide the answer as the
standard name for the chromosomal abnormality (e.g., Trisomy X, Monosomy X).

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 按题目文本给定的字段/单值格式返回。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## hb033
- **任务类型**：组织/来源推断
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/hb033.zip` -> `extracted/hb033/`
- **可读文件（Top-level）**：zebrafish_TPM_anonymized.csv
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> In this zebrafish RNA-seq dataset, identify which samples come from heart tissue. Format your answer as a list
of samples, such as: Sample_1, Sample_2, etc.

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 回答有显式格式要求，按题目中的示例逐字段输出。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## hb035
- **任务类型**：亲本/家系关系推断
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/hb035.zip` -> `extracted/hb035/`
- **可读文件（Top-level）**：miRNA_data.csv
- **任务标签**：human_solvable = no（建议在成绩分层里作为难度指标）

### 任务题面
> What is the name of the most common microRNA associated with the genes given in this data? (Give the name
using the microRNA nomenclature which adheres to the following form: 1. species, 2. miRNA family and member,
and 3. strand, e.g 5’ , 3’ specific to precursor hairpin, e.g. hsa-miR-102b-3p).

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 输出为单项答案（词名/符号/ID），仍建议做大小写和同义名归一化。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 此题目为公开评测中人工未解题，优先记录关键特征（如 QC、主成分、聚类、富集项）后再给出最可能答案。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## hb036
- **任务类型**：微生物/宏基因组来源判定
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/hb036.zip` -> `extracted/hb036/`
- **可读文件（Top-level）**：hb036_dataset_reduced.fastq
- **任务标签**：human_solvable = no（建议在成绩分层里作为难度指标）

### 任务题面
> The dataset comes from a research orchard, and consists of microbial genomic samples taken from trees grown
for an experiment. When preparing the samples for analysis, some became contaminated with Agrobacterium fabrum
from another experiment. Which samples are contaminated? Provide the answer by simply listing contaminated
samples (i.e. sample_1, sample_3, etc)

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 回答有显式格式要求，按题目中的示例逐字段输出。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 此题目为公开评测中人工未解题，优先记录关键特征（如 QC、主成分、聚类、富集项）后再给出最可能答案。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## hb038
- **任务类型**：样本标签识别
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/hb038.zip` -> `extracted/hb038/`
- **可读文件（Top-level）**：hb038.zip
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> Which of the bigWig files are from ChIP samples and which are from input controls? List the bigWig file names
(e.g., sample1.bw) grouped by their type: ChIP samples and input controls.

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 回答有显式格式要求，按题目中的示例逐字段输出。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## hb039
- **任务类型**：组织/来源推断
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/hb039.zip` -> `extracted/hb039/`
- **可读文件（Top-level）**：sample_X.CEL.gz
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> Based on the gene expression signatures in Affymetrix Mouse Genome 430 2.0 (GPL1261) microarray dataset from
Mus musculus, which organ does Sample_X originate from? Provide the organ name.

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 输出为单项答案（词名/符号/ID），仍建议做大小写和同义名归一化。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## hb040
- **任务类型**：样本标签识别
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/hb040.zip` -> `extracted/hb040/`
- **可读文件（Top-level）**：anonymized_mock_vs_cornea_samples.csv
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> The dataset contains gene expression measurements for cornea samples, with six columns: three mock-infected
samples (cornea_mock_1, cornea_mock_2, cornea_mock_3) and three virus-infected samples (cornea_viral_1,
cornea_viral_2, cornea_viral_3). For each gene, expression was measured in either mock-infected or virus-
infected samples. Other than HSV-1, what virus are these samples infected with? Provide the virus name or
standard abbreviation (e.g., HIV-1, influenza A).

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 输出为单项答案（词名/符号/ID），仍建议做大小写和同义名归一化。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## hb041
- **任务类型**：样本标签识别
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/hb041.zip` -> `extracted/hb041/`
- **可读文件（Top-level）**：methylation_fold_matrix.csv
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> What fruit was this methylation dataset generated from? Provide the common name of the fruit.

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 输出为单项答案（词名/符号/ID），仍建议做大小写和同义名归一化。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## hb043
- **任务类型**：样本性别推断
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/hb043.zip` -> `extracted/hb043/`
- **可读文件（Top-level）**：alcohol.txt
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> The following dataset comes from a mixed cohort of male and female post-mortem prefrontal cortex samples.
Using genes with known differential sex expression (i.e. XIST, RPS4Y1, EIF1AY, DDX3Y, UTY), identify which
samples came from female subjects. Simply list all female samples as the asnwer (i.e. samples 1, 3, 5, 7...
etc)

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 回答有显式格式要求，按题目中的示例逐字段输出。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## hb044
- **任务类型**：参考基因组或比对参数推断
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/hb044.zip` -> `extracted/hb044/`
- **可读文件（Top-level）**：peakset1.bed, peakset2.bed, peakset3.bed, peakset4.bed
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> Which set of peaks from histone mark ChIP-seq is from H3K4me3, and which is from H3K4me1? Genome alignment is
mm10. Format answer as "peakset1:h3k4mex, peakset2:h3k4mey[...]". Label all four peaksets (peakset1 through
peakset4) in your answer.

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 回答有显式格式要求，按题目中的示例逐字段输出。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## hb045
- **任务类型**：组织/来源推断
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/hb045.zip` -> `extracted/hb045/`
- **可读文件（Top-level）**：cotton_r1, cotton_r2
- **任务标签**：human_solvable = no（建议在成绩分层里作为难度指标）

### 任务题面
> Based on the read files from this Gossypium hirsutum transcriptomics dataset, what tissue type is this data
sampled from? Provide the tissue type as a simple anatomical term (e.g., leaf, root, stem).

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 输出为单项答案（词名/符号/ID），仍建议做大小写和同义名归一化。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 此题目为公开评测中人工未解题，优先记录关键特征（如 QC、主成分、聚类、富集项）后再给出最可能答案。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## hb046
- **任务类型**：亲本/家系关系推断
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/hb046.zip` -> `extracted/hb046/`
- **可读文件（Top-level）**：archive.tar.gz.part-aa, archive.tar.gz.part-ab, archive.tar.gz.part-ac, archive.tar.gz.part-ad, archive.tar.gz.part-ae
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> Given the mass spectrometry data, identify the taxonomic family of the organism from which the data is
derived. Provide the scientific name of the taxonomic family (e.g., Muridae, Hominidae).

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 输出为单项答案（词名/符号/ID），仍建议做大小写和同义名归一化。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## hb047
- **任务类型**：遗传变异/结构变异判定
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/hb047.zip` -> `extracted/hb047/`
- **可读文件（Top-level）**：data_scrubbed.txt
- **任务标签**：human_solvable = no（建议在成绩分层里作为难度指标）

### 任务题面
> Given the ATAC-seq dataset obtained from hiPSC samples, identify the six samples that were treated with one of
two variant class I HDAC inhibitor drugs. Provide the answer as a comma separated sample list (e.g. Sample_1,
Sample_2, Sample_3, etc).

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 回答有显式格式要求，按题目中的示例逐字段输出。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 此题目为公开评测中人工未解题，优先记录关键特征（如 QC、主成分、聚类、富集项）后再给出最可能答案。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## hb048
- **任务类型**：扩增子引物/marker 区域识别
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/hb048.zip` -> `extracted/hb048/`
- **可读文件（Top-level）**：data_scrubbed.mzML
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> What parent drug was administered to this patient given the untargeted mass spectrometry data? Provide the
answer as its generic drug name.

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 按题目文本给定的字段/单值格式返回。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## hb049
- **任务类型**：微生物/宏基因组来源判定
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/hb049.zip` -> `extracted/hb049/`
- **可读文件（Top-level）**：data_1_.csv
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> From microbial data provided, identify the habitat from which these samples were collected.

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 输出为单项答案（词名/符号/ID），仍建议做大小写和同义名归一化。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## hb050
- **任务类型**：微生物/宏基因组来源判定
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/hb050.zip` -> `extracted/hb050/`
- **可读文件（Top-level）**：data.csv
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> From the microbial dataset provided, identify what human-caused pollutant(s) is/are present in this
environment based on the the core taxa. Provide the pollutant type or category, and if applicable, list
specific chemical compounds using standard chemical names or formulas.

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 回答有显式格式要求，按题目中的示例逐字段输出。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## hb052
- **任务类型**：样本性别推断
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/hb052.zip` -> `extracted/hb052/`
- **可读文件（Top-level）**：Cancers.csv, refseq_to_symbol_map.csv
- **任务标签**：human_solvable = no（建议在成绩分层里作为难度指标）

### 任务题面
> This microarray dataset contains expression data from various ovarian and pancreatic cancer biopsies ran on
GPL 887 and GPL 4133 platforms, respectively. Based on the expression profile of each sample, assign a sex
(male, female, or unknown) to each sample. The final output should be in the format of “Sample; sex” (eg
Sample 1; male)

### 评分规则（要点）
- 需达到 95% 及以上正确率判为正确（否则为 0 分）；无部分分。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 回答有显式格式要求，按题目中的示例逐字段输出。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 此题目为公开评测中人工未解题，优先记录关键特征（如 QC、主成分、聚类、富集项）后再给出最可能答案。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## hb053
- **任务类型**：测序实验元数据提取
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/hb053.zip` -> `extracted/hb053/`
- **可读文件（Top-level）**：B.distachyon_DEG_scrubbed.txt
- **任务标签**：human_solvable = no（建议在成绩分层里作为难度指标）

### 任务题面
> The transcriptome of Brachypodium distachyon was sequenced under a specific stress. Based on the sequences of
differentially expressed genes, what was the perturbation? Provide the stress type as a short descriptive
phrase (e.g., 'drought stress', 'cold stress').

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 输出为单项答案（词名/符号/ID），仍建议做大小写和同义名归一化。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 此题目为公开评测中人工未解题，优先记录关键特征（如 QC、主成分、聚类、富集项）后再给出最可能答案。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## hb054
- **任务类型**：样本标签识别
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/hb054.zip` -> `extracted/hb054/`
- **可读文件（Top-level）**：Sample_1_minus.bw, Sample_1_plus.bw, Sample_2_minus.bw, Sample_2_plus.bw, Sample_3_minus.bw, Sample_3_plus.bw
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> The following PRO-seq datasets were collected from different samples of mice cells. Some of the samples were
treated with a drug that causes the endogenous NELF-B protein to be rapidly degraded within the samples.
Identify which of the sample(s) were treated with NELF-B. Provide the answer as a comma separated list of
sample/strand identifiers, in alphanumeric order (e.g. Sample_1_minus, Sample_1_plus, etc).

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 回答有显式格式要求，按题目中的示例逐字段输出。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## rec1vycgih4bavtur
- **任务类型**：基因缺失/敲除/靶基因定位
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/rec1vycgih4bavtur.zip` -> `extracted/rec1vycgih4bavtur/`
- **可读文件（Top-level）**：read1.fastq.gz, read2.fastq.gz
- **任务标签**：human_solvable = no（建议在成绩分层里作为难度指标）

### 任务题面
> Name 1 gene on chromosome 19 that is knocked out in this mouse tumor cell line. Provide the official gene
symbol.

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 输出为单项答案（词名/符号/ID），仍建议做大小写和同义名归一化。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 此题目为公开评测中人工未解题，优先记录关键特征（如 QC、主成分、聚类、富集项）后再给出最可能答案。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## rec35farlwqz6kmy7
- **任务类型**：组织/来源推断
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/rec35farlwqz6kmy7.zip` -> `extracted/rec35farlwqz6kmy7/`
- **可读文件（Top-level）**：anonymized_pbmc_reference.rds, bulk_RNA_seq_counts.csv
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> What freshly FACS-sorted cell type of PBMC (cellType in the SingleCellExperiment object) is this bulk RNA-seq
count data most likely derived from? Provide the exact cellType label as it appears in the
SingleCellExperiment object.

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 输出为单项答案（词名/符号/ID），仍建议做大小写和同义名归一化。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## rec4kcr3oroe3jc1j
- **任务类型**：测序实验元数据提取
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/rec4kcr3oroe3jc1j.zip` -> `extracted/rec4kcr3oroe3jc1j/`
- **可读文件（Top-level）**：RHYTHMIC.txt
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> Using the provided normalized RNA-sequencing time-series data, identify which gene displays circadian
rhythmicity (24-hour periodicity). Provide your answer as the gene name exactly as it appears in the dataset
(e.g., GENE1).

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 回答有显式格式要求，按题目中的示例逐字段输出。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## rec5qx7nedrwk4zog
- **任务类型**：亲本/家系关系推断
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/rec5qx7nedrwk4zog.zip` -> `extracted/rec5qx7nedrwk4zog/`
- **可读文件（Top-level）**：cDNA_seq.fa
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> Identify the type of cDNA (complementary DNA) sequence from a whole transcriptome RNA sequencing library.
Provide the type of cDNA as a general element category name (e.g., a transposable element family or transcript
class).

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 输出为单项答案（词名/符号/ID），仍建议做大小写和同义名归一化。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## rec5xuqc70ithi19c
- **任务类型**：样本性别推断
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/rec5xuqc70ithi19c.zip` -> `extracted/rec5xuqc70ithi19c/`
- **可读文件（Top-level）**：expression_matrix.csv, sample_metadata_masked.csv
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> During sample collection for a multi-tissue gene expression study, several sample labeling errors occurred,
and specific tissue subtype labels were masked with generic identifiers(e.g. brain subsample 1,2,3). Given
RNA-seq expression profiles for samples from multiple donors, identify the masked tissue labels, and determine
the true donor and tissue identity for each sample. Report your answer as a table with columns: Sample,
Tissue, and Sex (use tissue subtype names such as 'Cortex', 'Cerebellum', etc., and Sex as 'Male' or
'Female').

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 输出为单项答案（词名/符号/ID），仍建议做大小写和同义名归一化。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## rec6urlqzwqkhmhaj
- **任务类型**：样本标签识别
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/rec6urlqzwqkhmhaj.zip` -> `extracted/rec6urlqzwqkhmhaj/`
- **可读文件（Top-level）**：read1.fastq.gz
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> This RNA-seq sample contains multiple subtypes of influenza.  Please find all of subtypes in H,N format.  For
example (H2N10)... List all subtypes as a comma-separated list in HxNx format (e.g., H1N1, H2N2).

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 回答有显式格式要求，按题目中的示例逐字段输出。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## rec6xeqyddiz6desi
- **任务类型**：基因缺失/敲除/靶基因定位
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/rec6xeqyddiz6desi.zip` -> `extracted/rec6xeqyddiz6desi/`
- **可读文件（Top-level）**：annonymize1.fastq, annonymize2.fastq
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> Identify the genomic coordinate (hg38 assembly) of the primary on-target Cas9 cleavage site from paired-end
whole-genome sequencing data of CRISPR–edited human cell line.    Report the coordinate as the position of the
blunt end of the Cas9 cut (3bp upstream of the PAM, 1-based hg38 coordinates). Report the coordinate in the
format chr#:position (e.g., chr1:12345678).

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 回答有显式格式要求，按题目中的示例逐字段输出。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## rec9ogrlqg5u0ke09
- **任务类型**：样本标签识别
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/rec9ogrlqg5u0ke09.zip` -> `extracted/rec9ogrlqg5u0ke09/`
- **可读文件（Top-level）**：Sample1.bw, Sample10.bw, Sample2.bw, Sample3.bw, Sample4.bw, Sample5.bw, Sample6.bw, Sample7.bw, Sample8.bw, Sample9.bw
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> You are provided with 10 anonymized human RNA-seq BigWig files (sample01.bigWig to sample10.bigWig). Four
samples were prepared using Ribo-Zero rRNA depletion, and six samples were prepared using oligo(dT) polyA
selection. Using GENCODE v46 gene annotations (hg38), identify the four Ribo-Zero samples based on the
distribution of RNA-seq signal across genomic features (exons, introns, and intergenic regions). List the four
Ribo-Zero sample filenames exactly as provided (e.g., sample01.bigWig), separated by commas.

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 回答有显式格式要求，按题目中的示例逐字段输出。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## recaikavdwoimjy3b
- **任务类型**：基因缺失/敲除/靶基因定位
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/recaikavdwoimjy3b.zip` -> `extracted/recaikavdwoimjy3b/`
- **可读文件（Top-level）**：anonyomized_rnaseq_count.tsv.gz
- **任务标签**：human_solvable = no（建议在成绩分层里作为难度指标）

### 任务题面
> Which genes was knocked out in the sample 1,2,3 versus 4,5,6? Provide the knocked-out gene(s) as official gene
symbols, separated by commas if multiple.

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 输出为单项答案（词名/符号/ID），仍建议做大小写和同义名归一化。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 此题目为公开评测中人工未解题，优先记录关键特征（如 QC、主成分、聚类、富集项）后再给出最可能答案。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## recartntbrx7kwzkv
- **任务类型**：样本标签识别
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/recartntbrx7kwzkv.zip` -> `extracted/recartntbrx7kwzkv/`
- **可读文件（Top-level）**：sample1.vcf.gz, sample10.vcf.gz, sample11.vcf.gz, sample12.vcf.gz, sample13.vcf.gz, sample14.vcf.gz, sample15.vcf.gz, sample16.vcf.gz, sample17.vcf.gz, sample18.vcf.gz, sample19.vcf.gz, sample2.vcf.gz, sample20.vcf.gz, sample21.vcf.gz, sample22.vcf.gz, sample23.vcf.gz, sample24.vcf.gz, sample25.vcf.gz, sample26.vcf.gz, sample27.vcf.gz
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> Which 2 samples in this set are close relatives. Provide the two sample identifiers (e.g., sample1, sample2)
as they appear in the dataset.

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 按样本 ID 列表输出，建议保持顺序和命名一致。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## recav6jt6q0aa9sjs
- **任务类型**：多模态生信推断
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/recav6jt6q0aa9sjs.zip` -> `extracted/recav6jt6q0aa9sjs/`
- **可读文件（Top-level）**：sample_A_gene_quantifications.tsv
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> Which cell line is this RNA-seq gene expression data from?  Candidate cell lines (24 total): K562, HL-60,
GM12878, DND-41, THP-1, HepG2,  A549, IMR-90, MCF-7, MDA-MB-231, HCT116, Caco-2, SW620, SK-N-SH, SH-SY5Y,
BE2C, PC-3, DU145, Panc1, HEK293, H1, H9, BJ, HFFc6

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 输出为单项答案（词名/符号/ID），仍建议做大小写和同义名归一化。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## recbkqinqhpfdn9bq
- **任务类型**：测序实验元数据提取
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/recbkqinqhpfdn9bq.zip` -> `extracted/recbkqinqhpfdn9bq/`
- **可读文件（Top-level）**：read1.fastq.gz
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> What pathogen was sequenced to produce these RNA-seq reads? Please report the standard scientific name of
genus and species.

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 输出为单项答案（词名/符号/ID），仍建议做大小写和同义名归一化。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## recc3vmqjrsefqw57
- **任务类型**：遗传变异/结构变异判定
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/recc3vmqjrsefqw57.zip` -> `extracted/recc3vmqjrsefqw57/`
- **可读文件（Top-level）**：BRCA1_ANON_R1.fastq.gz, BRCA1_ANON_R2.fastq.gz
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> Which exon of the BRCA1 gene contains a homozygous deletion in this sample? Provide the Ensembl exon ID (e.g.,
ENSE00004011560).

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 回答有显式格式要求，按题目中的示例逐字段输出。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## reccipvrmk1k0gqkr
- **任务类型**：基因缺失/敲除/靶基因定位
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/reccipvrmk1k0gqkr.zip` -> `extracted/reccipvrmk1k0gqkr/`
- **可读文件（Top-level）**：read1.fastq.gz, read2.fastq.gz
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> Which 2 protein-coding genes are knocked out in this yeast strain? Provide the standard gene symbols for the
knocked out genes.

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 输出为单项答案（词名/符号/ID），仍建议做大小写和同义名归一化。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## reccniibn7ary80hj
- **任务类型**：样本标签识别
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/reccniibn7ary80hj.zip` -> `extracted/reccniibn7ary80hj/`
- **可读文件（Top-level）**：uploadData
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> What chromosome is triplicated in this sample? Provide the chromosome number (e.g., 'chromosome 21' or just
'21').

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 输出为单项答案（词名/符号/ID），仍建议做大小写和同义名归一化。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## reccslfjnjcfdpgak
- **任务类型**：亲本/家系关系推断
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/reccslfjnjcfdpgak.zip` -> `extracted/reccslfjnjcfdpgak/`
- **可读文件（Top-level）**：MOTHER_ANON_R1.fastq.gz, MOTHER_ANON_R2.fastq.gz, SON_ANON_R1.fastq.gz, SON_ANON_R2.fastq.gz
- **任务标签**：human_solvable = no（建议在成绩分层里作为难度指标）

### 任务题面
> Given mtDNA whole genome sequencing data from a mother-son pair, identify the number of homoplasmic variants
(≥95% heteroplasmy) that demonstrate maternal inheritance patterns. Report your answer as a single integer
representing the count of variants.

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 输出为单项答案（词名/符号/ID），仍建议做大小写和同义名归一化。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 此题目为公开评测中人工未解题，优先记录关键特征（如 QC、主成分、聚类、富集项）后再给出最可能答案。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## reccwgc4buredxvyz
- **任务类型**：测序实验元数据提取
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/reccwgc4buredxvyz.zip` -> `extracted/reccwgc4buredxvyz/`
- **可读文件（Top-level）**：data_files
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> Which two samples were swapped in the sequencing run? Provide the sample names or identifiers for the two
swapped samples.

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 输出为单项答案（词名/符号/ID），仍建议做大小写和同义名归一化。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## rece8yuamgclcpj9i
- **任务类型**：扩增子引物/marker 区域识别
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/rece8yuamgclcpj9i.zip` -> `extracted/rece8yuamgclcpj9i/`
- **可读文件（Top-level）**：anonymized_expression.txt
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> Given gene expression profiles from 4 drug treatments in OCI-LY3 cells, match each treatment group to the
correct compound from the following candidates: Geldanamycin, Trichostatin A, Rapamycin, Doxorubicin. Provide
your answer as a list matching each treatment group (A, B, C, D) to its compound, e.g., 'Group A: [Compound]'.

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 回答有显式格式要求，按题目中的示例逐字段输出。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## recea4hqimc4sypon
- **任务类型**：组织/来源推断
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/recea4hqimc4sypon.zip` -> `extracted/recea4hqimc4sypon/`
- **可读文件（Top-level）**：task2_data
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> The whole genome CpG methylation data are generated for different donor's different tissue types. Each data
file represents one donor's certain tissue's genome wide CpG methylation profile. During sample transfer and
processing, donor's different tissue data may get swapped or mislabelled. From the list of 16 CpG methylation
bed files (labeled as <tissue_type>-<donor>.bed.gz) from 7 donors across 4 different tissue types, identify
which donor's identity or tissue type information has been mislabelled. Report your findings by specifying
which donor(s) and tissue type(s) are mislabelled, and describe what the correct labels should be (e.g.,
'Donor X's tissue A is mislabelled as tissue B').

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 回答有显式格式要求，按题目中的示例逐字段输出。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## recffr4vmqdynph2n
- **任务类型**：基因缺失/敲除/靶基因定位
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/recffr4vmqdynph2n.zip` -> `extracted/recffr4vmqdynph2n/`
- **可读文件（Top-level）**：read1.fastq.gz, read2.fastq.gz
- **任务标签**：human_solvable = no（建议在成绩分层里作为难度指标）

### 任务题面
> Which protein-coding C. elegans gene has a heterozygous knockout in this sample? Provide the gene symbol.

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 输出为单项答案（词名/符号/ID），仍建议做大小写和同义名归一化。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 此题目为公开评测中人工未解题，优先记录关键特征（如 QC、主成分、聚类、富集项）后再给出最可能答案。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## recgrmy32hxalop9m
- **任务类型**：参考基因组或比对参数推断
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/recgrmy32hxalop9m.zip` -> `extracted/recgrmy32hxalop9m/`
- **可读文件（Top-level）**：Sample1.bed, Sample10.bed, Sample11.bed, Sample12.bed, Sample13.bed, Sample14.bed, Sample15.bed, Sample16.bed, Sample17.bed, Sample18.bed, Sample19.bed, Sample2.bed, Sample20.bed, Sample21.bed, Sample22.bed, Sample23.bed, Sample24.bed, Sample25.bed, Sample26.bed, Sample27.bed
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> You are provided with anonymized ChIP-seq peak files generated from multiple histone modification experiments
(e.g., H3K4me1/2/3, H3K27ac, H3K27me3, H3K36me3, H3K79me1/2, H3K9me3, H2A.Z, and others; up to 30 distinct
histone marks). The histone modification names and filenames are anonymized. Identify which sample corresponds
to the H3K36me3 histone modification experiment.    Data Characteristics Genome assembly: hg19 Cell line:
Human H1 embryonic stem cells (H1 ESC) File format: BED (chr, start, end, name, score, strand) Number of
anonymized peak files: 30 Design: One sample per histone modification. Provide your answer as the filename
(e.g., SampleX.bed).

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 回答有显式格式要求，按题目中的示例逐字段输出。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## rechlnhmn1jsmsser
- **任务类型**：参考基因组或比对参数推断
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/rechlnhmn1jsmsser.zip` -> `extracted/rechlnhmn1jsmsser/`
- **可读文件（Top-level）**：annonymize1.fastq, annonymize2.fastq, kpneumoniae_ref.fasta
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> Whole-genome sequencing reads from Klebsiella pneumoniae mutant strain generated via transposon mutagenesis is
provided. Identify the genomic coordinate (chromosome, position) of the 47bp transposon insertion site in the
reference genome. Report the chromosome as a RefSeq accession ID and the position as a 1-based coordinate
(e.g., Chromosome: NC_XXXXXX.X, Position: NNNNNN).

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 输出为单项答案（词名/符号/ID），仍建议做大小写和同义名归一化。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## rechnr2wkqiqxjwlv
- **任务类型**：组织/来源推断
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/rechnr2wkqiqxjwlv.zip` -> `extracted/rechnr2wkqiqxjwlv/`
- **可读文件（Top-level）**：ORGANISM_ANON_R1.fastq.gz, ORGANISM_ANON_R2.fastq.gz
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> Estimate the haploid genome size of this organism to the nearest megabase (Mb). Report your answer as a single
integer representing megabases (e.g., '5' for 5 Mb).

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 输出为单项答案（词名/符号/ID），仍建议做大小写和同义名归一化。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## reci6iglwiertmyyk
- **任务类型**：基因缺失/敲除/靶基因定位
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/reci6iglwiertmyyk.zip` -> `extracted/reci6iglwiertmyyk/`
- **可读文件（Top-level）**：matrixTpm_anonymized.tsv
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> Identify which anonymized sample corresponds to E2F6 knockdown based on gene expression data?  Gene expression
matrix file contains siRNA knock down of 32 different genes in a human cell line. Sample headers are
anonymized. Expression values are in tags per million (TPM). The sample headers are randomly anonymized as
sampleID1, sampleID2 and so on up to sample32.  Data characteristics: Organism: Human File format: TSV file
with genes as rows and sampleIDs as columns Number of gene knockdown: 32 Sample headers: Anonymized as
sample1, sample2, …., sample32

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 回答有显式格式要求，按题目中的示例逐字段输出。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## recjgwpbyodqoihqc
- **任务类型**：多模态生信推断
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/recjgwpbyodqoihqc.zip` -> `extracted/recjgwpbyodqoihqc/`
- **可读文件（Top-level）**：sample-data.txt, standards-data.txt
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> Can you calculate the observed molecular weight of my purified protein ( based on the elution profile of a gel
filtration standard containing Thyroglobulin (670 kDa), γ-Globulin (158 kDa), Ovalbumin (44 kDa), Myoglobin
(17 kDa), and Vitamin B12 (1.35 kDa)? Report the molecular weight in kDa, rounded to the nearest whole number.

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 输出为单项答案（词名/符号/ID），仍建议做大小写和同义名归一化。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## recmiryoehog9bvce
- **任务类型**：遗传变异/结构变异判定
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/recmiryoehog9bvce.zip` -> `extracted/recmiryoehog9bvce/`
- **可读文件（Top-level）**：FUSION_ANON_R1.fastq.gz, FUSION_ANON_R2.fastq.gz
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> Based on the provided RNA-seq dataset, which specific gene fusion product represents a translocation between
Chromosome 11 and Chromosome 21? Provide the gene symbols of the 5' and 3' partners

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 回答有显式格式要求，按题目中的示例逐字段输出。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## recmp75e1chtpzx3c
- **任务类型**：微生物/宏基因组来源判定
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/recmp75e1chtpzx3c.zip` -> `extracted/recmp75e1chtpzx3c/`
- **可读文件（Top-level）**：read1.fastq.gz, read2.fastq.gz
- **任务标签**：human_solvable = no（建议在成绩分层里作为难度指标）

### 任务题面
> What bacteria was spiked into this sample. Provide the scientific name (genus and species) of the bacteria.

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 输出为单项答案（词名/符号/ID），仍建议做大小写和同义名归一化。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 此题目为公开评测中人工未解题，优先记录关键特征（如 QC、主成分、聚类、富集项）后再给出最可能答案。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## recn4p43tkgazjeqy
- **任务类型**：遗传变异/结构变异判定
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/recn4p43tkgazjeqy.zip` -> `extracted/recn4p43tkgazjeqy/`
- **可读文件（Top-level）**：TP53_ANON_R1.fastq.gz, TP53_ANON_R2.fastq.gz
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> At which codon position in the TP53 gene is there a truncating mutation?

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 回答有显式格式要求，按题目中的示例逐字段输出。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## recn5sa8gwpqsx15g
- **任务类型**：分群/群体/标签聚类
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/recn5sa8gwpqsx15g.zip` -> `extracted/recn5sa8gwpqsx15g/`
- **可读文件（Top-level）**：chr22_5pops.vcf
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> Given genotype data for 60 individuals with anonymized IDs, cluster these individuals into 5 distinct
population groups corresponding to 1000 Genomes populations. Report the cluster assignments for each
individual using 1000 Genomes population codes (CEU, CHB, YRI, GIH, PEL). Format: Sample<tab>Population, one
per line.

### 评分规则（要点）
- 需达到 95% 及以上正确率判为正确（否则为 0 分）；无部分分。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 回答有显式格式要求，按题目中的示例逐字段输出。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## recnayu0v8zttjlgf
- **任务类型**：样本标签识别
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/recnayu0v8zttjlgf.zip` -> `extracted/recnayu0v8zttjlgf/`
- **可读文件（Top-level）**：BMB-NHK-Task3
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> Which of these RNA-seq  samples are technical replicates? sort these 15 samples into 3 sets of 5 technical
replicates. List each group with sample numbers separated by commas (e.g., Group 1: 1,2,3,4,5).

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 回答有显式格式要求，按题目中的示例逐字段输出。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## recnheebqpbdp1nj9
- **任务类型**：样本标签识别
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/recnheebqpbdp1nj9.zip` -> `extracted/recnheebqpbdp1nj9/`
- **可读文件（Top-level）**：infected-hepatocytes-1.anon.fastq.gz, infected-hepatocytes-2.anon.fastq.gz, infected-hepatocytes-3.anon.fastq.gz, viral-genomes-filtered.fna
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> What viral subspecies/strain are these cells most likely infected with (assume that there is only one valid
infection)? Provide the full virus name including the strain designation (e.g., 'Virus species strain
StrainName').

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 输出为单项答案（词名/符号/ID），仍建议做大小写和同义名归一化。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## recnquldskiadnpq8
- **任务类型**：样本标签识别
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/recnquldskiadnpq8.zip` -> `extracted/recnquldskiadnpq8/`
- **可读文件（Top-level）**：sample10_R1.fastq.gz, sample10_R2.fastq.gz, sample11_R1.fastq.gz, sample11_R2.fastq.gz, sample12_R1.fastq.gz, sample12_R2.fastq.gz, sample1_R1.fastq.gz, sample1_R2.fastq.gz, sample2_R1.fastq.gz, sample2_R2.fastq.gz, sample3_R1.fastq.gz, sample3_R2.fastq.gz, sample4_R1.fastq.gz, sample4_R2.fastq.gz, sample5_R1.fastq.gz, sample5_R2.fastq.gz, sample6_R1.fastq.gz, sample6_R2.fastq.gz, sample7_R1.fastq.gz, sample7_R2.fastq.gz
- **任务标签**：human_solvable = no（建议在成绩分层里作为难度指标）

### 任务题面
> Which gene has been knocked down in samples 1,3,4,11 (GENE1), and which gene in samples 7,9,10,12 (GENE2)
compared to samples 2,5,6,8 which have no genes knocked down? Provide answers as Ensembl gene IDs.

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 输出为单项答案（词名/符号/ID），仍建议做大小写和同义名归一化。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 此题目为公开评测中人工未解题，优先记录关键特征（如 QC、主成分、聚类、富集项）后再给出最可能答案。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## recoyp6qrymldcjle
- **任务类型**：微生物/宏基因组来源判定
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/recoyp6qrymldcjle.zip` -> `extracted/recoyp6qrymldcjle/`
- **可读文件（Top-level）**：read1.fastq.bz2, read2.fastq.bz2
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> What symbiont bacterial genome is contained within this FASTQ file? Provide the bacterial genus name.

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 回答有显式格式要求，按题目中的示例逐字段输出。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## recqgsfxqqodhjens
- **任务类型**：组织/来源推断
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/recqgsfxqqodhjens.zip` -> `extracted/recqgsfxqqodhjens/`
- **可读文件（Top-level）**：peaks_file.bed
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> Identify the transcription factor whose binding sites are represented by the provided peaks data. Provide the
transcription factor's gene symbol.

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 输出为单项答案（词名/符号/ID），仍建议做大小写和同义名归一化。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## recqjfzttushuxz4j
- **任务类型**：基因缺失/敲除/靶基因定位
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/recqjfzttushuxz4j.zip` -> `extracted/recqjfzttushuxz4j/`
- **可读文件（Top-level）**：read1.fastq.gz, read2.fastq.gz
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> What yeast gene on chromosome 1 was knocked out in this dataset? Provide the standard gene symbol (e.g., TDA1,
not the systematic ORF name).

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 输出为单项答案（词名/符号/ID），仍建议做大小写和同义名归一化。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## recrgfvzr5rrjpim7
- **任务类型**：样本标签识别
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/recrgfvzr5rrjpim7.zip` -> `extracted/recrgfvzr5rrjpim7/`
- **可读文件（Top-level）**：Sample1.bed, Sample10.bed, Sample11.bed, Sample12.bed, Sample13.bed, Sample14.bed, Sample15.bed, Sample16.bed, Sample17.bed, Sample18.bed, Sample19.bed, Sample2.bed, Sample20.bed, Sample21.bed, Sample22.bed, Sample23.bed, Sample24.bed, Sample25.bed, Sample26.bed, Sample27.bed
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> Identify the sample that corresponds to H3K27me3 histone modification experiment from 30 anonymized ChIP-seq
peak files. Provide your answer as the filename (e.g., SampleX.bed) corresponding to the H3K27me3 experiment.

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 按题目文本给定的字段/单值格式返回。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## recro5s1o0odyssqs
- **任务类型**：样本标签识别
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/recro5s1o0odyssqs.zip` -> `extracted/recro5s1o0odyssqs/`
- **可读文件（Top-level）**：read1.fastq.gz
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> What protein coding transcript is spiked into this FASTQ file and appears at a level much higher than any
other transcript? Provide the answer as the Ensembl transcript name (e.g., GENE-201).

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 回答有显式格式要求，按题目中的示例逐字段输出。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## recsvhviava5okg19
- **任务类型**：遗传变异/结构变异判定
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/recsvhviava5okg19.zip` -> `extracted/recsvhviava5okg19/`
- **可读文件（Top-level）**：mutation_matrix.txt
- **任务标签**：human_solvable = no（建议在成绩分层里作为难度指标）

### 任务题面
> Which COSMIC single-base substitution (SBS) mutational signature has the highest relative contribution (%) in
the breast tumor samples? Provide the answer as the COSMIC SBS signature ID (e.g., SBS1).

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 按题目文本给定的字段/单值格式返回。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 此题目为公开评测中人工未解题，优先记录关键特征（如 QC、主成分、聚类、富集项）后再给出最可能答案。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## rectaxd8eganpl4lw
- **任务类型**：遗传变异/结构变异判定
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/rectaxd8eganpl4lw.zip` -> `extracted/rectaxd8eganpl4lw/`
- **可读文件（Top-level）**：AMPLICON.txt, CRISPR_ANON_R1.fastq.gz, CRISPR_ANON_R2.fastq.gz
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> After Cas9-mediated genome editing, what percentage of sequencing reads show modifications (insertions,
deletions, or substitutions) at the target locus? Report to the nearest 1%. Include all modification types
(insertions, deletions, and substitutions) in the quantification window.

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 回答有显式格式要求，按题目中的示例逐字段输出。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## recug1uijclv7ni4q
- **任务类型**：微生物/宏基因组来源判定
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/recug1uijclv7ni4q.zip` -> `extracted/recug1uijclv7ni4q/`
- **可读文件（Top-level）**：goodReads.fastq
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> Which bacterial genome was deliberately spiked into this sample? Please report the genus and species

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 输出为单项答案（词名/符号/ID），仍建议做大小写和同义名归一化。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## recv1pkneurxhwpo9
- **任务类型**：基因表达/基因识别
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/recv1pkneurxhwpo9.zip` -> `extracted/recv1pkneurxhwpo9/`
- **可读文件（Top-level）**：task3_data
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> Gene fusions drive cancer by creating abnormal, hybrid proteins or altering gene expression. In the task,
peripheral blood samples of three cancer patients (with the same cancer type and stage) were collected to
extract genomic DNA and total RNA to perform whole exome DNA sequencing (WES-seq) and whole transcriptome RNA
sequencing (RNA-seq). Using the datasets to identify the common gene fusion variants among the three cancer
patients. Report the gene fusion using standard nomenclature (e.g., GENE1-GENE2 format with official gene
symbols).

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 回答有显式格式要求，按题目中的示例逐字段输出。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## recv7lmpypdi61mdi
- **任务类型**：遗传变异/结构变异判定
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/recv7lmpypdi61mdi.zip` -> `extracted/recv7lmpypdi61mdi/`
- **可读文件（Top-level）**：ECDNA_ANON_R1.fastq.gz, ECDNA_ANON_R2.fastq.gz
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> Identify which protein-coding oncogene has been amplified on an extrachromosomal DNA. Provide the answer as a
HUGO gene symbol.

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 回答有显式格式要求，按题目中的示例逐字段输出。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## recvgrwtebczhn3k8
- **任务类型**：亲本/家系关系推断
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/recvgrwtebczhn3k8.zip` -> `extracted/recvgrwtebczhn3k8/`
- **可读文件（Top-level）**：recVgRWtebCzHN3k8_plink.bed, recVgRWtebCzHN3k8_plink.bim, recVgRWtebCzHN3k8_plink.fam
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> Identify the mother and father of subject qU3pFkp4d4ILfsLN from a cohort of 1114 individuals with whole genome
SNP-microarray data. Report the mother and father using their subject IDs as they appear in the PLINK format
data files.

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 回答有显式格式要求，按题目中的示例逐字段输出。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## recvnlq3i6id6qqge
- **任务类型**：组织/来源推断
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/recvnlq3i6id6qqge.zip` -> `extracted/recvnlq3i6id6qqge/`
- **可读文件（Top-level）**：anonymizedGeneExp.tsv.gz
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> In the given RNA-seq expression data matrix, identify the sample “sampleID_2” comes from which tissue ?
Provide the tissue name, including specific anatomical region if applicable.

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 输出为单项答案（词名/符号/ID），仍建议做大小写和同义名归一化。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## recvwctg0xadnklms
- **任务类型**：组织/来源推断
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/recvwctg0xadnklms.zip` -> `extracted/recvwctg0xadnklms/`
- **可读文件（Top-level）**：gene_read_counts_2555_tissue_samples.csv, gene_read_counts_unknown_tissue_sample.csv, metadata_2555_tissue_samples.csv
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> What human tissue does this RNA-seq sample represent? Choose from a list of 68 possible tissues represented by
2555 samples. Provide the tissue name exactly as it appears in the sample metadata tissue column.

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 回答有显式格式要求，按题目中的示例逐字段输出。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## recx4bsaa5zoxy3nv
- **任务类型**：样本标签识别
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/recx4bsaa5zoxy3nv.zip` -> `extracted/recx4bsaa5zoxy3nv/`
- **可读文件（Top-level）**：ctrl1.tsv, ctrl2.tsv, kd1.tsv, kd2.tsv
- **任务标签**：human_solvable = no（建议在成绩分层里作为难度指标）

### 任务题面
> Identify the gene that was knocked down in the K562 cell line based on the provided transcript level
quantification. The candidate list is: MBNL1, ADD3, VEGFA, RBFOX1, RBFOX2, PTBP1, QKI, SRSF1, SRSF2, HNRNPA1,
NOVA1, SF3B1, HSP90AB1, EGR1, HBB, ALB, ACTB, RBM39,GADD45A.

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 回答有显式格式要求，按题目中的示例逐字段输出。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 此题目为公开评测中人工未解题，优先记录关键特征（如 QC、主成分、聚类、富集项）后再给出最可能答案。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## recxdlpmtviybebk8
- **任务类型**：测序实验元数据提取
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/recxdlpmtviybebk8.zip` -> `extracted/recxdlpmtviybebk8/`
- **可读文件（Top-level）**：sample10_annon.bam, sample10_annon.bam.bai, sample11_annon.bam, sample11_annon.bam.bai, sample12_annon.bam, sample12_annon.bam.bai, sample13_annon.bam, sample13_annon.bam.bai, sample14_annon.bam, sample14_annon.bam.bai, sample15_annon.bam, sample15_annon.bam.bai, sample1_annon.bam, sample1_annon.bam.bai, sample2_annon.bam, sample2_annon.bam.bai, sample3_annon.bam, sample3_annon.bam.bai, sample4_annon.bam, sample4_annon.bam.bai
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> Given 15 mapped BAM files, where identifiers, sequence lane information and file names are anonymized.
Identify all six BAM files that represent ATAC-seq assay.

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 回答有显式格式要求，按题目中的示例逐字段输出。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## recy5kshz8ysawujt
- **任务类型**：微生物/宏基因组来源判定
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/recy5kshz8ysawujt.zip` -> `extracted/recy5kshz8ysawujt/`
- **可读文件（Top-level）**：read1.fastq.gz, read2.fastq.gz
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> What bacteria is most prominent in this sample. Provide the answer as the full scientific name (genus and
species).

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 按题目文本给定的字段/单值格式返回。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## recyolnajpygz2xeo
- **任务类型**：参考基因组或比对参数推断
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/recyolnajpygz2xeo.zip` -> `extracted/recyolnajpygz2xeo/`
- **可读文件（Top-level）**：sample1.bed, sample10.bed, sample11.bed, sample12.bed, sample13.bed, sample14.bed, sample15.bed, sample16.bed, sample17.bed, sample18.bed, sample19.bed, sample2.bed, sample20.bed, sample21.bed, sample22.bed, sample23.bed, sample24.bed, sample25.bed, sample26.bed, sample27.bed
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> Identify the anonymized sampleID that corresponds to the experiment that immunoprecipitated the transcription
factor (TF) TP53.   You are provided with 30 anonymized ChIP-seq peak files (BED format). Each peak file
represents an immunoprecipitation experiment performed on a human embryonic cell line (hESC) cell line. Each
file is labeled only as sample1.bed through sample30.bed.  Data characteristics: Assembly: hg38 (GRCh38) File
format: BED (chr, start, end, name, score, strand) Number of anonymized TF peak files: 30 One sample per
transcription factor

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 回答有显式格式要求，按题目中的示例逐字段输出。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## recyomvehwpj8s6t1
- **任务类型**：组织/来源推断
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/recyomvehwpj8s6t1.zip` -> `extracted/recyomvehwpj8s6t1/`
- **可读文件（Top-level）**：MTDNA_ANON_R1.fastq.gz, MTDNA_ANON_R2.fastq.gz
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> Which major mtDNA haplogroup does this sample originate from? Provide the major haplogroup as a single letter
(A-Z).

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 输出为单项答案（词名/符号/ID），仍建议做大小写和同义名归一化。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---

## reczkg8fvfp1fo3nn
- **任务类型**：组织/来源推断
- **任务目录 / 数据归档**：`/data3/zcwang/biomysterybench/full/data/reczkg8fvfp1fo3nn.zip` -> `extracted/reczkg8fvfp1fo3nn/`
- **可读文件（Top-level）**：h3k27ac_peaks.bed.gz
- **任务标签**：human_solvable = yes（建议在成绩分层里作为难度指标）

### 任务题面
> Given H3K27ac ChIP-seq peaks from an unknown cell type, identify the cell type from 20 candidates by analyzing
super-enhancer profiles. Candidate cell types: B_cell_GM12878, Smooth_muscle, Endothelial_cell, T_cell_CD4,
T_cell_CD8, NK_cell, Monocyte, Macrophage, Dendritic_cell, Neutrophil, Erythroid_K562, Megakaryocyte, ESC_H1,
HSC, Hepatocyte_HepG2, Epithelial_lung, Epithelial_colon, Fibroblast, Neuron, Cardiomyocyte

### 评分规则（要点）
- 全对才给分（0/1）。
- 题目为无部分分制，任何缺失项或歧义通常直接判错。

### 输出建议
- 输出为单项答案（词名/符号/ID），仍建议做大小写和同义名归一化。
- 允许域名（供策略日志）：conda.anaconda.org, repo.anaconda.com, ncbi.nlm.nih.gov, ftp.ncbi.nlm.nih.gov, ensembl.org, ftp.ensembl.org, hgdownload.soe.ucsc.edu, unipro...

### 建议测试步骤
- 先快速列出样本元数据/注释列；再做约束筛选后再回写最终答案，避免误判。
- 使用可复现脚本（Python/R 均可）完成以下：读取 -> 清洗 -> 推断 -> 导出中间图表/统计表。
- 结果建议保存为独立文件（如 tsv/csv/tsv 或 png），用于审计与复盘。

---
