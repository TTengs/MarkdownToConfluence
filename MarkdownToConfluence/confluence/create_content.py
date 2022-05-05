import json
import codecs
import requests
import sys, os, base64
from requests.auth import HTTPBasicAuth
import MarkdownToConfluence.confluence.convert_markdown as convert_markdown
import MarkdownToConfluence.confluence.confluence_utils as confluence_utils
from MarkdownToConfluence.utils import get_parent_path_from_child
import MarkdownToConfluence.globals
from MarkdownToConfluence.confluence.create_empty_page import create_empty_page
from MarkdownToConfluence.confluence.upload_attachments import upload_attachment

BASE_URL = os.environ.get("INPUT_CONFLUENCE_URL")
AUTH_USERNAME = os.environ.get("INPUT_AUTH_USERNAME")
AUTH_API_TOKEN = os.environ.get("INPUT_AUTH_API_TOKEN")
SPACEKEY = os.environ.get('INPUT_CONFLUENCE_SPACE_KEY')
ROOT = os.environ.get('INPUT_FILESLOCATION')

auth = HTTPBasicAuth(AUTH_USERNAME, AUTH_API_TOKEN)

def create_page(filename: str):
    MarkdownToConfluence.globals.init()

    page_name, parent_name = convert_markdown.convert(filename, ROOT)

    if(confluence_utils.page_exists_in_space(confluence_utils.get_page_id(page_name, SPACEKEY))):
        return "Page already exists"

    print(f"Creating {page_name} with {parent_name} as parent")

    filename = filename.replace(".md", ".html")
    template = {
        "version" : {
            "number": 1
        },
        "title": page_name,
        "type": "page",
        "space": {
            "key": SPACEKEY
        },
        "body": {
                "storage": {
                    "value": "",
                    "representation": "storage"
                }
            }
    }

    if(parent_name != ""):
        if(confluence_utils.page_exists_in_space(parent_name, SPACEKEY)):
            template['ancestors'] = [
                {
                    "id": confluence_utils.get_page_id(parent_name),
                }
            ]
        else:
            if(parent_name == MarkdownToConfluence.globals.settings['parent_name']):
                print("Parent didnt exist, creating empty parent at root of space: " + parent_name)
                create_empty_page(parent_name)
            else:
                print("Parent didnt exist, creating parent: " + parent_name)
                create_page(get_parent_path_from_child(filename))

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

    url = f'{BASE_URL}/wiki/rest/api/content'

    headers = {
    'Content-Type': 'application/json; charset=utf-8',
    'User-Agent': 'python'
    }

    # Upload html to confluence
    response = requests.request("POST", url, headers=headers, data=json.dumps(template), auth=auth)

    if(response.status_code == 200):
        for attachment in MarkdownToConfluence.globals.attachments:
            upload_attachment(page_name, attachment[0], attachment[1])
        print(f"Created {page_name} with {parent_name} as parent")
    else:
        print(f"Error uploading {page_name}. Status code {response.status_code}")
        print(response.text)
        sys.exit(1)
    
    return response

if __name__ == "__main__":
    if(len(sys.argv) > 4):
        create_page(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        create_page(sys.argv[1], sys.argv[2], sys.argv[3])
