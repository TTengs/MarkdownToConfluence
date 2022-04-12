#!/bin/bash
echo "Hello world"
echo $(cd $INPUT_FILESLOCATION && ls)
#echo $(pwd)
#echo $(ls)
#echo ${INPUT_FILESLOCATION}
#echo "Hello $1"
#echo "sut den $2"
#time=$(date)
#echo "::set-output name=time::$time"
#docker run -it -v /path/to/diagrams:/data minlag/mermaid-cli -i /data/diagram.mmd
#py ./mermaid_parser.py
#pandoc -s sample_readme.md -o sample_readme.html
#py ./json_parser_test.py