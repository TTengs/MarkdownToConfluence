import json, os

def init():
    global attachments, settings
    attachments = []
    settings = json.load(open(os.path.join(os.environ.get('INPUT_FILESLOCATION'), 'settings.json')))