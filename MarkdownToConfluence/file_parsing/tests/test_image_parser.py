from MarkdownToConfluence.file_parsing.image_parser import convert_md_img_to_confluence_img
import os, pathlib

def test_convert_md_img_to_confluence_img():
    root=str(pathlib.Path(__file__).parent.resolve()) + '/testdocs'
    filepath = f'{root}/images/markdown/image.md'
    with open(filepath, 'r') as f:
        lines = f.readlines()
    with open("testfile.md", "w") as f:
        for line in lines:
            f.write(convert_md_img_to_confluence_img(line, filepath))
    with open("testfile.md", "r") as f:
        assert f.readline().strip('\n') == '<ac:image ac:original-height="144" ac:original-width="70"><ri:attachment ri:filename="title"/></ac:image>'
        assert f.readline().strip('\n') == '<ac:image ac:original-height="144" ac:original-width="70"><ri:attachment ri:filename="title"/></ac:image>'
        assert f.readline().strip('\n') == '<ac:image ac:original-height="144" ac:original-width="70"><ri:attachment ri:filename="title"/></ac:image>'
        assert f.readline().strip('\n') == '<ac:image ac:original-height="144" ac:original-width="70"><ri:attachment ri:filename="alt"/></ac:image>'
        assert f.readline().strip('\n') == '<ac:image ac:original-height="144" ac:original-width="70"><ri:attachment ri:filename="alt"/></ac:image>'
        assert f.readline().strip('\n') == '<ac:image ac:original-height="144" ac:original-width="70"><ri:attachment ri:filename="alt"/></ac:image>'
    #os.remove("testfile.md")
    