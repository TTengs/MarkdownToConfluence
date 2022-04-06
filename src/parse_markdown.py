import sys
from mermaid_parser import parse_mermaid_macro

if __name__ == "__main__":
    parse_mermaid_macro(f"{str(sys.argv[1])}")