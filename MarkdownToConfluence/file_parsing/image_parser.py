from posixpath import dirname, basename
import re, os

from PIL import Image

def convert_all_md_img_to_confluence_img(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    with open(filename, 'w') as f:
        for line in lines:
            img = re.match(r'!\[(?P<alt>[^\]]*)\]\((?P<filename>.*?)(?=\"|\))(\"(?P<title>.*)\")?\)', line) #RegEx magic
            path = img['filename'] if os.path.isabs(img['filename']) else os.path.join(dirname(filename), basename(img['filename']))
            res = convert_md_img_to_confluence_img(line, path)
            if(line != None):
                f.write(res)
            else:
                f.write(line)
            """
            if(img != None and (img['filename'].strip().endswith('.png') or img['filename'].strip().endswith('.jpg'))): 
                name = img['title'] if img["title"] != None else img["alt"]
                f.write(f'<ac:image ac:align=\"center\" ac:layout=\"center\" ac:original-width=\"600\"><ri:attachment ri:filename={name}/></ac:image>\n')
            else:
                f.write(line)
            """

def convert_md_img_to_confluence_img(md_image_link: str, image_path: str):
    img = re.match(r'!\[(?P<alt>[^\]]*)\]\((?P<filename>.*?)(?=\"|\))(\"(?P<title>.*)\")?\)', md_image_link) #RegEx magic
    if(img != None and (img['filename'].strip().endswith('.png') or img['filename'].strip().endswith('.jpg'))):
        # image = cv2.imread(img['filename'])
        # dimensions = image.shape
        # height = dimensions[0]
        # width = dimensions[1]
        image = Image.open(image_path)
        width, height = image.size
        name = img['title'] if img["title"] != None else img["alt"]
        return(f'<ac:image ac:original-height="{str(height)}" ac:original-width="{str(width)}"><ri:attachment ri:filename="{name}" ri:version-at-save=\"1\" /></ac:image>\n')
    else:
        return None
            

#print(convert_md_img_to_confluence_img('![mermaid-1](/mnt/e/uni/bachelor/markdowntoconfluence/MarkdownToConfluence/file_parsing/tests/testdocs/index-1.png)'))
#<ac:image ac:align=\"center\" ac:layout=\"center\" ac:original-height=\"2048\" ac:original-width=\"1363\"><ri:attachment ri:filename=\"manden.jpg\" ri:version-at-save=\"1\" /></ac:image>
#<ac:image><ri:attachment ri:filename="{name}"/></ac:image>