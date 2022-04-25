import os
from posixpath import dirname, basename

def get_abs_path_from_relative(relative_path: str, source_path: str):
    abs_path = ""
    if(os.path.isabs(relative_path)):
        abs_path = relative_path
    elif(os.path.exists(os.path.join(dirname(source_path), basename(relative_path)))):
        abs_path = os.path.join(dirname(source_path), basename(relative_path))
    else:
        abs_path = os.path.realpath(os.path.join(dirname(source_path), relative_path))
    return abs_path