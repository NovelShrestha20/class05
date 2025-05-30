names = ["Rishav", "Ram", "Sri", "Om", "Harry", "Potter"]
print("Given List:")
print(names)

new_names = []

for i in names:
    if len(i) > 3:
        new_names.append(i)
    else:
        print(f"Removing {i} as <= 3 letters.")

print("Updated List:")
print(new_names)