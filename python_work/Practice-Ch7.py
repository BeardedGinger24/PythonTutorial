
'''
7-1. Rental Car: Write a program that asks the user what kind of rental car they
would like. Print a message about that car, such as “Let me see if I can find you
a Subaru.”

7-2. Restaurant Seating: Write a program that asks the user how many people
are in their dinner group. If the answer is more than eight, print a message saying
they’ll have to wait for a table. Otherwise, report that their table is ready.

7-3. Multiples of Ten: Ask the user for a number, and then report whether the
number is a multiple of 10 or not.
'''

# 1
rental_car = input('What kind of rental car would you like? ')
print('Let me see if I can find you a ' + rental_car.title() + '.')

# 2
dinner_group = input('How many people are in their dinner group? ')
dinner_group = int(dinner_group)

if dinner_group > 8:
	print('You will have to wait for a table.')
else:
	print('There is a table ready.')

# 3
number = input('Input a number: ')
number = int(number)

if number % 10 == 0:
	print(str(number) + ' is a multiple of 10.')
else:
	print(str(number) + ' is not a multiple of 10.')


'''
7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
pizza toppings until they enter a 'quit' value. As they enter each topping,
print a message saying you’ll add that topping to their pizza.

7-5. Movie Tickets: A movie theater charges different ticket prices depending on
a person’s age. If a person is under the age of 3, the ticket is free; if they are
between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
$15. Write a loop in which you ask users their age, and then tell them the cost
of their movie ticket.
'''

# 4 
pizza_toppings = '\nWhat pizza topping would you like? \nEnter quit if you are finished. '
topping = ''

while topping != 'quit':
	topping = input(pizza_toppings)

	if topping != 'quit':
		print('Adding ' + topping + ' to your pizza.')


# 5
ask = ('How old are you? ')
age = ''

while age != 'quit':
	age = input(ask)

	if age == 'quit':
		break

	age = int(age)
	if age < 3:
		print('The ticket is free.')
	elif age >= 3 and age < 12:
		print('The ticket is $10.')
	else:
		print('The ticket is $15.')

'''
7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5
that do each of the following at least once:
• Use a conditional test in the while statement to stop the loop.
• Use an active variable to control how long the loop runs.
• Use a break statement to exit the loop when the user enters a 'quit' value.

7-7. Infinity: Write a loop that never ends, and run it. (To end the loop, press
ctrl-C or close the window displaying the output.)
'''

# 6
# done in notes

# 7
'''
while True:
	print(':)')
'''

'''
7-8. Deli: Make a list called sandwich_orders and fill it with the names of various
sandwiches. Then make an empty list called finished_sandwiches. Loop
through the list of sandwich orders and print a message for each order, such
as I made your tuna sandwich. As each sandwich is made, move it to the list
of finished sandwiches. After all the sandwiches have been made, print a
message listing each sandwich that was made.

7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
the sandwich 'pastrami' appears in the list at least three times. Add code
near the beginning of your program to print a message saying the deli has
run out of pastrami, and then use a while loop to remove all occurrences of
'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
in finished_sandwiches.

7-10. Dream Vacation: Write a program that polls users about their dream
vacation. Write a prompt similar to If you could visit one place in the world,
where would you go? Include a block of code that prints the results of the poll.
'''

# 8
sandwich_orders = ['pastrami', 'meatball', 'ham']
finished_sandwiches = []

while sandwich_orders:
	current_sandwich = sandwich_orders.pop()

	print('I made youre ' + current_sandwich + ' sandwich.')
	finished_sandwiches.append(current_sandwich)

print('The following sandwiches are ready:')
for sandwich in finished_sandwiches:
	print(sandwich + ' sandwich')
print('\n')

# 9
sandwich_orders = ['pastrami', 'meatball', 'pastrami', 'ham','pastrami', 'chicken']
print('The deli has run out of pastrami.')

while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')
print(sandwich_orders)
print('\n')

# 10
places = []
polling = True

while polling:
	prompt = 'If you could visit one place in the world, where would you go?'
	prompt += "\nEnter 'quit' when finished. "

	place = input(prompt)

	if place == 'quit':
		break

	places.append(place)
print(places)



