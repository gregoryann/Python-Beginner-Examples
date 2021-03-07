"""
Sock Pairs

Joseph is in the middle of packing for a vacation. He's having a bit of trouble finding all of his socks, though.

Write a function that returns the number of sock pairs he has. A sock pair consists of two of the same letter, such as "AA". The socks are represented as an unordered sequence.

Examples
sock_pairs("AA") ➞ 1

sock_pairs("ABABC") ➞ 2

sock_pairs("CABBACCC") ➞ 4


Notes
If given an empty string (no socks in the drawer), return 0.
There can be multiple pairs of the same type of sock, such as two pairs of CC for the last example.
"""



################################################################
"""
Solution 1
"""


def sock_pairs(socks):
	return sum(socks.count(i)//2 for i in set(socks))



################################################################
"""
Solution 2
"""


def sock_pairs(socks):
 sock_set=set(socks)
 #print(sock_set)
 pairs=0
 for sock in sock_set:
  count=0
  for i in range(0,len(socks)):
   if socks[i] == sock:
    count+=1
  if count // 2 > 0:
   pairs+=int(count//2)
 return pairs



################################################################
"""
Solution 3
"""


def sock_pairs(socks):
	p=0
	for i in socks:
		if socks.count(i)//2>=1:
			p+=socks.count(i)//2
			socks=socks.replace(i, '')
	return p


#################################################################
"""
Solution 4
"""


def sock_pairs(socks):
    countA = 0
    countB = 0
    countC = 0
    
    countA = socks.count("A") // 2
    countB = socks.count("B") // 2
    countC = socks.count("C") // 2
    
    return countA + countB + countC



#################################################################
"""
Solution 5
"""


import re
def sock_pairs(socks):
	return len(re.findall(r'([A-Z])\1', ''.join(sorted(socks))))