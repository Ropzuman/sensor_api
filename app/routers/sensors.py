from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

# from ..database.sensors_crud import
# from ..database.schemas import
from ..database.database import get_db

router = APIRouter(prefix="/measurements")
