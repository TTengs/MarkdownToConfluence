from MarkdownToConfluence.file_parsing.image_parser import convert_md_img_to_confluence_img
import re

def parse_and_get_attachments(filename):
    attachments = []
    with open(filename, 'r') as f:
        lines = f.readlines()
    with open(filename, 'w') as f:
        for line in lines:
            reg = re.match(r'!\[(?P<alt>[^\]]*)\]\((?P<filename>.*?)(?=\"|\))(\"(?P<title>.*)\")?\)', line)
            name = reg['title'] if reg['title'] != None else reg['alt']
            if (reg != None):
                image = convert_md_img_to_confluence_img(line)
                if(image != None):
                    f.write(image)
                else:
                    f.write(line) # TODO: Add support for other types of attachments
                attachments.append((name, reg['filename']))
            else:
                f.write(line)
    return attachments