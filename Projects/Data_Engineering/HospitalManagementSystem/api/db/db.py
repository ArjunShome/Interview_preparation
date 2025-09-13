from api.dbcon import db

async def get_yearly_patients():
    # Similar SQL Query - select date(year, Date)as year, patients_registed FROM new_registrations_patient_window_agg
    results = db.new_registrations_patient_window_agg.aggregate(
        [
            {
                "$group": {
                    "_id": {
                        "year": {"$year": "$Date"}
                    },
                    "patients": {
                        "$sum": "$patients_registered"
                    }
                }
            },
            {
                "$project": {
                    "year": "$_id.year", "patients": 1, "_id": 0
                }
            }
        ]
    )
    return results


async def get_monthly_patients():
    # Similar SQL Query - select date(month, Date), sum(patients) from new_registration_patient_window_agg group by date(month, Date)
    results = db.new_registrations_patient_window_agg.aggregate(
        [
            {
                "$group": {
                    "_id": {
                        "month": {
                            "$dateToString": {"format": "%B", "date": "$Date"}
                        }
                    },
                    "patients": {
                        "$sum": "$patients_registered"
                    }
                }
            }, 
            {
                "$project": {
                    "month": "$_id.month", "patients": 1, "_id": 0
                }
            }
        ]
    )
    return results

async def get_current_day_patients():
    results = db.new_registrations_patient_window_agg.aggregate(
        [
            {
                "$match": {
                    "$expr": {
                        "$eq": [
                            {"$dateTrunc": {"date": "$Date", "unit": "day", "timezone": "UTC"}},
                            {"$dateTrunc": {"date": "$$NOW", "unit": "day", "timezone": "UTC"}}
                        ]
                    }
                }
            },
            {
                "$group": {
                    "_id": None,
                    "patients": {"$sum": "$patients_registered"}
                }
            },
            {"$project": {"_id": 0, "patients": 1}}
        ]
    )
    return results


async def get_live_patients():
    results = db.new_registrations_patient.count_documents({})
    return results