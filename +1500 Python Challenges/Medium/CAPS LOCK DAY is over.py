"""
CAPS LOCK DAY is over!

October 22nd is CAPS LOCK DAY. Apart from that day, every sentence should be lowercase, so write a function to normalize a sentence.

Create a function that takes a string. If the string is all uppercase characters, convert it to lowercase and add an exclamation mark at the end.

Examples
normalize("CAPS LOCK DAY IS OVER") ➞ "Caps lock day is over!"

normalize("Today is not caps lock day.") ➞ "Today is not caps lock day."

normalize("Let us stay calm, no need to panic.") ➞ "Let us stay calm, no need to panic."

Notes
Each string is a sentence and should start with an uppercase character
"""




################################################################
"""
Solution 1
"""


def normalize(txt):
		return txt.capitalize() + ('!' if txt.isupper() else '')



################################################################
"""
Solution 2
"""


normalize=lambda t:t.capitalize()+'!'*t.isupper()


################################################################
"""
Solution 3
"""


def normalize(txt):
	if all(all(i.isupper() for i in x) for x in txt.split(' ')):
		return (txt.lower()).capitalize() + '!'
	return txt



#################################################################
"""
Solution 4
"""


def normalize(a):
	if a.isupper():
		return a.lower().capitalize() + '!'
	elif not a.isupper():
		return a.capitalize()



