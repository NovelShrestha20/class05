rows = 7
cols = 5

for i in range(rows):
    for j in range(cols):
        if j == 0 or j == cols - 1 or j == int(i * (cols - 1) / (rows - 1)):
            print("*", end="")
        else:
            print(" ", end="")
    print()