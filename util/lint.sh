#!/bin/bash
if ! [[ -z "$1" ]]
then
	flake8 $1 --count --exit-zero --max-complexity=15 --max-line-length=127 --statistics
else
	echo "Need a target for the linter yo."
fi
