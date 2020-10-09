"""
Replace Vowel With Another Character

Create a function that takes a string and replaces the vowels with another character.

a = 1
e = 2
i = 3
o = 4
u = 5
Examples
replace_vowel("karachi") ➞ "k1r1ch3"

replace_vowel("chembur") ➞ "ch2mb5r"

replace_vowel("khandbari") ➞ "kh1ndb1ri"

Notes
The input will always be in lowercase.
"""





################################################################
"""
Solution 1
"""

def replace_vowel(word):
	return word.translate(str.maketrans('aeiou', '12345'))




################################################################
"""
Solution 2
"""

def replace_vowel(word):
	v = {'a': '1', 'e': '2', 'i': '3', 'o': '4', 'u': '5'}
	return "".join([i if i not in v else v[i] for i in word])







################################################################
"""
Solution 3
"""

replace_vowel=lambda w:w.translate(w.maketrans('aeiou','12345'))






#################################################################
"""
Solution 4
"""


def replace_vowel(word):
    new_word = ""
    vowels = {"a": 1, "e": 2, "i": 3, "o": 4, "u": 5}
    for i in word:
        if i in vowels:
            new_word = new_word + str(vowels.get(i, 0))
        else:
            new_word = new_word + i
    return new_word





#################################################################
"""
Solution 5
"""


def replace_vowel(word):
	d = {'a' : 1, 'e' : 2, 'i' : 3 ,'o' : 4, 'u' : 5}
	return "".join(str(d[s]) if s in "aeiou" else s for s in list(word))





#################################################################
"""
Solution 6
"""


    def replace_vowel(word):
    for i in word:
        if i in "aeiou":
            if i=='a':
                word = word.replace(i,'1')
            elif i=='e':
                word = word.replace(i, '2')
            elif i=='i':
                word = word.replace(i, '3')
            elif i=='o':
                word = word.replace(i, '4')
            else:
                word = word.replace(i, '5')
    return word