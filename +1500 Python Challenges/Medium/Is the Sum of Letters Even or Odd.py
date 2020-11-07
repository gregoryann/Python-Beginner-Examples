"""
Is the Sum of Letters Even or Odd?

Create a function that takes a string and returns True if the sum of the position of every letter in the alphabet is even and False if the sum is odd.

Examples
is_alpha("i'am king")  ➞ True
# 9 + 1 + 13 + 11 + 9 + 14 + 7 = 64 (even)

is_alpha("True") ➞ True
# 20 + 18 + 21 + 5= 64 (even)

is_alpha("alexa") ➞ False
# 1 + 12 + 5 + 24 + 1= 43 (odd)


Notes
Case insensitive.
Ignore non-letter symbols.
"""



################################################################
"""
Solution 1
"""


def is_alpha(word):
	return sum(ord(i) - 96 for i in word if i.isalpha())%2 == 0



################################################################
"""
Solution 2
"""


def is_alpha(word):
    myans = 0
    for item in word:
        a = ord(item.lower())
        if 97 <= a <= 122:
            myans += a - 96
    return myans % 2 == 0


################################################################
"""
Solution 3
"""


def is_alpha(word):
	sum = 0 
	print(word)
	for char in word.lower() :
		if char >= 'a' and char <= 'z' :
			sum += ord(char) - ord('a') + 1
			print(ord(char) - ord('a'), char)
	return sum%2 == 0



#################################################################
"""
Solution 4
"""


def is_alpha(word):
        alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        count = 0
        for letters in word:
            if letters in alphabet:
                count+= alphabet.index(letters)+1
        return count%2 == 0



