#!/bin/sh

echo
echo "##################"
echo "# Running Pylint #"
echo "##################"
pylint --rcfile ../config.pylintrc *.py

echo "######################"
echo "# Running pydocstyle #"
echo "######################"
pydocstyle *.py

echo
