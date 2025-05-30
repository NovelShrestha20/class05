class car:
    def __init__(self, speed=40):
        self._speed=speed
        return
    @property
    def speed(self):
        return self._speed
    @speed.setter
    def speed(self, speed):
        if speed<0 or speed>100:
            print ("speed limit 0 to 100")
            return
        self._speed=speed
        return

c1=car()
print (c1.speed) #calls getter
c1.speed=60 #calls setter