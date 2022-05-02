from posixpath import dirname, basename
from MarkdownToConfluence.file_parsing.image_parser import convert_md_img_to_confluence_img
import re, os

def parse_and_get_attachments(filename):
    attachments = []
    with open(filename, 'r') as f:
        lines = f.readlines()
    with open(filename, 'w') as f:
        for line in lines:
            reg = re.match(r'!\[(?P<alt>[^\]]*)\]\((?P<filename>.*?)(?=\"|\))(\"(?P<title>.*)\")?\)', line)
            if (reg != None):
                name = reg['title'] if reg['title'] != None else reg['alt']
                image = convert_md_img_to_confluence_img(line)
                if(image != None):
                    f.write(image)
                else:
                    f.write(line) # TODO: Add support for other types of attachments
                path = reg['filename'] if os.path.isabs(reg['filename']) else os.path.join(dirname(filename), basename(reg['filename']))
                attachments.append((name, path))
            else:
                f.write(line)
    return attachments