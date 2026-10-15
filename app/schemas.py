from datetime import date

from pydantic import BaseModel,Field

class PatientCreate(BaseModel):
    patient_id: str
    first_name: str
    last_name: str
    dob: date
    policy_id: str
    provider_name: str
    coverage_limit: int
    status: str

class ClaimCreate(BaseModel):
    claim_id: int
    patient_id: str
    diagnosis_code: str = Field(...,pattern=r"^[A-Z]\d{2}(\.\d{1,4})?$")
    claimed_amount: int
    clinical_notes: str

class AiRequest(BaseModel):
    diagnosis_code: str 
    clinical_notes: str

class RiskAssesment(BaseModel):
    risk_score: float
    risk_level: str
    audit_recommendation: str