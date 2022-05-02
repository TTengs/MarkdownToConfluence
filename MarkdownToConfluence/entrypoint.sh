#!/bin/bash

git init
git config --global --add safe.directory /github/workspace
git config --global core.pager "less -FRSX"
#git fetch
#echo "---------TEST----------"
#git diff --name-only origin/main.. -- ${INPUT_FILESLOCATION}

#echo "----------lol---------"
#git diff --name-only origin/main... -- ${INPUT_FILESLOCATION}

#echo "---------test-------"
#sha=$(git log -n 1 --pretty=format:"%H" origin/main)
res=$(git --no-pager diff --name-status @ @{upstream} ./documentation) # | sed "s/^/'/;s/$/'/"
echo $res
echo "-------------"
while IFS=$'\t' read -r -a tmp ; do
    # Renamed files
    if [[ ${tmp[0]} = R* ]]
    then
        echo "---Renamed---"
        echo "from ${tmp[2]}" 
        echo "to ${tmp[1]}"
    elif [[ ${tmp[0]} = M* ]]
    then
        echo "---Modified---"
        echo ${tmp[1]}
    elif [[ ${tmp[0]} = D* ]]
    then
        echo "---Deleted---"
        echo ${temp[1]}
    elif [[ ${tmp[0]} = A* ]]
    then
        echo "---Added---"
        echo ${temp[1]}
    else
        echo "---Other changes---"
        echo ${tmp[@]}
    fi
done <<< $res

# readarray arr <<< $res

# for i in "${arr[@]}"; do
#     readarray changes <<< $i
#     for j in "${changes[@]}"; do
#         echo $j
#     done
# done

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