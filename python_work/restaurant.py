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