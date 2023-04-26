from fastapi import Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy import func
from sqlalchemy.orm import Session, relationship

from . import models
from .schemas import SensorBase, SensorPatchDB, StatusPatchDB


def get_all_sensors(db: Session):
    return db.query(models.Sensor).all()


def read_sensor_by_name(db: Session, name: str):
    sensor = db.query(models.Sensor).filter(models.Sensor.name == name).first()

    if sensor is None:
        raise HTTPException(status_code=404, detail="Sensor not found")
    return sensor


def read_sensor_by_section(section: str, db: Session):
    sensor = db.query(models.Sensor).filter(models.Sensor.section == section).all()

    if not sensor:
        raise HTTPException(status_code=404, detail="Sensor not found")
    if not section:
        raise HTTPException(status_code=400, detail="Section name required")

    for sensor in db.query(models.Sensor).filter(models.Sensor.section == section):
        latest_reading = (
            db.query(models.Measurement)
            .filter(models.Measurement.sensor_id == sensor.id)
            .order_by(models.Measurement.timestamp.desc())
            .first()
        )

        result = []

        sensor_data = {
            "name": sensor.name,
            "section": sensor.section,
            "status": sensor.status,
            "measurements": latest_reading if latest_reading else None,
        }
        result.append(sensor_data)

        return result


def read_sensor_by_status(status: str, db: Session):
    sensor = db.query(models.Sensor).filter(models.Sensor.status == status).all()

    if sensor is None:
        raise HTTPException(status_code=404, detail="Sensor not found")
    return sensor


def create_sensor(sensor_in: SensorBase, db: Session):
    sensor = models.Sensor(**sensor_in.dict())
    existing_sensor = (
        db.query(models.Sensor).filter(models.Sensor.name == sensor.name).first()
    )

    if existing_sensor is not None:
        raise HTTPException(
            status_code=400, detail="Sensor with this name already exists"
        )

    db.add(sensor)
    db.commit()
    db.refresh(sensor)
    return sensor


def update_sensor(name: str, sensorbase: SensorPatchDB, db: Session):
    sensor = db.query(models.Sensor).filter(models.Sensor.name == name).first()
    if sensor is None:
        raise HTTPException(status_code=404, detail="Sensor not found")
    sensor_data = jsonable_encoder(sensorbase)
    for field in sensor_data:
        setattr(sensor, field, sensor_data[field])
    db.add(sensor)
    db.commit()
    db.refresh(sensor)
    return sensor


def update_status(name: str, status: StatusPatchDB, db: Session):
    sensor = db.query(models.Sensor).filter(models.Sensor.name == name).first()
    if sensor is None:
        raise HTTPException(status_code=404, detail="Sensor not found")
    sensor_data = jsonable_encoder(status)
    for field in sensor_data:
        setattr(sensor, field, sensor_data[field])
    db.add(sensor)
    db.commit()
    db.refresh(sensor)
    return sensor
