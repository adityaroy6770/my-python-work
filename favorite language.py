favorite_languages={
'aditya':['python'],
'anand':['java','c','automation'],
'alok':['python'],
}
for name,languages in favorite_languages.items():
	print('\n'+name.title()+'favorite languages are')
	for language in languages:
		print('\t'+language.title())
