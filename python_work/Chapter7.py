
# How the input() Function Works
# run through command to make it work
'''
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# leave a space after the prompt for the user to see clearly
name = input("Please enter your name: ")
print("Hello, " + name + "!")
# you can also store the prompt into a variable then call it later using input()
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("\nHello, " + name + "!")

# Using int() to Accept Numerical Input
age = input("How old are you? ")
# How old are you? 21
age = int(age)
age >= 18


height = input("How tall are you, in inches? ")
height = int(height)

if height >= 36:
	print("\nYou're tall enough to ride!")
else:
	print("\nYou'll be able to ride when you're a little older.")

# The Modulo Operator
print(4 % 3)
print(5 % 3)
print(6 % 3)

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
	print("\nThe number " + str(number) + " is even.")
else:
	print("\nThe number " + str(number) + " is odd.")
'''
# Introducing while Loops
current_number = 1
while current_number <= 5:
	print(current_number)
	current_number += 1

# Letting the User Choose When to Quit
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
	message = input(prompt)
	print(message)

# get rid of printing quit
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""

while message != 'quit':
	message = input(prompt)

	if message != 'quit':
		print(message)

# Using a Flag
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
	message = input(prompt)
	
	if message == 'quit':
		active = False
	else:
		print(message)

# Using break to Exit a Loop
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
	city = input(prompt)
	if city == 'quit':
		break
	else:
		print("I'd love to go to " + city.title() + "!")

# Using continue in a Loop
current_number = 0
while current_number < 10:
	current_number += 1
	if current_number % 2 == 0:
		continue
	
	print(current_number)

# Avoiding Infinite Loops
x = 1
while x <= 5:
	print(x)
	x += 1
'''
This one will run forever

x = 1
while x <= 5:
	print(x)
'''

# Using a while Loop with Lists and Dictionaries
# Moving Items from One List to Another
# use while loop to modify lists

# Start with users that need to be verified,
# and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
	current_user = unconfirmed_users.pop()

	print("Verifying user: " + current_user.title())
	confirmed_users.append(current_user)

# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())

# Removing All Instances of Specific Values from a List
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
	pets.remove('cat')

print(pets)


# Filling a Dictionary with User Input
responses = {}

# Set a flag to indicate that polling is active.
polling_active = True
while polling_active:
	# Prompt for the person's name and response.
	name = input("\nWhat is your name? ")
	response = input("Which mountain would you like to climb someday? ")
	
	# Store the response in the dictionary:
	responses[name] = response
	
	# Find out if anyone else is going to take the poll.
	repeat = input("Would you like to let another person respond? (yes/ no) ")
	if repeat == 'no':
		polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
	print(name + " would like to climb " + response + ".")







