import json
import codecs
import requests

template = json.loads("""{
    "version" : {
        "number": 0,
        "minorEdit": true
    },
    "title": "Test page updated from postman again",
    "type": "page",
    "space": {
        "id": 33014,
        "key": "~955037829",
        "name": "Anders Larsen"
    },
   "body": {
        "storage": {
            "value": "",
            "representation": "storage"
        }
    }
}""")

# Remove <!DOCTYPE html> from html file
with open("sample_readme.html", "r") as f:
    lines = f.readlines()
with open("sample_readme.html", "w") as f:
    for line in lines:
        if line.strip("\n") != "<!DOCTYPE html>":
            f.write(line)


# Load html file into template
f = codecs.open("sample_readme.html", 'r', encoding='utf-8')
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

print(put_response.text)