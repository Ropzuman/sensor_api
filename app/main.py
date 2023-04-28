from fastapi import FastAPI  # Import the FastAPI class

# Import modules
from .database import models
from .database.database import engine
from .routers import measurements, sensors

# Create the necessary database tables based on the models defined in models.py
models.Base.metadata.create_all(bind=engine)

# Create a new instance of the FastAPI class
app = FastAPI(title="Sensor API", description="API for managing sensors")

# Include the router for sensors
app.include_router(sensors.router)

# Include the router for measurements
app.include_router(measurements.router)
