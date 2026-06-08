#!/usr/bin/env python
"""Baseline analysis for the GSE178088 NEC inflammation task."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import anndata as ad
import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA


MARKERS = ["IL1B", "CXCL8", "S100A8", "S100A9", "TREM1"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", type=Path, default=Path("tasks/geo_scrna_nec_inflammation/data/public_geo"))
    parser.add_argument("--out-dir", type=Path, default=Path("examples/baseline_outputs/geo_scrna"))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    adata = ad.read_h5ad(args.data_dir / "adata.h5ad")
    obs = adata.obs.copy()
    x = adata.X.toarray() if hasattr(adata.X, "toarray") else np.asarray(adata.X)
    marker_idx = [adata.var_names.get_loc(gene) for gene in MARKERS if gene in adata.var_names]
    marker_score = x[:, marker_idx].mean(axis=1)
    obs["inflammation_marker_score"] = marker_score
    score_table = (
        obs.groupby("blinded_cohort", observed=True)
        .agg(
            n_cells=("sample_id", "size"),
            mean_marker_score=("inflammation_marker_score", "mean"),
            median_percent_mito=("percent_mito", "median"),
            median_n_features=("n_features", "median"),
        )
        .reset_index()
        .sort_values("mean_marker_score", ascending=False)
    )
    score_table.to_csv(args.out_dir / "cohort_inflammation_scores.tsv", sep="\t", index=False)
    anomalous_group = str(score_table.iloc[0]["blinded_cohort"])

    variable_idx = np.argsort(np.asarray(x.var(axis=0)))[-500:]
    pca = PCA(n_components=2, random_state=0).fit_transform(np.log1p(x[:, variable_idx]))
    palette = {value: idx for idx, value in enumerate(sorted(obs["blinded_cohort"].unique()))}
    colors = obs["blinded_cohort"].map(palette).to_numpy()
    fig, ax = plt.subplots(figsize=(5.4, 4.4))
    ax.scatter(pca[:, 0], pca[:, 1], c=colors, cmap="Set1", s=6, alpha=0.75, linewidth=0)
    ax.set_xlabel("PC1")
    ax.set_ylabel("PC2")
    ax.set_title("GSE178088 cells colored by blinded cohort")
    fig.tight_layout()
    fig.savefig(args.out_dir / "scrna_pca.png", dpi=160)
    plt.close(fig)

    top = score_table.iloc[0]
    submission = {
        "task_id": "geo_scrna_nec_inflammation",
        "answer": {
            "anomaly_type": "cohort",
            "anomalous_group": anomalous_group,
            "rationale": "The selected cohort has the strongest inflammatory marker expression signal.",
            "key_statistics": {
                "mean_marker_score": float(top["mean_marker_score"]),
                "n_cells": int(top["n_cells"]),
                "marker_genes_used": ",".join([gene for gene in MARKERS if gene in adata.var_names]),
            },
        },
        "confidence": 0.82,
        "evidence": [
            {
                "type": "marker_score",
                "description": "Inflammatory marker genes were averaged by blinded cohort.",
                "value": float(top["mean_marker_score"]),
            },
            {
                "type": "pca",
                "description": "A PCA plot was generated to inspect cohort-level structure.",
                "value": "scrna_pca.png",
            },
        ],
        "artifacts": [
            {"type": "table", "path": "cohort_inflammation_scores.tsv", "description": "Cohort marker scores."},
            {"type": "plot", "path": "scrna_pca.png", "description": "PCA colored by blinded cohort."},
        ],
        "commands_summary": [
            "python examples/baseline_geo_scrna.py",
            "read adata.h5ad with anndata and metadata from adata.obs",
            "computed inflammatory marker scores, QC summaries, and PCA plot",
        ],
    }
    (args.out_dir / "submission.json").write_text(json.dumps(submission, indent=2) + "\n")
    print(args.out_dir / "submission.json")


if __name__ == "__main__":
    main()

