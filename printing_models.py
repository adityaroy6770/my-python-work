unprinted_designs=['iphone case','robot pendent','dodecahedron']
completed_models=[]
while unprinted_designs:
	current_design=unprinted_designs.pop()
	print('printing model:'+current_design)
	completed_models.append(current_design)
print('the following models have been printed:')
for completed_model in completed_models:
	print(completed_model)
def print_models(unprinted_designs,completed_models):
	""" simulate printing each design, until none are left
	move each design to completed_model after printing"""
	while unprinted_designs:
		current_design=unprinted_designs.pop()
		print('printing model:'+current_design)
		completed_models.append(current_design)
def show_completed_models(completed_models):
	"""show all the models that were printed"""
	print('\nthe following models have been printed')
	for completed_model in completed_models:
		print(completed_model)
unprinted_designs=['iphone case','robot pendent','dodecahedron']
completed_models=[]
print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)
