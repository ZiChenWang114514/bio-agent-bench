#!/usr/bin/env python
"""Baseline analysis for the GSE209844 ALMS1 KO task."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", type=Path, default=Path("tasks/geo_bulk_alms1_ko/data/public_geo"))
    parser.add_argument("--out-dir", type=Path, default=Path("examples/baseline_outputs/geo_bulk"))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rlog = pd.read_csv(args.data_dir / "rlog.tsv", sep="\t", index_col=0)
    samples = pd.read_csv(args.data_dir / "sample_sheet.tsv", sep="\t")
    annotations = pd.read_csv(args.data_dir / "gene_annotations.tsv", sep="\t")
    annotations = annotations.set_index("symbol", drop=False)

    group_means = rlog.T.join(samples.set_index("sample_id")["blinded_group"]).groupby("blinded_group").mean()
    alms1_gene_id = str(annotations.loc["ALMS1", "ensembl_gene_id"])
    alms1_by_group = group_means[alms1_gene_id].to_dict()
    anomalous_group = min(alms1_by_group, key=alms1_by_group.get)

    diff = group_means.loc["group_beta"] - group_means.loc["group_alpha"]
    top_table = (
        pd.DataFrame({"ensembl_gene_id": diff.index, "group_beta_minus_alpha": diff.values})
        .merge(annotations.reset_index(drop=True), on="ensembl_gene_id", how="left")
        .assign(abs_effect=lambda frame: frame["group_beta_minus_alpha"].abs())
        .sort_values("abs_effect", ascending=False)
    )
    top_table.to_csv(args.out_dir / "group_effect_scores.tsv", sep="\t", index=False)

    pca = PCA(n_components=2, random_state=0).fit_transform(rlog.T)
    fig, ax = plt.subplots(figsize=(5.2, 4.2))
    color = samples["blinded_group"].map({"group_alpha": 0, "group_beta": 1})
    ax.scatter(pca[:, 0], pca[:, 1], c=color, cmap="Set1", s=60, edgecolor="white", linewidth=0.5)
    ax.set_xlabel("PC1")
    ax.set_ylabel("PC2")
    ax.set_title("GSE209844 blinded-group PCA")
    fig.tight_layout()
    fig.savefig(args.out_dir / "bulk_pca.png", dpi=160)
    plt.close(fig)

    submission = {
        "task_id": "geo_bulk_alms1_ko",
        "answer": {
            "anomaly_type": "knockout_gene",
            "anomalous_group": anomalous_group,
            "rationale": "The group with lower ALMS1 expression is reported as the ALMS1 knockout group.",
            "key_statistics": {
                "ALMS1_group_alpha_mean_rlog": float(alms1_by_group["group_alpha"]),
                "ALMS1_group_beta_mean_rlog": float(alms1_by_group["group_beta"]),
                "ALMS1_group_beta_minus_alpha": float(alms1_by_group["group_beta"] - alms1_by_group["group_alpha"]),
            },
        },
        "confidence": 0.86,
        "evidence": [
            {
                "type": "target_gene_expression",
                "description": "ALMS1 expression is lower in the predicted knockout group.",
                "value": float(alms1_by_group["group_beta"] - alms1_by_group["group_alpha"]),
            },
            {
                "type": "pca",
                "description": "PCA was generated to inspect separation between blinded sample groups.",
                "value": "bulk_pca.png",
            },
        ],
        "artifacts": [
            {"type": "table", "path": "group_effect_scores.tsv", "description": "Group-level expression effects."},
            {"type": "plot", "path": "bulk_pca.png", "description": "PCA colored by blinded group."},
        ],
        "commands_summary": [
            "python examples/baseline_geo_bulk.py",
            "read rlog.tsv, sample_sheet.tsv, and gene_annotations.tsv with pandas",
            "computed ALMS1 group means, genome-wide group effects, and PCA plot",
        ],
    }
    (args.out_dir / "submission.json").write_text(json.dumps(submission, indent=2) + "\n")
    print(args.out_dir / "submission.json")


if __name__ == "__main__":
    main()

