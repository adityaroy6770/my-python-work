

file_name='pi_digits.txt'
with open(file_name)as file_object:
	lines=file_object.readlines()
pi_string=' '
for line in lines:
	pi_string+=line.strip()
print(pi_string[:52]+'.....')
print(len(pi_string))
birthday=input("enter your birthday in the form of ddmmyy")
if birthday in pi_string:
	print("your birthday appears in first million digits of pi number")
else:
	print("your birthday does not appear in first million digits of pi")

