from user import User

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