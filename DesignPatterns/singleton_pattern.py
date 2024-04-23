class Singleton:
    _instance = None

    @staticmethod
    def get_instance():
        if Singleton._instance is None:
            Singleton._instance = Singleton()
        return Singleton._instance

    def __init__(self):
        if Singleton._instance is not None:
            raise Exception("Singleton instance already exists")
        

# Retrieving the Singleton instance
singleton_instance1 = Singleton.get_instance()
singleton_instance2 = Singleton.get_instance()

print(singleton_instance1 is singleton_instance2)  # Output: True (Both references point to the same instance)

# s = Singleton() this raises an error since the instance is already created
