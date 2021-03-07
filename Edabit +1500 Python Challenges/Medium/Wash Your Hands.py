"""

Wash Your Hands :)

It takes 21 seconds to wash your hands and help prevent the spread of COVID-19.

Create a function that takes the number of times a person washes their hands per day N and the number of months they follow this routine nM and calculates the duration in minutes and seconds that person spends washing their hands.

Examples
wash_hands(8, 7) ➞ "588 minutes and 0 seconds"

wash_hands(0, 0) ➞ "0 minutes and 0 seconds"

wash_hands(7, 9) ➞ "661 minutes and 30 seconds"

Notes
Consider a month has 30 days.
Wash your hands.
"""



################################################################
"""
Solution 1
"""


def wash_hands(N, nM):
		return '{} minutes and {} seconds'.format(*divmod(630*N*nM, 60))



################################################################
"""
Solution 2
"""

wash_hands=lambda n,m:'%d minutes and %d seconds'%divmod(n*m*630,60)


################################################################
"""
Solution 3
"""

def wash_hands(N, nM):
	x = 21 * N * nM * 30
	return str(x//60) + " minutes and " + str(x%60) + " seconds"


#################################################################
"""
Solution 4
"""

import math
def wash_hands(n,m):
    frac, whole = math.modf(n*21*m*30/60)
    return '{} minutes and {} seconds'.format(int(whole), int(frac*60))




#################################################################
"""
Solution 5
"""

def wash_hands(N, nM):
    T = 21 * nM * 30 * N
    m = T // 60
    s = T % 60
    return str(m) + " minutes and " + str(s) + " seconds"