import os

def print_txt_files_in_current_folder():
    # Get the current directory
    current_directory = os.getcwd()
    
    # Get a list of all files in the current directory
    files = os.listdir(current_directory)
    
    # Iterate over each file in the directory
    for file in files:
        # Check if the file is a .txt file
        if file.endswith(".txt"):
            print(file[:-4])

# Example usage:
print_txt_files_in_current_folder()



