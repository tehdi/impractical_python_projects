#!/bin/sh

# If caller passed one or more filenames, check them
# Else check all *.py files in the working dir
files_to_check=$*
default_files_to_check=*.py
# https://www.gnu.org/software/bash/manual/html_node/Shell-Parameter-Expansion.html
to_check=${files_to_check:-${default_files_to_check}}

echo
echo "Checking files: ${to_check}"

echo
echo "##################"
echo "# Running Pylint #"
echo "##################"
~/.local/bin/pylint --rcfile ~/config.pylintrc ${to_check}

echo "######################"
echo "# Running pydocstyle #"
echo "######################"
~/.local/bin/pydocstyle ${to_check}

echo
