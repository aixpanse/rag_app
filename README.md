## Create venv if not exists
```cmd
python -m venv .venv
```

## Switch to created venv
```cmd
source .venv/bin/activate
```

## Install dependencies
```cmd
pip install -r agent/requirements.txt
```

## Update requirements.txt if you added new dependencies
```cmd
pip3 freeze > requirements.txt
```

## To run project for debugging
```cmd
langgraph dev --debug-port 5678
```
## Required env variables
- LANGSMITH_API_KEY=your_key
- OPENAI_API_KEY=your_key
- LANGSMITH_TRACING=true

## Build docker image
```cmd
langgraph build -t aixpanse/rag_app --platform linux/amd64
```

## Push to docker registry
```cmd
docker push aixpanse/rag_app
```
