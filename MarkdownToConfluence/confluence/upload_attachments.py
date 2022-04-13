import requests, json, os

BASE_URL = os.environ.get("CONFLUENCE_URL")
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")

#TODO: hvad er '1310721'??
url = f"{BASE_URL}/rest/api/content/1310721/child/attachment"

headers = {
'Authorization': AUTH_TOKEN,
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
