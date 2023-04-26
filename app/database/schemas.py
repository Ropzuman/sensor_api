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
    temperature: float
    timestamp: datetime.datetime
    sensor_id: int

    class Config:
        orm_mode = True


class StatusData(BaseModel):
    status: str
    status_timestamp: datetime.datetime

    class Config:
        orm_mode = True


class SensorPatchDB(BaseModel):
    name: str
    section: str

    class Config:
        orm_mode = True


class SectionDB(SensorBase):
    measurements: SensorData

    class Config:
        orm_mode = True


class StatusPatchDB(StatusData):
    status_list: list[StatusData] = []

    class Config:
        orm_mode = True


class StatusDB(StatusData):
    name: str
    status: str
    status_timestamp: datetime.datetime

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
    measurements: List[SensorData] = []

    class Config:
        orm_mode = True


class AllSensors(SensorBase):
    pass

    class Config:
        orm_mode = True
