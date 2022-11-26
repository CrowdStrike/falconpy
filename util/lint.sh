#!/bin/bash

if ! [[ -z "$1" ]]
then
	TARGET=$1
else
	TARGET="src/falconpy"
fi

function splat() ( echo "--------------------------------------------------------"; )

echo -e "\nFormatting"
splat
flake8 $TARGET --count --statistics

echo -e "\nCode style and syntax"
splat
pylint $TARGET

echo "Docstring style and syntax"
splat
pydocstyle $TARGET
