'''
6-1. Person: Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. You
should have keys such as first_name, last_name, age, and city. Print each
piece of information stored in your dictionary.

6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
Think of five names, and use them as keys in your dictionary. Think of a favorite
number for each person, and store each as a value in your dictionary. Print
each person’s name and their favorite number. For even more fun, poll a few
friends and get some actual data for your program.

6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
However, to avoid confusion, let’s call it a glossary.
• Think of five programming words you’ve learned about in the previous
chapters. Use these words as the keys in your glossary, and store their
meanings as values.
• Print each word and its meaning as neatly formatted output. You might
print the word followed by a colon and then its meaning, or print the word
on one line and then print its meaning indented on a second line. Use the
newline character (\n) to insert a blank line between each word-meaning
pair in your output.
'''

# 1
person_1 = {
	'first_name':'daniel',
	'last_name':'kale',
	'age':'22',
	'city':'arcadia',
	}
print(person_1['first_name'])
print(person_1['last_name'])
print(person_1['age'])
print(person_1['city'])
print('\n')

# 2
favorite_numbers = {
	'daniel':'1',
	'robert':'23',
	'emanoel':'3',
	'jose':'0',
	'richard':'50',
	}

num = favorite_numbers['daniel']
print("Daniel's favorite number is " + str(num) + ".")

num = favorite_numbers['robert']
print("Robert's favorite number is " + str(num) + ".")

num = favorite_numbers['emanoel']
print("Emanoel's favorite number is " + str(num) + ".")

num = favorite_numbers['jose']
print("Jose's favorite number is " + str(num) + ".")

num = favorite_numbers['richard']
print("Richard's favorite number is " + str(num) + ".")
print('\n')

# 3
glossary = {
	'boolean':'is a value that is either TRUE or FALSE',
	'conditional statement':'is a set of rules performed if a certain condition is met',
	'else':'is a programming conditional statement that if previous conditions are not true displays alternate'
	+ ' information or performs alternate commands',
	}

definition = glossary['boolean']
print("Boolean: " + definition)

definition = glossary['conditional statement']
print("Conditional Statement: " + definition)

definition = glossary['else']
print("Else: " + definition)
print('\n')

'''
6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
up the code from Exercise 6-3 (page 102) by replacing your series of print
statements with a loop that runs through the dictionary’s keys and values.
When you’re sure that your loop works, add five more Python terms to your
glossary. When you run your program again, these new words and meanings
should automatically be included in the output.

6-5. Rivers: Make a dictionary containing three major rivers and the country
each river runs through. One key-value pair might be 'nile': 'egypt'.
• Use a loop to print a sentence about each river, such as The Nile runs
through Egypt.
• Use a loop to print the name of each river included in the dictionary.
• Use a loop to print the name of each country included in the dictionary.

6-6. Polling: Use the code in favorite_languages.py (page 104).
• Make a list of people who should take the favorite languages poll. Include
some names that are already in the dictionary and some that are not.
• Loop through the list of people who should take the poll. If they have
already taken the poll, print a message thanking them for responding.
If they have not yet taken the poll, print a message inviting them to take
the poll.
'''

# 4
for word, definition in glossary.items():
	print(word.title() + ': ' + definition)

# 5
rivers = {
	'niles':'egypt',
	'mississippi':'united states',
	'zambezi':'zambia',
	}

for river, country in rivers.items():
	print(river.title() + ' runs through ' + country.title() + '.')
print('\n')

print('Rivers:')
for river in rivers.keys():
	print(river.title())
print('\n')

print('Countries:')
for country in rivers.values():
	print(country.title())
print('\n')

# 6
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

names = ['jose', 'daniel', 'jen', 'richard', 'sarah']
for name in names:
	if name in favorite_languages.keys():
		print('Thank you ' + name.title() + ' for taking the poll.')
	else:
		print(name.title() + ', please take the poll.')
print('\n')

