# Base class 1
class Person:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        return f"Hello, my name is {self.name}."
    
#Base class 2
class Employee:
    def __init__(self, employee_id):
        self.employee_id = employee_id

    def get_id(self):
        return f"My employee ID is {self.employee_id}."
    
# Derived class inheriting from both Person and Employee
class Manager(Person, Employee):
    def __init__(self, name , employee_id, department):
        Person.__init__(self, name) # Initialise Person Part
        Employee.__init__(self, employee_id) # Initialise Employee Part
        self.department = department

    def show_details(self):
        return f"{self.greet()} {self.get_id()} I manage the {self.department} department."
    
# Create an instance of the derived class
manager = Manager("Rishav", "S6679", "HR")

# Call methods from base classes and derived class
print(manager.greet())
print(manager.get_id())
print(manager.show_details())