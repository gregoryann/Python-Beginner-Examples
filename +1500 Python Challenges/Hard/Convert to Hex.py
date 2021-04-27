"""
Convert to Hex
Create a function that takes a strings characters as ASCII and returns each characters hexadecimal value as a string.

Examples
convert_to_hex("hello world") ➞ "68 65 6c 6c 6f 20 77 6f 72 6c 64"

convert_to_hex("Big Boi") ➞ "42 69 67 20 42 6f 69"

convert_to_hex("Marty Poppinson") ➞ "4d 61 72 74 79 20 50 6f 70 70 69 6e 73 6f 6e"

Notes
Each byte must be seperated by a space.
All alpha hex characters must be lowercase.
"""






################################################################
"""
Solution 1
"""


def convert_to_hex(txt):
	return ' '.join(hex(ord(i))[2:] for i in txt)




################################################################
"""
Solution 2
"""


def convert_to_hex(txt):
    a = txt
    b = []
    for i in a:
        b.append(hex(ord(i)))
    return "".join(" ".join(b).split("0x"))



################################################################
"""
Solution 3
"""


def convert_to_hex(txt):
	x = [hex(ord(x)).replace("0x","") for x in txt]
	return ' '.join(x)



################################################################
"""
Solution 4
"""

def convert_to_hex(txt):
	import re,codecs
	return " ".join(re.findall(r'\w\w',str(codecs.encode(txt.encode(), "hex")).replace("'","")[1:]))



