# Find the sum of digits of a number

num = input("Please enter a number: ")

# num.lstrip('-')  :  to handle negative numbers
if num.lstrip('-').isdigit():
    digit_sum = 0
    for digit in num.lstrip('-'):
        digit_sum += int(digit)
    # digit_sum = sum(map(int, num))
    print(f"Sum of digits: {digit_sum}")

else:
    print("Please enter a valid number.")

