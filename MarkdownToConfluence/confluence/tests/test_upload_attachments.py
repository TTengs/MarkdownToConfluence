import pathlib
from MarkdownToConfluence.confluence.upload_attachments import upload_attachment

def test_upload_attachment():
    upload_attachment("page 3", "test image", str(pathlib.Path(__file__).parent.resolve()) + '/test.png')