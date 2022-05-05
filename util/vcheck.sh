#!/bin/bash
#
# Compare the installed version of FalconPy
# to the available versions online.
#
# Execute this script straight from falconpy.io with:
# curl https://falconpy.io/vcheck --silent | bash
#
PACKAGE="crowdstrike-falconpy"
GREEN="\033[32m"
RED="\033[31m"
LIGHTRED="\033[91m"
BOLD="\033[1m"
UNDERLINE="\033[4m"
END="\033[0m"

if [ -f Pipfile ]
then
  echo "Pipenv detected"
  ENV_TYPE="pipenv run"
fi
if [ -f poetry.lock ]
then
  echo "Poetry detected"
  ENV_TYPE="poetry run"
fi

cur_version=$($ENV_TYPE python3 -m pip show $PACKAGE 2>/dev/null | grep Version | cut -c 10-)
if [ "$cur_version" == "" ]
then
  cur_version="Not installed"
fi
latest_version=$($ENV_TYPE python3 -m pip index versions $PACKAGE \
	--disable-pip-version-check --no-color 2>/dev/null \
	| grep "Available versions:" \
	| cut -d ":" -f2 | cut -d "," -f1 | cut -d " " -f2)
cur_dev=$(curl https://raw.githubusercontent.com/CrowdStrike/falconpy/dev/src/falconpy/_version.py --silent \
	| grep "_VERSION" | cut -d "=" -f2 | cut -d "'" -f2)

latest_major=$(echo $latest_version | cut -d "." -f1)
latest_minor=$(echo $latest_version | cut -d "." -f2)
latest_patch=$(echo $latest_version | cut -d "." -f3)

current_major=$(echo $cur_version | cut -d "." -f1)
current_minor=$(echo $cur_version | cut -d "." -f2)
current_patch=$(echo $cur_version | cut -d "." -f3)

if [ "$cur_version" == "Not installed" ]
then
  current_major=0
  current_minor=0
  current_patch=0
fi

UPDATE="$BOLD$RED Updated recommended $END"
vcolor=$LIGHTRED
if [ $current_major -ge $latest_major ]
then
  if [ $current_minor -ge $latest_minor ]
  then
    if [ $current_patch -ge $latest_patch ]
    then
      UPDATE=""
      vcolor=$GREEN
    fi
  fi
fi
if [ "$cur_version" == "Not installed" ]
then
  UPDATE=""
fi
echo
echo -e "$BOLD$UNDERLINE$PACKAGE version information$END"
echo -e Current version: $BOLD$vcolor$cur_version$END
echo -e Latest version: $BOLD$latest_version $UPDATE$END
echo -e Current development version: $BOLD$cur_dev$END
