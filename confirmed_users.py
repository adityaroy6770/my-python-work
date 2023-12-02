unconfirmed_users=['aditya','alok','anand']
confirmed_users=[]
while unconfirmed_users:
	current_users=unconfirmed_users.pop()
	print("verifying users:"+current_users.title())
	confirmed_users.append(current_users)
print("the following users have been confirmed")
for confirmed_user in confirmed_users:
		print(confirmed_user.title())
