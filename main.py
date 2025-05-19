from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import json
from pathlib import Path
from typing import List

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load student marks
with open("q-vercel-python.json", "r") as f:
    data = json.load(f)

@app.get("/api")
async def get_marks(name: List[str] = []):
    marks = [data.get(n, None) for n in name]
    return {"marks": marks}
