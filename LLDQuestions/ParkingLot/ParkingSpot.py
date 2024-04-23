from abc import ABC, abstractmethod

class ParkingSpot(ABC):
    def __init__(self, id, isFree, vehicle):
        self.__id = id
        self.__isFree = isFree
        self.__vehicle = vehicle # Refers to an instance of the Vehicle class
    
    def get_is_free(self):
        pass

# vehicle here refers to an instance of the Vehicle class
    @abstractmethod
    def assign_vehicle(self, vehicle):
        pass

    def remove_vehicle(self):
        pass

class Handicapped(ParkingSpot):
    def __init__(self, id, isFree, vehicle):
        super().__init__(id, isFree, vehicle)
    
    def assign_vehicle(self, vehicle):
        pass

class Compact(ParkingSpot):
    def __init__(self, id, isFree, vehicle):
        super().__init__(id, isFree, vehicle)
    
    def assign_vehicle(self, vehicle):
        pass

class Large(ParkingSpot):
    def __init__(self, id, isFree, vehicle):
        super().__init__(id, isFree, vehicle)
    
    def assign_vehicle(self, vehicle):
        pass

class Motorcycle(ParkingSpot):
    def __init__(self, id, isFree, vehicle):
        super().__init__(id, isFree, vehicle)
    
    def assign_vehicle(self, vehicle):
        pass