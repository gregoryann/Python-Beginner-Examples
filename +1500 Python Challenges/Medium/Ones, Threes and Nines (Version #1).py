"""
Ones, Threes and Nines (Version #1)

Given an int, figure out how many ones, threes and nines you could fit into the number. You must create a class. You will make variables(self.ones, self.threes, self.nines) to do this.

Examples
n1 = ones_threes_nines(5)
n1.nines ➞ 0

n1.ones ➞ 5

n1.threes ➞ 1

Notes
Do not use the math module.
No need to create objects of the class.
See version #2 of this series.
"""





################################################################
"""
Solution 1
"""


class ones_threes_nines:
	
	def __init__(self, n):
		self.ones = n
		self.threes = n // 3
		self.nines = n // 9



################################################################
"""
Solution 2
"""


class ones_threes_nines:
	def __init__(self, arg):
		self.arg = arg
		self.nines = int(self.arg / 9)
		self.threes = int(self.arg / 3)
		self.ones = int(self.arg / 1)



################################################################
"""
Solution 3
"""

class ones_threes_nines:
      def __init__(self, n ):
          self.ones = n //1
          self.threes = n//3
          self.nines = n//9
      def one(self):
          return self.ones
      def three(self):
          return self.threes
      def nine(self):
          return self.nines





