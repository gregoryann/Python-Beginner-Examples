"""
Count the Capital Letters
Given a string of letters, how many capital letters are there?

Examples
capital_letters("fvLzpxmgXSDrobbgMVrc") ➞ 6

capital_letters("JMZWCneOTFLWYwBWxyFw") ➞ 14

capital_letters("mqeytbbjwqemcdrdsyvq") ➞ 0

"""


"""
Solution 1
"""

def capital_letters(txt):
	return sum(i.isupper() for i in txt)
    
"""
Solution 2
"""

def capital_letters(txt):
	count = len([letter for letter in txt if letter.isupper()])
	return count

"""
Solution 3
"""

capital_letters = lambda txt : sum(1 for ch in txt if ch.isupper())

"""
Solution 4
"""

def capital_letters(txt):
        string1 = txt
        result_upper = ""
        count_Upper = 0
        for i in string1:
            if i == i.upper():
                result_upper = result_upper + i
                count_Upper +=1
            else:
                pass
        return count_Upper
user1 = "fvLzpxmgXSDrobbgMVrc"
clobj = capital_letters(user1)



