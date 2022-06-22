#!/bin/bash
#
# Report a list of public FalconPy modules and the classes they provide.
# Syntax is nebulous, but it was late... you might have to suffer a bit.
#
# Tested on Darwin 20.6.0, zsh 5.8 (x86_64-apple-darwin20.0)
#
# This application should be run from the root of repository folder,
# or you should pass the location of this folder as the only argument.
#
#				 - jshcodes@CrowdStrike 05.04.2022
#
clear
fp="."
r="\033[31m"
e="\033[0m"
b="\033[1m"
y="\033[33m"
g="\033[92m"
p="\033[4m"
o="\033[32m"
bz="\033[34m"
k="|"
ub="Uber$e"
ub="$g$ub"
ax=" Auth$e"
ax="$b$bz$ax"
# If you squint, it looks just like a falcon. Honest.
bf="$e     we$b stop$e"
be="$o            \" \"$e"
bd="$o         =^\`-'^="
bc="$o          <$r*$o,$r*$o>"
bb="$o            ___$e /"
ba="$e       breaches!"
if [[ ! -z "$1" && "$1" != --egg ]]
then
  fp=$1
fi
m="/src/falconpy"
a=$(ls $fp$m/*.py 2>/dev/null | grep -v '__\|/_\|debug.py')
sm=0
if [[ "$a" == "" ]]
then
  sm=1
  ba=""
  bb=""
  bc=""
  bd=""
  be=""
  bf=""
fi
echo -e "      $r __,  _, _,   _,  _, _, _$y __, , _                $bf"
echo -e "      $r |_  /_\ |   / \` / \ |\ |$y |_) \ |                 $ba"
echo -e "      $r |   | | | , \ , \ / | \|$y |    \|           $bb"
echo -e "      $r ~   ~ ~ ~~~  ~   ~  ~  ~$y ~     )            $bc"
echo -e "             $e  $b Public modules list$e$y  ~'            $bd"
echo -e "                                                  $be"
if [[ "$sm" == 1 ]]
then
  fa="FalconPy repository folder not found!\n"
  fb="If you are not in the repository folder,\n"
  fc="pass this location as an argument.\n\n"
  fd="Example:\n./public_modules.sh /path/to/repo/folder\n"
  echo -e "$r$fa$e$fb$fc$fd"
  exit
fi
t=0
n=$(wc -w <<< $a)
az=" $p      MODULE                      "
ab="     CLASS NAME                      METHODS $e"
echo -e "$az$ab"
tops=0
for fn in $a
do
    u=""
    t=$(($t+1))
    op=$(cat $fn | grep "(self:" | wc -l)
    tops=$(($tops+$op))
    q=$(cat $fn | grep \(Service)
    q=${q/\(ServiceClass\):/}
    q=${q/class /}
    if [ "$q" == "" ]
    then
      q="OAuth2"
    fi
    s="$(printf '%02d' $t) | ${fn/$fp$m\//}"
    if [ ${fn/$fp$m\//} == api_complete.py ]
    then
      u="           Uber"
      q="APIHarness"
#    else
#      if [ "$q" != "Iocs" ]
#      then
#	tops=$(($tops+$op))
#      fi
    fi
    if [ ${fn/$fp$m\//} == oauth2.py ]
    then
      u="               Auth"
    fi
    if [ $t == $n ]
    then
      j=$p
    fi
    z=${s/.py/}
    w=$(printf "%-35s" "$z")
    v=$(printf "%-28s" "$q $u")
    c=$(echo " $w | $v ")
    c=${c/Uber/$ub}
    c=${c/\ Auth/$ax}
    echo -e "$k$j$c |$op $e$k"
done
echo
echo "$tops total methods"
echo

if [[ "$2" == *--egg* ]]
then
  at="$b@$e"
  cr="CrowdStrike"
  echo -e "          $y  __,"
  echo -e "           /  |  |\\          _   , _|_    (|   |   ,   _ |\\       |\\"
  echo -e "          |   |  |/ /|/|/|  / \\_/ \\_|      |   |  / \\_|/ |/ |  |  |/"
  echo -e "           \\_/\\_/|_/ | | |_/\\_/  \\/ |_/     \\_/\\_/ \\/ |_/|_/ \\/|_/|_/"
  echo -e "                                                         |)"
  echo
  echo -e "                        ()  _   ,_  o    _|_ o        _,"
  echo -e "                        /\\ /   /  | | |/\\_|  | /|/|  / |"
  echo -e "                       /(_)\\__/   |/|/|_/ |_/|/ | |_/\\/|/"
  echo -e "                                     (|               (|$e"
  echo
  echo -e "	                                       by$g jshcodes$e$b@$e$r$cr$e! $e"
fi
