#!bin/sh

PATHNAME=$1
DIR="$(dirname "${PATHNAME}")"
FILE="$(basename "${PATHNAME}")"
FILENAME="$(echo "${FILE}" |cut -f 1 -d '.')"
echo "[${PATHNAME}] [${DIR}] [${FILENAME}]"
BASE_PATH=$(pwd)

#Conversion
#grep -q "\`\`\`mermaid" "$BASE_PATH/$PATHNAME/index.template.md" && docker run -v "$BASE_PATH"/"$PATHNAME":/data minlag/mermaid-cli -i /data/index.template.md -o /data/index.png
python3 /src/parse_markdown.py "$PATHNAME"
pandoc "$DIR"/"${FILENAME}_final.md" -f markdown -t html -o "$DIR"/"${FILENAME}".html
rm "$DIR/${FILENAME}_final.md"

#Uploading
python3 /src/upload_documentation.py "$PATHNAME" "$FILENAME"
