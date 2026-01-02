# Displays data to the user in a readable format
import datetime;

# View and display all records of files
def view_data(arr_of_file):
    for file in arr_of_file:
        if file:
            print(f"ID: {file['id']}")
            print(f"Path: {file['path']}")
            print(f"Title: {file['title']}")
            print(f"Description: {file['description']}")
            print(f"Tags: {file['tags']}")
            print(f"Safe to Delete: {file['safe_to_delete']}")
            print(f"Published At: {file['published_at']}")
            print("-" * 20)
        else:
            print("No existing record found.")

# View and display records yesterday
def view_year_by_yesterday(arr_of_file):
    yesterday_date = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    for file in arr_of_file:
        if file['published_at'] == yesterday_date:
            print(f"ID: {file['id']}")
            print(f"Path: {file['path']}")
            print(f"Title: {file['title']}")
            print(f"Description: {file['description']}")
            print(f"Tags: {file['tags']}")
            print(f"Safe to Delete: {file['safe_to_delete']}")
            print(f"Published At: {file['published_at']}")
            print("-" * 20)
        else:
            print("No records found for yesterday's date.")