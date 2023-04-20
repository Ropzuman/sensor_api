import datetime

from fastapi import HTTPException, Query
from fastapi.encoders import jsonable_encoder
from sqlalchemy import desc, func
from sqlalchemy.orm import Session

from . import models
from .schemas import (
    DataDB,
    DataIn,
    SectionDB,
    SensorBase,
    SensorData,
    SensorDataDB,
    SensorDB,
    StatusDB,
)


def get_all_measurements(db: Session):
    rels = db.query(models.Measurement).all()
    return rels


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


def get_measurement_by_id(
    id: int,
    db: Session,
    skip: int = 0,
    limit: int = 100,
    start_time: datetime.datetime = Query(None),
    end_time: datetime.datetime = Query(None),
    order_by: str = "timestamp",
    desc: bool = False,
):
    rels = db.query(models.Measurement).filter(models.Measurement.id == id).all()

    if start_time and end_time and start_time < end_time:
        raise HTTPException(
            status_code=400, detail="Start time must be before end time"
        )

    if desc:
        order_by = f"{order_by} desc"

    return rels


def get_latest_temperature(sensor_id, db: Session) -> SectionDB:
    rels = (
        db.query(models.Measurement)
        .filter(models.Measurement.sensor_id == sensor_id)
        .order_by(desc(models.Measurement.timestamp))
        .first()
    )
    return rels
