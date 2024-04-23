class __ElevatorSystem(object):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(__ElevatorSystem, cls).__new__(cls)
        
        return cls.__instance

class ElevatorSystem(metaclass=__ElevatorSystem):
    def __init__(self, building):
        self.__building = building
    
    def monitoring(self):
        pass

    def dispatcher(self):
        pass


