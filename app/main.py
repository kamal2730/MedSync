from fastapi import FastAPI
from app.schemas import UserCreate,ClaimCreate

app = FastAPI()

@app.post("/usercreate")
def user_create(user : UserCreate):
    return {"name": user.first_name}

@app.post("/claimcreate")
def claim_create(claim : ClaimCreate):
    return {"name": claim.claim_id}