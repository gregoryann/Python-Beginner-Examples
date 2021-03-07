"""
Wiggled Strings

Create a function that returns a list of the given string but offset by spaces. Here are some more precise instructions:

Keep adding spaces on the left until you have the same number of spaces as the word length.
Then keep removing spaces until you reach the original word.
Below are some helpful examples!

Examples
wiggle_string("hello") ➞ [
  "hello",
  " hello",
  "  hello",
  "   hello",
  "    hello",
  "     hello"
  "    hello",
  "   hello",
  "  hello",
  " hello",
  "hello"
]

wiggle_string("EDABIT") ➞ [
  "EDABIT",
  " EDABIT",
  "  EDABIT",
  "   EDABIT",
  "    EDABIT",
  "     EDABIT",
  "      EDABIT",
  "     EDABIT",
  "    EDABIT",
  "   EDABIT",
  "  EDABIT",
  " EDABIT",
  "EDABIT"
]

wiggle_string("Wiggle Time") ➞ [
  "Wiggle Time",
  " Wiggle Time",
  "  Wiggle Time",
  "   Wiggle Time",
  "    Wiggle Time",
  "     Wiggle Time",
  "      Wiggle Time",
  "       Wiggle Time",
  "        Wiggle Time",
  "         Wiggle Time",
  "          Wiggle Time",
  "           Wiggle Time",
  "          Wiggle Time",
  "         Wiggle Time",
  "        Wiggle Time",
  "       Wiggle Time",
  "      Wiggle Time",
  "     Wiggle Time",
  "    Wiggle Time",
  "   Wiggle Time",
  "  Wiggle Time",
  " Wiggle Time",
  "Wiggle Time"
]

"""



################################################################
"""
Solution 1
"""


def wiggle_string(s):
	lst = [' '*i+s for i in range(len(s)+1)]
	return lst + lst[-2::-1]


################################################################
"""
Solution 2
"""


def wiggle_string(s):
    a = []
    for i in range(len(s)+1):
        a.append(" " * i + s)
    for i in range(len(s)-1, -1, -1):
        a.append(" " * i + s)
    return a


################################################################
"""
Solution 3
"""


def wiggle_string(s):
	a=len(s)
	newStr=""
	newLst=[]
	for i in range(0,a):
		newStr=s.rjust(a+i," ")
		newLst.append(newStr)
	for i in range(a,-1,-1):
		newStr=s.rjust(a+i," ")
		newLst.append(newStr)
	return newLst



#################################################################
"""
Solution 4
"""


def wiggle_string(s):
	l = len(s) * 2 + 1
	f1 = [i * " " + s for i in range(0, l//2 + 1)]
	f2 = [i * " " + s for i in range(l//2 - 1, -1, -1)]	
	return f1 + f2



