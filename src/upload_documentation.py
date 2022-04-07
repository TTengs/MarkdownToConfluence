from posixpath import dirname, basename
from check_if_page_exists import page_exists_in_space, get_page_id
from create_page import create_page
from delete_page import delete_page
from update_page import update_page_content
from prefix import get_prefix
import os
import subprocess

space_obj = {
        "id": 33014,
        "key": "~955037829",
        "name": "Anders Larsen"
    }

def upload_documentation(path_name:str, root:str):
    response=""
    # If a directory is given as path, assume index.md as file
    if(os.path.isdir(path_name)):
        path_name += "/index.md"
    
    file_name = basename(path_name).replace(".md", "")

    pages = path_name.split('/')

    # Set page name
    page_name = get_prefix(path_name, root)
    if(file_name == "index"):
        page_name += pages[-2]
    else:
        page_name += file_name

    # Set parent name, is "none" if there is no parent
    parent_name = ""
    if(file_name == "index"):
        parent_name = get_prefix(dirname(dirname(path_name)), root) + pages[-3] if(len(pages) > 2 and pages[-3] != 'documentation') else "none"
    else:
        parent_name = get_prefix(path_name, root) + pages[-2]

    #If the page already exists, just update it
    if(page_exists_in_space(page_name, space_obj["key"])): #Deletes page if it already exists TODO: Update existing pages
        page_id = get_page_id(page_name, space_obj['key'])
        response = update_page_content(path_name, page_name, page_id, space_obj)
    #Else, create the page
    else:
        if(parent_name != "none"): #Create page as a child page, if there is a parent
            if(not page_exists_in_space(parent_name, space_obj['key'])): #If the parent page doesn't exists, create it
                if(file_name != "index"):
                    subprocess.call(["bash", "/src/convert.sh", f"{dirname(path_name)}/index.md"])
                else:
                    subprocess.call(["bash", "/src/convert.sh", f"{dirname(dirname(path_name))}/index.md"])
            parent_id = get_page_id(parent_name, space_obj['key'])
            response = create_page(path_name, page_name, space_obj, parent_id)
        else:
            response = create_page(path_name, page_name, space_obj) #Create page as top page

    if(response.status_code == 200):
        print(f"Uploaded {page_name} with {parent_name} as parent")
    else:
        print(f"Error uploading {page_name}. Status code {response.status_code}")
    return response

if __name__ == "__main__":
    import sys
    upload_documentation(sys.argv[1], sys.argv[2])