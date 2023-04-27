from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import models
from ..database.database import engine, get_db
from ..database.schemas import (
    AllSensors,
    SectionDB,
    SectionPatchDB,
    SensorBase,
    SensorDB,
    SensorPatchDB,
    StatusChanges,
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
    read_sensor_status_changes,
    update_sensor,
    update_status,
)

router = APIRouter(prefix="/Sensors")


@router.get("", response_model=list[AllSensors])
def read_sensors(name: str = "", db: Session = Depends(get_db)):
    return get_all_sensors(db)


@router.get("/section/{section}", response_model=list[SectionDB])
def read_sensors_by_section(section: str, db: Session = Depends(get_db)):
    return read_sensor_by_section(section, db)


@router.get("/{status}", response_model=list[SensorBase])
def read_sensors_by_status(status: str, db: Session = Depends(get_db)):
    return read_sensor_by_status(status, db)


@router.get("/sensor/{name}", response_model=list[SensorDB])
def read_sensors_by_name(name: str, db: Session = Depends(get_db)):
    return read_sensor_by_name(name, db)


@router.get("/{status}", response_model=list[StatusChanges])
def get_sensor_status_changes(name: str, db: Session = Depends(get_db)):
    return read_sensor_status_changes(name, db)


@router.post("", response_model=SensorDB)
def create_sensors(sensor_in: SensorBase, db: Session = Depends(get_db)):
    return create_sensor(sensor_in, db)


@router.patch("/{section}")
def update_sensors(
    name: str, sensorbase: SectionPatchDB, db: Session = Depends(get_db)
):
    return update_sensor(name, sensorbase, db)


@router.patch("/status/{name}")
def update_sensors_status(
    name: str, statusdb: StatusPatchDB, db: Session = Depends(get_db)
):
    return update_status(name, statusdb, db)
