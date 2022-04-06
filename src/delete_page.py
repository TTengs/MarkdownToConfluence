import requests

def delete_page(page_id: str):
    
    url = f"https://at-bachelor.atlassian.net/wiki/rest/api/content/{page_id}"

    #TODO: Get auth from secrets
    headers = {
    'Authorization': 'Basic bGFyc2UxOUBzdHVkZW50LnNkdS5kazp6RzFrQk1ick9PUEtZblNSSFA0bTQxNUI=',
    'User-Agent': 'python'
    }

    response = requests.request('DELETE', url, headers=headers)

    return response
