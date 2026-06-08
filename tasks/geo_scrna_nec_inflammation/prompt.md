# Task: geo_scrna_nec_inflammation

You are given a blinded single-cell RNA-seq dataset from human intestinal
tissue. Source identifiers have been removed; solve the task from the provided
data object and metadata, not from provenance lookup.

Files:

- `adata.h5ad`: single-cell expression object with blinded `obs` metadata.
- `metadata.tsv`: exported cell metadata.
- `sample_sheet.tsv`: blinded sample-level cell counts.
- `gene_annotations.tsv`: gene symbols.

Question:

Which blinded cohort shows the strongest inflammation-associated abnormality?

Return a `submission.json` following `expected_output.schema.json`.

Use:

- `anomaly_type`: `cohort`
- `anomalous_group`: the predicted blinded cohort, for example `cohort_alpha`,
  `cohort_beta`, or `cohort_gamma`

Requirements:

- Read `adata.h5ad` from the terminal with analysis code.
- Compute cohort-level QC and expression summaries.
- Generate at least one QC/statistical artifact.
- Include evidence from inflammatory markers such as `IL1B`, `CXCL8`,
  `S100A8`, `S100A9`, or `TREM1`.
