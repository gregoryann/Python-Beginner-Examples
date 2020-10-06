"""

Temperature Conversion

Write a program that takes temperature input in Celsius and returns temperature measurements , after conversion to Fahrenheit and Kelvin.

The formula to calculate the temperature in Fahrenheit from Celsius is:

F = C*9/5 +32
The formula to calculate the temperature in Kelvin from Celsius is:

K = C + 273.15
Examples
tempConversion(0) ➞ [32, 273.15]
// 0°C is equal to 32°F and 273.15 K.

tempConversion(100) ➞ [212, 373.15]

tempConversion(-10) ➞ [14, 263.15]

tempConversion(300.4) ➞ [572.72, 573.55]

Notes
Return calculated temperatures up to two decimal places. Check Tests to see what to output if the input is invalid
"""




################################################################
"""
Solution 1
"""

def tempConversion(cTemp):
  	return [round(cTemp * 9 / 5 + 32, 2), round(cTemp + 273.15, 2)] if cTemp > -273.15 else "Invalid"




################################################################
"""
Solution 2
"""

def tempConversion(cTemp):
  # return [fTemp, kTemp]
	fTemp = ((cTemp*9)/5) + 32
	kTemp = cTemp + 273.15
	f = round(fTemp, 2)
	c = round(kTemp, 2)
	if cTemp <= -273.16:
		return 'Invalid'
	else:
		return [f, c]



################################################################
"""
Solution 3
"""

def tempConversion(cTemp):
	if cTemp < -273.15 or isinstance(cTemp, str):
		return 'Invalid'
	return [round(cTemp*9/5 +32,2), round(cTemp + 273.15,2)]





#################################################################
"""
Solution 4
"""

tempConversion=lambda C: [round(C*9/5+32,2),round(C+273.15,2)] if C>-273.16 else 'Invalid'




