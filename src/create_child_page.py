import json
import codecs
import requests

def create_child_page(filename: str, title: str, space_obj, parent_id: str):
    filename = filename.replace('.md', '')
    template = {
        "version" : {
            "number": 1
        },
        "title": title,
        "type": "page",
        "space": space_obj,
        "ancestors": [
            {
                "id": parent_id,
            }
        ],
        "body": {
                "storage": {
                    "value": "",
                    "representation": "storage"
                }
            }
    }

    # Remove <!DOCTYPE html> from html file
    with open(f"{filename}.html", "r") as f:
        lines = f.readlines()
    with open(f"{filename}.html", "w") as f:
        for line in lines:
            if line.strip("\n") != "<!DOCTYPE html>":
                f.write(line)


    # Load html file into template
    f = codecs.open(f"{filename}.html", 'r', encoding='utf-8')
    template['body']['storage']['value'] = f.read()

    url = "https://at-bachelor.atlassian.net/wiki/rest/api/content"

    #TODO: Get auth from secrets
    headers = {
    'Authorization': 'Basic bGFyc2UxOUBzdHVkZW50LnNkdS5kazp6RzFrQk1ick9PUEtZblNSSFA0bTQxNUI=',
    'Content-Type': 'application/json; charset=utf-8',
    'User-Agent': 'python'
    }

    # Upload html to confluence
    response = requests.request("POST", url, headers=headers, data=json.dumps(template))

    return response

"""
space_obj = {
                "id": 33014,
                "key": "~955037829",
                "name": "Anders Larsen"
            }

print(create_child_page("./documentation/page 1/index.md", "Underpage tdqwest", space_obj, "none").text)
"""