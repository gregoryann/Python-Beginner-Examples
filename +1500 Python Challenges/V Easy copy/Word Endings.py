"""
Word Endings
Create a function that adds a string ending to each member in a list.

Examples
add_ending(["clever", "meek", "hurried", "nice"], "ly")
➞ ["cleverly", "meekly", "hurriedly", "nicely"]

add_ending(["new", "pander", "scoop"], "er")
➞ ["newer", "panderer", "scooper"]

add_ending(["bend", "sharpen", "mean"], "ing")
➞ ["bending", "sharpening", "meaning"]
Notes
Don't forget to return the result.
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.

"""


"""
Solution 1
"""

def add_ending(lst, ending):
	return [ word + ending for word in lst]

"""
Solution 2
"""

add_ending=lambda l,e:[i+e for i in l]

"""
Solution 3
"""

def add_ending(lst, ending):
    new_lst = []
    for word in lst:
           new_lst.append(word + ending)
    return new_lst

"""
Solution 4
"""

def add_ending(lst, ending):
	for x in range(len(lst)):
		lst[x] = lst[x] + ending
	return lst


