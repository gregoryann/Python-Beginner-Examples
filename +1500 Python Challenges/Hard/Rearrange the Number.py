"""
Rearrange the Number

Given a number, return the difference between the maximum and minimum numbers that can be formed when the digits are rearranged.

Examples
rearranged_difference(972882) ➞ 760833
# 988722 - 227889 = 760833

rearranged_difference(3320707) ➞ 7709823
# 7733200 - 23377 = 7709823

rearranged_difference(90010) ➞ 90981
# 91000 - 19 = 90981
"""






################################################################
"""
Solution 1
"""


def rearranged_difference(num):
	n = ''.join(sorted(str(num)))
	return int(n[::-1]) - int(n)




################################################################
"""
Solution 2
"""


def rearranged_difference(num):
	l1 = list(str(num))
	l1.sort()
	return int(''.join(l1[::-1]))- int(''.join(l1))


################################################################
"""
Solution 3
"""


def rearranged_difference(num):
    s = str(num)
    t = []
    for i in s:
        t.append(i)
    t.sort()
    s1 = "".join(t)
    t.sort(reverse=True)
    s2 = "".join(t)
    return int(s2)-int(s1)

print(rearranged_difference(123445))


################################################################
"""
Solution 4
"""


def rearranged_difference(a):
 s,d='',''
 for i in str(sorted([int(i) for i in str(a)])):
  if i.isdigit()==True:
   s+= i
 for i in str(sorted([int(i) for i in str(a)],reverse=True)):
  if i.isdigit()==True:
   d+= i
 return float(d)-float(s)



