#!/bin/sh

echo "Hello world"

ls
cd documentation
ls
#printenv
echo "${INPUT_DOCS_PATH}"

echo "Wat"

#echo "Hello $1"
#echo "sut den $2"

#time=$(date)
#echo "::set-output name=time::$time"
#docker run -it -v /path/to/diagrams:/data minlag/mermaid-cli -i /data/diagram.mmd

#py ./mermaid_parser.py
#pandoc -s sample_readme.md -o sample_readme.html
#py ./json_parser_test.py