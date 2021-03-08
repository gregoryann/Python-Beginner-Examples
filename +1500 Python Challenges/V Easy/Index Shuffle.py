"""
Index Shuffle

Write a function that takes all even-indexed characters and odd-indexed characters from a string and concatenates them together.

To illustrate:

index_shuffle("abcd") ➞ "acbd"
// "ac" (even-indexed) + "bd" (odd-indexed)
Examples
index_shuffle("abcdefg") ➞ "acegbdf"

index_shuffle("holiday") ➞ "hldyoia"

index_shuffle("maybe") ➞ "myeab"

Notes
0 should be treated as an even number.

"""


"""
Solution 1
"""

def index_shuffle(txt):
	return txt[::2] + txt[1::2]


"""
Solution 2
"""

def index_shuffle(txt):
	even = ''.join(i for i in txt[::2])
	odd = ''.join(i for i in txt[1::2])
	return even+odd

"""
Solution 3
"""

def index_shuffle(txt):
	charlist=list(txt)
	return "".join(charlist[::2])+"".join(charlist[1::2])

"""
Solution 4
"""

def index_shuffle(txt):
	return "".join([txt[i] for i in range(len(txt)) if i % 2 == 0]) + "".join([txt[i] for i in range(len(txt)) if i % 2 == 1])




