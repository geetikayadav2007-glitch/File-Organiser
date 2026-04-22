import os
import shutil

# Folder path to organize (change this path)
path = "C:/Users/YourName/Downloads"

# File categories
file_types = {
    "Images": [".jpg", ".png", ".jpeg", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
    "Programs": [".py", ".cpp", ".java"]
}

# Create folders if not exist
for folder in file_types.keys():
    folder_path = os.path.join(path, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Organize files
for file in os.listdir(path):
    file_path = os.path.join(path, file)

    if os.path.isfile(file_path):
        for folder, extensions in file_types.items():
            if file.endswith(tuple(extensions)):
                shutil.move(file_path, os.path.join(path, folder, file))
                print(file + " moved to " + folder)
                break

print("Files Organized Successfully!")
