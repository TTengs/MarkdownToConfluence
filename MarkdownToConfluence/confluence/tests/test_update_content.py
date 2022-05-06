from unittest import mock
import pathlib, os, pytest
from urllib import response

test_docs = str(pathlib.Path(__file__).parent.resolve()) + '/testdocs'

@pytest.fixture(autouse=True)
def reset_confluence():
    from MarkdownToConfluence.confluence.delete_content import delete_all_pages_in_space
    
    k = mock.patch.dict(os.environ, {"INPUT_FILESLOCATION": test_docs})
    k.start()

    delete_all_pages_in_space(os.environ.get('INPUT_CONFLUENCE_SPACE_KEY'))
    
    yield

    k.stop()

def test_update_page_content():
    from MarkdownToConfluence.confluence.update_content import update_page_content
    from MarkdownToConfluence.confluence.create_content import create_page
    from MarkdownToConfluence.confluence.confluence_utils import page_exists_in_space

    with open(f'{test_docs}/CRUD/testfile.md', 'w') as file:
        file.write('# testfile')
    create_page(f'{test_docs}/CRUD/testfile.md')

    with open(f'{test_docs}/CRUD/testfile.md', 'w') as file:
        file.write('# testfile as changed')
    response = update_page_content(f'{test_docs}/CRUD/testfile.md')

    assert response.status_code == 200
    assert page_exists_in_space('testfile', os.environ['INPUT_CONFLUENCE_SPACE_KEY'])

    with open(f'{test_docs}/CRUD/testfile2.md', 'w') as file:
        file.write('# testfile2')
    os.remove(f'{test_docs}/CRUD/testfile.md')

    response = update_page_content(f'{test_docs}/CRUD/testfile2.md', f'{test_docs}/CRUD/testfile.md')
    assert response.status_code == 200
    assert page_exists_in_space('testfile2', os.environ['INPUT_CONFLUENCE_SPACE_KEY'])
    assert page_exists_in_space('testfile', os.environ['INPUT_CONFLUENCE_SPACE_KEY']) == False
