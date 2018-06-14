
# Use if statements to control the outcome by checking the condition

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())
print('\n')

# Conditional statements
car = 'bmw'
print(car == 'bmw')

# case sensitive
car = 'Audi'
print(car=='audi')
print(car.lower() == 'audi')
print('\n')

# checking for inequality
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
	print("Hold the anchovies!")

answer = 17
if answer != 42:
	print("That is not the correct answer. Please try again!")
print('\n')

age = 19
print(age < 21)
print(age <= 21)
print(age > 21)
print(age >= 21)
print('\n')

# useing and to check multiple conditions at the same time
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)

# to improve readability we can also write it like this
(age_0 >= 21) and (age_1 >= 21)

# using or to check mutliple conditions
age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)
print('\n')

# Check if a value is in a list
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)

# check if not in list
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
	print(user.title() + ", you can post a response if you wish.")
print('\n')

# Booleans
game_active = True
can_edit = False


# if statements
# if conditional_test:
#	 do something

age = 19
if age >= 18:
	print("You are old enough to vote!")
print('\n')

# if else
age = 17
if age >= 18:
	print("You are old enough to vote!")
	print("Have you registered to vote yet?")
else:
	print("Sorry, you are too young to vote.")
	print("Please register to vote as soon as you turn 18!")
print('\n')

# if-elif-else Chain
age = 12
if age < 4:
	print("Your admission cost is $0.")
elif age < 18:
	print("Your admission cost is $5.")
else:
	print("Your admission cost is $10.")

# or
age = 12
if age < 4:
	price = 0
elif age < 18:
	price = 5
else:
	price = 10
print("Your admission cost is $" + str(price) + ".\n")

# Test mutliple conditions
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
	print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
	print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
	print("Adding extra cheese.")
print("\nFinished making your pizza!\n")


# this way only the first one is checked because it passes the first condition.
# so the rest are ignored
if 'mushrooms' in requested_toppings:
	print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
	print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
	print("Adding extra cheese.")


# if statements with lists
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
	print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!\n")

for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
		print("Sorry, we are out of green peppers right now.")
	else:
		print("Adding " + requested_topping + ".")
print('\n')

# Checking That a List Is Not Empty
requested_toppings = []
if requested_toppings:
	for requested_topping in requested_toppings:
		print("Adding " + requested_topping + ".")
		print("\nFinished making your pizza!")
else:
	print("Are you sure you want a plain pizza?")
print('\n')

# Using multiple lists
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("Adding " + requested_topping + ".")
	else:
		print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")





