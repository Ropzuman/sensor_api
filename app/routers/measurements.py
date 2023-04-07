from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import measurements_crud as crud
from ..database.database import get_db

# from ..database.schemas import


router = APIRouter(prefix="/measurements")
