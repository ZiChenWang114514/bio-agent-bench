#!/usr/bin/env bash
set -euo pipefail

ROOT="${BIOMYSTERY_FULL_ROOT:-/data3/zcwang/biomysterybench/full}"
DATA_DIR="${ROOT}/data"
FILELIST="${ROOT}/filelist.txt"
LOG="${ROOT}/wait_and_prepare.log"
STATUS="${ROOT}/wait_status.tsv"
OUT_DIR="${ROOT}/processed"
SLEEP_SECONDS="${BIOMYSTERY_WAIT_SECONDS:-60}"

mkdir -p "${ROOT}" "${OUT_DIR}"

timestamp() {
  date '+%Y-%m-%d %H:%M:%S'
}

log() {
  printf '[%s] %s\n' "$(timestamp)" "$*" | tee -a "${LOG}"
}

expected_zip_count() {
  if [[ -f "${FILELIST}" ]]; then
    awk '/^data\/.*\.zip$/ {n++} END {print n+0}' "${FILELIST}"
  else
    echo 99
  fi
}

download_alive() {
  pgrep -f 'download_biomysterybench.sh full|run_full_download.sh' >/dev/null 2>&1
}

write_status_line() {
  local expected="$1"
  local completed="$2"
  local partial="$3"
  local bytes="$4"
  local alive="$5"
  printf '%s\t%s\t%s\t%s\t%s\t%s\n' "$(timestamp)" "${expected}" "${completed}" "${partial}" "${bytes}" "${alive}" >> "${STATUS}"
}

prepare_after_download() {
  log "Starting initial BioMysteryBench-full processing."

  python - <<'PY'
import csv
import json
import os
import zipfile
from pathlib import Path

root = Path(os.environ.get("BIOMYSTERY_FULL_ROOT", "/data3/zcwang/biomysterybench/full"))
data_dir = root / "data"
out_dir = root / "processed"
out_dir.mkdir(parents=True, exist_ok=True)

problems_csv = root / "problems.csv"
filelist = root / "filelist.txt"

expected = []
if filelist.exists():
    expected = [
        line.strip()
        for line in filelist.read_text().splitlines()
        if line.startswith("data/") and line.endswith(".zip")
    ]

zip_paths = sorted(data_dir.glob("*.zip"))
missing = []
if expected:
    expected_names = {Path(p).name for p in expected}
    have_names = {p.name for p in zip_paths}
    missing = sorted(expected_names - have_names)

inventory_path = out_dir / "zip_inventory.tsv"
with inventory_path.open("w", newline="") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=[
            "id",
            "zip_file",
            "size_bytes",
            "n_members",
            "uncompressed_bytes",
            "top_level_entries",
            "zip_test",
        ],
        delimiter="\t",
    )
    writer.writeheader()
    for zp in zip_paths:
        task_id = zp.stem
        zip_test = "not_tested"
        n_members = 0
        uncompressed = 0
        top_levels = []
        try:
            with zipfile.ZipFile(zp) as zf:
                infos = zf.infolist()
                n_members = len(infos)
                uncompressed = sum(i.file_size for i in infos)
                top_levels = sorted({i.filename.split("/")[0] for i in infos if i.filename})
                bad = zf.testzip()
                zip_test = "ok" if bad is None else f"bad:{bad}"
        except Exception as exc:
            zip_test = f"error:{type(exc).__name__}"
        writer.writerow(
            {
                "id": task_id,
                "zip_file": str(zp),
                "size_bytes": zp.stat().st_size,
                "n_members": n_members,
                "uncompressed_bytes": uncompressed,
                "top_level_entries": ",".join(top_levels[:20]),
                "zip_test": zip_test,
            }
        )

summary_path = out_dir / "problems_summary.tsv"
rows = []
if problems_csv.exists():
    with problems_csv.open(newline="") as f:
        rows = list(csv.DictReader(f))
    with summary_path.open("w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "id",
                "human_solvable",
                "question_chars",
                "answer_rubric_chars",
                "allowed_domains_count",
            ],
            delimiter="\t",
        )
        writer.writeheader()
        for row in rows:
            domains = [d.strip() for d in row.get("allowed_domains", "").split(",") if d.strip()]
            writer.writerow(
                {
                    "id": row.get("id", ""),
                    "human_solvable": row.get("human_solvable", ""),
                    "question_chars": len(row.get("question", "")),
                    "answer_rubric_chars": len(row.get("answer_rubric", "")),
                    "allowed_domains_count": len(domains),
                }
            )

report = {
    "root": str(root),
    "expected_zip_count": len(expected) if expected else None,
    "downloaded_zip_count": len(zip_paths),
    "missing_zip_count": len(missing),
    "missing_zip_files": missing[:20],
    "problems_rows": len(rows),
    "outputs": {
        "zip_inventory": str(inventory_path),
        "problems_summary": str(summary_path),
    },
}
(out_dir / "processing_report.json").write_text(json.dumps(report, indent=2))
(out_dir / "processing_report.md").write_text(
    "\n".join(
        [
            "# BioMysteryBench Full Initial Processing",
            "",
            f"- Root: `{root}`",
            f"- Expected zip count: `{report['expected_zip_count']}`",
            f"- Downloaded zip count: `{report['downloaded_zip_count']}`",
            f"- Missing zip count: `{report['missing_zip_count']}`",
            f"- Problems rows: `{report['problems_rows']}`",
            "",
            "Generated files:",
            "",
            f"- `{inventory_path}`",
            f"- `{summary_path}`",
            f"- `{out_dir / 'processing_report.json'}`",
        ]
    )
    + "\n"
)
PY

  log "Initial processing finished. Outputs are in ${OUT_DIR}."
}

main() {
  local expected
  expected="$(expected_zip_count)"
  log "Watcher started. root=${ROOT}; expected_zip_count=${expected}; poll_seconds=${SLEEP_SECONDS}"

  printf 'timestamp\texpected_zip_count\tcompleted_zip_count\tpartial_count\tdata_bytes\tdownloader_alive\n' > "${STATUS}"

  while true; do
    local completed partial bytes alive
    completed="$(find "${DATA_DIR}" -maxdepth 1 -type f -name '*.zip' 2>/dev/null | wc -l)"
    partial="$(find "${DATA_DIR}" -maxdepth 1 -type f -name '*.partial' 2>/dev/null | wc -l)"
    bytes="$(du -sb "${ROOT}" 2>/dev/null | awk '{print $1}')"
    if download_alive; then
      alive="yes"
    else
      alive="no"
    fi
    write_status_line "${expected}" "${completed}" "${partial}" "${bytes}" "${alive}"
    log "status completed=${completed}/${expected} partial=${partial} bytes=${bytes} downloader_alive=${alive}"

    if [[ "${completed}" -ge "${expected}" && "${partial}" -eq 0 ]]; then
      log "All expected zip files are present."
      break
    fi

    if [[ "${alive}" == "no" ]]; then
      log "Downloader is not alive and download is incomplete. Waiting in case it is restarted."
    fi

    sleep "${SLEEP_SECONDS}"
  done

  prepare_after_download
}

main "$@"
