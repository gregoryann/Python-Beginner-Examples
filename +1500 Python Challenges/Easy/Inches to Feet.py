"""
Inches to Feet

Create a function that accepts a measurement value in inches and returns the equivalent of the measurement value in feet.

Examples
inches_to_feet(324) ➞ 27

inches_to_feet(12) ➞ 1

inches_to_feet(36) ➞ 3

Notes
If inches are under 12, return 0.
"""





################################################################
"""
Solution 1
"""

def inches_to_feet(inches):
	if inches < 12:
		return 0
	return inches/12




################################################################
"""
Solution 2
"""

def inches_to_feet(inches):
	return inches/12 if inches>=12 else 0




################################################################
"""
Solution 3
"""

inches_to_feet=lambda inches: round(inches/12) if inches >=12 else 0




#################################################################
"""
Solution 4
"""

def inches_to_feet(inches):
    inch=int(inches/12)
    if(inches<12):
        return 0
    return inch
    
print(inchesToFeet(60))




