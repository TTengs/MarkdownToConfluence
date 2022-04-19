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
#grep -q "\`\`\`mermaid" "$BASE_PATH/$PATHNAME" && docker run -v "$BASE_PATH"/"$DIR":/data minlag/mermaid-cli -i /data/"$FILE" -o /data/"$FILENAME".png
#grep -q "\`\`\`mermaid" "$BASE_PATH/$PATHNAME" && markdown_mermaid_to_images -m "$BASE_PATH/$PATHNAME" -o "$BASE_PATH/$DIR"
python3 /MarkdownToConfluence/file_parsing/parse_markdown.py "$PATHNAME"
pandoc "$DIR"/"${FILENAME}_final.md" -f markdown -t html -o "$DIR"/"${FILENAME}".html
rm "$DIR/${FILENAME}_final.md"

#Uploading
#python3 /MarkdownToConfluence/main.py "$PATHNAME" "$ROOT"
rm "$DIR/${FILENAME}.html"

