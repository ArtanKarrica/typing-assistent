#!/bin/bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="$SCRIPT_DIR/venv"

if [ ! -d "$VENV_DIR" ]; then
  echo "Creating virtual environment..."
  python3 -m venv "$VENV_DIR"
fi

source "$VENV_DIR/bin/activate"

if ! python3 -c "import httpx, pynput, pyperclip, rich" >/dev/null 2>&1; then
  echo "Installing Python dependencies..."
  pip install -r "$SCRIPT_DIR/requirements.txt"
fi

echo "Starting Typing Assistant..."
echo "Press Cmd+Ctrl+Q inside the app or Ctrl+C in this terminal to stop."
python3 "$SCRIPT_DIR/main.py"

deactivate
echo "Typing Assistant stopped."
