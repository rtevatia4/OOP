# Method OVerriding
class Animal:
    def print_animal(self):
        print("This is Animal Class")
    
    def do_something(self):
        print("I am Animal")

class Tiger(Animal):
    def print_animal(self):
        print("This is Tiger Class, I've overriden the Parent class implementation")

tiger = Tiger()
tiger.print_animal()
tiger.do_something()

# Method OVerloading
class Shape:
    def calculate_Area(self, length, breadth=None):
        if breadth:
            return length*breadth
        else:
            return length*length

shape = Shape()
print("Area of rectangle is: ", shape.calculate_Area(4,5))
print("Area of square is: ", shape.calculate_Area(4))