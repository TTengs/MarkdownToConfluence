import json, os

def init(settings_path=""):
    global attachments, settings
    _is_init = False
    if(not _is_init):
        _is_init = True
        attachments = []
        if(settings_path==""):
            if(os.environ.get('INPUT_FILESLOCATION') != None):
                try:
                    settings = json.load(open(os.path.join(os.environ.get('INPUT_FILESLOCATION'), 'settings.json')))
                except FileNotFoundError:
                    settings = None
        else:
            settings = json.load(open(settings_path))

def reset():
    global attachments
    attachments = []