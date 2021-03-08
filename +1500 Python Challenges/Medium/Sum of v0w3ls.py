"""
Sum of v0w3ls

Create a function that takes a string and returns the sum of vowels, where some vowels are considered numbers.

Vowel	Number
A	4
E	3
I	1
O	0
U	0
Examples
sum_of_vowels("Let\'s test this function.") ➞ 8

sum_of_vowels("Do I get the correct output?") ➞ 10

sum_of_vowels("I love edabit!") ➞ 12


Notes
Vowels are case-insensitive (e.g. A = 4 and a = 4).
"""



################################################################
"""
Solution 1
"""


def sum_of_vowels(sentence):
	v = {'a':4, 'e':3, 'i':1}
	return sum(v[ch] for ch in sentence.lower() if ch in v)



################################################################
"""
Solution 2
"""


def sum_of_vowels(sentence):
	txt = sentence.lower()
	return 4 * txt.count('a') + 3 * txt.count('e') + txt.count('i')



################################################################
"""
Solution 3
"""


sum_of_vowels=lambda s:sum({'a':4,'e':3,'i':1}.get(x,0)for x in s.lower())



#################################################################
"""
Solution 4
"""


def sum_of_vowels(sentence):
	point = {
    "A"	:4,
    "E"	:3,
    "I"	:1,
    "O"	:0,
    "U"	:0
	}
	result = 0
	for n in range(len(sentence)):
		if sentence[n] in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
			result += point.get(sentence[n].upper())
	return (result)



