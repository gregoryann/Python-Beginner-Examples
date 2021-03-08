"""
Fibonacci Sequence
The Fibonacci Sequence is the sequence of numbers (Fibonacci Numbers) whose sum is the two preceding numbers (e.g. 0, 1, 1, 2, 3, etc). Using 0 and 1 as the starting values, create a function that returns a list containing all of the Fibonacci numbers less than 255.

Examples
On generating a Fibonacci number where input is the two preceding values starting from 0 and 1 [0, 1, ...].

fibonacci_sequence(0, 1) ➞ 1

fibonacci_sequence(1, 1) ➞ 2

fibonacci_sequence(1, 2) ➞ 3
"""



################################################################
"""
Solution 1
"""


def fibonacci_sequence():
	return [0,1,1,2,3,5,8,13,21,34,55,89,144,233]



################################################################
"""
Solution 2
"""


def fibonacci_sequence():
	L = [0, 1]
	while L[-1] + L[-2] < 255:
		L.append(L[-1] + L[-2])
	return L



################################################################
"""
Solution 3
"""


def fibonacci_sequence():
	fibSeq = [0, 1]
	pointerVal = 0
	while True:
		curNum = fibSeq[pointerVal] + fibSeq[pointerVal + 1]
		if curNum >= 255:
			break
		fibSeq.append(curNum)
		pointerVal += 1
	return fibSeq



#################################################################
"""
Solution 4
"""


def fibonacciSequence():
	a = 0
	b = 1
	c = 0
	sequence = [0, 1,]
	while not b == 233:
		c = b + a
		sequence.append(c)
		###
		a = c + b
		sequence.append(a)
		###
		b = a + c
		sequence.append(b)
	return sequence



