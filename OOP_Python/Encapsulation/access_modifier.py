class Employee:
    def __init__(self, name, age, salary):
        self.name = name        # public variable
        self._age = age        # private variable
        self.__salary = salary   # protected variable
    
    def displayEmployee(self):
        print(f"Name: {self.name} Age: {self.__age} Salary: {self._salary}")

e1 = Employee("Novel", 24, 10000)

print(e1.name)
print(e1._salary)
print(e1.__age)

# Python displays error because __age is private and not available for use outside of class