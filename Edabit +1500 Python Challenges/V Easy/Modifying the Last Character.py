"""
Modifying the Last Character
Create a function which makes the last character of a string repeat n number of times.

Examples
modify_last("Hello", 3) ➞ "Hellooo"

modify_last("hey", 6) ➞ "heyyyyyy"

modify_last("excuse me what?", 5) ➞ "excuse me what?????"
Notes
Test will include numbers and punctuation.
Make sure the code is not case sensitive.

"""



"""
Solution 1
"""

def modify_last(txt, n):
    return txt[:-1] + txt[-1] * n

"""
Solution 2
"""

modify_last=lambda t,n:t[:-1]+n*t[-1]

"""
Solution 3
"""

def modify_last(txt, n):
	x = txt[-1]*(n-1)
	return txt+x

"""
Solution 4
"""

def modify_last(txt, n):
	x=txt[-1]
	y=txt+(x*(n-1))
	return y


def modify_last(txt, n):
	repeated_char = txt[-1] * (n - 1)
	return (txt + repeated_char)


def modify_last(txt, n):
  last = txt[-1] * n
  char = txt+last
  return char[:-1]



