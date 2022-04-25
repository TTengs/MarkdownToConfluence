from posixpath import dirname
from MarkdownToConfluence.filetools.paths import get_abs_path_from_relative
import pathlib, os


def test_get_abs_path_from_relative():
    source_path =str(pathlib.Path(__file__).resolve())
    assert str(get_abs_path_from_relative('./testdocs/page 1/index-1.png', source_path, './MarkdownToConfluence')) == f'{dirname(source_path)}/testdocs/page 1/index-1.png'
    assert str(get_abs_path_from_relative('MarkdownToConfluence/filetools/tests/testdocs/page 1/index.md', source_path, './MarkdownToConfluence')) == f'{(dirname(source_path))}/testdocs/page 1/index.md'
    assert str(get_abs_path_from_relative('../DAM Center 5/index.md', f'{dirname(source_path)}/testdocs/page 1/index.md', './MarkdownToConfluence')) == f'{dirname(source_path)}/testdocs/DAM Center 5/index.md'

