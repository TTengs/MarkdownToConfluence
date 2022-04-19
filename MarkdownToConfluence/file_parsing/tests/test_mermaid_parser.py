from MarkdownToConfluence.file_parsing.mermaid_parser import parse_mermaid_macro
import pathlib
import os

def test_parse_mermaid_macro():
    file = str(pathlib.Path(__file__).parent.resolve()) + '/testdocs/mermaid.md'
    parse_mermaid_macro(file)
    assert os.path.exists(str(pathlib.Path(__file__).parent.resolve()) + '/testdocs/mermaid-1.png')
    assert os.path.exists(str(pathlib.Path(__file__).parent.resolve()) + '/testdocs/mermaid_final.md')
    with open(str(pathlib.Path(__file__).parent.resolve()) + '/testdocs/mermaid_final.md', 'r') as f:
        line = f.readline()
        assert line == f'![mermaid-1]({str(pathlib.Path(__file__).parent.resolve())}/testdocs/mermaid-1.png)'
    #os.remove(str(pathlib.Path(__file__).parent.resolve()) + '/testdocs/mermaid_final.md')
    #os.remove(str(pathlib.Path(__file__).parent.resolve()) + '/testdocs/mermaid-1.png')