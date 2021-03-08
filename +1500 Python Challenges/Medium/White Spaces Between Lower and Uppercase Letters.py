"""
White Spaces Between Lower and Uppercase Letters

Write a function that inserts a white space between every instance of a lower character followed immediately by an upper character.

Examples
insert_whitespace("SheWalksToTheBeach") ➞ "She Walks To The Beach"

insert_whitespace("MarvinTalksTooMuch") ➞ "Marvin Talks Too Much"

insert_whitespace("TheGreatestUpsetInHistory") ➞ "The Greatest Upset In History"


Notes
Each word in the phrase will be at least two characters long.
"""



################################################################
"""
Solution 1
"""


def insert_whitespace(txt):
	return ''.join([' '+x if x == x.upper() else x for x in txt])[1:]



################################################################
"""
Solution 2
"""


import re

def insert_whitespace(txt):
	return re.sub(r'([a-z])(?=[A-Z])', r'\1 ', txt)



################################################################
"""
Solution 3
"""


import re
insert_whitespace=lambda t:re.sub(r'([a-z])([A-Z])',r'\1 \2',t)



#################################################################
"""
Solution 4
"""


import re
def insert_whitespace(txt):
	txt = re.findall('[\D][^A-Z]*',txt)
	return ' '.join(txt)



