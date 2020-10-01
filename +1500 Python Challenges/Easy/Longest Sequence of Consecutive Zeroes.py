"""
Longest Sequence of Consecutive Zeroes

Write a function that returns the longest sequence of consecutive zeroes in a binary string.

Examples
longest_zero("01100001011000") ➞ "0000"

longest_zero("100100100") ➞ "00"

longest_zero("11111") ➞ ""

Notes
If no zeroes exist in the input, return an empty string.
"""



################################################################






################################################################
"""
Solution 1
"""

def longest_zero(s):
	return max(s.split('1'), key=len)



################################################################

"""
Solution 2
"""

import re

def longest_zero(s):
    zeroes = re.findall(r'0+', s)
    return sorted(zeroes, key=len)[-1] if zeroes else ''


################################################################

"""
Solution 3
"""



def longest_zero(s):
    ender = s + '1'
    list1 = []
    stringy = ""
    counter = 0
    for i in ender:
        if i =='0':
            counter = counter + 1
        elif i == '1':
            list1.append(counter)
            counter = 0
    maxy = max(list1)
    for i in range(maxy):
        stringy = stringy + "0"

    return stringy





################################################################

"""
Solution 4
"""


import itertools
def longest_zero(l):
    solution=[list(g) for (k,g) in itertools.groupby(l) if k=='0']
    if solution:
        return len(max(solution))*'0'
    return ''

