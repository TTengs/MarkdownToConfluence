#!/bin/bash

#git diff --name-status HEAD^^ HEAD ${INPUT_FILESLOCATION}
#git init
echo $PWD
ls
git diff --name-only ${{ github.event.push.base.sha }} ${{ github.sha }}

#mod="$(git diff --name-only --diff-filter=M HEAD^^ HEAD ${INPUT_FILESLOCATION})"
#cre="$(git diff --name-only --diff-filter=A HEAD^^ HEAD ${INPUT_FILESLOCATION})"

#readarray modDiffs <<< $mod
#readarray -t creDiffs <<< $cre

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