# Deleting a file data entry by its ID
from pathlib import Path
from .load_json import load_json
from .save_json import save_json
from .update_data import update_file_safe_to_delete

to_save_path = Path('../FileWhy/FileWhy/directories.json')

# Delete file data by ID
def delete_file_data(file_id):
    directories = load_json(to_save_path)
    for i, file in enumerate(directories):
        if file['id'] == file_id:
            if file['safe_to_delete']:
                directories.pop(i)
                save_json(directories, to_save_path)
                print(f"File with ID {file_id} has been deleted.")
                return directories
            else:
                print(f"File with ID {file_id} is not marked as safe to delete.")
                print(f"Want to set it to safe to delete? (yes/no): ")
                choice = input().strip().lower()
                if choice == 'yes':
                    update_file_safe_to_delete(file_id)
                    directories = load_json(to_save_path)  # Reload after update
                    directories.pop(i)
                    save_json(directories, to_save_path)
                    print(f"File with ID {file_id} has been deleted.")
                    return directories
                else:
                    print("Deletion cancelled.")
                return None
    print(f"No file found with ID {file_id}.")
    return None