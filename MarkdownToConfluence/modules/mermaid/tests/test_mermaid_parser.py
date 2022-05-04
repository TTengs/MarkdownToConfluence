from MarkdownToConfluence.modules.mermaid.mermaid_parser import run
import pathlib
import os

def test_parse_mermaid_macro():
    file = str(pathlib.Path(__file__).parent.resolve()) + '/testdocs/index.md'
    test_file = file.replace('.md', '_test.md')
    with open(file, 'r') as f:
        lines = f.readlines()
    with open(test_file, 'w') as f:
        for line in lines:
            f.write(line)
    run(test_file)
    assert os.path.exists(str(pathlib.Path(__file__).parent.resolve()) + '/testdocs/index_test-1.png')
    with open(test_file, 'r') as f:
        line = f.readline()
        assert line == f'![mermaid-1]({str(pathlib.Path(__file__).parent.resolve())}/testdocs/index_test-1.png)'
    os.remove(test_file)
    os.remove(str(pathlib.Path(__file__).parent.resolve()) + '/testdocs/index_test-1.png')