# DUCK TYPING

class Duck:
    def sound(self):
        return "Quack Quack!"

class AnotherBird:
    def sound(self):
        return "I'm similar to a duck"
    

def makeSound(duck):
    print(duck.sound())

# Creating Instances
duck = Duck()
anotherBird = AnotherBird()

# Calling Method
makeSound(duck)
makeSound(anotherBird)

# Even though Duck and AnotherBird are different classes,
# they both respond to sound().