
# use a for loop to loop through the list
# indentation matters, the lines indented belong to the line above them
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician)
print("\n")
for magician in magicians:
	print(magician.title() + ", that was a great trick!")
	print("I can't wait to see your next trick, " + magician.title() + ".\n")

# you can use the range() function to print a series of numbers
for value in range(1,5):
	print(value)
print('\n')

# create a list of numbers using range
numbers = list(range(1,6))
print(numbers)

# can skip numbers as well
even_numbers = list(range(2,11,2))
print(even_numbers)

# we can allocate a list using a for loop
squares = []
for value in range(1,11):
	square = value**2
	squares.append(square)
print(squares)
print('\n')

# you can easily find the minimum, maximum, and sum of a list of numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))
print('\n')

# List Comprehensions:
# A list comprehension combines the
# for loop and the creation of new elements into one line, and automatically
# appends each new element
squares = [value**2 for value in range(1,11)]
print(squares)
print('\n')

# Slicing, working with a specific group of items in a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4]) # you can just specifiy your end result and python will start from the beginning
print(players[2:]) # or vice versa
print(players[-3:])
print('\n')

# looping through a list using slices
print("Here are the first three players on my team:")
for player in players[:3]:
	print(player.title())
print('\n')

# Copying a list, using slices
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

# doing this: friend_foods = my_foods, doesn't work. This just connects the new variable to the old one, 
# so any change in the old one shows in the new one

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)


# Tuples
# Lists change, but tuples do not change (aka immutable)
# Tuples use paratheses instead of brackets 
# Dimensions of a rectangle
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
print('\n')
# if you try to change one of the values, a type error is thrown

# Looping through all values of a tuple
for dimension in dimensions:
	print(dimension)
print('\n')

# you can overwrite the variables values for a tuple
dimensions = (400, 100)
print("Modified dimensions:")
for dimension in dimensions:
	print(dimension)




