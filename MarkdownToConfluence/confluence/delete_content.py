import requests, json
from MarkdownToConfluence.filetools import get_all_page_names_in_filesystem
import sys, os

BASE_URL = os.environ.get("CONFLUENCE_URL")
#BASE_URL = 'https://at-bachelor.atlassian.net/wiki'
FILES_PATH = os.environ.get("INPUT_FILESLOCATION")
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
#AUTH_TOKEN = "bGFyc2UxOUBzdHVkZW50LnNkdS5kazp6RzFrQk1ick9PUEtZblNSSFA0bTQxNUI="
SPACE_KEY = os.environ.get("CONFLUENCE_SPACE_KEY")

authorization_string = f"Basic {AUTH_TOKEN}"

def delete_page(page_id: str, page_name=""):
    
    url = f"{BASE_URL}/rest/api/content/{page_id}"

    headers = {
    'Authorization': authorization_string,
    'User-Agent': 'python'
    }

    response = requests.request('DELETE', url, headers=headers)

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
    url = f"{BASE_URL}/rest/api/content?spaceKey={space_key}"

    headers = {
    'Authorization': authorization_string,
    'User-Agent': 'python'
    }

    results = []
    response = requests.request("GET", url, headers=headers)
    response_json = json.loads(response.text)
    if(response.status_code == 200):
        results.extend(response_json['results'])
        while("next" in response_json['_links']):
            url = BASE_URL + response_json["_links"]["next"]
            response = requests.request("GET", url, headers=headers)
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