## Create venv if not exists
python -m venv .venv

## Switch to created venv
source .venv/bin/activate

## Install dependencies
pip install -r agent/requirements.txt

## Update requirements.txt if you added new dependencies
pip3 freeze > requirements.txt

## To run project for debugging
```cmd
langgraph dev --debug-port 5678
```
## Required env variables
- LANGSMITH_API_KEY=your_key
- OPENAI_API_KEY=your_key
- LANGSMITH_TRACING=true
- WEB_PATH=https://zielonepatio.pl