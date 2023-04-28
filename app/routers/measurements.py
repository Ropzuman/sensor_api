import datetime

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from ..database import measurements_crud as crud
from ..database import models
from ..database.database import engine, get_db
from ..database.schemas import DataDB, MeasurementDelete, SensorData, SensorDataDB

router = APIRouter(prefix="/Measurements")


@router.get("/", response_model=list[DataDB])
def get_measurements(db: Session = Depends(get_db)):
    return crud.get_all_measurements(db)


@router.post("/{id}/measurements", response_model=DataDB)
def add_measurement(
    id: int, temperature_in: SensorDataDB, db: Session = Depends(get_db)
):
    return crud.create_measurement(id, temperature_in, db)


@router.delete("/{id}", response_model=MeasurementDelete)
def delete_measurements_by_id(id: int, db: Session = Depends(get_db)):
    return crud.delete_measurement_by_id(id, db)
