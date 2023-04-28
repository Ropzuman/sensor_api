from fastapi import Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy import func
from sqlalchemy.orm import Session, relationship

from . import models
from .schemas import SectionPatchDB, SensorBase, StatusPatchDB


# retrieves all sensors from the database using a database session object db and returns them as a list.
def get_all_sensors(db: Session):
    return db.query(models.Sensor).all()


# retrieves a sensor by its name from the database using a database session object db and returns its data along with the latest 10 measurements for that sensor. If the sensor is not found, it raises an HTTP exception.
def read_sensor_by_name(name: str, db: Session):
    if name is None:
        raise HTTPException(status_code=400, detail="Sensor name required")
    sensor = db.query(models.Sensor).filter(models.Sensor.name == name).first()
    if not sensor:
        raise HTTPException(status_code=404, detail="Sensor not found")

    readings = (  # 10 most recent readings
        db.query(models.Measurement)
        .filter(models.Measurement.sensor_id == sensor.id)
        .order_by(models.Measurement.timestamp.desc())
        .limit(10)
        .all()
    )

    result = []

    sensor_data = {  # sensor data
        "name": sensor.name,
        "section": sensor.section,
        "status": sensor.status,
        "measurements": readings if readings else None,
    }
    result.append(sensor_data)

    return result


# retrieves all sensors in a given section from the database using a database session object db and returns their data along with the latest measurement for each sensor. If no measurements are found for a given sensor, the returned value will be None.
def read_sensor_by_section(section: str, db: Session):
    result = []
    for sensor in (
        db.query(models.Sensor).filter(models.Sensor.section == section).all()
    ):
        latest_reading = (
            db.query(models.Measurement)
            .filter(models.Measurement.sensor_id == sensor.id)
            .order_by(models.Measurement.timestamp.desc())
            .first()
        )

        sensor_data = {
            "name": sensor.name,
            "section": sensor.section,
            "status": sensor.status,
            "measurements": {"temperature": None, "timestamp": None, "sensor_id": None}
            if not latest_reading
            else latest_reading.to_dict(),
        }
        result.append(sensor_data)

    return result


# retrieves all sensors with a given status from the database using a database session object db and returns them as a list. If no sensors are found with the given status, it raises an HTTP exception.
def read_sensor_by_status(status: str, db: Session):
    sensor = (
        db.query(models.Sensor).filter(models.Sensor.status == status).all()
    )  # all sensors with a given status

    if not sensor:
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


# This function updates an existing sensor in the database with the provided data in a SectionPatchDB object sensorbase. It first checks if the sensor exists in the database, and if not, raises an HTTP exception. If the sensor is found, it updates the relevant fields with the new data and returns the updated sensor object.
def update_sensor(name: str, sensorbase: SectionPatchDB, db: Session):
    sensor = (
        db.query(models.Sensor).filter(models.Sensor.name == name).first()
    )  # check if sensor exists
    if not sensor:
        raise HTTPException(status_code=404, detail="Sensor not found")

    sensor_data = jsonable_encoder(sensorbase)  # update sensor data
    for field in sensor_data:
        setattr(sensor, field, sensor_data[field])  # update relevant fields
    db.add(sensor)
    db.commit()
    db.refresh(sensor)
    return sensor


# This function updates the status field of an existing sensor in the database with the provided data in a StatusPatchDB object status. It first checks if the sensor exists in the database, and if not, raises an HTTP exception. If the sensor is found, it updates the status field with the new data, commits the changes to the database, and returns both the updated sensor object and the new status data.
def update_status(name: str, status: StatusPatchDB, db: Session):
    sensor = db.query(models.Sensor).filter(models.Sensor.name == name).first()
    if not sensor:
        raise HTTPException(status_code=404, detail="Sensor not found")

    sensor_data = jsonable_encoder(status)
    for field in sensor_data:
        setattr(sensor, field, sensor_data[field])
    db.add(sensor)
    db.commit()
    db.refresh(sensor)

    return sensor, sensor_data
