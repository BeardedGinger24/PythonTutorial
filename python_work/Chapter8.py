import Chapter8extended

# Functions
# which are named blocks of code
# that are designed to do one specific job

# Defining a Function
# the keyword def to inform Python that you’re defining a function
def greet_user():
	"""Display a simple greeting."""
	print("Hello!")

greet_user()

# Passing Information to a Function
def greet_user(username):
	"""Display a simple greeting."""
	print("Hello, " + username.title() + "!")

greet_user('jesse')

# Passing Arguments
'''
You can pass arguments to your functions
in a number of ways:

You can use positional arguments, which need to be in
the same order the parameters were written; 

keyword arguments, where each
argument consists of a variable name and a value;

and lists and dictionaries
of values.
'''

# Positional Arguments
def describe_pet(animal_type, pet_name):
	"""Display information about a pet."""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')

# Keyword Arguments
# is a name-value pair that you pass to a function
# explicitly state the variable you're passing into
describe_pet(animal_type='hamster', pet_name='harry')

# Default Values
# define a default value in the paramter
def describe_pet(pet_name, animal_type='dog'):
	"""Display information about a pet."""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='willie')
print('\n')
 # or describe_pet('willie')

# Equivalent Function Calls

# Avoiding Argument Errors
# happens when too few or too many arguments passed in


# Return Values
def get_formatted_name(first_name, last_name):
	"""Return a full name, neatly formatted."""
	full_name = first_name + ' ' + last_name
	return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# Making an Argument Optional
def get_formatted_name(first_name, middle_name, last_name):
	"""Return a full name, neatly formatted."""
	full_name = first_name + ' ' + middle_name + ' ' + last_name
	return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

# make the middle name optional by giving it a defaul empty value
def get_formatted_name(first_name, last_name, middle_name=''):
	"""Return a full name, neatly formatted."""
	if middle_name:
		full_name = first_name + ' ' + middle_name + ' ' + last_name
	else:
		full_name = first_name + ' ' + last_name

	return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)


# Returning a Dictionary
def build_person(first_name, last_name):
	"""Return a dictionary of information about a person."""
	person = {'first': first_name, 'last': last_name}
	
	return person

musician = build_person('jimi', 'hendrix')
print(musician)


def build_person(first_name, last_name, age=''):
	"""Return a dictionary of information about a person."""
	person = {'first': first_name, 'last': last_name}
	if age:
		person['age'] = age
	
	return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)

# Using a Function with a while Loop
# This is an infinite loop!
'''
while True:
	print("\nPlease tell me your name:")
	f_name = input("First name: ")
	l_name = input("Last name: ")

	formatted_name = get_formatted_name(f_name, l_name)
	print("\nHello, " + formatted_name + "!")


Define a quit condition for this


while True:
	print("\nPlease tell me your name:")
	print("(enter 'q' at any time to quit)")

	f_name = input("First name: ")
	if f_name == 'q':
		break

	l_name = input("Last name: ")
	if l_name == 'q':
		break
	
	formatted_name = get_formatted_name(f_name, l_name)
	print("\nHello, " + formatted_name + "!")
'''

# Passing a List
def greet_users(names):
	"""Print a simple greeting to each user in the list."""
	
	for name in names:
		msg = "Hello, " + name.title() + "!"
		print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# Modifying a List in a Function
def print_models(unprinted_designs, completed_models):
	"""
	Simulate printing each design, until none are left.
	Move each design to completed_models after printing.
	"""

	while unprinted_designs:
		current_design = unprinted_designs.pop()

		# Simulate creating a 3D print from the design.
		print("Printing model: " + current_design)
		completed_models.append(current_design)

def show_completed_models(completed_models):
	"""Show all the models that were printed."""
	print("\nThe following models have been printed:")
	
	for completed_model in completed_models:
		print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


# Preventing a Function from Modifying a List
# if you dont want the original list to be touched
# pass a copy of the list: 
# function_name(list_name[:])
print_models(unprinted_designs[:], completed_models)


# Passing an Arbitrary Number of Arguments
'''
def make_pizza(*toppings):
	"""Summarize the pizza we are about to make."""
	print("\nMaking a pizza with the following toppings:")
	
	for topping in toppings:
		print("- " + topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
'''

# Mixing Positional and Arbitrary Arguments
'''
def make_pizza(size, *toppings):
	"""Summarize the pizza we are about to make."""
	print("\nMaking a " + str(size) +
	"-inch pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
'''

# Using Arbitrary Keyword Arguments
def build_profile(first, last, **user_info):
	"""Build a dictionary containing everything we know about a user."""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	
	for key, value in user_info.items():
		profile[key] = value

	return profile

user_profile = build_profile('albert', 'einstein',
							location='princeton',
							field='physics')
print(user_profile)

# Storing Your Functions in Modules
# Importing an Entire Module
# module_name.function_name()

Chapter8extended.make_pizza(16, 'pepperoni')
Chapter8extended.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Importing Specific Functions
# from module_name import function_name

from Chapter8extended import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Using as to Give a Function an Alias
# the same name may be used already, causing a conflict
# from pizza import make_pizza as mp
# mp(16, 'pepperoni')
# mp(12, 'mushrooms', 'green peppers', 'extra cheese')


# Using as to Give a Module an Alias
# import pizza as p
# p.make_pizza(16, 'pepperoni')
# p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Importing All Functions in a Module
# from pizza import *
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# Styling Functions


