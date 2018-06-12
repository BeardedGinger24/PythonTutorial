
# square brackets, [], indicate a list and individual elements in the list are seperated by commas
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# access a specific element in a list
print(bicycles[0])
# we can even use the string functions
print(bicycles[0].title())

# python uses the index -1 to access the last item in the list (it's a special case)
# helpful if you want to access the last item without knowing the length of the list
# and this extends to the values -2 (second from last) and -3, etc
print(bicycles[-1])

# we can use an individual value from the list to create a message like before
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)


# Modifying elements in a lists
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# to add new data to a list use append
motorcycles.append('ducati')
print(motorcycles)

# Insert elements into a list given a specific position
motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.insert(0, 'ducati')
print(motorcycles)	# gives: ['ducati', 'honda', 'yamaha', 'suzuki']

# Removing/Deleting elements given position/index
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del(motorcycles[0]) 
print(motorcycles)

# remove an element and store the value, use pop()
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# you can use position to pop as well
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

# if you dont know the position of the element, then remove by value (only removes first occurance)
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

# you can also use the value that you are removing using the remove function
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")


# Permantitly organizing a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# Or sort it backwards
cars.sort(reverse=True)
print(cars)

# temporarly sort a list
print("\nHere is the sorted list:")
print(sorted(cars))

# Reverse order, without sorting
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)

#or, temporarly reverse
print(sorted(cars,reverse=True))

# Finding the length of the list
# >>> cars = ['bmw', 'audi', 'toyota', 'subaru']
# >>> len(cars)
# 4



