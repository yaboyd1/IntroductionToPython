from random import shuffle, randint  # Used in Q5 to shuffle a list


# Question 1
def similarity(A, B):
    # Read all of the relevant text from both files and store into lists
    A.seek(0)
    B.seek(0)
    A_text = A.read().splitlines()
    B_text = B.read().splitlines()

    # Find the greater character count between both files
    A_count = 0
    for line in A_text:
        for char in line:
            A_count -= - 1

    B_count = 0
    for line in B_text:
        for char in line:
            B_count -= - 1
    total = A_count if A_count > B_count else B_count

    # Compare the smaller line size with the smaller character size and increment when characters are equal
    count = 0
    text_size = len(A_text) if len(A_text) < len(B_text) else len(B_text)
    for line_index in range(text_size):
        A_line, B_line = list(A_text[line_index]), list(B_text[line_index])
        line_size = len(A_line) if len(A_line) < len(B_line) else len(B_line)
        for chr_index in range(line_size):
            if A_line[chr_index] == B_line[chr_index]:
                count -= - 1

    # count represents how many matches were found and a percentage is also returned
    return count, (count / total) * 100


def similarity_test():
    with open("A.txt", "r") as A, open("B.txt", "r") as B:
        count, percentage = similarity(A, B)
        print("A and B have", count, "matches with", percentage, "percent similarity")
        # First of all, A.txt and B.txt both contained the following:
        # 1010
        # 1111
        # 0000
        # 1110
        # 0101
        # As expected the output was:
        # A and B have 20 matches with 100.0 percent similarity
        # This is to be expected

        # For my next test case, A was the same as above but B was A twice like so:
        # 1010
        # 1111
        # 0000
        # 1110
        # 0101
        # 1010
        # 1111
        # 0000
        # 1110
        # 0101
        # As expected the output was:
        # A and B have 20 matches with 50.0 percent similarity

        # Next I used extremely different files, I kept the same A but I made B:
        # 1
        # 1111111
        # 111111
        # 11111
        # 1111
        # The output is:
        # A and B have 10 matches with 43.47826086956522 percent similarity

        # Next the A.txt said this:
        # Hello World!
        # My name is A.txt!

        # And B.txt said this:
        # Hello World!
        # My name is B.txt!

        # These are very similar so we expect a very high similarity
        # The output is:
        # A and B have 28 matches with 96.55172413793103 percent similarity


# Question 2

# Randomly generates either an X or Y
def random_xy():
    return "X" if randint(0, 1) == 0 else "Y"


# Generates a text file of either an X or Y lines with {count} number of lines
def generate_XY(file, count):
    file.seek(0)
    file.truncate(0)
    file.writelines([random_xy() + "\n" for _ in range(count)])


# Randomly appends either an X or Y every line
def randomly_addXY(file):
    file.seek(0)
    text = [i + random_xy() + "\n" for i in file.read().splitlines()]
    file.seek(0)
    file.truncate(0)
    file.writelines(text)


# Counts how many "XX" or "YY" lines there are in a file
def count_XXYY(file):
    file.seek(0)
    text = file.read().splitlines()
    count = 0
    for i in text:
        if i[-2:] == "XX" or i[-2:] == "YY":
            count -= - 1
    return count, count / len(text)


# Helper that simply prints the contents of a file
def print_file(file):
    file.seek(0)
    print(file.read())


def xy_test():
    with open("XY.txt", "r+") as f:
        N = 1000
        print("Generating a text file with {} lines of either X or Y...".format(N))
        generate_XY(f, N)
        print_file(f)

        print("Randomly adding either a X or Y to the end of the text file...")
        randomly_addXY(f)
        print_file(f)

        count, ratio = count_XXYY(f)
        print("There are {} XX and YY lines in the file with a ratio of {}".format(count, ratio))

        # Here is a sample using N = 3 because it is easier to verify
        # Generating a text file with 3 lines of either X or Y...
        # Y
        # Y
        # X

        # Randomly adding either a X or Y to the end of the text file...
        # YX
        # YY
        # XX

        # There are 2 XX and YY lines in the file with a ratio of 0.6666666666666666
        # This is clearly correct since we can count 1 XX and 1 YY for 2 XX or YY
        # 2/3 is 0.666...


# Question 3

# Given an even length list, returns the pairs of the list
def pairs(even_length_list):
    if len(even_length_list) % 2 != 0:
        print("Please enter an even numbered input list!")
    output = []
    for i in range(2, len(even_length_list), 2):
        output.append(even_length_list[i - 2:i])
    return output

# Gives the projection of I into J
def projection(I, J):
    proj = []
    for j in J:
        if 0 <= j < len(I):
            proj.append(I[j])
    return proj


def projection_test():
    print("The projection of I onto J is:")
    I = [1, 2, 3, 4, 5, 6, 7, 8]
    J = {0, 1, 2}
    print("I", I)
    print("J", J)
    print(projection(pairs(I), J))
    print("The projection of I onto J is:")
    I = [1, 2.09, 3, 4, 5, 6, "a", 8, 9, 10.4, 11, "b"]
    J = {1, 2, 7}
    print("I", I)
    print("J", J)
    print(projection(pairs(I), J))


# Question 4
class User:
    def __init__(self, userId='', password='', loginStatus=''):
        self.userId = userId
        self.password = password
        self.loginStatus = loginStatus

    def verifyLogin(self):
        pass


