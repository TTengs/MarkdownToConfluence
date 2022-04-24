#!/bin/bash
cd ..
docsDiff=$(git diff --name-only HEAD^^ HEAD ${INPUT_FILESLOCATION})
echo $docsDiff

echo "-------"

for i in $docsDiff
do
    echo $i
done

echo "-------"

git diff --name-only HEAD^^ HEAD documentation

#echo ${CHANGED_FILES}