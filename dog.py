class dog():
	"""a simple attempt to model a dog"""
	def __init__(self,name,age):
		"""initialize name and age attribute"""
		self.name=name
		self.age=age
	def sit(self):
		"""simulate a dog sitting in response to the command"""
		print(self.name.title()+' '+"is now sitting")
	def roll_over(self):
		"""simulate rolling over in response to a command"""
		print(self.name.title()+' '+"rolled over")
my_dog=dog('willie',6)
your_dog=dog('lucy',3)
print('my dog is'+my_dog.name.title())
print("my dog is"+str(my_dog.age))
my_dog.sit()
my_dog.roll_over()
print("\nyour dogs name is"+' '+your_dog.name.title())
print("your dogs age is"+' '+str(your_dog.age))


