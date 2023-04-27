from datetime import datetime

from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Sensor(Base):
    __tablename__ = "sensors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    section = Column(String)
    status = Column(String, default="unknown")
    status_timestamp = Column(String, default=datetime.utcnow)
    measurement_timestamp = Column(String, default=datetime.utcnow)

    measurements = relationship("Measurement", back_populates="sensor")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "section": self.section,
            "status": self.status,
            "status_timestamp": self.status_timestamp,
            "measurement_timestamp": self.measurement_timestamp,
        }


class Measurement(Base):
    __tablename__ = "measurements"

    id = Column(Integer, primary_key=True, index=True)
    temperature = Column(Float(precision=2))
    timestamp = Column(String, default=datetime.utcnow())
    sensor_id = Column(Integer, ForeignKey("sensors.id"))

    sensor = relationship("Sensor", back_populates="measurements")

    def to_dict(self):
        return {
            "id": self.id,
            "timestamp": self.timestamp,
            "temperature": self.temperature,
            "sensor_id": self.sensor_id,
        }
