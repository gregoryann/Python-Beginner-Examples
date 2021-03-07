"""
Who's The Oldest?

Given a dictionary containing the names and ages of a group of people, return the name of the oldest person.

Examples
oldest({
  "Emma": 71,
  "Jack": 45,
  "Amy": 15,
  "Ben": 29
}) ➞ "Emma"

oldest({
  "Max": 9,
  "Josh": 13,
  "Sam": 48,
  "Anne": 33
}) ➞ "Sam"

Notes
All ages will be different.
"""





################################################################
"""
Solution 1
"""

def oldest(people):
	return max(people, key=people.get)






################################################################
"""
Solution 2
"""


def oldest(people):
	for k in people:
		if people[k] == max(people.values()):
			return k







################################################################
"""
Solution 3
"""


def oldest(people):
  return max(people.keys(), key=lambda x: people[x])







#################################################################
"""
Solution 4
"""


def oldest(people):
	v = list(people.values())
	k = list(people.keys())
	return k[v.index(max(v))]






#################################################################
"""
Solution 5
"""


def oldest(people):
	import operator
	return max(people.items(), key=operator.itemgetter(1))[0]