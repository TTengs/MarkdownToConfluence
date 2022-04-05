#!/bin/bash

echo "Hello world"

echo "Hello $1"
time=$(date)
echo "::set-output name=time::$time"
#docker run -it -v /path/to/diagrams:/data minlag/mermaid-cli -i /data/diagram.mmd

#py ./mermaid_parser.py
#pandoc -s sample_readme.md -o sample_readme.html
#py ./json_parser_test.py