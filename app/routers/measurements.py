from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from ..database import measurements_crud as crud
from ..database.database import engine, get_db
from ..database.schemas import DataDB, MeasurementDelete, SensorDataDB

router = APIRouter(prefix="/Measurements")


# Get all measurements
@router.get("/", response_model=list[DataDB])
def get_measurements(db: Session = Depends(get_db)):
    measurements = crud.get_all_measurements(db)
    if not measurements:
        raise HTTPException(status_code=404, detail="No measurements found")
    return measurements


# Add a measurement
@router.post("/{id}/measurements", response_model=DataDB)
def add_measurement(
    id: int, temperature_in: SensorDataDB, db: Session = Depends(get_db)
):
    try:  # Create the measurement
        measurement = crud.create_measurement(id, temperature_in, db)
        return measurement
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# Delete a measurement
@router.delete("/{id}", response_model=MeasurementDelete)
def delete_measurements_by_id(id: int, db: Session = Depends(get_db)):
    return crud.delete_measurement_by_id(id, db)
