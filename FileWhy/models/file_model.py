# A model for the File Class, listed here are the attributes and methods

class FileModel:
    def __init__(self, id, path, description, published_at = '0000-00-00'):
        self.__id = id
        self.__path = path
        self.__description = description
        self.__published_at = published_at

    # To dictionary method
    def to_dict(self):
        return {
            "id": self.__id,
            "path": self.__path,
            "description": self.__description,
            "published_at": self.__published_at
        }
    
    def print_info(self):
        print(f"File ID: {self.__id}")
        print(f"Path: {self.__path}")
        print(f"Description: {self.__description}")
        print(f"Published At: {self.__published_at}")