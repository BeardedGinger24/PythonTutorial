
'''
9-1. Restaurant: Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message indicating
that the restaurant is open.
	Make an instance called restaurant from your class. Print the two attributes
individually, and then call both methods.

9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
different instances from the class, and call describe_restaurant() for each
instance.

9-3. Users: Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.
	Create several instances representing different users, and call both methods
for each user.
'''

# 1

class Restaurant():

	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		print(self.restaurant_name.title() + ' sells ' + self.cuisine_type.title() + ' food.')

	def open_restuarant(self):
		print(self.restaurant_name.title() + ' is now open!')

	def tables_served(self):
		print(str(self.number_served) + ' tables served.')

	def set_number_served(self, tables):
		self.number_served = tables

	def increment_number_served(self, tables):
		self.number_served += tables

restaurant = Restaurant('bossa nova', 'brazilian')

print('Restaurant: ' + restaurant.restaurant_name.title())
print('Cuisine: ' + restaurant.cuisine_type.title())

restaurant.describe_restaurant()
restaurant.open_restuarant()

# 2
restaurant_1 = Restaurant('ichiban', 'japanese')
restaurant_2 = Restaurant('shabu shabu', 'chinese')
restaurant_3 = Restaurant('little palace', 'chinese')

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()

# 3

class User():
	def __init__(self, first_name, last_name, user_name):
		self.first_name = first_name
		self.last_name = last_name
		self.user_name = user_name
		self.full_name = first_name + ' ' + last_name
		self.login_attempts = 0

	def describe_user(self):
		print(self.full_name.title() + ' user name is: ' + self.user_name)

	def greet_user(self):
		print('Hello ' + self.full_name.title())

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0

user_1 = User('gabriel', 'iglesias', 'fluffy')
user_2 = User('marshall', 'mathers', 'eminem')

user_1.describe_user()
user_1.greet_user()
user_2.describe_user()
user_2.greet_user()


'''
9-4. Number Served: Start with your program from Exercise 9-1 (page 166).
Add an attribute called number_served with a default value of 0. Create an
instance called restaurant from this class. Print the number of customers the
restaurant has served, and then change this value and print it again.
	Add a method called set_number_served() that lets you set the number
of customers that have been served. Call this method with a new number and
print the value again.
	Add a method called increment_number_served() that lets you increment
the number of customers who’ve been served. Call this method with any number
you like that could represent how many customers were served in, say, a
day of business.

9-5. Login Attempts: Add an attribute called login_attempts to your User
class from Exercise 9-3 (page 166). Write a method called increment_
login_attempts() that increments the value of login_attempts by 1. Write
another method called reset_login_attempts() that resets the value of login_
attempts to 0.
	Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts(). Print login_attempts again to
make sure it was reset to 0.
'''

# 4
restaurant = Restaurant('bossa nova', 'brazilian')
restaurant.tables_served()

restaurant.number_served = 2
restaurant.tables_served()

restaurant.set_number_served(5)
restaurant.tables_served()

restaurant.increment_number_served(31)
restaurant.tables_served()

# 5
user = User('daniel', 'kale', 'dale')

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(str(user.login_attempts))

user.reset_login_attempts()
print(str(user.login_attempts))

'''
9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class you wrote
in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either version of
the class will work; just pick the one you like better. Add an attribute called
flavors that stores a list of ice cream flavors. Write a method that displays
these flavors. Create an instance of IceCreamStand, and call this method.

9-7. Admin: An administrator is a special kind of user. Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 166)
or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list
of strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator’s set of
privileges. Create an instance of Admin, and call your method.

9-8. Privileges: Write a separate Privileges class. The class should have one
attribute, privileges, that stores a list of strings as described in Exercise 9-7.
Move the show_privileges() method to this class. Make a Privileges instance
as an attribute in the Admin class. Create a new instance of Admin and use your
method to show its privileges.

9-9. Battery Upgrade: Use the final version of electric_car.py from this section.
Add a method to the Battery class called upgrade_battery(). This method
should check the battery size and set the capacity to 85 if it isn’t already.
Make an electric car with a default battery size, call get_range() once, and
then call get_range() a second time after upgrading the battery. You should
see an increase in the car’s range.
'''

# 6
class IceCreamStand(Restaurant):

	def __init__(self, restaurant_name, cuisine_type):
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = ['vanilla', 'chocholate', 'strawberry']

	def show_flavors(self):
		print('The flavors are: ')
		for flavor in self.flavors:
			print('\t' + flavor)

ice_cream = IceCreamStand('baskin robbins', 'ice cream')
ice_cream.show_flavors()

