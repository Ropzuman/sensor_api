import datetime

from pydantic import BaseModel


class SensorBase(BaseModel):
    section: str
    status: str | None = None

    class Config:
        orm_mode = True


class SensorData(BaseModel):
    id: int
    timestamp: datetime.datetime
    temperature: int

    class Config:
        orm_mode = True


class DataDB(SensorData):
    class Config:
        orm_mode = True


class SensorDB(SensorBase):
    id: int
    measurements: list[SensorData]


class AllSensors(BaseModel):
    section: str
    status: str
    id: int

    class Config:
        orm_mode = True
