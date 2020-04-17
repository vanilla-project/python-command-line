# Vanilla Python Command Line Project

This repository shows a basic setup for a command line application in Python.


## Getting Started

Python and Pipenv is expected to be installed on our system.


### Installing

After cloning this repository, change into the newly created directory and run

```
pipenv install --dev
```

This will install all dependencies needed for the project.


## Running the Tests

All tests can be run by executing

```
pipenv run test
```

`test` will invoke `pytest` which will then find all tests inside the `tests` directory and run them.


## Built With

- [Python](https://www.python.org)
- [Pipenv](https://github.com/pypa/pipenv)
- [pytest](https://docs.pytest.org/en/latest)


## License

This project is licensed under the MIT License - see the [license.md](license.md) file for details.

