from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "StackMinds AI is running"}
app/static/index.html
app/static/style.css
app/static/app.js
app/static/manifest.webmanifest
app/static/service-worker.js
