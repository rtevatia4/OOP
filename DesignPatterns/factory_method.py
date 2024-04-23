from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def getType(self):
        pass

class Car(Vehicle):
    def getType(self):
        return "Car"

class Bike(Vehicle):
    def getType(self):
        return "Bike"

class Truck(Vehicle):
    def getType(self):
        return "Truck"

class VehicleFactory(ABC):
    @abstractmethod
    def createVehicle(self):
        pass

class CarFactory(VehicleFactory):
    def createVehicle(self):
        return Car()

class BikeFactory(VehicleFactory):
    def createVehicle(self):
        return Bike()

class TruckFactory(VehicleFactory):
    def createVehicle(self):
        return Truck()


car = CarFactory()
bike = BikeFactory()
truck = TruckFactory()

mycar = car.createVehicle()
print(mycar.getType())

mybike = bike.createVehicle()
print(mybike.getType())

mytruck = truck.createVehicle()
print(mytruck.getType())

