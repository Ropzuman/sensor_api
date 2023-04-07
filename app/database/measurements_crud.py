from fastapi import HTTPException
from sqlalchemy.orm import Session

from . import models


def get_all_measurements(db: Session):
    return db.query(models.Measurement).all()
