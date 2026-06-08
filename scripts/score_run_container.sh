#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage:
  scripts/score_run_container.sh --task TASK_ID --run-id RUN_ID [--image IMAGE] [--process-log PATH]

Examples:
  scripts/score_run_container.sh --task geo_bulk_alms1_ko --run-id opus_001
  scripts/score_run_container.sh --task geo_scrna_nec_inflammation --run-id debug --process-log runs/debug/geo_scrna_nec_inflammation/workspace/process.log
USAGE
}

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TASK=""
RUN_ID=""
IMAGE="bio-agent-bench-evaluator:latest"
PROCESS_LOG=""

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
    --process-log)
      PROCESS_LOG="${2:-}"
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

RUN_ROOT="${ROOT}/runs/${RUN_ID}/${TASK}"
TASK_BUNDLE="${RUN_ROOT}/task"
WORKSPACE="${RUN_ROOT}/workspace"
SUBMISSION="${WORKSPACE}/submission.json"
ANSWER="${ROOT}/.hidden/geo_answers/${TASK}_answer.hidden.json"

if [[ ! -d "${TASK_BUNDLE}" ]]; then
  echo "Missing task bundle: ${TASK_BUNDLE}" >&2
  exit 1
fi
if [[ ! -f "${SUBMISSION}" ]]; then
  echo "Missing submission: ${SUBMISSION}" >&2
  exit 1
fi
if [[ ! -f "${ANSWER}" ]]; then
  echo "Missing hidden answer: ${ANSWER}" >&2
  exit 1
fi

EXTRA_ARGS=()
PROCESS_LOG_MOUNT=()
if [[ -n "${PROCESS_LOG}" ]]; then
  PROCESS_LOG_ABS="$(cd "$(dirname "${PROCESS_LOG}")" && pwd)/$(basename "${PROCESS_LOG}")"
  if [[ ! -f "${PROCESS_LOG_ABS}" ]]; then
    echo "Missing process log: ${PROCESS_LOG}" >&2
    exit 1
  fi
  PROCESS_LOG_MOUNT=(-v "${PROCESS_LOG_ABS}:/process.log:ro")
  EXTRA_ARGS=(--process-log /process.log)
fi

docker run --rm \
  --network none \
  --cpus 2 \
  --memory 8g \
  --pids-limit 256 \
  --cap-drop ALL \
  --security-opt no-new-privileges \
  --read-only \
  --tmpfs /tmp:rw,nosuid,size=512m \
  -v "${TASK_BUNDLE}:/task:ro" \
  -v "${WORKSPACE}:/workspace:rw" \
  -v "${ANSWER}:/hidden/answer.json:ro" \
  "${PROCESS_LOG_MOUNT[@]}" \
  "${IMAGE}" \
  --task-root /task \
  --submission /workspace/submission.json \
  --answer /hidden/answer.json \
  --out /workspace/score.json \
  "${EXTRA_ARGS[@]}"

echo "Wrote ${WORKSPACE}/score.json"
