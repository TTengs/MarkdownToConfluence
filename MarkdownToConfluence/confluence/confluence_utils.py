from urllib.parse import quote
import requests, json
import os
from requests.auth import HTTPBasicAuth
from MarkdownToConfluence.confluence.PageNotFoundError import PageNotFoundError 

BASE_URL = os.environ.get("INPUT_CONFLUENCE_URL")
AUTH_USERNAME = os.environ.get("INPUT_AUTH_USERNAME")
AUTH_API_TOKEN = os.environ.get("INPUT_AUTH_API_TOKEN")

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
        return False

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
            raise PageNotFoundError(title, spaceKey)
    else:
        print(response.text)
        raise PageNotFoundError(title, spaceKey)

def get_all_descendants(parent_page: str, space_key: str):
    if(page_exists_in_space(parent_page, space_key)):
        page_id = get_page_id(parent_page, space_key)

        url = f"{BASE_URL}/wiki/rest/api/content/{page_id}/descendant/page"

        headers = {
        'User-Agent': 'python'
        }

        results = []
        response = requests.request("GET", url, headers=headers, auth=auth)
        if(response.status_code == 200):
            #print(response)
            #print(response.text)
            response_json = json.loads(response.text)
            results.extend(response_json['results'])
            while("next" in response_json['_links']):
                url = response_json["_links"]["base"] + response_json["_links"]["next"]
                response = requests.request("GET", url, headers=headers, auth=auth)
                print(response, response.text)
                if(response.status_code == 200):
                    response_json = json.loads(response.text)
                    results.extend(response_json['results'])
                else:
                    break
        else:
            print(response)

        return results
    raise PageNotFoundError(parent_page, space_key)

def get_all_pages_in_space(space_key: str):
    url = f"{BASE_URL}/wiki/rest/api/content?spaceKey={space_key}"

    headers = {
    'User-Agent': 'python'
    }

    results = []
    response = requests.request("GET", url, headers=headers, auth=auth)
    if(response.status_code == 200):
        #print(response)
        #print(response.text)
        response_json = json.loads(response.text)
        results.extend(response_json['results'])
        while("next" in response_json['_links']):
            url = BASE_URL + '/wiki' + response_json["_links"]["next"]
            response = requests.request("GET", url, headers=headers, auth=auth)
            print(response, response.text)
            if(response.status_code == 200):
                response_json = json.loads(response.text)
                results.extend(response_json['results'])
            else:
                break

    else:
        print(response)

    return results