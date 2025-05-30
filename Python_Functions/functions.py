### Lambda Functions ###
square = lambda x: x * x
print(square(4))  # Output: 16

# Lambda with Condition Checking
# Eg: Check if a number is positive, negetive or zero
n = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"

print(n(5))
print(n(-3))
print(n(0))

# Filter even numbers from a list
n = [1, 2, 3, 4, 5, 6]
even = filter(lambda x: x % 2 == 0, n)
print(list(even))

# Double each number in list
a = [1, 2, 3, 4]
b = map(lambda x: x * 2, a)
print(list(b))


### Recursive Function ###
# Find the factorial of a number given by the user.
def factorial(n):
    if n < 0:
        print("Negative numbers not allowed.")
    else:    
        if n == 1 or n == 0:
            return 1
        else:
            return n * factorial(n-1)

n = int(input("Enter the number: "))
print(factorial(n))