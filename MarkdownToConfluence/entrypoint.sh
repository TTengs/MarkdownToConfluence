#!/bin/bash
cd ..
ls
#PATH="$(basename "${INPUT_FILESLOCATION}")"
#INPUT_FILESLOCATION = './documentation'
#echo $PATH
docsDiff="$(git diff --name-only HEAD^^ HEAD ./documentation)"
echo $docsDiff

echo "-------"

for i in $docsDiff
do
    echo $i
done

echo "-------"

git diff --name-only HEAD^^ HEAD documentation

#echo ${CHANGED_FILES}