'''
6-7. People: Start with the program you wrote for Exercise 6-1 (page 102).
Make two new dictionaries representing different people, and store all three
dictionaries in a list called people. Loop through your list of people. As you
loop through the list, print everything you know about each person.
'''

# 7
person_1 = {
	'first_name':'daniel',
	'last_name':'kale',
	'age':'22',
	'city':'arcadia',
	}
person_2 = {
	'first_name':'steven',
	'last_name':'hills',
	'age':'21',
	'city':'culver city',
	}
person_3 = {
	'first_name':'michael',
	'last_name':'davis',
	'age':'26',
	'city':'glendale',
	}

people = [person_1, person_2, person_3]

for person in people:
	full_name = person['first_name'].title() + ' ' + person['last_name'].title()
	age = person['age']
	city = person['city'].title()

	print(full_name + ' is ' + age + ' years old and lives in ' + city + '.')

print('\n')

'''
6-8. Pets: Make several dictionaries, where the name of each dictionary is the
name of a pet. In each dictionary, include the kind of animal and the owner’s
name. Store these dictionaries in a list called pets. Next, loop through your list
and as you do print everything you know about each pet.

6-9. Favorite Places: Make a dictionary called favorite_places. Think of three
names to use as keys in the dictionary, and store one to three favorite places
for each person. To make this exercise a bit more interesting, ask some friends
to name a few of their favorite places. Loop through the dictionary, and print
each person’s name and their favorite places.

6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so
each person can have more than one favorite number. Then print each person’s
name along with their favorite numbers.

6-11. Cities: Make a dictionary called cities. Use the names of three cities as
keys in your dictionary. Create a dictionary of information about each city and
include the country that the city is in, its approximate population, and one fact
about that city. The keys for each city’s dictionary should be something like
country, population, and fact. Print the name of each city and all of the information
you have stored about it.

6-12. Extensions: We’re now working with examples that are complex enough
that they can be extended in any number of ways. Use one of the example programs
from this chapter, and extend it by adding new keys and values, changing
the context of the program or improving the formatting of the output.
'''

# 8
pets = []
pet = {
	'name':'cupid',
	'type':'dog',
	'owner_first_name':'summer',
	'owner_last_name':'zavala',
	}
pets.append(pet)
pet = {
	'name':'zeus',
	'type':'dog',
	'owner_first_name':'roman',
	'owner_last_name':'atwood',
	}
pets.append(pet)
pet = {
	'name':'tux',
	'type':'cat',
	'owner_first_name':'brittney',
	'owner_last_name':'atwood',
	}
pets.append(pet)
for pet in pets:
	name = pet['name']
	owner = pet['owner_first_name'] + ' ' + pet['owner_last_name']
	animal = pet['type']
	print(name.title() + ' is a ' + animal + ' and its owner is ' + owner.title() + '.')
print('\n')

# 9
favorite_places = {
	'jose':['columbia','united states'],
	'daniel':['italy','argentina','armenia'],
	'justin':['france'],
	}

for name, places in favorite_places.items():
	print(name.title() + "'s favorite places are:")
	for place in places:
		print('\t'+place.title())
print('\n')

# 10
favorite_numbers = {
	'daniel':[1,3],
	'robert':[23,63],
	'emanoel':[50,30],
	'jose':[0,50,40],
	'richard':[90,81],
	}
for name, numbers in favorite_numbers.items():
	print(name.title() + "'s favorite numbers are:")
	for number in numbers:
		print('\t' + str(number))
print('\n')

# 11
cities = {
	'glendale':{
		'country':'united states',
		'population':197000,
		'fact':'we have ponchiks'
		},
	'london':{
		'country':'united kingdom',
		'population':81000000,
		'fact':'capital of england'
		},
	'paris':{
		'country':'france',
		'population':2200000,
		'fact':'have a great soccer team'
		},
	}

for city, city_info in cities.items():
	print("City: " + city.title())
	for category, info in city_info.items():
		print('\t' + category.title() + ': ' + str(info))
		