
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Serve static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Serve homepage
@app.get("/", response_class=HTMLResponse)
def read_root():
    with open("app/static/index.html") as f:
        return f.read()

# API route
@app.post("/api/run")
async def run_ai(req: Request):
    data = await req.json()
    user_input = data.get("input", "")

    return {
        "output": f"From chaos to clarity:\n\n{user_input}"
    }
