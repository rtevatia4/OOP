"""
We define an abstract class Shape that represents a generic geometric shape. 
It contains an abstract method area, which must be implemented by its subclasses.
Circle and Rectangle are concrete subclasses of Shape. They provide their own implementations of the area method, 
specific to their respective shapes.
We create objects of Circle and Rectangle and call the area method on each object.

Despite the differences in implementation between Circle and Rectangle, we can treat them uniformly as Shape objects and 
call the area method on them. This is the essence of abstraction: hiding the implementation details and providing a simplified 
interface for working with objects.

Abstraction allows us to work with complex systems in a more manageable way, focusing only on the essential aspects while 
hiding the complexities under the hood. This leads to cleaner, more modular, and more maintainable code.
"""
from abc import ABC, abstractmethod

# Abstract class representing a Shape
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Concrete class representing a Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# Concrete class representing a Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Creating objects of Circle and Rectangle
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Calling the area method on Circle and Rectangle objects
print("Area of circle:", circle.area())        # Output: Area of circle: 78.5
print("Area of rectangle:", rectangle.area())  # Output: Area of rectangle: 24