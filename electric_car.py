class Car():
	"""a simple attempt to present a car"""
	def __init__(self,make,model,year):
		self.make=make
		self.model=model
		self.year=year
		self.odometer_reading=0
	def get_descriptive_name(self):
		long_name=str(self.year)+' '+self.model+' '+self.make
		return long_name
	def read_odometer(self):
		print('this car has'+' '+str(self.odometer_reading)+' '+"miles on it")
	def update_odometer(self,mileage):
		if mileage>=self.odometer_reading():
			self.odometer_reading=mileage
		else:
			print("you cant roll back an odometer")
	def increment_odometer(self,miles):
		self.odometer_reading+=miles
class battery():
	"""a simple method to model a electric car"""
	def __init__(self,battery_size=70):
		"""initialize the battery attribute"""
		self.battery_size=battery_size
	def describe_battery(self):
		"""print a statement describing the battery size"""
		print("this car has a "+str(self.battery_size)+"kwh battery")
	def get_range(self):
		"""print a statement about the range this car provide"""
		if self.battery_size==70:
			range=240
		elif self.battery_size==85:
			range=270
		message=("this car can go"+' '+str(range)+' '+'miles on full charge')
		print(message)
class Electriccar(Car):
	"""represent aspect of car ,specific to electric car"""
	def __init__(self,make,model,year):
		"""initializeattribute of parent class"""
		"""initialize attribute of the parent class
		theninitialize attribute to electric class"""
		super().__init__(make,model,year)
		self.battery_size=70
		self.battery=battery()
	def describe_battery(self):
		"""print a statement describing battery size"""
		print("this car has a "+' '+str(self.battery_size)+"kwz battery")
		
my_tesla=Electriccar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
