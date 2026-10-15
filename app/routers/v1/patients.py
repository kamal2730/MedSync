from fastapi import APIRouter

from app.database import SessionDep
from app.models import Patient

router=APIRouter(prefix="/patients")

@router.post("/create")
def patient_create(patient : Patient,session : SessionDep):
    patient=Patient.model_validate(patient)
    session.add(patient)
    session.commit()
    session.refresh(patient)
    return {"name": patient.first_name}