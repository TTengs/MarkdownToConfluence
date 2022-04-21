#!/bin/bash
for i in ${{ steps.getfile.outputs.files }}
do
    echo $i
done

echo "-------"

echo ${{ steps.getfile.outputs.files }}