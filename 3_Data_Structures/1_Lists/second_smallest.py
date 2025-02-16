# Find the Second-Smallest Number in a List

def second_smallest(lst):

    min1 = min2 = float('inf')

    for num in lst:

        # Keep track of the smallest number
        if num < min1:
            min2 = min1
            min1 = num

        # Keep track of the second-smallest number in case the num is between min1 and min2
        # Example when this elif gets triggered: [8, 4, 6]
        elif min2 > num > min1:
            min2 = num

    return f"The second-smallest number is {min2}." if min2 != float('inf') else f"There is no second-smallest number."


print(second_smallest([8, 4, 6, 2, 9]))  # Output: The second-smallest number is 4.
print(second_smallest([3, 3, 3]))       # Output: There is no second-smallest number.
print(second_smallest([7]))             # Output: There is no second-smallest number.


