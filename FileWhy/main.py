# Python library imports
from pathlib import Path

# Python custom imports
from .services.load_json import load_json
from .models.file_model import FileModel
from .services.create import create_file_data
from .services.view_data import view_data

to_save_path = Path('../FileWhy/FileWhy/directories.json')

def main():
    print("Welcome to FileWhy!")    

    while True:
        print("\nMenu:")
        print("1. Create new file entry")
        print("2. View all file entries")
        print("3. Exit")
        
        choice = input("Enter your choice: \n")
        
        if choice == '1':
            path = input("Enter file path: ")
            description = input("Enter file description: ")
            published_at = input("Enter published date (YYYY-MM-DD) or leave blank for today: ")
            create_file_data(path, description, published_at)
            print("File entry created successfully!")
        
        elif choice == '2':
            try:
                files = load_json(to_save_path)
                view_data(files)
            except FileNotFoundError as e:
                print(e)
        
        elif choice == '3':
            print("Exiting FileWhy. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()