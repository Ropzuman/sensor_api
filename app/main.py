from fastapi import FastAPI

from .database import models
from .database.database import engine
from .database.schemas import StatusDB
from .routers import measurements, sensors

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(sensors.router)
app.include_router(measurements.router)


# # add error handlers
# @app.exception_handler(Exception)
# async def default_error_handler(request, exc):
#     return {"message": "Internal server error"}


# # add documentation to endpoints
# @app.get("/", tags=["root"])
# async def root():
#     """
#     Welcome to the Sensror API!
#     """
#     return {"message": "Welcome to the API!"}


# @app.get("/health", tags=["root"])
# async def health():
#     """
#     Check the API health status.
#     """
#     return {"status": "ok"}
