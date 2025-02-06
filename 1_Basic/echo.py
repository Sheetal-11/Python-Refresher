# Take user input and print it

# to handle cases where the user enters an empty string, add a fallback:
name = input("Enter your name: ").strip() or "Stranger"
print(f"Hello, {name}!")

# Note:
# or "Stranger" is a fallback here.
# A fallback is a default value or action used when something goes wrong or is missing.
# Now, if the input is empty, it would print: Hello, Stranger!
# so the output will always be meaningful.