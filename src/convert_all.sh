#!/bin/sh

find $INPUT_FILESLOCATION -type f -name "*.md" -not -path "$INPUT_FILESLOCATION" -print0 | xargs -0 -I file bash /src/convert.sh file
#find ./documentation -type f -name "*.html" -print0 | xargs -0 -I file rm file