"""
Sort a List by String Length

Create a function that takes a list of strings and return a list, sorted from shortest to longest.

Examples
sort_by_length(["Google", "Apple", "Microsoft"])
➞ ["Apple", "Google", "Microsoft"]

sort_by_length(["Leonardo", "Michelangelo", "Raphael", "Donatello"])
➞ ["Raphael", "Leonardo", "Donatello", "Michelangelo"]

sort_by_length(["Turing", "Einstein", "Jung"])
➞ ["Jung", "Turing", "Einstein"]

Notes
All test cases contain lists with strings of different lengths, so you won't have to deal with multiple strings of the same length.
"""



"""
Solution 1
"""

def sort_by_length(lst):
	return sorted(lst, key=len)

"""
Solution 2
"""

def sort_by_length(lst):
	dic = {}
	for item in lst:
		dic.update({len(item):item})
		
	return [dic[i] for i in sorted(dic.keys())]

"""
Solution 3
"""

def sort_by_length(lst):
	new = lst
	new.sort(key=len)
	return new







