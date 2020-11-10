"""
Sum of Two Numbers (with a twist!)

Wait, wait wait...

This is an "expert" challenge!??! Why is a sum of two numbers an "expert" challenge?!?! Well, the numbers can have 1000 digits...

Muahahahha!

Examples
sum2("5125515215521515", "125261616261626") ➞ "5250776831783141"

sum2("6666666666666666666666666666", "99999999999999999999999") ➞ "6666766666666666666666666665"

sum2("123456789123456789123456789", "987654321987654321987654329876543") ➞ "987654445444443445444443453333332"

Notes
Remember how to sum two numbers ON PAPER; it could be useful.
Your function must run in less than 10 seconds because Edabit has a time limit.
"""


################################################################
"""
Solution 1
"""


# `str(int(a) + int(b))` ARE good enough!
# But imagining numbers are really HUGE:
from itertools import zip_longest as zipl
def sum2(a, b):
    res, c = [], 0
    for d1, d2 in zipl(reversed(a), reversed(b), fillvalue=0):
        s = int(d1) + int(d2) + c
        res.append(s % 10)
        c = s // 10
    if c: res.append(c)
    return ''.join(map(str, reversed(res)))



################################################################
"""
Solution 2
"""


def sum2(a, b):
  return str(eval("{}+{}".format(a,b)))



################################################################
"""
Solution 3
"""


sum2 = lambda a,b: str(int(a)+int(b))





