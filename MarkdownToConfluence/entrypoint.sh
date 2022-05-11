#!/bin/bash
git init
git config --global --add safe.directory /github/workspace
git config --global core.pager "less -FRSX"

before=$(jq .before ${GITHUB_EVENT_PATH} | tr -d '"')
after=${GITHUB_SHA}

git fetch origin ${before} --depth=1
git fetch origin ${GITHUB_BASE_REF} --depth=1

echo "Checking for changes"
echo ""
res=""
if [[ ${GITHUB_EVENT_NAME} == "pull_request" ]]; then
    echo "On pull request"
    res=$(git --no-pager diff --name-status origin/${GITHUB_BASE_REF} -- ${INPUT_FILESLOCATION})
    #Find warnings
    #bash ./MarkdownToConfluence/convert_all.sh men som bare kun converter og smider warnings uden at uploade
elif [[ ${GITHUB_EVENT_NAME} == "push" ]]; then
    echo "On push"
    res=$(git --no-pager diff --name-status ${before}..${after} -- ${INPUT_FILESLOCATION})
fi

if [[ $res != "" ]]; then
    ReMoFilesArrOLD=()
    ReMoFilesArrNEW=()
    delFilesArr=()
    changedFilesArr=()
    addedFilesArr=()
    settingsFile=()
    while IFS=$'\t' read -r -a tmp ; do
        if [[ ${tmp[1]} == *settings.json || ${tmp[2]} == *settings.json ]]; then
            echo "Changes to settings.json found, converting all files."
            python3 /MarkdownToConfluence/confluence/delete_content.py --all
            bash /MarkdownToConfluence/create_all.sh
            exit 0
        fi
        if [[ ${INPUT_IS_PREVIEW} == true ]]; then
            echo "IS PREVIEW ${tmp[@]}"
            if [[ ${tmp[0]} != D* ]]; then
                if [[ ${tmp[0]} = R* ]]; then
                    addedFilesArr+=("${tmp[2]}")
                    echo "${tmp[2]}"
                else
                    addedFilesArr+=("${tmp[1]}")
                    echo "${tmp[2]}"
                fi
            fi
        # Renamed or moved files
        elif [[ ${tmp[0]} = R* ]]; then
            echo "---Renamed/Moved---"
            echo "from ${tmp[1]}"
            echo "to ${tmp[2]}"
            #TODO: rework, måske indsæt til et array som movedArr+=("${tmp[1]}", ${tmp[2]})
            ReMoFilesArrOLD+=("${tmp[1]}")
            ReMoFilesArrNEW+=("${tmp[2]}")
            #Skal kalde update med gamle og ny sti
        # Modified files
        elif [[ ${tmp[0]} = M* ]]; then
            echo "---Modified---"
            echo ${tmp[1]}
            changedFilesArr+=("${tmp[1]}")
        # Deleted files
        elif [[ ${tmp[0]} = D* ]]; then
            echo "---Deleted---"
            echo ${tmp[1]}
            delFilesArr+=("${tmp[1]}")
        # Added files
        elif [[ ${tmp[0]} = A* ]]; then
            echo "---Added---"
            echo ${tmp[1]}
            addedFilesArr+=("${tmp[1]}")
        else
            echo "---Other changes---"
            echo ${tmp[@]}
        fi
    done <<< $res

    if [[ ${INPUT_IS_PREVIEW} == true ]]; then
        python3 /MarkdownToConfluence/confluence/delete_content.py --all
    fi

    if [[ ! ${#delFilesArr[@]} -eq 0 ]]; then
        printf "\nDeleting pages:"
        for file in "${delFilesArr[@]}"
        do
            if [[ $file == *.md ]]; then
                python3 /MarkdownToConfluence/confluence/delete_content.py "${file}"
            else
                echo "${file} might not have been deleted"
            fi
        done
    fi

    if [[ ! ${#addedFilesArr[@]} -eq 0 ]]; then
        printf "\nCreating pages:"
        for file in "${addedFilesArr[@]}"
        do
            if [[ $file == *.md ]]; then
                python3 /MarkdownToConfluence/confluence/create_content.py "${file}"
            else
                echo "${file} might not have been created"
            fi
        done
    fi

    if [[ ! ${#changedFilesArr[@]} -eq 0 ]]; then
        printf "\nUpdating modified pages"
        for file in "${changedFilesArr[@]}"
        do
            if [[ $file == *.md ]]; then
                python3 /MarkdownToConfluence/confluence/update_content.py "${file}"
            else
                echo "Couldn't upload ${file}"
            fi
        done
    fi


    if [[ ! ${#ReMoFilesArrOLD[@]} -eq 0 ]]; then
        printf "\nRenaming or moving pages"
        for file in "${ReMoFilesArrOLD[@]}"
        do
            if [[ $file == *.md ]]; then
                python3 /MarkdownToConfluence/confluence/update_content.py "${ReMoFilesArrOLD[i]}" "${ReMoFilesArrNEW[i]}"
            else
                echo "${file} might not have been moved/renamed"
            fi
        done
    fi

    #printf "\nRemoving excess pages"
    #python3 /MarkdownToConfluence/confluence/delete_content.py --clean

else
    echo "There are no changes to documentation"
fi