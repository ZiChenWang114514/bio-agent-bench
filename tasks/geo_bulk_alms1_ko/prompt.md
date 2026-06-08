# Task: geo_bulk_alms1_ko

You are given a blinded bulk RNA-seq dataset from a two-group ALMS1
perturbation experiment. Source identifiers have been removed; solve the task
from the provided matrices, not from provenance lookup.

Files:

- `counts.tsv`: raw count matrix, genes by blinded samples.
- `rlog.tsv`: DESeq2 rlog-normalized expression matrix.
- `sample_sheet.tsv`: blinded sample metadata with `sample_id`,
  `blinded_group`, and replicate number.
- `gene_annotations.tsv`: Ensembl gene IDs and gene symbols.

Question:

One blinded group is ALMS1 knockout and the other is wild type. Determine which
`blinded_group` is the ALMS1 knockout group.

Return a `submission.json` following `expected_output.schema.json`.

Use:

- `anomaly_type`: `knockout_gene`
- `anomalous_group`: the predicted blinded group, for example `group_alpha` or
  `group_beta`

Requirements:

- Inspect the data from the terminal.
- Write and run analysis code.
- Generate at least one QC/statistical artifact.
- Include expression evidence involving ALMS1 or group-level differential
  expression.
