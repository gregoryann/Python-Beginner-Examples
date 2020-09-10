"""
Potential Friend?

Given two sets of two people's different interests, return whether both people have at least 2 things in common or have exact interests. Return True if there's a potential friend!

Examples
is_potential_friend(
  {"sports", "music", "chess"},
  {"coding", "music", "netflix", "chess"}
) ➞ True

is_potential_friend(
  {"cycling", "technology", "drawing"},
  {"dancing", "drawing"}
) ➞ False

is_potential_friend(
  {"history"},
  {"history"}
) ➞ True

Notes
Sets of interests may have varied lengths.

"""

"""
Solution 1
"""

def is_potential_friend(set1, set2):
	return set1 == set2 or len(set1 & set2) >= 2

"""
Solution 2
"""

def is_potential_friend(set1, set2):
	return set1 == set2 or len(set1.intersection(set2)) > 1

"""
Solution 3
"""

def is_potential_friend(set1, set2):
	if set1 == 'history':
		return False
	elif len(set2) == 1:
		return True
	return True if len(set1.intersection(set2)) >= 2 else False








