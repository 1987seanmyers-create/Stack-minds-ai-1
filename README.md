# StackMinds AI

**From chaos to clarity**

A runnable prototype that turns a messy idea into a structured plan using a small AI team:
- **Breakdown**
- **Expansion**
- **Simplified Plan**
- **Your Plan** (final synthesis)

## What is included
- FastAPI backend
- Branded frontend UI
- Mock mode out of the box
- Optional live OpenAI mode with an API key
- JSON run history for basic persistence

## Quick start

### 1) Create and activate a virtual environment

**macOS / Linux**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows (PowerShell)**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 2) Install dependencies
```bash
pip install -r requirements.txt
```

### 3) Optional: enable live OpenAI mode
Copy `.env.example` to `.env` and set your API key.

**macOS / Linux**
```bash
cp .env.example .env
export $(cat .env | xargs)
```

**Windows (PowerShell)**
```powershell
copy .env.example .env
$env:OPENAI_API_KEY="your_openai_api_key_here"
$env:OPENAI_MODEL="gpt-4.1-mini"
```

If you do not set an API key, the app runs in **demo mock mode**.

### 4) Run the app
```bash
uvicorn app.main:app --reload
```

Open:
- `http://127.0.0.1:8000`

## API
### POST `/api/run`
Request body:
```json
{
  "idea": "I want to launch a local clothing brand.",
  "context": "Budget is low and I need a 30-day plan."
}
```

## Project structure
```text
stackminds_ai/
├── app/
│   ├── main.py
│   ├── data/
│   │   └── runs.json
│   └── static/
│       ├── app.js
│       ├── index.html
│       └── styles.css
├── .env.example
├── README.md
└── requirements.txt
```

## Notes
- `app/data/runs.json` stores the last 100 runs.
- This is a prototype, not a hardened production deployment.
- The backend serves the frontend directly for simple posting and demo use.

## What to post with it
Use this line:

> **StackMinds AI — From chaos to clarity**  
> Turn any messy idea into a structured, actionable plan with an AI team.


## Deploy it as a live website
### Render backend + full web app
This repo includes `render.yaml` so you can deploy the FastAPI app directly on Render.

Basic flow:
1. Push this folder to GitHub.
2. Create a new Render Web Service from the repo.
3. Render will install `requirements.txt` and start Uvicorn using `render.yaml`.
4. Set `OPENAI_API_KEY` in Render if you want live model output.

## Make it installable as a PWA
This repo now includes:
- `app/static/manifest.webmanifest`
- `app/static/sw.js`
- app icons

Once deployed over HTTPS, supported browsers can install it to the home screen.

## Wrap it as an Android app
See `android-wrapper/README.md`.
The simplest path is:
1. Deploy StackMinds online first.
2. Use Capacitor to point a native Android shell at that deployed URL.
3. Open the Android project in Android Studio and build the APK.
