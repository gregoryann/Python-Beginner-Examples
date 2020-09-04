"""
Find the Falsehoods
Python will interpret empty values (e.g. 0, (), {}, [], "") as the boolean False. For example, the code "cat" if () else "dog" returns "dog", since () is False.

On the other hand, non-empty values are interpreted as True. For example, "cat" if (3, 2) else "dog" returns "cat" since (3, 2) is True.

Write a function that, given a list of values, returns the list of the values that are False.

Examples
find_the_falsehoods([0, 1, 2, 3]) ➞ [0]

find_the_falsehoods(["", "a", "ab"]) ➞ [""]

find_the_falsehoods([None, 1, [], [0], 0]) ➞ [None, [], 0]

find_the_falsehoods([]) ➞ []

find_the_falsehoods([[]]) ➞ [[]]

find_the_falsehoods([[[]]]) ➞ []

"""



"""
Solution 1
"""

def find_the_falsehoods(lst):
	return [e for e in lst if not e]

"""
Solution 2
"""

def find_the_falsehoods(lst):
	return [a for a in lst if bool(a)==False]

"""
Solution 3
"""

def find_the_falsehoods(lst):
	empty_lst = [x for x in lst if x == False or x == "" or x == None or x == [] or x == () or x == {}]
	return empty_lst

"""
Solution 4
"""
def find_the_falsehoods(lst):
	return list(filter(lambda x: not x,lst))





