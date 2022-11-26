#!/bin/bash
#
# Set the debug environment flag.
# 
#
if [ -z "$1" ]
then
  echo "No setting specified, disabling. (To enable: util/set-debug.sh debug)"
  export FALCONPY_UNIT_TEST_DEBUG="DISABLED"
else
  export FALCONPY_UNIT_TEST_DEBUG=$1
  echo "Debugging flag set to $1"
fi
