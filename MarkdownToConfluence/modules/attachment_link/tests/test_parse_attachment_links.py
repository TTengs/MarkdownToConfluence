from MarkdownToConfluence.modules.attachment_link import convert_md_attachment_links_to_confluence_attachment_links
import MarkdownToConfluence.globals
import pytest, pathlib

@pytest.fixture(autouse=True)
def run_before():
    MarkdownToConfluence.globals.init()
    yield
    MarkdownToConfluence.globals.init()

def test_convert_md_attachment_links_to_confluence_attachment_links():
    root = str(pathlib.Path(__file__).parent.resolve())
    assert convert_md_attachment_links_to_confluence_attachment_links('![test](./zip_test.zip)', root) == '<p class=\"media-group\"><ac:structured-macro ac:name=\"view-file\" ac:schema-version=\"1\" ac:macro-id=\"ce17b5c6-cfe6-4a77-92aa-7b810863f634\"><ac:parameter ac:name=\"name\"><ri:attachment ri:filename="zip_test.zip" ri:version-at-save=\"2\" /></ac:parameter></ac:structured-macro></p><p />'
    assert len(MarkdownToConfluence.globals.attachments) == 1
    assert MarkdownToConfluence.globals.attachments[0] == ('zip_test.zip', f'{root}/zip_test.zip')