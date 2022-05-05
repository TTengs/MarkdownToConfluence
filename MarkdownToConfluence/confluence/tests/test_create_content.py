from unittest import mock
import pathlib, os, pytest

test_docs = str(pathlib.Path(__file__).parent.resolve()) + '/testdocs'

@pytest.fixture(autouse=True)
def reset_confluence():
    from MarkdownToConfluence.confluence.delete_content import delete_all_pages_in_space
    
    k = mock.patch.dict(os.environ, {"INPUT_FILESLOCATION": test_docs})
    k.start()

    delete_all_pages_in_space(os.environ.get('INPUT_CONFLUENCE_SPACE_KEY'))
    
    yield
    k.stop()

def test_create_page():
    from MarkdownToConfluence.confluence.create_content import create_page

    with open(f'{test_docs}/testfile.md', 'w') as file:
        file.write('# testfile')
    response = create_page(f'{test_docs}/testfile.md')
    assert response.status_code == 200

    from MarkdownToConfluence.confluence.confluence_utils import page_exists_in_space
    assert page_exists_in_space('testfile', os.environ['INPUT_CONFLUENCE_SPACE_KEY'])