"""
Find the Unique Letters
Create a function that takes a string and returns the letters that occur only once.

Examples
find_letters("monopoly") ➞ ["m", "n", "p", "l", "y"]

find_letters("balloon") ➞ ["b", "a", "n"]

find_letters("analysis") ➞ ["n", "l", "y", "i"]
Notes
The final list should not include letters that appear more than once in the string.
Return the letters in the sequence they were originally in, do not sort them.
All letters will be in lowercase.

"""



"""
Solution 1
"""

def find_letters(word):
    return [ch for ch in word if word.count(ch)==1]


"""
Solution 2
"""

find_letters = lambda word: [ch for ch in word if word.count(ch) == 1]


"""
Solution 3
"""

def find_letters(word):
	word_list = [i for i in word if word.count(i) == 1]
	return word_list

"""
Solution 4
"""

def find_letters(word):
	l = []
	for i in word:
		if word.count(i) == 1 and i not in l:
			l.append(i)
	return l



def find_letters(word):
    return [x for x in word if word.count(x)==1]
