import os, json
from posixpath import basename
import pathlib

def run_module(module_name: str, filename=None):
    name = "MarkdownToConfluence.modules." + module_name
    mod = __import__(name, fromlist=[''])
    if(filename != None):
        return mod.run(filename)
    else:
        return mod.run()

def get_modules(settings_file=None):
    modules = []
    modules_location = str(pathlib.Path(__file__).parent.resolve()) + '/modules'
    for filename in os.listdir(modules_location):
        f = os.path.join(modules_location, filename)
        # checking if it is a file
        if(os.path.isdir(f)):
            module_name = basename(f)
            if(module_name != '__pycache__'):
                if(settings_file == None):
                    modules.append(module_name)
                else:
                    settings = json.load(open(settings_file, 'r'))
                    if('modules' in settings.keys()):
                        if(module_name in settings['modules']):
                            if(settings['modules'][module_name] == True):
                                modules.append(module_name)
                        else: 
                            modules.append(module_name) # assumes non specified modules, should be added
                    else:
                        modules.append(module_name) # Assume all modules should be added, if nothing is specified

    return modules