"""
Get Students with Names and Top Notes

Create a function that takes a dictionary of objects like { "name": 'John', "notes": [3, 5, 4]} and returns a dictionary of objects like { "name": "John", " top_note": 5 }.

Examples
top_note({ "name": "John", "notes": [3, 5, 4] }): ➞ { "name": "John", "top_note": 5 }

top_note({ "name": "Max", "notes": [1, 4, 6] }): ➞ { "name": "Max", "top_note": 6 }

top_note({ "name": "Zygmund", "notes":[1, 2, 3] }) ➞ {"name": "Zygmund", "top_note":3 }
"""



################################################################
"""
Solution 1
"""


def top_note(student):
	student["top_note"] = max(student["notes"])
	student.pop("notes")
	return student



################################################################
"""
Solution 2
"""


top_note=lambda s:{'name':s['name'],'top_note':max(s['notes'])}



################################################################
"""
Solution 3
"""


def top_note(student):
	newDict = {}
	newDict['name'] = student.get('name')
	newDict['top_note'] = max(student.get('notes'))
	return newDict



#################################################################
"""
Solution 4
"""


def top_note(student):
	student.update({'top_note': max(student.pop('notes'))})
	return student



