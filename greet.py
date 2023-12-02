def greet_user():
	"""display a simple greeting"""
	print("hello")
greet_user()
def greet_user(username):
	"""display a simple greeting"""
	print("hello"+' '+username.title())
greet_user('jesse')
def get_formatted_name(first_name,last_name):
	"""return a full name,nicely formatted"""
	full_name=first_name+' '+last_name
	return full_name.title()
while True:
	print('\nplease tell me your name')
	print(("please enter 'q' any time to quit"))
	f_name=input('first name:')
	if f_name=='q':
		break
	l_name=input('last_name:')
	if l_name=='q':
		break
	formatted_name=get_formatted_name(f_name,l_name)
	print('hello'+' '+formatted_name)
	
