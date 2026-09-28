# Claude AI Chatbot

A simple chatbot built with [Streamlit](https://streamlit.io/) and the [Anthropic Python SDK](https://github.com/anthropics/anthropic). It sends your message to Claude Sonnet 4.6 and displays the conversation in a web app.

## Requirements

- Python 3.9 or later
- An Anthropic API key from the [Anthropic Console](https://console.anthropic.com/settings/keys)

## Setup

Open PowerShell in the project folder and install the dependencies:

```powershell
py -m pip install streamlit anthropic
```

Set your API key in the current PowerShell session. Replace the example with your key:

```powershell
$env:ANTHROPIC_API_KEY = "your-api-key-here"
```

Keep the key private. Do not put it in source code or commit it to Git. If a key has been committed or exposed, revoke it in the Anthropic Console and create a replacement.

## Run

From the project folder, start the app:

```powershell
py -m streamlit run chatbot.py
```

Streamlit will print a local URL (usually `http://localhost:8501`) to open in your browser. The API key must be set again in each new PowerShell session before starting the app.

## Project files

- `chatbot.py` — Streamlit interface and Claude API request.
- `.env` — Local secrets file, if used. It should not be committed. The app currently reads `ANTHROPIC_API_KEY` from the process environment; it does not load `.env` automatically.

