prompt='enter the name of the city you have visited'
prompt+='enter quit when you are done'
while True:
	city=input(prompt)
	if city =='quit':
		break
	else:
		print('i did love to go'+city.title())
