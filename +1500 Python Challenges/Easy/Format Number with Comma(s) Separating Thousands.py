"""
Format Number with Comma(s) Separating Thousands

Create a function that takes a number as an argument and returns a string formatted to separate thousands.

Examples
format_num(1000) ➞ "1,000"

format_num(100000) ➞ "100,000"

format_num(20) ➞ "20"

Notes
You can expect a valid number for all test cases.
"""



################################################################
"""
Solution 1
"""


def format_num(n):
		return "{:,}".format(n)







################################################################
"""
Solution 2
"""


def format_num(n):
  n = str(n)[::-1]
  return ','.join([n[i:i+3] for i in range(0, len(n), 3)])[::-1]







################################################################
"""
Solution 3
"""


def format_num(n):
	result = list()
	n = str(n)[::-1]
	while n:
		result.append(n[:3])
		n = n[3:]
	return ",".join(result)[::-1]








#################################################################
"""
Solution 4
"""

format_num=lambda n:','.join([str(n)[::-1][i:i+3]for i in range(0,len(str(n)),3)])[::-1]







#################################################################
"""
Solution 5
"""


def format_num(n):
    n = list(str(n))

    if len(n) > 3:
        for x in range(0, len(n)+1):
            if (x + 1) % 4 == 0:
                n.insert(-x, ",")



    return ''.join(n)





#################################################################
"""
Solution 6
"""


    def format_num(n):
	listnum = list(str(n))
	threelen = -(int((len(listnum)-1)/3))
	lenrange = [i *3 for i in range(threelen,0)]
	for i in lenrange: 
		listnum.insert(i,',')
	return ''.join(listnum)