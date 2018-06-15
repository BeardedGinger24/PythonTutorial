
# Dictionaries
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
print('\n')
# A dictionary in Python is a collection of key-value pairs
# A key’s value can be a number, a string, a list, or even another dictionary.

#Adding New Key-Value Pairs
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
print('\n')

# Starting with an Empty Dictionary
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
print('\n')
# Typically, you’ll use empty dictionaries when storing user-supplied data
# in a dictionary or when you write code that generates a large number of
# key-value pairs automatically

# Modifying Values in a Dictionary
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")
print('\n')


alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	# This must be a fast alien.
	x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))
print('\n')

# Removing Key-Value Pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)
print('\n')

# A Dictionary of Similar Objects
# Say you want to poll a number of people and ask them what their favorite programming language
# is. A dictionary is useful for storing the results of a simple poll, like this:

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

print("Sarah's favorite language is " +
favorite_languages['sarah'].title() +
".")

# looping through a dictonary
# you can loop through a dictionary by its keys or by its values

# Looping Through All Key-Value Pairs
user_0 = {
	'username': 'efermi',
	'first': 'enrico',
	'last': 'fermi',
	}
# use a for lopp to loop through the dictionary
for key, value in user_0.items():
	print("\nKey: " + key)
	print("Value: " + value)
print('\n')
# items() returns a list of key-value pairs, which are stored in the variables provided

# Looping Through All the Keys in a Dictionary
# using keys() to loop
# searching through a dictionary uses the key as default, so you can also do this:
# for name in favorite_languages:
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

for name in favorite_languages.keys():
	print(name.title())
print('\n')

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
	print(name.title())
	
	if name in friends:
			print(" Hi " + name.title() +
				", I see your favorite language is " +
				favorite_languages[name].title() + "!")
print('\n')

# use keys() to find out if someone did not take the poll
if 'erin' not in favorite_languages.keys():
	print("Erin, please take our poll!")
print('\n')

# Looping Through a Dictionary’s Keys in Order
# sorted (as said by the book) returns the dictionary in its order
# For me leaving it as it is returns the original order
for name in sorted(favorite_languages.keys()):
	print(name.title() + ", thank you for taking the poll.")
print('\n')

# Looping Through All Values in a Dictionary
# using values()
print("The following languages have been mentioned:")
for language in favorite_languages.values():
	print(language.title())
print('\n')

# to avoid repetition use set
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
	print(language.title())
print('\n')

# When you wrap set() around a list that contains duplicate items, Python
# identifies the unique items in the list and builds a set from those items.

# Nesting
# A List of Dictionaries
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
	print(alien)
print('\n')

# Make an empty list for storing aliens.
aliens = []
# Make 30 green aliens.
for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)
# Show the first 5 aliens:
for alien in aliens[:5]:
	print(alien)
print("...")
# Show how many aliens have been created.
print("Total number of aliens: " + str(len(aliens)))
print('\n')

'''
Can add this after append to change a few of the aliens

for alien in aliens[0:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10
'''

#A List in a Dictionary
# Store information about a pizza being ordered.
pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'extra cheese'],
	}

# Summarize the order.
print("You ordered a " + pizza['crust'] + "-crust pizza " +
	"with the following toppings:")
for topping in pizza['toppings']:
	print("\t" + topping)
print('\n')

favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell'],
	}
for name, languages in favorite_languages.items():
	print("\n" + name.title() + "'s favorite languages are:")
	for language in languages:
		print("\t" + language.title())
print('\n')

# A Dictionary in a Dictionary
users = {
	'aeinstein': {
	'first': 'albert',
	'last': 'einstein',
	'location': 'princeton',
		},

	'mcurie': {
	'first': 'marie',
	'last': 'curie',
	'location': 'paris',
		},
	}

for username, user_info in users.items():
	print("\nUsername: " + username)
	full_name = user_info['first'] + " " + user_info['last']
	location = user_info['location']
	
	print("\tFull name: " + full_name.title())
	print("\tLocation: " + location.title())













