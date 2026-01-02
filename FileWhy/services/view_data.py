# Displays data to the user in a readable format

def view_data(arr_of_file):
    for file in arr_of_file:
        print(f"ID: {file['id']}")
        print(f"Path: {file['path']}")
        print(f"Description: {file['description']}")
        print(f"Published At: {file['published_at']}")
        print("-" * 20)