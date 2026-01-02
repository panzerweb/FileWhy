from pathlib import Path
from ..services.load_json import load_json
from ..services.save_json import save_json

to_save_path = Path('../FileWhy/FileWhy/directories.json')

# Update the safe_to_delete status of a file entry by its ID
def update_file_safe_to_delete(file_id):
    directories = load_json(to_save_path)
    for file in directories:
        if file['id'] == file_id:
            file['safe_to_delete'] = not file['safe_to_delete']
            save_json(directories, to_save_path)
            print(f"File ID {file_id} safe_to_delete status updated to {file['safe_to_delete']}.")
            return directories
    print(f"No file found with ID {file_id}.")
    return None