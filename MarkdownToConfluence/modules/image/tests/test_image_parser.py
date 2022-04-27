from MarkdownToConfluence.modules.image.image_parser import run
import os, pathlib

def test_convert_md_img_to_confluence_img():
    root=str(pathlib.Path(__file__).parent.resolve()) + '/testdocs'
    filepath = f'{root}/images/markdown/image.md'
    run(filepath)
    with open("testfile.md", "r") as f:
        assert f.readline().strip('\n') == '<ac:image ac:original-height="144" ac:original-width="70"><ri:attachment ri:filename="title"/></ac:image>'
        assert f.readline().strip('\n') == '<ac:image ac:original-height="144" ac:original-width="70"><ri:attachment ri:filename="title"/></ac:image>'
        assert f.readline().strip('\n') == '<ac:image ac:original-height="144" ac:original-width="70"><ri:attachment ri:filename="title"/></ac:image>'
        assert f.readline().strip('\n') == '<ac:image ac:original-height="144" ac:original-width="70"><ri:attachment ri:filename="alt"/></ac:image>'
        assert f.readline().strip('\n') == '<ac:image ac:original-height="144" ac:original-width="70"><ri:attachment ri:filename="alt"/></ac:image>'
        assert f.readline().strip('\n') == '<ac:image ac:original-height="144" ac:original-width="70"><ri:attachment ri:filename="alt"/></ac:image>'
    #os.remove("testfile.md")
    