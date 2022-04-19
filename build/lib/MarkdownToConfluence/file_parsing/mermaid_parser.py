import os
import requests
import base64

def parse_mermaid_macro(filename):
    if(os.path.isdir(filename)):
        filename += "/index.md"
    mermaid_diagram_num = 0
    reading_mermaid = False
    new_filename = filename.split('.md')[0] + '_final.md'
    graph = ""
    diagram_name = ""
    with open(f"{filename}", "r") as f:
        lines = f.readlines()
    with open(f"{new_filename}", "w") as f:
        for line in lines:
            if line.strip("\n") == "```mermaid":
                print("contains mermaid")
                reading_mermaid = True
                mermaid_diagram_num += 1                
                diagram_name = f"mermaid-{mermaid_diagram_num}"
                diagram_file_name = filename.split('.md')[0] + '-' + str(mermaid_diagram_num) + '.png'
                f.write(f'![{diagram_name}]({diagram_file_name})')
            if reading_mermaid:
                if(line.strip("\n") != "```mermaid" and line.strip("\n") != "```"):
                    graph += line
                if line.strip("\n") == "```":
                    print(graph)
                    reading_mermaid = False
                    graphbytes = graph.encode("ascii")
                    base64_bytes = base64.b64encode(graphbytes)
                    base64_string = base64_bytes.decode("ascii")
                    url = 'https://mermaid.ink/img/' + base64_string
                    response = requests.get(url)
                    print(response.status_code)
                    if response.status_code == 200:
                        print(diagram_file_name)
                        with open(diagram_file_name, 'wb') as f:
                            f.write(response.content)
            else:
                f.write(line)


#parse_mermaid_macro(str(pathlib.Path(__file__).parent.resolve()) + '/tests/testdocs/mermaid.md')