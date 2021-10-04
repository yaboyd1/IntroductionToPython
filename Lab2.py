from math import sqrt
# This import is used in Question 3 to find the distance between two points

# Question 1
# (15 points)  In number theory, a perfect number is a positive integer that is equal to the
# sum of its proper positive divisors, that is, the sum of its positive divisors excluding itself
# (also known as its aliquot sum).  In other words, a perfect number is a number that is half of
# the sum of all its positive divisors (including itself).  Write a Python3 program to check if a
# user-entered number is a perfect number or not.  Use exception handling to catch and handle invalid
# inputs.  Your program needs to run until the user decides to quit.

def isPerfectNumber(n):
    if n < 0:
        return False
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    if sum == n:
        return True
    return False

def isPerfectNumberTest():
    userInput = input("Please input a positive integer (Enter to quit): ")
    while userInput != "":
        try:
            n = int(userInput)
            if n > 0:
                print(n, "is a perfect number!") if isPerfectNumber(n) else print(n, "is not a perfect number")
            else:
                print("Invalid Input!")
        except:
            print("Invalid Input!")
        userInput = input("Please input a positive integer (Enter to quit): ")

isPerfectNumberTest()

# Please input a positive integer (Enter to quit): 0
# Invalid Input!
# Please input a positive integer (Enter to quit): -10
# Invalid Input!
# Please input a positive integer (Enter to quit): 1.5
# Invalid Input!
# Please input a positive integer (Enter to quit): Hello World!
# Invalid Input!
# Please input a positive integer (Enter to quit): 10
# 10 is not a perfect number
# Please input a positive integer (Enter to quit): 6
# 6 is a perfect number!
# Please input a positive integer (Enter to quit):

# As you can see, this program handles invalid inputs and prompts the user for another number
# 10 is not a perfect while 6 which is to be expected
# The user must press Enter or enter nothing if they want to quit which also works as you can see from the last input


# Question 2
# (15 points)  Write a Python3 program to find all prime numbers between 2 integer num-bers (both inclusive)
# entered by the user.  Print all the prime numbers in between both on  screen  and  to  an  output  file
# named  ’primes.txt’  that  needs  to  be  created  with  a compound statement of Python3.

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def findPrimesBetween(start, end):
    with open("primes.txt", "w") as f:
        for i in range(start, end + 1):
            if isPrime(i):
                print(i)
                print(i, file=f)

def findPrimesBetweenTest():
    start = int(input("Please input the start of the range (inclusive): "))
    end = int(input("Please input the end of the range (inclusive): "))
    findPrimesBetween(start, end)

findPrimesBetweenTest()

# Please input the start of the range (inclusive): 1
# Please input the end of the range (inclusive): 10
# 2
# 3
# 5
# 7

# 1 is not a prime number so this output correctly displays the prime numbers between 1 and 10 (inclusive)
# Please check out primes.txt which has the same output


# Question 3
# 15 points) Write a Python3 program to check if 3 user entered points on the coordinate
# plane creates a triangle or not. Your program needs to repeat until the user decides to
# quit, and needs to deal with invalid inputs.

