# Sensor API

Sensor API is a simple RESTful API built with Python that allows you to retrieve data from a sensor and store it in a database. This project is designed to be a starting point for developers who want to build their own API for sensor data.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

To run this project, you will need:

- Python 3.10 or higher
- pip (Python package manager)
- virtualenv (Python virtual environment manager)
- SQLite
- SQLalchemy
- FastAPI
- Uvicorn
- Pydantic
- Pylance
- Autopep, Black or similiar Python formatter

### Installing

1. Clone this repository to your local machine.

    ``` bash
    git clone https://github.com/Ropzuman/sensor_api.git
    ```

2. Create a virtual environment and activate it.

    Here the best course of action is to navigate to the requirements.txt file and run the following command:

    ``` bash
    pip install -r requirements.txt
    ```

    Or if VSCode suggests you to create a virtual environment, you can do so by clicking on the button that appears on the bottom right corner of the screen. It will create a virtual environment for you and install all the dependencies.

3. Run the project.

    ``` bash
    uvicorn main:app --reload
    ```
    This will run the project on the default port 8000. If you want to run it on a different port, you can do so by adding the following flag to the command above:

    ``` bash
    --port 8080
    ```
    This will run the project on port 8080.

## Usage

The API has the following endpoints:

- `/sensors` (GET): Get a list of all sensors.
- `/sensors/<id>` (GET): Get data from a specific sensor.
- `/sensors` (POST): Add data from a new sensor.
- `/sensors/<id>` (PUT): Update data from a specific sensor.
- `/sensors/<id>` (DELETE): Delete data from a specific sensor.

The API has been designed to be used with the FastAPI Swagger UI. To access it, go to `http://localhost:8000/docs` in your browser.

All responses are in JSON format.

## Built With

- [Python](https://www.python.org/) - Programming language.
- [FastAPI](https://fastapi.tiangolo.com/) - Web framework.
- [Uvicorn](https://www.uvicorn.org/) - ASGI server.
- [SQLite](https://www.sqlite.org/index.html) - Database engine.
- [SQLalchemy](https://www.sqlalchemy.org/) - Database toolkit.
- [Pydantic](https://pydantic-docs.helpmanual.io/) - Data validation.
- [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) - VSCode extension for Python.
- [Autopep](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) - VSCode extension for Python formatting.
