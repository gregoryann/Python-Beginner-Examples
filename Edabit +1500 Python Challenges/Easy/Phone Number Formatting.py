"""

Phone Number Formatting

Create a function that takes a list of 10 numbers (between 0 and 9) and returns a string of those numbers formatted as a phone number (e.g. (555) 555-5555).

Examples
format_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) ➞ "(123) 456-7890"

format_phone_number([5, 1, 9, 5, 5, 5, 4, 4, 6, 8]) ➞ "(519) 555-4468"

format_phone_number([3, 4, 5, 5, 0, 1, 2, 5, 2, 7]) ➞ "(345) 501-2527"

Notes
Don't forget the space after the closing parenthesis.
"""



#############################################################
"""
Solution 1
"""

def format_phone_number(lst):
  return '({}{}{}) {}{}{}-{}{}{}{}'.format(*lst)




#############################################################
"""
Solution 2
"""

def format_phone_number(lst):
  s = "".join(map(str, lst))
  return "({}) {}-{}".format(s[0:3], s[3:6], s[6:])




#############################################################
"""
Solution 3
"""

def format_phone_number(lst):
	return (lambda chars: '({0}) {1}-{2}'.format(
    ''.join(chars[:3]),
  	''.join(chars[3:6]),
		''.join(chars[6:])))([str(c) for c in lst])





#############################################################
"""
Solution 4
"""

format_phone_number = lambda x: "({}{}{}) {}{}{}-{}{}{}{}".format(*x)




#############################################################
"""
Solution 5
"""


def format_phone_number(lst):
  str_lst = ''.join([str(c) for c in lst])
  return "({0}) {1}-{2}".format(str_lst[:3], str_lst[3:6], str_lst[6:])





#############################################################
"""
Solution 6
"""


def format_phone_number(lst):
    def magic(numList):         # [1,2,3]
        s = map(str, numList)   # ['1','2','3']
        s = ''.join(s)          # '123'
        s = int(s)              # 123
        return s
    fst = magic(lst[0:3])
    snd = magic(lst[3:6])
    trd = magic(lst[6:10])
    print(fst,snd,trd)
    phone = "({}) {}-{}".format(fst,snd,trd)
    print(phone)
    return phone