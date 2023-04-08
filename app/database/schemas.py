import datetime

from pydantic import BaseModel


class SensorBase(BaseModel):
    section: str
    status: str

    class Config:
        orm_mode = True


class SensorData(BaseModel):
    sensor_id: int
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

    class Config:
        orm_mode = True


class AllSensors(BaseModel):
    id: int
    section: str

    class Config:
        orm_mode = True
