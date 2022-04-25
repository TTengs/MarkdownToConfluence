import os
from posixpath import dirname, basename

def get_abs_path_from_relative(relative_path: str, source_path: str, root=os.environ.get('INPUT_FILESLOCATION')):
    _root = os.path.abspath(root)
    if(os.path.isfile(source_path)):
        source_path = dirname(source_path)
    relative_path = relative_path.strip()
    source_path = source_path.strip()
    abs_path = ""
    if(os.path.isabs(relative_path)):
        if(os.fspath(relative_path).startswith(os.getcwd())):
            print(1.1)
            abs_path = relative_path
        else:
            print(1.2)
            abs_path = os.path.join(_root, relative_path)
    elif(os.path.exists(str(os.path.realpath((os.path.join(_root, source_path, relative_path))).strip()))):
        print(2)
        abs_path = (os.path.join(_root, source_path, relative_path)).strip()
    else:
        print(3)
        abs_path = os.path.abspath(relative_path)
    print(source_path, '\n', relative_path, '\n', os.path.realpath(abs_path), '\n')

    # abs_path = ""
    # if(os.path.exists(os.path.join(dirname(source_path), basename(relative_path)))):
    #     abs_path = os.path.join(dirname(source_path), basename(relative_path))
    # elif(not os.path.isabs(relative_path)):
    #     abs_path = os.path.realpath(os.path.join(dirname(source_path), relative_path))
    # else:
    #     abs_path = os.path.abspath(relative_path)
    return os.path.realpath(abs_path)