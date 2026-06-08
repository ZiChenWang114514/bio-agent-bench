#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

docker build \
  -f "${ROOT}/Dockerfile.agent" \
  -t bio-agent-bench-agent:latest \
  "${ROOT}"

docker build \
  -f "${ROOT}/Dockerfile.evaluator" \
  -t bio-agent-bench-evaluator:latest \
  "${ROOT}"

echo "Built bio-agent-bench-agent:latest and bio-agent-bench-evaluator:latest"

