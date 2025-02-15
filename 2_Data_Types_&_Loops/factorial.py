# Find the factorial of a number using a loop

num = int(input("Please enter a number: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    factorial_n = 1
    for i in range(1, num + 1):
        factorial_n *= i

    print(f"Factorial of {num} = {factorial_n}")
