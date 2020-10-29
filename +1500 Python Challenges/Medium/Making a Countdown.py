"""
Making a Countdown

Create a function where given the number n to count down from, and some words txt, return a countdown sequence as a string leading up to the words at the end.

Put a full stop after each number and uppercase and add an exclamation mark to the word. See the examples below for clarification!

Examples
countdown(10, "Blast Off") ➞ "10. 9. 8. 7. 6. 5. 4. 3. 2. 1. BLAST OFF!"

countdown(3, "go") ➞ "3. 2. 1. GO!"

countdown(5, "FIRE") ➞ "5. 4. 3. 2. 1. FIRE!"

Notes
n will be a number greater than 0.
txt won't already include an exclamation mark.
Don't include 0 in the countdown.
"""





################################################################
"""
Solution 1
"""


def countdown(n, txt):
    return ". ".join([str(k) for k in range(n, 0, -1)]) + ". " + txt.upper() + "!"



################################################################
"""
Solution 2
"""


def countdown(n, txt):
	rep = ""
	for x in range(n):
		rep = rep + str(n-x) + ". "
	rep = rep + txt.upper() + "!"
	
	return rep




################################################################
"""
Solution 3
"""


def countdown(n, txt):
    count = '. '.join(
		str(i) for i in reversed(range(1, n + 1))
	)
    return '{}. {}!'.format(count, txt.upper())



#################################################################
"""
Solution 4
"""


def countdown(n, txt):
	a=txt.upper()+"!"
	newStr=""
	for i in range(n,0,-1):
		newStr=newStr+str(i)+". "
	return newStr+a



