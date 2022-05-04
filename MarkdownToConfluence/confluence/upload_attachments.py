import requests, json, os, base64
from .check_if_page_exists import page_exists_in_space, get_page_id
from .PageNotFoundError import PageNotFoundError
from requests.auth import HTTPBasicAuth

BASE_URL = os.environ.get("INPUT_CONFLUENCE_URL")
SPACEKEY = os.environ.get("INPUT_CONFLUENCE_SPACE_KEY")
AUTH_USERNAME = os.environ.get("INPUT_AUTH_USERNAME")
AUTH_API_TOKEN = os.environ.get("INPUT_AUTH_API_TOKEN")

auth = HTTPBasicAuth(AUTH_USERNAME, AUTH_API_TOKEN)

headers = {
'User-Agent': 'python',
'X-Atlassian-Token': 'no-check'
}

def upload_attachment(page_title, attactchment_name, filepath):
    if(page_exists_in_space(page_title, SPACEKEY)):
        url = f"{BASE_URL}/wiki/rest/api/content/{get_page_id(page_title, SPACEKEY)}/child/attachment"

        # Get attachment id
        id = ""
        attachments = requests.get(url, headers=headers, auth=auth)
        for result in json.loads(attachments.text)['results']:
            if(result['title'] == attactchment_name):
                id = result['id']
        if(id == ""): # Attachment doesnt exist, create it
            # Create attachment
            file = {'file': (attactchment_name, open(filepath, 'rb'))}
            response = requests.post(url, headers=headers, files=file, auth=auth)
        else: # Attachment exists, update it
             # Update attachment
            files = {'file': (attactchment_name, open(os.path.abspath(filepath), 'rb'))}
            response = requests.post(f'{url}/{id}/data', headers=headers, files=files, auth=auth)

        if(response.status_code == 200):
            print(f"Uploaded {attactchment_name} as attachment on page {page_title}")
        else:
            print(f"Error uploading {attactchment_name} as attachment on page {page_title}. Status Code {response.status_code}")
        return response
    else:
        raise PageNotFoundError(page_title, SPACEKEY)
