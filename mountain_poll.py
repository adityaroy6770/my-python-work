responses={}
polling_active=True
while polling_active:
	name=input("\nwhat is your name?")
	response=input("which mountain would you like to climb one day?")
	responses[name]=response
	repeat=input("would you like another person to respond?(yes/no)")
	if repeat=='no':
		polling_active=False
print("\n--pole results--")
for name,response in responses.items():
	print(name + "would like to visit" + response)
