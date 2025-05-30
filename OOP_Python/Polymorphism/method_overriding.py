# Method Overriding

from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def draw(self):
        "Abstract Method"
        return
    
class circle(shape):
    def draw(self):
        super().draw()      # Using super() to call the parent method
        print("Draw a circle")
        return
    
class rectangle(shape):
    def draw(self):
        super().draw()      # Using super() to call the parent method
        print("Draw a rectangle")
        return
    
shapes = [circle(), rectangle()]
for shp in shapes:
    shp.draw()

#---------------------#

# Overridding a method named myMethod of Parent class

# define parent class
class Parent:
    def myMethod(self):
        print("Calling Parent method")

# define child class        
class Child(Parent):
    def myMethod(self):
        print("Calling Child method")

# instance of child
c = Child()
# child calls overridden method
c.myMethod()

#---------------------#

class Employee:
    def __init__(self, nm, sal):
        self.name = nm
        self.salary = sal
    
    def getName(self):
        return self.name
    
    def getSalary(self):
        return self.salary

class SalesOfficer(Employee):
    def __init__(self, nm, sal, inc):
        super().__init__(nm, sal)
        self.incnt = inc
    
    def getSalary(self):
        return self.salary+self.incnt

e1 = Employee("Rishav", 9000)
print(f"Total salary for {e1.getName()} is RS. {e1.getSalary()}")
s1 = SalesOfficer("Shrestha", 10000, 1000)
print(f"Total salary for {s1.getName()} is Rs {s1.getSalary()}")

#---------------------#