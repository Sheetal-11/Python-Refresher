# Reverse a string manually (without slicing)

def reverse_string_manually(s: str) -> str:
    """
    Reverses a given string manually (without slicing).
    """
    # return "".join(reversed(s))  # More efficient than manual method

    reversed_string = ""

    for char in s:
        reversed_string = char + reversed_string  # Adding character at the beginning

    return reversed_string


# Example usage
original_string = "Hello"
print(reverse_string_manually(original_string))  # Output: "olleH"
