# Find the maximum of three numbers

def max_of_three(num1: int, num2: int, num3: int) -> int:
    """
    Returns the maximum of three numbers.

    Parameters:
    num1 (int): First number
    num2 (int): Second number
    num3 (int): Third number

    Returns:
    int: The largest number among the three
    """
    return max(num1, num2, num3)

print( max_of_three(5, 7, 2) )
