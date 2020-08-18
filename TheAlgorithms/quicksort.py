"""Implement quick sort in Python.
Input a list.
Output a sorted list."""


def quicksort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return quicksort(less) + equal + quicksort(greater)
    else:
        return array


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))


# https://stackoverflow.com/a/18262384/933941