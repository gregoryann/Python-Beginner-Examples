"""
CMS Selector Based on a Given String

Create a function that takes a list and a string as arguments and returns the list of CMSs that include the given string. Return the names in a list in alphabetical order.

Examples
cms_selector(["WordPress", "Joomla", "Drupal"], "w") ➞ ["WordPress"]

cms_selector(["WordPress", "Joomla", "Drupal", "Magento"], "ru") ➞ ["Drupal"]

cms_selector(["WordPress", "Joomla", "Drupal", "Magento"], "") ➞ ["Drupal", "Joomla", "Magento", "WordPress"]

Notes
The given letter(s) are case insensitive and can be more than one.
In the case of an empty string, return the entire list.
A CMS is a Content Management System.
"""



########################################################################




"""
Solution 1
"""

def cms_selector(lst, txt):
	return sorted(i for i in lst if txt in i)

"""
Solution 2
"""

def cms_selector(lst, txt):
	lst2 = []
	for i in range(0, len(lst)):
		if txt in lst[i]:
			lst2.append(lst[i])
	return sorted(lst2)

"""
Solution 3
"""

cms_selector = lambda r, s: sorted(filter(lambda x: s in x, r))

"""
Solution 4
"""

def cms_selector(lst, letter):
	res = [] 
	for x in [m for m in lst]:
		if letter.lower() in x or letter.upper() in x:
			res.append(x)
	return sorted(res)



