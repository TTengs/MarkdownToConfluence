import requests, json
from MarkdownToConfluence.utils import get_all_page_names_in_filesystem
import sys, os, base64
from requests.auth import HTTPBasicAuth
from MarkdownToConfluence.confluence.confluence_utils import get_all_pages_in_space

BASE_URL = os.environ.get("INPUT_CONFLUENCE_URL")
FILES_PATH = os.environ.get("INPUT_FILESLOCATION")
SPACE_KEY = os.environ.get("INPUT_CONFLUENCE_SPACE_KEY")
AUTH_USERNAME = os.environ.get("INPUT_AUTH_USERNAME")
AUTH_API_TOKEN = os.environ.get("INPUT_AUTH_API_TOKEN")

auth = HTTPBasicAuth(AUTH_USERNAME, AUTH_API_TOKEN)

def delete_page(page_id: str, page_name=""):
    
    url = f"{BASE_URL}/wiki/rest/api/content/{page_id}"

    headers = {
    'User-Agent': 'python'
    }

    response = requests.request('DELETE', url, headers=headers, auth=auth)

    if(response.status_code == 204):
        print(f"Deleted {page_id} {page_name}")
    else:
        print(f"Error occured while attempting to delete page: {page_id}, status code: {response.status_code}")

    return response
"""
    deletes all pages on confluence, that are not part of the files system.
    the exclude arg takes a list of page names, that are not to be deleted, even if they dont exist in the filesystem
"""
def delete_non_existing_pages(space_key: str, root: str, exclude=['Overview']):
    url = f"{BASE_URL}/wiki/rest/api/content?spaceKey={space_key}"

    headers = {
    'User-Agent': 'python'
    }

    results = []
    response = requests.request("GET", url, headers=headers, auth=auth)
    response_json = json.loads(response.text)
    if(response.status_code == 200):
        results.extend(response_json['results'])
        while("next" in response_json['_links']):
            url = BASE_URL + response_json["_links"]["next"]
            response = requests.request("GET", url, headers=headers, auth=auth)
            response_json = json.loads(response.text)
            results.extend(response_json['results'])
        
        pages_in_filesystem = get_all_page_names_in_filesystem(root)
        for result in results:
            if (result['title'] not in pages_in_filesystem and result['title'] not in exclude):
                delete_page(result['id'], result['title'])
    
if __name__ == "__main__":
    if(len(sys.argv)> 1):
        delete_non_existing_pages(sys.argv[1], sys.argv[2])
    else:
        delete_non_existing_pages(SPACE_KEY, FILES_PATH)

def delete_all_pages_in_space(space_key):
    pages = get_all_pages_in_space(space_key)
    for page in pages:
        delete_page(page['id'])