from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Grade points mapping
grade_points = {
    "AA": 10, "AB": 9, "BB": 8,
    "BC": 7, "CC": 6, "CD": 5,
    "DD": 4, "FP": 0
}

# Credits per subject
credits = {
    "CST202": 3, "CST204": 3, "CST206": 3, "CST208": 3,
    "ECT212": 3, "MAT202": 3,
    "CSP202": 1, "CSP204": 2, "CSP206": 1, "CSP210": 1, "OTP202": 2
}

# Load the student data
with open("data.json", "r") as f:
    student_data = json.load(f)

@app.get("/api")
def get_student_result(name: str = Query(...)):
    entry = student_data.get(name)
    if not entry:
        return {"error": "Student ID not found"}

    total_points = 0
    total_credits = 0

    for subject, grade in entry.items():
        if subject == "SGPA" or not grade:
            continue
        point = grade_points.get(grade)
        if point is not None:
            credit = credits.get(subject, 0)
            total_points += credit * point
            total_credits += credit

    sgpa = round(total_points / 25, 2) if total_credits == 25 else ""

    # Return the original grades and the SGPA
    return {
        "Student ID": name,
        "Grades": entry,
        "SGPA": sgpa
    }
