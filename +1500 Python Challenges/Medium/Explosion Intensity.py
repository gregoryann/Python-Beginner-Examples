"""
Explosion Intensity
Given a number, return a string of the word "Boom", which varies in the following ways:

The string should include n number of "o"s, unless n is below 2 (in that case, return "boom").
If n is evenly divisible by 2, add an exclamation mark to the end.
If n is evenly divisible by 5, return the string in ALL CAPS.
The example below should help clarify these instructions.

Examples
boom_intensity(4) ➞ "Boooom!"
# There are 4 "o"s and 4 is divisible by 2 (exclamation mark included)

boom_intensity(1) ➞ "boom"
# 1 is lower than 2, so we return "boom"

boom_intensity(5) ➞ "BOOOOOM"
# There are 5 "o"s and 5 is divisible by 5 (all caps)

boom_intensity(10) ➞ "BOOOOOOOOOOM!"
# There are 10 "o"s and 10 is divisible by 2 and 5 (all caps and exclamation mark included)

Notes
A number which is evenly divisible by 2 and 5 will have both effects applied (see example #4).
"Boom" will always start with a capital "B", except when n is less than 2, then return a minature explosion as "boom".
"""





################################################################
"""
Solution 1
"""


def boom_intensity(n):
	if n < 2:
		return 'boom'
	return 'B' + ('oO'[n%5==0])*n + 'mM'[n%5==0] + '!'*(1-n%2)



################################################################
"""
Solution 2
"""


def boom_intensity(n):
    if n < 2:
        return 'boom'
    s = 'B{}m'.format('o'*n)
    if not n%2:
        s += '!'
    if not n%5:
        s = s.upper()
    return s



################################################################
"""
Solution 3
"""


def boom_intensity(n):
	if n < 2:
		return "boom"
	elif n % 5 == 0 and n % 2 == 0:
		return "B" + (n * "O") + "M!"
	elif n % 2 == 0:
		return "B" + (n * "o") + "m!"
	elif n % 5 == 0:
		return "B" + (n * "O") + "M"
	else:
		return "B" + (n * "o") + "m"




#################################################################
"""
Solution 4
"""


def boom_intensity(n):
	if n < 2: return 'boom'
	if n%2 == 0 and n%5 == 0: return ('B' + 'o'*n + 'm!').upper() 
	if n%2 == 0: return 'B' + 'o'*n + 'm!'
	if n%5 == 0: return ('B' + 'o'*n + 'm').upper()
	return 'B' + 'o'*n + 'm'



