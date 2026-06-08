# Public Notes

This task uses processed supplementary files from GEO series GSE178088. Original
sample and cohort labels were blinded in the benchmark data pack.

Useful analysis routes:

- Read the h5ad object and inspect `obs`.
- Summarize QC metrics by `blinded_cohort`.
- Score inflammation-associated marker genes by cohort.
- Use PCA or cluster-level summaries as supporting artifacts.

Do not rely on file names or internet lookup alone; process scoring expects
evidence that the h5ad file was actually read and analyzed.

