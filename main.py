import os
import shutil

# The path where file is located
downloads_folder = os.path.expanduser("~") + "/Documents/"

# The path where you want to move the file
target_folder = os.path.expanduser("~") + "/Documents/Movedfiles/"

# Those extension which you would like to move.
file_extension = (".txt", ".pdf", ".docx")

# Loop through all files in the downloads folder
for filename in os.listdir(downloads_folder):
    # Check if the file has the desired extension
    if filename.endswith(file_extension):
        # If so, construct the full path to the file
        source_path = os.path.join(downloads_folder, filename)
        # Construct the full path to the target folder
        target_path = os.path.join(target_folder, filename)
        # Move the file to the target folder
        shutil.move(source_path, target_path)
        print(f"Moved {filename} to {target_folder}")