def distance(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def isValidTriangle(a, b, c):
    return b + c > a and a + c > b and a + b > c

def isValidTriangleTest():
    userInput = "y"
    while userInput[0] == "Y" or userInput[0] == "y":
        try:
            x1 = eval(input("Please enter x coordinate of first point: "))
            y1 = eval(input("Please enter y coordinate of first point: "))
            x2 = eval(input("Please enter x coordinate of second point: "))
            y2 = eval(input("Please enter y coordinate of second point: "))
            x3 = eval(input("Please enter x coordinate of third point: "))
            y3 = eval(input("Please enter y coordinate of third point: "))

            a = distance(x1, y1, x2, y2)
            b = distance(x2, y2, x3, y3)
            c = distance(x1, y1, x3, y3)
            print("Valid Triangle!") if isValidTriangle(a, b, c) else print("Invalid Triangle!")
        except:
            print("Invalid Input! Please enter a number")
        userInput = input("Would you like to continue? (Y or N): ")

isValidTriangleTest()

# Please enter x coordinate of first point: 0
# Please enter y coordinate of first point: 0
# Please enter x coordinate of second point: 0
# Please enter y coordinate of second point: 3
# Please enter x coordinate of third point: 4
# Please enter y coordinate of third point: 0
# Valid Triangle!
# Would you like to continue? (Y or N): Y
# Please enter x coordinate of first point: 0
# Please enter y coordinate of first point: 0
# Please enter x coordinate of second point: 1
# Please enter y coordinate of second point: 1
# Please enter x coordinate of third point: 2
# Please enter y coordinate of third point: 2
# Invalid Triangle!
# Would you like to continue? (Y or N): N

# The first input included the coordinates of the 3 4 5 Triangle, which we know is a valid triangle
# The second input was a straight line which is not a valid triangle
# Our program determined this correctly

# Please enter x coordinate of first point: Hello World!
# Invalid Input! Please input a number
# Would you like to continue? (Y or N): N

# The program asks the user if they would like to continue even if there is an error


# Question 4
# (15 points) Open the file (quotes.txt) given below using Python3. Design a function to
# get the file object as a parameter, and get rid of every extra new line and save the result
# in a new file named quotes.txt. In file quotes.txt, there has to be only a single new
# line character after each name.

def removeNewLines(file):
    file.seek(0)
    with open("quotes2.txt", "w") as f:
        for line in file:
            if line != "\n":
                f.write(line)

def removeNewLinesTest():
    with open("quotes.txt", "r") as f:
        removeNewLines(f)

removeNewLinesTest()

# quotes.txt contains various quotes be Albert Einstein followed by 3 new line characters
# Not that even the last quote has 3 new line characters after the name

# quotes2.txt removes the excess new line characters so that there is only 1 new line character after the name
# Note that the last line is also allowed 1 new line character

# Please see quotes.txt and quotes2.txt for a better understanding


# Question 5
# (15 points) Design a Python3 function that takes in a file object as its parameter, read
# the contents of the file by using read() method only, if the number of lines is a prime
# number, clear all the new line characters. And write it back to the same file. If the
# number of lines is not a prime number then, remove the new line character and a tab
# space instead and write it back to the same file.

def primeReplaceLines(file):
    file.seek(0)
    text = file.read()
    file.seek(0)
    file.truncate(0)
    file.write(text.replace("\n", "" if isPrime(text.count("\n")) else "\t"))

def primeReplaceLinesTest():
    with open("primeNumberOfLines.txt", "r+") as f:
        primeReplaceLines(f)
    with open("notPrimeNumberOfLines.txt", "r+") as f:
        primeReplaceLines(f)

primeReplaceLinesTest()

# Originally, primeNumbersOfLines.txt had the following text:
# 0
# 1
# 2
# 3
# 4
# 5
# You can view this as "0\n1\n2\n3\n4\n5" where there are 5 (not prime) new line characters
# After the function is called, the text looks like this:
# 12345
# Thus, this works correctly when there are a prime number of lines

# Originally, notPrimeNumberOfLines.txt had the following text:
# 0
# 1
# 2
# 3
# 4
# You can view this as "0\n1\n2\n3\n4" where are are 4 (not prime) new line characters
# After the function is called, the text looks like this:
# 0    1    2    3    4
# You can view this as "0\t1\t2\t4"
# Thus, this works correctly when there are a prime number of lines


# Question 6
# (15 points) Write a Python3 function that works with any string A of length greater
# than user-defined k, and prints the string then trims one character from the end of the
# string at a time and prints it again until there are k characters are left. A sample output
# is given below when A='Greetings' and k = 3:

def trimStringRecursive(string, length):
    if len(string) <= length:
        print(string)
    else:
        print(string)
        trimStringRecursive(string[:-1], length)

def trimStringIterative(string, length):
    for i in range(len(string), length - 1, -1):
        print(string[:i])

# trimStringRecursive("Greetings", 3)
# trimStringIterative("Greetings", 3)

# Both return the same output of:
# Greetings
# Greeting
# Greetin
# Greeti
# Greet
# Gree
# Gre

def trimStringTest():
    string = input("Please enter a string to trim (A): ")
    length = int(input("Please enter how many characters you want left (k): "))
    trimStringIterative(string, length)

trimStringTest()

# Please enter a string to trim (A): Greetings
# Please enter how many characters you want left (k): 3
# Greetings
# Greeting
# Greetin
# Greeti
# Greet
# Gree
# Gre
