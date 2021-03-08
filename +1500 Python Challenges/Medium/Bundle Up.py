"""
Bundle Up!

Lets assume for the purposes of this challenge that for every layer of fabric you wear when it's cold outside (coats, cardigans, etc), the temperature increases by a tenth of the total.

Given n number of layers and a given temperature, return the temperature inside of all those warm fuzzy layers. Round to the nearest tenth of a degree.

calc_bundled_temp(2, "10*C") ➞ "12.1*C"
# 10 * 1.1 = 11
# 11 * 1.1 = 12.1
Examples
calc_bundled_temp(1, "2*C") ➞ "2.2*C"

calc_bundled_temp(4, "6*C") ➞ "8.8*C"

calc_bundled_temp(20, "4*C") ➞ "26.9*C"

Notes
The temperature will be given in celsius and as a string.
Note that the degrees sign is given as an asterisk.
"""



################################################################
"""
Solution 1
"""


def calc_bundled_temp(n, temp):
    t = int(temp[:-2])
    for _ in range(n):
        t *= 1.1
    return '{:.1f}*C'.format(t)



################################################################
"""
Solution 2
"""


def calc_bundled_temp(n, temp):
	return str(round(int(temp.strip('*C'))*(1.1**n), 1))+'*C'



################################################################
"""
Solution 3
"""


def calc_bundled_temp(n, temp):
	temp = int(temp.split('*')[0])
	while n>0:
		n -= 1
		temp *= 1.1
	return '{}*C'.format(round(temp, 1))



#################################################################
"""
Solution 4
"""


import re


def calc_bundled_temp(n, temp):
    initial_temp = float(re.search('\d+', temp).group())
    for num in range(1, n+1):
        initial_temp = (initial_temp * 0.1) + initial_temp
    return str(round(initial_temp,1)) + "*C"



