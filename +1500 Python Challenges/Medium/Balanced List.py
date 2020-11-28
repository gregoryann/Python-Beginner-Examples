"""
Balanced List

Given a list of even length, copy the half with the higher sum of numbers to the other half of the list. If the sum of the first half equals the sum of the second half, return the original list.

Examples
balanced([1, 2, 4, 6, 3, 1]) ➞ [6, 3, 1, 6, 3, 1]
# 1 + 2 + 4 < 6 + 3 + 1 sol = [6, 3, 1, 6, 3, 1]

balanced([88, 3, 27, 5, 9, 0, 13, 10]) ➞ [88, 3, 27, 5, 88, 3, 27, 5]
# 88 + 3 + 27 + 5 > 9 + 0 + 13 + 10  sol = [88, 3 ,27 ,5 ,88 ,3 ,27 ,5]

balanced([7, 5, 2, 6, 1, 0, 1, 5, 2, 7, 0, 6]) ➞ [7, 5, 2, 6, 1, 0, 1, 5, 2, 7, 0, 6]
# 7 + 5 + 2 + 6 + 1 + 0 = 1 + 5 + 2 + 7 + 0 + 6 sol =  [7, 5, 2, 6, 1, 0, 1, 5, 2, 7, 0, 6]

Notes
The length of the list is even.
"""



################################################################
"""
Solution 1
"""


def balanced(lst):
		h1, h2 = sorted((lst[:len(lst)//2], lst[len(lst)//2:]), key=sum)
		return lst if sum(h1) == sum(h2) else h2*2



################################################################
"""
Solution 2
"""


def balanced(lst):
 half1=lst[0:int(len(lst)/2)]
 sum1=0
 for i in range(0,len(half1)):
  sum1+=half1[i]
 half2=lst[int(len(lst)/2):len(lst)]
 sum2=0
 for k in range(0,len(half2)):
  sum2+=half2[k]
 # print('half1',half1)
 # print('sum1',sum1)
 # print('half2',half2)
 # print('sum2',sum2)
 output=[]
 if sum1 > sum2:
  output.extend(half1)
  output.extend(half1)
 elif sum1 < sum2:
  output.extend(half2)
  output.extend(half2)
 else:
  output.extend(lst)
 return output



################################################################
"""
Solution 3
"""


def balanced(lst):
	f=lst[:len(lst)//2]
	l=lst[-len(lst)//2:]
	if sum(f)==sum(l): return lst
	if sum(f)>sum(l): return f+f
	return l+l



