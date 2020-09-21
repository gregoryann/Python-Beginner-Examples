"""
Typing Game

You're in the midst of creating a typing game.

Create a function that takes in two lists: the list of user-typed words, and the list of correctly-typed words and outputs a list containing 1s (correctly-typed words) and -1s (incorrectly-typed words).

# Inputs:
User-typed: ["cat", "blue", "skt", "umbrells", "paddy"]
Correct: ["cat", "blue", "sky", "umbrella", "paddy"]

# Output: [1, 1, -1, -1, 1]
Examples
correct_stream(
  ["it", "is", "find"],
  ["it", "is", "fine"]
) ➞ [1, 1, -1]

correct_stream(
  ["april", "showrs", "bring", "may", "flowers"],
  ["april", "showers", "bring", "may", "flowers"]
) ➞ [1, -1, 1, 1, 1]

Notes
The input list lengths will always be the same.
"""



"""
Solution 1
"""

def correct_stream(user, correct):
	return [1 if user[i] == correct[i] else -1 for i in range(len(user))]

"""
Solution 2
"""

def correct_stream(user, correct):

    return [1 if typed == expected else -1
            for typed, expected in zip(user, correct)]

"""
Solution 3
"""

def correct_stream(user, correct):
	mylist = []
	for x,y in zip(user,correct):
		if x == y:
			mylist.append(1)
		else:
			mylist.append(-1)
	return mylist








