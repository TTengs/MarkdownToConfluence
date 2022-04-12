#!bin/sh

PATHNAME=$1
ROOT="$INPUT_FILESLOCATION"
DIR="$(dirname "${PATHNAME}")"
FILE="$(basename "${PATHNAME}")"
FILENAME="$(echo ${FILE%.*})"
#echo "[${PATHNAME}] [${DIR}] [${FILENAME}]"
BASE_PATH=$(pwd)

#Conversion
#grep -q "\`\`\`mermaid" "$BASE_PATH/$PATHNAME/index.template.md" && docker run -v "$BASE_PATH"/"$PATHNAME":/data minlag/mermaid-cli -i /data/index.template.md -o /data/index.png
python3 /MarkdownToConfluence/parse_markdown/parse_markdown.py "$PATHNAME"
pandoc "$DIR"/"${FILENAME}_final.md" -f markdown -t html -o "$DIR"/"${FILENAME}".html
rm "$DIR/${FILENAME}_final.md"

#Uploading
python3 /MarkdownToConfluence/upload_documentation.py "$PATHNAME" "$ROOT"
rm "$DIR/${FILENAME}.html"

