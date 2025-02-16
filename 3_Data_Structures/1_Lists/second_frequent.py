# Find the Second-Most Frequent Element

def count_dict(lst):
    """Returns a dictionary with key = element and value = element-count"""
    element_count = {}

    for num in lst:
        element_count[num] = element_count.get(num, 0) + 1  # Efficient counting

    # print(element_count)
    return element_count


def second_most_frequent(lst):
    """Returns the second-most frequent element in the list"""
    count = count_dict(lst)

    if len(count) < 2:  # If the dictionary is empty, return early
        return "There is no second-most frequent element."

    max1 = max2 = 0
    max1_key = max2_key = None  # Track the keys

    for key, value in count.items():
        if value > max1:
            max2, max1 = max1, value
            max2_key, max1_key = max1_key, key
        elif max2 < value < max1:
            max2 = value
            max2_key = key

    return f"The second-most frequent element is {max2_key}."


l = [3, 3, 5, 5, 5, 7, 7, 7, 7]
print(second_most_frequent(l))  # Output: The second-most frequent element is 5.

print(second_most_frequent([]))  # Output: There is no second-most frequent element.

print(second_most_frequent([4, 4, 4, 4]))  # Output: There is no second-most frequent element.

print(second_most_frequent([1, 2, 3, 4, 5]))  # Any one of them can be second-most frequent.
