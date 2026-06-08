from __future__ import annotations

from pathlib import Path

import anndata as ad
import pandas as pd

from bio_agent_bench.validate import validate_submission


ROOT = Path(__file__).resolve().parents[1]


def test_bulk_geo_pack_exists() -> None:
    data_dir = ROOT / "tasks/geo_bulk_alms1_ko/data/public_geo"
    counts = pd.read_csv(data_dir / "counts.tsv", sep="\t", index_col=0)
    samples = pd.read_csv(data_dir / "sample_sheet.tsv", sep="\t")
    annotations = pd.read_csv(data_dir / "gene_annotations.tsv", sep="\t")
    assert counts.shape[1] == 6
    assert set(samples["blinded_group"]) == {"group_alpha", "group_beta"}
    assert "ALMS1" in set(annotations["symbol"])


def test_scrna_geo_pack_exists() -> None:
    data_dir = ROOT / "tasks/geo_scrna_nec_inflammation/data/public_geo"
    adata = ad.read_h5ad(data_dir / "adata.h5ad", backed="r")
    assert adata.n_obs == 2404
    assert adata.n_vars > 20_000
    assert {"sample_id", "blinded_cohort", "seurat_cluster"}.issubset(adata.obs.columns)
    adata.file.close()


def test_baseline_submissions_match_schema() -> None:
    bulk = ROOT / "examples/baseline_outputs/geo_bulk/submission.json"
    scrna = ROOT / "examples/baseline_outputs/geo_scrna/submission.json"
    if bulk.exists():
        validate_submission(bulk)
    if scrna.exists():
        validate_submission(scrna)

