#!/bin/bash
# Command line usage: 
#       util/unit-test.sh MODULE_NAME
# ex:   util/unit-test.sh sample_uploads
#
# If you don't specify a class, this script
# will run every unit test without calculating
# code coverage.
TARGET=""
if ! [ -z "$1" ]
then
    if [[ $1 == *"manual"* ]]
    then
        TARGET="tests/manual/test_${1/manual\//}.py"
    else
    	TARGET="tests/test_$1.py"	
    fi
fi
DO_DEBUG=""
if [[ ("$FALCONPY_UNIT_TEST_DEBUG" != "" && $(echo $FALCONPY_UNIT_TEST_DEBUG | tr [:lower:] [:upper:]) != "DISABLED") ]]
then
  DO_DEBUG="--log-cli-level $FALCONPY_UNIT_TEST_DEBUG"
fi


coverage run --rcfile=util/coverage.config -m pytest -s -v $TARGET $DO_DEBUG
coverage report
# pytest -s -v $TARGET
