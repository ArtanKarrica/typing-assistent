#!/bin/bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OLLAMA_BIN="${OLLAMA_BIN:-/usr/local/bin/ollama}"
MODEL="${OLLAMA_MODEL:-qwen3.5:0.8b}"
OLLAMA_HOST="${OLLAMA_HOST:-127.0.0.1:11434}"
OLLAMA_LOG="$SCRIPT_DIR/application.log"

if [ ! -x "$OLLAMA_BIN" ] && ! command -v "$OLLAMA_BIN" >/dev/null 2>&1; then
  echo "Ollama was not found at $OLLAMA_BIN"
  exit 1
fi

if curl -fsS "http://$OLLAMA_HOST/api/tags" >/dev/null 2>&1; then
  echo "Ollama API is already running at http://$OLLAMA_HOST."
else
  echo "Starting Ollama API server in the background..."
  nohup "$OLLAMA_BIN" serve >>"$OLLAMA_LOG" 2>&1 &

  for _ in {1..20}; do
    if curl -fsS "http://$OLLAMA_HOST/api/tags" >/dev/null 2>&1; then
      break
    fi
    sleep 1
  done

  if ! curl -fsS "http://$OLLAMA_HOST/api/tags" >/dev/null 2>&1; then
    echo "Ollama API did not start successfully. Check $OLLAMA_LOG"
    exit 1
  fi
fi

echo "Ensuring model is available: $MODEL"
"$OLLAMA_BIN" pull "$MODEL"
echo "Ollama is ready."
