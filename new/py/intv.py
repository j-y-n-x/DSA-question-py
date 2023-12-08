import os
import shutil

def organize_files(source_dir, destination_dir):
    # Ensure the destination directory exists
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Loop through files in the source directory
    for filename in os.listdir(source_dir):
        source_path = os.path.join(source_dir, filename)

        # Ignore directories
        if os.path.isdir(source_path):
            continue

        # Get the file extension
        _, file_extension = os.path.splitext(filename)

        # Define destination directory based on file extension
        destination_subdir = os.path.join(destination_dir, file_extension[1:])
        if not os.path.exists(destination_subdir):
            os.makedirs(destination_subdir)

        # Build the destination path
        destination_path = os.path.join(destination_subdir, filename)

        # Move the file to the organized directory
        shutil.move(source_path, destination_path)

        print(f"Moved: {filename} to {destination_path}")

if __name__ == "__main__":
    # Specify the source and destination directories
    source_directory = "/path/to/source/directory"
    destination_directory = "/path/to/destination/directory"

    # Organize files
    organize_files(source_directory, destination_directory)
