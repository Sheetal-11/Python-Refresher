# Find the second-largest number in a list

# General case scenario: a list that contains 2+ elements
# Edge cases:
# I - the list contains no element
# II - the list contains only one element: in which case there is no second-largest number
# III - the list has all the elements the same

def second_largest(lst):

    max1 = max2 = float('-inf')  # Initialize both as negative infinity
    # float('-inf') ensures that any number in the list will be greater than this initial value.
    # Also, if the list has fewer than two unique numbers, second_largest remains -inf,
    # which helps handle cases where the second largest might not exist.

    for num in lst:

        # The if condition handles updates to largest.
        if num > max1:
            max2 = max1
            max1 = num

        # The elif condition ensures we correctly track the second largest in cases where num is between max1 and max2.
        # One example where it would get triggered: [5, 10, 7]
        elif max2 < num < max1:
            max2 = num

    return f"The second-largest number is {max2}." if max2 > float('-inf') else "There is no second-largest number."


print(second_largest([5, 9, 2, 6, 3]))  # Output: The second-largest number is 6.

print(second_largest([5, 10, 7]))       # Output: The second-largest number is 7.

# Edge case I - no element
print(second_largest([]))               # Output: There is no second-largest number.

# Edge case II - one element
print(second_largest([10]))             # Output: There is no second-largest number.

# Edge case III - same elements
print(second_largest([5, 5, 5]))        # Output: There is no second-largest number.
