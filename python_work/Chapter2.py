
print("Hello Python World!")

message = "Hello World!"
print(message)

message = "Hello Python Crash Course World!"
print(message)


name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

#concatenation
first_name = "Ada"
last_name = "Lovelace"
full_name = first_name + " " + last_name
print(full_name)

print("Hello, " + full_name.title() + "!")

#tabs
print("\tPython")
#new line
print("\nThis\nis\na\nnew\nline")

#stripping whitespace
	#strip white space on right end
favorite_language = "python "
favorite_language.rstrip()

	# ** this is only removed temporarily
	# need to write over old variable

	favorite_language = favorite_language.rstrip()

	# left strip
	favorite_language = " python"
	favorite_language.rstrip()

	# strip both sides
	favorite_language = " python "
	favorite_language.strip()




# Integers
'''
>>> 2 + 3
5
>>> 3 - 2
1
>>> 2 * 3
6
>>> 3 / 2
1.5

In terminal session, exponents are allowed by:
>>> 3 ** 2
9
>>> 3 ** 3
27
>>> 10 ** 6
1000000

'''

#Floats
'''
In python, any number with a decimal is a float.

>>> 0.1 + 0.1
0.2
>>> 0.2 + 0.2
0.4
>>> 2 * 0.1
0.2
>>> 2 * 0.2
0.4

But at times we can get an arbitrary number of decimal places in our answers:

>>> 0.2 + 0.1
0.30000000000000004
>>> 3 * 0.1
0.30000000000000004
'''


# we might want to add a number into a string, but it will throw errors (giving a type error):
age = 23
message = "Happy " + age + "rd Birthday!"
print(message)

# instead convert the number value to a stirng:
age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)



# use double quotes for outside if using single quote inside
message = "One of Python's strengths is its diverse community."
print(message)

# this one caauses an error
message = 'One of Python's strengths is its diverse community.'

# use the pound symbol for a single line comment

# Say hello to everyone.
print("Hello Python people!")

# The main reason to write comments is to explain what your code is supposed
# to do and how you are making it work.

'''
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

'''