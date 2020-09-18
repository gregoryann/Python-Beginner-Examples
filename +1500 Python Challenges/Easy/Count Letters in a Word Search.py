"""
Count Letters in a Word Search

Create a function that counts the number of times a particular letter shows up in the word search.

Examples
letter_counter([
  ["D", "E", "Y", "H", "A", "D"],
  ["C", "B", "Z", "Y", "J", "K"],
  ["D", "B", "C", "A", "M", "N"],
  ["F", "G", "G", "R", "S", "R"],
  ["V", "X", "H", "A", "S", "S"]
], "D") ➞ 3

# "D" shows up 3 times: twice in the first row, once in the third row.

letter_counter([
  ["D", "E", "Y", "H", "A", "D"],
  ["C", "B", "Z", "Y", "J", "K"],
  ["D", "B", "C", "A", "M", "N"],
  ["F", "G", "G", "R", "S", "R"],
  ["V", "X", "H", "A", "S", "S"]
], "H") ➞ 2

Notes
You will always be given a list with five sub-lists.
"""



"""
Solution 1
"""

def letter_counter(lst, letter):
	return str(lst).count(letter)

"""
Solution 2
"""

def letter_counter(lst, letter):
	return sum([x.count(letter) for x in lst])

"""
Solution 3
"""

def letter_counter(lst, letter):
	count = 0
	for x in lst:
		count += x.count(letter)
	return count

"""
Solution 4
"""

def letter_counter(lst, letter):
	return sum(sum(1 for i in j if i==letter) for j in lst)

"""
Solution 5
"""

letter_counter = lambda a,b:sum(x.count(b) for x in a)

"""
Solution 6
"""

def letter_counter(lst, letter):
	a = ''.join(str(r) for v in lst for r in v)
	return a.count(letter)