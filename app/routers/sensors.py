from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database.database import get_db
from ..database.schemas import AllSensors, SensorBase, SensorData, SensorDB
from ..database.sensors_crud import (
    create_sensor,
    get_all_sensors,
    read_sensor_by_id,
    read_sensor_by_section,
)

router = APIRouter(prefix="/Sensors")


@router.get("", response_model=AllSensors)
def read_sensors(id: int = 0, db: Session = Depends(get_db)):
    if id != 0:
        return read_sensor_by_id(db, id)
    return get_all_sensors(db)


@router.get("/{id}", response_model=SensorDB)
def read_sensors_by_id(id: int, db: Session = Depends(get_db)):
    return read_sensor_by_id(db, id)


@router.get("/{section}", response_model=SensorDB)
def read_sensors_by_section(section: str, db: Session = Depends(get_db)):
    return read_sensor_by_section(db, section)


@router.post("", response_model=SensorDB)
def create_sensors(sensor: SensorBase, db: Session = Depends(get_db)):
    return create_sensor(db, sensor)


@router.post("/{id}", response_model=SensorDB)
def add_measurement(id: int, measurement: SensorData, db: Session = Depends(get_db)):
    return add_measurement(id, measurement, db)
