from fastapi import HTTPException, Query
from fastapi.encoders import jsonable_encoder
from sqlalchemy import desc, func
from sqlalchemy.orm import Session

from . import models
from .schemas import SensorDataDB


# Get all measurements
def get_all_measurements(db: Session):
    try:
        rels = db.query(models.Measurement).all()
        return rels
    except:
        raise HTTPException(status_code=500, detail="Error retrieving measurements")


# Delete a measurement
def delete_measurement_by_id(measurement_id: int, db: Session):
    measurement = db.query(models.Measurement).get(measurement_id)
    if not measurement:
        raise HTTPException(status_code=404, detail="Measurement not found")
    db.delete(measurement)
    db.commit()
    return {
        "id": measurement.id,
        "sensor_id": measurement.sensor_id,
        "temperature": measurement.temperature,
        "timestamp": measurement.timestamp,
    }


# Create a measurement
def create_measurement(id: int, temperature_in: SensorDataDB, db: Session):
    try:  # Create the measurement
        mes = models.Measurement(**temperature_in.dict(), sensor_id=id)
        db.add(mes)
        db.commit()
        db.refresh(mes)
        return mes
    except:
        raise HTTPException(status_code=500, detail="Error creating measurement")
