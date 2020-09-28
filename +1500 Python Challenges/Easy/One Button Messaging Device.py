"""
One Button Messaging Device

Imagine a messaging device with only one button. For the letter A, you press the button one time, for E, you press it five times, for G, it's pressed seven times, etc, etc.

Write a function that takes a string (the message) and returns the total number of times the button is pressed.

Examples
how_many_times("abde") ➞ 12

how_many_times("azy") ➞ 52

how_many_times("qudusayo") ➞ 123

Notes
Ignore spaces.
"""




#############################################################
#                        MY SOLUTIONS                       #
#############################################################



"""
Solution 1
"""

def how_many_times(msg):
	return sum(ord(i) - 96 for i in msg)

"""
Solution 2
"""

def how_many_times(msg):
	letters='abcdefghijklmnopqrstuvwxyz'
	total=0
	for i in msg:
		total+=letters.find(i)+1
	return total

"""
Solution 3
"""

import string
def how_many_times(msg):
	return sum([string.ascii_lowercase.index(i) + 1 for i in msg])

"""
Solution 4
"""

def how_many_times(msg):
    lst = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    count = 0
    for i in msg.lower():
        count += lst.index(i)        
    return count




