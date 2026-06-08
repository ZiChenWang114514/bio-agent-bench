# Public Notes

This task uses processed public single-cell data with source identifiers
removed from the benchmark data pack. Original sample and cohort labels were
blinded.

Useful analysis routes:

- Read the h5ad object and inspect `obs`.
- Summarize QC metrics by `blinded_cohort`.
- Score inflammation-associated marker genes by cohort.
- Use PCA or cluster-level summaries as supporting artifacts.

Do not rely on file names, source lookup, or memorized dataset provenance;
process scoring expects evidence that the h5ad file was actually read and
analyzed.
