"""
First Before Second Letter

You are given three inputs: a string, one letter, and a second letter.

Write a function that returns True if every instance of the first letter occurs before every instance of the second letter.

Examples
first_before_second("a rabbit jumps joyfully", "a", "j") ➞ True
# Every instance of "a" occurs before every instance of "j".

first_before_second("knaves knew about waterfalls", "k", "w") ➞  True

first_before_second("happy birthday", "a", "y") ➞ False
# The "a" in "birthday" occurs after the "y" in "happy".

first_before_second("precarious kangaroos", "k", "a") ➞ False


Notes
All strings will be in lower case.
All strings will contain the first and second letters at least once.
"""



################################################################
"""
Solution 1
"""


def first_before_second(s, first, second):
	return s.rindex(first) < s.index(second)


################################################################
"""
Solution 2
"""


def first_before_second(s, first, second):
	fInd = max([i for i in range(len(s)) if s[i] == first])
	sInd = min([i for i in range(len(s)) if s[i] == second])
	return fInd < sInd



################################################################
"""
Solution 3
"""


def first_before_second(st,w1,w2):
    s1 = []
    s2 = []
    for i in range(len(st)):
        if st[i]==w1:
            s1.append(i)
        elif st[i]==w2:
            s2.append(i)
    for a in s1:
        if a > s2[0]:
            return False
    return True



################################################################
"""
Solution 4
"""


def first_before_second(s, first, second):
	if ''.join(s).rindex(first)<s.find(second) and s.find(second)!=-1:
		return True
	return False





