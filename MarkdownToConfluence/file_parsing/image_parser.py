import re, pathlib

def convert_all_md_img_to_confluence_img(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    with open(filename, 'w') as f:
        for line in lines:
            img = re.match(r'!\[(?P<alt>[^\]]*)\]\((?P<filename>.*?)(?=\"|\))(\"(?P<title>.*)\")?\)', line) #RegEx magic
            if(img != None and (img['filename'].strip().endswith('.png') or img['filename'].strip().endswith('.jpg'))):
                name = img['title'] if img["title"] != None else img["alt"]
                f.write(f'<ac:image><ri:attachment ri:filename="{name}" /></ac:image>\n')
            else:
                f.write(line)

def convert_md_img_to_confluence_img(md_image_link: str):
    img = re.match(r'!\[(?P<alt>[^\]]*)\]\((?P<filename>.*?)(?=\"|\))(\"(?P<title>.*)\")?\)', md_image_link) #RegEx magic
    if(img != None and (img['filename'].strip().endswith('.png') or img['filename'].strip().endswith('.jpg'))):
        name = img['title'] if img["title"] != None else img["alt"]
        return(f'<ac:image><ri:attachment ri:filename="{name}" /></ac:image>\n')
    else:
        return None
            

#convert_md_image_to_confluence_img(str(pathlib.Path(__file__).parent.resolve()) + '/tests/testdocs/mermaid_final.md')
