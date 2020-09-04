"""
Word Numbers!
Create a function that returns a number, based on the string provided. Here is a list of all digits (if you are non english speaker):

String	Number
"one"	1
"two"	2
"three"	3
"four"	4
"five"	5
"six"	6
"seven"	7
"eight"	8
"nine"	9
"zero"	0
Examples
word("one") ➞ 1

word("two") ➞ 2

word("nine") ➞ 9
Notes
All numbers will be 1 digit and they will always exist, also all numbers will be in ℕ ℕo(don't have decimal places, and they are positive, including 0).

"""






"""
Solution 1
"""

def word(s):
	return 'zero one two three four five six seven eight nine'.split(' ').index(s)

"""
Solution 2
"""

def word(s):
	return ['zero','one','two','three','four','five','six','seven','eight','nine'].index(s)

"""
Solution 3
"""

word=lambda s:{'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'zero':0}[s]

"""
Solution 4
"""

def word(s):
	string = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
	for x, y in enumerate(string):
		if y == s:
			return x


"""
Solution 5
"""

def word(s):
	d = {
	"one" : 1,
	"two"	: 2,
	"three"	: 3,
	"four"	: 4,
	"five"	: 5,
	"six"	: 6,
	"seven"	: 7,
	"eight"	: 8,
	"nine"	: 9,
	"zero"	:0
	}
	return d[s]