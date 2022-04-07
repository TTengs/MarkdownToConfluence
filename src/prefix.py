import os, sys
from posixpath import dirname

def get_prefix(filepath: str, root: str) -> str:
    if(os.path.isfile(filepath)):
        filepath = os.path.dirname(filepath)
    while("prefix.txt" not in os.listdir(filepath)):
        filepath = os.path.dirname(filepath)
        if(filepath == root):
            return ""
    with open(f"{filepath}/prefix.txt") as f:
        return f.readline()

if __name__ == "__main__":
    get_prefix(sys.argv[1], sys.argv[2])
    