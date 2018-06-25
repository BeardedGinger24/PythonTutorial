import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
	"""Tests for 'name_function.py'."""
	
	# adding test as the first word and then underscore lets python know to run it automatically
	def test_first_last_name(self): 
		"""Do names like 'Janis Joplin' work?"""
		formatted_name = get_formatted_name('janis', 'joplin')
		self.assertEqual(formatted_name, 'Janis Joplin')

	def test_first_last_middle_name(self):
		"""Do names like 'Wolfgang Amadeus Mozart' work?"""
		formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
		self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

unittest.main()

# Running test:
# The dot on the first line of output tells us that a single test passed.
# The next line tells us that Python ran one test, and it took less than 0.001 seconds
# to run.
# The final OK tells us that all unit tests in the test case passed.