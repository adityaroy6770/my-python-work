def get_formatted_name(first_name,last_name):
	"""return a full_name,formatted neatly"""
	full_name=first_name+' '+last_name
	return full_name.title()
musician=get_formatted_name('aditya','roy')
print(musician)
def get_formatted_name(first_name,middle_name,last_name):
	"""return full name,neatly formatted"""
	full_name=first_name+" "+middle_name+" "+last_name
	return full_name.title()
musician=get_formatted_name('john','lee','hooker')
print(musician)
def get_formatted_name(first_name,last_name,middle_name=' '):
	"""return a full name,formatted_neatly"""
	if middle_name:
		full_name=first_name+' '+middle_name+' '+last_name
	else:
		full_name=first_name+' '+last_name
	return full_name.title()
musician=get_formatted_name('aditya','roy')
print(musician)
musician=get_formatted_name('robert','dwanye','junior')
print(musician)
