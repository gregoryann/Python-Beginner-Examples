# Assume names is sorted
# Assume names is a list


def binary_search(to_find, names):
    # If the list is empty
    if len(names) == 0:
        return False
    # Cut our list in half, examine the midpoint item
    mid = len(names) // 2
    item = names[mid]
    # If the item is equal to to_find:
    if item == to_find:
        return True
    # Otherwise, if it's smaller
    elif item > to_find:
        return binary_search(to_find, names[:mid])
        # Repeat binary search on first half of the list
    # Otherwise
    else:
        return binary_search(to_find, names[mid+1:])
        # Repeat binary search on second half