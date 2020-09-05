"""

Get the File Extension
Write a function that maps files to their extension names.

Examples
get_extension(["code.html", "code.css"])
➞ ["html", "css"]

get_extension(["project1.jpg", "project1.pdf", "project1.mp3"])
➞ ["jpg", "pdf", "mp3"]

get_extension(["ruby.rb", "cplusplus.cpp", "python.py", "javascript.js"])
➞ ["rb", "cpp", "py", "js"]

"""


"""
Solution 1
"""

def get_extension(lst):
	return [i.split(".")[1] for i in lst]

"""
Solution 2
"""

def get_extension(lst):
	return [ch[ch.index('.')+1:] for ch in lst];

"""
Solution 3
"""

def get_extension(lst):
		ext = []
		for i in lst:
				ext.append(i.split('.')[1])
		return ext

"""
Solution 4
"""

from pathlib import Path
def get_extension(lst):
	a = []
	for i in lst:
		a.append(Path(i).suffix)
	return [i.strip('.') for i in a]




