import sys
from .mermaid_parser import parse_mermaid_macro

def parse_markdown(filename):
    parse_mermaid_macro(filename)

if __name__ == "__main__":
    parse_markdown(f"{str(sys.argv[1])}")

"""<ac:image><ri:attachment ri:filename="{diagram_name}" /></ac:image>"""