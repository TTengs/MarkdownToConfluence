from posixpath import dirname, basename
import re, os
from MarkdownToConfluence.filetools import get_abs_path_from_relative
import globals

from PIL import Image

def convert_all_md_img_to_confluence_img(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    with open(filename, 'w') as f:
        for line in lines:
            res = convert_md_img_to_confluence_img(line, filename)
            if(res != None):
                f.write(res)
            else:
                f.write(line)

def convert_md_img_to_confluence_img(md_image_link: str, md_path: str):
    img = re.match(r'!\[(?P<alt>[^\]]*)\]\((?P<filename>.*?)(?=\"|\))(\"(?P<title>.*)\")?\)', md_image_link) #RegEx magic
    if(img != None and (img['filename'].strip().endswith('.png') or img['filename'].strip().endswith('.jpg'))):
        path = get_abs_path_from_relative(img['filename'], md_path)
        image = Image.open(path)
        width, height = image.size
        name = img['title'] if img["title"] != None else basename(img['filename'])
        globals.attachments.append((name, path))
        return(f'<ac:image ac:original-height="{str(height)}" ac:original-width="{str(width)}"><ri:attachment ri:filename="{name}"/></ac:image>\n')
    else:
        return None

def run(filename):
    return convert_all_md_img_to_confluence_img(filename)
            

#print(convert_md_img_to_confluence_img('![mermaid-1](/mnt/e/uni/bachelor/markdowntoconfluence/MarkdownToConfluence/file_parsing/tests/testdocs/index-1.png)'))
#<ac:image ac:align=\"center\" ac:layout=\"center\" ac:original-height=\"2048\" ac:original-width=\"1363\"><ri:attachment ri:filename=\"manden.jpg\" ri:version-at-save=\"1\" /></ac:image>
#<ac:image><ri:attachment ri:filename="{name}"/></ac:image>