"""
Little Dictionary


Create a function that takes an initial word and filters out a list which contains words that start with the same letters as the initial word.

Examples
dictionary("bu", ["button", "breakfast", "border"]) ➞ ["button"]

dictionary("tri", ["triplet", "tries", "trip", "piano", "tree"]) ➞ ["triplet", "tries", trip"]

dictionary("beau", ["pastry", "delicious", "name", "boring"]) ➞ []


Notes
If none of the words match, return an empty list.
Keep the filtered list in the same relative order as the original list of words.
"""



"""
Solution 1
"""

def dictionary(initial, words):
	lst = []
	
	for word in words:
		if word.startswith(initial) == True:
			lst.append(word)
			
	return lst

"""
Solution 2
"""

def dictionary(initial, words):
	return [i for i in words if i[:len(initial)] == initial]

"""
Solution 3
"""

def dictionary(initial, words):
    return list(filter(lambda x : x[:len(initial)] == initial, words))

"""
Solution 4
"""

def dictionary(initial, words):
	result = []
	for i in words:
		if initial == i[:len(initial)]:
			result.append(i)
	return result



