requested_topping='mushroom'
if requested_topping!='archovies':
	print('hold on archovies')
requested_toppings=['mushroom','extra cheese']
if 'mushroom' in requested_toppings:
	print('adding mushroom')
if 'extra cheese' in requested_toppings:
	print('adding extra cheese')
if 'pepperoni' in requested_toppings:
	print('adding papperoni')
print('\nfinished making your pizza')
requested_toppings=['mushroom','extra cheese','pepper']
for requested_topping in requested_toppings:
	print('adding'+' '+requested_topping)
print('\nyour pizza is ready')
requested_toppings=['shimla','corn','tomato']
for requested_topping in requested_toppings:
	if requested_topping=='shimla':
		print('sorry we are running out of shimla')
	else:
		print("adding"+" "+requested_topping)
print("your pizza is ready")
requested_toppings=[]
if requested_toppings:
	for requested_topping in requested_toppings:
		print('adding'+' '+requested_topping)
		print('finished making your pizza')
else:
	print('are you sure you want a plain pizza')
available_toppings=['mushroom','corn','extra cheese','pepper','pineapple']
requested_toppings=['mushroom','corn','extra cheese','french fries']
for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print('adding'+' '+requested_topping)
	else:
		print('sorry we dont have the topping you requested for')
print('\nhere is your pizza')
pizza={
'crust':'thick',
'toppings':['mushroom','cheese','corn'],
}
print('you ordered a'+pizza['crust']+'crust pizza'+'with the following toppings')
for topping in pizza['toppings']:
	print('\t'+topping)




	

