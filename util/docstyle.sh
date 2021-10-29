#!/bin/bash
BASE="src/falconpy"
if ! [ -z "$1" ];
then
	BASE="$BASE/${1/.py/}.py"
fi

pydocstyle $BASE --count
