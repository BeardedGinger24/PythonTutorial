
# Files and Exceptions
# Reading from a File

# Reading an Entire File
'''
using pi_digits.txt and file_reader.py

with open('pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents)
'''


# File Paths
# if we had another folder (text_files), we would have to 
# write the file directory differntly;
# with open('text_files/filename.txt') as file_object:
# for Windows you would use a backslash (\) instead of a fowardslash (/)

# OR give the absolute file path for where ever the file may be

# Linux/OS X:
# file_path = '/home/ehmatthes/other_files/text_files/filename.txt'
# with open(file_path) as file_object:

# Windows:
# file_path = 'C:\Users\ehmatthes\other_files\text_files\filename.txt'
# with open(file_path) as file_object:


# Reading Line by Line
'''
filename = 'pi_digits.txt'

with open(filename) as file_object:
	for line in file_object:
		print(line)
'''

# Making a List of Lines from a File
'''
If you want to retain access to a file’s contents
outside the with block, you can store the file’s lines in a list inside the block
and then work with that list.


filename = 'pi_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line.rstrip())
'''

# Working with a File’s Contents
filename = 'pi_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

pi_string = ''
for line in lines:
	pi_string += line.strip() # use strip to get rid of spaces on both sides

print(pi_string)
print(len(pi_string))


# Large Files: One Million Digits
filename = 'pi_million_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

pi_string = ''
for line in lines:
	pi_string += line.strip()

print(pi_string[:52] + "...")
print(len(pi_string))


# Is Your Birthday Contained in Pi?
filename = 'pi_million_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

pi_string = ''
for line in lines:
	pi_string += line.rstrip()
'''
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
	print("Your birthday appears in the first million digits of pi!")
else:
	print("Your birthday does not appear in the first million digits of pi.")
'''


# Writing to a File
# Writing to an Empty File
'''
The second argument, 'w',
tells Python that we want to open the file in write mode. You can open a file
in read mode ('r'), write mode ('w'), append mode ('a'), or a mode that allows
you to read and write to the file ('r+').
'''
filename = 'programming.txt'

with open(filename, 'w') as file_object:
	file_object.write("I love programming.\n")
	file_object.write("I love creating new games.\n") 
	# need to add new line or it will continue off of the last line

# Writing Multiple Lines
# add this: file_object.write("I love creating new games.")

# Appending to a File
with open(filename, 'a') as file_object:
	file_object.write("I also love finding meaning in large datasets.\n")
	file_object.write("I love creating apps that can run in a browser.\n")


# Exceptions
# Exceptions are handled with try-except blocks.

# Handling the ZeroDivisionError Exception
# Using try-except Blocks
try:
	print(5/0)
except ZeroDivisionError:
	print("You can't divide by zero!")

# Using Exceptions to Prevent Crashes
# The else Block
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
	first_number = input("\nFirst number: ")

	if first_number == 'q':
		break

	second_number = input("Second number: ")

	try:
		answer = int(first_number) / int(second_number)
	except ZeroDivisionError:
		print("You can't divide by 0!")
	else:
		print(answer)
'''
The try-except-else block works like this: Python attempts to run the
code in the try statement. The only code that should go in a try statement
is code that might cause an exception to be raised. Sometimes you’ll have
additional code that should run only if the try block was successful; this
code goes in the else block. The except block tells Python what to do in case
a certain exception arises when it tries to run the code in the try statement.
'''

# Handling the FileNotFoundError Exception
filename = 'alice.txt'

try:
	with open(filename) as f_obj:
		contents = f_obj.read()
except FileNotFoundError:
	msg = "Sorry, the file " + filename + " does not exist."
	print(msg)

# Analyzing Text
'''
>>> title = "Alice in Wonderland"
>>> title.split()
['Alice', 'in', 'Wonderland']
'''

