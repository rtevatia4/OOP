"""
we only need to define the radius of the circle in the constructor. After that, the area() and perimeter() functions are available to us. 
This interface is part of encapsulation.

We use the functions to calculate the area and perimeter. Users do not need to know the implementation details of the functions. 
Even pi is hidden since it’s a constant. This is how we can achieve abstraction using classes.
"""
class Circle:
    def __init__(self):
        self.__radius = 0
        self.__pi = 3.142
    
    def __init__(self, r):
        self.__radius = r
        self.__pi = 3.142
    
    def calculate_area(self):
        return self.__pi * self.__radius * self.__radius

    def calculate_perimeter(self):
        return 2 * self.__pi * self.__radius

if __name__=="__main__":
    circle = Circle(5)
    print("Area:", circle.calculate_area())
    print("Perimeter:", circle.calculate_perimeter())