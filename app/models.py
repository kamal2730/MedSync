from fastapi import Depends
from sqlmodel import SQLModel,Field
from datetime import date
from app.database import engine

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


class Patient(SQLModel,table=True):
    __tablename__ = "patients"
    patient_id: str = Field(primary_key=True)
    first_name: str 
    last_name: str 
    dob: date 
    policy_id: str 
    provider_name: str 
    coverage_limit: int  
    status: str 

class Claim(SQLModel,table=True):
    __tablename__ = "claims"
    claim_id: int = Field(primary_key=True)
    patient_id: str = Field(foreign_key="patients.patient_id")
    diagnosis_code: str = Field(...,schema_extra={"pattern": r"^[A-Z]\d{2}(\.\d{1,4})?$"})
    claimed_amount: int 
    clinical_notes: str 
    risk_score: str