# Local Scope
def myfunction():
    a = 10
    b = 20
    print("Variable a:", a)
    print(f"Variable b: {b}")
    return a + b

print(myfunction())