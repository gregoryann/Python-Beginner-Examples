"""
Power Calculator
Create a function that takes voltage and current and returns the calculated power.

Examples
circuit_power(230, 10) ➞ 2300

circuit_power(110, 3) ➞ 330

circuit_power(480, 20) ➞ 9600

Notes
Requires basic calculation of electrical circuits (see Resources for info).
"""


"""
Solution 1
"""

circuit_power=int.__mul__

"""
Solution 2
"""

def circuit_power(voltage, current):
	return voltage * current

"""
Solution 3
"""

circuit_power=lambda v,c: v*c

"""
Solution 4
"""

def circuit_power(voltage, current):
	return voltage * current
	
circuit_power(220, 10)




