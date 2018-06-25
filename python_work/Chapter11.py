
# Testing Your Code
# Testing a Function
# useing name_function.py and names.py

# Unit Tests and Test Cases
'''
The module unittest from the Python standard library provides tools for
testing your code. A unit test verifies that one specific aspect of a function’s
behavior is correct. A test case is a collection of unit tests that together prove
that a function behaves as it’s supposed to, within the full range of situations
you expect it to handle.
'''

# A Passing Test
# Here’s a test case with one method that verifies that the function
# get_formatted_name() works correctly when given a first and last name:
# using test_name_function.py

# A Failing Test
# second commented out function in name_function.py
# The first item in the output is a single E, which
# tells us one unit test in the test case resulted in an error.
# Next, we see that test_first_last_name() in NamesTestCase caused an error.
# At 3 we see a standard traceback, which reports that the function call
# get_formatted_name('janis', 'joplin') no longer works because it’s missing a
# required positional argument.

# Responding to a Failed Test
# updated function to handle middle names

# Adding New Tests
# adding middle name test to test name function file


# Testing a Class
# A Variety of Assert Methods

# Method 					Use
# ============================================================
# assertEqual(a, b) 		Verify that a == b
# assertNotEqual(a, b) 		Verify that a != b
# assertTrue(x) 			Verify that x is True
# assertFalse(x)			 Verify that x is False
# assertIn(item, list)		 Verify that item is in list
# assertNotIn(item, list)	 Verify that item is not in list


# A Class to Test
# using survey.py

# Testing the AnonymousSurvey Class
# using test_survey.py

# The setUp() Method
# using test_survey.py

