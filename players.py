players=['aditya','anand','girish','bhanu','manoj']
print(players[0:4])
print(players[1:4])
print(players[:5])
print(players[3:])
print(players[-3:])
players=['aditya','abdul','anand','manoj']
print('here are the list of first three players of the team:')
for player in players[:3]:
	print(player.title())
