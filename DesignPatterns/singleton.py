class Singleton:
    __instance = None

    @staticmethod
    def create_instance():
        if Singleton.__instance == None:
            Singleton.__instance = Singleton()
        return Singleton.__instance
    
    def __init__(self) -> None:
        if Singleton.__instance is not None:
            raise Exception("Instance is already created")
        else:
            Singleton.__instance = self

class __ParkingLot(object):
    __instances = None

    def __new__(cls):
        if cls.__instances is None:
            cls.__instances = super(__ParkingLot, cls).__new__(cls)
        return cls.__instances
    
if __name__ == "__main__":
    singleton_ins1 = Singleton.create_instance()
    print(singleton_ins1)
    singleton_ins2 = Singleton.create_instance()
    print(singleton_ins2)  # Same instance as 1
    # s = Singleton()    Throws error
    s = __ParkingLot
    print(s)