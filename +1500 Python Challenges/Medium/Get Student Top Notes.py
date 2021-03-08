"""
Get Student Top Notes

Create a function that takes a list of student dictionaries and returns a list of their top notes. If the student does not have notes then let's assume their top note is equal to 0.

Examples
get_student_top_notes([
  {
    "id": 1,
    "name": "Jacek",
    "notes": [5, 3, 4, 2, 5, 5]
  },
  {
    "id": 2,
    "name": "Ewa",
    "notes": [2, 3, 3, 3, 2, 5]
  },
  {
    "id": 3,
    "name": "Zygmunt",
    "notes": [2, 2, 4, 4, 3, 3]
  }
]) ➞ [5, 5, 4]
"""



################################################################
"""
Solution 1
"""


def get_student_top_notes(students):
	return [max(i['notes'] + [0]) for i in students]



################################################################
"""
Solution 2
"""


def get_student_top_notes(students):
	
	top_notes = []
	
	for student in students:
		try:
			top_notes.append(max(student['notes']))
		except ValueError:
			top_notes.append(0)
	
	return top_notes


################################################################
"""
Solution 3
"""


def get_student_top_notes(students):
	return [
		max(d.get('notes')) 
		if d.get('notes') else 0 
		for d in students



#################################################################
"""
Solution 4
"""


def get_student_top_notes(students):
	return [max(i.get('notes')) if i.get('notes') else 0 for i in students]



