from pydantic import BaseModel
import uuid

class PatientRegistrationResponse(BaseModel):
    patient_id: uuid.UUID
    patient_first_name: str
    patient_second_name: str
    patient_address: str
    patient_registration_date: str

class RegistrationYears(BaseModel):
    patients: int
    year: int

class RegistrationMonths(BaseModel):
    patients: int
    month: str

class CurrentDayPatients(BaseModel):
    patients: int

class LivePatientsCount(BaseModel):
    total_patients: int