import os

#get the full path to the directory the Python file is contained in
#dir_path = os.path.dirname(os.path.realpath(__file__))
#print(dir_path)

# Define the directory path
path = 'C:\\Users\\Nutzer\\Desktop\\files_to_rename'

# Define the file prefix or suffix
prefix = "prefix_"

# Loop through the files in the directory
for filename in os.listdir(path):
    # Rename the files
    os.rename(os.path.join(path, filename), os.path.join(path, prefix + filename))
