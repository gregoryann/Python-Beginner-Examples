"""

Convert Yen to USD
Create a function that can turn Yen (Japanese dollar) to USD (American dollar).

Examples
yen_to_usd(1) ➞ 0.01

yen_to_usd(500) ➞ 4.65

yen_to_usd(649) ➞ 6.04
Notes
Each Yen to USD conversion is Yen / 107.5




"""






"""
Solution 1
"""


def yen_to_usd(yen):
	return round(yen / 107.5, 2)




"""
Solution 2
"""

yen_to_usd=lambda y:round(y/107.5,2)



"""
Solution 3
"""

def yen_to_usd(yen):
	return round(float(yen)/107.5,2)



"""
Solution 4
"""






