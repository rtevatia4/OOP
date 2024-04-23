# Base Class (Parent)
class Vehicle:
    def __init__(self, name, model):
        self.name = name
        self.model = model
    
    def get_details(self):
        print("This car is a ", self.name, self.model)

# Single Inheritance

# Child class extending from Base class
class FuelCar(Vehicle):
    def __init__(self, name, model, combust_type):
        self.combust_type = combust_type
        Vehicle.__init__(self, name, model)
    
    def get_fuel_car(self):
        super().get_details()
        print("And it is of type: ", self.combust_type)

#Hierachical, along with fuel class ElectricCar also extends from Vehicle class
# Child class extending from Base class
class ElectricCar(Vehicle):
    def __init__(self, name, model, battery_power):
        self.battery_power = battery_power
        Vehicle.__init__(self, name, model)
    
    def get_electric_car(self):
        super().get_details()
        print("And it has battery power: ", self.battery_power)

# Multiple inheritance
# The HybridCar class is derived from two different classes, The GasolineCar class and the ElectricCar class 
# Derived class
class HybridCar(FuelCar, ElectricCar):

    def __init__(self, name, model, combust_type, battery_power):
        FuelCar.__init__(self, name, model, combust_type)
        ElectricCar.__init__(self,name, model, battery_power)
        self.battery_power = battery_power

    def get_hybrid(self):
        self.get_fuel_car()
        print(", battery power is",self.battery_power)

# main
def main():
    print("Single inheritance:")
    Fuel = FuelCar("Honda", "Accord", "Petrol")
    Fuel.get_fuel_car()
    print("\n")

    print("Hierarchical inheritance:")
    Electric = ElectricCar("Tesla", "ModelX", "200MWH")
    Electric.get_electric_car()
    print("\n")

    print("Multiple inheritance:")
    Hybrid = HybridCar("Toyota", "Prius", "Hybrid", "100MWH")
    Hybrid.get_hybrid()
main()