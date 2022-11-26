#!/bin/bash
#

DO_MANUAL="--ignore-glob=**/manual/*"
if ! [ -z "$1" ]
then
  if [ "$1" == "--include-manual" ]
  then
    DO_MANUAL=""
  fi
fi
DO_DEBUG=""
if [[ ("$FALCONPY_UNIT_TEST_DEBUG" != "" && $(echo $FALCONPY_UNIT_TEST_DEBUG | tr [:lower:] [:upper:]) != "DISABLED") ]]
then
  DO_DEBUG="--log-cli-level $FALCONPY_UNIT_TEST_DEBUG"
fi
coverage run --rcfile=util/coverage.config -m pytest -s -v $DO_MANUAL $DO_DEBUG
coverage report
bandit -r src
