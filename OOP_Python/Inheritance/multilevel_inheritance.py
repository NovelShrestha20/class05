# Base Class
class Animal:
    def __init__(self, species):
        self.species = species
    def eat(self):
        return f"{self.species} is eating."
    
# Derived class from Animal
class Mammal(Animal):
    def __init__(self, species, fur_color):
        super().__init__(species) # Initialise the base class
        self.fur_color = fur_color
    def breathe(self):
        return f"{self.species} is breathing air."
    
# Further derived class from Mammal
class Dog(Mammal):
    def __init__(self, species, fur_color, name):
        super().__init__(species, fur_color) # Initialise the base class (Mammal)
        self.name = name
    def bark(self):
        return f"{self.name} says Woooff!"
    
# Create an instance of the dog
my_dog = Dog("Dog", "Brown", "Buddy")

# Call methods from all levels of inheritance
print(my_dog.eat())
print(my_dog.breathe())
print(my_dog.bark())