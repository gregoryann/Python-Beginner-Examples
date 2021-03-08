"""
List of Consecutive Numbers
Implement a function that returns a list containing all the consecutive numbers in ascendant order from the given value low up to the given value high (bounds included).

Examples
get_sequence(1, 5) ➞ [1, 2, 3, 4, 5]

get_sequence(98, 100) ➞ [98, 99, 100]

get_sequence(1000, 1000) ➞ [1000]
Notes
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.

"""



"""
Solution 1
"""

def get_sequence(low, high):
	return list(range(low,high+1))

"""
Solution 2
"""

def get_sequence(low, high):

    arr = []
    
    for number in range(low, high + 1):
        arr.append(number)

    return arr

"""
Solution 3
"""

def get_sequence(low, high):
	num_lst = []
	for num in range(low, high + 1):
		num_lst.append(num)
	return num_lst

"""
Solution 4
"""

def get_sequence(low, high):
	nums = []
	for x in range(low, high + 1):
		nums.append(x)
	return nums



