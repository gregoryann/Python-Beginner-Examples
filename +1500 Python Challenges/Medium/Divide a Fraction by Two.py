"""
Divide a Fraction by Two

Create a function that takes a number as an argument and returns half of it.

Examples
half_a_fraction("1/2") ➞ "1/4"

half_a_fraction("6/8") ➞ "3/8"

half_a_fraction("3/8") ➞ "3/16"

Notes
Always return the simplified fraction.
"""


################################################################
"""
Solution 1
"""


def half_a_fraction(fract):
	num, den = map(int, fract.split('/'))
	return '{}/{}'.format(*[(num//2, den), (num, den*2)][num%2])



################################################################
"""
Solution 2
"""


def half_a_fraction(fract):
    fract = list(map(lambda x:int(x), fract.split('/')))
    if (fract[0]) % 2 == 0:
        fract[0] = str(int(fract[0]/ 2))
    else:
        fract[1] = str(fract[1]* 2)
    fract = list(map(lambda x:str(x), fract))
    return '/'.join(fract)



################################################################
"""
Solution 3
"""


def half_a_fraction(fract):
	i1 = int(fract[fract.find("/")+1:])
	i2 = int(fract[:fract.find("/")])
	if i2%2 == 0:
	 return "{}/{}".format(int(i2/2),int(i1))
	if i2%2 != 0:
	 return "{}/{}".format(int(i2),int(i1*2))




#################################################################
"""
Solution 4
"""


from fractions import Fraction
def half_a_fraction(fract):
	x = Fraction(fract)
	y = x * Fraction(1,2)
	z = '{}/{}'.format(y.numerator,y.denominator)
	return z