# 7
'''
class Admin(User):

	def __init__(self, first_name, last_name, user_name):
		super().__init__(first_name, last_name, user_name)
		# self.privileges = ['can add post', 'can delete post', 'can ban user']
		self.privileges = Privileges()
'''
'''
	def show_privileges(self):
		print('Admins privileges: ')
		for privilege in self.privileges:
			print('\t' + privilege)
	'''
#admin_1 = Admin('jose', 'macias', 'jmacias')
#admin_1.show_privileges()

# 8
'''
class Privileges():

	def __init__(self):
		self.privileges = ['can add post', 'can delete post', 'can ban user']

	def show_privileges(self):
		print('Admins privileges: ')
		for privilege in self.privileges:
			print('\t' + privilege)

admin_2 = Admin('jose', 'macias', 'jmacias')
admin_2.privileges.show_privileges()
'''

# 9
class Car():
	"""A simple attempt to represent a car."""
	
	def __init__(self, make, model, year):
		"""Initialize attributes to describe a car."""
		self.make = make
		self.model = model
		self.year = year

	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

class Battery():
	"""A simple attempt to model a battery for an electric car."""
	
	def __init__(self, battery_size=70):
		"""Initialize the battery's attributes."""
		self.battery_size = battery_size

	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print("This car has a " + str(self.battery_size) + "-kWh battery.")

	def get_range(self):
		"""Print a statement about the range this battery provides."""
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270

		message = "This car can go approximately " + str(range)
		message += " miles on a full charge."
		print(message)

	def upgrade_battery(self):
		if self.battery_size != 85:
			self.battery_size = 85

class ElectricCar(Car):
	"""Represent aspects of a car, specific to electric vehicles."""

	def __init__(self, make, model, year):
		"""
		Initialize attributes of the parent class.
		Then initialize attributes specific to an electric car.
		"""
		super().__init__(make, model, year)
		self.battery = Battery()

nissan_leaf = ElectricCar('nissan', 'leaf', '2018')
nissan_leaf.battery.get_range()
nissan_leaf.battery.upgrade_battery()
nissan_leaf.battery.get_range()


'''
9-10. Imported Restaurant: Using your latest Restaurant class, store it in a module.
Make a separate file that imports Restaurant. Make a Restaurant instance,
and call one of Restaurant’s methods to show that the import statement is working
properly.

9-11. Imported Admin: Start with your work from Exercise 9-8 (page 178).
Store the classes User, Privileges, and Admin in one module. Create a separate
file, make an Admin instance, and call show_privileges() to show that
everything is working correctly.

9-12. Multiple Modules: Store the User class in one module, and store the
Privileges and Admin classes in a separate module. In a separate file, create
an Admin instance and call show_privileges() to show that everything is still
working correctly.
'''


# 10
# restaurant.py and my_restaurant.py

# 11
# user.py and my_user.py

# 12
# user.py and my_user.py and admin.py

'''
9-13. OrderedDict Rewrite: Start with Exercise 6-4 (page 108), where you
used a standard dictionary to represent a glossary. Rewrite the program using
the OrderedDict class and make sure the order of the output matches the order
in which key-value pairs were added to the dictionary.

9-14. Dice: The module random contains functions that generate random numbers
in a variety of ways. The function randint() returns an integer in the
range you provide. The following code returns a number between 1 and 6:

from random import randint
x = randint(1, 6)

	Make a class Die with one attribute called sides, which has a default
value of 6. Write a method called roll_die() that prints a random number
between 1 and the number of sides the die has. Make a 6-sided die and roll
it 10 times.
	Make a 10-sided die and a 20-sided die. Roll each die 10 times.

9-15. Python Module of the Week: One excellent resource for exploring the
Python standard library is a site called Python Module of the Week. Go to
http://pymotw.com/ and look at the table of contents. Find a module that
looks interesting to you and read about it, or explore the documentation of
the collections and random modules.
'''

# 13
from collections import OrderedDict

glossary = OrderedDict()

glossary['boolean'] = 'is a value that is either TRUE or FALSE'
glossary['conditional statement'] = 'is a set of rules performed if a certain condition is met'
glossary['else'] = 'is a programming conditional statement that if previous conditions are not true displays alternate information or performs alternate commands'

for word, definition in glossary.items():
	print(word.title() + ': ' + definition)

# 14
from random import randint

class Die():

	def __init__(self, sides = 6):
		self.sides = sides

	def roll_die(self):
		print(str(randint(1, self.sides)))

die_6 = Die()
die_6.roll_die()
die_6.roll_die()
die_6.roll_die()
die_6.roll_die()
die_6.roll_die()
print()
die_10 = Die(10)
die_10.roll_die()
die_10.roll_die()
die_10.roll_die()
die_10.roll_die()
die_10.roll_die()

# 15





