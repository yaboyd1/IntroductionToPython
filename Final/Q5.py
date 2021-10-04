from math import sqrt, isclose
# isclose is used since we are comparing floating point numbers for equality
# print(help(isclose))

# Finds the distance between two points
def distance(x1, y1, x2, y2):
	return sqrt((x2 - x1)**2 + (y2 - y1)**2)

def isclose3(a, b, c):
	return isclose(a, b) and isclose(b, c) and isclose(a, c)

# Check if a triangle is an equalateral triange given 3 points
def isEqualateralTriangle(x1, y1, x2, y2, x3, y3):
	a = distance(x1, y1, x2, y2)
	b = distance(x2, y2, x3, y3)
	c = distance(x1, y1, x3, y3)
	# return a == b == c
	return isclose3(a, b, c)

# Check if a triangle is a right triange given 3 points
def isRightTriangle(x1, y1, x2, y2, x3, y3):
	a = distance(x1, y1, x2, y2)
	b = distance(x2, y2, x3, y3)
	c = distance(x1, y1, x3, y3)
	# return (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2)
	return isclose(a**2 + b**2, c**2) or isclose(a**2 + c**2, b**2) or isclose(b**2 + c**2, a**2)

# User Input
x1 = eval(input("Please enter X coordinate of the first point: "))
y1 = eval(input("Please enter Y coordinate of the first point: "))
x2 = eval(input("Please enter X coordinate of the second point: "))
y2 = eval(input("Please enter Y coordinate of the second point: "))
x3 = eval(input("Please enter X coordinate of the third point: "))
y3 = eval(input("Please enter Y coordinate of the third point: "))

# A triangle cannot be both a Right and Equalateral Triangle at the same time
if isRightTriangle(x1, y1, x2, y2, x3, y3):
	print("This is a Right Triangle!")
elif isEqualateralTriangle(x1, y1, x2, y2, x3, y3):
	print("This is an Equalateral Triangle!")
else:
	print("This is not a Right Triangle nor an Equalateral Triangle!")

# Sample Output

# Please enter X coordinate of the first point: 0
# Please enter Y coordinate of the first point: 0
# Please enter X coordinate of the second point: 1
# Please enter Y coordinate of the second point: 1
# Please enter X coordinate of the third point: 2
# Please enter Y coordinate of the third point: 2
# This is not a Right Triangle nor an Equalateral Triangle!

### Great our last case works as intended!

# Please enter X coordinate of the first point: 0
# Please enter Y coordinate of the first point: 0
# Please enter X coordinate of the second point: 10
# Please enter Y coordinate of the second point: 0
# Please enter X coordinate of the third point: 0
# Please enter Y coordinate of the third point: 10
# This is not a Right Triangle nor an Equalateral Triangle!

### Uh oh. This is odd. This should be a Right Triangle
### I think I know the issue. It has to do with floating point values
### We can use math.isclose() to compare floating point values together
### This is a simple change

# Please enter X coordinate of the first point: 0
# Please enter Y coordinate of the first point: 0
# Please enter X coordinate of the second point: 10
# Please enter Y coordinate of the second point: 0
# Please enter X coordinate of the third point: 0
# Please enter Y coordinate of the third point: 10
# This is a Right Triangle!

### Now our output is as we expect!

# Please enter X coordinate of the first point: -4
# Please enter Y coordinate of the first point: 0
# Please enter X coordinate of the second point: 4
# Please enter Y coordinate of the second point: 0
# Please enter X coordinate of the third point: 0
# Please enter Y coordinate of the third point: 6.928203230275509
# This is an Equalateral Triangle!

### This makes sense! Why?
### 4 * sqrt(3) is roughly 6.928203230275509 
### Thus isEqualateralTriangle(-4, 0, 4, 0, 0, 4 * sqrt(3)) should return True
### and send the message to the user
