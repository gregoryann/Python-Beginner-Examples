"""
Coaxial Cable Impedance

Create a function that takes the values Dd ( Dielectric Outer Diameter) , Dc (Inner Conductor Diameter) and er (Dielectric constant) and calculates the Coaxial Cable Impedance. Impedance Calculator(Dd,Dc,er)

Examples
Impedance Calculator(20.7,2,4) ➞ 70.0 

Impedance Calculator(5.3,1.2,2.2) ➞ 60.0 

Impedance Calculator(4.48,1.33,2.2) ➞ 50.0 

Notes
If you get stuck on a challenge, find help in the Resources tab.
Round your result to one decimal places.
"""



################################################################
"""
Solution 1
"""


import math
def Impedance_Calculator(Dd,Dc,er):
	return round(138 * math.log(Dd / Dc, 10) / math.sqrt(er),1)



################################################################
"""
Solution 2
"""


def Impedance_Calculator(Dd,Dc,er):
	import math
	return round(138*math.log(Dd/Dc, 10)/math.sqrt(er), 1)



################################################################
"""
Solution 3
"""


from math import sqrt , log10
def Impedance_Calculator(Dd,Dc,er):
    Zo=(138*log10(Dd/Dc))/sqrt(er)
    return round(Zo,1)





