def greet_user(names):
	"""print a simple greeting to each user in the list"""
	for name in names:
		msg="hello"+name.title()
		print(msg)
usernames=['aditya','alok','anand']
greet_user(usernames)
