
# Classes
# Creating and Using a Class

# Let’s start by writing a simple
# class, Dog, that represents a dog—not one dog in particular, but any dog.

# Each instance created from the Dog class will store a name and an age, and
# we’ll give each dog the ability to sit() and roll_over():

class Dog():
	"""A simple attempt to model a dog."""
	
	def __init__(self, name, age):
		"""Initialize name and age attributes."""
		self.name = name
		self.age = age

	def sit(self):
		"""Simulate a dog sitting in response to a command."""
		print(self.name.title() + " is now sitting.")

	def roll_over(self):
		"""Simulate rolling over in response to a command."""
		print(self.name.title() + " rolled over!")

# The __init__() Method
# A function that’s part of a class is a method.
'''
The __init__() method at line 14 is a special method
Python runs automatically whenever we create a new instance based on the
Dog class.

The self parameter is required in the method definition, and it
must come first before the other parameters

Whenever we want to make an instance from the Dog class,
we’ll provide values for only the last two parameters, name and age.

Variables that are accessible
through instances like this are called attributes.
'''


# Making an Instance from a Class
'''
Think of a class as a set of instructions for how to make an instance. The
class Dog is a set of instructions that tells Python how to make individual
instances representing specific dogs.
'''
my_dog = Dog('willie', 6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

# Accessing Attributes
# To access the attributes of an instance, you use dot notation:
# my_dog.name

# Calling Methods
my_dog.sit()
my_dog.roll_over()

# Creating Multiple Instances
your_dog = Dog('lucy', 3)

print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()


# Working with Classes and Instances
# You can modify the attributes of an
# instance directly or write methods that update attributes in specific ways.
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

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

# Setting a Default Value for an Attribute
# Every attribute in a class needs an initial value, even if that value is 0 or an empty string.
class Car():
	"""A simple attempt to represent a car."""
	
	def __init__(self, make, model, year):
		"""Initialize attributes to describe a car."""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0 # added this as a default

	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	def read_odometer(self):
		"""Print a statement showing the car's mileage."""
		print("This car has " + str(self.odometer_reading) + " miles on it.")

	def update_odometer(self, mileage):
		"""
		Set the odometer reading to the given value.
		Reject the change if it attempts to roll the odometer back.
		"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")

	def increment_odometer(self, miles):
		"""Add the given amount to the odometer reading."""
		self.odometer_reading += miles

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# Modifying Attribute Values
'''
You can change an attribute’s value in three ways: you can change the value
directly through an instance, set the value through a method, or increment
the value (add a certain amount to it) through a method.
'''

# Modifying an Attribute’s Value Directly
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# Modifying an Attribute’s Value Through a Method
'''
added this:

def update_odometer(self, mileage):
	"""Set the odometer reading to the given value."""
	self.odometer_reading = mileage
'''
my_new_car.update_odometer(26)
my_new_car.read_odometer()

'''
add this to prevent from reducing miles

Set the odometer reading to the given value.
Reject the change if it attempts to roll the odometer back.

if mileage >= self.odometer_reading:
	self.odometer_reading = mileage
else:
	print("You can't roll back an odometer!")
'''
my_new_car.update_odometer(22)
my_new_car.read_odometer()


# Incrementing an Attribute’s Value Through a Method
'''
def increment_odometer(self, miles):
	"""Add the given amount to the odometer reading."""
	self.odometer_reading += miles
'''
my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()


# Inheritance
'''
You don’t always have to start from scratch when writing a class. If the class
you’re writing is a specialized version of another class you wrote, you can
use inheritance. When one class inherits from another, it automatically takes
on all the attributes and methods of the first class. The original class is
called the parent class, and the new class is the child class. The child class
inherits every attribute and method from its parent class but is also free to
define new attributes and methods of its own.
'''

# The __init__() Method for a Child Class
'''
class Battery():
	"""A simple attempt to model a battery for an electric car."""
	def __init__(self, battery_size=70):
		"""Initialize the battery's attributes."""
		self.battery_size = battery_size

	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print("This car has a " + str(self.battery_size) + "-kWh battery.")


class ElectricCar(Car):
	"""Represent aspects of a car, specific to electric vehicles."""

	def __init__(self, make, model, year):
		"""
		Initialize attributes of the parent class.
		Then initialize attributes specific to an electric car.
		"""
		super().__init__(make, model, year)
		# self.battery_size = 70
		self.battery = Battery()
	
	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print("This car has a " + str(self.battery_size) + "-kWh battery.")
	
	
	def fill_gas_tank(self):
		"""Electric cars don't have gas tanks."""
		print("This car doesn't need a gas tank!")
'''

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

class ElectricCar(Car):
	"""Represent aspects of a car, specific to electric vehicles."""

	def __init__(self, make, model, year):
		"""
		Initialize attributes of the parent class.
		Then initialize attributes specific to an electric car.
		"""
		super().__init__(make, model, year)
		self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())

# Defining Attributes and Methods for the Child Class
# my_tesla.describe_battery()

# Overriding Methods from the Parent Class
'''
You can override any method from the parent class that doesn’t fit what
you’re trying to model with the child class. To do this, you define a method
in the child class with the same name as the method you want to override
in the parent class. Python will disregard the parent class method and only
pay attention to the method you define in the child class.
'''
# my_tesla.fill_gas_tank()

# Instances as Attributes
'''
When modeling something from the real world in code, you may find that
you’re adding more and more detail to a class. You’ll find that you have a
growing list of attributes and methods and that your files are becoming
lengthy. In these situations, you might recognize that part of one class can
be written as a separate class. You can break your large class into smaller
classes that work together.
'''
# self.battery = Battery() added to electric car
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()



# Modeling Real-World Objects
'''
As you begin to model more complicated items like electric cars, you’ll
wrestle with interesting questions. Is the range of an electric car a property
of the battery or of the car? If we’re only describing one car, it’s probably
fine to maintain the association of the method get_range() with the Battery
class. But if we’re describing a manufacturer’s entire line of cars, we probably
want to move get_range() to the ElectricCar class. The get_range() method
would still check the battery size before determining the range, but it would
report a range specific to the kind of car it’s associated with. Alternatively,
we could maintain the association of the get_range() method with the battery
but pass it a parameter such as car_model. The get_range() method would
then report a range based on the battery size and car model.
This brings you to an interesting point in your growth as
'''


# Importing Classes
#Importing a Single Class
# working with car.py and my_car.py

# Storing Multiple Classes in a Module
# working with my_electric_car.py

# Importing Multiple Classes from a Module


# The Python Standard Library
'''
The Python standard library is a set of modules included with every Python
installation. Now that you have a basic understanding of how classes work,
you can start to use modules like these that other programmers have written.
You can use any function or class in the standard library by including
a simple import statement at the top of your file. Let’s look at one class,
OrderedDict, from the module collections.


Dictionaries allow you to connect pieces of information, but they don’t
keep track of the order in which you add key-value pairs. If you’re creating
a dictionary and want to keep track of the order in which key-value pairs
are added, you can use the OrderedDict class from the collections module.
Instances of the OrderedDict class behave almost exactly like dictionaries
except they keep track of the order in which key-value pairs are added.
'''

from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'
for name, language in favorite_languages.items():
	print(name.title() + "'s favorite language is " +
		language.title() + ".")






