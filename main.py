from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json
from typing import List

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],          # Allow all HTTP methods
    allow_headers=["*"],          # Allow all headers
)

# Load student marks data from JSON file
with open("q-vercel-python.json") as f:
    students = json.load(f)

marks_dict = {student["name"]: student["marks"] for student in students}

@app.get("/api")
def get_marks(name: List[str] = Query(...)):
    # Return marks for each requested name; 0 if not found
    result = [marks_dict.get(n, 0) for n in name]
    return {"marks": result}
