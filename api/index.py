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

# Grade point mapping
grade_point = {
    "AA": 10, "AB": 9, "BB": 8, "BC": 7,
    "CC": 6, "CD": 5, "DD": 4, "FP": 0
}

# Subject credits
credits = {
    "CST202": 3, "CST204": 3, "CST206": 3, "CST208": 3,
    "ECE2126": 3, "MAT202": 3,
    "CSP202": 1, "CSP204": 2, "CSP206": 1,
    "CSP210": 1, "OTP202": 2
}

# Load student data
with open("data.json") as f:
    student_data = json.load(f)

@app.get("/api")
def get_result(name: str = Query(...)):
    if name not in student_data:
        return {"error": "Student ID not found"}
    
    grades = student_data[name]
    total = 0
    for subject, grade in grades.items():
        total += credits[subject] * grade_point.get(grade, 0)
    
    sgpa = round(total / 25, 2)
    
    return {
        "Student ID": name,
        "Subjects": grades,
        "SGPA": sgpa
    }
