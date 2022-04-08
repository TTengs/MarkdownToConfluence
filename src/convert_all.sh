#!/bin/sh
#Delete pages from confluence, that dont exist in the filesystem
python3 /src/delete_content.py "~955037829" "$INPUT_FILESLOCATION"

#Convert all files and ypload
find $INPUT_FILESLOCATION -type f -name "*.md" -not -path "$INPUT_FILESLOCATION" -print0 | xargs -0 -I file bash /src/convert.sh file
#find ./documentation -type f -name "*.html" -print0 | xargs -0 -I file rm file