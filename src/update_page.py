import json
import codecs
import requests

def update_page_content(pathname: str, title: str, space_obj,):
    filename = pathname + "/index"
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
    with open(f"{filename}.html", "r") as f:
        lines = f.readlines()
    with open(f"{filename}.html", "w") as f:
        for line in lines:
            if line.strip("\n") != "<!DOCTYPE html>":
                f.write(line)

    # Load html file into template
    f = codecs.open(f"{filename}.html", 'r', encoding='utf-8')
    template['body']['storage']['value'] = f.read()

    url = "https://at-bachelor.atlassian.net/wiki/rest/api/content/1310721"

    headers = {
    'Authorization': 'Basic bGFyc2UxOUBzdHVkZW50LnNkdS5kazp6RzFrQk1ick9PUEtZblNSSFA0bTQxNUI=',
    'Content-Type': 'application/json; charset=utf-8',
    'User-Agent': 'python'
    }

    # Get current version
    get_response = requests.request("GET", "https://at-bachelor.atlassian.net/wiki/rest/api/content/1310721?expand=version", headers=headers)
    version_number = int(json.loads(get_response.text)['version']['number'])
    template['version']['number'] = version_number + 1

    # Upload html to confluence
    put_response = requests.request("PUT", url, headers=headers, data=json.dumps(template))

    return(put_response)