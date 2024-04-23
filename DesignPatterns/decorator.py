# Component Interface
class Coffee:
    def get_cost(self):
        pass

# Concrete Component
class SimpleCoffee(Coffee):
    def get_cost(self):
        return 10

#Decorator class
class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self.coffee = coffee
    
    def get_cost(self):
        return self.coffee.get_cost()

#Concrete Decorators
class MilkDecorator(CoffeeDecorator):
    def get_cost(self):
        return f"Price of simple coffee with Milk is ${self.coffee.get_cost()+5}"

#Concrete Decorators
class SugarDecorator(CoffeeDecorator):
    def get_cost(self):
        return f"Price of simple coffee with Sugar is ${self.coffee.get_cost()+2}"

#cleint code
coffee = SimpleCoffee()
print("Cost of simple coffee is: $", coffee.get_cost())

# Add milk to the coffee
coffee_with_milk = MilkDecorator(coffee)
print(coffee_with_milk.get_cost())

# Add sugar to the coffee
coffee_with_sugar = SugarDecorator(coffee)
print(coffee_with_sugar.get_cost())