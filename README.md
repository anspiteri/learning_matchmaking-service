# learning_matchmaking-service
An online match-making service for matching players in competitive games.

<br>

## Project Structure
```
learning_matchmaking-service/
├── scripts/
|	├── demo.py
|	└── run.py
├── src/
|	└── matchmaking_service/
|		├── __init__.py
|		├── api.py
|		├── service.py
|		├── models.py
|		└── state.py
├── tests/
├── .gitignore
├── LICENSE
└── pyproject.toml
```

<br>

## Development
### Setting up & using a python environment
For first time use, set up a python environment using:
`python3 -m venv .venv`

Afterwards, use the following to activate the environment when working on the project:
`source .venv/bin/activate`

<br>

### Building & running
For building the project into a runnable program use:
`pip install -e ".[dev]"`

To spin up the server, use run.py in `scripts`:
`python scripts/run.py`

<br>

## Dependencies
This project utilises the following dependencies:
- fastapi for the web backend framework
- uvicorn for running the application server
- setuptools as the backend build system
- pytest as the test framework
