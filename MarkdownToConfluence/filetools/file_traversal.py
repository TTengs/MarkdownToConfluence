import os
# assign directory
FILES_PATH = os.environ.get("INPUT_FILESLOCATION")
SPACE_ID = os.environ.get("CONFLUENCE_SPACE_ID")

space_obj = {
                "key": SPACE_ID
            }
        
# iterate over files in
# that directory
def traverse(directory):
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # checking if it is a file
        if(os.path.isdir(f)):
            traverse(f)
        if(f.endswith('.md')):
            print(f)


traverse(FILES_PATH) 