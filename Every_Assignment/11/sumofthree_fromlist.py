# List of numbers
array = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]
list_length = len(array)   # Finding lenght of list

# To check if sum does exist
# If it doesnt exist we can use False value to print it doesnt exist
found = False

# Iterate through all combinations of three numbers
for a in range(list_length): # First iteration for 1st number
    for b in range(a + 1, list_length): # Second iteration for 2nd number
        for c in range(b + 1, list_length): # Third iteration for 3rd number
            # Check if the sum of three numbers is zero
            if array[a] + array[b] + array[c] == 0:
                print(f"Found: {array[a]}, {array[b]}, {array[c]} sum to 0")
                found = True

# Print no combination results to zero
if not found:
    print("No Three numbers sums to 0.")