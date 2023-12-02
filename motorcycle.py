motorcycle=['honda','hero','bajaj','tvs']
print(motorcycle)
motorcycle[0]='ducati'
print(motorcycle)
motorcycle.append('suzuki')
print(motorcycle)
motorcycle.append('honda')
print(motorcycle)
motorcycle=[]
motorcycle.append('ducati')
motorcycle.append('ktm')
motorcycle.append('ninja')
print(motorcycle)
motorcycle=['hero','tvs','suzuki','honda']
motorcycle.insert(0,'ducati')
print(motorcycle)
motorcycle=['honda','ktm','hero','tvs']
del motorcycle[0]
print(motorcycle)
del motorcycle[1]
print(motorcycle)
motorcycle=['honda','ninja','harley','ducati']
print(motorcycle)
popped_motorcycle=motorcycle.pop()
print(motorcycle)
print(popped_motorcycle)
motorcycle=['honda','hero','suzuki','tvs']
last_bike=motorcycle.pop()
message='my last motorcycle was a'+' '+last_bike
print(message)
motorcycle=['tvs','honda','hero','yamaha']
last_bike=motorcycle.pop(0)
message='my last bike was'+' '+last_bike
print(message)
motorcycle=['hero','yamaha','suzuki','ninja']
print(motorcycle)
too_expensive='ninja'
motorcycle.remove(too_expensive)
print(too_expensive)
message='\na'+' '+too_expensive+' '+'is too expensive for me'
print(message)
