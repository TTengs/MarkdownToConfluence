#!/bin/bash
i=0
while results=$(find ./documentation -mindepth $i -maxdepth $i) && [[ -n $results ]]; do
    if [ ! "$results" == "./documentation" ];
    then
        readarray files <<< "$results"
        for f in "${files[@]}"; do
            file="$(echo ${f%\\n*})"
            if [[ ${file} == *.md ]]; then
                #echo "${file}"
                bash ./src/convert.sh "${file}"
            fi
        done
    fi
    ((i++))
done