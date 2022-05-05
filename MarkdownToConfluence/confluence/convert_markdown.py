import os, markdown
import MarkdownToConfluence.module_loader as module_loader
from MarkdownToConfluence.utils import convert_all_md_img_to_confluence_img
from MarkdownToConfluence.utils.page_file_info import get_page_name_from_path, get_parent_name_from_path

def convert(filename: str, root: str):
     # If a directory is given as path, assume index.md as file
    if(os.path.isdir(filename)):
        filename += "/index.md"

    #file_name = basename(filename).replace(".md", "")
    temp_file = filename.replace('.md', '_final.md')

    # Get page name
    page_name = get_page_name_from_path(filename, root)

    # Get parent name
    parent_name = get_parent_name_from_path(filename, root)

    # Copy into name_final.md
    with open(filename, 'r') as i, open(temp_file, 'w') as o:
        lines = i.readlines()
        for line in lines:
            o.write(line)

    # Load and run modules
    settings_path = f"{os.environ.get('INPUT_FILESLOCATION')}/settings.json"
    if(os.path.exists(settings_path)):
        modules = module_loader.get_modules(settings_path)
    else:
        modules = module_loader.get_modules()
    
    for module in modules:
        module_loader.run_module(module, temp_file)

    # Convert images
    convert_all_md_img_to_confluence_img(temp_file)

    # Convert to html
    with open(temp_file, 'r') as f:
        text = f.read()
        html = markdown.markdown(text)
    with open(filename.replace('.md', '.html'), 'w') as f:
        f.write(html)

    return (page_name, parent_name)