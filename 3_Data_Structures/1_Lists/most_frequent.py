# Find the Most Frequent Element

def count_dict(lst):
    """Returns a dictionary with key = element and value = element-count"""
    element_count = {}

    for num in lst:
        element_count[num] = element_count.get(num, 0) + 1  # Efficient counting

    # print(element_count)
    return element_count


def most_frequent(lst):
    """Returns the most frequent element in the list"""
    count = count_dict(lst)

    if not count:  # If the dictionary is empty, return early
        return "The list is empty. No most frequent element."

    max_count = 0
    max_key = None  # Initialize to None in case the list is empty

    for key, value in count.items():
        if value > max_count:
            max_count = value
            max_key = key

    return f"The most frequent element is {max_key}."


l = [3, 3, 5, 5, 5, 7, 7, 7, 7]
print(most_frequent(l))  # Output: The most frequent element is 7.

print(most_frequent([]))  # Output: The list is empty. No most frequent element.
