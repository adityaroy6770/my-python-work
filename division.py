try:
	print(5/0)
except ZeroDivisionError:
	print('you cant divide by 0')
print('give me two number and i will divide')
print("enter 'q' to quit")
while True:
	first_number=input("\nfirst number")
	if first_number=='q':
		break
	second_number=input("\nsecond number")
	if second_number=='q':
		break
	try:
		
	    answer=int(first_number)/int(second_number)
	except ZeroDivisionError:
		print("you cant divide by zero")
	else:
		print(answer)
