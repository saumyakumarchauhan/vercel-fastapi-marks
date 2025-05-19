from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load JSON data
with open("q-vercel-python.json") as f:
    data = json.load(f)

name_to_marks = {entry["name"]: entry["marks"] for entry in data}

@app.get("/api")
def get_marks(name: list[str] = Query(...)):
    result = [name_to_marks.get(n, 0) for n in name]
    return {"marks": result}
