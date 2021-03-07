"""
Money Formatting

Given a number, return a string which is formatted into US Dollars and cents!

Remember that:

You should round to two digits after the decimal point (even for integers).
Thousandths should be separated by commas.
Examples
dolla_dolla_bills(10) ➞ "$10.00"

dolla_dolla_bills(1000000) ➞ "$1,000,000.00"

dolla_dolla_bills(-314159.2653) ➞ "-$314,159.27"

dolla_dolla_bills(-56.99) ➞ "-$56.99"

Notes
There will be both negative and positive inputs.
Check the Resources Tab for many tutorials on how to approach string formatting
"""



################################################################
"""
Solution 1
"""


def dolla_dolla_bills(money):
	return '${:,.2f}'.format(money).replace('$-', '-$')



################################################################
"""
Solution 2
"""


def dolla_dolla_bills(money):
		if money > 0:
			return '${:,.2f}'.format(money)
		return '-${:,.2f}'.format(abs(money))



################################################################
"""
Solution 3
"""


def dolla_dolla_bills(money):
    if money>0:
        return ('${:,.2f}'.format(money))
    else:
        money=(-money)
        return ('-${:,.2f}'.format(money))




#################################################################
"""
Solution 4
"""


def dolla_dolla_bills(n):
		s = '${:,.2f}'.format(abs(n))
		return '-' + s if n < 0 else s




#################################################################
"""
Solution 5
"""

def dolla_dolla_bills(money):
 
	Numbers = "{0:,.2f}".format(money)
	
	Text = str(Numbers)
	
	if (Text[0] == "-"):
		Answer = "-$" + Text[1:]
		return Answer
	else:
		Answer = "$" + Text
		return Answer