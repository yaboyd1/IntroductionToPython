# Custom EmptySet Exception
class EmptySet(Exception):
	pass

# Function to find the cartesian product of two sets
def cartesian_product(set1, set2):
	if set1 == set() or set2 == set():
		raise EmptySet()
	return set([(i, j) for i in set1 for j in set2])

# Program that keeps going until 2 non-empty sets are provided for the cartesian product
while True:
	try:
		set1 = set(input("Please input several elements (separated by spaces): ").split())
		set2 = set(input("Please input several elements (separated by spaces): ").split())
		print("Cartesian Product:")
		print(cartesian_product(set1, set2))
		break;
	except EmptySet:
		print("Uh oh! One of the sets you have entered is empty!")
		print("Please enter a valid set where the elements are space separated!")

# Sample Output

# Please input several elements (separated by spaces): 1 2
# Please input several elements (separated by spaces):
# Cartesian Product:
# Uh oh! One of the sets you have entered is empty!
# Please enter a valid set where the elements are space separated!
# Please input several elements (separated by spaces):
# Please input several elements (separated by spaces): a b c
# Cartesian Product:
# Uh oh! One of the sets you have entered is empty!
# Please enter a valid set where the elements are space separated!
# Please input several elements (separated by spaces): 1 2
# Please input several elements (separated by spaces): a b c
# Cartesian Product:
# {('1', 'b'), ('1', 'a'), ('2', 'b'), ('1', 'c'), ('2', 'a'), ('2', 'c')}
