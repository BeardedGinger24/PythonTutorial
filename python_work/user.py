class User():
	def __init__(self, first_name, last_name, user_name):
		self.first_name = first_name
		self.last_name = last_name
		self.user_name = user_name
		self.full_name = first_name + ' ' + last_name
		self.login_attempts = 0

	def describe_user(self):
		print(self.full_name.title() + ' user name is: ' + self.user_name)

	def greet_user(self):
		print('Hello ' + self.full_name.title())

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0

'''
class Admin(User):

	def __init__(self, first_name, last_name, user_name):
		super().__init__(first_name, last_name, user_name)
		# self.privileges = ['can add post', 'can delete post', 'can ban user']
		self.privileges = Privileges()

class Privileges():

	def __init__(self):
		self.privileges = ['can add post', 'can delete post', 'can ban user']

	def show_privileges(self):
		print('Admins privileges: ')
		for privilege in self.privileges:
			print('\t' + privilege)
'''