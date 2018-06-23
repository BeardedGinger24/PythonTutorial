
# Reading an Entire File
'''
with open('pi_digits.txt') as file_object:
	contents = file_object.read()
	#print(contents)
	print(contents.rstrip()) # use this get rid of empty strings added to the end
'''

# Reading Line by Line
'''
filename = 'pi_digits.txt'

with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip()) # use rstrip to get on the blank spaces
'''

# Making a List of Lines from a File

filename = 'pi_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line.rstrip())