import json
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the existing JSON
with open("public/passport-index-map.json", "r") as f:
    visa_data = json.load(f)

class VisaQuery(BaseModel):
    passport: str  # ISO code (e.g., "AFG")
    destination: str  # ISO code (e.g., "ALB")

@app.post("/get-visa-info")
def get_visa_info(query: VisaQuery):
    passport = query.passport.upper()
    destination = query.destination.upper()

    try:
        requirement = visa_data[passport][destination]
        return {"requirement": requirement}
    except KeyError:
        raise HTTPException(status_code=404, detail="Country data not found.")
