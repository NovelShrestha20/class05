a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]
c = a

# Comapring and printing return values
print(a is c)
print(a is b)

# Printing IDs of a, b, and c
# id() provides the memory address
print("id(a) : ", id(a))
print("id(b) : ", id(b))
print("id(c) : ", id(c))