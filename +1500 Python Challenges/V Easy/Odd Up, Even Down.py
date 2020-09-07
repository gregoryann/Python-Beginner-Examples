"""
Odd Up, Even Down

Create a function that goes through the array, incrementing (+1) for each odd number and decrementing (-1) for each even number.

Examples

transform([1, 2, 3, 4, 5]) ➞ [2, 1, 4, 3, 6]
transform([3, 3, 4, 3]) ➞ [4, 4, 3, 4]
transform([2, 2, 0, 8, 10]) ➞ [1, 1, -1, 7, 9]

"""


"""
Solution 1
"""

def transform(lst):
	return [n+1 if n%2==1 else n-1 for n in lst]

"""
Solution 2
"""

def transform(lst):
    new_lst = []
    for i in lst:
        if i % 2 == 0:
            new_lst.append(i - 1)
        else:
            new_lst.append(i + 1)
    return new_lst

"""
Solution 3
"""

transform = lambda l: [n+1 if n % 2 else n-1 for n in l]

"""
Solution 4
"""

def transform(lst):
	new_list = []
	for num in lst:
		if num % 2 == 0:
			new_list.append(num - 1)
		else:
			new_list.append(num + 1)
	return new_list




