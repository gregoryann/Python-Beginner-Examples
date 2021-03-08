"""
Re-Form the Word
A word has been split into a left part and a right part. Re-form the word by adding both halves together, changing the first character to an uppercase letter.

Examples
get_word("seas", "onal") ➞ "Seasonal"

get_word("comp", "lete") ➞ "Complete"

get_word("lang", "uage") ➞ "Language"

"""




"""
Solution 1
"""

def get_word(left, right):
	return (left+right).capitalize()


"""
Solution 2
"""

def get_word(left, right):
	return left[0].upper() + left[1:] + right


"""
Solution 3
"""

def get_word(left, right):
	return '{0}{1}'.format(left, right).capitalize()
    
"""
Solution 4
"""

def get_word(left, right):
	word = left+right
	return word.title()





