"""
Count Syllables
Create a function that counts the number of syllables a word has. Each syllable is separated with a dash -.

Examples
number_syllables("buf-fet") ➞ 2

number_syllables("beau-ti-ful") ➞ 3

number_syllables("mon-u-men-tal") ➞ 4

number_syllables("on-o-mat-o-poe-ia") ➞ 6
Notes
Don't forget to return the result.
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.

"""


"""
Solution 1
"""

def number_syllables(word):
	return len(word.split('-'))


"""
Solution 2
"""

# Count Syllables
def number_syllables(String):
    New_String = String.split("-")
    return len(New_String)
print(number_syllables("buf-fet"))
print(number_syllables("mon-u-men-tal"))


"""
Solution 3
"""

number_syllables = lambda word: word.count('-') + 1

"""
Solution 4
"""

def number_syllables(word):
	words2 = word.split("-")
	return len(words2)



def number_syllables(word):
	return sum([1 for i in word if i == '-']) + 1