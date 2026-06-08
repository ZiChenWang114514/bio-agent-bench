"""Prepare real GEO-derived benchmark task packs."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

import anndata as ad
import numpy as np
import pandas as pd

from bio_agent_bench.schema import write_schema


GEO_SOURCES: dict[str, dict[str, str]] = {
    "GSE209844": {
        "title": "Loss of centrosomal gene ALMS1 alters lipid metabolism and extracellular matrix regulation",
        "series_url": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE209844",
        "counts_url": "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE209nnn/GSE209844/suppl/GSE209844_CountMatrixMerged.txt.gz",
        "rlog_url": "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE209nnn/GSE209844/suppl/GSE209844_NormalizedCountMatrix_rlog.txt.gz",
        "deseq_url": "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE209nnn/GSE209844/suppl/GSE209844_RNA-seq_results_DESeq2.txt.gz",
    },
    "GSE178088": {
        "title": "CD16+ CD163+ monocytes traffic to sites of inflammation in NEC",
        "series_url": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE178088",
        "h5ad_url": "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE178nnn/GSE178088/suppl/GSE178088_cluster3.h5ad.gz",
    },
}


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n")


def _read_geo_table(path: Path) -> pd.DataFrame:
    return pd.read_csv(path, sep=r"\s+", engine="python")


def _clean_decimal(value: object) -> float:
    return float(str(value).replace(",", "."))


def write_all_schemas(repo_root: str | Path) -> None:
    root = Path(repo_root)
    write_schema(root / "tasks/geo_bulk_alms1_ko/expected_output.schema.json")
    write_schema(root / "tasks/geo_scrna_nec_inflammation/expected_output.schema.json")


def prepare_bulk_alms1_task(repo_root: str | Path) -> None:
    """Prepare a blinded bulk RNA-seq task from GSE209844."""

    root = Path(repo_root)
    raw_dir = root / "data/raw_geo/GSE209844"
    out_dir = root / "tasks/geo_bulk_alms1_ko/data/public_geo"
    hidden_dir = root / ".hidden/geo_answers"
    out_dir.mkdir(parents=True, exist_ok=True)
    hidden_dir.mkdir(parents=True, exist_ok=True)

    counts_raw = _read_geo_table(raw_dir / "GSE209844_CountMatrixMerged.txt.gz")
    counts_raw = counts_raw[~counts_raw["ENSEMBL_GeneID"].astype(str).str.startswith("__")].copy()
    counts_raw = counts_raw.set_index("ENSEMBL_GeneID")

    rlog_raw = pd.read_csv(
        raw_dir / "GSE209844_NormalizedCountMatrix_rlog.txt.gz",
        sep=r"\s+",
        engine="python",
        index_col=0,
    )
    rlog_raw.index = rlog_raw.index.astype(str).str.strip('"')
    rlog_raw.columns = rlog_raw.columns.astype(str).str.strip('"')
    deseq = pd.read_csv(raw_dir / "GSE209844_RNA-seq_results_DESeq2.txt.gz", sep="\t")
    deseq = deseq.rename(columns={deseq.columns[0]: "ensembl_gene_id", "TXBIOTYPE": "tx_biotype"})

    source_to_blind = {
        "C1_countMatrix": "sample_01",
        "C2_countMatrix": "sample_02",
        "C3_countMatrix": "sample_03",
        "KO1_countMatrix": "sample_04",
        "KO2_countMatrix": "sample_05",
        "KO3_countMatrix": "sample_06",
    }
    rlog_to_blind = {
        "C1": "sample_01",
        "C2": "sample_02",
        "C3": "sample_03",
        "KO1": "sample_04",
        "KO2": "sample_05",
        "KO3": "sample_06",
    }
    group_by_sample = {
        "sample_01": "group_alpha",
        "sample_02": "group_alpha",
        "sample_03": "group_alpha",
        "sample_04": "group_beta",
        "sample_05": "group_beta",
        "sample_06": "group_beta",
    }
    source_label = {
        "sample_01": "WT_1",
        "sample_02": "WT_2",
        "sample_03": "WT_3",
        "sample_04": "ALMS1_KO_1",
        "sample_05": "ALMS1_KO_2",
        "sample_06": "ALMS1_KO_3",
    }

    counts = counts_raw.rename(columns=source_to_blind).loc[:, list(group_by_sample)]
    counts.index.name = "ensembl_gene_id"
    counts.to_csv(out_dir / "counts.tsv", sep="\t")

    rlog = rlog_raw.rename(columns=rlog_to_blind).loc[counts.index, list(group_by_sample)]
    rlog.index.name = "ensembl_gene_id"
    rlog.to_csv(out_dir / "rlog.tsv", sep="\t")

    sample_sheet = pd.DataFrame(
        {
            "sample_id": list(group_by_sample),
            "blinded_group": [group_by_sample[sid] for sid in group_by_sample],
            "replicate": [1, 2, 3, 1, 2, 3],
        }
    )
    sample_sheet.to_csv(out_dir / "sample_sheet.tsv", sep="\t", index=False)

    annotations = deseq[["ensembl_gene_id", "symbol", "tx_biotype"]].drop_duplicates()
    annotations = annotations[annotations["ensembl_gene_id"].isin(counts.index)]
    annotations.to_csv(out_dir / "gene_annotations.tsv", sep="\t", index=False)

    alms1 = deseq[deseq["symbol"].astype(str).str.upper().eq("ALMS1")].iloc[0]
    provenance = {
        "geo_accession": "GSE209844",
        "source_title": GEO_SOURCES["GSE209844"]["title"],
        "source_url": GEO_SOURCES["GSE209844"]["series_url"],
        "public_files": {
            "counts": "counts.tsv",
            "rlog": "rlog.tsv",
            "sample_sheet": "sample_sheet.tsv",
            "gene_annotations": "gene_annotations.tsv",
        },
        "blinding": "Original sample labels were replaced with sample_01..sample_06 and group_alpha/group_beta.",
    }
    _write_json(hidden_dir / "geo_bulk_alms1_ko_provenance.hidden.json", provenance)

    answer = {
        "task_id": "geo_bulk_alms1_ko",
        "answer": {
            "anomaly_type": "knockout_gene",
            "anomalous_group": "group_beta",
            "rationale": "group_beta corresponds to the ALMS1 knockout samples in GSE209844.",
            "key_statistics": {
                "target_gene": "ALMS1",
                "target_ensembl_gene_id": "ENSG00000116127",
                "source_log2_fold_change_ko_vs_wt": _clean_decimal(alms1["log2FoldChange"]),
                "source_padj": _clean_decimal(alms1["padj"]),
            },
        },
        "source_mapping": source_label,
        "source_urls": GEO_SOURCES["GSE209844"],
    }
    _write_json(hidden_dir / "geo_bulk_alms1_ko_answer.hidden.json", answer)


def prepare_scrna_nec_task(repo_root: str | Path) -> None:
    """Prepare a blinded scRNA-seq task from GSE178088."""

    root = Path(repo_root)
    raw_path = root / "data/raw_geo/GSE178088/GSE178088_cluster3.h5ad"
    out_dir = root / "tasks/geo_scrna_nec_inflammation/data/public_geo"
    hidden_dir = root / ".hidden/geo_answers"
    out_dir.mkdir(parents=True, exist_ok=True)
    hidden_dir.mkdir(parents=True, exist_ok=True)

    adata = ad.read_h5ad(raw_path)
    adata.raw = None
    feature_names = (
        adata.var["features"].astype(str).to_numpy()
        if "features" in adata.var.columns
        else adata.var_names.astype(str).to_numpy()
    )
    adata.var_names = pd.Index(feature_names, name="gene_symbol")
    adata.var_names_make_unique()
    adata.var = pd.DataFrame(index=adata.var_names)

    source_sample = adata.obs["orig.ident"].astype(str)
    source_cohort = source_sample.str.extract(r"^(Fetal|Neonatal|NEC)", expand=False)
    sample_values = sorted(source_sample.unique())
    sample_map = {sample: f"sample_{idx + 1:02d}" for idx, sample in enumerate(sample_values)}
    cohort_map = {"Fetal": "cohort_alpha", "Neonatal": "cohort_beta", "NEC": "cohort_gamma"}

    obs = pd.DataFrame(index=[f"cell_{idx + 1:05d}" for idx in range(adata.n_obs)])
    obs["sample_id"] = source_sample.map(sample_map).to_numpy()
    obs["blinded_cohort"] = source_cohort.map(cohort_map).to_numpy()
    obs["seurat_cluster"] = adata.obs["seurat_clusters"].astype(str).to_numpy()
    obs["n_counts"] = adata.obs["nCount_RNA"].to_numpy()
    obs["n_features"] = adata.obs["nFeature_RNA"].to_numpy()
    obs["percent_mito"] = adata.obs["percent.mt"].to_numpy()
    adata.obs = obs

    adata.write_h5ad(out_dir / "adata.h5ad", compression="gzip")
    obs.reset_index(names="cell_id").to_csv(out_dir / "metadata.tsv", sep="\t", index=False)
    pd.DataFrame({"gene_symbol": adata.var_names}).to_csv(
        out_dir / "gene_annotations.tsv", sep="\t", index=False
    )
    sample_sheet = (
        obs.groupby(["sample_id", "blinded_cohort"], observed=True)
        .size()
        .reset_index(name="n_cells")
        .sort_values("sample_id")
    )
    sample_sheet.to_csv(out_dir / "sample_sheet.tsv", sep="\t", index=False)

    marker_genes = ["IL1B", "CXCL8", "S100A8", "S100A9", "TREM1"]
    x = adata.X.toarray() if hasattr(adata.X, "toarray") else np.asarray(adata.X)
    marker_idx = [adata.var_names.get_loc(gene) for gene in marker_genes if gene in adata.var_names]
    marker_score_by_cohort: dict[str, float] = {}
    if marker_idx:
        marker_score = np.asarray(x[:, marker_idx]).mean(axis=1)
        for cohort in sorted(obs["blinded_cohort"].unique()):
            marker_score_by_cohort[cohort] = float(marker_score[obs["blinded_cohort"].to_numpy() == cohort].mean())

    provenance = {
        "geo_accession": "GSE178088",
        "source_title": GEO_SOURCES["GSE178088"]["title"],
        "source_url": GEO_SOURCES["GSE178088"]["series_url"],
        "public_files": {
            "adata": "adata.h5ad",
            "metadata": "metadata.tsv",
            "sample_sheet": "sample_sheet.tsv",
            "gene_annotations": "gene_annotations.tsv",
        },
        "blinding": "Original sample and cohort labels were replaced with sample_XX and cohort_alpha/beta/gamma.",
        "marker_hint": "Inflammation-associated markers such as IL1B, CXCL8, S100A8, S100A9, and TREM1 are useful evidence.",
    }
    _write_json(hidden_dir / "geo_scrna_nec_inflammation_provenance.hidden.json", provenance)

    answer = {
        "task_id": "geo_scrna_nec_inflammation",
        "answer": {
            "anomaly_type": "cohort",
            "anomalous_group": "cohort_gamma",
            "rationale": "cohort_gamma corresponds to NEC intestinal samples and shows the strongest inflammatory marker signal.",
            "key_statistics": {
                "source_truth": "NEC",
                "marker_genes": marker_genes,
                "marker_score_by_blinded_cohort": marker_score_by_cohort,
            },
        },
        "source_sample_mapping": sample_map,
        "source_cohort_mapping": cohort_map,
        "source_urls": GEO_SOURCES["GSE178088"],
    }
    _write_json(hidden_dir / "geo_scrna_nec_inflammation_answer.hidden.json", answer)


def prepare_all_geo_tasks(repo_root: str | Path) -> None:
    write_all_schemas(repo_root)
    prepare_bulk_alms1_task(repo_root)
    prepare_scrna_nec_task(repo_root)


def decompress_h5ad_if_needed(repo_root: str | Path) -> None:
    """Decompress the GSE178088 h5ad.gz if the plain h5ad is missing."""

    import gzip
    import shutil

    root = Path(repo_root)
    gz_path = root / "data/raw_geo/GSE178088/GSE178088_cluster3.h5ad.gz"
    h5ad_path = root / "data/raw_geo/GSE178088/GSE178088_cluster3.h5ad"
    if h5ad_path.exists():
        return
    with gzip.open(gz_path, "rb") as source, h5ad_path.open("wb") as target:
        shutil.copyfileobj(source, target)
