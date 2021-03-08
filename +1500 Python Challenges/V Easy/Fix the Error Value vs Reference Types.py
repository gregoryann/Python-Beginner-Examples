"""
Fix the Error: Value vs. Reference Types
Create a function that returns True if two lists contain identical values, and False otherwise.

To solve this question, your friend writes the following code:

def check_equals(lst1, lst2):
    if lst1 is lst2:
        return True
    else:
        return False
But testing the code, you see that something is not quite right. Running the code yields the following results:

check_equals([1, 2], [1, 3]) ➞ False
# Good so far...

check_equals([1, 2], [1, 2]) ➞ False
# Yikes! What happened?
Rewrite your friend's code so that it correctly checks if two lists are equal. The tests below should pass:

Examples
check_equals([1, 2], [1, 3]) ➞ False

check_equals([1, 2], [1, 2]) ➞ True

check_equals([4, 5, 6], [4, 5, 6]) ➞ True

check_equals([4, 7, 6], [4, 5, 6]) ➞ False
Notes
Hint: This has to do with value vs. reference types.

"""


"""
Solution 1
"""

def check_equals(lst1, lst2):
	return lst1 == lst2


"""
Solution 2
"""

# Fix this broken code!
def check_equals(lst1, lst2):
	if lst1 == lst2:
		return True
	else:
		return False




