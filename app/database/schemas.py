import datetime
from typing import List, Optional

from pydantic import BaseModel


class SensorBase(
    BaseModel
):  # A base model for sensor data, which includes name, block, and status fields. It also has a nested Config class with orm_mode = True attribute, which is used to enable ORM mode for this model as does most of the other models in this file.
    name: str
    block: str
    status: str

    class Config:
        orm_mode = True


class SensorData(
    BaseModel
):  # model that includes temperature, timestamp, and sensor_id fields for sensor measurements.
    temperature: float
    timestamp: datetime.datetime
    sensor_id: int

    class Config:
        orm_mode = True


class StatusData(
    BaseModel
):  # model that includes status and status_timestamp fields for sensor status data.
    status: str
    status_timestamp: datetime.datetime

    class Config:
        orm_mode = True


class SensorPatchDB(
    BaseModel
):  # model that includes name and block fields for updating sensor data.
    name: str
    block: str

    class Config:
        orm_mode = True


class BlockPatchDB(
    BaseModel
):  # model that includes block field for updating block data.
    block: str

    class Config:
        orm_mode = True


class StatusPatchDB(
    StatusData
):  # model that extends StatusData and is used for updating sensor status.
    class Config:
        orm_mode = True


class BlockDB(
    SensorBase
):  # model that extends SensorBase and includes a list of measurements for a specific block.
    measurements: SensorData

    class Config:
        orm_mode = True


class StatusDB(
    StatusData
):  # model that extends StatusData and is used to store sensor status data in the database.
    class Config:
        orm_mode = True


class SensorDataDB(
    BaseModel
):  # model that includes temperature and timestamp fields for sensor measurements, to be stored in the database.
    temperature: int
    timestamp: datetime.datetime

    class Config:
        orm_mode = True


class DataIn(BaseModel):  # A model that includes an id field to specify sensor ID.
    id: int

    class Config:
        orm_mode = True


class DataDB(
    SensorData
):  # model that extends SensorData and includes an additional id field to store sensor measurement data in the database. It also has an optional sensor field to reference the DataIn model
    id: int
    sensor: Optional[DataIn] = None

    class Config:
        fields = {"sensor_id": {"exclude": True}}
        orm_mode = True
        allow_population_by_field_name = True
        allow_none = True


class SensorDB(
    SensorBase
):  # model that extends SensorBase and includes a list of measurements for a specific sensor.
    measurements: List[SensorData] = []

    class Config:
        orm_mode = True


class MeasurementDelete(
    BaseModel
):  # model that includes id, sensor_id, temperature, and timestamp fields for deleting a specific sensor measurement.
    id: int
    sensor_id: int
    temperature: float
    timestamp: Optional[str] = None

    class Config:
        orm_mode = True


class AllSensors(
    SensorBase
):  # model that extends SensorBase and is used to retrieve all sensor data.
    pass

    class Config:
        orm_mode = True
