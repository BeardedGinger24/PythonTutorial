
def make_pizza(size, *toppings):
	"""Summarize the pizza we are about to make."""
	print("\nMaking a " + str(size) +
	"-inch pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)

def make_shirt(size, text):
	print('\nThe size of the shirt: ' + size)
	print('Message: ' + text.title())