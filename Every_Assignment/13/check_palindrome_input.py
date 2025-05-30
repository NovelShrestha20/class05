word = input("Enter your word: ")
reverse = word[::-1]

if word == reverse:
    print("it is a palindrome word.")
else:
    print("it is not a palindrome")