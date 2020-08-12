"""
This script creates an empty file.
"""
import imp
filename = "sample1.txt"

# Create empty file


def create_file():
    """This functions creates an empty file"""
    with open(filename, "w") as file:
        file.write("")  # writing empty string


imp.reload(example)
example.__doc__