from urllib.parse import quote
import requests, json
import os
from requests.auth import HTTPBasicAuth 

BASE_URL = os.environ.get("CONFLUENCE_URL")
AUTH_USERNAME = os.environ.get("AUTH_USERNAME")
AUTH_API_TOKEN = os.environ.get("AUTH_API_TOKEN")

auth = HTTPBasicAuth(AUTH_USERNAME, AUTH_API_TOKEN)

def page_exists_in_space(title: str, spaceKey: str) -> bool:
    url = f"{BASE_URL}/wiki/rest/api/content?spaceKey={spaceKey}&title={quote(title)}"
    headers = {
    'User-Agent': 'python'
    }
    response = requests.request('GET', url, headers=headers, auth=auth)
    if(response.status_code == 200):
        results = json.loads(response.text)['results']
        if(len(results) > 0):
            return True
        else:
            return False
    else:
        print(response.text)

def get_page_id(title: str, spaceKey: str) -> str:
    url = f"{BASE_URL}/wiki/rest/api/content?spaceKey={spaceKey}&title={quote(title)}"
    headers = {
    'User-Agent': 'python'
    }
    response = requests.request('GET', url, headers=headers, auth=auth)
    if(response.status_code == 200):
        results = json.loads(response.text)['results']
        if(len(results) > 0):
            return results[0]['id']
        else:
            return 'Page does not exist'
    else:
        print(response.text)