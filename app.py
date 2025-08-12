from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow your Lovable site to call this API from the browser.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # later you can restrict to your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/analyze")
def analyze(payload: dict):
    text = payload.get("text", "")
    # TODO: your business logic goes here
    return {"length": len(text), "message": "analyzed"}
