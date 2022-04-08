import re
import requests, json

url = f"https://at-bachelor.atlassian.net/wiki/rest/api/content/1310721/child/attachment"

headers = {
'Authorization': 'Basic bGFyc2UxOUBzdHVkZW50LnNkdS5kazp6RzFrQk1ick9PUEtZblNSSFA0bTQxNUI=',
'User-Agent': 'python',
'X-Atlassian-Token': 'no-check'
}

def upload_new_attachment(name, filename):

    file = {'file': (name, open(filename, 'rb'))}

    response = requests.post(url, headers=headers, files=file)

    return response

def update_attachment_data(name, filename):

    # Get attachment id
    id = ""
    attachments = requests.get(url, headers=headers)
    for result in json.loads(attachments.text)['results']:
        if(result['title'] == name):
            id = result['id']

    # Update attachment
    files = {'file': (f'{name}', open(f'./{filename}', 'rb'))}
    response = requests.post(url + f'/{id}/data', headers=headers, files=files)

    return response
