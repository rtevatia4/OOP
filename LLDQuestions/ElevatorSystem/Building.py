class __Building(object):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(__Building, cls).__new__(cls)
        
        return cls.__instance

class Building(__Building):
    def __init__(self):
        self.__floors = []
        self.__elevators = []