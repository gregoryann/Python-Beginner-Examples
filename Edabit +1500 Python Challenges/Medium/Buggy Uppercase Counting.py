"""
Buggy Uppercase Counting

In the Code tab is a function which is meant to return how many uppercase letters there are in a list of various words. Fix the list comprehension so that the code functions normally!

Examples
count_uppercase(["SOLO", "hello", "Tea", "wHat"]) ➞ 6

count_uppercase(["little", "lower", "down"]) ➞ 0

count_uppercase(["EDAbit", "Educate", "Coding"]) ➞ 5

Notes
Check the Resources for some helpful tutorials on list comprehensions.
"""




################################################################
"""
Solution 1
"""


def count_uppercase(lst):
	return sum(letter.isupper() for word in lst for letter in word)



################################################################
"""
Solution 2
"""


count_uppercase=lambda l:sum(w.isupper()for w in str(l))





################################################################
"""
Solution 3
"""


def count_uppercase(lst):
    n_lst = []
    for word in lst:
        for letter in word:
            if letter.isupper() == True:
                n_lst.append(letter)
    return len(n_lst)






#################################################################
"""
Solution 4
"""


def count_uppercase(lst):
	return sum(1 for letter in "".join(lst) if letter.isupper())




