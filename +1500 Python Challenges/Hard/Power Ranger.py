"""
Power Ranger

Create a function that takes in n, a, b and returns the number of positive values raised to the nth power that lie in the range [a, b], inclusive.

Examples
power_ranger(2, 49, 65) ➞ 2
# 2 squares (n^2) lie between 49 and 65, 49 (7^2) and 64 (8^2)

power_ranger(3, 1, 27) ➞ 3
# 3 cubes (n^3) lie between 1 and 27, 1 (1^3), 8 (2^3) and 27 (3^3)

power_ranger(10, 1, 5) ➞ 1
# 1 value raised to the 10th power lies between 1 and 5, 1 (1^10)

power_ranger(5, 31, 33) ➞ 1

power_ranger(4, 250, 1300) ➞ 3


Notes
Remember that the range is inclusive.
a < b will always be true.
"""




################################################################
"""
Solution 1
"""


def power_ranger(power, minimum, maximum):
	return sum(i**(1/power)%1==0 for i in range(minimum,maximum+1))



################################################################
"""
Solution 2
"""


def power_ranger(power, minimum, maximum):
	
	lst = [1,2,3,4,5,6,7,8,9,10]
	a = 0
	counter = 0
	for num in lst:
		a = num ** power
		if (a >= minimum) and (a <= maximum):
			counter += 1
		elif a < minimum:
			continue
		elif a > maximum:
			break
	return counter



################################################################
"""
Solution 3
"""


def power_ranger(power, minimum, maximum):
  square = []
  square_list = []
  for number in range(0,maximum+1):
    square = number**power
    if square in range(minimum,maximum+1):
      square_list.append(square)
  print(square_list)
  return(len(square_list))



################################################################
"""
Solution 4
"""


import math
def power_ranger(power, minimum, maximum):
    result = 0
    for i in range(math.ceil(minimum**(1/power)), math.ceil(maximum**(1/power))+1):
        if i**power >= minimum and i**power <= maximum:
            result+=1
    return result




################################################################
"""
Solution 5
"""


def power_ranger(power, minimum, maximum):
	cnt=0
	for num in range(minimum,maximum+1):
		res=num**(1/power)
		if (res).is_integer():
			cnt+=1
	return cnt