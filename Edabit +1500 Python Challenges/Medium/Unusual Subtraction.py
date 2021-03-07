"""
Unusual Subtraction

Create a function that subtracts 1 from n (unless it ends in 0) k number of times. If n ends in 0, remove the 0.

To illustrate:

n = 22
k = 3
This means our number is 22 and we have to repeat the algorithm three times. 22 does not end in 0 so we continue subtracting 1.

22 - 1 = 21
k = 1
21 - 1 = 20
k =2
Now 20 ends in 0, so we can remove it. We get 2; k = 3. The algorithm ends there because we applied it three times.

N:  K:
22
21  1
20  2
2   3


Examples
not_good_math(540, 5) ➞ 50

not_good_math(1000000000, 9) ➞ 1

not_good_math(42023110, 10) ➞ 4201
"""



################################################################
"""
Solution 1
"""


def not_good_math(n,k):
	for i in range(k):
		n=n-1 if n%10 else n//10
	
	return n



################################################################
"""
Solution 2
"""


def not_good_math(n, k):
    i = 0
    while i < k:
        if n % 10 == 0:
            n = n // 10
        else:
            n = n - 1
        i=i+1
    return n


################################################################
"""
Solution 3
"""


def not_good_math(n, k):
	num=0
	while num<k:
		if str(n).endswith('0'):
			n=int(str(n)[:-1])
			num+=1
		else:
			n-=1
			num+=1
	return n


#################################################################
"""
Solution 4
"""


def not_good_math(n, k):
	times = 0
	while times != k:
		if str(n)[-1] == '0':
			n = int(str(n)[:-1])
			times += 1
		else:
			n -= 1
			times += 1
	return n



