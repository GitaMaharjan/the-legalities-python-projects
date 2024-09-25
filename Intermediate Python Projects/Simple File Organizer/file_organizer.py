# 21.  Simple File Organizer   
#     *Description*: Write a program to organize files in a directory based on file types.  
#     *Skills*: File handling, os module, loops.
import os
import shutil

# Defines the directory to be organized
directory = 'Simple File Organizer/trial_directory'

# Creates a mapping of file extensions to their corresponding folder names
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx'],
    'Audio': ['.mp3', '.wav', '.aac'],
    'Videos': ['.mp4', '.avi', '.mov'],
    'Archives': ['.zip', '.tar', '.rar'],
    'Others': []  # Categorizes files with unknown extensions
}

# Lists all files in the specified directory
for filename in os.listdir(directory):
    # Gets the full path of each file
    file_path = os.path.join(directory, filename)
    
    # Skips directories if encountered
    if os.path.isdir(file_path):
        continue

    # Extracts the file extension and converts it to lowercase
    file_ext = os.path.splitext(filename)[1].lower()

    # Initializes the default folder as 'Others' for files with unknown extensions
    destination_folder = 'Others'
    # Loops through file types to find a matching extension
    for folder, extensions in file_types.items():
        if file_ext in extensions:
            destination_folder = folder
            break

    # Constructs the destination folder path
    dest_folder_path = os.path.join(directory, destination_folder)
    # Creates the folder if it doesn't already exist
    if not os.path.exists(dest_folder_path):
        os.makedirs(dest_folder_path)

    # Moves the file to the appropriate folder
    shutil.move(file_path, os.path.join(dest_folder_path, filename))

# Prints a message when the process completes successfully
print("Files have been organized successfully.")
