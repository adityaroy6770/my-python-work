favorite_language={
'sarah':'python',
'arun':'java',
'dangi':'c',
'naveen':'script'
	}
print('sarah favorite language is'+' '+favorite_language['sarah'].title())
favorite_language={
'aditya':'python',
'anand':'java',
'alok':'c',
'shankar':'javascript'
	}
for name,language in favorite_language.items():
	print(name.title()+"'s favorite language is"+' '+language.title())
for name in favorite_language.keys():
	print(name.title())
friends=['shankar','aditya']
for name in favorite_language.keys():
	print(name.title())
	if name in friends:
		print('hi'+' '+name.title()+'i see your favorite language is'+favorite_language[name].title())
if 'manoj' not in favorite_language.keys():
	print("manoj plz take the poll")
for name in sorted(favorite_language.keys()):
	print(name.title()+' '+"thank you for taking poll")
print("the following languages have been mentioned")
for language in favorite_language.values():
	print(language)
for language in set(favorite_language.values()):
	print(language.title())

