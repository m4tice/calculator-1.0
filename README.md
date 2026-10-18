# Calculator

A small Python calculator library and command-line application used to learn
Python packaging, Docker, and GitHub Actions.

## Run from the repository

```powershell
python -m app.cli add 1 2
```

## Install locally

```powershell
python -m pip install -e .
calculator add 1 2
```

## Use the library

```python
from app.calculator import Calculator

calculator = Calculator()
print(calculator.multiply(4, 5))
```

## Run tests

```powershell
python -m pytest
```

## Build the package

```powershell
python -m pip install -r requirements.txt
python -m build
```

The wheel and source distribution are created in `dist/`.