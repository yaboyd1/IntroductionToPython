# Encrypts a [string] with a given shift value
def encrypt(str, s):
	output = ""
	for char in str:
		if char.isupper():
			start = ord("A")
			output += chr((ord(char) - start + s) % 26 + start)
		elif char.islower():
			start = ord("a")
			output += chr((ord(char) - start - s) % 26 + start)
		elif char.isnumeric():
			start = ord("0")
			output += chr((ord(char) - start - s) % 10 + start)
		else:
			output += char
	return output

# Decrypts a [string] with a given shift value
def decrypt(str, s):
	output = ""
	for char in str:
		if char.isupper() or char.islower():
			output += encrypt(char, 26 - s)
		elif char.isnumeric():
			output += encrypt(char, 10 - s)
		else:
			output += char
	return output

# Encrypts an input file object's text and writes in output file object
def encrypt_file(input, output, s):
	input.seek(0)
	output.seek(0)
	output.truncate(0)
	output.write(encrypt(input.read(), s))

# Decrypts an input file object's text and writes in output file object
def decrypt_file(input, output, s):
	input.seek(0)
	output.seek(0)
	output.truncate(0)
	output.write(decrypt(input.read(), s))

# This is a simple test that will encrypt original.txt to encrypted.txt
# This will also decrypt encrypted.txt to decrypted.txt
# The shift is 1
# Please check out the files!
def simple_test():
	print("This is a simple test that will encrypt original.txt to encrypted.txt")
	print("This will also decrypt encrypted.txt to decrypted.txt")
	print("The shift is 1")
	print("Please check out the files!")
	with open("original.txt", "r") as original, open("encrypted.txt", "w+") as encrypted, open("decrypted.txt", "w") as decrypted:
		encrypt_file(original, encrypted, 1);
		decrypt_file(encrypted, decrypted, 1);

# Hello World!1! (Original)
# Idkkn Xnqkc!0! (Encrypted)
# Hello World!1! (Decrypted)
simple_test() 

# The simple tests work!

# More complicated tests to prove it works for all cases
# Skip to user_input_test() if you would like to try out some values of your own

# Generated Tests
def generated_tests():
	NUMERICS = "0123456789"
	UPPERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	LOWERS = UPPERS.lower()
	ALL = "Hello 1st World! This is string with uppercases, lowercases, numbers and punctuation!?!"
	TEST = [NUMERICS, UPPERS, LOWERS, ALL]
	SHIFTS = [1, 10, 26, 27]

	for s in SHIFTS:	
		print("\nShift:", s)
		for str in TEST:
			with open("original.txt", "w") as original, open("encrypted.txt", "w") as encrypted, open("decrypted.txt", "w") as decrypted:
				print("Original  String:", str)
				original.write(str)

				# NOTE: It is more effiecient to use encrypt() with strings
				encrypted_str = encrypt(str, s)
				print("Encrypted String:", encrypted_str)
				encrypted.write(encrypted_str) 

				decrypted_str = decrypt(encrypted_str, s)
				print("Decrypted String:", decrypted_str)
				decrypted.write(decrypted_str)

# Commented out (Check out the output below)
# generated_tests()

# Output

# Shift: 1
# Original  String: 0123456789
# Encrypted String: 9012345678
# Decrypted String: 0123456789
# Original  String: ABCDEFGHIJKLMNOPQRSTUVWXYZ
# Encrypted String: BCDEFGHIJKLMNOPQRSTUVWXYZA
# Decrypted String: ABCDEFGHIJKLMNOPQRSTUVWXYZ
# Original  String: abcdefghijklmnopqrstuvwxyz
# Encrypted String: zabcdefghijklmnopqrstuvwxy
# Decrypted String: abcdefghijklmnopqrstuvwxyz
# Original  String: Hello 1st World! This is string with uppercases, lowercases, numbers and punctuation!?!
# Encrypted String: Idkkn 0rs Xnqkc! Ughr hr rsqhmf vhsg toodqbzrdr, knvdqbzrdr, mtladqr zmc otmbstzshnm!?!
# Decrypted String: Hello 1st World! This is string with uppercases, lowercases, numbers and punctuation!?!

