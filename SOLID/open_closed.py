# Open closed principle states that classes should be open for extension but
# closed for modification

# Below class does not follow the principle.
# In below class , we have to make the change if more animal types are being added.
# class Animal:
#     def __init__(self, animal_type):
#         self.animal_type = animal_type
    
#     def get_animal(self):
#         return self.animal_type
    
#     def eats(self):
#         if self.animal_type == "Monkey":
#             print("Monkey eats Banana")
#         elif self.animal_type == "Squirrel":
#             print("Squirrle eats Peanuts")
#         elif self.animal_type == "Dog":
#             print("Dog eats cookies")
#         else:
#             print("Default")

# Below implmentaion follow the principle
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def eats(self):
        pass

class Monkey(Animal):
    def __init__(self, animal_type):
        self.animal_type = animal_type

    def eats(self):
        print(f"{self.animal_type} eats Banana")

class Squirrel(Animal):
    def __init__(self, animal_type):
        self.animal_type = animal_type

    def eats(self):
        print(f"{self.animal_type} eats Peanuts")

class Dog(Animal):
    def __init__(self, animal_type):
        self.animal_type = animal_type

    def eats(self):
        print(f"{self.animal_type} eats cookies")

an = Dog("Dog")
an.eats()
