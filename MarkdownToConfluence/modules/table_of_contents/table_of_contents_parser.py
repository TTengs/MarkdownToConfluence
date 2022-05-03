import os

def parse_table_of_contents_macros(filename):
    if(os.path.isdir(filename)):
        filename += "/index_final.md"
    reading_toc = False
    root = '@self'
    search_depth = 1
    with open(f"{filename}", "r") as file:
        lines = file.readlines()
    with open(f"{filename}", "w") as file:
        for line in lines:
            if line.strip("\n") == "```table-of-contents" or line.strip("\n") == "```TOC":
                reading_toc = True               
            if reading_toc:
                if(line.strip("\n") != "```mermaid" and line.strip("\n") != "```"):
                    if(line.find('root') != -1):
                        root = line.split('=')[-1].strip()
                    if(line.find('search-depth') != -1):
                        depth = line.split('=')[-1].strip()
                        if(depth.isnumeric()):
                            search_depth = int(depth)
                if line.strip("\n") == "```":
                    file.write(f'<p><ac:structured-macro ac:name=\"pagetree\" ac:schema-version=\"1\" ac:macro-id=\"cace95ee428b28ba686848696668d8ca\"><ac:parameter ac:name=\"root\"><ac:link><ri:page ri:content-title="{root}" /></ac:link></ac:parameter><ac:parameter ac:name=\"startDepth\">{search_depth}</ac:parameter></ac:structured-macro></p><p />')
                    reading_toc = False
            else:
                file.write(line)

def run(filename):
    parse_table_of_contents_macros(filename)