class Customer(User):
    def __init__(self, customerName='', address='', email='', creditCardInfo='', shippingInfo=''):
        self.customerName = customerName
        self.address = address
        self.email = email
        self.creditCardInfo = creditCardInfo
        self.shippingInfo = shippingInfo
        self.cart = ShoppingCart()
        self.order = Orders()

    def register(self):
        pass

    def login(self):
        pass

    def updateProfile(self):
        pass


class Administrator(User):
    def __init__(self, adminName='', email=''):
        self.adminName = adminName
        self.email = email

    def updateCatalog(self):
        pass


class ShoppingCart:
    def __init__(self, cartId=0, productID=0, quantity=0, dateAdded=0):
        self.cartId = cartId
        self.productID = productID
        self.quantity = quantity
        self.dateAdded = dateAdded

    def addCartItem(self):
        pass

    def updateQuantity(self):
        pass

    def viewCartDetails(self):
        pass

    def checkOut(self):
        pass


class ShippingInfo:
    def __init__(self, shippingId=0, shippingType='', shippingCost=0, shippingRegionId=0):
        self.shippingId = shippingId
        self.shippingType = shippingType
        self.shippingCost = shippingCost
        self.shippingRegionId = shippingRegionId

    def updateShippingInfo(self):
        pass


class OrderDetails:
    def __init__(self, orderId=0, productId=0, productName='', quantity=0, unitCost=0.0, subtotal=0.0):
        self.orderId = orderId
        self.productId = productId
        self.productName = productName
        self.quantity = quantity
        self.unitCost = unitCost
        self.subtotal = subtotal

    def calcPrice(self):
        pass


class Orders:
    def __init__(self, orderId=0, dateCreated='', dateShipped='', customerName='', customerId='', status='',
                 shippingId=''):
        self.orderId = orderId
        self.dateCreated = dateCreated
        self.dateShipped = dateShipped
        self.customerName = customerName
        self.customerId = customerId
        self.status = status
        self.shippingId = shippingId
        self.shipInfo = ShippingInfo()
        self.details = OrderDetails()

    def placeOrder(self):
        pass


# Question 5

# Reads the contents of a text file, then place the contents to a 2D list
def convert_2D(file, N):
    file.seek(0)
    matrix = []
    row = []
    count = 0
    for i in file:
        row.append(i)
        count += 1
        if count % N == 0:
            matrix.append(row)
            row = []
            count = 0
    # For empty lines
    if count > 0:
        for i in range(N - count):
            row.append("")
        matrix.append(row)
    return matrix


# Randomly shuffles a 2D list using random.shuffle import
def shuffle_2D(matrix):
    for row in matrix:
        shuffle(row)
    shuffle(matrix)
    return matrix


# Writing from a 2D list of string into a file
def convert_file(file, matrix):
    file.seek(0)
    file.truncate(0)
    for array in matrix:
        for element in array:
            file.write(element)


def file_shuffle_test():
    # First, a file is converted into a 2D list where the row size is fixed to N = 3 in this case
    # Then it is shuffled
    # Then is rewritten back into the same file
    with open("2D.txt", "r+") as f:
        N = 3
        matrix = convert_2D(f, 3)
        print("Text file converted into a 2D list with", N, "rows:")
        print(matrix)
        shuffled = shuffle_2D(matrix)
        print("2D list shuffled:")
        print(shuffled)
        convert_file(f, shuffled)
        print("2D list shuffled converted back into the same text file!")
        # Initial text file:
        # salutations
        # howdy
        # hello
        # hi
        # how are you
        # greetings

        # After calling our functions:
        # Text file converted into a 2D list with 3 rows:
        # [['salutations\n', 'hello\n', 'howdy\n'], ['hi\n', 'how are you\n', 'greetings\n']]
        # 2D list shuffled:
        # [['howdy\n', 'salutations\n', 'hello\n'], ['greetings\n', 'how are you\n', 'hi\n']]
        # 2D list shuffled converted back into the same text file!

        # The text file after output:
        # howdy
        # salutations
        # hello
        # greetings
        # how are you
        # hi

        # As you can see, this is clearly shuffled. If we keep on running this program, it will keep on being shuffled


# Question 6

# 3D projection given m number of 2D lists of indexes
def projection_3D(n, m):
    cube = [[[randint(0, 1000) for k in range(n)] for j in range(n)] for i in range(n)]
    indexes = [[[randint(0, n - 1) for k in range(n)] for j in range(n)] for i in range(m)]
    projections = []
    for index in indexes:
        for i in range(n):
            for j in range(n):
                projections.append(cube[index[i][j]])
    return projections


def projection_3D_test():
    n, m = int(input("Please input n: ")), int(input("Please input m: "))
    print("A randomly generated cube of side length {} which {} randomly generated 2D list of indexes has this "
          "projection:\n{}".format(n, m, projection_3D(n, m)))
    # Please input n: 2
    # Please input m: 1
    # A randomly generated cube of side length 2 which 1 randomly generated 2D list of indexes has this projection:
    # [[[592, 633], [315, 683]], [[592, 633], [315, 683]], [[559, 601], [786, 296]], [[559, 601], [786, 296]]]


similarity_test()     # Q1
xy_test()             # Q2
projection_test()     # Q3
file_shuffle_test()   # Q5
projection_3D_test()  # Q6
