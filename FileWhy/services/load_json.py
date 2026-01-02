import json
from pathlib import Path

# This file contains a function to load data from a JSON file

def load_json(file_path):
    path = Path(file_path)
    if path.exists() and path.suffix == '.json':
        with open(path, 'r') as file:
            try:
                data = json.load(file)
                return data
            except json.JSONDecodeError:
                # If file is empty or corrupted, start fresh
                return []
    else:
        return []
        # raise FileNotFoundError(f"The file {file_path} does not exist or is not a JSON file.")
    
