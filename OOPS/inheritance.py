# Parent Class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Unknown Sound"

# Child Class inherting from Animal
class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"


dog = Dog("Buddy")
cat = Cat("Whiskey")

print(dog.name + " says " + dog.speak())
print(cat.name + " says " + cat.speak())

'''
Animal is the parent class with a constructor __init__ method that initializes the name attribute.

Animal also has a method speak, which returns "Unknown sound". This method will be overridden by child classes.

Dog and Cat are child classes inheriting from Animal. They inherit both the attributes and methods of the parent class.

Both Dog and Cat classes have their own speak method, which overrides the speak method inherited from Animal.
Instances of Dog and Cat classes (dog and cat) are created with specific names.

The speak method is called on each instance, returning the appropriate sound for each animal.

This demonstrates how child classes inherit properties and behaviors from their parent class and can override methods to 
provide specialized behavior. Inheritance promotes code reuse and facilitates the creation of hierarchical relationships between classes.
'''