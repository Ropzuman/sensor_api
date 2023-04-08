from fastapi import HTTPException
from sqlalchemy.orm import Session

from . import models
from .schemas import SensorBase, SensorDB


def get_all_sensors(db: Session):
    return db.query(models.Sensor).all()


def read_sensor_by_id(db: Session, sensor_id: int):
    sensor = db.query(models.Sensor).filter(models.Sensor.id == sensor_id).first()
    if sensor is None:
        raise HTTPException(status_code=404, detail="Sensor not found")
    return sensor


def read_sensor_by_section(db: Session, section: str):
    sensor = db.query(models.Sensor).filter(models.Sensor.section == section).first()
    if sensor is None:
        raise HTTPException(status_code=404, detail="Sensor not found")
    return sensor


def create_sensor(db: Session, sensor: SensorBase):
    sensor = models.Sensor(section=sensor.section, status=sensor.status)
    db.add(sensor)
    db.commit()
    db.refresh(sensor)
    return sensor
