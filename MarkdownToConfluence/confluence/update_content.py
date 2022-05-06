import json, sys
import codecs
import requests
import os, base64
from requests.auth import HTTPBasicAuth
from MarkdownToConfluence.confluence import convert_markdown
from MarkdownToConfluence.utils.page_file_info import get_page_name_from_path, get_parent_name_from_path, get_parent_path_from_child
from MarkdownToConfluence.confluence import confluence_utils
import MarkdownToConfluence.globals
from MarkdownToConfluence.confluence.create_content import create_page
from MarkdownToConfluence.confluence.create_empty_page import create_empty_page
from MarkdownToConfluence.confluence.upload_attachments import upload_attachment


def update_page_content(filename: str, old_filename=""):
    BASE_URL = os.environ.get("INPUT_CONFLUENCE_URL")
    AUTH_USERNAME = os.environ.get("INPUT_AUTH_USERNAME")
    AUTH_API_TOKEN = os.environ.get("INPUT_AUTH_API_TOKEN")
    SPACE_KEY = os.environ.get("INPUT_CONFLUENCE_SPACE_KEY")
    ROOT = os.environ.get("INPUT_FILESLOCATION")
    MarkdownToConfluence.globals.init()

    auth = HTTPBasicAuth(AUTH_USERNAME, AUTH_API_TOKEN)

    old_page_name = ""
    old_parent_name = ""
    page_name, parent_name = convert_markdown.convert(filename, ROOT)

    if(old_filename != ""):
        if(not os.path.exists(old_filename)):
            with open(old_filename, 'w') as old: # create the file temporaily to get names
                old.write(" ")
            old_page_name = get_page_name_from_path(old_filename, ROOT)
            page_id = confluence_utils.get_page_id(old_page_name, SPACE_KEY)
            os.remove(old_filename)
        else:
            old_page_name = get_page_name_from_path(old_filename, ROOT)
            old_parent_name = get_parent_name_from_path(old_filename, ROOT)
    else:
        page_id = confluence_utils.get_page_id(page_name, SPACE_KEY)


    print(f"Updating page {page_id} with title {page_name}")

    filename = filename.replace(".md", ".html")
    template = {
        "version" : {
            "number": 0,
        },
        "title": page_name,
        "type": "page",
        "space": {
            "key": SPACE_KEY
        },
        "body": {
                "storage": {
                    "value": "",
                    "representation": "storage"
                }
            }
    }
    """
    if(parent_name != ""):
        if(confluence_utils.page_exists_in_space(parent_name, SPACE_KEY)):
            template['ancestors'] = [
                {
                    "id": confluence_utils.get_page_id(parent_name, SPACE_KEY),
                }
            ]
        else:
            if('parent_name' in MarkdownToConfluence.globals.settings.keys() and parent_name == MarkdownToConfluence.globals.settings['parent_name']):
                    print("Parent didnt exist, creating empty parent at root of space: " + parent_name)
                    create_empty_page(parent_name)
            else:
                print("Parent didnt exist, creating parent: " + parent_name)
                create_page(get_parent_path_from_child(filename))
    """
    # Remove <!DOCTYPE html> from html file
    with open(f"{filename}", "r") as f:
        lines = f.readlines()
    with open(f"{filename}", "w") as f:
        for line in lines:
            if line.strip("\n") != "<!DOCTYPE html>":
                f.write(line)

    # Load html file into template
    f = codecs.open(f"{filename}", 'r', encoding='utf-8')
    template['body']['storage']['value'] = f.read()


    url = f"{BASE_URL}/wiki/rest/api/content/{page_id}"

    headers = {
    'Content-Type': 'application/json; charset=utf-8',
    'User-Agent': 'python'
    }

    if(old_parent_name != parent_name):
        move_url = f"{BASE_URL}/wiki/rest/api/content/{page_id}/move/append/{confluence_utils.get_page_id(parent_name)}"
        move_response = requests.request("PUT", move_url, headers=headers, auth=auth)
        if(move_response.status_code == 200):
            print(f"Moved page {page_name} from {old_parent_name} to {parent_name}")

    # Get current version
    get_response = requests.request("GET", f"{url}?expand=version", headers=headers, auth=auth)
    version_number = int(json.loads(get_response.text)['version']['number'])
    template['version']['number'] = version_number + 1

    # Upload html to confluence
    put_response = requests.request("PUT", url, headers=headers, data=json.dumps(template), auth=auth)

    if(put_response.status_code == 200):
        for attachment in MarkdownToConfluence.globals.attachments:
            upload_attachment(page_name, attachment[0], attachment[1])
        print(f"Updated page {page_id} with title {page_name}")
        MarkdownToConfluence.globals.reset()
    else:
        print(f"Error uploading {page_name}. Status code {put_response.status_code}")
        print(put_response.text)
        sys.exit(1)
    
    return put_response