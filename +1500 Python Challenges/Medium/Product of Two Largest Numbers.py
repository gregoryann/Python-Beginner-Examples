"""
Product of Two Largest Numbers

Create a function that takes a list and returns the product of the largest and second largest number.

Examples
product([2, 3, 1, -1, 2]) ➞ 6
# 2 * 3 = 6

product([-2, -2, -1, -1]) ➞ 2
# -2 * - 1 = 2
# Not 1, because you can only use -1 one time.

product([8, 8, 8]) ➞ 64
# 8 * 8 = 64
# You can repeat here because there is only one value.

product([2, 8, 8, 8]) ➞ 16
# 2 * 8 = 16
# Not 64, because you can only use 8 one time.

Notes
Numbers in the list are all integers.
Numbers can be both positive or negative.
"""



################################################################
"""
Solution 1
"""


def product(lst):
    x=[]
    a=list(set(lst))
    x.append(max(a))
    a.remove(max(a))
    if len(a)>=1:
        x.append(max(a))
        return x[0]*x[1]
    else:
        return x[0]**2



################################################################
"""
Solution 2
"""


def product(lst):
    lst_ = list(set(lst))
    
    if len(lst_) == 1:
        return lst_[0] * lst_[0] 
    
    else:
        lst_.sort()
        return lst_[-1] * lst_[-2]




################################################################
"""
Solution 3
"""


def product(lst):

	set_lst = set(lst)

	if len(set_lst) == 1:
		return max(set_lst) * max(set_lst)
	
	first_num = max(set_lst)
	set_lst.remove(first_num)
	second_num = max(set_lst)

	return first_num * second_num




#################################################################
"""
Solution 4
"""


def product(lst):
	a =	max(lst)
	while lst.count(a) > 0 and len(lst) != lst.count(a):
		lst = lst[:lst.index(a)] + lst[lst.index(a)+1:]  
	c = max(lst)
	return a*c



