class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def display(self):
        print(f"Person name is {self.name}:{self.id}")
    
    def details(self):
        print(f"Person name is {self.name}")
        print(f"Person id is {self.id}")

class Employee(Person):
    def __init__(self, name, id, salary, post):
        self.salary = salary
        self.post = post
        Person.__init__(self, name, id)
        # super().__init__(name, id)   # don't have to pass self explicitly as an argument
    
    def details(self):
        print(f"Employee name is {self.name}")
        print(f"Employee id is {self.id}")
        print(f"Employee Salary is {self.salary}")
        print(f"Employee Post is {self.post}")

        super().details()

a = Employee("Rahul", 123456, 500000, "SDE3")

a.display()
a.details()