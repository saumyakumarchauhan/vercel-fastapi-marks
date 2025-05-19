from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import json
from typing import List

app = FastAPI()

# Enable CORS for all origins and GET methods
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load marks data from JSON file once at startup
with open("q-vercel-python.json", "r") as f:
    data = json.load(f)

# data assumed to be a list of objects: [{"name": "X", "marks": 10}, ...]
# create a dict for fast lookup
marks_dict = {student['name']: student['marks'] for student in data}

@app.get("/api")
def get_marks(name: List[str] = Query(...)):
    # return marks in same order as requested names
    results = []
    for n in name:
        results.append(marks_dict.get(n, None))  # or 0 if you want a default
    return JSONResponse(content={"marks": results})
