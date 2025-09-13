from api.db import db


async def get_yearly_patients_service():
    try:
        result = await db.get_yearly_patients()
    except Exception as e:
        message = "Exception occured while fetching data from database"
        print(message)
        raise Exception(message)
    result = [res for res in result]
    return result


async def get_monthly_patients_service():
    try:
        result = await db.get_monthly_patients()
    except Exception as e:
        message = "Exception occured while fetching data from database"
        print(message)
        raise Exception(message)
    result = [res for res in result]
    return result


async def get_current_day_patients_service():
    try:
        result = await db.get_current_day_patients()
    except Exception as e:
        message = "Exception occured while fetching data from database"
        print(e)
        raise Exception(message)
    result = next(result, {"patients": 0})
    return result

async def get_live_patients_count_service():
    try:
        result = await db.get_live_patients()
    except Exception as e:
        message = "Exception occured while fetching data from database"
        print(e)
        raise Exception(message)
    result = {"total_patients": result}
    return result