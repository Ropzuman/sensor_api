from fastapi import HTTPException
from sqlalchemy.orm import Session

from . import models


def get_all_measurements(db: Session):
    rels = db.query(models.Measurement).all()
    return rels


def get_measurement_by_id(db: Session, id: int):
    rel = db.query(models.Measurement).filter(models.Measurement.id == id).first()
    if not rel:
        raise HTTPException(status_code=404, detail="Measurement not found")
    return rel


# def create_measurement(db: Session, measurement: models.Measurement):
#     measurement = models.Measurement(**measurement.dict())
#     db.add(measurement)
#     db.commit()
#     db.refresh(measurement)
#     return measurement


def delete_measurement_by_id(db: Session, id: int):
    rel = db.query(models.Measurement).filter(models.Measurement.id == id).first()
    if not rel:
        raise HTTPException(status_code=404, detail="Measurement not found")
    db.delete(rel)
    db.commit()
    return rel
