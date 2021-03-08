"""
Count the Syllables
Create a function that returns the number of syllables in a simple string. The string is made up of short repeated words like "Lalalalalalala" (which would have 7 syllables).

Examples
count_syllables("Hehehehehehe") ➞ 6

count_syllables("bobobobobobobobo") ➞ 8

count_syllables("NANANA") ➞ 3
Notes
For simplicity, please note that each syllable will consist of two letters only.
Your code should accept strings of any case (upper, lower and mixed case).

"""



"""
Solution 1
"""

def count_syllables(txt):
	return sum(1 for i in txt.lower() if i in 'aeiou')

"""
Solution 2
"""

def count_syllables(txt):
	syllables = ['a', 'e', 'i', 'o', 'u']
	counter = 0
	
	for char in txt.lower():
		if char in syllables:
			counter += 1
			
	return counter

"""
Solution 3
"""

def count_syllables(txt):
	txt = txt.lower()
	return txt.count(txt[:2])

"""
Solution 4
"""
count_syllables=lambda txt: len(txt)/2





