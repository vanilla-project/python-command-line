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


### Testing Approach

The test for class `Example` is only verifying the return value of one method.

`Main` on the other hand is tested via a test-double that gets injected.
This allows us to _spy_ on the output of it.
We want to avoid printing anything to the screen while running the tests.
Injecting a test double in this instance is a nice way to isolate our application from the command line.

At the bottom of the executable main module [`sample/main.py`](sample/main.py) we inject `sys.stdout`, which is Python's variable for its standard output.


## Running the Application

To run the application execute the main module `sample.main`.
You should see the text &ldquo;Python Example&rdquo; being printed.

```
$: python -m sample.main
Python Example
```


## Built With

- [Python](https://www.python.org)
- [Pipenv](https://github.com/pypa/pipenv)
- [pytest](https://docs.pytest.org/en/latest)


## License

This project is licensed under the MIT License - see the [license.md](license.md) file for details.

