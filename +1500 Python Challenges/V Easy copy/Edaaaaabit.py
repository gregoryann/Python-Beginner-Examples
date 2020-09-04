"""
Edaaaaabit
Write a function that takes an integer and returns a string with the given number of "a"s in Edabit.

Examples
how_many_times(5) ➞ "Edaaaaabit"

how_many_times(0) ➞ "Edbit"

how_many_times(12) ➞ "Edaaaaaaaaaaaabit"
Notes
The string must start with "Ed" and end with "bit".
You'll only be given integers as test input.

"""






"""
Solution 1
"""

def how_many_times(num):
    return "Ed{}bit".format("a" * num)

"""
Solution 2
"""

def how_many_times(num):
		return "Ed" + (num * "a") + "bit"

"""
Solution 3
"""

def how_many_times(num):
	middle = ""
	for i in range(num):
		middle = middle + "a"
	edabit = "Ed" + middle + "bit"
	return edabit



"""
Solution 4
"""


def how_many_times(num):
	string = ""
	for x in range(0, num):		
		string = string + "a"
	return("Ed"+string+"bit")


