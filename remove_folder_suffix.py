import os

def rename_folders(suffix_to_remove):
    # Get the current directory where the script is located
    current_directory = os.getcwd()

    # Get a list of all subdirectories in the current directory
    subdirectories = [d for d in os.listdir(current_directory) if os.path.isdir(os.path.join(current_directory, d))]

    # Iterate over each subdirectory
    for folder_name in subdirectories:
        # Check if the folder name ends with the specified suffix
        if folder_name.endswith(suffix_to_remove):
            # Remove the suffix from the folder name
            new_folder_name = folder_name[:-len(suffix_to_remove)]

            # Construct the full paths for the old and new folder names
            old_path = os.path.join(current_directory, folder_name)
            new_path = os.path.join(current_directory, new_folder_name)

            # Rename the folder
            os.rename(old_path, new_path)
            print(f"Renamed '{folder_name}' to '{new_folder_name}'")

# Ask the user for the suffix to remove
suffix_to_remove = input("Enter the folder suffix to remove: ")

# Call the function to rename folders in the current directory
rename_folders(suffix_to_remove)
