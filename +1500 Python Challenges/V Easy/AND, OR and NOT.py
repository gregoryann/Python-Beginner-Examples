"""
AND, OR and NOT
Continue to write the three logic gates: AND, OR and NOT.

Examples
AND(1, 1) ➞ 1
AND(0, 0) ➞ 0

OR(1, 0) ➞ 1
OR(1, 1) ➞ 1

NOT(0) ➞ 1
NOT(1) ➞ 0
Notes
Check the Resourses tab for some help.

"""





"""
Solution 1
"""

def how_many_times(num):
    return "Ed{}bit".format("a" * num)





"""
Solution 2
"""


NOT = lambda n:not n
AND = lambda a,b:a and b
OR = lambda a,b:a or b


"""
Solution 3
"""

def NOT(num):
	return 0 if num ==1 else 1
def AND(num,num2):
	return 0 if (num == 0 or num2 == 0) else 1
def OR(num,num2):
	return 1 if (num == 1 or num2 == 1) else 0



"""
Solution 4
"""


def NOT(num):
	if num == 1:
		return 0
	else:
		return 1
def AND(num,num2):
	if num == 1 and num2 == 1:
		return 1
	else:
		return 0
def OR(num,num2):
	if num == 0 and num2 == 0:
		return 0
	else:
		return 1


