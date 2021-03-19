#!/bin/sh

echo Running Pylint:
pylint --rcfile ../config.pylintrc *.py

echo Running pydocstyle:
pydocstyle *.py
