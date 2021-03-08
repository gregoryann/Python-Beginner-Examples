"""
Complete the Binary Number

Create a function which adds zeros to the start of a binary string, so that its length is a mutiple of 8.

Examples
complete_binary("1100") ➞ "00001100"

complete_binary("1101100") ➞ "01101100"

complete_binary("110010100010") ➞ "0000110010100010"

Notes
Return the same string if its length is already a multiple of 8.
"""





#############################################################
"""
Solution 1
"""

def complete_binary(s):
	return (-len(s)%8 * '0') + s




#############################################################
"""
Solution 2
"""

complete_binary=lambda s:s if len(s)%8<1else(8*(len(s)//8+1)-len(s))*'0'+s






#############################################################
"""
Solution 3
"""

def complete_binary(s):
    if len(s) % 8 == 0:
        return s
    elif len(s) < 8:
        return ('0' * (8 - len(s))) + s
    else:
        return ('0' * (8 - len(s) % 8)) + s






#############################################################
"""
Solution 4
"""

def complete_binary(s):
	return '{}{}'.format('0'*(8-len(s)%8) if len(s)%8 else '0'*0,s)







#############################################################
"""
Solution 5
"""


from math import ceil
def complete_binary(s):
	n = ceil(len(s)/8)*8
	return s.zfill(n)