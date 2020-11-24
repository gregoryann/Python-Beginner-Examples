"""
Collatz Conjecture

A Collatz sequence is generated like this. Start with a positive number. If it's even, halve it. If it's odd, multiply it by three and add one. Repeat the process with the resulting number. The Collatz Conjecture is that every sequence eventually reaches 1 (continuing past 1 just results in an endless repeat of the sequence 4, 2, 1).

The length of the sequence from starting number to 1 varies widely.

Create a function that takes a number as an argument and returns a tuple of two elements — the number of steps in the Collatz sequence of the number, and the highest number reached.

Examples
collatz(2) ➞ (2, 2)
# seq = [2, 1]

collatz(3) ➞ (8, 16)
# seq = [3, 10, 5, 16, 8, 4, 2, 1]

collatz(7) ➞ (17, 52)
# seq = [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]

collatz(8) ➞ (4, 8)
# seq = [8, 4, 2, 1]

Notes
(Improbable) Bonus: Find a positive starting number that doesn't reach 1, and score a place in Math history plus a cash prize.
"""



################################################################
"""
Solution 1
"""


def collatz(n):
    res = []
    while n != 1:
        res.append(n)
        n = n*3 + 1 if n%2 else n//2
    return len(res) + 1, max(res)



################################################################
"""
Solution 2
"""


def collatz(n):
    seq = [n]
    while seq[-1] != 1:
        seq.append(seq[-1] * 3 + 1 if seq[-1] % 2 else seq[-1] // 2)
    return (len(seq), max(seq))



################################################################
"""
Solution 3
"""


def collatz(n):
    seq = [n]
    k = n
    while True:
        if k % 2 == 0:
            k /= 2
        else:
            k = k*3+1
        seq.append(k)
        if k == 1:
            break
    return len(seq), round(max(seq))



#################################################################
"""
Solution 4
"""


def collatz(n):
	max_number = 0
	steps = 1
	while n != 1:
		if n % 2 == 0:
			n = n // 2
			steps += 1
			if n > max_number:
				max_number = n
		elif n % 2 != 0:
			n = (n*3) + 1
			steps += 1
			if n > max_number:
				max_number = n
	return (steps,max_number)





