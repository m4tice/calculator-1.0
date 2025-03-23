"""
Setup script for the py-dummy-app package.

This script uses setuptools to package the application and define its entry points.
The application can be run from the command line using the 'calculator' command.

Attributes:
    name (str): The name of the package.
    version (str): The version of the package.
    packages (list): A list of all Python import packages
    that should be included in the distribution package.
    entry_points (dict): A dictionary specifying
    what scripts should be made available to the user's PATH.
"""
from setuptools import setup, find_packages

setup(
    name="py-dummy-app",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "calculator=app.cli:main",
        ],
    },
)
