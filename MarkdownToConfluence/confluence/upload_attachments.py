import requests, json, os
from .check_if_page_exists import page_exists_in_space, get_page_id
from .PageNotFoundError import PageNotFoundError

BASE_URL = os.environ.get("CONFLUENCE_URL")
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
SPACEKEY = os.environ.get("CONFLUENCE_SPACE_KEY")

authorization_string = f"Basic {AUTH_TOKEN}"

headers = {
'Authorization': authorization_string,
'User-Agent': 'python',
'X-Atlassian-Token': 'no-check'
}

def upload_attachment(page_title, attactchment_name, filepath):
    if(page_exists_in_space(page_title, SPACEKEY)):
        url = f"{BASE_URL}/rest/api/content/{get_page_id(page_title, SPACEKEY)}/child/attachment"

        # Get attachment id
        id = ""
        attachments = requests.get(url, headers=headers)
        for result in json.loads(attachments.text)['results']:
            if(result['title'] == attactchment_name):
                id = result['id']
        if(id == ""): # Attachment doesnt exist, create it
            # Create attachment
            file = {'file': (attactchment_name, open(filepath, 'rb'))}
            response = requests.post(url, headers=headers, files=file)
        else: # Attachment exists, update it
             # Update attachment
            files = {'file': (attactchment_name, open(os.path.abspath(filepath), 'rb'))}
            response = requests.post(f'{url}/{id}/data', headers=headers, files=files)
        print(response.status_code)
        if(response.status_code == 200):
            print(f"Uploaded {attactchment_name} as attachment on page {page_title}")
        else:
            print(f"Error uploading {attactchment_name} as attachment on page {page_title}. Status Code {response.status_code}")
        return response
    else:
        raise PageNotFoundError(page_title, SPACEKEY)

"""
def update_attachment_data(page_title, attactchment_name, filepath):
    if(page_exists_in_space(page_title, SPACEKEY)):
        url = f"{BASE_URL}/rest/api/content/{get_page_id(page_title, SPACEKEY)}/child/attachment"

        # Get attachment id
        id = ""
        attachments = requests.get(url, headers=headers)
        for result in json.loads(attachments.text)['results']:
            if(result['title'] == attactchment_name):
                id = result['id']

        # Update attachment
        files = {'file': (f'{attactchment_name}', open(f'./{filepath}', 'rb'))}
        response = requests.post(url + f'/{id}/data', headers=headers, files=files)

        return response
    else:
        raise PageNotFoundError(page_title, SPACEKEY)
"""