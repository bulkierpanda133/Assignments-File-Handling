import os

def list_directory_contents(path):
    try:
        # Check if the path exists
        if not os.path.exists(path):
            print(f"The directory '{path}' does not exist.")
            return
        
        # List all files and directories in the given path
        items = os.listdir(path)
        
        # If the directory is empty
        if not items:
            print(f"The directory '{path}' is empty.")
            return
        
        print(f"Contents of the directory '{path}':")
        for item in items:
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                print(f"[DIR]  {item}")
            else:
                print(f"[FILE] {item}")
    
    except PermissionError:
        print(f"Permission denied: Unable to access the directory '{path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Prompt the user for the directory path
directory_path = input("Enter the directory path: ")
list_directory_contents(directory_path)
