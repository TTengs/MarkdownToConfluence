import upload_attachments

def parse_mermaid_macro(filename):
    mermaid_diagram_num = 0
    reading_mermaid = False
    new_filename = filename.split('.md')[0] + '_final.md'
    with open(f"{filename}", "r") as f:
        lines = f.readlines()
    with open(f"{new_filename}", "w") as f:
        for line in lines:
            if line.strip("\n") == "```mermaid":
                reading_mermaid = True
                mermaid_diagram_num += 1
                diagram_name = f"{filename}-{mermaid_diagram_num}"
                f.write(f'<ac:image><ri:attachment ri:filename="{diagram_name}" /></ac:image>')
                """
                response = upload_attachments.upload_new_attachment(diagram_name, f'./{diagram_name}.png')
                print(response)
                if(response.status_code == 400):
                    response = upload_attachments.update_attachment_data(diagram_name, f'./{diagram_name}.png')
                    print(response)
                """
            if reading_mermaid:
                if line.strip("\n") == "```":
                    reading_mermaid = False
            else:
                f.write(line)