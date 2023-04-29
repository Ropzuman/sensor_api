from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database.database import engine, get_db
from ..database.schemas import (
    AllSensors,
    BlockDB,
    BlockPatchDB,
    SensorBase,
    SensorDB,
    StatusPatchDB,
)
from ..database.sensors_crud import (
    create_sensor,
    get_all_sensors,
    read_sensor_by_block,
    read_sensor_by_name,
    read_sensor_by_status,
    update_sensor,
    update_status,
)

# Create a new APIRouter instance with the prefix "/Sensors"
router = APIRouter(prefix="/Sensors")


# Create a new sensor
@router.get("", response_model=list[AllSensors])
def read_sensors(name: str = "", db: Session = Depends(get_db)):
    return get_all_sensors(db)


# Read block
@router.get("/{block}", response_model=list[BlockDB])
def read_sensors_by_block(block: str, db: Session = Depends(get_db)):
    return read_sensor_by_block(block, db)


# Read Status
@router.get("/sensors/{status}", response_model=list[SensorBase])
def read_sensors_by_status(status: str, db: Session = Depends(get_db)):
    return read_sensor_by_status(status, db)


# Read Name
@router.get("/sensor/{name}", response_model=list[SensorDB])
def read_sensors_by_name(name: str, db: Session = Depends(get_db)):
    # Wrap the database function call in a try block to catch any exceptions
    try:
        return read_sensor_by_name(name, db)
    except:
        # If an exception is caught, raise an HTTPException with a 500 status code and a custom error message
        raise HTTPException(status_code=500, detail="Database connection error")


@router.post("", response_model=SensorDB)  # Create a new sensor
def create_sensors(sensor_in: SensorBase, db: Session = Depends(get_db)):
    return create_sensor(sensor_in, db)


# Update Sensor
@router.patch("/{block}")
def update_sensors(name: str, sensorbase: BlockPatchDB, db: Session = Depends(get_db)):
    # Wrap the database function call in a try block to catch any exceptions
    try:
        return update_sensor(name, sensorbase, db)
    except:
        # If an exception is caught, raise an HTTPException with a 500 status code and a custom error message
        raise HTTPException(status_code=500, detail="Database connection error")


# Update Status
@router.patch("/status/{name}")
def update_sensors_status(  # Update the status of a sensor
    name: str, statusdb: StatusPatchDB, db: Session = Depends(get_db)
):
    sensor = read_sensor_by_name(name, db)  # Check if the sensor exists
    if not sensor:
        raise HTTPException(status_code=404, detail="Sensor not found")
    return update_status(name, statusdb, db)
