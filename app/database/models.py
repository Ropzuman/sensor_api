from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

# class Sensor(Base):
#     __tablename__ = "sensors"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, unique=True, index=True)
#     description = Column(String)
#     unit = Column(String)
#     measurements = relationship("Measurement", back_populates="sensor")
