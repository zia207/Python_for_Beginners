import os

folder_path = "/home/zia207/Dropbox/WebSites/GitHub/python-colab/NoteBook/Machine_Learning/Tree_based" # Change this to your folder's path

for filename in os.listdir(folder_path):
    if filename.endswith(".ipynb"):
        old_filepath = os.path.join(folder_path, filename)
        new_filename = filename.replace('-', '_')
        new_filepath = os.path.join(folder_path, new_filename)

        os.rename(old_filepath, new_filepath)
        print(f"Renamed: {filename} -> {new_filename}")