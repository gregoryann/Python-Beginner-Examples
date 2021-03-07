"""
Hitting the Jackpot
Create a function that takes a list (slot machine outcome) and returns True if all elements in the list are identical, and False otherwise. The list will contain 4 elements.

Examples
test_jackpot(["@", "@", "@", "@"]) ➞ True

test_jackpot(["abc", "abc", "abc", "abc"]) ➞ True

test_jackpot(["SS", "SS", "SS", "SS"]) ➞ True

test_jackpot(["&&", "&", "&&&", "&&&&"]) ➞ False

test_jackpot(["SS", "SS", "SS", "Ss"]) ➞ False
Notes
The elements must be exactly identical for there to be a jackpot.

"""


"""
Solution 1
"""

def test_jackpot(result):
    return result.count(result[0]) == 4

"""
Solution 2
"""

def test_jackpot(result):
    return result.count(result[0]) == 4

"""
Solution 3
"""

def test_jackpot(result):
    return bool(result[0] == result[1] and result[0] == result[2] and result[0] == result[3])







