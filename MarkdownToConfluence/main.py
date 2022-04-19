from posixpath import dirname, basename
from MarkdownToConfluence.file_parsing import attachments
from confluence import page_exists_in_space, get_page_id
from confluence import create_page
from confluence import update_page_content
from confluence import upload_attachment
from file_parsing import parse_and_get_attachments
from filetools.page_file_info import get_page_name_from_path, get_parent_name_from_path
import os
import subprocess
import markdown

SPACE_KEY = os.environ.get("CONFLUENCE_SPACE_KEY")

space_obj = {
        "key": SPACE_KEY,
        "name": "Anders Larsen"
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

    # Get and parse attachments
    attachments = parse_and_get_attachments(path_name.replace('.md', '_final.md'))

    # Convert to html
    with open(path_name.replace('.md', '_final.md'), 'r') as f:
        text = f.read()
        html = markdown.markdown(text)
    with open(path_name.replace('.md', '.html'), 'w') as f:
        f.write(html)

    #print(f"Uploading {page_name} with {parent_name} as parent")
    #If the page already exists, just update it
    if(page_exists_in_space(page_name, space_obj["key"])):
        page_id = get_page_id(page_name, space_obj['key'])
        response = update_page_content(path_name, page_name, page_id, space_obj)
        if(response.status_code == 200):
            print(f"Updated {page_name} with {parent_name} as parent")
    #Else, create the page
    else:
        if(parent_name != "none"): #Create page as a child page, if there is a parent
            if(not page_exists_in_space(parent_name, space_obj['key'])): #If the parent page doesn't exists, create it
                print(f"uploading parent: {parent_name}")
                if(file_name != "index"):
                    subprocess.call(["bash", "/MarkdownToConfluence/convert.sh", f"{dirname(path_name)}/index.md"])
                else:
                    subprocess.call(["bash", "/MarkdownToConfluence/convert.sh", f"{dirname(dirname(path_name))}/index.md"])
            parent_id = get_page_id(parent_name, space_obj['key'])
            response = create_page(path_name, page_name, space_obj, parent_id)
        else:
            response = create_page(path_name, page_name, space_obj) #Create page as top page
        if(response.status_code == 200):
            print(f"Created {page_name} with {parent_name} as parent")

    if(response.status_code == 200):
        for attachment in attachments:
            upload_attachment(page_name, attachment[0], attachment[1])
    else:
        print(f"Error uploading {page_name}. Status code {response.status_code}")
        print(response.text)
    return response

if __name__ == "__main__":
    import sys
    upload_documentation(sys.argv[1], sys.argv[2])