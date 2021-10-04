from math import sqrt, pi

# Question 1
timeMinutes = eval(input("Please enter a time in minutes: "))
timeMilliseconds = timeMinutes * 60 * 1000

print(timeMinutes, "minutes is", timeMilliseconds, "milliseconds")
# 1 minutes is 60000 milliseconds
# 2 minutes is 120000 milliseconds
# 3 minutes is 180000 milliseconds

# Question 2
a, b, c = 1, 2, 1
delta = b**2 - (4 * a * c)

root1 = (-b + sqrt(delta)) / 2 * a
root2 = (-b - sqrt(delta)) / 2 * a

print("The roots are", root1, "and", root2)
# The roots are -1.0 and -1.0

# Question 3
midtermGrade = eval(input("Please input your midterm grade: "))
finalGrade = eval(input("Please input your final grade: "))

print("Your overall grade is", midtermGrade * 0.4 + finalGrade * 0.6)
# Please input your midterm grade: 0
# Please input your final grade: 0
# Your overall grade is 0.0

# Please input your midterm grade: 100
# Please input your final grade: 100
# Your overall grade is 100.0

# Please input your midterm grade: 0
# Please input your final grade: 100
# Your overall grade is 60.0

# Question 4
print(help("modules"))
print(help("tkinter"))
print(dir("tkinter"))
# Output too long but it should print out all of the modules and all of the functions and variables
# in the module called "tkinter" which is used to make GUIs

# Question 5
sideA = eval(input("Please input the first side of the triangle: "))
sideB = eval(input("Please input the second side of the triangle: "))
sideC = eval(input("Please input the third side of the triangle: "))

s = (sideA + sideB + sideC) / 2
areaTriangle = sqrt(s * (s - sideA) * (s - sideB) * (s - sideC))

print("The area of the triangle is", areaTriangle)
# Please input the first side of the triangle: 10
# Please input the second side of the triangle: 10
# Please input the third side of the triangle: 10
# The area of the triangle is 43.30127018922193

# NOTE: 14.1421356237 is roughly 10 * sqrt(2)
# This should be a right triangle so we expect an output like 50

# Please input the first side of the triangle: 10
# Please input the second side of the triangle: 10
# Please input the third side of the triangle: 14.1421356237
# The area of the triangle is 49.99999999999999

# We get very close to 50

# Question 6
sideN = eval(input("Please enter the side length of the cube: "))
marbleRadius = sideN / 4
cubeVolume = sideN**3
marbleVolume = (4 / 3) * pi * marbleRadius**3
howManyFit = cubeVolume // marbleVolume
print(howManyFit, "marbles fit inside a cube of side length", sideN)

# Please enter the side length of the cube: 10
# 15.0  marbles fit inside a cube of side length 10

# Please enter the side length of the cube: 12
# 15.0  marbles fit inside a cube of side length 12

# Please enter the side length of the cube: 120
# 15.0  marbles fit inside a cube of side length 120

# Question 7
celsius = eval(input("Please enter the temperature in celsius: "))
fahrenheit = (celsius * (9 / 5)) + 32
kelvin = celsius + 273.15
reamur = celsius * (4 / 5)
rankine = (celsius * (9 / 5)) + 491.67
print("Fahrenheit:", fahrenheit)
print("Kelvin:", kelvin)
print("Reamur:", reamur)
print("Rankine:", rankine)

# Please enter the temperature in celsius: 100
# Fahrenheit: 212.0
# Kelvin: 373.15
# Reamur: 80.0
# Rankine: 671.6700000000001
