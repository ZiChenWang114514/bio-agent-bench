# Data Sources

The current tasks use public GEO processed supplementary files.

## GSE209844

- GEO: <https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE209844>
- Title: Loss of centrosomal gene ALMS1 alters lipid metabolism and the
  regulation of processes linked to the extracellular matrix.
- Public processed files used:
  - `GSE209844_CountMatrixMerged.txt.gz`
  - `GSE209844_NormalizedCountMatrix_rlog.txt.gz`
  - `GSE209844_RNA-seq_results_DESeq2.txt.gz`
- Benchmark task: `geo_bulk_alms1_ko`

## GSE178088

- GEO: <https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE178088>
- Title: CD16+ CD163+ monocytes traffic to sites of inflammation in NEC.
- Public processed file used:
  - `GSE178088_cluster3.h5ad.gz`
- Benchmark task: `geo_scrna_nec_inflammation`

## Blinding Policy

Original sample labels and disease/perturbation labels are not included in
public task metadata. They are mapped to `sample_XX`, `group_alpha/beta`, or
`cohort_alpha/beta/gamma`. Hidden answer files under `.hidden/` contain the
source mapping and are not committed.

