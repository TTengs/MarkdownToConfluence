from MarkdownToConfluence.modules.mermaid.mermaid_parser import run
import pathlib
import os

def test_parse_mermaid_macro():
    file = str(pathlib.Path(__file__).parent.resolve()) + '/testdocs/index.md'
    run(file)
    assert os.path.exists(str(pathlib.Path(__file__).parent.resolve()) + '/testdocs/index-1.png')
    assert os.path.exists(str(pathlib.Path(__file__).parent.resolve()) + '/testdocs/index_final.md')
    with open(str(pathlib.Path(__file__).parent.resolve()) + '/testdocs/index_final.md', 'r') as f:
        line = f.readline()
        assert line == f'![mermaid-1]({str(pathlib.Path(__file__).parent.resolve())}/testdocs/index-1.png)'
    os.remove(str(pathlib.Path(__file__).parent.resolve()) + '/testdocs/index_final.md')
    os.remove(str(pathlib.Path(__file__).parent.resolve()) + '/testdocs/index-1.png')