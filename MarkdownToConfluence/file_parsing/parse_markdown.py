# TODO: remove this file
import sys
import MarkdownToConfluence.modules.mermaid as mermaid

def parse_markdown(filename):
    mermaid.convert(filename)


if __name__ == "__main__":
    parse_markdown(f"{str(sys.argv[1])}")

"""<ac:image><ri:attachment ri:filename="{diagram_name}" /></ac:image>"""