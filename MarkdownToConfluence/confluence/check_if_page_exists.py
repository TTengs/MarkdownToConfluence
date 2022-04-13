from urllib.parse import quote
import requests, json

def page_exists_in_space(title: str, spaceKey: str) -> bool:
    url = f"https://at-bachelor.atlassian.net/wiki/rest/api/content?spaceKey={spaceKey}&title={quote(title)}"
    #TODO: Get auth from secrets
    headers = {
    'Authorization': 'larse19:zG1kBMbrOOPKYnSRHP4m415B',
    'User-Agent': 'python'
    }
    response = requests.request('GET', url, headers=headers)
    if(response.status_code == 200):
        results = json.loads(response.text)['results']
        if(len(results) > 0):
            return True
        else:
            return False
    else:
        print(response.text)

def get_page_id(title: str, spaceKey: str) -> str:
    url = f"https://at-bachelor.atlassian.net/wiki/rest/api/content?spaceKey={spaceKey}&title={quote(title)}"
    #TODO: Get auth from secrets
    headers = {
    'Authorization': 'larse19:zG1kBMbrOOPKYnSRHP4m415B',
    'User-Agent': 'python'
    }
    response = requests.request('GET', url, headers=headers)
    if(response.status_code == 200):
        results = json.loads(response.text)['results']
        if(len(results) > 0):
            return results[0]['id']
        else:
            return 'Page does not exist'
    else:
        print(response.text)