import json
import requests
import os
from requests.auth import HTTPBasicAuth
import MarkdownToConfluence.confluence.confluence_utils as confluence_utils

BASE_URL = os.environ.get("INPUT_CONFLUENCE_URL")
AUTH_USERNAME = os.environ.get("INPUT_AUTH_USERNAME")
AUTH_API_TOKEN = os.environ.get("INPUT_AUTH_API_TOKEN")
SPACEKEY = os.environ.get('INPUT_CONFLUENCE_SPACE_KEY')

auth = HTTPBasicAuth(AUTH_USERNAME, AUTH_API_TOKEN)

def create_empty_page(page_name: str):
    if(confluence_utils.page_exists_in_space(confluence_utils.get_page_id(page_name, SPACEKEY))):
        return "Page already exists"


    template = {
        "version" : {
            "number": 1
        },
        "title": page_name,
        "type": "page",
        "space": {
            "key": SPACEKEY
        }
    }

    url = f'{BASE_URL}/wiki/rest/api/content'

    headers = {
    'Content-Type': 'application/json; charset=utf-8',
    'User-Agent': 'python'
    }

    # Upload html to confluence
    response = requests.request("POST", url, headers=headers, data=json.dumps(template), auth=auth)

    if(response.status_code == 200):
        print(f"Created empty page, {page_name} at root of space")
    else:
        print(f"Error occured while attampting to create empty page, {page_name} at root of space. Status code: {response.status_code}")
    return response
