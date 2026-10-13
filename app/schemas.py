from datetime import date

from pydantic import BaseModel

class UserCreate(BaseModel):
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
    diagnosis_code: str
    claimed_amount: int
    clinical_notes: str

    