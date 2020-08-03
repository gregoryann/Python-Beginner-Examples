"""


Frames Per Second
Create a function that returns the number of frames shown in a given number of minutes for a certain FPS.

Examples
frames(1, 1) ➞ 60

frames(10, 1) ➞ 600

frames(10, 25) ➞ 15000
Notes
FPS stands for "frames per second" and it's the number of frames a computer screen shows every second.
Assume the screen produces 60 frames every second.

"""






"""
Solution 1
"""


def frames(minutes, fps):
    return minutes * fps * 60




"""
Solution 2
"""


def frames(m, f): return m * 60 * f


"""
Solution 3
"""


def frames(minutes, fps):
	total_frames = (minutes*60) * fps
	return (total_frames)


"""
Solution 4
"""






