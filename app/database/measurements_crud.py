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
    rel = db.query(models.Measurement).filter(models.Measurement.id == id).first()
    if not rel:
        raise HTTPException(status_code=404, detail="Measurement not found")
    return rel


def delete_measurement_by_id(id: datetime.datetime, db: Session):
    rel = db.query(models.Measurement).filter(models.Measurement.id == id).first()
    if not rel:
        raise HTTPException(status_code=404, detail="Measurement not found")
    db.delete(rel)
    db.commit()
    return rel


# def create_measurement(id: int, measurement_in: SensorDataDB, db: Session):
#     rel = models.Measurement(**measurement_in.dict(), sensor_id=id)
#     db.add(rel)
#     db.commit()
#     db.refresh(rel)
#     return rel


# def create_measurement(id: int, measurement_in: SensorDataDB, db: Session):
#     rel = db.query(models.Sensor).filter(models.Sensor.id == id).first()
#     if not rel:
#         raise HTTPException(status_code=404, detail="Sensor not found")
#     measurement = models.Measurement(
#         sensor_id=id,
#         temperature=measurement_in,
#         timestamp=measurement_in.timestamp,
#     )
#     db.add(measurement)
#     db.commit()
#     db.refresh(measurement)
#     return measurement


def create_measurement(id: int, temperature_in: SensorDataDB, db: Session):
    mes = models.Measurement(**temperature_in.dict(), sensor_id=id)
    db.add(mes)
    db.commit()
    db.refresh(mes)
    return mes
