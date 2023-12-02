message=input('tell me something and i will repeat after you')
print(message)
prompt='tell me something and i will repeat after you'
prompt+='\nenter quit to end programme'
message=''
while message!='quit':
	message=input(prompt)
	if message!='quit':
		print(message)
promt='tell me something and i will repeat after you'
prompt+='\nenter quit to end programme'
active=True
while active:
	message = input(prompt)
	if message=='quit':
		active=False
	else:
		print(message)
