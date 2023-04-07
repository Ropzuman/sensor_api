# Sensor API Specification

## Endpoints

- GET /sensors - All the sensors with:

  - id
  - section
  - status

- GET /sensor/:section - All the sensors in a section with:

  - id
  - status
  - temperature with time and date

- GET /sensors/:id - A specific sensor with:

  - id
  - section
  - status
  - temperature with timestamp
  - 10 latest values of the sensor
  - Possibility to get values between two timestamps

- GET /sensors/:id/temperature - All the measurements of a sensor with:

  - timestamp

- GET /sensors/:error - All the sensor errors with:

  - graph showing error timestamps

- POST /sensors/:id - Add a new sensor with:

  - id
  - section
  - status

- POST /sensors/:id/status - Change the status of a sensor with:

  - status

- POST /sensors/:id/sec - Change the section of a sensor with:

  - section

- DELETE /sensors/:id - Delete a sensor with:

  - id

- DELETE /sensors/:id/temperature - Delete a specific sensor measurement with:
  - timestamp

## Schema

### SensorBase (Inherits from BaseModel)

Used to create a new sensor.

- section: string
- status: string

### SensorDB (Inherits from SensorBase)

- id: int
- temperature: (list[SensorData])

### AllSensors (Inherits from BaseModel)

- id: int
- section: string
- status: string
- temperature: (list[SensorData])

### SensorData (Inherits from BaseModel)

- timestamp: datetime
- temperature: int (As someone working as a process operator, ambient temperatures are almost never needed to be measured beyond full degrees celsius)

### SensorDB (Inherits from SensorBase)

- id: int
- temperature: (list[SensorData])
- error: (list[SensorError])
- timestamp: datetime

### SensorError (Inherits from BaseModel)

- timestamp: datetime
- error: string

### ErrorDB (Inherits form SensorError)

- id: int

## Routers

- Sensors
- Measurements

## Databases

- Sensors crud
- Measurements crud
- Errors crud

## Models

- Class Sensor
- Class Measurement
