''' How to prevent from opening a file by user in e.g. in .pdf format during code execution? My code is opening/saving multiple files in a loop and opening a new one may lead to an error. The OS is Windows.

Solution

Make it a function for opening file

Check the extension if extension is allowed then

read

else return or can raise custom exception
'''

from os import path

def open_conditional_file(file_name):
  ignore_extensions = [".pdf", ".jpg"]
  extensions = path.splitext(file_name)[1]
  if extensions in ignore_extensions:
    return # or you can also raise a custom exception here
  else:
    with open(file_name, "r") as f:
      #do the file operations here
      return # or return with the results here



''' Explanations

1. os.path.splitext() - https://docs.python.org/3/library/os.path.html#os.path.splitext

Split the pathname path into a pair (root, ext) such that root + ext == path, and ext is empty or begins with a period and contains at most one period. Leading periods on the basename are ignored; splitext('.cshrc') returns ('.cshrc', '').

2. https://pymotw.com/2/ospath/

splitext() works like split() but divides the path on the extension separator, rather than the directory separator.

splitext(For '/path/to/filename.txt') will return ('/path/to/filename', '.txt')

 '''