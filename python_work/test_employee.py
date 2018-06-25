import unittest
from employees import Employee

class TestEmployee(unittest.TestCase):
	"""docstring for TestEmployee"""

	def setUp(self):
		self.employee = Employee('jose', 'macias', 100000)

	def test_give_default_raise(self):
		self.employee.give_raise()
		self.assertEqual(self.employee.annual_salary, 105000)

	def test_give_custom_raise(self):
		self.employee.give_raise(400)
		self.assertEqual(self.employee.annual_salary, 100400)

unittest.main()