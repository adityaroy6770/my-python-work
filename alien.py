alien_0={'color':'red','points':5}
print(alien_0['color'])
print(alien_0['points'])
alien_0={'color':'red','points':5}
new_point=alien_0['points']
print('you earned'+' '+str(new_point)+' '+'points')
alien_0={'color':'red','points':5}
print(alien_0)
alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)
alien_0={}
alien_0['color']='red'
alien_0['points']=5
print(alien_0)
alien_0={'color':'green'}
print('alien color is'+' '+alien_0['color'])
alien_0['color']='yellow'
print('alien is now'+' '+alien_0['color'])
alien_0={'x_position':0,'y_position':25,'speed':'medium'}
print('original position'+' '+str(alien_0['x_position']))
#move the alien towards the right
#determine how fast to move the alien based on its current speed
if alien_0['speed']=='slow':
	x_increment=1
elif alien_0['speed']=='medium':
	x_increment=2
else :
	x_increment=3
alien_0['x_position']=alien_0['x_position']+x_increment
print('new x position'+' '+str(alien_0['x_position']))
alien_0={'color':'green','points':5}
print(alien_0)
del(alien_0['points'])
print(alien_0)
alien_0={'color':'green','points':5}
alien_1={'color':'yellow','points':10}
alien_2={'color':'red','points':0}
aliens=[alien_0,alien_1,alien_2]
for alien in aliens:
	print(alien)
#make an empty set for storing aliens
aliens=[]
#make 30 aliens
for alien_number in range(30):
	new_alien={'color':'green','point':5,'speed':'slow'}
	aliens.append(new_alien)
for alien in aliens[0:3]:
	if alien['color']=='green':
		alien['color']='yellow'
		alien['speed']='medium'
		alien['points']=15
		
#show first 5 alien
for alien in aliens[:5]:
	print(alien)
print('...')
print("total number og aliens"+str(len(aliens)))


