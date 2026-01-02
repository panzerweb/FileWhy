# Python library imports
from pathlib import Path

# Python custom imports
from .services.load_json import load_json
from .models.file_model import FileModel
from .services.create import *
from .services.view_data import *
from .services.delete_data import *

to_save_path = Path('../FileWhy/FileWhy/directories.json')

def main():
    print("Welcome to FileWhy!")    

    while True:
        print("\nMenu:")
        print("new_file -> Create new file entry")
        print("view_all -> View all file entries")
        print("view_history -> View history by yesterday's date")
        print("add_tag -> Add tag to a file entry")
        print("delete_file -> Delete a file entry by ID")
        print("0. Exit")
        
        choice = input("Enter your choice: \n").strip()
        
        if choice == 'new_file':
            path = input("Enter full file path: ")
            title = input("Enter file title: ")
            description = input("Enter file description: ")
            published_at = input("Enter published date (YYYY-MM-DD) or leave blank for today: ")
            create_file_data(path, title,description, published_at)
        
        elif choice == 'view_all':
            try:
                files = load_json(to_save_path)
                if len(files) > 0:
                    view_data(files)
                else:
                    print("No records found.")
            except FileNotFoundError as e:
                print(e)
        
        elif choice == 'view_history':
            try:
                files = load_json(to_save_path)
                if len(files) > 0:
                    view_year_by_yesterday(files)
                else:
                    print("No records found.")
            except FileNotFoundError as e:
                print(e)
        
        elif choice == 'add_tag':
            file_id = int(input("Enter File Id: "))
            tag = input("Enter tag to add: ")
            add_tag_to_file(file_id, tag)

        elif choice == 'delete_file':
            file_id = int(input("Enter File Id to delete: "))
            delete_file_data(file_id)
        
        elif choice == '0':
            print("Exiting FileWhy. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()