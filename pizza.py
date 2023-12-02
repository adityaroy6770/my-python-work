def make_pizza(*toppings):
	"""print the list of toppings that have been requested"""
	"""summarize the pizza we are about to make"""
	print("making pizza with the following toppings")
	for topping in toppings:
		print(topping)
make_pizza('papperoni')
make_pizza('mushroom','green pepper','cheese')
def make_pizza(size,*toppings):
	"""summarize the pizza we are about to make"""
	print('\nmaking a '+str(size)+'inch pizza with the following toppings')
	for topping in toppings:
		print(topping)
make_pizza(16,'pepparoni')
make_pizza(12,'mushroom','cheese','corn')
