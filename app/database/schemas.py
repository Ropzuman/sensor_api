import datetime
from typing import List

from pydantic import BaseModel


class SensorBase(BaseModel):
    name: str
    section: str
    status: str

    class Config:
        orm_mode = True


class SensorData(BaseModel):
    id: int
    timestamp: datetime.datetime
    temperature: int

    class Config:
        orm_mode = True


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
    name: str
    sensors: list["SensorBase"] = []

    class Config:
        orm_mode = True


class AllSensors(SensorBase):
    # name: str
    # section: str
    # status: str
    id: int

    class Config:
        orm_mode = True
