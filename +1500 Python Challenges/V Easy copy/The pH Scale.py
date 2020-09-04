"""
The pH Scale
Given a pH value, return whether that value is "alkaline" (greater than 7), "acidic" (less than 7), or "neutral" (7). Return "invalid" if the value given is less than 0 or greater than 14.

Image of a pH chart

Examples
pH_name(5) ➞ "acidic"

pH_name(8.7) ➞ "alkaline"

pH_name(7) ➞ "neutral"
Notes
Values such as 6.9999 and 8.00001 should return "acidic" and "alkaline" respectively.
"""


"""
Solution 1
"""

def pH_name(pH):
	if pH < 0 or pH > 14 :
		return "invalid"
	if pH < 7.0 : 
		return "acidic"
	if pH > 8.0 : 
		return "alkaline"
	else:
		return "neutral"




