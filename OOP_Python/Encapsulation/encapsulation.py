class BankAccount:
    def __init__(self, balance):
        self.__balance = balance # Private Attribute

    def deposit(self, amount):
        self.__balance += amount
    
    def get_balance(self):
        return self.__balance
# __balance is private and cannot be accessed directly


account = BankAccount(100)
account.deposit(50)
print(account.get_balance()) # Output: 150

class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age # Private Attribute
    
    # Getter method
    def get_age(self):
        return self.__age
    
    # Setter method
    def set_age(self, age):
        self.__age = age

stud = Student("Rishav", 24)

# Retrieving age using getter
print("Name: ", stud.name, stud.get_age())

# Changing age using setter
stud.set_age(25)

# Retrieving age using getter
print("Name: ", stud.name, stud.get_age())