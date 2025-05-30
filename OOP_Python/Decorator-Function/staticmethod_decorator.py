class counter:
    count=0
    def __init__(self):
        print ("init called by ", self)
        counter.count=counter.count+1
        print ("count=",counter.count)
    @staticmethod
    def showcount():
        print ("count=",counter.count)

c1=counter()
c2=counter()
print ("class method called by object")
c1.showcount()
print ("class method called by class")
counter.showcount()