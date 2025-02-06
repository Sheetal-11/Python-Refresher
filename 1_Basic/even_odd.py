# Check if a number is even or odd

try:
    num = int(input('Enter a number: '))

    if num % 2 == 0:
        print(f"{num} is an even number.")
    else:
        print(f"{num} is an odd number.")

except ValueError:
    print("Invalid input! Please enter a valid integer.")
