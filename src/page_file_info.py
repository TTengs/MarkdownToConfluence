import os, sys, json
from posixpath import basename, dirname

def get_prefix(filepath: str, root: str) -> str:
    if(filepath.endswith("index.md") and "prefix.txt" in os.listdir(dirname(filepath))): # No prefix for index page in folder with prefix.txt (prefix is only for underpages)
        return ""
    if(os.path.isfile(filepath)):
        filepath = os.path.dirname(filepath)
    else:
        if("prefix.txt" in os.listdir(filepath)): # assume index.md, No prefix for index page in folder with prefix.txt (prefix is only for underpages)
            return ""
    while("prefix.txt" not in os.listdir(filepath)):
        filepath = os.path.dirname(filepath)
        if(filepath == root or filepath == ""):
            return ""
    with open(f"{filepath}/prefix.txt") as f:
        return f.readline()

def get_page_name_from_path(path: str, root: str):
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
def get_parent_name_from_path(path: str, root: str, default="Overview"):
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

print(get_parent_name_from_path("./documentation/page 1/index.md", "./documentation"))

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
        page_names.append(get_page_name_from_path(path, root))
    return page_names
