"""

Concatenate First and Last Name into One String
Given two strings, first_name and last_name, return a single string in the format "last, first".

Examples
concat_name("First", "Last") ➞ "Last, First"

concat_name("John", "Doe") ➞ "Doe, John"

concat_name("Mary", "Jane") ➞ "Jane, Mary"
Notes
Don't forget to return the result.
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.


"""


#############################################################
#                        MY SOLUTIONS                       #
#############################################################




"""
Solution 1
"""


def concat_name(first_name, last_name):
	return last_name + ', ' + first_name




"""
Solution 2
"""

def concat_name(first_name, last_name):
	return "{0}, {1}".format(last_name, first_name)



"""
Solution 3
"""


def concat_name(first_name, last_name):
	return last_name + ", " + first_name


"""
Solution 4
"""


def concat_name(first_name, last_name):
	full_name = last_name + ", " + first_name
	return full_name





def concat_name(first_name, last_name):
	result_str=last_name + ', ' + first_name
	return(result_str)