#!/bin/bash

#git diff --name-status HEAD^^ HEAD ${INPUT_FILESLOCATION}

echo $PWD
ls

mod="$(git diff --name-only --diff-filter=M HEAD^^ HEAD ${INPUT_FILESLOCATION})"
cre="$(git diff --name-only --diff-filter=A HEAD^^ HEAD ${INPUT_FILESLOCATION})"

readarray modDiffs <<< $mod
readarray -t creDiffs <<< $cre

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