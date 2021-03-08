"""
Hashes and Pluses
Create a function that returns the number of hashes and pluses in a string.

Examples
hash_plus_count("###+") ➞ [3, 1]

hash_plus_count("##+++#") ➞ [3, 3]

hash_plus_count("#+++#+#++#") ➞ [4, 6]

hash_plus_count("") ➞ [0, 0]
Notes
Return [0, 0] for an empty string.
Return in the order of [hashes, pluses].

"""






"""
Solution 1
"""

def hash_plus_count(txt): 
	return [txt.count('#'), txt.count('+')]


"""
Solution 2
"""

def hash_plus_count(txt):
	return [txt.count(i) for i in "#+"]

"""
Solution 3
"""

hash_plus_count=lambda txt:[txt.count("#"), txt.count("+")]

"""
Solution 4
"""

def hash_plus_count(txt):
	hash = 0
	plus = 0

	for i in txt:
		if i == '#':
			hash += 1
		else:
			plus += 1
	
	return [hash, plus]


