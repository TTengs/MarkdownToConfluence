#!/bin/bash

PATH="$(basename ${INPUT_FILESLOCATION})"
#INPUT_FILESLOCATION = './documentation'
echo $PATH
ls
git diff --name-status HEAD^^ HEAD $PATH
mod="$(git diff --name-only --diff-filter=M HEAD^ HEAD $PATH)"
cre="$(git diff --name-only --diff-filter=A HEAD^ HEAD $PATH)"
readarray modDiffs <<< "$mod"
readarray creDiffs <<< "$cre"

echo "------Modified-------"

for i in "${modDiffs[@]}";
do
    echo $i
done

echo "------Created-------"

for i in "${creDiffs[@]}";
do
    echo $i
done

echo "-------"

git diff --name-only HEAD^^ HEAD documentation

#echo ${CHANGED_FILES}