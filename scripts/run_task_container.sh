#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage:
  scripts/run_task_container.sh --task TASK_ID --run-id RUN_ID [--image IMAGE] [--command CMD] [--timeout-seconds N]

Examples:
  scripts/run_task_container.sh --task geo_bulk_alms1_ko --run-id opus_001
  scripts/run_task_container.sh --task geo_scrna_nec_inflammation --run-id debug --command "python -V && bash"
USAGE
}

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TASK=""
RUN_ID=""
IMAGE="bio-agent-bench-agent:latest"
COMMAND="/bin/bash"
TIMEOUT_SECONDS=0

while [[ $# -gt 0 ]]; do
  case "$1" in
    --task)
      TASK="${2:-}"
      shift 2
      ;;
    --run-id)
      RUN_ID="${2:-}"
      shift 2
      ;;
    --image)
      IMAGE="${2:-}"
      shift 2
      ;;
    --command)
      COMMAND="${2:-}"
      shift 2
      ;;
    --timeout-seconds)
      TIMEOUT_SECONDS="${2:-}"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

if [[ -z "${TASK}" || -z "${RUN_ID}" ]]; then
  usage >&2
  exit 2
fi

TASK_ROOT="${ROOT}/tasks/${TASK}"
DATA_ROOT="${TASK_ROOT}/data/public_geo"
if [[ ! -d "${DATA_ROOT}" ]]; then
  echo "No public data directory for task: ${TASK}" >&2
  exit 1
fi

RUN_ROOT="${ROOT}/runs/${RUN_ID}/${TASK}"
TASK_BUNDLE="${RUN_ROOT}/task"
WORKSPACE="${RUN_ROOT}/workspace"
rm -rf "${TASK_BUNDLE}"
mkdir -p "${TASK_BUNDLE}/data" "${WORKSPACE}"

cp "${TASK_ROOT}/prompt.md" "${TASK_BUNDLE}/prompt.md"
cp "${TASK_ROOT}/expected_output.schema.json" "${TASK_BUNDLE}/expected_output.schema.json"
if [[ -f "${TASK_ROOT}/public_notes.md" ]]; then
  cp "${TASK_ROOT}/public_notes.md" "${TASK_BUNDLE}/public_notes.md"
fi
cp -a "${DATA_ROOT}/." "${TASK_BUNDLE}/data/"
rm -f "${TASK_BUNDLE}/data/source_provenance.json"

cat > "${RUN_ROOT}/README.txt" <<EOF
Task: ${TASK}
Run ID: ${RUN_ID}

Inside the container:
  /task      read-only task bundle
  /workspace writable output directory

Required output:
  /workspace/submission.json
EOF

DOCKER_TTY=(-i)
if [[ -t 0 && -t 1 ]]; then
  DOCKER_TTY=(-it)
fi

DOCKER_CMD=(
  docker run --rm "${DOCKER_TTY[@]}"
  --network none \
  --cpus 4 \
  --memory 16g \
  --pids-limit 512 \
  --cap-drop ALL \
  --security-opt no-new-privileges \
  --read-only \
  --tmpfs /tmp:rw,nosuid,size=2g \
  -e HOME=/workspace \
  -e MPLBACKEND=Agg \
  -v "${TASK_BUNDLE}:/task:ro" \
  -v "${WORKSPACE}:/workspace:rw" \
  -w /workspace \
  "${IMAGE}" \
  bash -lc "${COMMAND}"
)

if [[ "${TIMEOUT_SECONDS}" != "0" ]]; then
  timeout --preserve-status "${TIMEOUT_SECONDS}" "${DOCKER_CMD[@]}"
else
  "${DOCKER_CMD[@]}"
fi
