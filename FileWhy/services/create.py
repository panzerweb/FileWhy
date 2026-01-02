from pathlib import Path
import json
import datetime
from .load_json import load_json
from .save_json import save_json
from ..models.file_model import FileModel

# This file serves to create a new file entry and save it to the directories.json file

to_save_path = Path('../FileWhy/FileWhy/directories.json')

def create_file_data(path, description, published_at):
    if not published_at:
        published_at = datetime.datetime.now().strftime('%Y-%m-%d')

    directories = load_json(to_save_path)

    if directories:
        new_id = max(file['id'] for file in directories) + 1
    else:
        new_id = 1
    
    new_file = FileModel(new_id, path, description, published_at)
    directories.append(new_file.to_dict())

    save_json(directories, to_save_path)
    