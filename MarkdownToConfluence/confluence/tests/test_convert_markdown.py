from ..convert_markdown import convert
import pathlib, os

def test_convert():
    root=str(pathlib.Path(__file__).parent.resolve()) + '/testdocs'
    filename = root + '/convert/test.md'
    page_name, parent_name = convert(filename, root)
    assert page_name == 'test'
    assert parent_name == 'convert'
    assert os.path.exists(filename.replace('.md', '.html'))
    
test_convert()