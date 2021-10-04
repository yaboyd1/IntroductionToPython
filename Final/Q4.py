from random import randint

# Custom Matrix Class
class Matrix:
	# Takes in number of rows and columns as the constructor
	def __init__(self, row=0, col=0):
		self.row = row
		self.col = col
		self.matrix = [[randint(0, 9) for c in range(col)] for r in range(row)]

	# So that print(Matrix) works nicely
	def __str__(self):
		return "\n".join([" ".join(str(elm) for elm in row) for row in self.matrix])

	# Rotates the matrix once clockwise
	def rotateClockwise(self):
		new = [[None for row in range(self.row)] for col in range(self.col)]

		for i in range(self.row):
			for j in range(self.col):
				new[j][self.row - 1 - i] = self.matrix[i][j]

		self.matrix, self.row, self.col = new, self.col, self.row

	# Rotates the matrix n times clockwise (if negative, goes anti-clockwise)
	def rotateClockwiseNTimes(self, n):
		n = n % 4
		for i in range(n):
			self.rotateClockwise()

# Can change the amount of rows or columns of the matrix here
A = Matrix(2, 5)
print("A has {} rows and {} columns initially:".format(A.row, A.col), A, sep="\n")

print("Rotating A clockwise 4 times (should be the same matrix): ")
A.rotateClockwiseNTimes(4)
print(A)

print("Rotating A anti-clockwise 4 times (should be the same matrix): ")
A.rotateClockwiseNTimes(4)
print(A)

print("Rotating A clockwise 1 time: ")
A.rotateClockwiseNTimes(1)
print(A)
A.rotateClockwiseNTimes(3) # Back to initial state

print("Rotating A anti-clockwise 3 times (should be the same as matrix above):")
A.rotateClockwiseNTimes(-3)
print(A)
A.rotateClockwiseNTimes(-1) # Back to initial state

print("Rotating A clockwise 2 times: ")
A.rotateClockwiseNTimes(2)
print(A)
A.rotateClockwiseNTimes(2) # Back to initial state

print("Rotating A anti-clockwise 2 times (should be the same as matrix above):")
A.rotateClockwiseNTimes(-2)
print(A)
A.rotateClockwiseNTimes(-2) # Back to initial state

print("Rotating A clockwise 6 times (should be the same as 2 matrices above):")
A.rotateClockwiseNTimes(6)
print(A)

# This works for negative numbers! See for yourself
# Output:

# A has 2 rows and 5 columns initially:
# 9 6 2 8 9
# 0 8 9 0 7
# Rotating A clockwise 4 times (should be the same matrix): 
# 9 6 2 8 9
# 0 8 9 0 7
# Rotating A anti-clockwise 4 times (should be the same matrix): 
# 9 6 2 8 9
# 0 8 9 0 7
# Rotating A clockwise 1 time: 
# 0 9
# 8 6
# 9 2
# 0 8
# 7 9
# Rotating A anti-clockwise 3 times (should be the same as matrix above):
# 0 9
# 8 6
# 9 2
# 0 8
# 7 9
# Rotating A clockwise 2 times: 
# 7 0 9 8 0
# 9 8 2 6 9
# Rotating A anti-clockwise 2 times (should be the same as matrix above):
# 7 0 9 8 0
# 9 8 2 6 9
# Rotating A clockwise 6 times (should be the same as 2 matrices above):
# 7 0 9 8 0
# 9 8 2 6 9
