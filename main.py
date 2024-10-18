import time
import logging
import httpx
from rich.console import Console
from string import Template
from pynput import keyboard
from pynput.keyboard import Key, Controller
import pyperclip
import time

from templates import CORRECT_TEXT_TEMPLATE, IMPROVE_TEXT_TEMPLATE, CORRECT_TEXT_V2_TEMPLATE 

console = Console()

# Initialize controller for keyboard actions
controller = Controller()

# Setup basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# OLLAMA API configuration
OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
OLLAMA_CONFIG = {
    #"model": "mistral:7b-instruct-v0.2-q4_K_S",
    "model": "llama3.2",
    "keep_alive": "15m",
    "stream": False,
    "options":{
        "temperature": 0.5,
    },
}



def suggest_improvements(text):
    """Sends text for stylistic improvements."""
    prompt = CORRECT_TEXT_V2_TEMPLATE.substitute(text=text)
    console.log("Sending data to API...", style="bold magenta")
    response = httpx.post(
        OLLAMA_ENDPOINT,
        json={"prompt": prompt, **OLLAMA_CONFIG},
        headers={"Content-Type": "application/json"},
        timeout=60,
    )
    if response.status_code != 200:
        logging.error("Error %s", response.status_code)
        return None
    console.log("Data received. Processing...", style="bold green")
    return response.json()["response"].strip()

def fix_text(text):
    """Corrects typos and grammatical errors in text."""
    console.log("Sending data to API...", style="bold magenta")
    prompt = IMPROVE_TEXT_TEMPLATE.substitute(text=text)
    response = httpx.post(
        OLLAMA_ENDPOINT,
        json={"prompt": prompt, **OLLAMA_CONFIG},
        headers={"Content-Type": "application/json"},
        timeout=30,
    )
    if response.status_code != 200:
        logging.error("Error %s", response.status_code)
        return None
    console.log("Data received. Processing...", style="bold green")
    return response.json()["response"].strip()

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

# Setup global hotkeys
with keyboard.GlobalHotKeys({
    "<101>": on_f9,
    "<109>": on_f10,
    '<cmd>+<ctrl>+s': on_cmd_ctrl_s
}) as hotkeys:
    hotkeys.join()
