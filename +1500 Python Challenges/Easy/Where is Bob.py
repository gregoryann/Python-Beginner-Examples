"""
Where is Bob!?!

Write a function that searches a list of names (unsorted) for the name "Bob" and returns the location in the list. If Bob is not in the array, return -1.

Examples
find_bob(["Jimmy", "Layla", "Bob"]) ➞ 2

find_bob(["Bob", "Layla", "Kaitlyn", "Patricia"]) ➞ 0

find_bob(["Jimmy", "Layla", "James"]) ➞ -1

Notes
Assume all names start with a capital letter and are lowercase thereafter (i.e. don't worry about finding "BOB" or "bob").
"""





################################################################
"""
Solution 1
"""


def find_bob(names):
		return names.index('Bob') if 'Bob' in names else -1




################################################################
"""
Solution 2
"""


def find_bob(names):
	for index, name in enumerate(names):
		if name == 'Bob':
			return index
	return -1





################################################################
"""
Solution 3
"""

def find_bob(names):
 try:
  bob = list.index(names , "Bob")
  return bob
 except:
  return -1






#################################################################
"""
Solution 4
"""

def find_bob(names):
	if names.count('Bob') == 0:
		return -1
	else:
		return names.index('Bob')




