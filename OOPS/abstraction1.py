from abc import ABC, abstractmethod

class Organization(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_employees(self):
        pass

class Department(Organization):
    def __init__(self, name):
        self.name = name
        self.employees = []

    def get_name(self):
        return self.name

    def get_employees(self):
        return self.employees

class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department

    def get_name(self):
        return self.name

    def get_department(self):
        return self.department

# Create an organization
# org = Organization()

# Create a department
dept = Department("Engineering")

# Add employees to the department
dept.employees.append(Employee("Alice", dept))
dept.employees.append(Employee("Bob", dept))

# Get the name of the organization
print(dept.get_name())

# Get the employees of the department
print(dept.get_employees())