import requests, json, shutil, time
import os.path
from urllib.parse import quote
from os import path
from requests.auth import HTTPBasicAuth

SPACE_KEY = 'space key'
BASE_URL = 'https:// 'network name' .atlassian.net'
AUTH_USERNAME = 'user email'
AUTH_API_TOKEN = 'Super secret api token'
DOCS_FOLDER_NAME = "Name of folder to place docs into" #if left empty, the script will create a folder called "docs"

#If this GET_DOCS_FOLDER is set to true, the script will try to find a page on the space that is equal to DOCS_FOLDER_NAME 
#and only download the pages under
GET_DOCS_FOLDER = False

auth = HTTPBasicAuth(AUTH_USERNAME, AUTH_API_TOKEN)

def get_all_pages_in_space(space_key: str):
    url = f"{BASE_URL}/wiki/rest/api/content?spaceKey={space_key}"

    headers = {
    'User-Agent': 'python'
    }

    results = []
    response = requests.request("GET", url, headers=headers, auth=auth)
    if(response.status_code == 200):
        response_json = json.loads(response.text)
        results.extend(response_json['results'])
        while("next" in response_json['_links']):
            url = BASE_URL + '/wiki' + response_json["_links"]["next"]
            response = requests.request("GET", url, headers=headers, auth=auth)
            #print(response, response.text)
            if(response.status_code == 200):
                response_json = json.loads(response.text)
                results.extend(response_json['results'])
            else:
                break
    else:
        print(response)
    results_title = [s['title'] for s in results]
    return results_title

def get_all_decendants_in_page(pageID: str):
    url = f"{BASE_URL}/wiki/rest/api/content/{pageID}/descendant/page?limit=9999"

    headers = {
    'User-Agent': 'python'
    }

    results = []
    response = requests.request("GET", url, headers=headers, auth=auth)
    if(response.status_code == 200):
        response_json = json.loads(response.text)
        results.extend(response_json['results'])
        while("next" in response_json['_links']):
            url = BASE_URL + '/wiki' + response_json["_links"]["next"]
            response = requests.request("GET", url, headers=headers, auth=auth)
            #print(response, response.text)
            if(response.status_code == 200):
                response_json = json.loads(response.text)
                results.extend(response_json['results'])
            else:
                break
    else:
        print(response)

    results_title = [str(s['title']) for s in results]
    #print(results_title)
    
    return results_title

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
            print(f"Page was not found with {title}, {spaceKey}")
    else:
        print(response.text)
        print(f"Page was not found with {title}, {spaceKey}")

def getChildren(pageId: str):
    url = f"{BASE_URL}/wiki/rest/api/content/{pageId}/child/page"

    headers = {
    'User-Agent': 'python'
    }

    results = []
    response = requests.request("GET", url, headers=headers, auth=auth)
    if(response.status_code == 200):
        response_json = json.loads(response.text)
        results.extend(response_json['results'])
        while("next" in response_json['_links']):
            url = response_json["_links"]["base"] + response_json["_links"]["next"]
            response = requests.request("GET", url, headers=headers, auth=auth)
            if(response.status_code == 200):
                response_json = json.loads(response.text)
                results.extend(response_json['results'])
            else:
                break
    else:
        print(response)

    return results

def findPath(folder: str, dirname: str):
    for root, dirs, files in os.walk(os.path.abspath(folder)):
        for name in dirs:
            if name == dirname:  
                #name = pathReplacer(name)
                result = os.path.abspath(os.path.join(root, name))
                return result

def checkIfFolderExist():
    global DOCS_FOLDER_NAME
    if(DOCS_FOLDER_NAME == ""):
        if(not path.exists("docs")):
            os.mkdir("docs")
        DOCS_FOLDER_NAME = "docs"
    else:
        if(not path.exists(DOCS_FOLDER_NAME)):
            os.mkdir(DOCS_FOLDER_NAME)

def createPages(pages: any):
    for page in pages:
        page = pathReplacer(page)
        path = f"{DOCS_FOLDER_NAME}/{page}"
        os.mkdir(path)
        open(f"{path}/index.md", 'w')

def sortPages(pages: any):
    for page in pages:
        id = get_page_id(page, SPACE_KEY)
        page = pathReplacer(page)
        for child in getChildren(id):
            child = pathReplacer(child['title'])
            print(f"moving {child} to {page}")
            childPath = findPath(DOCS_FOLDER_NAME, child)
            parentPath = findPath(DOCS_FOLDER_NAME, page)
            shutil.move(childPath, parentPath)

def pathReplacer(page: str):
    page = page.replace('"', "'")
    page = page.replace("*", "")
    page = page.replace("\\", "")
    page = page.replace("?", "")
    page = page.replace("<", "")
    page = page.replace(">", "")
    page = page.replace("|", "")
    page = page.replace(":", "")
    return page.replace("/", "%")

if __name__ == "__main__":
    start = time.time()

    checkIfFolderExist()

    if (GET_DOCS_FOLDER):
        id = get_page_id(DOCS_FOLDER_NAME, SPACE_KEY)
        pages = get_all_decendants_in_page(id)
    else:
        pages = get_all_pages_in_space(SPACE_KEY)

    createPages(pages)

    sortPages(pages)
    
    end = time.time()
    print("Time taken to was: ")
    print((end - start) / 60, "minutes")
