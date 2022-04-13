import json
import codecs
import requests
import sys

def create_page(filename: str, title: str, space_obj, parent_id="none"):
    filename = filename.replace(".md", ".html")
    template = {
        "version" : {
            "number": 1
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

    if(parent_id != "none"):
        template['ancestors'] = [
            {
                "id": parent_id,
            }
        ]

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

if __name__ == "__main__":
    print(sys.argv)
    if(len(sys.argv) > 4):
        create_page(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        create_page(sys.argv[1], sys.argv[2], sys.argv[3])
