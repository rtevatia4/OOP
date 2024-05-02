from abc import ABC, abstractmethod

class Burger:
  def __init__(self):
    self.bread = None
    self.patties = None
    self.cheese = None
    self.toppings = []
  
  def __str__(self):
    return f"Burger with Bread: {self.bread}, Patties: {self.patties}, Cheese: {self.cheese}, Topping: {self.toppings}"
  
class Builder:
  @abstractmethod
  def add_bread(self):
    pass
  
  @abstractmethod
  def add_patties(self):
    pass
  
  @abstractmethod
  def add_cheese(self):
    pass
  
  @abstractmethod
  def add_topping(self):
    pass

  @abstractmethod
  def build(self):
    pass

class BurgerBuilder(Builder):
  def __init__(self):
    self.burger = Burger()
  
  def add_bread(self, bread):
    self.burger.bread = bread
    return self
  
  def add_patties(self, patty):
    self.burger.patties = patty
    return self
  
  def add_cheese(self, cheese):
    self.burger.cheese = cheese
    return self
  
  def add_topping(self, topping):
    self.burger.toppings.append(topping)
    return self
  
  def build(self):
    return self.burger

builder = BurgerBuilder()
burger = builder.add_bread("Wheat") \
                .add_patties("Chicken") \
                .add_cheese("American") \
                .add_topping("Tomato") \
                .add_topping("Onion") \
                .add_topping("Lettuce") \
                .build()

print(burger)
