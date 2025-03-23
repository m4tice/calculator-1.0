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
