"""
The Million Dollar Fence

Your task is to create a fence worth $1 million. You are given the price of the material (per character), meaning the length of the fence will change depending on the cost of the material.

Create a function which constructs this pricey pricey fence, using the letter "H" to build.

construct_fence("$50,000") ➞ "HHHHHHHHHHHHHHHHHHHHHHHHHHHH"
# 20 fence posts were set up ($1,000,000 / $50,000 = 20)
Examples
construct_fence("$50,000") ➞ "HHHHHHHHHHHHHHHHHHHHHHHHHHHH"

construct_fence("$100,000") ➞ "HHHHHHHHHH"

construct_fence("$1,000,000") ➞ "H"

Notes
You are ordered to spend all of your $1,000,000 budget...
"""


################################################################


"""
Solution 1
"""

def construct_fence(p):
	p = int(p.replace(',', '')[1:])
	return 'H' * (1000000//p)

"""
Solution 2
"""

def construct_fence(p):
	return 'H' * (1000000//int(''.join(ch for ch in p if ch.isdigit())))

"""
Solution 3
"""

def construct_fence(p):
	p = p.replace("$", "").replace(",", "")
	l = 1000000/int(p)
	return 'H' * int(l)

"""
Solution 4
"""

def construct_fence(p):
	a = [x for x in (p.split('$'))[1]]
	for x in a:
		if x == ',':
			a.remove(x)
	k = int(1000000/(int(''.join(a))))
	return 'H'*k

"""
Solution 5
"""

def construct_fence(p):
	 
	cost = ""
	
	for i in p:
		if i != '$' and i != ',':
			cost += i 
	num = 1000000 // int(cost,10)
	res = "H" * num
	
	return res

