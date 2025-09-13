from fastapi import APIRouter, status
from api.response_schema.patient_registration import (
    PatientRegistrationResponse, RegistrationYears, RegistrationMonths, CurrentDayPatients,
    LivePatientsCount,
)
from typing import Optional
import uuid
from fastapi import HTTPException

# Service imports
from api.services.patient_registration_service import (
    get_yearly_patients_service, get_monthly_patients_service, get_current_day_patients_service,
    get_live_patients_count_service
)


router = APIRouter()

@router.get(
    path="/patient_registration/yearly",
    response_model= list[RegistrationYears],
    tags=["Patient Registration"],
    status_code=status.HTTP_200_OK
)
async def get_yearly_patient_registrations():
    try:
        yearly_patients = await get_yearly_patients_service()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "detail": f"Error - {e.args[0]}"
            }
        )
    return yearly_patients

     

@router.get(
    "/patient_registration/monthly",
    response_model= list[RegistrationMonths],
    tags=["Patient Registration"],
    status_code=status.HTTP_200_OK
)
async def get_monthly_patient_registrations():
    try:
        monthly_patients = await get_monthly_patients_service()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={
                "detail": f"Error - {e.args[0]}"
            }
        )
    return monthly_patients
    

@router.get(
    "/patient_registration/today",
    response_model= CurrentDayPatients,
    tags=["Patient Registration"],
    status_code=status.HTTP_200_OK
)
async def get_current_day_patient_registrations():
    try:
        current_day_patients = await get_current_day_patients_service()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={
                "detail": f"Error - {e.args[0]}"
            }
        )
    return current_day_patients


@router.get(
    "/patient_registration/live",
    response_model= LivePatientsCount,
    tags=["Patient Registration"],
    status_code=status.HTTP_200_OK
)
async def get_live_patient_registrations():
    try:
        live_patients = await get_live_patients_count_service()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={
                "detail": f"Error - {e.args[0]}"
            }
        )
    return live_patients