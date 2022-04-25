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
                path = ""
                if(os.path.isabs(reg["filename"])):
                    path = reg["filename"]
                elif(os.path.exists(os.path.join(dirname(filename), basename(reg['filename'])))):
                    path = os.path.join(dirname(filename), basename(reg['filename']))
                else:
                    path = os.path.abspath(reg["filename"])
                print("image path", path)
                image = convert_md_img_to_confluence_img(line, path)
                if(image != None):
                    f.write(image)
                else:
                    f.write(line) # TODO: Add support for other types of attachments
                attachments.append((name, path))
            else:
                f.write(line)
    return attachments