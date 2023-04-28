# Sensor API Specifications

The Sensor API is a RESTful API for managing sensor data. This document outlines the specifications for the API.

## Endpoints

The API has the following endpoints:

- `/sensors` (GET): Get a list of all sensors.
- `/sensors/<id>` (GET): Get data from a specific sensor.
- `/sensors` (POST): Add data from a new sensor.
- `/sensors/<id>` (PUT): Update data from a specific sensor.
- `/sensors/<id>` (DELETE): Delete data from a specific sensor.

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
