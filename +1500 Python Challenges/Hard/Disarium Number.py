"""
Disarium Number

A number is said to be Disarium if the sum of its digits raised to their respective positions is the number itself.

Create a function that determines whether a number is a Disarium or not.

Examples
is_disarium(75) ➞ False
# 7^1 + 5^2 = 7 + 25 = 32

is_disarium(135) ➞ True
# 1^1 + 3^2 + 5^3 = 1 + 9 + 125 = 135

is_disarium(518) ➞ True

is_disarium(8) ➞ True


Notes
Position of the digit is 1-indexed.
A recursive version of this challenge can be found via this link.
"""




################################################################
"""
Solution 1
"""


def is_disarium(n):
    r = 0
    for i in range(len(str(n))):
        r += int(str(n)[i]) ** (i + 1)
    return r == n



################################################################
"""
Solution 2
"""


def is_disarium(n):
	s = 0
	for i in str(n):
		s += int(i)**(str(n).index(i) + 1)
	return s == n



################################################################
"""
Solution 3
"""


def is_disarium(n):
	list1 = []
	a = 1
	total = 0
	for i in str(n):
		list1.append(int(i))
	for i in list1:
		total += i**a
		a+=1
	return total == int(n)


################################################################
"""
Solution 4
"""


def is_disarium(number):
	
	# Local variables 
	position = 0
	product = 1
	sum = 0
	
	# Turn number into string and store in variable 
	number = str(number)
	
	# Loop through the number 
	for digit in number:
		# Increase value of position by one 
		position += 1
		
		# Get the number and turn to integer 
		digit = int(digit)
		
		# Loop from 0 to position 
		for i in range(0, position):
			# Get the product and store in variable 
			product *= digit
		
		# Sum up the product
		sum += product 
		
		# Reset the value of product to one 
		product = 1
	
	# Turn number back to integer 
	number = int(number)
	
	# Check if sum equals number 
	if sum == number:
		# Return true 
		return True
	
	# Return false 
	return False



################################################################
"""
Solution 5
"""


def is_disarium(n):
    sum = 0
    digits_lst = []
    digit_dict = dict()
    for i in str(n):
        digits_lst.append(i.split())
    for j in range(len(digits_lst)):
        for k in range(len(digits_lst[j])):
            digit_dict[j + 1] = int(digits_lst[j][k])
    for key, value in digit_dict.items():
        sum += value ** key
    if sum == n :
        return True
    return False    
    
print(is_disarium(518))