import datetime
from typing import List, Optional

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


class SectionPatchDB(BaseModel):
    section: str

    class Config:
        orm_mode = True


class StatusPatchDB(StatusData):
    class Config:
        orm_mode = True


class StatusDB(StatusData):
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
    sensor: Optional[DataIn] = None

    class Config:
        fields = {"sensor_id": {"exclude": True}}
        orm_mode = True
        allow_population_by_field_name = True
        allow_none = True


class SensorDB(SensorBase):
    measurements: List[SensorData] = []

    class Config:
        orm_mode = True


class MeasurementDelete(BaseModel):
    id: int
    sensor_id: int
    temperature: float
    timestamp: Optional[str] = None

    class Config:
        orm_mode = True


class AllSensors(SensorBase):
    pass

    class Config:
        orm_mode = True
