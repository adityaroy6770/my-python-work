users={
'aienstein':{
'first':'albert',
'last':'eienstein',
'location':'princeton',
},
'mcurie':{
'first':'marie',
'last':'curie',
'location':'paris',
},
}
for user,user_info in users.items():
	print('\nusername'+user)
	full_name=user_info['first']+" "+user_info['last']
	location=user_info['location']
	print('\tfull name:'+full_name.title())
	print('\tlocation:'+location.title())
