import os

OBSIDIAN_FOLDER_PATH = r"D:\Notes"
DOCUSAURUS_FOLDER_PATH = r"D:\MindLab\second-brain"

for path, subdirs, files in os.walk(OBSIDIAN_FOLDER_PATH):
    for name in files:
        print(os.path.join(path, name))