
import json
file_name = 'favorite_number.json'

try:
	with open(file_name) as f_obj:
		number = json.load(f_obj)
except FileNotFoundError:
	favorite_number = input('What is your favorite number?\n')
	with open(file_name, 'w') as f_obj:
		json.dump(favorite_number, f_obj)
else:
	print('Your favorite number is: ' + number)