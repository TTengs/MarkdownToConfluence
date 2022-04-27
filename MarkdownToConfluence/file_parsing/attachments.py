from posixpath import dirname, basename
#from MarkdownToConfluence.modules.image.image_parser import convert_md_img_to_confluence_img
import re, os
from MarkdownToConfluence.filetools import get_abs_path_from_relative
"""
def parse_and_get_attachments(filename):
    attachments = []
    with open(filename, 'r') as f:
        lines = f.readlines()
    with open(filename, 'w') as f:
        for line in lines:
            reg = re.match(r'!\[(?P<alt>[^\]]*)\]\((?P<filename>.*?)(?=\"|\))(\"(?P<title>.*)\")?\)', line)
            if (reg != None):
                name = reg['title'] if reg['title'] != None else reg['alt']
                image = convert_md_img_to_confluence_img(line, filename)
                if(image != None):
                    f.write(image)
                else:
                    f.write(line) # TODO: Add support for other types of attachments
                path = get_abs_path_from_relative(reg['filename'], filename)
                attachments.append((name, path))
            else:
                f.write(line)
    return attachments
"""
