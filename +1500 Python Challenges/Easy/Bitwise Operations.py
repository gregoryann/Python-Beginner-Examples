"""
Bitwise Operations

A decimal number can be represented as a sequence of bits. To illustrate:

6 = 00000110
23 = 00010111
From the bitwise representation of numbers, we can calculate the bitwise AND, bitwise OR and bitwise XOR. Using the example above:

bitwise_and(6, 23) ➞ 00000110

bitwise_or(6, 23) ➞ 00010111

bitwise_xor(6, 23) ➞ 00010001
Write three functions to calculate the bitwise AND, bitwise OR and bitwise XOR of two numbers.

Examples
bitwise_and(7, 12) ➞ 4

bitwise_or(7, 12) ➞ 15

bitwise_xor(7, 12) ➞ 11
"""



#############################################################
#                        MY SOLUTIONS                       #
#############################################################



"""
Solution 1
"""

def bitwise_and(n1, n2):
	return n1 & n2

def bitwise_or(n1, n2):
	return n1 | n2

def bitwise_xor(n1, n2):
	return n1 ^ n2


"""
Solution 2
"""

for s in["and&","or |","xor^"]:exec("bitwise_"+s[:3]+"=lambda a,b:a"+s[3]+"b")

"""
Solution 3
"""

def bitwise_and(n1, n2):
    n1b = "{:08b}".format(n1) #'00000111'
    n2b = "{:08b}".format(n2) #'00001100'
    zipped_list = zip(n1b, n2b) #[('0', '0'), ('0', '0'), ('0', '0'), ('0', '0'), ('0', '1'), ('1', '1'), ('1', '0'), ('1', '0')]
    n1b_and_n2b = ['1' if i[0]== '1' and i[1]== '1' else '0' for i in zipped_list]
    return int("".join(n1b_and_n2b), 2)

def bitwise_or(n1, n2):
    n1b = "{:08b}".format(n1)
    n2b = "{:08b}".format(n2)
    zipped_list = zip(n1b, n2b)
    n1b_or_n2b = ['0' if i[0]== '0' and i[1]== '0' else '1' for i in zipped_list]
    return int("".join(n1b_or_n2b), 2)

def bitwise_xor(n1, n2):
    n1b = "{:08b}".format(n1)
    n2b = "{:08b}".format(n2)
    zipped_list = zip(n1b, n2b)
    n1b_xor_n2b = ['0' if i[0] == i[1] else '1' for i in zipped_list]
    return int("".join(n1b_xor_n2b), 2)


"""
Solution 4
"""

def bitwise_and(n1, n2):
	n1="{0:b}".format(n1).zfill(10)
	n2="{0:b}".format(n2).zfill(10)
	#print(n1,n2)
	r=''.join(['1' if n1[c]=='1' and n2[c]=='1' else '0' for c in range(len(n1))])
	print(r)
	return int(r,base=2)
	
def bitwise_or(n1, n2):
	n1="{0:b}".format(n1).zfill(10)
	n2="{0:b}".format(n2).zfill(10)
	return int(''.join(['1' if n1[c]=='1' or n2[c]=='1' else '0' for c in range(len(n1))]),base=2)

def bitwise_xor(n1, n2):
	n1="{0:b}".format(n1).zfill(10)
	n2="{0:b}".format(n2).zfill(10)
	print(n1,n2)
	r=''.join(['1' if (n1[c]=='1' or n2[c]=='1') and not(n1[c]=='1' and n2[c]=='1') else '0' for c in range(len(n1))])
	print(r)
	return int(r,base=2)

