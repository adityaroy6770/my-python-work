def build_profile(first,last,**user_info):
	"""build a dictionary everything we know about a user"""
	profile={}
	profile['first_name']=first
	profile['last_name']=last
	for key,value in user_info.items():
		profile[key]=value
	return profile
user_profile=build_profile('albert','eienstein',location='germany',field='physics')
print(user_profile)
	
