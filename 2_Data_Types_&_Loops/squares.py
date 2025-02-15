# Generate a list of squares from 1 to n

num = int(input("Enter a positive number: "))

if num > 0:
    squares = [i ** 2 for i in range(1, num + 1)]
    print(squares)
else:
    print("Please enter a positive integer.")
