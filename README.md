# Text Correction Assistant

## Overview

The Text Correction Assistant is a powerful tool designed to enhance your productivity by automatically correcting typographical errors, adjusting casing, and fixing punctuation in your text. Utilizing the advanced capabilities of the Ollama AI model server, this assistant provides real-time text correction through easy-to-use hotkeys.

## Getting Started

### Prerequisites

- Python 3.6 or later.
- Access to a command-line interface.
- Ollama AI Model Server for text processing.

### Step 1: Install Ollama

1. **Ollama Installation**: Follow the Ollama installation guide on the [official Ollama GitHub repository](https://github.com/ollama/ollama).
2. **Run Ollama with Mistral Model**:
   ```bash
   ollama run mistral:7b-instruct-v0.2-q4_K_S
   ```
   Note: Mistral 7B Instruct is recommended for its proficiency in text corrections. However, you're encouraged to experiment with other models.

### Step 2: Set Up Your Environment

1. **Clone the Project Repository** (replace `YourProjectURL` with the actual URL of your project):
   ```bash
   git clone YourProjectURL
   cd YourProjectDirectoryName
   ```
2. **Create and Activate a Python Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install Required Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Step 3: Run the Assistant

Execute the script to start the assistant:

```bash
python main.py
```

### Hotkeys

- **F9**: Corrects the current line of text.
- **F10**: Corrects the currently selected text.

### Troubleshooting

- **Accessibility Permissions**: On macOS, you might encounter an error regarding accessibility permissions. Ensure that your script (or the IDE/terminal running it) is granted the necessary permissions in the system settings under Security & Privacy > Accessibility and Input Monitoring.
- **Key Bindings**: The default key bindings are set for macOS (using `Cmd` key). For Windows or Linux, you may need to modify the script to use the `Ctrl` key instead of `Cmd`.

## Customization

You can customize the hotkeys, prompt templates, and Ollama configuration within the code to suit your preferences or specific tasks. Example prompt templates are provided in the script for easy adjustments.

---

Replace `YourProjectURL` and `YourProjectDirectoryName` with your project's actual repository URL and directory name, respectively. This README provides a comprehensive guide for users to set up and start using the Text Correction Assistant.