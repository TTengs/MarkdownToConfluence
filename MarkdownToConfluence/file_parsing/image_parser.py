import re, pathlib

def convert_md_image_to_confluence_img(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    with open(filename, 'w') as f:
        for line in lines:
            img = re.match(r'!\[[^\]]*\]\((.*?)\s*("(?:.*[^"])")?\s*\)', line)
            print(img)
            

convert_md_image_to_confluence_img(str(pathlib.Path(__file__).parent.resolve()) + '/tests/testdocs/mermaid.md')
"""<ac:image><ri:attachment ri:filename="{diagram_name}" /></ac:image>"""