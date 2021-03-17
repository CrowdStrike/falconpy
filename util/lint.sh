#!/bin/bash
if ! [[ -z "$1" ]]
then
	TARGET=$1
else
	TARGET="."
fi
flake8 $TARGET --count --exit-zero --max-complexity=15 --max-line-length=127 --statistics