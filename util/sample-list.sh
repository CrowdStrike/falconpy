#!/bin/bash
# Quickly display a list of available samples
#
# This should be executed from the repository root.
# i.e.  util/sample-list.sh
#
LR="\033[91m"
BO="\033[1m"
EM="\033[0m"
LB="\033[94m"
YE="\033[93m"
DR="\033[31m"
GR="\033[32m"
# I keep expecting someone to show up and take my Figlet away...
echo -e "$DR ____ ____ _    ____ ____ _  _$LB ___$YE  _   _$EM"
echo -e "$DR |___ |__| |    |    |  | |\ |$LB |__]$YE  \_/$EM$BO  Sample$EM"
echo -e "$DR |    |  | |___ |___ |__| | \|$LB |$YE      |$EM$BO   Library$EM"
echo -e "$LR--------------------------------------------------$EM"
find samples -type f -name "*.py" -mindepth 1 | sort
echo
echo $(find samples -type f -name "*.py" -mindepth 1 | wc -l) FalconPy samples found.

if [[ "$1" == *--egg* ]]
then
  at="$BO@$EM"
  cr="CrowdStrike"
  echo -e "          $YE  __,"
  echo -e "           /  |  |\\          _   , _|_    (|   |   ,   _ |\\       |\\"
  echo -e "          |   |  |/ /|/|/|  / \\_/ \\_|      |   |  / \\_|/ |/ |  |  |/"
  echo -e "           \\_/\\_/|_/ | | |_/\\_/  \\/ |_/     \\_/\\_/ \\/ |_/|_/ \\/|_/|_/"
  echo -e "                                                         |)"
  echo
  echo -e "                        ()  _   ,_  o    _|_ o        _,"
  echo -e "                        /\\ /   /  | | |/\\_|  | /|/|  / |"
  echo -e "                       /(_)\\__/   |/|/|_/ |_/|/ | |_/\\/|/"
  echo -e "                                     (|               (|$EM"
  echo
  echo -e "                                            by$GR jshcodes$EM$BO@$EM$DR$cr$EM! $EM"
fi
