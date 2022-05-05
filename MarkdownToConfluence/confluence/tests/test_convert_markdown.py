from MarkdownToConfluence.confluence.convert_markdown import convert
import pathlib, os
import pytest
from unittest import mock
import MarkdownToConfluence.globals


@pytest.fixture(autouse=True)
def before():
    MarkdownToConfluence.globals.init()
    yield


@mock.patch.dict(os.environ, {"INPUT_FILESLOCATION": str(pathlib.Path(__file__).parent.resolve()) + '/testdocs'})
def test_convert():
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
    