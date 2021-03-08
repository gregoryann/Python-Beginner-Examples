"""
Missing Third Angle
You are given 2 out of 3 angles in a triangle, in degrees.

Write a function that classifies the missing angle as either "acute", "right", or "obtuse" based on its degrees.

An acute angle is less than 90 degrees.
A right angle is exactly 90 degrees.
An obtuse angle is greater than 90 degrees (but less than 180 degrees).
For example: missing_angle(11, 20) should return "obtuse", since the missing angle would be 149 degrees, which makes it obtuse.

Examples
missing_angle(27, 59) ➞ "obtuse"

missing_angle(135, 11) ➞ "acute"

missing_angle(45, 45) ➞ "right"
Notes
The sum of angles of any triangle is always 180 degrees.

"""




"""
Solution 1
"""

def missing_angle(angle1, angle2):
	if (angle1+angle2) < 90: return "obtuse"
	if (angle1+angle2) == 90: return "right"
	if (angle1+angle2) > 90: return "acute"

"""
Solution 2
"""

def missing_angle(angle1, angle2):
	angle3 = 180 - angle1 - angle2
	if angle3 == 90:
	  return "right"
	elif angle3 > 90:
	  return "obtuse"
	else:
	  return "acute"

"""
Solution 3
"""

def missing_angle(angle1, angle2):
	diff = 180 - angle1 - angle2
	if(diff < 90):
		return "acute"
	if(diff > 90):
		return "obtuse"
	if(diff == 90):
		return "right"

"""
Solution 4
"""

def missing_angle(angle1, angle2):
	res = 180 - angle1 - angle2
	if res < 90:
		return "acute"
	if res == 90:
		return "right"
	if res > 90:
		return "obtuse"




