"""
ATM PIN Code Validation

ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits. Your task is to create a function that takes a string and returns True if the PIN is valid and False if it's not.

Examples
is_valid_PIN("1234") ➞ True

is_valid_PIN("12345") ➞ False

is_valid_PIN("a234") ➞ False

is_valid_PIN("") ➞ False

Notes
Some test cases contain special characters.
Empty strings must return False
"""


"""
Solution 1
"""

def is_valid_PIN(pin):
	return len(pin) in [4, 6] and pin.isdigit()

"""
Solution 2
"""

def is_valid_PIN(pin):
	return (len(pin) == 4 or len(pin) == 6) and pin.isdigit()


"""
Solution 3
"""

def is_valid_PIN(pin):
  return bool(re.match('^(?:\d{4}|\d{6})$', pin))






