#!/bin/sh
#Delete pages from confluence, that dont exist in the filesystem
#python3 /src/delete_content.py "~955037829" "$INPUT_FILESLOCATION"

#Convert all files and upload
find "${INPUT_FILESLOCATION}" -type f -name "*.md" -not -path "${INPUT_FILESLOCATION}" -print0 | xargs -0 -I file bash /MarkdownToConfluence/convert.sh file