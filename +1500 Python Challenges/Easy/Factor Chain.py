"""
Factor Chain

A factor chain is a list where each previous element is a factor of the next consecutive element. The following is a factor chain:

[3, 6, 12, 36]

# 3 is a factor of 6
# 6 is a factor of 12
# 12 is a factor of 36
Create a function that determines whether or not a list is a factor chain.

Examples
factor_chain([1, 2, 4, 8, 16, 32]) ➞ True

factor_chain([1, 1, 1, 1, 1, 1]) ➞ True

factor_chain([2, 4, 6, 7, 12]) ➞ False

factor_chain([10, 1]) ➞ False
"""


"""
Solution 1
"""

def factor_chain(lst):
	for x in lst:
		if (lst[-1]%x != 0):
			return False
	return True


"""
Solution 2
"""

def factor_chain(lst):
	return all(lst[i] % lst[i-1] == 0 for i in range(1, len(lst)))


"""
Solution 3
"""

def factor_chain(lst):
    result = [lst[0]]
    for x in range(len(lst)-1):
        if lst[x+1] % lst[x] == 0:
            result.append(lst[x+1])
    return len(result) == len(lst)







