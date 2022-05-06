import os
from posixpath import dirname
import requests
import base64

def parse_mermaid_macros(filename):
    if(os.path.isdir(filename)):
        filename += "/index_final.md"
    mermaid_diagram_num = 0
    reading_mermaid = False
    graph = ""
    diagram_name = ""
    with open(f"{filename}", "r") as infile:
        lines = infile.readlines()
    with open(f"{filename}", "w") as outfile:
        for line in lines:
            if line.strip("\n") == "```mermaid":
                reading_mermaid = True
                mermaid_diagram_num += 1                
                diagram_name = f"mermaid-{mermaid_diagram_num}"
                diagram_file_name = f'{str(filename).replace(".md","-")}{str(mermaid_diagram_num)}.png'
                outfile.write(f'![{diagram_name}]({diagram_file_name})')
            if reading_mermaid:
                if(line.strip("\n") != "```mermaid" and line.strip("\n") != "```"):
                    graph += line
                if line.strip("\n") == "```":
                    reading_mermaid = False
                    graphbytes = graph.encode("ascii")
                    base64_bytes = base64.b64encode(graphbytes)
                    base64_string = base64_bytes.decode("ascii")
                    url = 'https://mermaid.ink/img/' + base64_string
                    response = requests.get(url)
                    if response.status_code == 200:
                        with open(diagram_file_name, 'wb') as imgfile:
                            imgfile.write(response.content)
            else:
                outfile.write(line)

def run(filename):
    parse_mermaid_macros(filename)


#parse_mermaid_macro('./documentation/page 3/index.md')