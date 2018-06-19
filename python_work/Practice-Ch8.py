import printing_models
# import Chapter8extended
# from Chapter8extended import make_shirt
# from Chapter8extended import make_shirt as ms
# import Chapter8extended as ch8
from Chapter8extended import * 

'''
8-1. Message: Write a function called display_message() that prints one sentence
telling everyone what you are learning about in this chapter. Call the
function, and make sure the message displays correctly.

8-2. Favorite Book: Write a function called favorite_book() that accepts one
parameter, title. The function should print a message, such as One of my
favorite books is Alice in Wonderland. Call the function, making sure to
include a book title as an argument in the function call.
'''

# 1
def display_message():
	print('We are learning how to write functions!')

display_message()

# 2
def favorite_book(title):
	print('\nOne of my favorite books is ' + title.title() + '.')

favorite_book('of mice and men')

'''
8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
text of a message that should be printed on the shirt. The function should print
a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the
function a second time using keyword arguments.

8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python. Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a different
message.

8-5. Cities: Write a function called describe_city() that accepts the name of
a city and its country. The function should print a simple sentence, such as
Reykjavik is in Iceland. Give the parameter for the country a default value.
Call your function for three different cities, at least one of which is not in the
default country.
'''

# 3
def make_shirt(size, text):
	print('\nThe size of the shirt: ' + size)
	print('Message: ' + text.title())

make_shirt('large', 'just keep coding')
make_shirt(text = 'just keep coding', size = 'large')

# 4
def make_shirt(size = 'large', text = 'i love python'):
	print('\nThe size of the shirt: ' + size)
	print('Message: ' + text.title())

make_shirt(size = 'medium')
make_shirt(text = 'i need coffee')

# 5
def describe_city(city, country = 'united states'):
	print('\n' + city.title() + ' is in ' + country.title() + '.')

describe_city('glendale')
describe_city(city = 'hollywood')
describe_city(city = 'london', country = 'england')


'''
8-6. City Names: Write a function called city_country() that takes in the name
of a city and its country. The function should return a string formatted like this:
"Santiago, Chile"
Call your function with at least three city-country pairs, and print the value
that’s returned.

8-7. Album: Write a function called make_album() that builds a dictionary
describing a music album. The function should take in an artist name and an
album title, and it should return a dictionary containing these two pieces of
information. Use the function to make three dictionaries representing different
albums. Print each return value to show that the dictionaries are storing the
album information correctly.

Add an optional parameter to make_album() that allows you to store the
number of tracks on an album. If the calling line includes a value for the number
of tracks, add that value to the album’s dictionary. Make at least one new
function call that includes the number of tracks on an album.

8-8. User Albums: Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album’s artist and title. Once you have that
information, call make_album() with the user’s input and print the dictionary
that’s created. Be sure to include a quit value in the while loop.
'''

# 6
def city_country(city, country):
	return city.title() + ', ' + country.title()

glendale = city_country('glendale', 'united states')
print(glendale)

hollywood = city_country('hollywood', 'united states')
print(hollywood)

yerevan = city_country('yerevan', 'armenia')
print(yerevan)

# 7
def make_album(artist_name, album, tracks = ''):
	music_album = {
		'artist_name':artist_name,
		'album_title':album,
		}

	if tracks:
		music_album['tracks'] = tracks

	return music_album

soad = make_album('serj tankian', 'toxicity', 10)
print(soad)

# 8
'''
while True:
	print('Enter q to quit anytime.\n')

	artist = input('Please enter an artists name: ')
	if artist == 'q':
		break

	album = input('Please enter the album’s title: ')
	if album == 'q':
		break

	music = make_album(artist, album)
	print(music)
'''

'''
8-9. Magicians: Make a list of magician’s names. Pass the list to a function
called show_magicians(), which prints the name of each magician in the list.

8-10. Great Magicians: Start with a copy of your program from Exercise 8-9.
Write a function called make_great() that modifies the list of magicians by adding
the phrase the Great to each magician’s name. Call show_magicians() to
see that the list has actually been modified.

8-11. Unchanged Magicians: Start with your work from Exercise 8-10. Call the
function make_great() with a copy of the list of magicians’ names. Because the
original list will be unchanged, return the new list and store it in a separate list.
Call show_magicians() with each list to show that you have one list of the original
names and one list with the Great added to each magician’s name.
'''

# 9
magicians = ['harry houdini', 'criss angel', 'david blaine']
greatest_magicians = []

def show_magicians(magicians):
	print('Magicians: ')

	for magician in magicians:
		print('\t' + magician.title())

show_magicians(magicians)

# 10
def make_great(magicians):
	while magicians:
		greatest = magicians.pop() + ' the greatest'
		greatest_magicians.append(greatest)

make_great(magicians)
show_magicians(greatest_magicians)

# 11
magicians = ['harry houdini', 'criss angel', 'david blaine']
greatest_magicians = []

make_great(magicians[:])
show_magicians(magicians)
show_magicians(greatest_magicians)

'''
8-12. Sandwiches: Write a function that accepts a list of items a person wants
on a sandwich. The function should have one parameter that collects as many
items as the function call provides, and it should print a summary of the sandwich
that is being ordered. Call the function three times, using a different number
of arguments each time.

8-13. User Profile: Start with a copy of user_profile.py from page 153. Build
a profile of yourself by calling build_profile(), using your first and last names
and three other key-value pairs that describe you.

8-14. Cars: Write a function that stores information about a car in a dictionary.
The function should always receive a manufacturer and a model name. It
should then accept an arbitrary number of keyword arguments. Call the function
with the required information and two other name-value pairs, such as a
color or an optional feature. Your function should work for a call like this one:

car = make_car('subaru', 'outback', color='blue', tow_package=True)

Print the dictionary that’s returned to make sure all the information was
stored correctly.
'''

# 12
def sandwich(*ingridients):
	for ingridient in ingridients:
		print('Adding: ' + ingridient)

sandwich('salami', 'ham', 'roast beef', 'swiss cheese', 'olives', 'mustard')

# 13
def build_profile(first, last, **user_info):
	"""Build a dictionary containing everything we know about a user."""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	
	for key, value in user_info.items():
		profile[key] = value

	return profile

user_profile = build_profile('mher', 'oganesyan',
							location='earth',
							field='computer science')
print(user_profile)

# 14
def cars(manufacturer, model, **extra_info):
	car = {}
	car['manufacturer'] = manufacturer
	car['model'] = model

	for key, value in extra_info.items():
		car[key] = value

	return car

car = cars('jeep', 'wrangler', color = 'black', package = 'sahara')
print(car)

'''
8-15. Printing Models: Put the functions for the example print_models.py in a
separate file called printing_functions.py. Write an import statement at the top
of print_models.py, and modify the file to use the imported functions.

8-16. Imports: Using a program you wrote that has one function in it, store that
function in a separate file. Import the function into your main program file, and
call the function using each of these approaches:

import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *

8-17. Styling Functions: Choose any three programs you wrote for this chapter,
and make sure they follow the styling guidelines described in this section.
'''

# 15
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

printing_models.print_models(unprinted_designs, completed_models)
printing_models.show_completed_models(completed_models)

# 16
# Chapter8extended.make_shirt('large', 'more code more problems')
# make_shirt('medium', 'hello')
# ms('small', 'boy bye')
# ch8.make_shirt('small', 'sushi')
make_shirt('large', "i'm out")
