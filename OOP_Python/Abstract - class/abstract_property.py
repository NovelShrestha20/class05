from abc import ABC, abstractmethod

class Animal(ABC):
    @property
    @abstractmethod
    def sound(self):
        pass

class Bird(Animal):
    @property
    def sound(self):
        return "Chirp"

bird = Bird()
print(bird.sound)