from pathlib import Path
import json
import datetime
from .load_json import load_json
from .save_json import save_json
from ..models.file_model import FileModel

# This file serves to create a new file entry and save it to the directories.json file

to_save_path = Path('../FileWhy/FileWhy/directories.json')

# Create and save new file data
def create_file_data(path, title, description, published_at):
    directories = load_json(to_save_path)

    if not published_at:
        published_at = datetime.datetime.now().strftime('%Y-%m-%d')

    if path == '' or title == '' or description == '':
        print("Path, Title, and Description cannot be empty.")
        return

    try:
        if directories:
            new_id = max(file['id'] for file in directories) + 1
        else:
            new_id = 1

        new_file = FileModel(new_id, path, title, description, [], False, published_at)
        directories.append(new_file.to_dict())

        save_json(directories, to_save_path)
    except Exception as e:
        print(f"An error occurred while creating the file entry: {e}")

# Add a tag to an existing file entry
def add_tag_to_file(file_id, tag):
    directories = load_json(to_save_path)
    for file in directories:
        if file['id'] == file_id:
            file['tags'].append(tag)
            save_json(directories, to_save_path)
            print(f"Tag '{tag}' added to file ID {file_id}.")
            print("Successfully added tag.")
            break
    else:
        print(f"No file found with ID {file_id}.")
