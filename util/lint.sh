#!/bin/bash
if ! [[ -z "$1" ]]
then
	TARGET=$1
else
	TARGET="src/falconpy"
fi
flake8 $TARGET --count --exit-zero --max-complexity=15 --max-line-length=127 --statistics --exclude=debug.py
pylint $TARGET --exit-zero --max-line-length=127 --disable=R0801 --ignore=debug.py
