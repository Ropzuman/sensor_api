import datetime
from typing import List, Optional

from pydantic import BaseModel


class SensorBase(BaseModel):
    name: str | None = None
    section: str | None = None
    status: str | None = None


class SensorData(BaseModel):
    id: int
    timestamp: datetime.datetime
    temperature: int


class SectionDB(SensorBase):
    section: str

    class Config:
        orm_mode = True


class StatusDB(SensorBase):
    status: str

    class Config:
        orm_mode = True


class DataDB(SensorData):
    class Config:
        orm_mode = True


class SensorDB(SensorBase):
    id: int

    class Config:
        orm_mode = True


class AllSensors(BaseModel):
    name: str
    section: str
    status: str
    id: int

    class Config:
        orm_mode = True
