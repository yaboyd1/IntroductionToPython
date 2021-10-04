from random import random

# User inputs a size n
n = int(input("Please enter the table size: "))

# Initialize the table based on the user's size
Table1 = [0] * n
Table2 = [0] * n

# Distrubutes random probability values that add up to 1 for a given table of length n
def randomize(table):
	sum = 0
	for i in range(n):
		random_number = random()
		table[i] = random_number
		sum += random_number
	return [i / sum for i in table]

# Randomize and print the tables for the user
Table1 = randomize(Table1)
Table2 = randomize(Table2)
print("Table 1:", Table1)
print("Table 2:", Table2)
print("Table 1 Sum:", sum(Table1))
print("Table 2 Sum:", sum(Table2))

# Sample Outputs:

# Please enter the table size: 3
# Table 1: [0.5762427339924909, 0.02861057135726544, 0.39514669465024366]
# Table 2: [0.5068558543303735, 0.3022426238088224, 0.19090152186080417]
# Table 1 Sum: 1.0
# Table 2 Sum: 1.0

# Please enter the table size: 5
# Table 1: [0.24312286354053478, 0.22227007962416703, 0.11455888289548558, 0.22927072180039976, 0.19077745213941288]
# Table 2: [0.23113203025055395, 0.3146378074628352, 0.027477967623847594, 0.19769268351413635, 0.2290595111486269]
# Table 1 Sum: 1.0
# Table 2 Sum: 1.0
