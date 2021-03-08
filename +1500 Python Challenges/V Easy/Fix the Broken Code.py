"""
Fix the Broken Code

A student learning Python was trying to make a function that sorts all the letters of a string, but their code is broken, and they can't figure out why.

Spot and fix the error(s) in the code to make the function work. As an added challenge for those who are more advanced, see if you can shrink (the fixed version of) the student's code down to only a single line.

Examples
sort_word("dcba") ➞ "abcd"

sort_word("Unpredictable") ➞ "Uabcdeeilnprt"
# Capital letters should come first.

sort_word("pneumonoultramicroscopicsilicovolcanoconiosis") ➞ "aacccccceiiiiiilllmmnnnnooooooooopprrsssstuuv"

Notes
If you're trying to get a function definition into a single line, try assigning a variable to a lambda function.
"""


"""
Solution 1
"""

def sort_word(word):
	return ''.join(sorted(list(word)))

"""
Solution 2
"""

def sort_word(word):
	word = list(word)
	word.sort()
	final_word = ''
	
	for char in word:
		final_word = final_word + char
	
	return final_word
	
sort_word('dcba')

"""
Solution 3
"""

def sort_word(word):
	return "".join(sorted(c for c in word if c.isupper()))+"".join(sorted(c for c in word if c.islower()))

"""
Solution 4
"""

sort_word = lambda w: ''.join(sorted(w))




