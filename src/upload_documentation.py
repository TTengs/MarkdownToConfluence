from check_if_page_exists import page_exists_in_space, get_page_id
from create_page import create_page
from delete_page import delete_page

space_obj = {
        "id": 33014,
        "key": "~955037829",
        "name": "Anders Larsen"
    }

def upload_documentation(path_name:str):
    pages = path_name.split('/')
    page_name = pages[-1]
    parent_name = pages[-2] if(len(pages) > 2 and pages[-2] != 'documentation') else "none"

    if(page_exists_in_space(page_name, space_obj["key"])): #Deletes page if it already exists TODO: Update existing pages
        page_id = get_page_id(page_name, space_obj['key'])
        delete_page(page_id)

    if(parent_name != "none" and page_exists_in_space(parent_name, space_obj['key'])): #Create page as a child page, if there is a parent
        parent_id = get_page_id(parent_name, space_obj['key'])
        create_page(path_name, page_name, space_obj, parent_id)
    else:
        create_page(path_name, page_name, space_obj) #Create page as top page

if __name__ == "__main__":
    import sys
    upload_documentation(sys.argv[1])