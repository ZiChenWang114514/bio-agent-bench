# Task Authoring Notes

Use this repository as a template for realistic biological agent tasks based on
public processed GEO data.

## Principles

- Prefer processed GEO supplementary files over FASTQ/SRA reprocessing.
- Make the correct answer objective and hidden.
- Require terminal use and analysis artifacts.
- Avoid pure LeetCode-style programming puzzles.
- Avoid tasks that require domain tools unavailable in a fresh Python
  environment.

## Current Task Families

`geo_bulk_alms1_ko` tests whether an agent can combine count normalization,
gene annotation, perturbation reasoning, and group-level statistics.

`geo_scrna_nec_inflammation` tests whether an agent can read an `.h5ad`,
compute basic single-cell QC, and aggregate inflammation marker expression by
blinded cohort.

## GEO Task Preparation

After downloading raw GEO supplementary files into `data/raw_geo/`, run:

```bash
python scripts/prepare_geo_tasks.py
```

The script writes blinded task packs under `tasks/*/data/public_geo` and hidden
answer keys under `.hidden/geo_answers/`.
