from fastapi import FastAPI
from app.models import Patient,Claim,create_db_and_tables
from app.database import SessionDep


app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
def root():
    return {"status":"Backend is awake!"}

@app.post("/patientcreate")
def patient_create(patient : Patient,session : SessionDep):
    patient=Patient.model_validate(patient)
    session.add(patient)
    session.commit()
    session.refresh(patient)
    return {"name": patient.first_name}

@app.post("/claimcreate")
def claim_create(claim : Claim,session : SessionDep):
    session.add(claim)
    session.commit()
    session.refresh(claim)
    return {"name": claim.claim_id}