# 39.  Simple Backup Script   
#     *Description*: Write a script that backs up important files or directories to a specified location.  
#     *Skills*: File handling, os module, automation.

import os
import shutil
from datetime import datetime

def backup(source, destination):
    """Backup files or directories to the specified location."""
    # Check if source exists
    if not os.path.exists(source):
        print(f"Error: Source '{source}' does not exist.")
        return
    
    # Create a timestamped folder in the destination directory
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    source_name = os.path.basename(source.rstrip(os.sep))  # Get name of the file/directory
    backup_folder = f"{source_name}_backup_{timestamp}"
    backup_path = os.path.join(destination, backup_folder)
    
    try:
        # If it's a file, copy the file
        if os.path.isfile(source):
            shutil.copy2(source, backup_path)
            print(f"File '{source}' backed up successfully to '{backup_path}'.")
        
        # If it's a directory, copy the whole directory
        elif os.path.isdir(source):
            shutil.copytree(source, backup_path)
            print(f"Directory '{source}' backed up successfully to '{backup_path}'.")
    except Exception as e:
        print(f"Error during backup: {e}")

# Example usage
if __name__ == "__main__":
    source = input("Enter the path to the file or directory to back up: ")
    destination = input("Enter the backup destination folder: ")
    backup(source, destination)
