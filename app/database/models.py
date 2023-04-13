from datetime import datetime, time, timedelta

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Sensor(Base):
    __tablename__ = "sensors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    section = Column(String)
    status = Column(String)

    measurements = relationship("Measurement", back_populates="sensor")


class Measurement(Base):
    __tablename__ = "measurements"

    id = Column(Integer, primary_key=True, index=True)
    sensor_id = Column(Integer, ForeignKey("sensors.id"))
    temperature = float
    timestamp = datetime
    timestamp = id

    sensor = relationship("Sensor", back_populates="measurements")
