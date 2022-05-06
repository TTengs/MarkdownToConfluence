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

    testfile = f'{test_docs}/CRUD/testfile.md'
    testfile2 = f'{test_docs}/CRUD/testfile2.md'
    testfile3 = f'{test_docs}/CRUD2/testfile.md'

    # Update content only
    with open(testfile, 'w') as file:
        file.write('# testfile')
    create_page(testfile)

    with open(testfile, 'w') as file:
        file.write('# testfile as changed')
    response = update_page_content(testfile)

    assert response.status_code == 200
    assert page_exists_in_space('testfile', os.environ['INPUT_CONFLUENCE_SPACE_KEY'])

    # Update title
    with open(testfile2, 'w') as file:
        file.write('# testfile2')
    os.remove(testfile)

    response = update_page_content(testfile2, testfile)
    assert response.status_code == 200
    assert page_exists_in_space('testfile2', os.environ['INPUT_CONFLUENCE_SPACE_KEY'])
    assert page_exists_in_space('testfile', os.environ['INPUT_CONFLUENCE_SPACE_KEY']) == False

    #Update parent
    with open(testfile3, 'w') as  file:
        file.write("# CRUD2 testifle")
    os.remove(testfile2)

    response = update_page_content(testfile3, testfile2)
    assert response.status_code == 200
    assert page_exists_in_space('testfile3', os.environ['INPUT_CONFLUENCE_SPACE_KEY'])
    assert page_exists_in_space('testfile2', os.environ['INPUT_CONFLUENCE_SPACE_KEY']) == False