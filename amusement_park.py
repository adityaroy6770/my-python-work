age=17
if age<4:
	print('your entry fee is rs0')
elif age<18:
	print('your entry fee is rs10')
else:
	print('your entry fee is rs20')
age=21
if age<=4:
	price=0
elif age<=18:
	price=10
else:
	price=20
print('your entry fee is'+' '+str(price))
age=65
if age<=4:
	price=0
elif age<=18:
	price=10
elif age<=65:
	price=20
else:
	price=5
print('your entry fee is'+' '+str(price))

