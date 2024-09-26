# 26.  Directory Tree Generator   
#     *Description*: Develop a program that prints a visual tree structure of directories and files.  
#     *Skills*: File handling, os module, recursion.


import os

class DirectoryTree:
    def __init__(self, root_dir):
        self.root_dir = root_dir

    def generate_tree(self):
        print(self.root_dir)  # Print the root directory name
        self._print_tree(self.root_dir, 0)  # Start recursion from the root directory

    def _print_tree(self, current_dir, depth):
        try:
            # List all files and directories in the current directory
            items = sorted(os.listdir(current_dir))  # Sort items alphabetically
        except PermissionError:
            return  # Skip directories we don't have permission to access

        # Loop through all items in the directory
        for item in items:
            item_path = os.path.join(current_dir, item)
            # Create appropriate indentation based on depth
            prefix = "|   " * depth + "|-- "
            
            if os.path.isdir(item_path):
                # Print the directory with "/" at the end
                print(f"{prefix}{item}/")
                # Recursively call the function for the subdirectory
                self._print_tree(item_path, depth + 1)
            else:
                # Print the file
                print(f"{prefix}{item}")

# Example usage:
if __name__ == "__main__":
    root_directory = input("Enter the root directory path: ")
    tree = DirectoryTree(root_directory)
    tree.generate_tree()
