from datetime import datetime, time, timedelta

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import models
from ..database.database import engine, get_db
from ..database.schemas import (
    AllSensors,
    DataDB,
    SectionDB,
    SensorBase,
    SensorData,
    SensorDB,
    SensorPatchDB,
    StatusData,
    StatusDB,
    StatusPatchDB,
)
from ..database.sensors_crud import (
    create_sensor,
    get_all_sensors,
    read_sensor_by_name,
    read_sensor_by_section,
    read_sensor_by_status,
    update_sensor,
    update_status,
)

router = APIRouter(prefix="/Sensors")


@router.get("", response_model=list[AllSensors])
def read_sensors(name: str = "", db: Session = Depends(get_db)):
    if name != "":
        return read_sensor_by_name(db, name)
    return get_all_sensors(db)


@router.get("/section/{section}/{timestamp}", response_model=list[SectionDB])
def read_sensors_by_section(section: str, db: Session = Depends(get_db)):
    return read_sensor_by_section(section, db)


@router.get("/status/{status}", response_model=list[StatusDB])
def read_sensors_by_status(status: str, db: Session = Depends(get_db)):
    return read_sensor_by_status(status, db)


@router.post("", response_model=SensorDB)
def create_sensors(sensor_in: SensorBase, db: Session = Depends(get_db)):
    return create_sensor(sensor_in, db)


@router.patch("/{name}")
def update_sensors(name: str, sensorbase: SensorPatchDB, db: Session = Depends(get_db)):
    return update_sensor(name, sensorbase, db)


@router.patch("/status/{name}")
def update_sensors_status(
    name: str, statusdb: StatusPatchDB, db: Session = Depends(get_db)
):
    return update_status(name, statusdb, db)
