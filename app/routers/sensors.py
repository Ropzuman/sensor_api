from datetime import datetime, time, timedelta

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database.database import get_db
from ..database.schemas import (
    AllSensors,
    DataDB,
    SectionBase,
    SensorBase,
    SensorData,
    SensorDB,
)
from ..database.sensors_crud import create_sensor  # add_measurement,
from ..database.sensors_crud import (
    get_all_sensors,
    read_sensor_by_id,
    read_sensor_by_name,
    read_sensor_by_section,
)

router = APIRouter(prefix="/Sensors")


@router.get("", response_model=list[AllSensors])
def read_sensors(name: str = "", db: Session = Depends(get_db)):
    if name != "":
        return read_sensor_by_name(db, name)
    return get_all_sensors(db)


@router.get("/section/{section}", response_model=list[SectionBase])
def read_sensors_by_section(section: str, db: Session = Depends(get_db)):
    return read_sensor_by_section(db, section)


@router.get("/{id}", response_model=SensorDB)
def read_sensors_by_id(id: int, db: Session = Depends(get_db)):
    return read_sensor_by_id(db, id)


@router.post("", response_model=SensorDB)
def create_sensors(sensor_in: SensorBase, db: Session = Depends(get_db)):
    return create_sensor(sensor_in, db)
