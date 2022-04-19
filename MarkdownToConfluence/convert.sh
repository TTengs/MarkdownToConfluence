#!bin/sh

PATHNAME=$1
#ROOT="$INPUT_FILESLOCATION"
DIR="$(dirname "${PATHNAME}")"
FILE="$(basename "${PATHNAME}")"
FILENAME="$(echo ${FILE%.*})"
#echo "[${PATHNAME}] [${DIR}] [${FILENAME}]"
BASE_PATH=$(pwd)

#Conversion
echo "$BASE_PATH"/"$PATHNAME"
python3 /MarkdownToConfluence/file_parsing/parse_markdown.py "$PATHNAME"
pandoc "$DIR"/"${FILENAME}_final.md" -f markdown -t html -o "$DIR"/"${FILENAME}".html
rm "$DIR/${FILENAME}_final.md"

#Uploading
python3 /MarkdownToConfluence/main.py "$PATHNAME" "$ROOT"
rm "$DIR/${FILENAME}.html"

