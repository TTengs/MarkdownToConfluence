import pathlib
import pytest
import collections
import os
from MarkdownToConfluence.filetools.page_file_info import get_page_name_from_path, get_parent_name_from_path, get_prefix, get_all_md_paths, get_all_page_names_in_filesystem

def test_get_prefix():
    root=str(pathlib.Path(__file__).parent.resolve()) + '/testdocs'
    test_path=f'{root}/page 1/index.md'
    assert type(get_prefix(test_path, root)) is str
    assert get_prefix(test_path, root) == ""
    test_path=f'{root}/page 1'
    assert type(get_prefix(test_path, root)) is str
    assert get_prefix(test_path, root) == ""
    test_path=f'{root}/DAM Center 5/DC 5.0/5 Security/index.md'
    assert type(get_prefix(test_path, root)) is str
    assert get_prefix(test_path, root) == "DC5.0.0 "
    test_path=f'{root}/DAM Center 5/DC 5.0/5 Security/Configuring CORS.md'
    assert type(get_prefix(test_path, root)) is str
    assert get_prefix(test_path, root) == "DC5.0.0 "
    assert type(get_prefix(test_path, root)) is str
    assert get_prefix(root, root) == ""
    with pytest.raises(FileNotFoundError):
        get_prefix("path/that/dont/exists.md", root)
    with pytest.raises(FileNotFoundError):
        get_prefix(f'{root}/page 1/index.md', 'path/that/dont/exist')

def test_get_page_name_from_path():
    root=str(pathlib.Path(__file__).parent.resolve()) + '/testdocs'
    test_path=f'{root}/page 1/index.md'
    assert type(get_page_name_from_path(test_path, root)) is str
    assert get_page_name_from_path(test_path, root) == 'page 1'
    test_path=f'{root}/page 1'
    assert type(get_page_name_from_path(test_path, root)) is str
    assert get_page_name_from_path(test_path, root) == 'page 1'
    test_path=f'{root}/DAM Center 5/DC 5.0/5 Security/index.md'
    assert type(get_page_name_from_path(test_path, root)) is str
    assert get_page_name_from_path(test_path, root) == 'DC5.0.0 5 Security'
    test_path=f'{root}/DAM Center 5/DC 5.0/5 Security/Configuring CORS.md'
    assert type(get_page_name_from_path(test_path, root)) is str
    assert get_page_name_from_path(test_path, root) == 'DC5.0.0 Configuring CORS'
    test_path=root
    assert type(get_page_name_from_path(test_path, root)) is str
    assert get_page_name_from_path(test_path, root) == ''
    with pytest.raises(FileNotFoundError):
        get_page_name_from_path("path/that/dont/exists.md", root)
    with pytest.raises(FileNotFoundError):
        get_page_name_from_path(f'{root}/page 1/index.md', 'path/that/dont/exist')

def test_get_parent_name_from_path():
    root=str(pathlib.Path(__file__).parent.resolve()) + '/testdocs'
    test_path=f'{root}/page 1/index.md'
    assert type(get_parent_name_from_path(test_path, root)) is str
    assert get_parent_name_from_path(test_path, root) == "parent page test name"
    test_path=f'{root}/page 1'
    assert type(get_parent_name_from_path(test_path, root)) is str
    assert get_parent_name_from_path(test_path, root) == "parent page test name"
    test_path=f'{root}/DAM Center 5/DC 5.0/5 Security/index.md'
    assert type(get_parent_name_from_path(test_path, root)) is str
    assert get_parent_name_from_path(test_path, root) == 'DC 5.0'
    test_path=f'{root}/DAM Center 5/DC 5.0/5 Security/Configuring CORS.md'
    assert type(get_parent_name_from_path(test_path, root)) is str
    assert get_parent_name_from_path(test_path, root) == 'DC5.0.0 5 Security'
    assert type(get_parent_name_from_path(root, root)) is str
    assert get_parent_name_from_path(root, root) == ''
    with pytest.raises(FileNotFoundError):
        get_parent_name_from_path("path/that/dont/exists.md", root)
    with pytest.raises(FileNotFoundError):
        get_parent_name_from_path(f'{root}/page 1/index.md', 'path/that/dont/exist')

def test_get_all_md_paths():
    root=str(pathlib.Path(__file__).parent.resolve()) + '/testdocs'
    testpaths=[f'{root}/DAM Center 5/DC 5.0/5 Security/Configuring CORS.md', f'{root}/DAM Center 5/DC 5.0/5 Security/index.md',
    f'{root}/DAM Center 5/DC 5.0/index.md', f'{root}/DAM Center 5/index.md', f'{root}/page 1/index.md', f'{root}/page 1/page 1.1/index.md',
    f'{root}/page 1/page 1.1/abe.md']
    paths = get_all_md_paths(root)
    assert type(paths) is list
    abspaths = [os.path.abspath(path) for path in paths]
    abstestpaths = [os.path.abspath(path) for path in testpaths]
    assert collections.Counter(abspaths) == collections.Counter(abstestpaths)
    for path in abspaths:
        assert os.path.exists(path)

def test_get_all_page_names_in_filesystem():
    root= str(pathlib.Path(__file__).parent.resolve()) + '/testdocs'
    testnames = ['DC5.0.0 5 Security', 'DC5.0.0 Configuring CORS', 'DC 5.0', 'DAM Center 5', 'page 1', 'page 1.1', 'abe']
    names = get_all_page_names_in_filesystem(root)
    print(names)
    assert type(names) is list
    assert collections.Counter(names) == collections.Counter(testnames)
    assert len(names) == len(set(names))