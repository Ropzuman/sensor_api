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
    "location": "Room 2",
    "status": "active",
  },
  ...
]
```
