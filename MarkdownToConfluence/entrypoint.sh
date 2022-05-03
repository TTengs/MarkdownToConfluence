#!/bin/bash
git init
git config --global --add safe.directory /github/workspace
git config --global core.pager "less -FRSX"

git diff --name-status origin/main ${INPUT_FILESLOCATION}
echo "Checking for changes"
echo ""

if [[ $(git status --porcelain ${INPUT_FILESLOCATION}) ]]; then
    res=$(git --no-pager diff --name-status origin/main ${INPUT_FILESLOCATION})
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
else
    echo "There are no changes to documentation"
fi

echo "
All files
"

echo "Modified files"
for i in "${modFilesArr[@]}"
do
    echo $i
    bash ./MarkdownToConfluence/Convert.sh "$i"
done

echo "Added files"
for i in "${addedFilesArr[@]}"
do
    echo $i
done