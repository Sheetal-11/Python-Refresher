# Remove duplicates from a list

def remove_duplicates(lst):
    """
        Removes duplicate elements from a list while maintaining the original order.

    Args:
        lst (list): The input list containing duplicate elements.

    Returns:
        list: A new list with duplicates removed, preserving the original order.
    """
    # "num not in unique_items" check takes O(n) time for each element which has a time complexity of O(n²)
    # To improve the efficiency, I'm using a set, which allows O(1) lookups
    unique_items = []
    seen = set()

    for num in lst:
        if num not in seen:
            seen.add(num)
            unique_items.append(num)

    return unique_items

l = [2, 2, 3, 3, 3, 5, 7, 5, 8, 7, 8]
print(remove_duplicates(l))
