"""
In Python, __init__ and self are special constructs used in object-oriented programming, 
specifically in classes and object instantiation.

__init__ is a special method in Python classes that is automatically called when an object of the class is created (instantiated).
It is commonly used to initialize the object's attributes or perform any setup tasks needed for the object to be in a valid state.

The self(refers to the instance of the class itself) parameter inside the __init__ method refers to the current instance of the Dog class, 
allowing us to access and set the attributes of the object.

Every time you create a new Dog object, .__init__() sets the initial state of the object by assigning the values of the 
object’s properties. That is, .__init__() initializes each new instance of the class.

Methods like .__init__() and .__str__() are called dunder methods because they begin and end with double underscores.

"""
class Dog:
    species = "Canis Familiaris" # class attribute: will have same value for all class instances

    def __init__(self, name, age):
        self.name = name  # instance attributes (instance variables)
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
    # Instance Methods 
    def description(self):
        return f"{self.name} is {self.age} year old"
    
    def speak(self, sound):
        return f"{self.name} says {sound}"

dog = Dog("tuffy",5)
print(dog.name,dog.age,dog.description(), dog.speak("bbbb"))
print(dog)