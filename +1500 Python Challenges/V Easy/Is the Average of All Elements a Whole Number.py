"""
Is the Average of All Elements a Whole Number?

Create a function that takes a list as an argument and returns True or False depending on whether the average of all elements in the list is a whole number or not.

Examples
is_avg_whole([1, 3]) ➞ True

is_avg_whole([1, 2, 3, 4]) ➞ False

is_avg_whole([1, 5, 6]) ➞ True

is_avg_whole([1, 1, 1]) ➞ True

is_avg_whole([9, 2, 2, 5]) ➞ False

"""


"""
Solution 1
"""

def is_avg_whole(arr):
	return sum(arr) % len(arr) == 0

"""
Solution 2
"""

def is_avg_whole(arr):
	return statistics.mean(arr) == int(statistics.mean(arr))

"""
Solution 3
"""

def is_avg_whole(arr):
	avg = sum(arr) / len(arr)
	return avg.is_integer()


"""
Solution 4
"""

def is_avg_whole(arr):


    avg = sum(arr) / len(arr)

    if round(avg, 1) == round(avg,0):

        return True

    else:

        return False

