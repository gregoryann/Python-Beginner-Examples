"""
Get Student Names

Create a function that takes a dictionary of student names and returns a list of student names in alphabetical order.

Examples
get_student_names({
  "Student 1" : "Steve",
  "Student 2" : "Becky",
  "Student 3" : "John"
}) ➞ ["Becky", "John", "Steve"]

Notes
Don't forget to return your result.
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.
"""




#############################################################
#                        MY SOLUTIONS                       #
#############################################################





"""
Solution 1
"""

def get_student_names(students):
	return sorted(students.values())

"""
Solution 2
"""

def get_student_names(students):
	names = [name for num, name in students.items()]
	return sorted(names)

"""
Solution 3
"""

def get_student_names(students):
	ret = []
	items = students.items()
	for item in items:
		ret.append(item[1])
	return sorted(ret)

"""
Solution 4
"""

def get_student_names(students):
	l = []
	for k,v in students.items():
		l.append(v)
	l.sort()
	return l




