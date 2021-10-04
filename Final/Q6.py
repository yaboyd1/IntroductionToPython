from random import randint

A_row, A_col, B_row, B_col = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)

A = [[randint(1, 10) for col in range(A_col)] for row in range(A_row)]
A = [[randint(1, 10) for col in range(B_col)] for row in range(B_row)]

if A_col == B_row:
	print("These two matrices are allowed to be multiplied!")
	print("AxB = {}x{} * {}x{}".format(A_row, A_col, B_row, B_col))
elif B_col == A_row:
	print("These two matrices are allowed to be multiplied!")
	print("BxA = {}x{} * {}x{}".format(B_row, B_col, A_row, A_col))
else:
	print("These two matrices cannot be multiplied :(")
	print("A: {}x{}".format(A_row, A_col))
	print("B: {}x{}".format(B_row, B_col))

### Sample Outputs:
### Each output demonstrates each case from the statement above respectively^^^

# These two matrices are allowed to be multiplied!
# AxB = 7x5 * 5x10

# These two matrices are allowed to be multiplied!
# BxA = 5x5 * 5x9

# These two matrices cannot be multiplied :(
# A: 10x6
# B: 4x2
