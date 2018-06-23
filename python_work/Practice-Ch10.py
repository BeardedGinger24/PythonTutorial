
'''
10-1. Learning Python: Open a blank file in your text editor and write a few
lines summarizing what you’ve learned about Python so far. Start each line
with the phrase In Python you can.... Save the file as learning_python.txt in the
same directory as your exercises from this chapter. Write a program that reads
the file and prints what you wrote three times. Print the contents once by reading
in the entire file, once by looping over the file object, and once by storing
the lines in a list and then working with them outside the with block.

10-2. Learning C: You can use the replace() method to replace any word in a
string with a different word. Here’s a quick example showing how to replace
'dog' with 'cat' in a sentence:

>>> message = "I really like dogs."
>>> message.replace('dog', 'cat')
'I really like cats.'

Read in each line from the file you just created, learning_python.txt, and
replace the word Python with the name of another language, such as C. Print
each modified line to the screen.
'''

# 1
file_path = 'learning_python.txt'

with open(file_path) as file_object:
	contents = file_object.read()
	print(contents.rstrip())
print()

with open(file_path) as file_object:
	for line in file_object:
		print(line.rstrip())
print()

with open(file_path) as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line.rstrip())
print()

# 2
with open(file_path) as file_object:
	lines_2 = file_object.readlines()

for line_2 in lines_2:
	line_2 = line_2.replace('Python', 'C') # replace works temporarly, store in variable
	print(line_2.rstrip())

'''
10-3. Guest: Write a program that prompts the user for their name. When they
respond, write their name to a file called guest.txt.

10-4. Guest Book: Write a while loop that prompts users for their name. When
they enter their name, print a greeting to the screen and add a line recording
their visit in a file called guest_book.txt. Make sure each entry appears on a
new line in the file.

10-5. Programming Poll: Write a while loop that asks people why they like
programming. Each time someone enters a reason, add their reason to a file
that stores all the responses.
'''

# 3
'''
guest = input('Please enter your name:\n')

with open('guest.txt', 'w') as file_object:
	file_object.write(guest)

# 4
while True:
	name = input('Please enter your name (enter "quit" if done):\n')

	if name == 'quit':
		break

	print('Hello ' + name.title())

	with open('guest_book.txt', 'a') as file_object:
		file_object.write(name + '\n')

# 5
while True:
	reason = input('Why do you like programming? (enter quit when done):\n')

	if reason == 'quit':
		break

	with open('reasons.txt', 'a') as file_object:
		file_object.write(reason + '\n')
'''

'''
10-6. Addition: One common problem when prompting for numerical input
occurs when people provide text instead of numbers. When you try to convert
the input to an int, you’ll get a TypeError. Write a program that prompts for
two numbers. Add them together and print the result. Catch the TypeError if
either input value is not a number, and print a friendly error message. Test your
program by entering two numbers and then by entering some text instead of a
number.
'''

# 6
while True:
	first_number = input("\nFirst number: ")

	if first_number == 'q':
		break

	second_number = input("Second number: ")

	try:
		answer = int(first_number) + int(second_number)
	except ValueError:
		print("You can't add text!")
	else:
		print(answer)


'''
10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop
so the user can continue entering numbers even if they make a mistake and
enter text instead of a number.

10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three
names of cats in the first file and three names of dogs in the second file. Write
a program that tries to read these files and print the contents of the file to the
screen. Wrap your code in a try-except block to catch the FileNotFound error,
and print a friendly message if a file is missing. Move one of the files to a different
location on your system, and make sure the code in the except block
executes properly.

10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail
silently if either file is missing.
'''

# 7
# done

# 8
file_name = 'dogs.txt'
try:
	with open(file_name) as file_object:
		contents = file_object.read()
except FileNotFoundError:
	print('This file doesnt exist.')
else:
	print(contents)

# 9
file_name = 'dogs.txt'
try:
	with open(file_name) as file_object:
		contents = file_object.read()
except FileNotFoundError:
	pass
else:
	print(contents)

'''
10-10. Common Words: Visit Project Gutenberg (http://gutenberg.org/ )
and find a few texts you’d like to analyze. Download the text files for these
works, or copy the raw text from your browser into a text file on your
computer.
	You can use the count() method to find out how many times a word or
phrase appears in a string. For example, the following code counts the number
of times 'row' appears in a string:

>>> line = "Row, row, row your boat"
>>> line.count('row')
2
>>> line.lower().count('row')
3

	Notice that converting the string to lowercase using lower() catches
all appearances of the word you’re looking for, regardless of how it’s
formatted.
	Write a program that reads the files you found at Project Gutenberg and
determines how many times the word 'the' appears in each text.
'''

# 10
try:
	with open('all_things_are_possible.txt') as f_object:
		contents = f_object.read()
except FileNotFoundError:
	pass
else:
	count = contents.lower().count('the')
	print(str(count))

'''
10-11. Favorite Number: Write a program that prompts for the user’s favorite
number. Use json.dump() to store this number in a file. Write a separate program
that reads in this value and prints the message, “I know your favorite
number! It’s _____.”

10-12. Favorite Number Remembered: Combine the two programs from
Exercise 10-11 into one file. If the number is already stored, report the favorite
number to the user. If not, prompt for the user’s favorite number and store it in a
file. Run the program twice to see that it works.

10-13. Verify User: The final listing for remember_me.py assumes either that the
user has already entered their username or that the program is running for the
first time. We should modify it in case the current user is not the person who
last used the program.
	Before printing a welcome back message in greet_user(), ask the user if
this is the correct username. If it’s not, call get_new_username() to get the correct
username.
'''

# 11
import json

file_name = 'favorite_number.json'
favorite_number = input('What is your favorite number?\n')

with open(file_name, 'w') as f_object:
	json.dump(favorite_number, f_object)

with open(file_name) as f_object:
	number = json.load(f_object)
print('I know your favorite number! It’s ' + number)

# 12
# favorite_number.py

# 13
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
		check = input('Is this the right username? (y/n) "' + username + '"')
		if check == 'y':
			print("Welcome back, " + username + "!")
		else:
			username = get_new_username()
			print('We have update the username to ' + username)
	else:
		username = get_new_username()
		print("We'll remember you when you come back, " + username + "!")

greet_user()



