from fastapi import HTTPException
from sqlalchemy.orm import Session

from . import models
from .schemas import SensorBase, SensorData


def get_all_sensors(db: Session):
    return db.query(models.Sensor).all()


def read_sensor_by_id(db: Session, id: int):
    sensor = db.query(models.Sensor).filter(models.Sensor.id == id).first()
    if sensor is None:
        raise HTTPException(status_code=404, detail="Sensor not found")
    return sensor


def read_sensor_by_section(db: Session, section: str):
    sensor = db.query(models.Sensor).filter(models.Sensor.section == section).all()

    if sensor is None:
        raise HTTPException(status_code=404, detail="Sensor not found")
    return sensor


def create_sensor(sensor_in: SensorBase, db: Session):
    sensor = models.Sensor(**sensor_in.dict())
    db.add(sensor)
    db.commit()
    db.refresh(sensor)
    return sensor


# def add_measurement(db: Session, id: int, measurement: SensorData):
#     rel = models.Measurement(**measurement.dict(), sensor_id=id)
#     db.add(rel)
#     db.commit()
#     db.refresh(rel)
#     return rel
