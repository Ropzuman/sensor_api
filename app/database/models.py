from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Sensor(Base):
    __tablename__ = "sensors"

    section = Column(String, nullable=False)
    status = Column(String, nullable=False)
    id = Column(Integer, primary_key=True, index=True)

    measurements = relationship("Measurement", back_populates="sensor")


class Measurement(Base):
    __tablename__ = "measurements"

    id = Column(Integer, primary_key=True, index=True)
    sensor_id = Column(Integer, ForeignKey("sensors.id"))
    value = Column(Integer)
    timestamp = Column(String)

    sensor = relationship("Sensor", back_populates="measurements")
