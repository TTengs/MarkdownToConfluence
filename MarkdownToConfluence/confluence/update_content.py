import json
import codecs
import requests
import os, base64
from requests.auth import HTTPBasicAuth

BASE_URL = os.environ.get("CONFLUENCE_URL")
AUTH_USERNAME = os.environ.get("AUTH_USERNAME")
AUTH_API_TOKEN = os.environ.get("AUTH_API_TOKEN")

auth = HTTPBasicAuth(AUTH_USERNAME, AUTH_API_TOKEN)

def update_page_content(filename: str, title: str, page_id: str, space_obj,):
    filename = filename.replace(".md", ".html")
    template = {
        "version" : {
            "number": 0,
        },
        "title": title,
        "type": "page",
        "space": space_obj,
        "body": {
                "storage": {
                    "value": "",
                    "representation": "storage"
                }
            }
    }

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

    # Get current version
    get_response = requests.request("GET", f"{url}?expand=version", headers=headers, auth=auth)
    version_number = int(json.loads(get_response.text)['version']['number'])
    template['version']['number'] = version_number + 1

    # Upload html to confluence
    put_response = requests.request("PUT", url, headers=headers, data=json.dumps(template), auth=auth)

    if(put_response.status_code != 200):
        print(template['body'])

    return(put_response)