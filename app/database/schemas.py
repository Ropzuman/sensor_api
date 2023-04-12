import datetime
from typing import List, Optional

from pydantic import BaseModel


class SensorBase(BaseModel):
    name: str | None = None
    section: str | None = None
    status: str | None = None
    id: int | None = None

    class Config:
        orm_mode = True


class SensorData(BaseModel):
    id: int
    timestamp: datetime.datetime
    temperature: int

    class Config:
        orm_mode = True


class SectionBase(SensorBase):
    section: str

    class Config:
        orm_mode = True


class StatusBase(SensorBase):
    # name: str | None = None
    # section: str | None = None
    # status: str | None = None

    class Config:
        orm_mode = True


class StatusDB(StatusBase):
    id: int
    status: str
    # measurements: list[StatusBase]

    class Config:
        orm_mode = True


class DataDB(SensorData):
    class Config:
        orm_mode = True


class SensorDB(SensorBase):
    id: int
    measurements: list[SensorData]


class AllSensors(BaseModel):
    name: str
    section: str
    status: str
    id: int

    class Config:
        orm_mode = True
