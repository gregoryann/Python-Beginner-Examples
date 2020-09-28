"""
Card Counting (BlackJack)

In BlackJack, cards are counted with -1, 0, 1 values:

2, 3, 4, 5, 6 are counted as +1
7, 8, 9 are counted as 0
10, J, Q, K, A are counted as -1
Create a function that counts the number and returns it from the list of cards provided.

Examples
count([5, 9, 10, 3, "J", "A", 4, 8, 5]) ➞ 1

count(["A", "A", "K", "Q", "Q", "J"]) ➞ -6

count(["A", 5, 5, 2, 6, 2, 3, 8, 9, 7]) ➞ 5

Notes
String inputs will always be upper case.
You do not need to consider case sensitivity.
If the argument is empty, return 0.
No input other than: 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A".
"""



#############################################################
#                        MY SOLUTIONS                       #
#############################################################


"""
Solution 1
"""

def count(deck):
	return sum([1 if str(i) in '23456' else -1 if str(i) in 'AKQJ10' else 0 for i in deck])

"""
Solution 2
"""

def count(deck):
	count = 0
	for card in deck:
		if card in [2, 3, 4, 5, 6]:
			count += 1
		if card in [10, "J", "Q", "K", "A"]:
			count -= 1
	return count

"""
Solution 3
"""

def count(deck):
    a = [2, 3, 4, 5, 6]
    b = [10, 'J', 'Q', 'K', 'A']
    return sum([1 if i in a else -1 if i in b else 0 for i in deck])

"""
Solution 4
"""

import re
def count(deck):
	s = ''.join([str(i) for i in deck])
	cnt = len(re.findall('[2-6]',s)) * 1
	cnt += len(re.findall('[JQKA1]',s)) * -1
	return cnt


"""
Solution 5
"""

count=lambda l:sum((e<7)+(e<10)for e in l if e*0==0)-len(l)

count=lambda d:sum(-1 if i in [10,'J','Q','K','A']else 1if i>1and i<7else 0for i in d)


"""
Solution 6
"""

def count(deck):
	
	one = [2, 3, 4, 5, 6]
	zero = [7, 8, 9]
	neg_one = [10, 'J', 'Q', 'K', 'A']
	
	result = 0
	
	for card in deck:
		
		if card in one:
			result += 1
		elif card in zero:
			result += 0
		elif card in neg_one:
			result += -1
		else:
			return 'Error!'.upper() + '{}Incorrect card value'.format(card)
	
	return result