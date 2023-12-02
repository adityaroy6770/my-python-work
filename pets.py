pets=['dog','cat','rabbit','hamster','cat','cat','dog','fish','cat','cat','fish']
print(pets)
while 'cat' in pets:
	pets.remove('cat')
print(pets)
def describe_pet(animal_type,pet_name):
	"""display information about pet"""
	print("\ni have a "+' '+animal_type)
	print("my"+' '+animal_type+' '+"name is "+' '+pet_name)
describe_pet('dog','bunny')
