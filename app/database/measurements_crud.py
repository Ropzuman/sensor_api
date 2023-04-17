import datetime

from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from . import models
from .schemas import (
    DataDB,
    DataIn,
    SensorBase,
    SensorData,
    SensorDataDB,
    SensorDB,
    StatusDB,
)


def get_all_measurements(db: Session):
    rels = db.query(models.Measurement).all()
    return rels


def get_measurement_by_id(db: Session, id: int):
    rel = db.query(models.Measurement).filter(models.Measurement.id == id).all()
    if not rel:
        raise HTTPException(status_code=404, detail="Measurement not found")
    return rel


def delete_measurement_by_id(id: datetime.datetime, db: Session):
    rel = db.query(models.Measurement).filter(models.Measurement.id == id).all()
    if not rel:
        raise HTTPException(status_code=404, detail="Measurement not found")
    db.delete(rel)
    db.commit()
    return rel


def create_measurement(id: int, temperature_in: SensorDataDB, db: Session):
    mes = models.Measurement(**temperature_in.dict(), sensor_id=id)
    db.add(mes)
    db.commit()
    db.refresh(mes)
    return mes


def read_sensor_by_name(db: Session, name: str):
    sensor = db.query(models.Sensor).filter(models.Sensor.name == name).first()

    if sensor is None:
        raise HTTPException(status_code=404, detail="Sensor not found")
    return sensor
