import re
import requests, json, os
from requests.auth import HTTPBasicAuth

def parse_tickets(filename: str):
    with open(filename, 'r') as f:
        lines = f.readlines()   
    with open(filename, 'w') as f:
        for line in lines:
            res = parse_ticket(line)
            new_line = res if res.endswith('\n') else res + '\n'
            f.write(new_line)

def parse_ticket(line: str) -> str:
    tickets = re.findall(r'\d+-[A-Z]+(?!-?[a-zA-Z]{1,10})', line[::-1]) #official atlassian regex magic
    new_line = line
    for ticket in tickets:
        if(check_if_ticket_exists(ticket)): # TODO: Raise warning in pipeline
            ticket = ticket[::-1]
            ticket_tag = f"<ac:structured-macro ac:name='jira'><ac:parameter ac:name='columns'>key,summary,type,created,updated,due,assignee,reporter,priority,status,resolution</ac:parameter><ac:parameter ac:name='key'>{ticket}</ac:parameter> </ac:structured-macro>"
            new_line = new_line.replace(ticket, ticket_tag)
    return new_line

def check_if_ticket_exists(ticket: str):
    base_url = os.environ.get('INPUT_CONFLUENCE_URL')
    url = f'{base_url}/rest/api/3/issue/{ticket}'
    username = os.environ.get('INPUT_AUTH_USERNAME')
    token = os.environ.get('INPUT_AUTH_API_TOKEN')
    auth = HTTPBasicAuth(username, token)

    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'User-Agent': 'python'
    }

    response = requests.request(
        "GET",
        url,
        headers=headers,
        auth=auth
    )

    return response.status_code == 200

def run(filename):
    return parse_tickets(filename)

#print(check_if_ticket_exists('BAasdaC-74'))
