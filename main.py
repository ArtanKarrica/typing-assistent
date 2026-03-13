import os
import logging
import time
import httpx
import pyperclip
from pynput import keyboard
from pynput.keyboard import Controller, Key
from rich.console import Console

from templates import CORRECT_TEXT_TEMPLATE, CORRECT_TEXT_V2_TEMPLATE, SYSTEM_PROMPT_TEMPLATE

console = Console()

# Initialize controller for keyboard actions
controller = Controller()

# Setup basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# OLLAMA API configuration
# Use IPv4 loopback by default to avoid localhost resolving to ::1 on macOS.
OLLAMA_ENDPOINT = os.getenv("OLLAMA_ENDPOINT", "http://127.0.0.1:11434/api/generate")
OLLAMA_CONFIG = {
    "model": "qwen3.5:0.8b",
    #"model": "deepseek-r1:8b",
    "keep_alive": "15m",
    "think": False,
    "stream": False,
    "system": SYSTEM_PROMPT_TEMPLATE.substitute(),
    "options":{
        "temperature": 0.5,
    },
}


def send_prompt(prompt, timeout):
    """Sends a prompt to Ollama and returns the response text."""
    console.log("Sending data to API...", style="bold magenta")

    try:
        response = httpx.post(
            OLLAMA_ENDPOINT,
            json={"prompt": prompt, **OLLAMA_CONFIG},
            headers={"Content-Type": "application/json"},
            timeout=timeout,
        )
        response.raise_for_status()
        payload = response.json()
        result = payload.get("response", "").strip()
    except httpx.ConnectError:
        logging.error(
            "Could not connect to Ollama at %s. Start Ollama with 'ollama serve' and ensure the model is available.",
            OLLAMA_ENDPOINT,
        )
        console.print(
            f"[bold red]Ollama is not reachable at {OLLAMA_ENDPOINT}.[/bold red] "
            "Start it with [cyan]ollama serve[/cyan]."
        )
        return None
    except httpx.ReadTimeout:
        logging.error(
            "Ollama timed out after %ss at %s. The model may still be loading or generating.",
            timeout,
            OLLAMA_ENDPOINT,
        )
        console.print(
            f"[bold red]Ollama timed out after {timeout}s.[/bold red] "
            "If this is the first request, let the model load once or increase the timeout."
        )
        return None
    except httpx.HTTPStatusError as exc:
        logging.error("Ollama returned HTTP %s: %s", exc.response.status_code, exc.response.text)
        console.print(f"[bold red]Ollama returned HTTP {exc.response.status_code}.[/bold red]")
        return None
    except (httpx.HTTPError, ValueError) as exc:
        logging.error("Unexpected Ollama error: %s", exc)
        console.print("[bold red]Failed to process the Ollama response.[/bold red]")
        return None

    if not result:
        logging.error("Ollama response did not include any text: %s", payload)
        console.print("[bold red]Ollama returned an empty response.[/bold red]")
        return None

    console.log("Data received. Processing...", style="bold green")
    return result


def suggest_improvements(text):
    """Sends text for stylistic improvements."""
    prompt = CORRECT_TEXT_V2_TEMPLATE.substitute(text=text)
    return send_prompt(prompt, timeout=120)

def fix_text(text):
    """Corrects typos and grammatical errors in text."""
    prompt = CORRECT_TEXT_TEMPLATE.substitute(text=text)
    return send_prompt(prompt, timeout=90)

def fix_current_line():
    """Selects and fixes the current line."""
    # Shortcut to select the current line
    controller.press(Key.cmd)
    controller.press(Key.shift)
    controller.press(Key.left)
    controller.release(Key.left)
    controller.release(Key.shift)
    controller.release(Key.cmd)
    fix_selection()

def fix_selection():
    """Fixes the currently selected text."""
    # Copy selection to clipboard
    with controller.pressed(Key.cmd):
        controller.tap('c')
    time.sleep(0.1)  # Allow time for clipboard to update

    text = pyperclip.paste()
    if not text:
        return

    fixed_text = fix_text(text)
    if not fixed_text:
        return

    console.print(f"[cyan]Fixed text response: {fixed_text}.")
    pyperclip.copy(fixed_text)
    time.sleep(0.1)  # Allow time for clipboard to update

    # Paste the fixed text
    with controller.pressed(Key.cmd):
        controller.tap('v')

def fix_selection_with_improvements():
    """Improves and replaces the selected text."""
    # Copy selection to clipboard
    with controller.pressed(Key.cmd):
        controller.tap('c')
    time.sleep(0.1)  # Allow time for clipboard to update

    text = pyperclip.paste()
    if not text:
        return

    improved_text = suggest_improvements(text)
    if not improved_text:
        return
    console.print(f"[cyan]Fixed text response: {improved_text}.")
    pyperclip.copy(improved_text)
    time.sleep(0.1)  # Allow time for clipboard to update

    # Paste the improved text
    with controller.pressed(Key.cmd):
        controller.tap('v')

def on_f9():
    """Handler for F9 key press."""
    fix_current_line()

def on_f10():
    """Handler for F10 key press."""
    fix_selection()

def on_cmd_ctrl_s():
    """Handler for Cmd+Ctrl+S key combination."""
    fix_selection_with_improvements()

def remove_non_printable_selection():
    """Removes non-printable chars from the current selection."""
    # Copy current selection
    with controller.pressed(Key.cmd):
        controller.tap('c')
    time.sleep(0.1)

    text = pyperclip.paste()
    if not text:
        return

    # Filter out everything except tab, LF, CR, and printable ASCII
    cleaned = ''.join(
        ch for ch in text
        if 32 <= ord(ch) <= 126 or ch in ('\t', '\n', '\r')
    )

    console.log("Non-printables removed.", style="bold yellow")
    pyperclip.copy(cleaned)
    time.sleep(0.1)

    # Paste the cleaned text back
    with controller.pressed(Key.cmd):
        controller.tap('v')

def quit_app():
    """Stops the application listener."""
    console.print("[bold yellow]Stopping Typing Assistant...[/bold yellow]")
    return False


def main():
    """Starts the global hotkey listener."""
    console.print("[bold green]Typing Assistant is running.[/bold green]")
    console.print("Hotkeys: F9 fix line, F10 fix selection, Cmd+Ctrl+S improve, Cmd+Ctrl+Q quit.")

    with keyboard.GlobalHotKeys({
        "<101>": on_f9,                    # F9 → fix_current_line
        "<109>": on_f10,                   # F10 → fix_selection
        '<cmd>+<ctrl>+s': on_cmd_ctrl_s,   # Cmd+Ctrl+S → improve selection
        '<cmd>+<ctrl>+q': quit_app,        # Cmd+Ctrl+Q → quit app
        "<media_previous>": remove_non_printable_selection,  # F7 → strip non-printables
    }) as hotkeys:
        hotkeys.join()


if __name__ == "__main__":
    main()
