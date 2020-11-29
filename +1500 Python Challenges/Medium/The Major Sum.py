"""
The Major Sum

Create a function that takes an integer list and return the biggest between positive sum, negative sum, or 0s count. The major is understood as the greatest absolute.

l = [1,2,3,4,0,0,-3,-2], the function has to return 10, because:

Positive sum = 1+2+3+4 = 10
Negative sum = (-3)+(-2) = -5
0s count = 2 (there are two zeros in list)
Examples
major_sum([1, 2, 3, 4, 0, 0, -3, -2]) ➞ 10

major_sum([-4, -8, -12, -3, 4, 7, 1, 3, 0, 0, 0, 0]) ➞ -27

major_sum([0, 0, 0, 0, 0, 1, 2, -3]) ➞ 5
# Because -3 < 1+2 < 0sCount = 5


Notes
All numbers are integers.
There aren't empty lists.
All tests are made to return only one value.
"""



################################################################
"""
Solution 1
"""


def major_sum(lst):
	p = sum(n for n in lst if n > 0)
	n = sum(n for n in lst if n < 0)
	z = lst.count(0)
	return n if -n > p and -n > z else max(p, z)


################################################################
"""
Solution 2
"""


def major_sum(lst):
    pos = sum([a for a in lst if a > 0])
    zeros = lst.count(0)
    neg = sum([a for a in lst if a < 0])
    return max(pos, zeros, neg,key=lambda x: abs(x))


################################################################
"""
Solution 3
"""


def major_sum(lst):
    new = []
    zero = lst.count(0)
    pos = sum(i for i in lst if i>0)
    neg = (sum(j for j in lst if j<0))
    new.append(zero)
    new.append(pos)
    new.append(neg)
    
    return neg if abs(neg) > zero and abs(neg) > pos else max(new)


#################################################################
"""
Solution 4
"""


def major_sum(lst):
	pos=sum([x for x in lst if x>0])
	neg=sum([x for x in lst if x<0])
	return sorted([pos,neg,lst.count(0)], key=abs)[-1]



