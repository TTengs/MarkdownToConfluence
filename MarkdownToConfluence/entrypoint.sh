#!/bin/bash

#PATH="$(basename "${INPUT_FILESLOCATION}")"
#INPUT_FILESLOCATION = './documentation'
#echo $PATH
ls
git diff --name-only HEAD^ HEAD documentation
mod="$(git diff --name-only --diff-filter=M HEAD^ HEAD documentation)"
cre="$(git diff --name-only --diff-filter=A HEAD^ HEAD documentation)"
readarray modDiffs <<< "$mod"
#readarray creDiffs <<< "$cre"

echo "------Modified-------"

for i in "${modDiffs[@]}";
do
    echo $i
done

echo "------Created-------"

#for i in "${creDiffs[@]}";
#do
#    echo $i
#done

#echo ${CHANGED_FILES}