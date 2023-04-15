import datetime
from typing import List

from pydantic import BaseModel

from . import models


class SensorBase(BaseModel):
    name: str
    section: str
    status: str

    class Config:
        orm_mode = True


class SensorData(BaseModel):
    temperature: int
    timestamp: datetime.datetime
    sensor_id: int

    class Config:
        orm_mode = True


class SectionDB(SensorBase):
    section: str
    measurements: list[SensorData] = []

    class Config:
        orm_mode = True


class StatusDB(SensorBase):
    status: str

    class Config:
        orm_mode = True


class SensorDataDB(BaseModel):
    temperature: int
    timestamp: datetime.datetime

    class Config:
        orm_mode = True


class DataIn(BaseModel):
    id: int

    class Config:
        orm_mode = True


class DataDB(SensorData):
    id: int
    sensor: DataIn

    class Config:
        fields = {"sensor_id": {"exclude": True}}


class SensorDB(SensorBase):
    id: int
    name: str
    measurements: List[SensorData] = []

    class Config:
        orm_mode = True


class AllSensors(SensorBase):
    id: int

    class Config:
        orm_mode = True