# count the number of words
'''
filename = 'alice.txt'

try:
	with open(filename) as f_obj:
		contents = f_obj.read()
except FileNotFoundError:
	msg = "Sorry, the file " + filename + " does not exist."
	print(msg)
else:
	# Count the approximate number of words in the file.
	words = contents.split()
	num_words = len(words)
	print("The file " + filename + " has about " + str(num_words) + " words.")
'''

# Working with Multiple Files
# put the file reading into a function
def count_words(filename):
	"""Count the approximate number of words in a file."""
	try:
		with open(filename) as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
		msg = "Sorry, the file " + filename + " does not exist."
		print(msg)
	else:
		# Count approximate number of words in the file.
		words = contents.split()
		num_words = len(words)
		print("The file " + filename + " has about " + str(num_words) +
			" words.")

filename = 'alice.txt'
count_words(filename)


#Count the number of words for multiple books by iterating through a list.
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
	count_words(filename)

# Failing Silently
# use the keyword pass in the exception to 'silently' process it



# Storing Data
'''
Many of your programs will ask users to input certain kinds of information.
You might allow users to store preferences in a game or provide data for a
visualization. Whatever the focus of your program is, you’ll store the information
users provide in data structures such as lists and dictionaries. When
users close a program, you’ll almost always want to save the information
they entered. A simple way to do this involves storing your data using the
json module.

The json module allows you to dump simple Python data structures into a
file and load the data from that file the next time the program runs. You can
also use json to share data between different Python programs. Even better,
the JSON data format is not specific to Python, so you can share data you
store in the JSON format with people who work in many other programming
languages. It’s a useful and portable format, and it’s easy to learn.
'''

# Using json.dump() and json.load()
'''
Let’s write a short program that stores a set of numbers and another program
that reads these numbers back into memory. The first program will
use json.dump() to store the set of numbers, and the second program will use
json.load().

The json.dump() function takes two arguments: a piece of data to
store and a file object it can use to store the data. Here’s how you can use
json.dump() to store a list of numbers:
'''
import json

#json.dump()
numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
	json.dump(numbers, f_obj)

# json.load()
with open(filename) as f_obj:
	numbers = json.load(f_obj)
print(numbers)

# Saving and Reading User-Generated Data
username = input("What is your name? ")

# dump
filename = 'username.json'
with open(filename, 'w') as f_obj:
	json.dump(username, f_obj)
	print("We'll remember you when you come back, " + username + "!")

# load
with open(filename) as f_obj:
	username = json.load(f_obj)
	print("Welcome back, " + username + "!")

# try and load username if it exists
# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.
filename = 'username.json'

try:
	with open(filename) as f_obj:
		username = json.load(f_obj)
except FileNotFoundError:
	username = input("What is your name? ")
	with open(filename, 'w') as f_obj:
		json.dump(username, f_obj)
		print("We'll remember you when you come back, " + username + "!")
else:
	print("Welcome back, " + username + "!")


# Refactoring
'''
Often, you’ll come to a point where your code will work, but you’ll recognize
that you could improve the code by breaking it up into a series of functions
that have specific jobs. This process is called refactoring.
'''
'''
import json

def greet_user():
	"""Greet the user by name."""

	filename = 'username.json'
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		username = input("What is your name? ")
		with open(filename, 'w') as f_obj:
			json.dump(username, f_obj)
			print("We'll remember you when you come back, " + username + "!")
	else:
		print("Welcome back, " + username + "!")

greet_user()
'''

def get_stored_username():
	"""Get stored username if available."""

	filename = 'username.json'
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return username

def get_new_username():
	"""Prompt for a new username."""
	
	username = input("What is your name? ")
	filename = 'username.json'
	with open(filename, 'w') as f_obj:
		json.dump(username, f_obj)
	return username

def greet_user():
	"""Greet the user by name."""
	
	username = get_stored_username()
	if username:
		print("Welcome back, " + username + "!")
	else:
		username = get_new_username()
		print("We'll remember you when you come back, " + username + "!")

greet_user()









