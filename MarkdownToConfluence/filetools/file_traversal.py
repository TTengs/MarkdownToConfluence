import os
# assign directory
FILES_PATH = os.environ.get("INPUT_FILESLOCATION")

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