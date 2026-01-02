# A model for the File Class, listed here are the attributes and methods

class FileModel:
    def __init__(self, id, path, title, description, tags = [],safe_to_delete = False, published_at = '0000-00-00'):
        self.__id = id
        self.__path = [path]
        self.__title = title
        self.__description = description
        self.__tags = tags
        self.__safe_to_delete = safe_to_delete
        self.__published_at = published_at

    # To dictionary method
    def to_dict(self):
        return {
            "id": self.__id,
            "path": self.__path,
            "title": self.__title,
            "description": self.__description,
            "tags": self.__tags,
            "safe_to_delete": self.__safe_to_delete,
            "published_at": self.__published_at
        }
    
    def print_info(self):
        print(f"File ID: {self.__id}")
        print(f"Path: {self.__path}")
        print(f"Title: {self.__title}")
        print(f"Description: {self.__description}")
        print(f"Tags: {self.__tags}")
        print(f"Safe to Delete: {self.__safe_to_delete}")
        print(f"Published At: {self.__published_at}")