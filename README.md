# learning_matchmaking-service
An online match-making service for matching players in competitive games.

# Development
## Setting up & using a python environment
For first time use, set up a python environment using:
`python3 -m venv .venv`

Afterwards, use the following to activate the environment when working on the project:
`source .venv/bin/activate`

## Building
For building the project into a runnable program use: 
`pip install -e ".[dev]"`

# Dependencies
This project utilises the following dependencies:
- fastapi for the web backend framework
- setuptools as the backend build system
- pytest as the test framework
