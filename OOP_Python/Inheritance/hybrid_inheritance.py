# Base class
class Animal:
    def speak(self):
        print("Animal makes a sound")

# Derived class (Multi-level inheritance)
class Mammal(Animal):
    def walk(self):
        print("Mammal walks on land")

# Another class (Base class for multiple inheritance)
class Bird(Animal):
    def fly(self):
        print("Bird flies in the sky")

# Hybrid inheritance: Combining Mammal and Bird classes into one
class Bat(Mammal, Bird):
    def hang(self):
        print("Bat hangs upside down")

# Creating an instance of Bat class
bat = Bat()

# Calling methods from different parent classes
bat.speak()   # Inherited from Animal class
bat.walk()    # Inherited from Mammal class
bat.fly()     # Inherited from Bird class
bat.hang()    # Defined in Bat class