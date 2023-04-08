from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database.database import get_db
from ..database.schemas import AllSensors, DataDB, SensorBase, SensorData, SensorDB
from ..database.sensors_crud import create_sensor  # add_measurement,
from ..database.sensors_crud import (
    get_all_sensors,
    read_sensor_by_id,
    read_sensor_by_section,
)

router = APIRouter(prefix="/Sensors")


@router.get("", response_model=list[AllSensors])
def read_sensors(section: str = "", db: Session = Depends(get_db)):
    if section != "":
        return read_sensor_by_section(db, section)
    return get_all_sensors(db)


@router.get("/{id}", response_model=SensorDB)
def read_sensors_by_id(id: int, db: Session = Depends(get_db)):
    return read_sensor_by_id(db, id)


@router.post("", response_model=SensorDB)
def create_sensors(sensor_in: SensorBase, db: Session = Depends(get_db)):
    return create_sensor(sensor_in, db)


# @router.post("/{id}", response_model=DataDB)
# def add_measurement_for_sensor(
#     id: int, measurement: SensorData, db: Session = Depends(get_db)
# ):
#     return add_measurement(db, id, measurement)
