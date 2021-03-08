"""
Orthogonal Vector

Create a function that takes two vectors as lists and checks if the two vectors are orthogonal or not. The return value is boolean. Two vectors first and second are orthogonal if their dot product is equal to zero.

Examples
is_orthogonal([1, 2], [2, -1]) ➞ True

is_orthogonal([3, -1], [7, 5]) ➞ False

is_orthogonal([1, 2, 0], [2, -1, 10]) ➞ True

Notes
The two lists are of same length.
Check out the Resource tab.
"""


#############################################################
#                        MY SOLUTIONS                       #
#############################################################





"""
Solution 1
"""

def is_orthogonal(A, B):
	return not sum(x*y for x, y in zip(A,B))

"""
Solution 2
"""

is_orthogonal=lambda a,b:sum(x*y for x,y in zip(a,b))==0

"""
Solution 3
"""

def is_orthogonal(first, second):
    a=0
    for i in range(0,len(first)):
        a=a+first[i]*second[i]
    return (a==0)

"""
Solution 4
"""

def is_orthogonal(first, second):
	i = 0
	list = []
	for x in first:
		list.append(first[i]*second[i])
		i += 1
	return sum(list) == 0




