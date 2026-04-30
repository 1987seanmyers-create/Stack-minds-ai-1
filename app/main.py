from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "StackMinds AI is running"}
