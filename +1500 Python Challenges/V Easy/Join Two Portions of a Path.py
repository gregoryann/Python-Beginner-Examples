"""

Join Two Portions of a Path
Write a function that receives two portions of a path and joins them. The portions will be joined with the "/" separator. There could be only one separator and if it is not present it should be added.

Examples
join_path("portion1", "portion2") ➞ "portion1/portion2"
join_path("portion1/", "portion2") ➞ "portion1/portion2"
join_path("portion1", "/portion2") ➞ "portion1/portion2"
join_path("portion1/", "/portion2") ➞ "portion1/portion2"

Notes
Try not to solve this challenge using only if-else conditions.

"""



"""
Solution 1
"""

def join_path(portion1, portion2):
	return '/'.join((portion1.rstrip('/'), portion2.lstrip('/')))

"""
Solution 2
"""

def join_path(portion1, portion2):
  return "".join([p for p in portion1 if p != "/"] + ["/"] + [p for p in portion2 if p != "/"])




