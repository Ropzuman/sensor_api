from fastapi import FastAPI

from .database import models
from .database.database import engine
from .routers import measurements, sensors

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(sensors.router)
app.include_router(measurements.router)
