from random import shuffle # Used in Q4 to shuffle a 2D array

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
            A_count += 1

    B_count = 0
    for line in B_text:
        for char in line:
            B_count += 1
    total = A_count if A_count > B_count else B_count

    # Compare the smaller line size with the smaller character size and increment when characters are equal
    count = 0
    text_size = len(A_text) if len(A_text) < len(B_text) else len(B_text)
    for line_index in range(text_size):
        A_line, B_line = list(A_text[line_index]), list(B_text[line_index])
        line_size = len(A_line) if len(A_line) < len(B_line) else len(B_line)
        for chr_index in range(line_size):
            if A_line[chr_index] == B_line[chr_index]:
                count += 1

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

similarity_test()

# Question 2
def switch_words(file, n):
    file.seek(0)
    lines = file.readlines()

    # Second and last lines
    second_line = lines[1].split()
    last_line = lines[-1].split()

    # New second and last lines to replace old ones
    new_second_line = last_line[-n:] + second_line[n:]
    new_last_line = last_line[:-n] + second_line[:n]

    # Replacing old lines with new lines
    lines[1] = " ".join(new_second_line) + "\n"
    lines[-1] = " ".join(new_last_line) + "\n"

    # Writing the array back into the file
    file.seek(0)
    file.truncate(0)
    file.writelines(lines)

def switch_words_test():
    with open("switch_words_input.txt", "r+") as f:
        # The original text file was:
        # apple0 apple1 apple2
        # orange0 orange1 orange2 orange3 orange4
        # banana0
        # pear0 pear1 pear2 pear3 pear4

        # After calling switch words with n = 1, we expect orange0 and pear4 to be switched

        # apple0 apple1 apple2
        # pear4 orange1 orange2 orange3 orange4
        # banana0
        # pear0 pear1 pear2 pear3 orange0

        # This is clearly the case
        switch_words(f, 1)

        # If we do switch words again this time with n = 2,
        # we expect pear4 orange1 to be swapped with pear3 orange 0
        # Let us see if that is the case
        switch_words(f, 2)

        # The file was rewritten to:
        # apple0 apple1 apple2
        # pear3 orange0 orange2 orange3 orange4
        # banana0
        # pear0 pear1 pear2 pear4 orange1

        # This is clearly the case so switch case works correctly!

switch_words_test()

# Question 3

# Given an even length list, returns the pairs of the list
def pairs(input):
    if len(input) % 2 != 0:
        print("Please enter an even numbered input list!")
    output = []
    for i in range(2, len(input), 2):
        output.append(input[i - 2:i])
    return output

# pairs([1, 2, 3, 4, 5, 6, 7])

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

projection_test()

# Question 4

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

file_shuffle_test()

# Question 5
print("**", "*", "****", "***", "******", "*****", "********", "*******", "**********", sep="\n")

# Question 6
print("*", "**", "***", "***", "****", "*****", "****", "*****", "******", "*******", "*****", "******", "*******", "********", "*********", sep="\n")

# Question 7
def caesar_shift(file, n):
    file.seek(0)
    text = file.read()
    with open("caesar_output.txt", "w") as f:
        for i in text:
            # Only shift if it is alphabetical (ignore spaces, tabs, newlines, and punctuation)
            if i.isalpha():
                start = ord("a") if i.islower() else ord("A")
                # Shift the character n bits (uses % to "wrap" around for better shifting for negatives and > 26)
                f.write(chr((ord(i) - start + n) % 26 + start))
            else:
                f.write(i)

def caesar_shift_test():
    with open("caesar_input.txt", "r+") as f:
        f.seek(0)
        f.truncate(0)
        f.write("aaaaabbbcc")
        caesar_shift(f, 2) # This correctly outputs "cccccdddee" in the file which we expect
        caesar_shift(f, 2 + 26) # This also outputs "cccccdddee" which means it works if greater than alphabet (26)
        caesar_shift(f, 2 - 26) # This also outputs "cccccdddee" which means it works for negative values

        f.seek(0)
        f.truncate(0)
        f.write("Testing spaces\ttabs\t\nnewlines\nand even punctuation!?!?!")
        caesar_shift(f, 2)
        # This file has the text:
        # Testing spaces    tabs
        # newlines
        # and even punctuation!?!?!
        # which you can think of as: "Testing spaces\ttabs\t\nnewlines\nand even punctuation!?!?!"
        # from the string representation
        # The output after the function returns:
        # Vguvkpi urcegu    vcdu
        # pgynkpgu
        # cpf gxgp rwpevwcvkqp!?!?!
        # which you can think of as: "Vguvkpi urcegu\tvcdu\t\npgynkpgu\ncpf gxgp rwpevwcvkqp!?!?!"

        # Thus, as you can see, our program clearly ignores whitespace characters and punctuation marks

caesar_shift_test()

# Question 8
def prefix_set(X, Y):
    matches = set()
    for i in range(1, len(X)):
        if X[:i] in Y:
            matches.add(X[:i])
    sorted_matches = sorted(matches)
    return matches, sorted_matches, sorted_matches[::-1]

def prefix_set_test():
    X = "Hello World!"
    Y = "He is the one who said Hello"
    print("X:", X)
    print("Y:", Y)
    initial, lsort, rsort = prefix_set(X, Y)
    print("Sorted:", lsort)
    print("Reversed Sorted", rsort)
    print("Original Set", initial)

prefix_set_test()
