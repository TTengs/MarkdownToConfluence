
# import required module
import os
# assign directory
directory = 'documentation'

space_obj = {
                "id": 33014,
                "key": "~955037829",
                "name": "Anders Larsen"
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


traverse(directory) 