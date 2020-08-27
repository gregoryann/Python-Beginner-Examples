"""
The Full Length of a Google
Google's logo can be stretched depending on how many pages it lets you skip forward to.

Image of Goooooooooogle

Let's say we wanted to change the number of pages that Google could skip to. Create a function where given a number of pages n, return the word "Google" but with the correct number of "o"s.

Examples
googlify(10) ➞ "Goooooooooogle"

googlify(23) ➞ "Gooooooooooooooooooooooooogle"

googlify(2) ➞ "Google"

googlify(-2) ➞ "invalid"
Notes
If n is equal to or less than 1, return invalid.

"""



"""
Solution 1
"""

def googlify(n):
	return 'G{}gle'.format('o' * n) if n > 1 else 'invalid'

"""
Solution 2
"""

def googlify(n):
  if n < 2:
	  return "invalid"
  else:
	  return "G" + "o" * n + "gle"

"""
Solution 3
"""

def googlify(n):
	return 'G{}gle'.format('o'*n) if n > 1 else 'invalid'

"""
Solution 4
"""

def googlify(n):
	if n <= 1:
		return 'invalid'
	else:
		return "G" + ("o" * n) + "gle"

"""
Solution 5
"""


def googlify(n):
	return "invalid" if n<=1 else "Goo{}gle".format("o"*int(n-2))

