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
coverage run --rcfile=util/coverage.config -m pytest -s -v $DO_MANUAL
coverage report
bandit -r src
