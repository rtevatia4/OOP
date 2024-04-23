class Car:
    def __init__(self, make, model, year):
        self.__make = make   # Private attribute (making it private with __ prefix)
        self.__model = model # Private attribute
        self.__year = year   # Private attribute

    def display_info(self):
        print(f"Make: {self.__make}, Model: {self.__model}, Year: {self.__year}")

    def get_make(self):
        return self.__make

    def set_make(self, make):
        self.__make = make

# Creating an object of the Car class
car1 = Car("Toyota", "Camry", 2020)

# Accessing attributes using methods
print(car1.get_make())  # Output: Toyota

# Modifying attributes using methods
car1.set_make("Honda")
print(car1.get_make())  # Output: Honda

# Directly accessing private attributes (not recommended)
# Note: Python does not enforce strict encapsulation like other languages
print(car1._Car__make)  # Output: Honda

# Attempting to access private attributes (raises AttributeError)
# print(car1.__make)

"""
The Car class encapsulates the data (make, model, year) and methods (display_info, get_make, set_make) within a single unit.
The attributes (__make, __model, __year) are marked as private by prefixing them with double underscores (__). 
This means they are not directly accessible from outside the class.

Methods like get_make and set_make are provided to interact with the private attributes. 
These methods encapsulate the logic for accessing and modifying the attributes, providing controlled access to the data.
The display_info method allows for displaying the information about the car.

Although Python does not enforce strict encapsulation (like some other languages), using private attributes and methods helps 
in organizing code and preventing accidental modification of internal state. Accessing private attributes directly (using name mangling)
 is possible but discouraged.
 
Encapsulation helps in hiding the internal state of objects and providing controlled access to it, thus promoting data integrity and 
reducing the risk of unintended side effects.
"""