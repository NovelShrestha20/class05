# Base Class
class Animal:
    def __init__(self, species):
        self.species = species
    def speak(self):
        return f"{self.species} makes a sound."
    
# Derived Class 1
class Dog(Animal):
    def __init__(self, name):
        super().__init__("Dog")         # Initialise with base class
        self.name = name
    def bark(self):
        return f"{self.species} says WOOOF!."
    
# Derived Class 2
class Cat(Animal):
    def __init__(self, name):
        super().__init__("Cat")         # Initialise with base class
        self.name = name
    def meow(self):
        return f"{self.species} says MEOWW!."
    
# Creating instances of derived classes.
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Calling methods from base class and derived classes
print(dog.speak())
print(dog.bark())
print(cat.speak())
print(cat.meow())