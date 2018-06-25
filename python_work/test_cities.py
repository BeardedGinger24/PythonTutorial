import unittest
from city_functions import city_country

class CityTestCase(unittest.TestCase):
	# Tests for city_functions.py

	def test_city_country(self):
		formatted_name = city_country('glendale', 'california')
		self.assertEqual(formatted_name, 'Glendale, California')

	def test_city_country_population(self):
		formatted_name = city_country('santiago', 'chile', population = '5000000')
		self.assertEqual(formatted_name, 'Santiago, Chile - population 5000000')		

unittest.main()