# Shift: 10
# Original  String: 0123456789
# Encrypted String: 0123456789
# Decrypted String: 0123456789
# Original  String: ABCDEFGHIJKLMNOPQRSTUVWXYZ
# Encrypted String: KLMNOPQRSTUVWXYZABCDEFGHIJ
# Decrypted String: ABCDEFGHIJKLMNOPQRSTUVWXYZ
# Original  String: abcdefghijklmnopqrstuvwxyz
# Encrypted String: qrstuvwxyzabcdefghijklmnop
# Decrypted String: abcdefghijklmnopqrstuvwxyz
# Original  String: Hello 1st World! This is string with uppercases, lowercases, numbers and punctuation!?!
# Encrypted String: Rubbe 1ij Gehbt! Dxyi yi ijhydw myjx kffuhsqiui, bemuhsqiui, dkcruhi qdt fkdsjkqjyed!?!
# Decrypted String: Hello 1st World! This is string with uppercases, lowercases, numbers and punctuation!?!

# Shift: 26
# Original  String: 0123456789
# Encrypted String: 4567890123
# Decrypted String: 0123456789
# Original  String: ABCDEFGHIJKLMNOPQRSTUVWXYZ
# Encrypted String: ABCDEFGHIJKLMNOPQRSTUVWXYZ
# Decrypted String: ABCDEFGHIJKLMNOPQRSTUVWXYZ
# Original  String: abcdefghijklmnopqrstuvwxyz
# Encrypted String: abcdefghijklmnopqrstuvwxyz
# Decrypted String: abcdefghijklmnopqrstuvwxyz
# Original  String: Hello 1st World! This is string with uppercases, lowercases, numbers and punctuation!?!
# Encrypted String: Hello 5st World! This is string with uppercases, lowercases, numbers and punctuation!?!
# Decrypted String: Hello 1st World! This is string with uppercases, lowercases, numbers and punctuation!?!

# Shift: 27
# Original  String: 0123456789
# Encrypted String: 3456789012
# Decrypted String: 0123456789
# Original  String: ABCDEFGHIJKLMNOPQRSTUVWXYZ
# Encrypted String: BCDEFGHIJKLMNOPQRSTUVWXYZA
# Decrypted String: ABCDEFGHIJKLMNOPQRSTUVWXYZ
# Original  String: abcdefghijklmnopqrstuvwxyz
# Encrypted String: zabcdefghijklmnopqrstuvwxy
# Decrypted String: abcdefghijklmnopqrstuvwxyz
# Original  String: Hello 1st World! This is string with uppercases, lowercases, numbers and punctuation!?!
# Encrypted String: Idkkn 4rs Xnqkc! Ughr hr rsqhmf vhsg toodqbzrdr, knvdqbzrdr, mtladqr zmc otmbstzshnm!?!
# Decrypted String: Hello 1st World! This is string with uppercases, lowercases, numbers and punctuation!?!

# User Input Tests
def user_input_test():
	shift = int(input("Please enter how much you want to shift original.txt by: "))
	print("Shift:", shift)
	with open("original.txt", "r") as original, open("encrypted.txt", "w") as encrypted, open("decrypted.txt", "w") as decrypted:
		print("Taking the text from original.txt and encrypting to encrypted.txt, decrypting to decrypted.txt")
		str = original.read()
		print("Original Text:", str, sep="\n")
		
		encrypted_str = encrypt(str, shift)
		print("Encrypted Text:", encrypted_str, sep="\n")
		encrypted.write(encrypted_str)
		
		decrypted_str = decrypt(encrypted_str, shift)
		print("Decrypted Text:", decrypted_str, sep="\n")
		decrypted.write(decrypted_str)

print("Want to try your own shift value or change the contents of original.txt?")
print("Feel free! Go ahead")
user_input_test()

# Sample Output

# Please enter how much you want to shift original.txt by: 3
# Shift: 3
# Taking the text from original.txt and encrypting to encrypted.txt, decrypting to decrypted.txt
# Original Text:
# Dear TextFile,
# Today I wrote a program to encrypt you.
# I hope you enjoy the security!
# I will shift you 3 times.
# Do not worry because I can decrypt you anytime!
# Sincerely,
# Yours Truly

# Encrypted Text:
# Gbxo WbuqIfib,
# Wlaxv L tolqb x moldoxj ql bkzovmq vlr.
# L elmb vlr bkglv qeb pbzrofqv!
# L tfii pefcq vlr 0 qfjbp.
# Gl klq tloov ybzxrpb L zxk abzovmq vlr xkvqfjb!
# Vfkzbobiv,
# Blrop Woriv

# Decrypted Text:
# Dear TextFile,
# Today I wrote a program to encrypt you.
# I hope you enjoy the security!
# I will shift you 3 times.
# Do not worry because I can decrypt you anytime!
# Sincerely,
# Yours Truly
