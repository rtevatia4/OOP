# Singleton Library class

class Library:
    __instance = None

    def __init__(self):
        self.name = None
        self.address = None

    @staticmethod
    def get_instance():
        if Library.__instance is None:
            Library.__instance = Library()
        return Library.__instance
    
    def get_address(self):
        return self.address
    
    
# @classmethod
# def get_instance(cls):
#     if cls._library is None:
#         cls._library = cls()
#     return cls._library