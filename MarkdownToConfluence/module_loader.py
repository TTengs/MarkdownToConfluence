import os, json
from posixpath import basename
import pathlib
import MarkdownToConfluence.globals

def run_module(module_name: str, filename=None):
    name = "MarkdownToConfluence.modules." + module_name
    mod = __import__(name, fromlist=[''])
    if(filename != None):
        return mod.run(filename)
    else:
        return mod.run()

def get_modules():
    modules = []
    settings = MarkdownToConfluence.globals.settings
    modules_location = str(pathlib.Path(__file__).parent.resolve()) + '/modules'
    for filename in os.listdir(modules_location):
        f = os.path.join(modules_location, filename)
        # checking if it is a file
        if(os.path.isdir(f)):
            module_name = basename(f)
            if(module_name != '__pycache__'):
                if(settings == None):
                    modules.append(module_name)
                else:
                    if('modules' in settings.keys()):
                        if(module_name in settings['modules']):
                            if(settings['modules'][module_name] == True):
                                modules.append(module_name)
                        else: 
                            modules.append(module_name) # assumes non specified modules, should be added
                    else:
                        modules.append(module_name) # Assume all modules should be added, if nothing is specified

    return modules