"""
Trolls are attacking your comment section!
A common way to deal with this situation is to remove all of the vowels
from the troll's comments, neutralizing the threat.
Your task is to write a function that takes a string and return a new string
with all vowels removed.
For example, the string 'This website is for losers LOL!' would become
'Ths wbst s fr lsrs LL!'.
Note: For this kata 'y' isn't considered a vowel.
"""


#############################################################
#                        MY SOLUTIONS                       #
#############################################################



# My Answer
def disemvowel(string):
    condition = 'aAeEiIoOuU'
    filter = [character for character in string if character not in condition]
    return ''.join(filter)

# Best Answer
def disemvowel(s):
    return s.translate(None, "aeiouAEIOU")

#Tests
test.assert_equals(disemvowel("This website is for losers LOL!"),
                              "Ths wbst s fr lsrs LL!")