"""
Making Change

Create a function that takes an amount of monetary change (e.g. 47 cents) and breaks down the most efficient way that change can be made using USD quarters, dimes, nickels and pennies. Your function should return a dictionary.

Examples
make_change(47) ➞ { "q": 1, "d": 2, "n": 0, "p": 2 }

make_change(24) ➞ { "q": 0, "d": 2, "n": 0, "p": 4 }

make_change(92) ➞ { "q": 3, "d": 1, "n": 1, "p": 2 }

Notes
Amount given will always be less than 100 and more than 0.
"""



################################################################
"""
Solution 1
"""


def make_change(c):
	return {"q": c//25, "d": c%25//10, "n": c%25%10//5, "p": c%5}



################################################################
"""
Solution 2
"""


def make_change(c):
	ret = {}
	ret['q'], c = c // 25, c % 25
	ret['d'], c = c // 10, c % 10
	ret['n'], ret['p'] = c // 5, c % 5
	return ret



################################################################
"""
Solution 3
"""


def make_change(c):
	res = {'q': 0, 'd': 0, 'n': 0, 'p': 0}
	while c >= 25:
		c -= 25
		res['q'] += 1
	while c >= 10:
		c -= 10
		res['d'] += 1
	while c >= 5:
		c -= 5
		res['n'] += 1
	res['p'] += c
	return res



#################################################################
"""
Solution 4
"""


def make_change(c):
	coin_to_penny = {
		'q': 25,
		'd': 10,
		'n': 5,
		'p': 1,
	}
	coins = ['q', 'd', 'n', 'p']
	change = {}
	for coin in coins:
		coin_count = c // coin_to_penny[coin]
		change[coin] = coin_count
		c -= coin_count * coin_to_penny[coin]
	return change




