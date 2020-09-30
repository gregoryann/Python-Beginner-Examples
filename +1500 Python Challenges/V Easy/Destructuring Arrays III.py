"""
Destructuring Arrays III

You can assign variables from arrays with destructuring like this:

arr = ["eyes", "nose", "lips", "ears"]
head, *middle, tail = arr

print(head)    # "eyes"
print(middle)  # ["nose", "lips"]
print(tail)    # "ears"

Notes
Check the Resources tab for more examples.
"""


"""
Solution 1
"""

# DO NOT change arr
# "eyes", "nose", and "ears" should not be assigned to anything

arr = ["eyes", "nose", "lips", "ears"]
#Create variable lips here and assign it to arr[2]
eyes, nose, lips, ears = arr
arr[2] = lips






