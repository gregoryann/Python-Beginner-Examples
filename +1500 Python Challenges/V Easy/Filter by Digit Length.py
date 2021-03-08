"""
Filter by Digit Length
Create a function that filters out a list to include numbers which only have a certain number of digits.

Examples
filter_digit_length([88, 232, 4, 9721, 555], 3) ➞ [232, 555]
# Include only numbers with 3 digits.

filter_digit_length([2, 7, 8, 9, 1012], 1) ➞ [2, 7, 8, 9]
# Include only numbers with 1 digit.

filter_digit_length([32, 88, 74, 91, 300, 4050], 1) ➞ []
# No numbers with only 1 digit exist => return empty list.

filter_digit_length([5, 6, 8, 9], 1) ➞ [5, 6, 8, 9]
# All numbers in the list have 1 digit only => return original list.
Notes
If no numbers of the specified digit length exist, return an empty list.
If all numbers in the list have the specified digit length, return original list.
The sub-list returned should have the same relative order as the original list.

"""


"""
Solution 1
"""

def filter_digit_length(lst, num):
    return [number for number in lst if len(str(number)) == num]

"""
Solution 2
"""

def filter_digit_length(lst, num):
	return list(filter(lambda x: len(str(x))==num, lst))

"""
Solution 3
"""

def filter_digit_length(lst, num):
	temp = []
	for item in lst:
		if len(str(item)) == num:
			temp.append(item)
	return temp

"""
Solution 4
"""

def filter_digit_length(lst, num):
	new_list = []
	for item in lst:
	  if len(str(item)) == num:
		  new_list.append(item)
	return new_list

"""
Solution 5

"""

def filter_digit_length(lst,num):
    l = []
    for x in lst:
        if (len(str(abs(x))))== num:
            l.append(x)
    return(l)




