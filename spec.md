# Sensor API Specifications

The Sensor API is a RESTful API for managing sensor data. This document outlines the specifications for the API.

## Functions

The API has the following fucntions:

- Get a list of all sensors.
  - Returns a list of all sensors in the database with their name, block and status.
- Get data from a specific sensor.
  - Depending on the query parameters, returns a list of data points for the sensor with the given ID.
  - For example querying by name will return the sensor with matching name along with its 10 latest measurements.
- Add a new sensor.
  - Adds a new sensor to the database.
- Add measurements for a specific sensor.
  - Adds measurements for the sensor with the given name.
  - Simualtes a sensor sending data to the API.
- Update block from a specific sensor.
  - Updates the block for the sensor with the given ID.
- Update status from a specific sensor.
  - Updates the status for the sensor with the given ID.
  - Can be used to reset a sensor that has gone into an error state.
- Delete data from a specific sensor.
  - Delete measurements form a specific sensor.

## Request and Response Formats

The API accepts and returns JSON-encoded request bodies and response bodies.
Example request:

``` bash
GET /sensors HTTP/1.1
Host: localhost:5000
```

Example response:

``` bash
HTTP/1.1 200 OK
Content-Type: application/json

[
  {
    "id": 1,
    "name": "Sensor 1",
    "block": "Room 1",
    "status": "active",

  },
  {
    "id": 2,
    "name": "Sensor 2",
    "block": "Room 2",
    "status": "active",
  },
  ...
]
```

## Response body format

The response body for the GET /sensors endpoint should be a JSON object with a single field, sensors, which is an array of sensor objects.

Each sensor object should have the following fields:

- id (integer): the ID of the sensor
- name (string): the name of the sensor
- block (string): the location of the sensor
- data (array): an array of data points for the sensor, where each data point is an object with the following fields:
      - value (float): the value of the data point in Celsius
      - timestamp (string): the timestamp of the data point in UTC

## Error handling

The API should return appropriate HTTP status codes for all requests. The following status codes should be used:

- 200 OK: The request was successful.
- 201 Created: The request was successful and a new resource was created.
- 400 Bad Request: The request was invalid.
- 404 Not Found: The requested resource was not found.
- 500 Internal Server Error: An internal server error occurred.

## Authentication

No user authentication is required for this API.

## Built With

- [Python](https://www.python.org/) - Programming language.
- [FastAPI](https://fastapi.tiangolo.com/) - Web framework.
- [Uvicorn](https://www.uvicorn.org/) - ASGI server.

## Authors

- **Ropzuman** - [Ropzuman] Roope Vähä-Aho / AEA21SP
