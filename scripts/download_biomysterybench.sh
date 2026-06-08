#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage:
  scripts/download_biomysterybench.sh preview
  scripts/download_biomysterybench.sh full

Environment:
  BIOMYSTERY_ROOT   Output root. Default: /data3/zcwang/biomysterybench
  HF_ENDPOINT       Hugging Face mirror endpoint. Default: https://hf-mirror.com
  HF_TOKEN          Required for the gated full dataset.

Notes:
  - preview is public and small.
  - full is gated; accept the dataset terms on Hugging Face first, then export
    HF_TOKEN before running this script.
USAGE
}

if [[ $# -ne 1 ]]; then
  usage >&2
  exit 2
fi

MODE="$1"
ROOT="${BIOMYSTERY_ROOT:-/data3/zcwang/biomysterybench}"
ENDPOINT="${HF_ENDPOINT:-https://hf-mirror.com}"

download_file() {
  local repo="$1"
  local remote_path="$2"
  local out_dir="$3"
  local out_path="${out_dir}/${remote_path}"
  local partial_path="${out_path}.partial"
  mkdir -p "$(dirname "${out_path}")"

  local url="${ENDPOINT}/datasets/${repo}/resolve/main/${remote_path}"
  local curl_args=(--location --fail --retry 5 --retry-delay 2)
  if [[ -n "${HF_TOKEN:-}" ]]; then
    curl_args+=(--header "Authorization: Bearer ${HF_TOKEN}")
  fi
  curl "${curl_args[@]}" --output "${partial_path}" "${url}"
  mv "${partial_path}" "${out_path}"
}

case "${MODE}" in
  preview)
    OUT="${ROOT}/preview"
    mkdir -p "${OUT}"
    for path in README.md LICENSE problems.csv problems.parquet data.zip; do
      download_file "Anthropic/BioMysteryBench-preview" "${path}" "${OUT}"
    done
    mkdir -p "${OUT}/extracted"
    unzip -q -o "${OUT}/data.zip" -d "${OUT}/extracted"
    ;;
  full)
    if [[ -z "${HF_TOKEN:-}" ]]; then
      echo "HF_TOKEN is required for Anthropic/BioMysteryBench-full." >&2
      echo "Accept the gated dataset terms on Hugging Face, then run:" >&2
      echo "  export HF_TOKEN=..." >&2
      echo "  scripts/download_biomysterybench.sh full" >&2
      exit 1
    fi
    OUT="${ROOT}/full"
    mkdir -p "${OUT}"
    for path in README.md LICENSE problems.csv problems.parquet; do
      download_file "Anthropic/BioMysteryBench-full" "${path}" "${OUT}"
    done
    if [[ ! -f "${OUT}/filelist.txt" ]]; then
      HF_ENDPOINT="${ENDPOINT}" python - <<'PY' > "${OUT}/filelist.txt"
import os
from huggingface_hub import HfApi
api = HfApi(endpoint=os.environ["HF_ENDPOINT"])
for filename in api.list_repo_files("Anthropic/BioMysteryBench-full", repo_type="dataset"):
    print(filename)
PY
    fi
    while IFS= read -r path; do
      [[ "${path}" == data/*.zip ]] || continue
      download_file "Anthropic/BioMysteryBench-full" "${path}" "${OUT}"
    done < "${OUT}/filelist.txt"
    ;;
  -h|--help)
    usage
    ;;
  *)
    echo "Unknown mode: ${MODE}" >&2
    usage >&2
    exit 2
    ;;
esac
