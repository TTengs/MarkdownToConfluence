#!bin/sh

PATHNAME=$1
BASE_PATH=$(pwd)

#Conversion
#grep -q "\`\`\`mermaid" "$BASE_PATH/$PATHNAME/index.template.md" && docker run -v "$BASE_PATH"/"$PATHNAME":/data minlag/mermaid-cli -i /data/index.template.md -o /data/index.png
python3 ./scripts/parse_markdown.py "$PATHNAME"
pandoc "$PATHNAME"/index.md -f markdown -t html -s -o "$PATHNAME"/index.html --metadata pagetitle="$PATHNAME"
rm "$PATHNAME/index.md"

#Uploading
#python3 ./scripts/upload_documentation.py "$PATHNAME"
