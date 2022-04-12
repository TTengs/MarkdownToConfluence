import os, json
from posixpath import basename, dirname

# Returns "" if path == root
def get_prefix(path: str, root: str) -> str:
    if(not os.path.exists(path) or not os.path.exists(root)):
        raise FileNotFoundError
    if(path == root):
        return ""
    if(path.endswith("index.md") and "prefix.txt" in os.listdir(dirname(path))): # No prefix for index page in folder with prefix.txt (prefix is only for underpages)
        return ""
    if(os.path.isfile(path)):
        path = os.path.dirname(path)
    else:
        if("prefix.txt" in os.listdir(path)): # assume index.md, No prefix for index page in folder with prefix.txt (prefix is only for underpages)
            return ""
    while("prefix.txt" not in os.listdir(path)):
        path = os.path.dirname(path)
        if(path == root or path == ""):
            return ""
    with open(f"{path}/prefix.txt") as f:
        return f.readline()

# Returns "" if path == root
def get_page_name_from_path(path: str, root: str):
    if(path == root):
        return ""
    if(os.path.isdir(path)): # Assume index.md if path is dir
        path += "/index.md"
    path_arr = path.split('/')
    page_name = get_prefix(path, root)
    file_name = basename(path).replace(".md", "")
    if(file_name == "index"):
        page_name += path_arr[-2]
    else:
        page_name += file_name
    return page_name

# Returns the page name of the parent of the file in path. Returns default value if no parent exists i system
# Returns "" if path == root
def get_parent_name_from_path(path: str, root: str, default="Overview"):
    if(path == root):
        return ""
    if("settings.json" in os.listdir(root)):
        settings = json.load(open(root + "/settings.json"))
        if("parent_page" in settings.keys()):
            default = settings["parent_page"]
    if(os.path.isdir(path)): # Assume index.md if path is dir
        path += "/index.md"
    path_arr = path.split('/')
    file_name = basename(path).replace(".md", "")
    parent_name = ""
    if(file_name == "index"):
        if(len(path_arr) > 2 and path_arr[-3] != basename(root)):
            parent_name = get_prefix(dirname(dirname(path)), root) + path_arr[-3]
        else:
            parent_name = default
    else:
        parent_name = get_prefix(path, root) + path_arr[-2]
    return parent_name

def get_all_md_paths(root: str):
    paths = []      
    def traverse(directory):
        for filename in os.listdir(directory):
            f = os.path.join(directory, filename)
            # checking if it is a file
            if(os.path.isdir(f)):
                traverse(f)
            if(f.endswith('.md')):
                paths.append(f)
    traverse(root)
    return paths

def get_all_page_names_in_filesystem(root: str):
    page_names = []
    for path in get_all_md_paths(root):
        name = (get_page_name_from_path(path, root))
        print(name)
        page_names.append(name)
    return page_names
