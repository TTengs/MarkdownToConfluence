from posixpath import dirname, basename
from confluence import page_exists_in_space, get_page_id
from confluence import create_page
from confluence import update_page_content
from filetools.page_file_info import get_page_name_from_path, get_parent_name_from_path
import os
import subprocess

SPACE_ID = os.environ.get("CONFLUENCE_SPACE_ID")

space_obj = {
        "key": SPACE_ID
    }

def upload_documentation(path_name:str, root:str):
    response=""
    # If a directory is given as path, assume index.md as file
    if(os.path.isdir(path_name)):
        path_name += "/index.md"
    
    file_name = basename(path_name).replace(".md", "")

    pages = path_name.split('/')

    # Get page name
    page_name = get_page_name_from_path(path_name, root)

    # Get parent name
    parent_name = get_parent_name_from_path(path_name, root)

    #If the page already exists, just update it
    if(page_exists_in_space(page_name, space_obj["key"])): #Deletes page if it already exists TODO: Update existing pages
        page_id = get_page_id(page_name, space_obj['key'])
        response = update_page_content(path_name, page_name, page_id, space_obj)
    #Else, create the page
    else:
        if(parent_name != "none"): #Create page as a child page, if there is a parent
            if(not page_exists_in_space(parent_name, space_obj['key'])): #If the parent page doesn't exists, create it
                if(file_name != "index"):
                    subprocess.call(["bash", "/MarkdownToConfluence/convert.sh", f"{dirname(path_name)}/index.md"])
                else:
                    subprocess.call(["bash", "/MarkdownToConfluence/convert.sh", f"{dirname(dirname(path_name))}/index.md"])
            parent_id = get_page_id(parent_name, space_obj['key'])
            response = create_page(path_name, page_name, space_obj, parent_id)
        else:
            response = create_page(path_name, page_name, space_obj) #Create page as top page

    if(response.status_code == 200):
        #TODO: Den skriver det her også selvom at den ikke uploader sider
        print(f"Uploaded {page_name} with {parent_name} as parent")
    else:
        print(f"Error uploading {page_name}. Status code {response.status_code}")
    return response

if __name__ == "__main__":
    import sys
    upload_documentation(sys.argv[1], sys.argv[2])