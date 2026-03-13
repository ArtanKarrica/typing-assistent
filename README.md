# Typing Assistant

Typing Assistant is a macOS keyboard helper that sends selected text to Ollama, fixes mistakes, and pastes the edited text back into the active app.

## What It Does

- Fixes typos, grammar, punctuation, and capitalization
- Improves selected text while keeping the original meaning and tone
- Cleans non-printable characters from the current selection
- Works through global hotkeys

## Requirements

- macOS
- Python 3.11 or newer
- [Ollama](https://ollama.com/)
- Accessibility and Input Monitoring permissions for the terminal or app that runs the script

## Quick Start

1. Start Ollama:

   ```bash
   ./start_ollama.sh
   ```

2. Start the Typing Assistant in a second terminal:

   ```bash
   ./run_app.sh
   ```

3. Use the hotkeys in any app.

## Hotkeys

- `F9`: Fix the current line
- `F10`: Fix the selected text
- `Cmd+Ctrl+S`: Improve the selected text
- `F7` / `media_previous`: Remove non-printable characters from the selected text
- `Cmd+Ctrl+Q`: Quit the Typing Assistant

## Stop the App

- Press `Cmd+Ctrl+Q` while the assistant is running
- Or press `Ctrl+C` in the terminal where `./run_app.sh` is running

## Notes

- `./run_app.sh` creates the `venv` folder the first time and installs dependencies if needed.
- `./start_ollama.sh` starts the Ollama API server if it is not already running and pulls the configured model.
- The default model is `qwen3.5:0.8b`. You can change it in `main.py` or by setting `OLLAMA_MODEL` before running `./start_ollama.sh`.

## Troubleshooting

- If requests time out, wait for the model to finish loading and try again.
- If hotkeys do not work, grant Accessibility and Input Monitoring permissions in macOS settings.
- If Ollama is not reachable, verify the API is available at `http://127.0.0.1:11434`.
