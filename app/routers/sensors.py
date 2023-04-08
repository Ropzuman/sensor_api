from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database.database import get_db
from ..database.schemas import AllSensors, SensorBase, SensorData, SensorDB
from ..database.sensors_crud import (
    create_sensor,
    get_all_sensors,
    get_sensor_by_section,
    read_sensor_by_id,
)

router = APIRouter(prefix="/measurements")


@router.get("/", response_model=AllSensors)
def get_all_sensors(db: Session = Depends(get_db)):
    return get_all_sensors(db)


@router.get("/{id}", response_model=SensorDB)
def read_sensor_by_id(id: int, db: Session = Depends(get_db)):
    return read_sensor_by_id(id, db)
