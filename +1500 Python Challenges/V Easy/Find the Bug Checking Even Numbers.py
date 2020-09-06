"""
Find the Bug: Checking Even Numbers
Create a function that takes in an array and returns True if all its values are even, and False otherwise.

Not a big deal, your friend says. He writes the following code:

def check_all_even(lst):
  return all(x % 2 == 0)
The code above leads to a Reference Error, with x being undefined. Fix the code above so that all tests pass:

Examples
check_all_even([1, 2, 3, 4]) ➞ False
check_all_even([2, 4, 6]) ➞ True
check_all_even([5, 6, 8, 10]) ➞ False
check_all_even([-2, 2, -2, 2]) ➞ True

Notes
For help, check Resources or ask a question in the Comments.

"""



"""
Solution 1
"""

def check_all_even(lst):
  return all(x % 2 == 0 for x in lst)


"""
Solution 2
"""

def check_all_even(lst):
	t = []
	for i in lst:
		if i % 2 == 0:
			t.append(i)
	return len(t) == len(lst)

"""
Solution 3
"""

def check_all_even(lst):
  return len([x for x in lst if x % 2 == 0]) == len(lst)





