from MarkdownToConfluence.file_parsing.image_parser import convert_all_md_img_to_confluence_img
import os

def test_convert_md_img_to_confluence_img():
    with open("testfile.md", "w") as f:
        f.write('![alt](path/to/image.png "title")\n')
        f.write('![alt](path/to/image.jpg "title")\n')
        f.write('![alt](path with space/to/image.jpg "title")\n')
        f.write('![alt](path/to/image.png)\n')
        f.write('![alt](path/to/image.jpg)\n')
    convert_all_md_img_to_confluence_img("testfile.md")
    with open("testfile.md", "r") as f:
        assert f.readline().strip('\n') == '<ac:image><ri:attachment ri:filename="title"/></ac:image>'
        assert f.readline().strip('\n') == '<ac:image><ri:attachment ri:filename="title"/></ac:image>'
        assert f.readline().strip('\n') == '<ac:image><ri:attachment ri:filename="title"/></ac:image>'
        assert f.readline().strip('\n') == '<ac:image><ri:attachment ri:filename="alt"/></ac:image>'
        assert f.readline().strip('\n') == '<ac:image><ri:attachment ri:filename="alt"/></ac:image>'
    #os.remove("testfile.md")
    