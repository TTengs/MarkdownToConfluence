#!/bin/bash

#git init
git config --global --add safe.directory .
git config --global core.pager "less -FRSX"
#git fetch
#echo "---------TEST----------"
#git diff --name-only origin/main.. -- ${INPUT_FILESLOCATION}

#echo "----------lol---------"
#git diff --name-only origin/main... -- ${INPUT_FILESLOCATION}

echo "---------rename-------"
git --no-pager diff HEAD^ HEAD -M100% -B ${INPUT_FILESLOCATION} | sed "s/^/'/;s/$/'/" 

#git diff --name-only ${{ github.event.push.base.sha }} ${{ github.sha }}

#mod="$(git diff --name-only --diff-filter=M HEAD^^ HEAD ${INPUT_FILESLOCATION})"
#cre="$(git diff --name-only --diff-filter=A HEAD^^ HEAD ${INPUT_FILESLOCATION})"

#readarray modDiffs <<< $mod
#readarray -t creDiffs <<< $cre

#echo "------Modified-------"

#for i in "${modDiffs[@]}";
#do
#    echo $i
#done

#echo "------Created-------"

#for i in "${creDiffs[@]}";
#do
#    echo $i
#done