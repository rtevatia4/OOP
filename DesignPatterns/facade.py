from __future__ import annotations

class Facade:
    def __init__(self, subsystem1 : Subsystem1, subsystem2: Subsystem2):
        self.subsystem1 = subsystem1 or Subsystem1()
        self.subsystem2 = subsystem2 or Subsystem2()
    
    def operation(self):
        print("Facade Initializes Subsystems")
        print(self.subsystem1.operation1())
        print(self.subsystem1.operation_n())
        print(self.subsystem2.operation1())
        print(self.subsystem2.operation_n())

class Subsystem1:
    def operation1(self):
        return "Subsystem 1: Start"
    
    def operation_n(self):
        return "Subsystem 1: End"

class Subsystem2:
    def operation1(self):
        return "Subsystem 2: Start"
    
    def operation_n(self):
        return "Subsystem 2: End"

def client_code(facade: Facade):
    facade.operation()

if __name__ == "__main__":
    subsystem1 = Subsystem1()
    subsystem2 = Subsystem2()
    facade = Facade(subsystem1,subsystem2)
    client_code(facade)