"""
Get the File Name
Create a function that returns the selected filename from a path. Include the extension in your answer.

Examples
get_filename("C:/Projects/pil_tests/ascii/edabit.txt") ➞ "edabit.txt"

get_filename("C:/Users/johnsmith/Music/Beethoven_5.mp3") ➞ "Beethoven_5.mp3"

get_filename("ffprobe.exe") ➞ "ffprobe.exe"
Notes
Tests will include both absolute and relative paths.
For simplicity, all paths will include forward slashes.

"""




"""
Solution 1
"""

def get_filename(path):
	return path.split('/')[-1]

"""
Solution 2
"""

from pathlib import PurePath

def get_filename(path):
	return PurePath(path).name

"""
Solution 3
"""

get_filename = lambda p: p.split('/')[-1]

"""
Solution 4
"""

def get_filename(path):
	return path if '/' not in path else path.split('/')[-1]


"""
Solution 5
"""

def get_filename(path):
	path_arr = path.split("/")
	return path_arr[len(path_arr) - 1]





