import pathlib, os
import pytest
from unittest import mock


@pytest.fixture(autouse=True)
def before():
    import MarkdownToConfluence.globals
    
    MarkdownToConfluence.globals.init(str(pathlib.Path(__file__).parent.resolve()) + '/testdocs/settings.json')
    yield


@mock.patch.dict(os.environ, {"INPUT_FILESLOCATION": str(pathlib.Path(__file__).parent.resolve()) + '/testdocs'})
def test_convert():
    from MarkdownToConfluence.confluence.convert_markdown import convert

    root=str(pathlib.Path(__file__).parent.resolve()) + '/testdocs'
    filename = root + '/convert/test.md'
    page_name, parent_name = convert(filename, root)
    assert page_name == 'test'
    assert parent_name == 'convert'
    assert os.path.exists(filename.replace('.md', '.html'))
    assert os.path.exists(filename.replace('.md', '_final.md'))
    assert os.path.exists(filename.replace('.md', '_final-1.png'))
    os.remove(filename.replace('.md', '_final.md'))
    os.remove(filename.replace('.md', '_final-1.png'))
    os.remove(filename.replace('.md', '.html'))
    