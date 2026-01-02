from pathlib import Path
import json

# This file contains a function to save data to a JSON file
# Would contain as well to save to a backup file if needed

def save_json(data, file_path):
    path = Path(file_path)
    with open(path, 'w') as file:
        json.dump(data, file, indent=4)
        