# Swap two numbers without using a third variable

# There are three ways to swap two numbers without using a third variable.

# Method 1️⃣: Using Arithmetic Operations (Addition & Subtraction)
a = 5
b = 10

a = a + b  # a becoming 15 (5+10=15)
b = a - b  # b becomes 5 (original value of a) (15-10=5)
a = a - b  # a becomes 10 (original value of b) (15-5=10)

print("After swapping: a =", a, ", b =", b)


# Method 2️⃣: Using XOR Bitwise Operator
a = 5
b = 10

a = a ^ b  # Step 1: XOR (a and b)
b = a ^ b  # Step 2: XOR (updated a and original b)
a = a ^ b  # Step 3: XOR (updated a and updated b)

print("After swapping: a =", a, ", b =", b)
# 💡 XOR swapping is an efficient way to swap values without using extra space or arithmetic operations.


# Method 3️⃣: Using Python’s Tuple Unpacking (Best & Easiest Way)
a = 5
b = 10

a, b = b, a  # Swapping in one line

print("After swapping: a =", a, ", b =", b)


