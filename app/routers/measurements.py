from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import measurements_crud as crud
from ..database.database import get_db
from ..database.schemas import DataDB

router = APIRouter(prefix="/measurements")


@router.get("/", response_model=list[DataDB])
def get_measurements(db: Session = Depends(get_db)):
    return crud.get_all_measurements(db)


@router.get("/{id}", response_model=DataDB)
def measurement_by_id(id: int, db: Session = Depends(get_db)):
    return crud.get_measurement_by_id(db, id)


@router.delete("/{id}", response_model=DataDB)
def delete_measurement_by_id(id: int, db: Session = Depends(get_db)):
    return crud.delete_measurement_by_id(db, id)
