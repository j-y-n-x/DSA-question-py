import os
import shutil

def organize_files(source_folder, destination_folder):
    # Ensure the destination folder exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Iterate through each file in the source folder
    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)

        # Check if it's a file
        if os.path.isfile(source_path):
            # Get the file extension
            file_extension = filename.split('.')[-1].lower()

            # Define destination folder based on the file extension
            destination_path = os.path.join(destination_folder, file_extension)

            # Ensure the destination folder for the file type exists
            if not os.path.exists(destination_path):
                os.makedirs(destination_path)

            # Move the file to the corresponding folder
            shutil.move(source_path, os.path.join(destination_path, filename))

if __name__ == "__main__":
    source_directory = "C:/Users/shris/OneDrive/Desktop/py/"
    destination_directory = "C:/Users/shris/OneDrive/Desktop/py/new/"

    organize_files(source_directory, destination_directory)