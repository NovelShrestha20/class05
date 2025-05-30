def add(*nums):
    return sum(nums)

# Call the function with different number of parameters
result1 = add(10 , 25)
result2 = add(10, 25, 35)

print(result1)
print(result2)

#---------------------#

class example:
    def add(self, a = None, b =  None, c = None):
        x = 0 
        if a != None and b != None and c != None:
            x = a + b + c
        elif a != None and b != None and c == None:
            x = a + b
        return x

obj = example()

print (obj.add(10,20,30))
print (obj.add(10,20))