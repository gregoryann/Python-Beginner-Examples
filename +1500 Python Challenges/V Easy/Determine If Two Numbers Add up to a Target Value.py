"""
Determine If Two Numbers Add up to a Target Value
Given two unique integer lists a and b, and an integer target value v, create a function to determine whether there is a pair of numbers that add up to the target value v, where one number comes from one list a and the other comes from the second list b.

Return True if there is a pair that adds up to the target value and False otherwise.

Examples
sum_of_two([1, 2], [4, 5, 6], 5) ➞ True

sum_of_two([1, 2], [4, 5, 6], 8) ➞ True

sum_of_two([1, 2], [4, 5, 6], 3) ➞ False

sum_of_two([1, 2], [4, 5, 6], 9) ➞ False
"""



"""
Solution 1
"""

def sum_of_two(a, b, v):
		return any(i+j == v for i in a for j in b)

"""
Solution 2
"""

sum_of_two=lambda a,b,v:any(x+y==v for x in a for y in b)

"""
Solution 3
"""

def sum_of_two(a, b, v):
    for i in a:
        for j in b:
            if i + j == v:
                return i + j == v
                break
            else:
                continue
    return False




