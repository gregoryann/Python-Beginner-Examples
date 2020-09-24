"""
Pythagorean Triplet
Create a function that validates whether three given integers form a Pythagorean triplet. The sum of the squares of the two smallest integers must equal the square of the largest number to be validated.

Examples
is_triplet(3, 4, 5) ➞ True
# 3² + 4² = 25
# 5² = 25

is_triplet(13, 5, 12) ➞ True
# 5² + 12² = 169
# 13² = 169

is_triplet(1, 2, 3) ➞ False
# 1² + 2² = 5
# 3² = 9

Notes
Numbers may not be given in a sorted order.
"""


"""
Solution 1
"""

def is_triplet(*n):
    a, b, c = sorted(n)
    return a*a + b*b == c*c

"""
Solution 2
"""

def is_triplet(n1, n2, n3):
	l = sorted([n1,n2,n3])
	return l[0]**2 + l[1]**2 == l[2]**2

"""
Solution 3
"""

def is_triplet(n1, n2, n3):
    lst = [n1, n2, n3]
    maxi = max(lst)
    mini = min(lst)
    lst.remove(maxi)
    lst.remove(mini)
    return maxi ** 2 == (mini ** 2) + (lst[0] ** 2)

"""
Solution 4
"""

def is_triplet(n1, n2, n3):
	new=[]
	new.append(n1)
	new.append(n2)
	new.append(n3)
	new.sort()
	return new[0]**2+new[1]**2==new[2]**2




