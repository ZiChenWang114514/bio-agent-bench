# Public Notes

This task uses processed public sequencing data with source identifiers removed
from the benchmark data pack. Original sample labels were blinded.

Useful analysis routes:

- Compare ALMS1 expression between blinded groups.
- Compute genome-wide group effects on the rlog matrix.
- Use PCA or clustering as a QC artifact.

Do not rely on file names, source lookup, or memorized dataset provenance;
process scoring expects evidence that the expression matrices were actually
read and analyzed.
