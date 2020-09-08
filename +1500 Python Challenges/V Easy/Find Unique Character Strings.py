"""
Find Unique Character Strings

Create a function that returns only strings with unique characters.

Examples

filter_unique(["abb", "abc", "abcdb", "aea", "bbb"]) ➞ ["abc"]
# "b" occurs in "abb" more than once, "b" occurs in "abcdb" more than once, etc.
filter_unique(["88", "999", "989", "9988", "9898"]) ➞ []
filter_unique(["ABCDE", "DDEB", "BED", "CCA", "BAC"]) ➞ ["ABCDE", "BED", "BAC"]

"""

"""
Solution 1
"""

def filter_unique(lst):
	return [x for x in lst if len(x)==len(set(x))]

"""
Solution 2
"""

def filter_unique(lst):
	new_lst = []
	
	for string in lst:
		if len(set(string)) == len(string):
			new_lst.append(string)
			
	return new_lst

"""
Solution 3
"""

def filter_unique(lst):
	return [i for i in lst if check(i)]
	
def check(string):
	s=set([i for i in string])
	return len(s)==len(string)

"""
Solution 4
"""
def filter_unique(lst):
	return [i for i in lst	if ''.join(sorted(set(i))) == ''.join(sorted(i))]





