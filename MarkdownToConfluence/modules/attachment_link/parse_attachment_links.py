from os import link
from posixpath import dirname, basename
import re
from MarkdownToConfluence.utils.paths import get_abs_path_from_relative
import MarkdownToConfluence.globals

def convert_all_md_attachment_links_to_confluence_attachment_links(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    with open(filename, 'w') as f:
        for line in lines:
            res = convert_md_attachment_links_to_confluence_attachment_links(line, filename)
            f.write(res)

def convert_md_attachment_links_to_confluence_attachment_links(line: str, md_path: str):
    links = re.findall(r'(!\[(?P<alt>[^\]]*)\]\((?P<filename>.*?)(?=\"|\))(\"(?P<title>.*)\")?\))', line)
    new_line = line
    for link in links:
        print(link)
        if(link != None and not (link[2].strip().endswith('.png') or link[2].strip().endswith('.jpg'))):
            path = get_abs_path_from_relative(link[2], md_path)
            name = link[4] if link[4] != '' else basename(link[2])
            MarkdownToConfluence.globals.attachments.append((name, path))
            new_line = new_line.replace(link[0], f'<p class=\"media-group\"><ac:structured-macro ac:name=\"view-file\" ac:schema-version=\"1\" ac:macro-id=\"ce17b5c6-cfe6-4a77-92aa-7b810863f634\"><ac:parameter ac:name=\"name\"><ri:attachment ri:filename="{name}" ri:version-at-save=\"2\" /></ac:parameter></ac:structured-macro></p><p />')
    return new_line

def run(filename):
    return convert_all_md_attachment_links_to_confluence_attachment_links(filename)


