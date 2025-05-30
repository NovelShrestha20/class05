class Car:                      # Class
    def __init__(self, color, model):
        self.color = color      # Attribute
        self.model = model      # Attribute
    
    def honk(self):             # Method
        print("BEEP BEEEP!")

# Creating an object
my_car = Car("Red", "Toyota")   # Object
my_car.honk() 
# Output: BEEP BEEEP!