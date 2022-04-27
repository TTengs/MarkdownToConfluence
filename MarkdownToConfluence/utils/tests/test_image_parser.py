from MarkdownToConfluence.utils.image_parser import run
from MarkdownToConfluence import globals
import os, pathlib

def test_convert_md_img_to_confluence_img():
    globals.init()
    root=str(pathlib.Path(__file__).parent.resolve()) + '/testdocs'
    filepath = f'{root}/markdown/image.md'
    test_path = filepath.replace('.md', '_test.md')
    print(test_path)
    with open(filepath, 'r') as i, open(test_path, 'w') as o:
        lines = i.readlines()
        for line in lines:
            o.write(line)
    run(test_path)
    with open(test_path, "r") as f:
        assert f.readline().strip('\n') == '<ac:image ac:original-height="144" ac:original-width="70"><ri:attachment ri:filename="title"/></ac:image>'
        assert f.readline().strip('\n') == '<ac:image ac:original-height="144" ac:original-width="70"><ri:attachment ri:filename="title"/></ac:image>'
        assert f.readline().strip('\n') == '<ac:image ac:original-height="144" ac:original-width="70"><ri:attachment ri:filename="title"/></ac:image>'
        assert f.readline().strip('\n') == '<ac:image ac:original-height="144" ac:original-width="70"><ri:attachment ri:filename="image.png"/></ac:image>'
        assert f.readline().strip('\n') == '<ac:image ac:original-height="144" ac:original-width="70"><ri:attachment ri:filename="image.png"/></ac:image>'
        assert f.readline().strip('\n') == '<ac:image ac:original-height="144" ac:original-width="70"><ri:attachment ri:filename="image.png"/></ac:image>'
    os.remove(test_path)
    