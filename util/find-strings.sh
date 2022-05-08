#!/bin/bash
#
# The easily distracted developer's 'find in files'.
#
# Quickly scan falconpy module source for a specific string or strings.
# Multiple strings may be provided by using comma as a delimiter.
# Returns line number and module file name for each match.
#
# Run me from the root of the repository.
#   Example: util/find-strings.sh action,uninstall
#
B="\033[1m"
E="\033[0m"
DC="\033[36m"
Y="\033[33m"
G="\033[92m"
R="\033[31m"
U="\033[4m"
BL="\033[34m"
echo -e "$B$R.-:::::' :::.      :::       .,-:::::     ...   :::.    :::.$Y::::::::::..-:.     ::-.$E"
echo -e "$B$R;;;''''  ;;\`;;     ;;;     ,;;;'\`\`\`\`'  .;;;;;;;.\`;;;;,  \`;;;$Y \`;;;\`\`\`.;;;';;.   ;;;;'$E"
echo -e "$B$R[[[,,== ,[[ '[[,   [[[     [[[        ,[[     \\[[,[[[[[. '[[$Y  \`]]nnn]]'   '[[,[[['$E"
echo -e "$B$R\`\$\$\$\"\`\`c\$\$\$cc\$\$\$c  \$\$'     \$\$\$        \$\$\$,     \$\$\$\$\$\$ \"Y\$c\$\$$Y   \$\$\$\"\"       c$$\"$E"
echo -e "$B$R 888    888   888,o88oo,.__\`88bo,__,o,\"888,_ _,88P888    Y88$Y   888o       ,8P\"\`$E"
echo -e "$B$R \"MM,   YMM   \"\"\` \"\"\"\"YUMMM  \"YUMMMMMP\" \"YMMMMMP\" MMM     YM$Y   YMMMb     mM\"$BL$B"

echo -e "_  _  _  _____   ______ ______       _______ _______ _______  ______ _______ _     _"
echo -e "|  |  | |     | |_____/ |     \      |______ |______ |_____| |_____/ |       |_____|"
echo -e "|__|__| |_____| |    \_ |_____/      ______| |______ |     | |    \_ |_____  |     |"
echo -e "$E$U                                                                                    $E"
if [ -z "$2" ]
then
  SRC=""
else
  if [[ ${SRC: -1} == "/" ]]
  then
    SRC=$2
  else
    SRC="$2/"
  fi
fi
mod="src/falconpy/*.py"
matched=0
files=$(ls $SRC$mod)
for file in $files
do
  for search in ${1//,/ }
  do
    hit=$(cat $file | grep -n $search | cut -d : -f 1)
    if [[ "$hit" != "" ]]
    then
      for match in $hit
      do
        matched=$(($matched+1))
        FN=${file/src\/falconpy\//}
        FN=${FN/$SRC/}
        echo -e "Match on $Y$B$search$E found in $B$DC$FN$E on line $B$match$E"
      done
    fi
  done
done
echo
echo -e "$B$matched$E total matches found"
if [[ "$3" == *--egg* ]]
then
  cr="CrowdStrike"
  echo -e "          $Y  __,"
  echo -e "           /  |  |\\          _   , _|_    (|   |   ,   _ |\\       |\\"
  echo -e "          |   |  |/ /|/|/|  / \\_/ \\_|      |   |  / \\_|/ |/ |  |  |/"
  echo -e "           \\_/\\_/|_/ | | |_/\\_/  \\/ |_/     \\_/\\_/ \\/ |_/|_/ \\/|_/|_/"
  echo -e "                                                         |)"
  echo
  echo -e "                        ()  _   ,_  o    _|_ o        _,"
  echo -e "                        /\\ /   /  | | |/\\_|  | /|/|  / |"
  echo -e "                       /(_)\\__/   |/|/|_/ |_/|/ | |_/\\/|/"
  echo -e "                                     (|               (|$E"
  echo
  echo -e "	                                       by$G jshcodes$E$B@$E$R$cr$E!"
fi
