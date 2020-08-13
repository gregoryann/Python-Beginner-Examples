"""


Convert Number to String of Dashes
Create a function that takes a number (from 1 - 60) and returns a corresponding string of hyphens.

Examples
num_to_dashes(1) ➞ "-"

num_to_dashes(5) ➞ "-----"

num_to_dashes(3) ➞ "---"
Notes
You will be provided integers ranging from 1 to 60.
Don't forget to return your result as a string.
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.

"""






"""
Solution 1
"""


def num_to_dashes(num):
	return "-" * num




"""
Solution 2
"""

def num_to_dashes(num):
	dashes = ''
	counter = 0
	while counter < num:
		dashes += '-'
		counter += 1
	return dashes



"""
Solution 3
"""

def num_to_dashes(num):
	output = ''
	output = num * '-'
	return output



"""
Solution 4
"""




def num_to_dashes(num):
  x = '-'
  return num * x

