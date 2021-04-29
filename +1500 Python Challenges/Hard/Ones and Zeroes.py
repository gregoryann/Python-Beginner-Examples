"""
Ones and Zeroes

Write a function that returns True if every consecutive sequence of ones is followed by a consecutive sequence of zeroes of the same length.

Examples
same_length("110011100010") ➞ True

same_length("101010110") ➞ False

same_length("111100001100") ➞ True

same_length("111") ➞ False
"""


################################################################
"""
Solution 1
"""


import re
def same_length(txt):
	return [len(i) for i in re.findall('1+',txt)]==[len(i) for i in re.findall('0+',txt)]




################################################################
"""
Solution 2
"""


def same_length(t):
	s=[]
	try:
		for x in t:
			if x=='1':s.append('1')
			else:s.pop()
	except:return 0
	return not s



################################################################
"""
Solution 3
"""


import re
def same_length(txt):
    # I hate seeing the solutions
    # because they are
    #always so fking simple :)
	return [len(i) for i in re.findall('1+',txt)] == [len(i) for i in re.findall('0+',txt)]



################################################################
"""
Solution 4
"""


def same_length(txt):
	s = txt.replace('0',' ')
	d = [len(x) for x in  s.split()]
	return txt == ''.join('1'*x+'0'*x  for x in d)



