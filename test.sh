#!/bin/bash

res=$(git --no-pager diff --name-status origin/main documentation)
ReMoFilesArrOLD=()
ReMoFilesArrNEW=()
delFilesArr=()
modFilesArr=()
addedFilesArr=()
while IFS=$'\t' read -r -a tmp ; do
    # Renamed or moved files
    if [[ ${tmp[0]} = R* ]]
    then
        echo "---Renamed/Moved---"
        echo "from ${tmp[1]}"
        echo "to ${tmp[2]}"
        ReMoFilesArrOLD+=("${tmp[1]}")
        ReMoFilesArrNEW+=("${tmp[2]}")
    # Modified files
    elif [[ ${tmp[0]} = M* ]]
    then
        echo "---Modified---"
        echo ${tmp[1]}
        modFilesArr+=("${tmp[1]}")
    # Deleted files
    elif [[ ${tmp[0]} = D* ]]
    then
        echo "---Deleted---"
        echo ${tmp[1]}
        delFilesArr+=("${tmp[1]}")
    # Added files
    elif [[ ${tmp[0]} = A* ]]
    then
        echo "---Added---"
        echo ${tmp[1]}
        addedFilesArr+=("${tmp[1]}")
    else
        echo "---Other changes---"
        echo ${tmp[@]}
    fi
done <<< $res

echo "
All files
"

echo "Modified files"
for i in "${modFilesArr[@]}"
do
    echo $i
    #bash ./MarkdownToConfluence/convert.sh "$i"
done

echo "Added files"
for i in "${addedFilesArr[@]}"
do
    echo $i
done