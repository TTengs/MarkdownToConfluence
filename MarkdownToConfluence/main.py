from importlib.resources import path
from posixpath import dirname, basename
from MarkdownToConfluence.confluence.PageNotFoundError import PageNotFoundError
from confluence import page_exists_in_space, get_page_id
from confluence import create_page
from confluence import update_page_content
from confluence import upload_attachment
from utils import convert_all_md_img_to_confluence_img
import MarkdownToConfluence.globals
from utils.page_file_info import get_page_name_from_path, get_parent_name_from_path
import os
import subprocess
import markdown
import module_loader

SPACE_KEY = os.environ.get("CONFLUENCE_SPACE_KEY")

space_obj = {
        "key": SPACE_KEY,
    }

def upload_documentation(path_name:str, root:str):
    response=""
    # If a directory is given as path, assume index.md as file
    if(os.path.isdir(path_name)):
        path_name += "/index.md"

    file_name = basename(path_name).replace(".md", "")
    temp_file = path_name.replace('.md', '_final.md')

    pages = path_name.split('/')

    # Get page name
    page_name = get_page_name_from_path(path_name, root)

    # Get parent name
    parent_name = get_parent_name_from_path(path_name, root)

    # Copy into name_final.md
    with open(path_name, 'r') as i, open(temp_file, 'w') as o:
        lines = i.readlines()
        for line in lines:
            o.write(line)

    # Load and run modules
    settings_path = f"{os.environ.get('INPUT_FILESLOCATION')}/settings.json"
    if(os.path.exists(settings_path)):
        modules = module_loader.get_modules(settings_path)
    else:
        modules = module_loader.get_modules()
    
    for module in modules:
        module_loader.run_module(module, temp_file)

    # Convert images
    convert_all_md_img_to_confluence_img(temp_file)

    # Convert to html
    with open(temp_file, 'r') as f:
        text = f.read()
        html = markdown.markdown(text)
    with open(path_name.replace('.md', '.html'), 'w') as f:
        f.write(html)

    #print(f"Uploading {page_name} with {parent_name} as parent")
    #If the page already exists, just update it
    if(page_exists_in_space(page_name, SPACE_KEY)):
        try:
            page_id = get_page_id(page_name, SPACE_KEY)
            response = update_page_content(path_name, page_name, page_id, space_obj)
            if(response.status_code == 200):
                print(f"Updated {page_name} with {parent_name} as parent")
        except PageNotFoundError:
            print(PageNotFoundError(page_name, SPACE_KEY))
    #Else, create the page
    else:
        if(parent_name != "none"): #Create page as a child page, if there is a parent
            try:
                if(not page_exists_in_space(parent_name, SPACE_KEY)): #If the parent page doesn't exists, create it
                    print(f"uploading parent: {parent_name}")
                    if(file_name != "index"):
                        subprocess.call(["bash", "/MarkdownToConfluence/convert.sh", f"{dirname(path_name)}/index.md"])
                    else:
                        subprocess.call(["bash", "/MarkdownToConfluence/convert.sh", f"{dirname(dirname(path_name))}/index.md"])
                parent_id = get_page_id(parent_name, SPACE_KEY)
                response = create_page(path_name, page_name, space_obj, parent_id)
            except PageNotFoundError:
                print(PageNotFoundError(page_name, SPACE_KEY))
        else:
            response = create_page(path_name, page_name, space_obj) #Create page as top page
        if(response.status_code == 200):
            print(f"Created {page_name} with {parent_name} as parent")

    if(response.status_code == 200):
        for attachment in MarkdownToConfluence.globals.attachments:
            upload_attachment(page_name, attachment[0], attachment[1])
    else:
        print(f"Error uploading {page_name}. Status code {response.status_code}")
        print(response.text)
        sys.exit(1)
    return response

if __name__ == "__main__":
    import sys
    MarkdownToConfluence.globals.init()
    upload_documentation(sys.argv[1], sys.argv[2])