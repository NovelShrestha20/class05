# Enclosed Scope: non local variable
def yourfunction():
    a = 5
    b = 6
    #nested funtion
    def myfunction():
        # non local function
        nonlocal a
        nonlocal b
        a = 10
        b = 20
        print(f"Variable a: {a}")
        print(f"Variable b: {b}")
        return a + b
    print(myfunction())
yourfunction()