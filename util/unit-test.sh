#!/bin/bash
# Command line usage: 
#       util/unit-test.sh CLASS_NAME
# ex:   util/unit-test.sh sample_uploads
#
# If you don't specify a class, this script
# will run every unit test without calculating
# code coverage.
TARGET=""
if ! [ -z "$1" ]
then
	TARGET="tests/test_$1.py"	
fi
pytest -s -v $TARGET
