this_set = {1, 2, 3, 4, 5}

check = int(input("Enter the number to check: "))
if check in this_set:
    position = list(this_set).index(check)
    print(f"Number exists in {position} index")
else:
    print(f"Number doesnt exist.")