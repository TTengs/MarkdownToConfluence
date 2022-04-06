from check_if_page_exists import page_exists_in_space, get_page_id
from create_page import create_page
from delete_page import delete_page
from update_page import update_page_content

space_obj = {
        "id": 33014,
        "key": "~955037829",
        "name": "Anders Larsen"
    }

def upload_documentation(path_name:str, page_name:str):
    pages = path_name.split('/')

    _page_name = ""
    if(page_name == "index"):
        _page_name = pages[-2]
    else:
        _page_name = page_name

    parent_name = ""
    if(page_name == "index"):
        parent_name = pages[-3] if(len(pages) > 2 and pages[-3] != 'documentation') else "none"
    else:
        parent_name = pages[-2]

    if(page_exists_in_space(_page_name, space_obj["key"])): #Deletes page if it already exists TODO: Update existing pages
        page_id = get_page_id(_page_name, space_obj['key'])
        update_page_content(path_name, _page_name, page_id, space_obj)
    else:
        if(parent_name != "none" and page_exists_in_space(parent_name, space_obj['key'])): #Create page as a child page, if there is a parent
            parent_id = get_page_id(parent_name, space_obj['key'])
            create_page(path_name, _page_name, space_obj, parent_id)
        else:
            create_page(path_name, _page_name, space_obj) #Create page as top page

    print(f"Uploaded {_page_name} with {parent_name} as parent")

if __name__ == "__main__":
    import sys
    upload_documentation(sys.argv[1], sys.argv[2])